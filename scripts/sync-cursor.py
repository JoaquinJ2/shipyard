#!/usr/bin/env python3
"""Materialize shipyard kernel + packs into a consuming repo's .cursor/."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

MANIFEST_REL = Path(".cursor/shipyard-managed.json")
OVERLAY_REL = Path("docs/agents/shipyard.md")
SKILL_ROUTING_REL = Path("docs/agents/skill-routing.md")
SUBMODULE_PATH = Path(".cursor/plugins/shipyard")

PACK_FOLDER = {
    "visual": "visual",
    "react": "react",
    "vite": "vite",
    "typescript": "typescript",
    "database": "postgres",
    "security": "security",
}

BOOLEAN_PACK_KEYS = tuple(PACK_FOLDER.keys())
PACK_LINE = re.compile(r"^([A-Za-z0-9_-]+):\s*(\S+)\s*$")


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def is_plugin_root(path: Path) -> bool:
    return (
        (path / ".cursor-plugin" / "plugin.json").is_file()
        and (path / "packs").is_dir()
        and (path / "skills" / "setup-shipyard" / "SKILL.md").is_file()
    )


def run_git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def git_head(path: Path) -> str | None:
    proc = run_git(path, "rev-parse", "HEAD")
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def plugin_version(plugin: Path) -> str:
    raw = (plugin / ".cursor-plugin" / "plugin.json").read_text(encoding="utf-8")
    data = json.loads(raw)
    version = data.get("version")
    return str(version) if version else "unknown"


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Copy shipyard kernel and overlay packs into a consuming repo."
    )
    p.add_argument("--target", help="Consuming repo root (default: cwd)")
    p.add_argument("--plugin", help="Shipyard plugin root (default: detect)")
    p.add_argument(
        "--pull",
        action="store_true",
        help="Update the submodule in the target, or git-pull a loose --plugin clone",
    )
    p.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    p.add_argument(
        "--keep-local",
        action="store_true",
        help="Do not overwrite pack files that differ from the plugin",
    )
    p.add_argument(
        "--no-kernel",
        action="store_true",
        help="Skip commands/agents/routing/plugin skills (packs only)",
    )
    p.add_argument(
        "--no-packs",
        action="store_true",
        help="Skip overlay packs (kernel only)",
    )
    p.add_argument(
        "--no-skill-routing",
        action="store_true",
        help="Do not refresh docs/agents/skill-routing.md from the template",
    )
    return p.parse_args(argv)


def resolve_target(raw: str | None) -> Path:
    target = Path(raw or os.getcwd()).expanduser().resolve()
    if not target.is_dir():
        die(f"target is not a directory: {target}")
    return target


def submodule_recorded(target: Path) -> bool:
    gitmodules = target / ".gitmodules"
    if not gitmodules.is_file():
        return False
    text = gitmodules.read_text(encoding="utf-8")
    return "path = .cursor/plugins/shipyard" in text or "path = .cursor/plugins/shipyard\n" in text


def pull_plugin(target: Path, plugin_override: Path | None) -> None:
    if submodule_recorded(target):
        print(f"pull: git submodule update --init --remote --recursive -- {SUBMODULE_PATH}")
        proc = run_git(
            target,
            "submodule",
            "update",
            "--init",
            "--remote",
            "--recursive",
            "--",
            str(SUBMODULE_PATH),
        )
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout or "").strip()
            die(f"submodule update failed: {detail}")
        return

    loose = plugin_override
    if loose is None:
        die(
            " --pull needs a shipyard submodule at .cursor/plugins/shipyard "
            "or an explicit --plugin clone"
        )
    if not (loose / ".git").exists() and run_git(loose, "rev-parse", "--is-inside-work-tree").returncode != 0:
        die(f"--plugin is not a git work tree: {loose}")
    print(f"pull: git -C {loose} pull --ff-only")
    proc = run_git(loose, "pull", "--ff-only")
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        die(f"git pull --ff-only failed: {detail}")


def resolve_plugin(target: Path, override: str | None, script_root: Path) -> Path:
    if override:
        path = Path(override).expanduser().resolve()
        if not is_plugin_root(path):
            die(f"--plugin is not a shipyard root: {path}")
        return path

    candidates = [
        target / SUBMODULE_PATH,
        script_root,
        Path.home() / ".cursor/plugins/local/shipyard",
    ]
    for cand in candidates:
        if is_plugin_root(cand):
            return cand
    die(
        "could not find shipyard plugin root. Add the submodule "
        "(.cursor/plugins/shipyard) or pass --plugin."
    )
    raise AssertionError("unreachable")


def parse_overlay_packs(overlay: Path) -> dict[str, bool]:
    enabled = {key: False for key in BOOLEAN_PACK_KEYS}
    if not overlay.is_file():
        return enabled
    text = overlay.read_text(encoding="utf-8")
    marker = re.search(r"^## Packs\s*$", text, re.MULTILINE)
    if not marker:
        return enabled
    rest = text[marker.end() :]
    fence = re.search(r"```[^\n]*\n(.*?)```", rest, re.DOTALL)
    if not fence:
        return enabled
    for line in fence.group(1).splitlines():
        m = PACK_LINE.match(line.strip())
        if not m:
            continue
        key, value = m.group(1), m.group(2).lower()
        if key in enabled:
            enabled[key] = value in {"on", "true", "yes"}
    return enabled


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    if not root.exists():
        return files
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name in {".DS_Store"}:
            continue
        files.append(path)
    return files


def collect_kernel(plugin: Path) -> list[tuple[Path, Path, str]]:
    ops: list[tuple[Path, Path, str]] = []
    for src in sorted((plugin / "commands").glob("*.md")):
        ops.append((src, Path(".cursor/commands") / src.name, "kernel"))
    for src in sorted((plugin / "agents").glob("*.md")):
        ops.append((src, Path(".cursor/agents") / src.name, "kernel"))
    routing = plugin / "rules" / "agent-routing.mdc"
    if routing.is_file():
        ops.append((routing, Path(".cursor/rules/agent-routing.mdc"), "kernel"))
    for skill_dir in sorted((plugin / "skills").iterdir()):
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
            continue
        for src in iter_files(skill_dir):
            rel = src.relative_to(plugin / "skills")
            ops.append((src, Path(".cursor/skills") / rel, "kernel"))
    return ops


def skip_security_rule(name: str, packs: dict[str, bool]) -> bool:
    if name == "typescript-security.mdc" and not packs.get("typescript"):
        return True
    if name == "react-security.mdc" and not packs.get("react"):
        return True
    return False


def collect_packs(plugin: Path, packs: dict[str, bool]) -> list[tuple[Path, Path, str]]:
    ops: list[tuple[Path, Path, str]] = []
    for key, folder in PACK_FOLDER.items():
        if not packs.get(key):
            continue
        pack_root = plugin / "packs" / folder
        skills = pack_root / "skills"
        rules = pack_root / "rules"
        if skills.is_dir():
            for src in iter_files(skills):
                rel = src.relative_to(skills)
                ops.append((src, Path(".cursor/skills") / rel, "pack"))
        if rules.is_dir():
            for src in sorted(rules.glob("*.mdc")):
                if skip_security_rule(src.name, packs):
                    continue
                ops.append((src, Path(".cursor/rules") / src.name, "pack"))
    return ops


def collect_generated(plugin: Path, target: Path, refresh_skill_routing: bool) -> list[tuple[Path, Path, str]]:
    ops: list[tuple[Path, Path, str]] = []
    if refresh_skill_routing:
        src = plugin / "templates" / "docs" / "agents" / "skill-routing.md"
        if src.is_file() and (target / OVERLAY_REL).is_file():
            ops.append((src, SKILL_ROUTING_REL, "generated"))
    return ops


def load_manifest(target: Path) -> dict:
    path = target / MANIFEST_REL
    if not path.is_file():
        return {"pluginVersion": None, "pluginCommit": None, "files": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"pluginVersion": None, "pluginCommit": None, "files": []}
    files = data.get("files") or []
    if not isinstance(files, list):
        files = []
    return {
        "pluginVersion": data.get("pluginVersion"),
        "pluginCommit": data.get("pluginCommit"),
        "files": [str(f) for f in files],
    }


def write_if_needed(dest: Path, data: bytes, dry_run: bool) -> str:
    exists = dest.is_file()
    if exists and dest.read_bytes() == data:
        return "unchanged"
    action = "updated" if exists else "created"
    if dry_run:
        return action
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return action


def remove_file(dest: Path, dry_run: bool) -> str:
    if not dry_run:
        dest.unlink()
        prune_empty_parents(dest.parent)
    return "removed"


def prune_empty_parents(start: Path) -> None:
    current = start
    for _ in range(8):
        if current.name in {".cursor", "docs", ""}:
            break
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def print_row(action: str, rel: Path, dry_run: bool) -> None:
    label = {
        "created": "would create" if dry_run else "created",
        "updated": "would update" if dry_run else "updated",
        "removed": "would remove" if dry_run else "removed",
        "skipped": "skipped",
        "unchanged": "unchanged",
    }.get(action, action)
    print(f"{label:14} {rel.as_posix()}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    script_root = Path(__file__).resolve().parent.parent
    target = resolve_target(args.target)
    plugin_override = Path(args.plugin).expanduser().resolve() if args.plugin else None
    if plugin_override is not None and not is_plugin_root(plugin_override):
        die(f"--plugin is not a shipyard root: {plugin_override}")

    if args.pull:
        pull_plugin(target, plugin_override)

    plugin = resolve_plugin(
        target,
        str(plugin_override) if plugin_override else None,
        script_root,
    )
    if plugin == target:
        die("target is the shipyard repo itself; pass --target to the consuming repo")

    overlay = target / OVERLAY_REL
    packs = parse_overlay_packs(overlay)
    if not overlay.is_file():
        print("warn: docs/agents/shipyard.md missing; skipping packs (run /setup-shipyard)")
        packs = {key: False for key in BOOLEAN_PACK_KEYS}

    ops: list[tuple[Path, Path, str]] = []
    if not args.no_kernel:
        ops.extend(collect_kernel(plugin))
    if not args.no_packs:
        ops.extend(collect_packs(plugin, packs))
    ops.extend(collect_generated(plugin, target, not args.no_skill_routing))

    # Stable unique dests (last source wins; should not overlap)
    by_dest: dict[Path, tuple[Path, str]] = {}
    for src, dest_rel, kind in ops:
        by_dest[dest_rel] = (src, kind)

    old_manifest = load_manifest(target)
    old_files = set(old_manifest["files"])
    new_files = sorted(dest.as_posix() for dest in by_dest)

    counts = {
        "created": 0,
        "updated": 0,
        "unchanged": 0,
        "skipped": 0,
        "removed": 0,
    }

    print(f"plugin: {plugin}")
    print(f"target: {target}")
    enabled = [k for k, v in packs.items() if v]
    print(f"packs:  {', '.join(enabled) if enabled else '(none)'}")
    if args.dry_run:
        print("mode:   dry-run")
    if args.keep_local:
        print("mode:   keep-local")

    for dest_rel, (src, kind) in sorted(by_dest.items(), key=lambda item: item[0].as_posix()):
        dest = target / dest_rel
        data = src.read_bytes()
        if (
            args.keep_local
            and kind == "pack"
            and dest.is_file()
            and dest.read_bytes() != data
        ):
            print_row("skipped", dest_rel, args.dry_run)
            counts["skipped"] += 1
            continue
        action = write_if_needed(dest, data, args.dry_run)
        counts[action] = counts.get(action, 0) + 1
        if action != "unchanged":
            print_row(action, dest_rel, args.dry_run)

    kept_stale: list[str] = []
    stale = sorted(old_files - set(new_files))
    for rel in stale:
        dest = target / rel
        if not dest.is_file():
            continue
        if args.keep_local:
            # Pack turned off or kernel file removed: keep a locally edited copy.
            print_row("skipped", Path(rel), args.dry_run)
            counts["skipped"] += 1
            kept_stale.append(rel)
            continue
        action = remove_file(dest, args.dry_run)
        counts["removed"] += 1
        print_row(action, Path(rel), args.dry_run)

    manifest = {
        "pluginVersion": plugin_version(plugin),
        "pluginCommit": git_head(plugin),
        "files": sorted(set(new_files) | set(kept_stale)),
    }
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
    action = write_if_needed(target / MANIFEST_REL, manifest_bytes, args.dry_run)
    if action != "unchanged":
        print_row(action, MANIFEST_REL, args.dry_run)
        counts[action] = counts.get(action, 0) + 1
    else:
        counts["unchanged"] += 1

    print(
        "summary: "
        + ", ".join(f"{name}={counts.get(name, 0)}" for name in ("created", "updated", "unchanged", "skipped", "removed"))
    )
    if not args.dry_run:
        print("Reload the Cursor window to pick up commands and agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
