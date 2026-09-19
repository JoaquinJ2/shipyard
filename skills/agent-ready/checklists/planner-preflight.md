# Planner preflight (not the CORE gate)

Run by the **planner** in the drafting context, **before** launching `ticket-readiness-reviewer`.
This is a structural presence check. It does **not** authorize `ready-for-agent`.

If any item is missing, fix the body (or open a BLOCKING question) and **do not** launch the gate.

Score YES / NO. `N/A` only for Parent when the tree has no PRD (then the body must show `—`).

## Presence

- [ ] **C1** — `Done means:` (or an equivalent one-sentence observable done) is in the body
- [ ] **C2** — Current state / locators exist (state table or named paths/symbols)
- [ ] **C3** — Decisions (or Approvals) exist; grill locks folded if this was `/plan-work`
- [ ] **C4** — Out of scope or explicit empty
- [ ] **C5** — Acceptance criteria as a checkbox list
- [ ] **C6** — Proof plan present
- [ ] **C7** — Proof plan cites overlay Agent profile commands or a ticket narrowing
- [ ] **C8** — Stop conditions **or** explicit `None — no admitted unknowns`
- [ ] **C10** — No unresolved BLOCKING open questions left in the body (or they have defaults + stops)
- [ ] **Surface:** is exactly one of `backend` | `frontend` | `design-system` | `tooling`
- [ ] **Lane:** is `light` | `standard` | `high` (and `light` is not used when the work is DB/auth/RLS/payments/secrets/public contract/new DS rule)
- [ ] **Parent** is a PRD link or `—`
