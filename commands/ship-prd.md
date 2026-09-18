---
description: Ship a full PRD — branch, all tickets in dependency order, conventional commits per ticket
---

# /ship-prd

Deliver every ticket in `.scratch/<feature-slug>/` respecting `Blocked by` edges.

Inherits the full **`/ship-ticket`** pipeline per ticket (CORE section gate, plan gate, frozen AC, reviews, QA).

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Git rules: `docs/agents/git-conventions.md`. Base branch from overlay (default `main`).

## Arguments

Feature slug (directory name under `.scratch/`).

## Orchestrator

**Grok** (`cursor-grok-4.6-high`). Does not write product code.

## Step 1 — Load PRD

- Read `.scratch/<slug>/PRD.md` and all `issues/*.md`
- Abort if PRD missing or no tickets
- Verify every ticket has `**Surface:**`
- Prefer tickets already `ready-for-agent`. If a ticket is still `needs-info`, run `/refine-ticket` (or abort) — do not ship undecidable work
- If any ticket has `## Agent-readiness gaps`, require explicit user confirm before that ticket

## Step 2 — Branch (once, before any ticket)

Create or checkout the increment branch **from the overlay base branch**:

```
feat/<feature-slug>
```

1. `git fetch origin` when possible
2. Checkout base, pull (or local base if offline)
3. `git checkout -b feat/<feature-slug>` — or checkout if same increment in progress
4. If branch has unrelated work → **stop**, ask user
5. **Never** implement on the base branch

All tickets in this run commit to this single branch.

## Step 3 — Build execution order

1. Parse `Blocked by:` on each ticket
2. Tickets with no unresolved blockers are **ready**
3. Independent ready tickets **may run in parallel** when they touch disjoint file trees
4. Sequential chain when blockers exist
5. UI tickets (`Surface: frontend` or `design-system`) that touch the same overlay frontend/DS globs → run **serially** even if unblocked

## Step 4 — Per ticket

For each ticket in order, run the **`/ship-ticket`** pipeline **on the shared branch** `feat/<feature-slug>`:

- claim → CORE/plan gates → writer by `Surface:` → parallel reviewers → `qa-verifier` → fix loop → livingdocs → resolve

| Surface | Writer |
| --- | --- |
| `backend`, `tooling` | `implementer` (Composer) |
| `frontend` | `frontend-developer` (Composer) |
| `design-system` | `designer` (Grok) |

Use a fresh `FIXED_POINT` per ticket (tip of branch before that ticket's implementation).

Never reuse a writer's context for review. Never let a writer self-review.
Do not re-run the readiness gate unless the ticket body mutated since READY.

## Step 5 — Commit per ticket

After each ticket passes gates, commit **on `feat/<feature-slug>`** before starting the next (unless user asked to squash — default is one commit per ticket). Format: `docs/agents/git-conventions.md`.

Ask user before the first commit if not explicitly requested; subsequent tickets may commit without re-asking if the user approved the increment.

## Step 6 — Archive increment

When all tickets are `resolved`:

1. Archive tree to `.scratch/archive/<slug>/` per `docs/agents/issue-tracker.md`
2. Update `.scratch/archive/README.md` and any map files the issue-tracker doc names
3. Run `/livingdocs-record` if not already done for final behaviour
4. Optional final commit if archive/map changes remain unstaged: `docs(<feature-slug>): archive shipped PRD increment`
5. Set PRD **Status:** `shipped` before or as part of archive

## Parallelism note

Parallel tickets only when `Blocked by` allows **and** file trees do not overlap. Serialize commits on one branch.

## Forbidden

- Skipping review for "small" tickets
- Shipping tickets that fail the CORE section gate
- Silently editing AC mid-loop
- Leaving shipped PRD under active `.scratch/<slug>/`
- Commits on the base branch
- Force-push or amend pushed commits
