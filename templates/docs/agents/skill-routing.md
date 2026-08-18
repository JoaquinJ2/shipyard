# Skill and agent routing

How shipyard commands, plugin agents, Matt skills, and in-repo packs fit together.

Kernel (commands, agents, `agent-routing`, `setup-shipyard`, `verification-loop`) is materialized into `.cursor/commands`, `.cursor/agents`, `.cursor/skills`, and `.cursor/rules` by `scripts/sync-cursor.sh`. Overlay: [shipyard.md](./shipyard.md). Packs land in the same folders. Refresh with `/update-shipyard`.

## Quick reference

| I want to… | Use |
| --- | --- |
| Figure out which flow fits | Matt `/ask-matt` (global) |
| Sharpen an idea + glossary/ADRs | Matt `/grill-with-docs` |
| Plan without coding | `/plan-prd` |
| Ship one ticket | `/ship-ticket` |
| Ship whole PRD | `/ship-prd` |
| Review current diff only | `/review-diff` |
| Audit UI/copy without editing product UI | `/audit-ui` (visual pack) |
| Pull plugin updates into `.cursor/` | `/update-shipyard` |
| Record behaviour in docs | `/livingdocs-record` |

## Invariant: writer ≠ reviewer

Writers never run `/code-review` or commit. Reviewers are read-only Grok in fresh context. Models never inherit writer → reviewer.

Every ticket declares **`Surface:`** (`backend` | `frontend` | `design-system` | `tooling`). Paths come from [shipyard.md](./shipyard.md).

## Commands → pipeline

### `/plan-prd`

```
planner (Grok)
  → grill-with-docs (optional)
  → if visual on and UI: designer specs in design-system/ (before tickets)
  → confirm seams
  → to-spec → .scratch/<feature>/PRD.md
  → to-tickets → issues/*.md (each with Surface:)
  → stop (no code)
```

### `/ship-ticket`

```
claim ticket (must have Surface:)
  → branch feat/<feature>/<NN>-<ticket-slug> from overlay base
  → writer by Surface
  → parallel reviewers (Grok; conditional copy/design/database)
  → qa-verifier (overlay QA list)
  → fix loop (max 2)
  → livingdocs-record
  → resolve ticket (+ archive if last)
  → conventional commit on ship branch
```

### `/ship-prd`

Same as `/ship-ticket` per ticket on `feat/<feature-slug>`, ordered by `Blocked by`. One conventional commit per ticket.

### `/review-diff`

Review battery + QA only. No writer.

## Matt skills (global, not in repo)

Do **not** duplicate `ask-matt`, `grill-with-docs`, `to-spec`, `to-tickets`, `implement`, `tdd`, `code-review` in the repo.

## In-repo packs

Copied by `scripts/sync-cursor.sh` according to overlay packs (`/setup-shipyard` first time, `/update-shipyard` later). Livingdocs stays a separate install.

## Agents

Materialized into `.cursor/agents/` (and still authored in the plugin). Commands pin models when launching Task:

- Composer writers: `composer-2.5`
- Grok agents: `cursor-grok-4.6-high`

## Issue tracker

See [issue-tracker.md](./issue-tracker.md). Ship tickets live in `.scratch/<feature>/issues/` even if Matt triage uses GitHub.

## Git

See [git-conventions.md](./git-conventions.md).

## Models policy

Use **only** Cursor models (Composer, Grok). Do not use Claude or GPT slugs in shipyard commands.
