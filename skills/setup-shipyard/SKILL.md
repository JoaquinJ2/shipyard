---
name: setup-shipyard
description: Configure this repo's shipyard overlay and copy stack/visual packs. Run once after Matt setup and livingdocs-install. Use when installing shipyard, adding packs, or regenerating docs/agents/shipyard.md.
disable-model-invocation: true
---

# Setup shipyard

Prompt-driven. Explore, present findings, walk decisions **one section at a time**, show a draft, then write.

After the overlay exists, **materialize** kernel (commands, agents, routing, plugin skills) and enabled packs with `scripts/sync-cursor.sh`. Do not copy those files by hand. Refresh later with `/update-shipyard`.

## Plugin root

This file lives at `skills/setup-shipyard/SKILL.md`. Packs, templates, and `scripts/sync-cursor.sh` are sibling folders of `skills/`:

- `packs/<pack>/skills/` and `packs/<pack>/rules/`
- `templates/docs/agents/`
- `scripts/sync-cursor.sh`

Resolve plugin root as the directory that contains both `packs/` and `skills/setup-shipyard/`. Try, in order:

1. `.cursor/plugins/shipyard` in the workspace (git submodule — **preferred**)
2. Two levels up from this `SKILL.md` when the skill runs from an installed plugin
3. `~/.cursor/plugins/local/shipyard` (global dev fallback only)

If none exist, stop and tell the user to add the submodule (see shipyard `README.md`) or run `/setup-shipyard` after installing the plugin in the repo.

## Gate (do not skip)

Livingdocs and domain layout must exist. If missing, **stop** and name the command. Do not invent livingdocs files.

| Required | Command if missing |
| --- | --- |
| `docs/agents/domain.md` | `/setup-matt-pocock-skills` |
| `.livingdocs.json` and `DDD.md` | `/livingdocs-install` |

`docs/agents/issue-tracker.md` and `docs/agents/triage-labels.md`: if missing, setup copies shipyard templates (do not overwrite existing Matt copies). Prefer Matt versions when present.

Do **not** re-ask domain layout when `domain.md` already exists.

Ship tickets always live under `.scratch/<feature>/issues/` even if Matt triage uses GitHub Issues. Record that in the overlay. Create `.scratch/` (with `.gitkeep`) if it does not exist.

## 1. Explore

Read whatever exists; don't assume:

- `package.json` / `pyproject.toml` / `go.mod` — scripts, deps
- Tree: `src/`, `app/`, `lib/`, `supabase/`, `design-system/`, `*.sql`
- `AGENTS.md` / `CLAUDE.md` — existing `## Shipyard` or `## Delivery system`
- `docs/agents/shipyard.md` — already configured?
- `.cursor/skills/` and `.cursor/rules/` — packs already copied?
- Overlay git base: `git symbolic-ref refs/remotes/origin/HEAD` or local default branch (default `main`)

## 2. Interview (one section at a time)

Each section: short explainer, detected default, choices. Wait for the answer before the next section.

### A — Surfaces

Explainer: every ship ticket has a `Surface:` so `/ship-ticket` launches one writer. Map directories this repo actually has.

Propose globs from the tree (examples: `src/lib/`, `src/hooks/`, `supabase/` → backend; `src/routes/`, `src/components/`, `src/styles.css` → frontend; `design-system/**` → design-system; `docs/agents/`, `.cursor/skills`, `.cursor/rules` → tooling).

If there is no UI, propose `visual: off` and only `backend` + `tooling`.

### B — QA

Explainer: `qa-verifier` has two scopes. **Ticket** uses Agent profile `proof_commands` (focal). **Increment** uses the full ordered suite when a scratch tree closes. Stop on failure.

Propose the **increment** list from real scripts (`npm run build`, `npx tsc --noEmit`, `npm run lint`, `npm test`, `go test ./...`, etc.). Do not invent gates that are not in the repo. `proof_commands` (section F) should be a cheaper subset (often typecheck + targeted test).

### C — Visual and copy (skip if no UI / user chose visual off)

Explainer: visual pack copies design-system + frontend-surfaces + copy-voice and enables `/audit-ui`.

- visual: on / off
- copy: `es-tuteo` (default when visual on) / `off` / another skill path later

### D — Git

Explainer: ship branches fork from the base branch. Conventional Commits are fixed.

Ask only if the detected default branch is not `main`. Do not mention third-party git hosts or editors.

### E — Stack packs

Explainer: setup copies skills and rules into `.cursor/` so reviewers and writers have stack context.

Propose on/off from detection:

