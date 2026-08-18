---
name: setup-shipyard
description: Configure this repo's shipyard overlay and copy stack/visual packs. Run once after Matt setup and livingdocs-install. Use when installing shipyard, adding packs, or regenerating docs/agents/shipyard.md.
disable-model-invocation: true
---

# Setup shipyard

Prompt-driven. Explore, present findings, walk decisions **one section at a time**, show a draft, then write.

Kernel (commands, agents, routing) stays in the plugin — **do not copy** `commands/`, `agents/`, or `rules/agent-routing.mdc` into the repo.

## Plugin root

This file lives at `skills/setup-shipyard/SKILL.md`. Packs and templates are sibling folders of `skills/`:

- `packs/<pack>/skills/` and `packs/<pack>/rules/`
- `templates/docs/agents/`

Resolve plugin root as the directory that contains both `packs/` and `skills/setup-shipyard/`. Try, in order: two levels up from this `SKILL.md`; `~/.cursor/plugins/local/shipyard`. If none exist, stop.

## Gate (do not skip)

All of these must exist. If any is missing, **stop** and name the command to run. Do not invent issue-tracker or livingdocs files.

| Required | Command if missing |
| --- | --- |
| `docs/agents/issue-tracker.md` | `/setup-matt-pocock-skills` |
| `docs/agents/triage-labels.md` | `/setup-matt-pocock-skills` |
| `docs/agents/domain.md` | `/setup-matt-pocock-skills` |
| `.livingdocs.json` and `DDD.md` | `/livingdocs-install` |

Do **not** re-ask issue tracker, triage labels, or domain layout.

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

Explainer: `qa-verifier` runs these commands in order and stops on failure.

Propose from real scripts (`npm run build`, `npx tsc --noEmit`, `npm run lint`, `npm test`, `go test ./...`, etc.). Do not invent gates that are not in the repo.

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

## 3. Draft

Show:

- Full `docs/agents/shipyard.md`
- List of pack files that will be copied vs skipped (already exist)
- `## Shipyard` block for `AGENTS.md` (or `CLAUDE.md` if that is the file Matt used — prefer `AGENTS.md` if both exist and already has Agent skills / Living documentation)

Let the user edit before writing.

## 4. Write

Idempotent. Never duplicate `## Shipyard`. Never touch `## Agent skills` or `## Living documentation`.

1. Write `docs/agents/shipyard.md` from the draft (fill `templates/docs/agents/shipyard.md`).
2. Write `docs/agents/git-conventions.md` from `templates/docs/agents/git-conventions.md` with `{{BASE_BRANCH}}` replaced. If the file already exists, update the base branch line only unless the user asked to refresh.
3. Write `docs/agents/skill-routing.md` from the template (safe to replace — it is generated).
4. Upsert `## Shipyard` in `AGENTS.md`:

```markdown
## Shipyard

Kernel (commands, agents, routing) loads from the **shipyard plugin**. This repo's overlay is [docs/agents/shipyard.md](docs/agents/shipyard.md).

| Command | Purpose |
| --- | --- |
| `/plan-prd` | Grill → spec → tickets with `Surface:` (designer first if visual UI). No product code. |
| `/ship-ticket` | One ticket: branch → writer by `Surface:` → review → QA → livingdocs → conventional commit |
| `/ship-prd` | Full PRD on `feat/<slug>` — one commit per ticket |
| `/review-diff` | Review + QA only (no writer) |
| `/audit-ui` | UI/copy audit report only (visual pack; no product UI edits) |

**Writer ≠ reviewer.** See [docs/agents/skill-routing.md](docs/agents/skill-routing.md). Git: [docs/agents/git-conventions.md](docs/agents/git-conventions.md). Matt process skills stay global. Livingdocs stays a separate install.
```

If a `## Delivery system` heading exists, replace it with `## Shipyard` (do not leave both).

5. Copy enabled packs: for each file in `packs/<pack>/skills/<name>/` → `.cursor/skills/<name>/`; each `packs/<pack>/rules/*.mdc` → `.cursor/rules/`. **Skip** if the destination already exists unless the user asked to refresh from template.
6. Ensure `.scratch/.gitkeep` exists.
7. Do not create `CONTEXT.md`. Do not run `/livingdocs-vision`. Do not copy plugin `commands/`, `agents/`, or `agent-routing.mdc`.

## 5. Done

List paths created, skipped (already present), and packs enabled. Tell the user to Reload Window if the plugin was just symlinked, then `/plan-prd`.
