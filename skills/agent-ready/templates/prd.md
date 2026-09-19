# Template — PRD (shipyard)

Path: `.scratch/<feature>/PRD.md`

A PRD is the **parent definition** for an initiative. It is **not** agent-ready for
implementation — delivery issues under `issues/` are. Write this file **only** for shape D or E
from `rules/20-slicing.md`. Do **not** stub a PRD for shape B or C (`/plan-work`).

Matt `/to-spec` may draft content; this template is the required skeleton.

---

# <Feature title>

**Status:** needs-info
**Slug:** `<feature-slug>`

## Problem

<Why this initiative exists, in outcome terms. Evidence, not assertion.>

## Outcomes

- <Observable outcome in the user's terms.>
- **Measured by:** <metric or qualitative check, if any.>

## Who this is for

| Persona | Need | Today instead |
| --- | --- | --- |
| <…> | <…> | <…> |

## Approvals / proposed defaults (locked)

Grill outcomes land here. Do not write tickets until seams (below) are human-confirmed.

| # | Decision | Proposed default |
| --- | --- | --- |
| A1 | <…> | **<bold default>** |
| A10 | Test seams | **Highest seam:** `<path>` + adapter; CI never hits <X> |

## Test seams (proposed — confirm)

**Highest seam:** <module + test approach>
**Ban:** <what tests must not do>

Seams are **decided** only after human confirm. Do not set ticket `ready-for-agent` until then.

## Policy and decisions

| # | Decision | Source | Supersedes |
| --- | --- | --- | --- |
| D1 | <assertion> | <…> | <…> |

## Scope

**In scope:** <capability-level>
**Out of scope:** <with owner / deferred / never>
**Explicitly deferred:** <condition to bring back>

## Delivery map

| NN | Slice | Surface | Blocked by | Proof unit |
| --- | --- | --- | --- | --- |
| 01 | <what it delivers> | backend | — | <demoable behaviour> |

Children live at `issues/<NN>-<slug>.md`. Prefer split by blocked-ness then proof unit; assign
Surface after the split.

## Design (when visual: on and UI)

- Design-system work lands **before** frontend tickets.
- Link `design-system/` paths once designer has written them.

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| <…> | <…> | <…> |

## Open questions

| # | Question | Blocks | Default |
| --- | --- | --- | --- |
| Q1 | <…> | tickets / none | <…> |

## Inventory

- Searched `.scratch/` for: <terms>
- Duplicate / near-dupe / candidate parent: <none | path>
- Outcome code (A–E / Dup): <…> — refused to create/split: <…>

## References

- <CONTEXT.md, ADRs, AUDIT.md, features/ — only what was consulted>
