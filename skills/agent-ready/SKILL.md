---
name: agent-ready
description: >-
  Write, refine, slice, or gate shipyard tickets for cold-start agent implementation.
  Use for /plan-work, /plan-prd (alias), /refine-ticket, ticket drafting, slicing, acceptance criteria,
  proof plans, stop conditions, and READY vs NEEDS_MORE_INFO readiness reviews.
---

# Agent-ready tickets (shipyard)

Adapted from the sibling **agent-ready-tickets** standard. Shipyard owns ticket anatomy,
slicing, refinement, and the readiness gate. Matt skills still drive discovery (`/grill-with-docs`,
`/to-spec`, `/to-tickets`); this skill constrains what those drafts must become before
`ready-for-agent`.

## The one goal

> A ticket is done when an implementing agent can open it cold, with no access to the author,
> and be **≥95% certain** of what to build, what not to build, where it lives, and when to stop.

Uncertainty above 5% is a **defect in the ticket**, not something the writer will figure out.

## Failure modes

| Failure | Prevented by |
| --- | --- |
| Ambiguity — two valid implementations | `rules/30-decisions-and-boundaries.md` |
| Silent scope drift — no end boundary | `rules/30-decisions-and-boundaries.md` |
| Unverifiable done — criteria restate HOW | `rules/40-acceptance-criteria.md` |

## Load order

| When | Read |
| --- | --- |
| Always, before writing | `rules/00-invariants.md` |
| Delivery ticket | `rules/10-ticket-anatomy.md` + `templates/feature-task.md` |
| One vs many | `rules/20-slicing.md` |
| Forks / scope | `rules/30-decisions-and-boundaries.md` |
| AC / proof | `rules/40-acceptance-criteria.md` |
| Refining | `rules/50-refinement-loop.md` + `templates/refinement-comment.md` |
| READY vs NMI | `rules/60-readiness-gate.md` + `checklists/readiness-gate.md` |
| Bug | `templates/bug.md` |
| Intake | `templates/request-intake.md` |
| Parent / epic | `templates/epic.md` (never agent-ready) |
| Spec warranted? | `rules/20-slicing.md` §Spec + `templates/spec.md` |
| PRD under `.scratch/` (shape D/E only) | `templates/prd.md` |

## Shipyard homes

| Artifact | Path |
| --- | --- |
| Delivery issues | `.scratch/<feature>/issues/<NN>-<slug>.md` |
| PRD (shape D/E only) | `.scratch/<feature>/PRD.md` |
| Project proof/traps/escalation | `docs/agents/shipyard.md` → **Agent profile** |
| Surfaces / QA / packs | `docs/agents/shipyard.md` |

## Non-negotiables

1. Never invent a path, symbol, identifier, field, label, command or endpoint. "Unknown" is allowed; a plausible guess is not.
2. Never set `ready-for-agent` as the ticket author — only `ticket-readiness-reviewer` in fresh context.
3. An open fork in the body means not ready. Close it, or park under Open questions with default + stop condition.
4. Every current-system claim carries evidence.
5. Transcribe screenshots/attachments/design frames into text.
6. If discussion redirected the ticket, the body must say so and what it supersedes.
7. After a justified split, assign **exactly one** `Surface:` (`backend` | `frontend` | `design-system` | `tooling`). Never invent `fullstack`.

## Ready marker

In shipyard markdown: `**Status:** ready-for-agent` only after a fresh-context `READY` verdict.
Drafts stay at `needs-info` (or `needs-triage`) until then.
