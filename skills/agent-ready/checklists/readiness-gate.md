# Readiness gate checklist

Run in a **fresh context** by someone who did not write the ticket (`rules/60-readiness-gate.md`).

Two tiers:

- **CORE (10 items) — blocking.** Any NO fails the ticket. They test *decidability*, never format.
- **ADVISORY — non-blocking.** Findings that go in the review output and shape the severity
  count, but do not on their own fail the ticket.

Every item may be scored **YES / NO / N/A**. `N/A` is a legitimate answer and is not a NO — a
ticket with no dependencies scores those items `N/A`. Forcing a NO where `N/A` is true is how a
gate stops meaning anything.

## Reviewer inputs

The body, the discussion thread, the links and states, the repository, the pass number. Not the
drafting conversation, and not the author.

**The thread is read to detect contradiction and currency (C10, N2) — never to supply missing
specification.** If a locator, a decision or a requirement exists only in a comment, the body
fails C2 or C3.

## Counting findings

The severity count is **distinct located defects**, deduplicated across items — not item hits.
Three forks in one paragraph are three findings; one omission that trips both C5 and C9 is one.
**C9 is the roll-up and never adds to the count.**

---

## CORE — blocking

- [ ] **C1 · Outcome.** A reader who knows the product can restate, from the body alone, what
      changes for a user and what state means "done". *(A `Done means:` sentence is the easy way
      to pass, not the only way.)*
- [ ] **C2 · Located.** For every piece of the system this ticket touches, the body says what
      happens to it, named precisely enough to find: a path or symbol for code; a template,
      setting, record or surface for configuration, copy and data work. Anything that does not
      yet exist is declared as created here. *(A table is the easy way to pass; a bullet list
      carrying the same information passes too. It must be in the **body** — a locator that
      lives only in a comment is a NO.)*
- [ ] **C3 · No consequential forks.** The body never leaves the agent to choose something
      **observable**: an output contract, a scope boundary, a data shape, user-visible copy, or
      which surfaces are affected — unless that choice is an explicit Open question with a
      recommended default and a stop condition. Watch for `or`, `either`, `if it turns out`,
      `evaluate`, `assess`.
      *Latitude over the seam is fine and wanted.* "Delete or shrink the class", "whichever hook
      is cleanest" are **not** failures when the criteria pin the observable result.
- [ ] **C4 · Empty-value semantics.** For every field, event or section the ticket introduces,
      absent / null / empty string / empty collection / zero behaviour is defined, and it is
      explicit whether anything is ever fabricated.
- [ ] **C5 · Stop conditions.** Every unknown the body admits — an upstream contract not yet
      confirmed, a seam not yet chosen, a key list marked "historically" — has a
      `If <detectable condition>, stop and <action>` beside it. An unknown with no halt is a
      guess waiting to happen.
- [ ] **C6 · Observable criteria.** Acceptance criteria exist, are observable from outside the
      code, and at least one covers the empty/absent case and one covers no-regression.
- [ ] **C7 · Executable proof.** The ticket says how done is proven, specifically enough to
      execute without asking: a real command, **or** a named environment + a named entity + the
      expected observation. "Unit tests cover it" is not proof.
- [ ] **C8 · Self-contained evidence.** Everything the specification depends on is **readable as
      text**. No requirement lives only in a screenshot, an attachment, a design frame or a
      temporary blob URL. Colours, copy, layouts and payloads referenced by an image are
      transcribed.
- [ ] **C10 · Current.** The body reflects the latest decision in the discussion thread. If
      someone with authority redirected the ticket in a comment, the body says so and says what
      it supersedes. A body contradicted by its own thread is not untidy — it is wrong, and it
      is the most common way a well-formed ticket sends an agent to build the wrong thing.
- [ ] **C9 · The 95% question.** Write the answer to: *"If an agent picked this up right now with
      no access to the author, what would it still have to guess?"* — and every item in that
      answer is covered by a stop condition.

