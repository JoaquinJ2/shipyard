---
description: Pull shipyard updates and re-materialize kernel + packs into .cursor/
---

# /update-shipyard

Non-interactive. Refresh this repo from the shipyard plugin. Do **not** run the `/setup-shipyard` interview. Do **not** rewrite `docs/agents/shipyard.md`.

## Plugin root

Resolve the same way as setup-shipyard:

1. `.cursor/plugins/shipyard` in this workspace (git submodule — **preferred**)
2. Two levels up from `skills/setup-shipyard/SKILL.md` when that skill is loaded from an installed plugin
3. `~/.cursor/plugins/local/shipyard` (global dev fallback only)

The script lives at `scripts/sync-cursor.sh` in that root.

## Steps

1. If this repo records the submodule at `.cursor/plugins/shipyard`, run:

```bash
.cursor/plugins/shipyard/scripts/sync-cursor.sh --pull
```

`--pull` runs `git submodule update --init --remote --recursive -- .cursor/plugins/shipyard`, then copies.

2. If you are developing from a sibling shipyard clone (no submodule checkout, or unpushed local plugin changes), run:

```bash
/path/to/shipyard/scripts/sync-cursor.sh --target "$(pwd)" --plugin /path/to/shipyard
```

Do **not** pass `--pull` on a sibling clone unless the user asked to `git pull` that clone.

3. Optional flags the user may request:
   - `--dry-run` — print actions, write nothing
   - `--keep-local` — do not overwrite pack files that differ from the plugin
   - `--no-kernel` — packs only (when Cursor loads project plugins again)

4. Report the script summary (`created` / `updated` / `unchanged` / `skipped` / `removed`). List notable paths.

5. Tell the user to **Developer: Reload Window** so `.cursor/commands` and `.cursor/agents` show up in the `/` menu.

## Do not

- Edit `docs/agents/shipyard.md` (overlay is per-repo).
- Touch livingdocs skills, feature-spark, or anything not listed in `.cursor/shipyard-managed.json`.
- Copy files by hand. The script owns the projection.
