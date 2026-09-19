# Triage and ship labels (shipyard)

Canonical status strings for `.scratch/` PRDs and issues. Write them as `**Status:** <label>` near the top of the file.

## Planning / triage

| Label | Meaning |
| --- | --- |
| `needs-triage` | Maintainer has not evaluated the item yet |
| `needs-info` | Drafting or refining; waiting on answers or CORE fixes. **Default after `/plan-work` draft.** |
| `ready-for-agent` | Fresh `ticket-readiness-reviewer` READY. Delivery issues only — never a PRD/epic for implementation. |
| `ready-for-human` | Stop condition, product decision, or fix-loop cap — needs a human |
| `wontfix` | Will not be actioned (reason required in body) |

## Ship lifecycle

| Label | Meaning |
| --- | --- |
| `claimed` | `/ship-ticket` started; AC frozen |
| `resolved` | Ticket shipped (Answer appended) |
| `shipped` | PRD archived after all issues resolved |

## Mapping from Matt roles

| Matt role | Shipyard label |
| --- | --- |
| needs-triage | `needs-triage` |
| needs-info | `needs-info` |
| ready-for-agent | `ready-for-agent` (only after readiness gate) |
| ready-for-human | `ready-for-human` |
| wontfix | `wontfix` |

## Forbidden on new tickets

- `done` — use `resolved`
- Self-setting `ready-for-agent` without a fresh readiness verdict
- Marking a PRD `ready-for-agent` as if it were implementable work
