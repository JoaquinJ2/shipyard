# Template — parent item / epic

A parent is an **overview**, not a delivery item. It never carries the delivery stencil and is
never marked `ready-for-agent`. In shipyard the usual parent is `.scratch/<feature>/PRD.md`
(`templates/prd.md`); use this epic shape when you need a lighter parent without a full PRD.

---

## Problem

<Why this initiative exists, in outcome terms. 2–4 sentences.>

## What we are building

<The shape of the solution at initiative level. No locators, no implementation.>

## Decisions (do not reopen)

1. **<Assertion.>** Source: <…>.

<Decisions that bind every child. A child may refine them; a child may not contradict them.>

## Children

| Key | Slice | Surface | State | Blocked by |
| --- | --- | --- | --- | --- |
| `issues/01-….md` | <what it delivers> | <surface> | <state> | <NN or —> |

<Say how the slices relate: sequential phases, parallel per segment, data-then-interface.>

## In scope

- <…>

## Out of scope

- <…> → <owning initiative / deferred / never>

## Constraints

<Legal, contractual, deadline, gating, platform limits.>

## Related

- <path> — <relationship, and what it does not cover>
