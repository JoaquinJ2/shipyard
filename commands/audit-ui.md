---
description: Audit UI and copy — read-only report to .scratch/<audit-slug>/AUDIT.md; no src/ edits
---

# /audit-ui

Read-only audit of product UI and copy. Produces a report for human confirmation before `/plan-work`.

**Never edits product UI source.** Never ships fixes directly.

## On start

Read **`docs/agents/shipyard.md`**. If missing, stop and tell the user to run `/setup-shipyard`.

If overlay `visual: off`, stop — this command does not apply.

## Arguments

Scope (required — one of):

| Scope | Meaning |
| --- | --- |
| `app` | Full product surfaces under overlay frontend globs |
| `feature:<slug>` | Routes/components tied to `features/<slug>/` and matching routes |
| `<routes>` | Explicit route paths or screen names |
| `commits:<ref>` | Diff since ref — audit only changed UI/copy |

Optional: audit slug (default: `ui-audit-<date>` or derived from scope).

## Orchestrator

**Grok** (`cursor-grok-4.6-high`). Does not write product code.

## Step 1 — Resolve scope

1. Parse scope argument
2. List files and routes in scope (read-only)
3. For `commits:<ref>`: `git diff <ref>...HEAD` limited to overlay UI/css/DS globs
4. Create output directory: `.scratch/<audit-slug>/`

## Step 2 — Parallel audit (Grok, read-only)

Launch in **one message**, fresh contexts:

| Agent | When |
| --- | --- |
| `copywriter` | overlay copy not `off` |
| `designer` | always (visual is on) |

Each prompt: scope; shipyard agent; MASTER/pages for designer; `CONTEXT.md` for copywriter; **read-only**.

## Step 3 — Write AUDIT.md

Merge findings into `.scratch/<audit-slug>/AUDIT.md`:

```markdown
# UI audit — <scope>

**Date:** <ISO date>
**Scope:** <scope description>

## Copy findings
## Design findings
## Proposed wording
## Proposed DS updates
## How to fix
```

## Step 4 — Close

Tell the user to run `/plan-work` with path `.scratch/<audit-slug>/AUDIT.md` when they want tickets.

Do not run `/plan-work`, `/plan-prd`, `/ship-ticket`, or `/ship-prd` unless the user asks.

## Forbidden

- Editing product source
- Auto-fixing findings
- Commits
- Skipping human confirmation before planning
