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

## QA (ordered, stop on fail)

{{QA_LIST}}

## Git

```
base: {{BASE_BRANCH}}
commits: conventional
```

## Review globs

- SQL (database-reviewer): {{SQL_GLOBS}}
- UI (designer reviewer / audit-ui): {{UI_GLOBS}}
