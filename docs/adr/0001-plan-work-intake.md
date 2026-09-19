# Plan-work is the intake; a PRD is not the default parent

`/plan-prd` always manufactured a PRD (or a stub) even when slicing said the work was one delivery unit. That contradicted `rules/20` (do not write a spec because the workflow has a spec step) and skipped grill when the ask “looked small”, which hid initiatives.

We made `/plan-work` the canonical intake: grill always runs first, then inventory, then shape A–E. `PRD.md` is written only for D/E. B and C live as issues with `## Parent: —`. `/plan-prd` remains as an alias so existing muscle memory does not break. `/ship-prd` still requires a real PRD; a C ships as N × `/ship-ticket`.

**Considered options:** two commands (`/plan-ticket` vs `/plan-prd`); keep the `/plan-prd` name with a conditional pipeline; stub PRDs for folder uniformity. Rejected: two front doors; a name that implies every ask is an initiative; empty parent files.

**Consequences:** `/refine-ticket` and `/ship-ticket` must not abort when `PRD.md` is missing. Archive still moves the whole scratch tree.
