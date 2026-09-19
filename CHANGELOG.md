# Changelog

## 0.4.0

### Added

- **Lane** `light | standard | high` on tickets (and PRDs). Routes review, QA, and whether a design-system ticket is warranted.
- Planner **preflight** (`checklists/planner-preflight.md`) before the CORE gate; gate may batch 1–5 tickets of the same tree.
- Overlay **QA (ticket)** vs **QA (increment)**; `qa-verifier` scope. Legacy single `## QA` list still works (increment + `proof_commands` for ticket).
- `.scratch/deferred/` for parked trees; `archive/` is shipped-only.
- ADR `docs/adr/0002-risk-proportional-process.md`.

### Changed

- `/plan-work` does not launch designer merely because `visual: on` and the work touches UI.
- Ship review matrix: spec always; standards skipped on light (static lints); security always only on `high`.
- `/livingdocs-record` at contract close (last ticket / no-PRD tree), not every PRD slice.
- `/ship-prd` serializes writers; increment QA once at the end.

## 0.3.0

### Added

- **`/plan-work`** — canonical intake: always `/grill-with-docs`, then inventory, then shape A–E. PRD only for D/E. Shape B/C write issues without `PRD.md`.
- Kernel **`CONTEXT.md`** and **`docs/adr/0001-plan-work-intake.md`**.

### Changed

- **`/plan-prd`** is an alias of `/plan-work` (does not always write a PRD).
- `/refine-ticket` and `/ship-ticket` load a parent PRD only if present.
- Issue tracker: `## Parent` is `—` when there is no PRD; archive still moves the tree.

## 0.2.0

### Added

- **`skills/agent-ready/`** — ticket anatomy, slicing, decisions/stops, AC/proof, refinement loop, CORE readiness gate, anti-patterns, examples, and templates (feature-task, bug, epic, spec, intake, refinement, OQ answers, PRD). Adapted from agent-ready-tickets.
- **`ticket-readiness-reviewer`** agent — fresh-context READY vs NEEDS_MORE_INFO; only READY authorizes `ready-for-agent`.
- **`/refine-ticket`** — refine one `.scratch` issue + readiness gate.
- Overlay **Agent profile** (proof_commands, must_stay_green, traps, do_not, escalation).
- Templates: `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md` (unified status state machine).
- Ship-ticket **Plan gate** (Step 2.5) and CORE section gate before implement.

### Changed

- `/plan-prd` manufactures tickets at `needs-info`, then gates — never self-marks `ready-for-agent`.
- `Surface:` documented as routing after justified split (blocked-ness → proof → ownership).
- Writers honor stop conditions and Proof plans; AC frozen at `claimed`.
- `spec-reviewer` grades against `Done means:` / AC / Out of scope / stops.
- Routing invariant: ticket author ≠ readiness gate.

## 0.1.0

Initial kernel: plan/ship/review commands, writers ≠ reviewers, overlay packs, sync materialization.
