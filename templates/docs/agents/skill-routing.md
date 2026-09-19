# Skill and agent routing

How shipyard commands, plugin agents, Matt skills, and in-repo packs fit together.

Kernel (commands, agents, `agent-routing`, `setup-shipyard`, `verification-loop`, `agent-ready`) is materialized into `.cursor/commands`, `.cursor/agents`, `.cursor/skills`, and `.cursor/rules` by `scripts/sync-cursor.sh`. Overlay: [shipyard.md](./shipyard.md). Packs land in the same folders. Refresh with `/update-shipyard`.

## Quick reference

| I want to… | Use |
| --- | --- |
| Figure out which flow fits | Matt `/ask-matt` (global) |
| Sharpen an idea + glossary/ADRs | Matt `/grill-with-docs` |
| Plan without coding (to ready tickets) | `/plan-work` (`/plan-prd` alias) |
| Refine one ticket + readiness gate | `/refine-ticket` |
| Ship one ticket | `/ship-ticket` |
| Ship whole PRD | `/ship-prd` |
| Review current diff only | `/review-diff` |
| Audit UI/copy without editing product UI | `/audit-ui` (visual pack) |
| Pull plugin updates into `.cursor/` | `/update-shipyard` |
| Record behaviour in docs | `/livingdocs-record` |

## Invariants

**Writer ≠ reviewer (code):** Writers never run `/code-review` or commit. Reviewers are read-only Grok in fresh context. Models never inherit writer → reviewer.

**Author ≠ readiness gate (tickets):** `planner` drafts at `needs-info`. Only `ticket-readiness-reviewer` in fresh context may authorize `ready-for-agent`. Never inherit planner → readiness reviewer.

Every ticket declares **`Surface:`** (`backend` | `frontend` | `design-system` | `tooling`) **after** a justified split. Paths come from [shipyard.md](./shipyard.md).

## Commands → pipeline

### `/plan-work`

`/plan-prd` is an alias of this command.

```
planner (Grok) + agent-ready skill
  → grill-with-docs (always) → locks A1…An
  → inventory active + deferred + archive
  → shape A–E + Lane (rules/20; bias A/B; light forbidden on DB/auth/…)
  → halt on C/D/E or ambiguous B vs D; continue on A/B/Dup
  → designer specs only if reusable visual contract changes
  → seams on ticket (B/C) or PRD (D/E)
  → D/E only: to-spec → .scratch/<feature>/PRD.md (templates/prd.md)
  → to-tickets → issues/*.md (Lane; Parent PRD or —; Surface after slice; Status needs-info)
  → refine loop (max 3) + planner-preflight
  → ticket-readiness-reviewer (fresh, batch 1–5 same tree)
  → only READY → ready-for-agent
  → stop (no code); /ship-prd only if PRD.md exists
```

### `/refine-ticket`

```
planner refine (agent-ready rules/50 + preflight)
  → ticket-readiness-reviewer (fresh; batch 1 unless siblings named)
  → READY → ready-for-agent | NMI → needs-info | pass3 CORE fail → intake/spike
```

### `/ship-ticket`

```
claim ticket (ready-for-agent or claimed; CORE sections present)
  → branch feat/<feature>/<NN>-<ticket-slug> from overlay base
  → Plan gate (## Plan) — halt if Decisions/stops violated
  → writer by Surface
  → review matrix by Lane + diff (spec always)
  → qa-verifier ticket or increment
  → fix loop (max 2; AC frozen at claimed)
  → livingdocs-record on contract close only
  → resolve ticket (+ archive if last and fully resolved)
  → conventional commit on ship branch
```

### `/ship-prd`

Same as `/ship-ticket` per ticket on `feat/<feature-slug>`, **one writer at a time**, ordered by `Blocked by`. Ticket QA per slice; increment QA + livingdocs at close. One conventional commit per ticket.

### `/review-diff`

Review matrix + QA (default increment). No writer.

## Matt skills (global, not in repo)

Do **not** duplicate `ask-matt`, `grill-with-docs`, `to-spec`, `to-tickets`, `implement`, `tdd`, `code-review` in the repo. Shipyard `agent-ready` constrains ticket quality after Matt drafts.

## In-repo packs

Copied by `scripts/sync-cursor.sh` according to overlay packs (`/setup-shipyard` first time, `/update-shipyard` later). Livingdocs stays a separate install. Kernel skill `agent-ready` always syncs.

## Agents

Materialized into `.cursor/agents/` (and still authored in the plugin). Commands pin models when launching Task:

- Composer writers: `composer-2.5`
- Grok agents (including `ticket-readiness-reviewer`): `cursor-grok-4.6-high`

## Issue tracker

See [issue-tracker.md](./issue-tracker.md). Ship tickets live in `.scratch/<feature>/issues/` even if Matt triage uses GitHub. Ticket craft: `.cursor/skills/agent-ready/`.

## Git

See [git-conventions.md](./git-conventions.md).

## Models policy

Use **only** Cursor models (Composer, Grok). Do not use Claude or GPT slugs in shipyard commands.