C9 is the gate and the roll-up. If C1–C8 and C10 pass and C9 still names an uncovered guess,
the ticket is not ready. C9 never adds to the severity count.

---

## ADVISORY — findings, not failures

*Ordered roughly by how often each one actually fires. Skim from the top.*

### Currency and hygiene

- [ ] **N2** No fix for this problem is already live as a manual workaround or another item's
      deploy. If one is, the body says what it covers and what remains.
- [ ] **N3** State and markers are consistent with the body: nothing marked ready that fails
      CORE, nothing in progress with no acceptance criteria, nothing marked ready while every
      blocker is untouched. **A NO here is escalated, not just recorded** — name it in the
      review's first line so someone moves the item or stops the work.
- [ ] **N4** The summary carries no scratch prefix (`TEST`, `DRAFT`, a personal tag) and no
      internal identifier that means nothing outside the author's notes.

### Grounding

- [ ] **N5** What exists is separated from the gaps this ticket owns.
- [ ] **N6** A precedent is named for each substantial new artifact.
- [ ] **N7** Tests needing updates are listed, including any asserting hard-coded counts.
- [ ] **N8** Load-bearing or contestable claims about current behaviour cite evidence — a commit,
      a version, a URL, a payload, a query. *(Not every line of the state table.)*
- [ ] **N9** Known traps are named where the author knew one: casts, trims, coercions, defaults,
      counts.
- [ ] **N10** Exact strings are pasted verbatim for anything a machine compares.

### Boundaries

- [ ] **N11** Out of scope pre-empts the obvious over-read, and each item names an owner — an
      item key, deferred, or never.
- [ ] **N12** The do-not list covers destructive moves this area has already suffered.
- [ ] **N13** Decisions the agent may not make are stated where they apply.
- [ ] **N14** One owner, one kind of work: design deliverables, delivery and open-ended
      investigation ("evaluate the impact on X") do not share a body.
- [ ] **N15** Assumptions are separated from decisions, and each says what happens if it is false.
- [ ] **N16** Where the refinement corrected the original text, it says so explicitly.

### Graph and verification

- [ ] **N17** Dependencies use real keys with current state.
- [ ] **N18** Body dependencies and tracker links agree — or the mismatch is reported.
- [ ] **N19** Inventory is visible in the body: the duplicate, parent, related or
      closed-but-recurring item is named, or the body says none was found.
- [ ] **N20** Preconditions are stated where an unrelated job, cron or cache could mask the
      result.
- [ ] **N21** Negative criteria exist where the ticket forbids something.
- [ ] **N22** The body is in the project's ticket language, and the Problem carries no
      implementation jargon.

### Size — a split signal, not a failure

- [ ] **N23** Acceptance criteria ≤ ~10.
- [ ] **N24** One "done" state, not two.
- [ ] **N25** The current-state section fits on one screen.
- [ ] **N26** The agent can run the proof plan without waiting on another human.

Three or more NO here → **recommend** a split (`rules/20-slicing.md`). The recommendation is a
finding; it does not by itself fail the ticket.

---

## Verdict format

```
VERDICT: NEEDS_MORE_INFO (pass 2/3) — 3 core, 5 advisory findings

CORE FAILURES
- C3 §Implementation hypothesis: "empty (preferred) or a reused label" is an unclosed fork on
  the output contract.
- C5 §step 3: the agent is told to decide scope mid-implementation, with no stop condition.
- C10 §body vs thread: redirected on <date>; the body still specifies the superseded approach.

ADVISORY
- N17: two linked items carry no state.
- N4: summary still carries a scratch prefix.

WOULD STILL GUESS: whether the adjacent field is in scope, and what the sentinel emits.
```

`READY` is: zero CORE NOs. Advisory findings still get written down — they are the next pass's
cheap wins, and they are what keeps the standard honest.
