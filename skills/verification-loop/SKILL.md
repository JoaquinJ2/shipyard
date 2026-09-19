---
name: verification-loop
description: Run this repo's quality gates from docs/agents/shipyard.md before claiming work complete. Use after implementation, before PR or ticket close.
---

# Verification loop

Read **`docs/agents/shipyard.md`** first.

The orchestrator passes a **scope**: `ticket` | `increment`.

## Resolve command list

1. If overlay has `## QA (ticket)` and `## QA (increment)`, run that section's commands **in order**.
2. **Fallback** (legacy single `## QA` list):
   - `increment` → that whole list
   - `ticket` → Agent profile `proof_commands` (split on commas). If empty, run the whole list.

Stop on first failure and report stderr.

If the overlay is missing, stop and tell the user to run `/setup-shipyard`.

## Livingdocs

Run `node bin/livingdocs-lint.mjs` only when:

- scope is **`increment`**, and `.livingdocs.json` exists, and files under `triggerPaths` changed; **or**
- scope is `ticket` but the diff already touched those `triggerPaths` on this close (contract commit)

Skip otherwise (`Livingdocs: SKIP`).

`/livingdocs-record` is the orchestrator's job (last ticket / increment close), not this loop.

## Security spot-check

Search product source (from overlay surface globs, not `node_modules/`) for hardcoded secrets and stray debug logs. Flag findings; do not fail the loop solely on `console.log` unless the overlay says so.

## Output format

```
VERIFICATION REPORT
==================
Scope:     ticket | increment
(one line per command run: PASS/FAIL)
Livingdocs:[PASS/FAIL/SKIP]
Security:  [PASS/FAIL] (notes)

Overall:   [READY / NOT READY]
```

Mark Overall **READY** only if every command that ran passed.

Used by the `qa-verifier` agent and `/ship-ticket`.
