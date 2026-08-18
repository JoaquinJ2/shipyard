# Shipyard

Cursor plugin: plan a PRD, ship tickets with **writer ≠ reviewer**, then record behaviour.

Kernel (commands, agents, routing) loads from the plugin. Per-repo overlay and stack packs are created by `/setup-shipyard`.

## Install from Cursor (local repo)

Customize → Add → Plugin from local repo. Point at this repository root. Cursor indexes `.cursor-plugin/marketplace.json` (not `plugin.json` alone). Then enable **shipyard** at **User** scope and Reload Window.

Do **not** pick Project in that dialog. Cursor currently crashes project-scope marketplace installs with `Failed to install Shipyard, please try again or reload the window.` ([tracked](https://forum.cursor.com/t/project-scope-marketplace-plugin-install-fails-with-workspace-collection-is-not-available-3-13-25-remote-wsl/167083)). Per-repo install is the submodule + hook flow below, not that toggle.

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

Reload the Cursor window. Then run `/setup-shipyard` in the target repo.

After clone: `git submodule update --init --recursive .cursor/plugins/shipyard`

## Install globally (dev only)

Copy (do not symlink — Cursor rejects plugin symlinks whose target is outside `~/.cursor/plugins/local`):

```bash
rsync -a --delete --exclude .git /absolute/path/to/shipyard/ ~/.cursor/plugins/local/shipyard/
```

Reload Window. Applies to **all** projects — prefer the submodule flow above for product repos.

## Layout

| Path | Role |
| --- | --- |
| `commands/` | `/plan-prd`, `/ship-ticket`, `/ship-prd`, `/review-diff`, `/audit-ui`, `/setup-shipyard` |
| `agents/` | Writer and reviewer prompts (read overlay first) |
| `rules/agent-routing.mdc` | Always-on routing |
| `skills/setup-shipyard/` | Interactive overlay + pack copy |
| `skills/verification-loop/` | QA from overlay command list |
| `packs/` | Copied into the repo by setup (visual, react, vite, typescript, postgres, security) |
| `templates/` | overlay, git-conventions, skill-routing, workspace hook |

## Overlay

`docs/agents/shipyard.md` in the consuming repo: surfaces, packs, QA commands, git base branch. Agents and commands read it on start.

Tickets of `/plan-prd` and `/ship-*` live under `.scratch/` even if Matt triage uses GitHub Issues.
