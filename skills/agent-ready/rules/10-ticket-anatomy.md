# 10 — Ticket anatomy

The canonical body of a delivery ticket. Order is fixed: an agent skims top-down and must hit
the constraints **before** it hits the instructions.

Each section states **what it answers** and **the test it must pass**. A section that cannot
pass its test is filler — fix it, or the ticket is not ready.

Section names are a convention, not a law. What is graded is the content
(`checklists/readiness-gate.md`), not the headings.

---

## 1. Summary

**Answers:** what changes, in outcome terms.
**Test:** a reader who knows the product can restate the change without opening the body.

- Outcome, not mechanism: *"Stop listing sold-out variants in search results"* beats
  *"Fix VariantFilterResolver"*.
- Prefix only with a convention the team actually uses. Do not invent prefixes, and remove
  scratch ones.
- No internal identifiers that mean nothing outside your notes.

## 2. Goal / Problem

**Answers:** who is blocked, and what "done" looks like **from the outside**.
**Test:** contains an observable end-state, and one concrete example.

- 1–3 sentences, plus a worked example with real values: a URL, a payload, a rendered string,
  an error message.
- End with an explicit **`Done means:`** clause. This is the sentence the agent measures itself
  against when the criteria get long.
- No implementation jargon here.

## 3. Context

**Answers:** which anchors a cold reader needs to orient.
**Test:** every line is an anchor a stranger would otherwise have to hunt for.

Affected market, customer, tenant or segment; the parent item; the source (a support ticket, a
thread, a QA run); the environment; the deadline. Nothing else. Context is not a narrative.

## 4. Current state — the state table

**Answers:** what already exists, and what this ticket does to each piece.
**Test:** every row has a real locator **and** a verb.

The highest-leverage section in the standard. Write it as a table:

| Role | Where | Action |
| --- | --- | --- |
| Duplicate config UI (10 fields) | `src/settings/LegacyConsentPanel.*` | **Remove** |
| Event bridge consumers depend on | `src/consent/emit.*` | **Keep and complete** |
| Second injector writing the same global | `src/vendor/ConsentInjector.*` | **Retire** |
| Damage normaliser | `src/catalog/normalisers/Damage.*` | **Add** (does not exist yet) |

Legal actions: **Keep**, **Keep and complete**, **Add**, **Remove**, **Retire**, **Retarget**,
**Do not touch**.

Rules:

- Split **what exists** from **the gaps this ticket owns**. The gap list is the work.
- Name the **precedent** an agent should copy from, and why it is the right one. Precedent beats
  prose; the wrong precedent is how an agent writes plausible, unidiomatic code.
- List the **tests that will need updating**, by path, plus the searches that find stragglers
  (`grep` for the removed symbol).
- Say what must stay green. *"Keep the existing fallback suite passing"* is a constraint an
  agent can honour; *"don't break anything"* is not.
- For work that is not code — copy, configuration, templates, data — the locator is the
  template, setting, record or surface. The rule is the same: name it precisely enough to find.

## 5. Decisions (do not reopen)

**Answers:** which forks are closed, and on whose authority.
**Test:** zero open forks; every decision names its source.

- Number them. Write them as assertions, not discussion.
- Each decision carries its **source**: a person's answer, a thread, a live payload, prior
  behaviour, a linked item, a regulation, a metadata call.
- **Supersede explicitly.** If the original text is now wrong, say so: *"the criterion naming
  channel `X` is superseded by the two-channel mapping below, including its typo"*. Silent
  correction gets re-litigated by the agent.
- Anything here is off-limits to the implementing agent. It may not "improve" a decision.

## 6. Assumptions

**Answers:** what you filled in where evidence was missing.
**Test:** each assumption is falsifiable and says what happens if it is false.

The honest half of Decisions. Separate them so a reviewer can attack them cheaply. If an
assumption turning out false would change the implementation, it belongs in **Open questions**
instead.

## 7. Implementation hypothesis

**Answers:** the concrete seam, named in plain English, plus the ordered steps.
**Test:** no verb like "adjust", "handle", "improve", "align" without a named artifact.

- Numbered steps. Each step: the artifact, the operation, and the **position** — *"registered in
  the pipeline immediately after the image normaliser and before the equipment one"*.
- Include the **traps**: a cast that turns absent into zero, a trim that eats meaningful
  whitespace, a coercion that fabricates an empty row, a test asserting a hard-coded count that
  must move. These separate a ticket the agent completes from one it half-completes.
- Name the **contract shapes** an output must match — exact keys, exact event names, exact
  configuration keys. Paste verbatim anything a machine compares.
- State ownership boundaries when two layers could do the job.
- A tiny contract that *is* the decision — a state machine, an event table, a payload shape —
  belongs here. A code dump does not.
- Prescribe the observable result, not the craftsmanship. Leave the agent room on the seam.

## 8. In scope / Out of scope

**Answers:** the edges.
**Test:** every out-of-scope line kills a plausible over-read, and names who owns it.

- In scope: the deliverables, including tests.
- Out of scope: the things a competent agent would *reasonably* also do. Each with a
  destination — another item, "deferred", or "never". A bare "out of scope: X" with no owner
  invites the agent to do it anyway.
- Include the do-not lines this codebase has earned.

## 9. Stop conditions

**Answers:** when the agent must halt and ask rather than decide.
**Test:** each one names a detectable trigger and a concrete action.

Format: `If <detectable condition>, stop and <action>.`

> If the upstream payload does not separate external from internal descriptions, stop, expose a
> single combined field, document the real keys beside the mapping, and flag it on the ticket.
> Do not invent categories.

A ticket with genuine unknowns and good stop conditions is **more** agent-ready than one that
pretends the unknowns do not exist.

## 10. Blast radius

**Answers:** where the diff may and may not reach.
**Test:** a reviewer can predict the changed-file list from this section.

Modules, packages, templates, configuration, data, tests. Say explicitly where the diff must
**not** reach.

## 11. Acceptance criteria

See `rules/40-acceptance-criteria.md`. Checkbox list, Given/When/Then, observable.

## 12. Proof plan

**Answers:** how the agent proves it is done before a human looks.
**Test:** specific enough to execute without asking anyone.

- Commands from `docs/agents/shipyard.md` **Agent profile** (`proof_commands`), with the
  narrowing filter where one exists.
- Fixtures to add, by case: full / partial / empty / boundary.
- Manual verification naming an environment, a real entity, and the expected observation.
- Preconditions: what to disable or seed so the right thing is being proven.
- Do not invent a gate the project does not have. If there is no automated one, say so and give
  the manual check instead.

## 13. Dependencies

**Answers:** what must land first, and what this unlocks.
**Test:** real keys, correct direction, consistent with the tracker's link graph.

`Blocked by:` / `Blocks:` / `Relates:` with real keys **and their current state**. If the body
and the links disagree, say so here.

## 14. Risks

**Answers:** how a plausible, competent implementation still goes wrong.
**Test:** each risk is specific to this change, not generic engineering advice.

Races, caching and multi-tenant leakage, an admin-vs-public leak, a filter that overwrites
user-managed data, a rule that must never be bypassed.

## 15. Open questions (only if any remain)

Numbered. Each one: the question, whether it blocks, and a **recommended default**. Mark each
`BLOCKING` or `NON-BLOCKING`.

A ticket with an unanswered `BLOCKING` question is never marked ready.

---

## Optional: References

Specs, documentation, live payload URLs, regulation articles. Only links actually consulted.
