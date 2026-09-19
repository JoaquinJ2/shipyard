# Template — delivery item (feature / task / story)

Path: `.scratch/<feature>/issues/<NN>-<slug>.md`

Copy from the title down. Omit a heading only when it would be pure noise — prefer a one-line
stub over dropping structure. Rules: `rules/10-ticket-anatomy.md`.

---

# NN — <Title>

**Status:** needs-info
**Type:** task
**Surface:** backend | frontend | design-system | tooling
**Blocked by:** <NN, … or —>
**Risk:** low | medium | high

## Parent

[PRD](../PRD.md) or `—` if this tree has no PRD (shape B/C)

## Why this is a separate ticket

<One line: blocked-ness | proof unit | ownership | domain | risk | convention — not "because Surface".>

## Goal

<Who is blocked and what changes for them, 1–3 sentences, no implementation jargon.>

<Optional worked example with real values: a URL, a payload, a rendered string, an error.>

**Done means:** <one sentence, observable from outside>.

This item is self-contained. Implement it from the artifacts listed below.

## Context

- Affected: <market / tenant / customer / segment>   Provider or upstream: <…>
- Source: <support item, thread, QA run, AUDIT.md>
- Environment: <URL>   Deadline: <date or none>

## Current state

| Role | Where | Action |
| --- | --- | --- |
| <what it does today> | `<real locator>` | **Keep** / **Keep and complete** / **Add** / **Remove** / **Retire** / **Retarget** / **Do not touch** |

**Exists:** <what already works, with locators>
**Gaps this item owns:** <the work, with locators>
**Precedent to copy:** `<file>` — <why it is the right precedent>
**Tests that will need updating:** `<paths>`. Search for `<symbol>` and fix every remaining
reference.
**Must stay green:** `<test>` — <what it protects> (also see overlay Agent profile `must_stay_green`)

## Decisions (do not reopen)

1. **<Assertion.>** Source: <person's answer / thread / live payload <URL> / prior behaviour /
   ticket / regulation>. <What this supersedes in the original text.>
2. **<Assertion.>** …

## Assumptions

- <Falsifiable assumption.> If false: <what changes>.

## Implementation hypothesis

<One sentence naming the seam in plain English.>

1. **<Artifact>** — `<locator>`. <Operation.> <Position: after X, before Y.>
2. **<Artifact>** — `<locator>`. <Operation.>
3. **Traps:** <the cast / trim / default / hard-coded count that will silently break this.>
4. **Contract shapes:** <exact keys, exact names, exact values — paste verbatim.>

<Pin the observable result; leave the agent room on the seam.>

## In scope

- <deliverable>
- <tests / fixtures>

## Out of scope

- <plausible over-read> → **<owning ticket NN>** / deferred / never
- <destructive move this codebase has already suffered> → **do not**

## Stop conditions

- If <detectable condition>, stop and <concrete action> (set `ready-for-human`, comment on ticket,
  escalate via overlay Agent profile if needed). Do not <the invention to avoid>.
- None — no admitted unknowns. *(Only if literally true.)*

## Blast radius

`<module / package / area>` — <sub-areas>. <Where the diff must not reach.>

## Acceptance criteria

- [ ] Given <state>, when <action>, then <observable outcome>.
- [ ] Given <the empty / absent case>, then <what is not rendered, emitted or fabricated>.
- [ ] Given <existing behaviour>, then no regression / <named test> still passes.
- [ ] <negative criterion: what must NOT appear in the diff>.

## Proof plan

Commands (see `docs/agents/shipyard.md` Agent profile): <command>, <command>.
Fixtures: <full / partial / empty / boundary>.
Manual: <environment, entity, expected observation>.
Precondition: <what to disable or seed so the right thing is proven>.
Overlay QA still runs after the diff; this plan is what the writer runs before claiming done.

## Dependencies

- **Blocked by:** <NN> (<state> — <what it delivers>)
- **Blocks:** <NN> (<what it unlocks>)
- **Relates:** <path or NN> (<state> — <why related, and what it does not cover>)
- <Graph mismatch, if any.>

## Risks

- **<Risk name>:** <how a correct-looking implementation still goes wrong.>

## Open questions

1. **<Question> (BLOCKING | NON-BLOCKING).** <Why it matters.>
   Recommended default: <the fallback if nobody answers>.

## References

- <only links actually consulted>

## Readiness

<!-- Filled by ticket-readiness-reviewer — do not self-certify -->

## Plan

<!-- Filled at /ship-ticket Step 2.5 — files, tests, proof commands, will-not-touch -->

## Answer

<!-- Filled on resolve -->
