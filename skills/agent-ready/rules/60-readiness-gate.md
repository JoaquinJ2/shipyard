# 60 — The readiness gate

The gate decides `READY` vs `NEEDS_MORE_INFO`. In shipyard, `READY` is what authorizes
`**Status:** ready-for-agent` on a delivery issue under `.scratch/<feature>/issues/`.

## Who runs it

**Not the author.** Run the gate in a **fresh context** — a separate agent, a separate session,
or a human who did not write the ticket. An author reviewing their own ticket scores the intent
they remember, not the text on the page.

## What the reviewer gets

- the ticket **body**;
- the **discussion thread**;
- the **links and states** of this item and everything it names;
- the repository, and the pass number.

Not the drafting conversation, and not the author. If the reviewer has to ask the author a
question to score the ticket, the answer is already `NEEDS_MORE_INFO`.

**The thread is an input for detecting contradiction and currency, never for supplying missing
specification.** A path, decision or requirement that exists only in a comment does not count as
present: the reviewer sees the thread, the implementing agent gets the body.

## The gate

Score `checklists/readiness-gate.md`.

- **CORE — 10 items, blocking.** Any NO → `NEEDS_MORE_INFO`.
- **ADVISORY — everything else.** Reported, never fatal on its own.
- **`N/A` is a legal answer** and is not a NO.

The split is deliberate. CORE tests whether the ticket is **decidable**; advisory tests whether
it is **tidy**. A gate that fails a decidable ticket on formatting gets routed around within a
month, and then it protects nothing.

## What CORE tests, in one line each

| | |
| --- | --- |
| C1 Outcome | can a reader state what changes and what "done" is? |
| C2 Located | does every touched thing have a real locator and a fate? |
| C3 No consequential forks | is the agent ever left to choose something observable? |
| C4 Empty semantics | is absent / null / zero / empty defined? |
| C5 Stop conditions | does every admitted unknown have a halt? |
| C6 Observable criteria | can done be checked from outside the code? |
| C7 Executable proof | is there a real command, or a real manual check? |
| C8 Self-contained evidence | is the spec readable without opening an image? |
| C10 Current | has the thread superseded the body? |
| C9 The 95% question | what would the agent still guess, and is it covered? (roll-up) |

C3 is about **consequential** forks — an output contract, a scope boundary, a data shape, copy,
which surfaces are affected. Latitude over the seam is fine and wanted; pushing authors to
over-specify the HOW is its own failure mode.

## Automatic failures

A cheat sheet, not an eleventh gate — every line maps to a CORE item and **adds no new item**.
Any one of these fails the ticket outright:

- No external "done" — the body only describes a mechanism. *(C1)*
- **A verb with no artifact** — "adjust the module", "align the behaviour", "improve the
  handling". *(C2)*
- An unresolved fork in Decisions, Implementation hypothesis or Scope. *(C3)*
- The body asks a question instead of stating a decision — *"could you check this and, if it's
  not useful, remove it?"* is an intake, not a ticket. *(C3)*
- Acceptance criteria missing, unobservable, or only restating the HOW. *(C6)*
- The specification depends on an image, attachment or design frame a text-only reader cannot
  open. *(C8)*
- The body specifies an approach the thread has since superseded. *(C10)*
- An agent would still have to re-derive existing behaviour by hand. *(C9)*

"The story makes sense" is not a pass.

## Outcomes

| Verdict | Consequence |
| --- | --- |
| `READY` | Zero CORE NOs. May be marked ready — delivery items only, never a parent, a spike, or a link-or-comment-only operation. Advisory findings are still written down. |
| `NEEDS_MORE_INFO`, pass < 3 | Author enriches — from code, from grounding, or from **one** human product question — then a new **fresh** review. Pass count is per ticket. |
| `NEEDS_MORE_INFO` at pass 3, **advisory only** | Ship without the ready marker. Append an `Agent-readiness gaps` section from the last review. No fourth pass. |
| `NEEDS_MORE_INFO` at pass 3, **still failing CORE** | Do **not** ship it as work. A ticket still not decidable after three passes is an intake, not a ticket: hand it back with the CORE failures, or reclassify it (`templates/request-intake.md`, or a spike). Shipping it unmarked just moves the guesswork to the next person. |

A ticket with only advisory findings is `READY`. Fix them in the same edit if they are cheap; do
not spend a pass on them.

## Review output format

Count **distinct located defects**, deduplicated across items — not item hits. Three forks in
one paragraph are three findings; one omission that trips both C5 and C9 is one. C9 is the
roll-up and never adds to the count.

```markdown
VERDICT: NEEDS_MORE_INFO (pass 2/3) — 3 core, 5 advisory findings

CORE FAILURES
- C3 §Implementation hypothesis: "resolve to empty (preferred) or a reused label" is an
  unclosed fork on the output contract.
- C5 §step 3: the agent is told to decide scope mid-implementation, with no stop condition.
- C10 §body vs thread: the decision-maker redirected this on <date> ("no capacity for an engine
  rebuild; handle it as a template configuration change"). The body still specifies the engine
  fix across six files.

ADVISORY
- N17: two linked items carry no state.
- N4: the summary still carries a scratch prefix.

WOULD STILL GUESS: whether the adjacent field is in scope, and what the sentinel emits.
```

The severity count matters: `0 core, 4 advisory` is half an hour of tidy-up; `7 core, 20
advisory` is a rewrite. A verdict that cannot tell those apart is not useful.

Findings are specific and **located** — section, quoted phrase, checklist id. "Needs more
detail" is not a finding.

## Marker discipline

- A ready marker (`**Status:** ready-for-agent`) is applied **only** after a fresh-context
  `READY` from `ticket-readiness-reviewer`.
- Never self-certified by the author, the `planner`, or the drafting agent.
- Whoever executes `/plan-work` (or alias `/plan-prd`) or `/refine-ticket` may not add the marker if the gate omitted it.
- Parents / PRDs / epics are never `ready-for-agent` for implementation — only delivery issues.
- At pass 3 with advisory-only failures: do **not** set `ready-for-agent`; append
  `## Agent-readiness gaps` and require explicit human confirm before `/ship-ticket`.
