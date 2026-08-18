---
description: Plan a feature end-to-end — grill, spec, tickets — without implementing code
---

# /plan-prd

Orchestrate planning for a new or extended feature. **No product code.**

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Use overlay `visual` / `copy` to decide whether to launch `designer` and allow `Surface: frontend` | `design-system`.

## Arguments

Optional: feature slug, idea description, path to notes, or path to **`AUDIT.md`** from `/audit-ui`.

When `AUDIT.md` is provided, treat approved findings as requirements input — do not re-audit.

## Model

Orchestrator and `planner` agent: **`cursor-grok-4.6-high`**

## Steps

1. If the idea is fuzzy, delegate to **`planner`** (Grok) with Matt `/grill-with-docs` — one question at a time when needed.
2. Explore the repo: `CONTEXT.md`, relevant ADRs, existing `features/<slug>/`, optional `AUDIT.md`.
3. Confirm **test seams** with the user before writing tickets.
4. Delegate to **`planner`** to run Matt `/to-spec` → `.scratch/<feature>/PRD.md`.
5. **If overlay `visual: on` and the PRD / idea touches UI** — after the PRD exists, delegate to **`designer`** (Grok) to land `design-system/` specs **before** frontend tickets are written.
6. Delegate to **`planner`** to run Matt `/to-tickets` with `Blocked by` edges.
7. **Every ticket** must declare **`Surface:`** (`backend` | `frontend` | `design-system` | `tooling`). Omit frontend/design-system when `visual: off`.
8. **Mixed work** — split tickets: `backend` → `implementer`, `frontend` → `frontend-developer`, `design-system` → `designer`. `Blocked by` so frontend waits on backend and/or DS as needed.
9. Set `**Status:** ready-for-agent` on PRD and tickets per `docs/agents/triage-labels.md`.
10. **Stop.** Tell the user to run `/ship-ticket` or `/ship-prd` when ready.

## Surface → writer

| Surface | Writer |
| --- | --- |
| `backend` | `implementer` |
| `frontend` | `frontend-developer` |
| `design-system` | `designer` |
| `tooling` | `implementer` |

## Launching subagents

Use the Task tool with pinned models. Tell each agent to follow its shipyard agent prompt and `docs/agents/shipyard.md`. Fallback if custom subagent type unavailable: still pin the model and paste that instruction.

## Forbidden

- `/implement`, editing product source or migrations
- Commits
