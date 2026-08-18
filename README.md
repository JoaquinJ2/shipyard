# Shipyard

Cursor plugin: plan a PRD, ship tickets with **writer ≠ reviewer**, then record behaviour.

Kernel (commands, agents, routing) loads from the plugin. Per-repo overlay and stack packs are created by `/setup-shipyard`.

## Prerequisites (in the target repo)

1. Matt `/setup-matt-pocock-skills`
2. `/livingdocs-install`

## Install in a repo (recommended)

Project scope — not global:

```bash
git submodule add https://github.com/JoaquinJ2/shipyard.git .cursor/plugins/shipyard
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

```bash
ln -s /absolute/path/to/shipyard ~/.cursor/plugins/local/shipyard
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
