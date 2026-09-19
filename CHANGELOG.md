# Changelog

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
