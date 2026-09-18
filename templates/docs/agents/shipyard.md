# Shipyard overlay

Per-repo contract. Kernel commands and agents read this file on start. Written by `/setup-shipyard`.

## Surfaces

| Surface | Writer | Owns |
| --- | --- | --- |
| `backend` | implementer | {{BACKEND_GLOBS}} |
| `frontend` | frontend-developer | {{FRONTEND_GLOBS}} |
| `design-system` | designer | design-system/** |
| `tooling` | implementer | .cursor/skills, .cursor/rules (overlay), docs/agents/ |

Omit `frontend` and `design-system` rows when `visual: off`.

`Surface:` is routing metadata after a justified ticket split — not the primary split reason.

## Packs

```
visual: {{VISUAL}}
database: {{DATABASE}}
copy: {{COPY}}
react: {{REACT}}
vite: {{VITE}}
typescript: {{TYPESCRIPT}}
security: {{SECURITY}}
```

`copy` is `es-tuteo` | `off` | path to a copy skill. `visual: off` implies skip `/audit-ui` and `Surface: frontend` / `design-system`.

## Agent profile

Ticket Proof plans and stop escalations read this section (agent-ready C7 / stops). Prefer real commands from the repo — do not invent.

```
proof_commands: {{PROOF_COMMANDS}}
must_stay_green: {{MUST_STAY_GREEN}}
traps: {{TRAPS}}
do_not: {{DO_NOT}}
escalation:
  product: {{ESCALATION_PRODUCT}}
  env: {{ESCALATION_ENV}}
```

- `proof_commands` — default targeted test / typecheck / lint a writer can run before handoff (tickets may narrow)
- `must_stay_green` — suites or paths that must not regress
- `traps` — cron/cache/jobs that mask bugs; known flaky areas
- `do_not` — standing constraints (e.g. no new deps without approval)
- `escalation` — who/role to mention when a stop condition needs a human

## QA (ordered, stop on fail)

{{QA_LIST}}

Overlay QA is the post-diff gate (`qa-verifier`). Ticket Proof plans are what writers run before claiming done.

## Git

```
base: {{BASE_BRANCH}}
commits: conventional
```

## Review globs

- SQL (database-reviewer): {{SQL_GLOBS}}
- UI (designer reviewer / audit-ui): {{UI_GLOBS}}
