---
description: Plan a feature end-to-end — grill, invent, slice, draft, refine, readiness gate — without implementing code
---

# /plan-prd

Orchestrate planning for a new or extended feature. **No product code.**

Pipeline: Discover (Matt) → Manufacture tickets (`agent-ready`) → Gate (`ticket-readiness-reviewer`) → hand off to `/ship-*`.

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Read **`.cursor/skills/agent-ready/SKILL.md`** (load order table).

Use overlay `visual` / `copy` to decide whether to launch `designer` and allow `Surface: frontend` | `design-system`.

## Arguments

Optional: feature slug, idea description, path to notes, or path to **`AUDIT.md`** from `/audit-ui`.

When `AUDIT.md` is provided, treat approved findings as requirements input — do not re-audit.

## Model

Orchestrator and `planner` agent: **`cursor-grok-4.6-high`**. Readiness reviewer: same model, **fresh** context — never `inherit` from planner.

## Steps

1. **Overlay gate** — as above.

2. **Discover** — If the idea is fuzzy, delegate to **`planner`** with Matt `/grill-with-docs` (one question at a time when needed). Grill outcomes must land in the PRD as `## Approvals / proposed defaults (locked)` (A1…An). **No tickets** until the human confirms test seams (A-seam / A10-style row).

3. **Explore** — `CONTEXT.md`, relevant ADRs, existing `features/<slug>/`, optional `AUDIT.md`, overlay Agent profile.

4. **Inventory first** — Search `.scratch/` (and tracker if used) per `agent-ready` `rules/20-slicing.md`. Record what was searched and refused.

5. **Shape A–E** — Decide refine / one item / several / parent+children / spec+items. Do **not** always force a fat PRD. Shape B may use a thin PRD stub linking one ticket.

6. **PRD** — Delegate to **`planner`** to run Matt `/to-spec` constrained by `skills/agent-ready/templates/prd.md` → `.scratch/<feature>/PRD.md`. Skip a duplicate narrative spec when tickets alone would reconstruct the product (`rules/20` §Spec); still keep the PRD skeleton for Approvals, seams, and Delivery map when using `/ship-prd`.

7. **Design-system first** — If overlay `visual: on` and the PRD / idea touches UI — after the PRD exists, delegate to **`designer`** to land `design-system/` specs **before** frontend tickets are written.

8. **Draft tickets** — Delegate to **`planner`** to run Matt `/to-tickets` constrained by `templates/feature-task.md` + rules `10` / `20` / `30` / `40`.
   - Split by **blocked-ness**, then **proof unit**, then **ownership** — not by layer as a reflex.
   - After each justified split, assign **exactly one** `Surface:` (`backend` | `frontend` | `design-system` | `tooling`). Omit frontend/design-system when `visual: off`. Never invent `fullstack`.
   - Each ticket includes `## Why this is a separate ticket` (one line).
   - Fill state table, Decisions, Stop conditions, AC, Proof plan (Agent profile commands).
   - Set `**Status:** needs-info` on every new ticket. **Forbidden** to set `ready-for-agent` in this step.

9. **Refine** — Run `agent-ready` `rules/50-refinement-loop.md` (ground → OQs → fold). Max **3** planner passes through draft→gate.

10. **Readiness gate** — For **each** delivery ticket, launch **`ticket-readiness-reviewer`** in a **fresh** Grok context (pass number N). Paste verdict into ticket `## Readiness`.
    - `READY` → orchestrator sets `**Status:** ready-for-agent`
    - `NEEDS_MORE_INFO` and pass &lt; 3 → back to refine
    - Pass 3, advisory only → append `## Agent-readiness gaps`; leave **not** ready-for-agent unless human explicitly accepts
    - Pass 3, still CORE fail → reclassify intake/spike; do not hand off to `/ship-ticket`

11. **Stop.** Tell the user which tickets are `ready-for-agent` and to run `/ship-ticket` or `/ship-prd` when ready. Optionally `/refine-ticket` for stragglers.

## Surface → writer (routing only)

| Surface | Writer |
| --- | --- |
| `backend` | `implementer` |
| `frontend` | `frontend-developer` |
| `design-system` | `designer` |
| `tooling` | `implementer` |

## Launching subagents

Use the Task tool with pinned models. Tell each agent to follow its shipyard agent prompt, `docs/agents/shipyard.md`, and `agent-ready` skill. Fallback if custom subagent type unavailable: still pin the model and paste that instruction.

## Forbidden

- `/implement`, editing product source or migrations
- Commits
- Setting `ready-for-agent` without a fresh `ticket-readiness-reviewer` READY verdict
- Self-gating tickets the planner just wrote in the same context
