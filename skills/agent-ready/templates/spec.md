# Template — spec

Use only when a future reader cannot reconstruct the product from the items alone
(`rules/20-slicing.md` §Spec). A spec is a **definition** artifact; parent items and tickets
remain **tracking**. They are not the same thing, and a spec replaces neither.

A spec contains no implementation steps, no locators, no commands. If it does, it has become a
ticket and should be split.

---

# <Title>

**Status:** draft | agreed | superseded by <…>
**Owner:** <name>   **Date:** <…>   **Supersedes:** <…>

## 1. Problem

<The situation, the cost of leaving it as is, and who bears that cost. Evidence, not assertion:
numbers, items, accounts, regulation articles.>

## 2. Who this is for

| Persona | What they need | What they do today instead |
| --- | --- | --- |
| <…> | <…> | <…> |

<Name the conflicts between personas explicitly — those conflicts are why this document exists.>

## 3. Outcomes and success

- <Outcome, in the user's terms.>
- **Measured by:** <metric, current value, target, how it is observed.>

## 4. Policy and rules

<The rules that outlive any single item: obligations per segment, gating, precedence when two
rules collide, exact locked copy. This is the section tickets will cite.>

| Rule | Applies to | Source | Precedence |
| --- | --- | --- | --- |
| <…> | <…> | <…> | <what it overrides> |

## 5. Scope

**In scope:** <capability-level, not task-level.>
**Out of scope:** <with the reason and the owner.>
**Explicitly deferred:** <with the condition that would bring it back.>

## 6. Decisions

| # | Decision | Alternatives rejected | Why | Reversible? |
| --- | --- | --- | --- | --- |
| D1 | <…> | <…> | <…> | yes / no / costly |

## 7. Open questions

| # | Question | Blocks | Owner | Default if unanswered |
| --- | --- | --- | --- | --- |
| Q1 | <…> | <…> | <…> | <…> |

## 8. Glossary

<Opinionated terms, one or two sentences each, with the synonyms to avoid. A shared vocabulary
is most of what a spec buys you. Mirror durable terms into `CONTEXT.md`.>

## 9. Delivery map

| Slice | Delivers | Tracking | Depends on |
| --- | --- | --- | --- |
| <…> | <…> | <KEY> | <…> |

<The map only. The items own their own detail.>

## 10. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
