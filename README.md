# Shipyard

Cursor plugin: plan a PRD, ship tickets with **writer ≠ reviewer**, then record behaviour.

Kernel (commands, agents, routing) loads from the plugin. Per-repo overlay and stack packs are created by `/setup-shipyard`.

## Prerequisites (in the target repo)

1. Matt `/setup-matt-pocock-skills`
2. `/livingdocs-install`

## Install (local)

```bash
ln -s /absolute/path/to/shipyard ~/.cursor/plugins/local/shipyard
```

Reload the Cursor window. Confirm **Customize → Plugins** lists `shipyard`.

Then in the target repo: `/setup-shipyard`.

## Layout

| Path | Role |
| --- | --- |
| `commands/` | `/plan-prd`, `/ship-ticket`, `/ship-prd`, `/review-diff`, `/audit-ui` |
| `agents/` | Writer and reviewer prompts (read overlay first) |
| `rules/agent-routing.mdc` | Always-on routing |
| `skills/setup-shipyard/` | Interactive overlay + pack copy |
| `skills/verification-loop/` | QA from overlay command list |
| `packs/` | Copied into the repo by setup (visual, react, vite, typescript, postgres, security) |
| `templates/` | `git-conventions.md`, `skill-routing.md`, overlay example |

## Overlay

`docs/agents/shipyard.md` in the consuming repo: surfaces, packs, QA commands, git base branch. Agents and commands read it on start.

Tickets of `/plan-prd` and `/ship-*` live under `.scratch/` even if Matt triage uses GitHub Issues.
