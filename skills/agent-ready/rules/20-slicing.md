# 20 — Slicing and structure

Decide the **smallest** structure that matches how the team actually delivers. Structure is a
consequence of evidence, never of aesthetics.

## Inventory first — it is a constraint, not a hint

Before proposing any shape, search `.scratch/` (and the product issue tracker if the repo uses
one) for duplicates, near-duplicates, candidate parents and related work.

| Inventory result | Required response |
| --- | --- |
| **Duplicate** of the same WHAT | Refine the existing item, or link as duplicate. Never create a parallel one. |
| **Near-duplicate** | Refine, with an explicit scope delta stated in the body. |
| **Candidate parent exists** | Attach as a child. Do not open a second parent for the same initiative. |
| **Related but distinct** | Create only if it is a real delivery unit. Always propose the links. |
| **Closed match** | Decide reopen-vs-new **with a rationale in the body**. Never silently recreate. |
| **Nothing found** | Choose a shape below, and say what you searched for. |

A closed item whose problem came back is evidence of an **incomplete fix**, not a new discovery.
Say so in the body and link it — it changes how the agent scopes the work.

## Choose one outcome

| Code | Shape | When |
| --- | --- | --- |
| **A** | Refine an existing item | The work belongs on something that already exists |
| **B** | One new item | Self-contained; attach the parent if inventory found one |
| **C** | Several items | Independent delivery units; add links only when real |
| **D** | Parent + children | A genuine initiative **and** no suitable open parent exists |
| **E** | Spec + items | Complexity needs a *definition* artifact; items stay *tracking* |
| **Dup** | Link, no create | Same WHAT already tracked |
| — | Ask | A human product fact still blocks the structure |
| — | No action | Not defined, not viable, or the ask was inventory only |

A spec and a parent item are **not** the same thing. Do not call something a spec unless it is
one, and do not assume an initiative needs one.

## Reasons that justify a split

Split only when at least one is true. Otherwise prefer A or B.

1. **Blocked-ness** — part of the work is unblocked today and part waits on something else.
   *The highest-value split and the most often missed.* If the data layer can start now but the
   interface work waits on a design still unstarted, those are two slices, and the ticket must
   say which is which.
2. **Domain** — different bounded problems, different vocabularies.
3. **Delivery unit** — separately demoable or releasable.
4. **Dependency** — one piece must land before another; record the link.
5. **Risk** — isolating a risky integration or migration.
6. **Ownership** — different teams or disciplines. Design deliverables and delivery never share
   a ticket.
7. **Convention** — confirmed in the project's own history, not assumed.

## Anti-rules

- Do not split reflexively by layer (backend / frontend / design system). Vertical slices are
  **one** option, not the default. Prefer split by **blocked-ness**, then by **independently
  verifiable proof** (observable behaviour), then by ownership.
- Do not create items to fill pretty categories.
- Do not open a parent because the idea "feels big".
- Do not write a spec because your workflow has a spec step.
- Do not slice below the point where a slice is independently verifiable.
- Do not split a defect into "investigate" + "fix" unless the investigation has a real,
  separately valuable output.

## Surface after slice (shipyard)

`Surface:` is **routing metadata**, not a slicing reason.

1. Justify the split (blocked-ness / proof unit / ownership / …).
2. Assign **exactly one** `Surface:`: `backend` | `frontend` | `design-system` | `tooling`.
3. If the slice still needs two writers, the slice is wrong — split again by blocked-ness or
   ownership (e.g. design-system before frontend). **Never** invent `Surface: fullstack`.
4. Record one line in the ticket: `## Why this is a separate ticket` naming the split reason.

Omit `frontend` / `design-system` when overlay `visual: off`.

## Sizing heuristic

A slice is the right size when:

- its `Done means:` sentence is one sentence;
- its acceptance criteria fit in ~8 checkboxes;
- its state table fits on one screen;
- an agent can run the proof plan without waiting on another human.

If the criteria cross 12, or the body contains two unrelated "done" states, split.

## Dependency direction

Write dependencies from this item's point of view, with state. Prefer shipyard paths:

```
Blocked by: 01 (resolved — DS tokens), 02 (needs-info — catalog API)
Blocks:     04 (frontend list — waits on this)
Relates:    .scratch/archive/foo/issues/03-….md (resolved — pattern to extend)
```

Or ticket numbers under the same `.scratch/<feature>/issues/` tree. Then **verify** `Blocked by`
fields and Status values agree across files. A mismatch is a finding you report, not a detail
you smooth over.

## Spec — when one is actually warranted

Write a spec only when a future reader **cannot reconstruct the product from the items**:

- several personas with conflicting needs;
- policy or legal rules that outlive any single item;
- a platform-level change whose rationale would be buried in a comment;
- a decision record that must survive the items closing.

A spec is not a parent-item description dump, and not a place for implementation steps.
Shape: `templates/spec.md`.

## Output of a slicing decision

State, in one short paragraph: the outcome code, why, which inventory class drove it, and
**what you refused to split or refused to create, and why**. The refusals are the part that
stops the same debate next week.
