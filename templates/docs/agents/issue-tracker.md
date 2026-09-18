# Issue tracker: Local Markdown (shipyard)

Issues and PRDs live as markdown under `.scratch/`. Shipped trees move to `.scratch/archive/<feature-slug>/`.

Ticket craft (anatomy, slicing, readiness): `.cursor/skills/agent-ready/` (templates under that skill).

## Layout

| Artifact | Path |
| --- | --- |
| PRD | `.scratch/<feature-slug>/PRD.md` |
| Delivery issues | `.scratch/<feature-slug>/issues/<NN>-<slug>.md` (from `01`) |
| Archive | `.scratch/archive/<feature-slug>/` |

## Required ticket fields

Near the top of every delivery issue:

- `**Status:**` — see [triage-labels.md](./triage-labels.md)
- `**Surface:**` — `backend` | `frontend` | `design-system` | `tooling` (routing after a justified split)
- `**Blocked by:**` — ticket numbers or `—`
- `## Parent` — link to PRD

Prefer full agent-ready anatomy (`Done means:`, Current state, Decisions, Stop conditions, AC, Proof plan). See `skills/agent-ready/templates/feature-task.md`.

## `Surface:` (routing, not slicing)

| Surface | Writer | Typical paths (override in shipyard.md) |
| --- | --- | --- |
| `backend` | `implementer` | overlay backend globs |
| `frontend` | `frontend-developer` | overlay frontend globs |
| `design-system` | `designer` | `design-system/**` only |
| `tooling` | `implementer` | overlay tooling globs |

Split by blocked-ness / proof unit / ownership first; then assign Surface. Never invent `fullstack`.

## Status state machine

```
needs-triage → needs-info → ready-for-agent → claimed → resolved
                              ↑                ↓
                         readiness READY   ready-for-human → needs-info
```

- Drafts from `/plan-prd` start at **`needs-info`**
- Only **`ticket-readiness-reviewer`** READY → **`ready-for-agent`**
- `/ship-ticket` sets **`claimed`** (AC frozen)
- Stop conditions / fix-cap → **`ready-for-human`**
- Success → **`resolved`**; PRD when archived → **`shipped`**
- Do **not** use orphan labels like `done` on new tickets

## Closing the last ticket (mandatory archive)

When the **final** open issue for a PRD increment is resolved:

1. Every issue is `resolved` (or `wontfix` with reason)
2. `/livingdocs-record` if behaviour changed
3. Move tree to `.scratch/archive/<feature-slug>/`
4. Set PRD `**Status:** shipped`
5. Fix Parent links; remove empty active feature dir
6. Update archive README / map files if the repo uses them

Do not archive while any issue is still `claimed`, `ready-for-agent`, or open.

## Comments

Append conversation under `## Comments`. Thread redirects must be folded into Decisions (currency / C10).
