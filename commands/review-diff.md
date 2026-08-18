---
description: Run the review and QA battery on current diff — no writer
---

# /review-diff

Review-only gate. Use before merge, after manual work, or to re-check a branch.

**No writer** — report only unless the user asks to fix.

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

## Arguments

Fixed point: commit SHA, branch name, tag, or overlay base branch (default: ask user if unclear).

Optional: ticket/PRD path, or writer context (`implementer` | `frontend-developer` | `designer`) to decide Design self-review skip.

## Orchestrator

**Grok** (`cursor-grok-4.6-high`).

## Step 1 — Pin diff

```bash
git rev-parse <fixed-point>
git diff <fixed-point>...HEAD --stat
git log <fixed-point>..HEAD --oneline
```

Abort if empty diff or bad ref.

## Step 2 — Identify spec source

1. Ticket/PRD path from user argument
2. `.scratch/**/issues/*.md` matching branch or recent commits
3. Ask user if none found

Infer writer from ticket `Surface:` when available (for Design axis skip).

## Step 3 — Review battery (parallel, Grok, read-only)

Launch in one message:

| Agent | When |
| --- | --- |
| `spec-reviewer` | always |
| `standards-reviewer` | always |
| `security-reviewer` | always |
| `database-reviewer` | overlay `database: on` and diff matches SQL globs |
| `copywriter` | overlay copy not `off` and visible strings changed |
| `designer` (reviewer) | overlay `visual: on`, UI/css/DS changed, **and** writer ≠ `designer` |

When reviewing a `Surface: design-system` ticket where `designer` was the writer, **skip** the Design axis.

Each gets diff command, spec path, and the shipyard agent. **No editing.**

## Step 4 — QA

Launch `qa-verifier` with `verification-loop` and overlay QA list.

## Step 5 — Report

Aggregate under headings:

```
## Spec
## Standards
## Security
## Database
## Copy
## Design
## QA
```

One-line summary: READY / NOT READY and worst issue per axis.

## Forbidden

- Launching any **writer**
- Skipping the Design **review** axis when Step 3 requires it
- Auto-fixing findings (report only unless user asks to fix)
