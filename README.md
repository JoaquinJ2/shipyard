# Shipyard

Cursor plugin: plan a PRD, ship tickets with **writer ≠ reviewer**, then record behaviour.

Kernel (commands, agents, routing) lives in this repo. Per-repo overlay is created by `/setup-shipyard`. Because Cursor does not reliably load project-scope plugins yet, `scripts/sync-cursor.sh` **materializes** kernel + enabled packs into the consuming repo's `.cursor/` (committed projection). Refresh with `/update-shipyard`.

## Install from Cursor (local repo)

Customize → Add → Plugin from local repo. Point at this repository root. Cursor indexes `.cursor-plugin/marketplace.json` (not `plugin.json` alone). Then enable **shipyard** at **User** scope and Reload Window.

Do **not** pick Project in that dialog. Cursor currently crashes project-scope marketplace installs with `Failed to install Shipyard, please try again or reload the window.` ([tracked](https://forum.cursor.com/t/project-scope-marketplace-plugin-install-fails-with-workspace-collection-is-not-available-3-13-25-remote-wsl/167083)). Per-repo install is the submodule + sync flow below, not that toggle.

## Prerequisites (in the target repo)

1. Matt `/setup-matt-pocock-skills`
2. `/livingdocs-install`

## Install in a repo (recommended)

Keep the plugin in the product repo (not a global Cursor install):

```bash
git submodule add https://github.com/JoaquinJ2/shipyard.git .cursor/plugins/shipyard
git submodule update --init --recursive .cursor/plugins/shipyard
```

If the submodule is already recorded but the folder is empty or deleted:

```bash
git submodule update --init --recursive .cursor/plugins/shipyard
```

Add to `.cursor/hooks.json` (merge with existing hooks):

```json
"workspaceOpen": [{ "command": ".cursor/hooks/shipyard-workspace-open.sh" }]
```

Copy the hook script from `templates/hooks/shipyard-workspace-open.sh` in this repo to `.cursor/hooks/shipyard-workspace-open.sh` and `chmod +x` it.

Then run `/setup-shipyard` in the target repo. That writes `docs/agents/shipyard.md` and runs `scripts/sync-cursor.sh`, which copies:

- `commands/` → `.cursor/commands/`
- `agents/` → `.cursor/agents/`
- `rules/agent-routing.mdc` → `.cursor/rules/`
- plugin `skills/` → `.cursor/skills/`
- enabled `packs/` → `.cursor/skills/` and `.cursor/rules/`

Commit those files. Reload the Cursor window.

After clone: `git submodule update --init --recursive .cursor/plugins/shipyard`

## Update an installed repo

Pull plugin changes, then re-copy:

```bash
git submodule update --init --remote --recursive .cursor/plugins/shipyard
.cursor/plugins/shipyard/scripts/sync-cursor.sh
```

Or run `/update-shipyard` (same thing). Commit the updated projection. Reload Window.

Local plugin checkout (this repo as a sibling, unpushed changes):

```bash
/path/to/shipyard/scripts/sync-cursor.sh --target /path/to/consuming-repo --plugin /path/to/shipyard
```

Flags:

```bash
scripts/sync-cursor.sh --dry-run          # print actions, write nothing
scripts/sync-cursor.sh --keep-local       # do not overwrite pack files that differ
scripts/sync-cursor.sh --no-kernel        # packs only (when Cursor loads project plugins again)
```

Idempotent: a second run with no plugin changes should report `unchanged` only.

When Cursor loads project plugins again, drop kernel copies (`--no-kernel` or stop listing them) so slash commands are not duplicated. Packs stay copied.

## Install globally (dev only)

Copy (do not symlink — Cursor rejects plugin symlinks whose target is outside `~/.cursor/plugins/local`):

```bash
rsync -a --delete --exclude .git /absolute/path/to/shipyard/ ~/.cursor/plugins/local/shipyard/
```

Reload Window. Applies to **all** projects — prefer the submodule flow above for product repos.

## Layout

| Path | Role |
| --- | --- |
| `commands/` | `/plan-prd`, `/ship-ticket`, `/ship-prd`, `/review-diff`, `/audit-ui`, `/setup-shipyard`, `/update-shipyard` |
| `agents/` | Writer and reviewer prompts (read overlay first) |
| `rules/agent-routing.mdc` | Always-on routing |
| `skills/setup-shipyard/` | Interactive overlay + sync |
| `skills/verification-loop/` | QA from overlay command list |
| `scripts/sync-cursor.sh` | Materialize kernel + packs into the consuming repo |
| `packs/` | Copied into the repo by sync (visual, react, vite, typescript, postgres, security) |
| `templates/` | overlay, git-conventions, skill-routing, workspace hook |

## Overlay

`docs/agents/shipyard.md` in the consuming repo: surfaces, packs, QA commands, git base branch. Agents and commands read it on start.

Tickets of `/plan-prd` and `/ship-*` live under `.scratch/` even if Matt triage uses GitHub Issues.
