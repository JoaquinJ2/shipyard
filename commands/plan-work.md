---
description: Plan work — grill, choose shape A–E, draft agent-ready tickets, readiness gate — without implementing code
---

# /plan-work

Orchestrate planning for an ask. **No product code.** Canonical intake. `/plan-prd` is an alias of this command.

Pipeline: Grill (always) → Inventory → Shape A–E → Manufacture tickets (`agent-ready`) → Gate (`ticket-readiness-reviewer`) → hand off to `/ship-*`.

A **PRD** is written only for shape **D** or **E** (an initiative). Shape **B** and **C** use `.scratch/<slug>/issues/` with no `PRD.md`.

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Read **`.cursor/skills/agent-ready/SKILL.md`** (load order table) and `rules/20-slicing.md`.

Use overlay `visual` / `copy` to decide whether to launch `designer` and allow `Surface: frontend` | `design-system`.

## Arguments

Optional: feature slug, idea description, path to notes, or path to **`AUDIT.md`** from `/audit-ui`.

When `AUDIT.md` is provided, treat approved findings as requirements input — do not re-audit.

## Model

Orchestrator and `planner` agent: **`cursor-grok-4.6-high`**. Readiness reviewer: same model, **fresh** context — never `inherit` from planner.

## Steps

1. **Overlay gate** — as above.

2. **Grill always** — Delegate to **`planner`** with Matt `/grill-with-docs` (even if only a couple of questions). Do **not** skip because the ask looks small. Locks are numbered A1…An. **No tickets** until grill locks exist.

3. **Explore** — `CONTEXT.md`, relevant ADRs, existing `features/<slug>/`, optional `AUDIT.md`, overlay Agent profile.

4. **Inventory first** — Search `.scratch/` **active**, `.scratch/deferred/`, and `.scratch/archive/` (and tracker if used) per `agent-ready` `rules/20-slicing.md`. Deferred is **not** shipped. Record what was searched and refused.

5. **Shape A–E + Lane** — Bias to **A** or **B**. State in one paragraph: outcome code, why, inventory class, what you refused to create or split. Then set `**Lane:**` `light` | `standard` | `high` (after grill + inventory).
   - **light** is forbidden when the work includes DB/migration, auth/RLS, payments, secrets, a public contract, or a **new** reusable visual rule (`design-system/**`).
   - **light** is typically shape B, one ticket, no DS ticket.
   - Forbidden: a PRD because the workflow has a PRD step.
   - Forbidden: split by layer (backend / frontend) as a reflex.
   - **A / B / Dup:** announce the shape and **continue**.
   - **C / D / E**, or **B vs D ambiguous:** **halt** with one question. Do not write artifacts until the human confirms.

6. **Artifacts** (after continue or confirm) — Delegate to **`planner`**. Fold grill locks into the right home (below). Do not create `APPROVALS.md` or a stub PRD.

   | Shape | Write | Do not write |
   | --- | --- | --- |
   | **A** | Refine the existing issue (same loop as `/refine-ticket`) | New tree, PRD |
   | **B** | `.scratch/<slug>/issues/01-<slug>.md`; `## Parent`: `—`; seam on the ticket | `PRD.md`, `to-spec` |
   | **C** | N issues in the **same** `.scratch/<slug>/issues/`; `## Parent`: `—`; real links only | `PRD.md` |
   | **D / E** | `templates/prd.md` → `.scratch/<slug>/PRD.md` via Matt `/to-spec`, then children | Stub PRD for a single ticket |

   Grill locks: **D/E** → PRD `## Approvals / proposed defaults (locked)`. **B/C** → each ticket `## Decisions` (or `## Approvals`).

   Skip a duplicate narrative spec when tickets alone would reconstruct the product (`rules/20` §Spec). `to-spec` runs **only** for D/E.

7. **Seams** — D/E: human confirms test seams (A-seam / A10-style) before child tickets if not already locked in Approvals. B/C: Highest seam + Ban on the ticket. If the seam is **new** or conflicts with Agent profile, halt with one question.

8. **Design-system first** — Overlay `visual: on` does **not** by itself create a `design-system` ticket or launch `designer` before frontend. Do that **only** when a reusable visual contract is created or changed (`design-system/**`). Applying existing MASTER/tokens → `Surface: frontend`; Design review later if the ship **diff** touches UI.

9. **Draft tickets** — Matt `/to-tickets` constrained by `templates/feature-task.md` (or `bug.md`) + rules `10` / `20` / `30` / `40`.
   - Split by **blocked-ness**, then **proof unit**, then **ownership** — not by layer as a reflex.
   - After each justified split, assign **exactly one** `Surface:` (`backend` | `frontend` | `design-system` | `tooling`). Omit frontend/design-system when `visual: off`. Never invent `fullstack`.
   - Each ticket includes `## Why this is a separate ticket` (one line).
   - Fill state table, Decisions (including grill locks on B/C), Stop conditions, AC, Proof plan (Agent profile commands).
   - Set `**Lane:**` on every ticket (and on the PRD when D/E).
   - Set `**Status:** needs-info` on every new ticket. **Forbidden** to set `ready-for-agent` in this step.

10. **Refine** — Run `agent-ready` `rules/50-refinement-loop.md` (ground → OQs → fold). Max **3** planner passes through draft→gate. Before launching the gate, the planner runs `checklists/planner-preflight.md`. If preflight fails, do **not** launch the reviewer.

11. **Readiness gate** — Launch **`ticket-readiness-reviewer`** in a **fresh** Grok context (pass number N) with a **batch of 1–5** delivery tickets from the **same** scratch tree. Never `inherit` from planner. One independent `VERDICT` per file. Paste each into that ticket `## Readiness`.
    - `READY` → orchestrator sets `**Status:** ready-for-agent`
    - `NEEDS_MORE_INFO` and pass &lt; 3 → back to refine
    - Pass 3, advisory only → append `## Agent-readiness gaps`; leave **not** ready-for-agent unless human explicitly accepts
    - Pass 3, still CORE fail → reclassify intake/spike; do not hand off to `/ship-ticket`

12. **Stop.** Name the shape, paths written, which tickets are `ready-for-agent`. Suggest `/ship-ticket` per ticket. Suggest `/ship-prd` **only** when `PRD.md` exists (D/E). Shape **C** ships as N × `/ship-ticket`. Optionally `/refine-ticket` for stragglers.

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
- Writing `PRD.md` for shape A, B, or C
- Skipping `/grill-with-docs`
