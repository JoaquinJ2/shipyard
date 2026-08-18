# Overlay packs

`scripts/sync-cursor.sh` copies from here into the consuming repo (`/setup-shipyard` first time, `/update-shipyard` later). Do not load `packs/` as plugin skills (not under `skills/` at plugin root).

| Pack | Destination skills | Destination rules |
| --- | --- | --- |
| `visual` | `copy-voice`, `design-system`, `frontend-surfaces` | `copy-voice.mdc`, `design-system.mdc` |
| `react` | `ecc-react-patterns` | `react-*.mdc` |
| `vite` | `ecc-vite-patterns` | — |
| `typescript` | — | `typescript-*.mdc` |
| `postgres` | `ecc-postgres-patterns`, `ecc-database-migrations` | `postgres-supabase.mdc` |
| `security` | `ecc-security-review`, `ecc-error-handling` | `security.mdc`, `typescript-security.mdc`, `react-security.mdc` (last two only if typescript/react packs are also on) |

Copy destination: `.cursor/skills/<name>/` and `.cursor/rules/<file>.mdc`.

Default: overwrite shipyard-managed files so plugin updates reach the repo. Pass `--keep-local` to skip pack files that differ from the plugin. Files not listed in `.cursor/shipyard-managed.json` (livingdocs, feature-spark, …) are never touched.
