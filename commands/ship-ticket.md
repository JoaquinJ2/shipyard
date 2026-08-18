---
description: Ship one ready-for-agent ticket — branch, implement, multi-reviewer gate, livingdocs, conventional commit
---

# /ship-ticket

End-to-end ship for **one** ticket under `.scratch/<feature>/issues/`.

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

Git rules: `docs/agents/git-conventions.md`. Base branch from overlay (default `main`).

## Arguments

Ticket path (e.g. `.scratch/my-feature/issues/01-slug.md`) or ticket number + feature slug.

## Orchestrator

Parent session: **Grok** (`cursor-grok-4.6-high`). Orchestrator does not write product code.

## Step 1 — Load ticket

- Read ticket + parent PRD
- Verify `**Status:**` is `ready-for-agent` or `claimed`
- Verify `**Surface:**` is present (`backend` | `frontend` | `design-system` | `tooling`)
- Reject `frontend` / `design-system` when overlay `visual: off`
- Verify blockers listed in `Blocked by:` are `resolved`
- Set `**Status:** claimed` if not already
- Derive `<feature-slug>`, `<NN>`, `<ticket-slug>` from the ticket path

## Step 2 — Branch (before any product code)

Create or checkout the ship branch **from the overlay base branch**:

```
feat/<feature-slug>/<NN>-<ticket-slug>
```

1. `git fetch origin` when possible
2. Checkout base, pull (or use local base if offline)
3. `git checkout -b feat/<feature-slug>/<NN>-<ticket-slug>` — or checkout existing if same ticket and scope
4. If branch exists with unrelated work → **stop**, ask user
5. **Never** implement on the base branch

Capture `FIXED_POINT` = current `HEAD` on the ship branch **after** branch creation.

## Step 3 — Implement (writer by Surface)

Launch **exactly one** writer in **fresh context** per ticket `Surface:`:

| Surface | Writer | Model |
| --- | --- | --- |
| `backend` | `implementer` | `composer-2.5` |
| `frontend` | `frontend-developer` | `composer-2.5` |
| `design-system` | `designer` | `cursor-grok-4.6-high` |
| `tooling` | `implementer` | `composer-2.5` |

Prompt must include: follow the named shipyard agent; read `docs/agents/shipyard.md`; implement ONLY this ticket; Matt `/implement` + `/tdd` at seams for Composer writers; do NOT run `/code-review` or commit; ticket/PRD/branch paths.

## Step 4 — Review battery (read-only, parallel)

Launch in **one message**, all Grok, **fresh contexts**:

| Agent | When |
| --- | --- |
| `spec-reviewer` | always |
| `standards-reviewer` | always |
| `security-reviewer` | always |
| `database-reviewer` | overlay `database: on` and diff matches overlay SQL globs |
| `copywriter` | overlay copy not `off` and diff touches visible user-facing strings |
| `designer` (reviewer) | overlay `visual: on`, diff touches UI/css/DS, **and** writer ≠ `designer` |

When `Surface: design-system`, skip the Design review axis.

Each prompt: `git diff FIXED_POINT...HEAD`; ticket + PRD; shipyard agent; writer used; **read-only**.

## Step 5 — QA gate

Launch **`qa-verifier`** (Grok) with the `verification-loop` skill and overlay QA list.

## Step 6 — Fix loop

If any CRITICAL/HIGH finding or QA failure:

| Finding type | Writer |
| --- | --- |
| Copy / UI strings / layout in frontend globs | `frontend-developer` (Composer) |
| DS gap / MASTER / page spec | `designer` (Grok) → then `frontend-developer` if UI still needed |
| Domain / SQL / hooks / tooling | `implementer` (Composer) |

1. Send aggregated findings to the matching writer (fresh context)
2. Repeat steps 4–5
3. Max **2** fix cycles; then set ticket `ready-for-human` and stop

## Step 7 — Close

1. Run **`/livingdocs-record`** if behaviour changed
2. Append `## Answer` to ticket; set `**Status:** resolved`
3. If last open ticket in PRD → archive per `docs/agents/issue-tracker.md`

## Step 8 — Commit (Conventional Commits)

After gates pass. Ask user first unless they already asked to commit in this command.

Format per `docs/agents/git-conventions.md`:

```
<type>(<scope>): <imperative subject>

Ticket: .scratch/<feature>/issues/<NN>-<slug>.md
```

- Default type: `feat` (use `fix` if the ticket is a defect)
- Scope: `<feature-slug>`
- One commit for this ticket on the ship branch
- Use HEREDOC for `git commit -m`

Do not commit on the base branch. Do not amend pushed commits. Do not force-push.

## Invariant

Writers never run reviewers. Reviewers never implement. Models never inherit writer → reviewer.