- `react` — tsx/React deps
- `vite` — vite in package.json
- `typescript` — tsconfig
- `postgres` — supabase/, `*.sql`, postgres deps (`database: on` when this is on)
- `security` — default on

Confirm with the user. Copy `react-security.mdc` / `typescript-security.mdc` only when those packs are also on.

### F — Agent profile

Explainer: ticket Proof plans and stop escalations read this block (agent-ready skill). Prefer commands that already exist in the repo.

Ask / propose:

- `proof_commands` — e.g. same as targeted test + typecheck + lint from section B (comma-separated or YAML list)
- `must_stay_green` — critical suites or paths
- `traps` — jobs/caches/flaky areas that mask bugs (`none` if unknown)
- `do_not` — standing constraints (`none` if none)
- `escalation.product` / `escalation.env` — role or handle strings (e.g. `human-product`, `human-env`) — not invented GitHub users

Defaults when user is unsure: proof_commands = QA list; others = `none` / `human`.

## 3. Draft

Show:

- Full `docs/agents/shipyard.md`
- That `scripts/sync-cursor.sh` will materialize kernel + enabled packs (overwrite shipyard-managed files)
- `## Shipyard` block for `AGENTS.md` (or `CLAUDE.md` if that is the file Matt used — prefer `AGENTS.md` if both exist and already has Agent skills / Living documentation)

Let the user edit before writing.

## 4. Write

Idempotent. Never duplicate `## Shipyard`. Never touch `## Agent skills` or `## Living documentation`.

1. Write `docs/agents/shipyard.md` from the draft (fill `templates/docs/agents/shipyard.md`, including **Agent profile**).
2. Write `docs/agents/git-conventions.md` from `templates/docs/agents/git-conventions.md` with `{{BASE_BRANCH}}` replaced. If the file already exists, update the base branch line only unless the user asked to refresh.
3. If missing, copy `templates/docs/agents/issue-tracker.md` → `docs/agents/issue-tracker.md` and `templates/docs/agents/triage-labels.md` → `docs/agents/triage-labels.md`. **Do not overwrite** if they already exist (Matt or prior setup owns them).
4. Upsert `## Shipyard` in `AGENTS.md`:

```markdown
## Shipyard

Kernel (commands, agents, routing) is materialized into `.cursor/commands`, `.cursor/agents`, and `.cursor/rules` from the **shipyard** submodule at `.cursor/plugins/shipyard`. After clone: `git submodule update --init --recursive .cursor/plugins/shipyard`, then `/update-shipyard` (or `scripts/sync-cursor.sh`). Reload Window.

This repo's overlay is [docs/agents/shipyard.md](docs/agents/shipyard.md).

| Command | Purpose |
| --- | --- |
| `/plan-work` | Grill (always) → inventory → shape A–E + Lane → draft → preflight → batched gate → tickets. PRD only for D/E. `/plan-prd` is an alias. |
| `/refine-ticket` | Refine one `.scratch` issue + fresh CORE readiness gate |
| `/ship-ticket` | One ticket: branch → plan gate → writer → review matrix → QA ticket/increment → livingdocs on contract close → commit |
| `/ship-prd` | Full PRD on `feat/<slug>` — one writer at a time; increment QA at end |
| `/review-diff` | Review + QA only (no writer) |
| `/audit-ui` | UI/copy audit report only (visual pack; no product UI edits) |
| `/update-shipyard` | Pull submodule + re-copy kernel and packs into `.cursor/` |

**Writer ≠ reviewer.** **Ticket author ≠ readiness gate.** See [docs/agents/skill-routing.md](docs/agents/skill-routing.md). Git: [docs/agents/git-conventions.md](docs/agents/git-conventions.md). Matt process skills stay global. Ticket craft: `agent-ready` skill. Livingdocs stays a separate install.
```

If a `## Delivery system` heading exists, replace it with `## Shipyard` (do not leave both).

5. Ensure `.scratch/.gitkeep` exists.
6. Do not create `CONTEXT.md`. Do not run `/livingdocs-vision`.
7. Materialize kernel + packs (no `--pull` on first setup):

```bash
<plugin-root>/scripts/sync-cursor.sh --target <repo-root>
```

The script overwrites shipyard-managed files, writes `.cursor/shipyard-managed.json`, and refreshes `docs/agents/skill-routing.md` from the template. It does not touch livingdocs, feature-spark, or `docs/agents/shipyard.md`.

If the user asked to preserve local pack edits, add `--keep-local`.

## 5. Done

List the script summary (created / updated / unchanged / skipped / removed) and packs enabled. Tell the user to Reload Window, then `/plan-work`. Later updates: `/update-shipyard`.
