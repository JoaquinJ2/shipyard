---
description: Refine one .scratch ticket — ground, fold, fresh readiness gate — without implementing code
---

# /refine-ticket

Run the agent-ready refinement loop + readiness gate on **one** existing issue. **No product code.**

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Read **`.cursor/skills/agent-ready/SKILL.md`**, especially `rules/50-refinement-loop.md` and `rules/60-readiness-gate.md`.

## Arguments

Ticket path (e.g. `.scratch/my-feature/issues/01-slug.md`) or ticket number + feature slug. Optional: pass number (default: infer from existing `## Readiness` or start at 1).

## Model

Orchestrator and `planner`: **`cursor-grok-4.6-high`**. `ticket-readiness-reviewer`: same model, **fresh** context — never `inherit` from planner.

## Steps

1. Load ticket. Load parent `PRD.md` **if present**. Do **not** abort when there is no PRD (shape B/C). Abort if the ticket file is missing.
2. If status is `claimed` / `resolved`, stop — do not refine mid-ship without human confirm.
3. Delegate to **`planner`** to refine per `rules/50`:
   - Ground in repo (commit/environment Limitation line)
   - Inventory related `.scratch/` items (active, deferred, archive)
   - Draft or replace body using `templates/feature-task.md` / `bug.md` as appropriate
   - Run `checklists/planner-preflight.md` — if it fails, do not launch the gate
   - Open questions → fold answers into Decisions
   - Keep or set `**Status:** needs-info`
   - **Never** set `ready-for-agent`
4. Launch **`ticket-readiness-reviewer`** in fresh context with pass number N (this command: batch of 1 unless the user named siblings in the same tree, then 1–5).
5. Apply outcome:
   - `READY` → set `ready-for-agent`; paste `## Readiness`
   - `NEEDS_MORE_INFO` and pass &lt; 3 → leave `needs-info`; tell user to re-run or continue answers
   - Pass 3, advisory only → append `## Agent-readiness gaps`; do **not** set ready unless human explicitly accepts
   - Pass 3, still CORE fail → reclassify toward intake/spike (`templates/request-intake.md`); do not `/ship-ticket`
6. **Stop.** Suggest `/ship-ticket` only when `ready-for-agent` (or human-accepted gaps).

## Forbidden

- `/implement`, product source edits, commits
- Self-certifying READY in the planner context
