# Template — refinement comment

Posted on an item you refined, whether or not you rewrote the body. See
`rules/50-refinement-loop.md`.

Pick one opening depending on what you did.

**(a) You replaced the body:**

> A refinement pass reworked this item's requirements and **replaced the description** with a
> refined context document. The original description is preserved verbatim at the bottom of this
> comment.

**(b) You left the body alone:**

> Refinement pass <n>/3. The description is unchanged; the refined content is below for review.

---

## Refined summary

<One paragraph: what this item now means, in outcome terms, after refinement.>

## Problem statement

<Who is blocked, what is true today, and what changes. Include the prior mechanism and say which
part of it is kept as an outcome and which part is replaced.>

## Proposed solution

<Split by slice, and mark each blocked or unblocked — usually the most useful thing a refinement
produces.>

### <Slice A> (unblocked)

<Concrete artifacts, positions, contract shapes, traps.>

### <Slice B> (blocked on <KEY>)

<What must exist first, and exactly what will be done once it does. What must NOT be done in the
meantime.>

## Decisions

- **<Assertion.>** Source: <…>. Supersedes: <…>.

## Assumptions

- <Falsifiable assumption.> If false: <consequence>.

## Acceptance criteria

1. Given <…>, when <…>, then <…>.

## Technical notes

**Verified** (<commit / version / environment>): <what you actually checked and found.>
**Implementation pointers:** <precedents, tests to add, commands to run.>
**Dependencies / graph mismatch:** <what the text claims vs the links vs the states.>
**Risks:** <specific to this change.>

## Out of scope

- <…> → <owning KEY / never>

## Open questions

1. **<Question> (BLOCKING | NON-BLOCKING).** Recommended default: <…>.

---

**Limitation:** <what grounded this refinement and what it could not see — attachments,
production data, a private service, a missing document.>

### Previous description

<the original, verbatim — only in form (a)>
