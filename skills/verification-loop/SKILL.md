---
name: verification-loop
description: Run this repo's quality gates from docs/agents/shipyard.md before claiming work complete. Use after implementation, before PR or ticket close.
---

# Verification loop

Read **`docs/agents/shipyard.md`** first. Run the **QA** commands listed there **in order**. Stop on first failure and report stderr.

If the overlay is missing, stop and tell the user to run `/setup-shipyard`.

## Livingdocs

If `.livingdocs.json` exists and files under its `triggerPaths` changed:

```bash
node bin/livingdocs-lint.mjs
```

Behaviour changes require `/livingdocs-record` before ticket close. Skip this phase when those paths were not touched.

## Security spot-check

Search product source (from overlay surface globs, not `node_modules/`) for hardcoded secrets and stray debug logs. Flag findings; do not fail the loop solely on `console.log` unless the overlay says so.

## Output format

```
VERIFICATION REPORT
==================
(one line per overlay QA command: PASS/FAIL)
Livingdocs:[PASS/FAIL/SKIP]
Security:  [PASS/FAIL] (notes)

Overall:   [READY / NOT READY]
```

Mark Overall **READY** only if every overlay QA command passed.

Used by the `qa-verifier` agent and `/ship-ticket`.
