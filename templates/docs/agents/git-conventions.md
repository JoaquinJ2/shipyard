# Git conventions for ship commands

Branch and commit rules for `/ship-ticket` and `/ship-prd`. Based on [Conventional Commits](https://www.conventionalcommits.org/).

Base branch: **`{{BASE_BRANCH}}`** (match `origin` HEAD). Override in `docs/agents/shipyard.md` if this file still says `main` and the overlay differs.

## Branches

Never implement on the base branch. Create a dedicated branch before the writer runs.

### `/ship-ticket` (one ticket)

```
feat/<feature-slug>/<NN>-<ticket-slug>
```

- `<feature-slug>` = directory under `.scratch/`
- `<NN>` = ticket number from filename (`01`, `02`, …)
- `<ticket-slug>` = rest of filename without `.md`

### `/ship-prd` (full increment)

```
feat/<feature-slug>
```

All tickets in that increment commit to this branch (one commit per ticket when possible).

### Branch setup (orchestrator)

1. `git fetch origin` (when network available)
2. If not already on the ship branch:
   - checkout base, pull (or merge-base from local base if pull fails offline)
   - `git checkout -b feat/...` (or checkout existing if **same scope**)
3. If the branch exists with unrelated work, **stop** and ask the user
4. Set `FIXED_POINT` to the branch tip **after** branch creation

Do not force-push, rebase, or amend commits already pushed.

## Commits

Use **Conventional Commits** for every commit created by ship commands.

### Format

```
<type>(<scope>): <subject>

[optional body]

Ticket: .scratch/<feature>/issues/<NN>-<slug>.md
```

### Types

| Type | When |
| --- | --- |
| `feat` | New user-visible capability (default for most tickets) |
| `fix` | Bug fix or incorrect behaviour |
| `docs` | Documentation-only change (no code behaviour) |
| `refactor` | Structure change, same behaviour |
| `test` | Tests only |
| `chore` | Tooling, deps, config — no product behaviour |

### Scope

Feature slug in kebab-case. Omit scope only if the change is truly repo-wide (`chore(deps): ...`).

### Subject

- Imperative mood: "add catalog seed" not "added" or "adds"
- Lowercase start
- No trailing period
- ~72 characters max

### `/ship-ticket`

- **One commit** when the pipeline passes and the user confirms (or commit was requested)
- Stage only files for this ticket; do not bundle unrelated changes

### `/ship-prd`

- **One commit per ticket** after each ticket passes review + QA
- Final ticket may include archive-only `.scratch/` moves in the same commit as its code if they belong together

### Commit command

Always use a HEREDOC for the message:

```bash
git add <paths>
git commit -m "$(cat <<'EOF'
feat(example): add the thing

Ticket: .scratch/example/issues/01-slug.md
EOF
)"
```

## What not to do

- No commits on the base branch during ship
- No `--no-verify` unless the user explicitly asks
- No `git commit --amend` on pushed commits
- No empty commits
- No force-push
