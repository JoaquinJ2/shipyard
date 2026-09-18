# Anti-patterns

Each of these has cost a real run somewhere. Search a draft for the left column.

## Language that hides a fork

| Phrase | What the agent does | Write instead |
| --- | --- | --- |
| "adjust the X module" | searches, guesses, edits the wrong seam | the file, the function, the position |
| "handle edge cases appropriately" | invents a rule | the empty / null / zero table |
| "align with the existing pattern" | copies the nearest file, which may be the wrong precedent | name the precedent |
| "improve / optimise / clean up" | unbounded diff | the observable outcome and the boundary |
| "as needed", "if applicable", "where relevant" | decides for you | state the condition |
| "should probably" | treats it as optional | decide, or make it an Open question |
| "etc." | truncates the contract | finish the list, or say the list is open and why |

## Structural failures

- **The thin ticket.** A planning proposal ("create: summary + criteria bullets") pasted as the
  body. The proposal is the operations list; the body is the product.
- **Template theatre.** Every heading present, every heading empty. Worse than fewer headings,
  because the gate can be passed without saying anything.
- **The invented locator.** A plausible path that does not exist and is not declared as new.
  Costs a full agent run.
- **The rotted fact.** "Currently 18 handlers", "in the next sprint", "the new API". Pin it with
  a date and source, or phrase it durably.
- **Two disciplines, one body.** Design and delivery, or delivery and investigation. Two owners,
  two definitions of done, neither satisfied.
- **The unlinked dependency.** The body says "blocked by X"; the tracker says nothing. Or the
  reverse.
- **State theatre.** Marked ready while its blockers are untouched.
- **The silent supersede.** The refinement fixes a wrong criterion without saying the old one was
  wrong, so the agent implements both.
- **Borrowed vocabulary.** Importing another product's headings or artifact names, so the agent
  looks for things that do not exist in this codebase.
- **Over-specification.** Prescribing the seam so tightly that the agent cannot write idiomatic
  code and the reviewer cannot improve it. Pin the observable; leave the craft.

## Acceptance-criteria failures

- Criteria that restate the implementation steps.
- No empty/absent case — the single most common source of fabricated placeholder data.
- No no-regression criterion on a change inside a shared code path.
- "Performance is acceptable" with no metric and no threshold.
- A criterion that can only be checked by reading the diff.

## Refinement failures

- Refining without grounding — no commit, no live check, no payload.
- Hiding blind spots instead of writing a Limitation line.
- Deleting the reporter's original words.
- Resolving a contradiction between two sources by picking one silently.
- Ending with twelve open questions instead of saying the ticket is not refinable yet.
- Answering an open question in chat and never folding it into the body.
- Self-certifying the ticket as ready.

## Bug-specific failures

- No "why this is not <the similar item>". Two bugs with identical symptoms and unrelated causes
  is the normal case, not the exception.
- Treating a returning symptom as a new discovery instead of an incomplete fix.
- A remediation that depends on an unverified branch, with no diagnosis precondition.
- QA notes that let an unrelated job mask the fix.
- A production workaround with no verification query and no "do not set this field" warning.

## Slicing failures

- Splitting by layer as a reflex.
- One ticket containing an unblocked slice and a blocked slice, with no line between them.
- A parent opened when a suitable one is already open.
- A spec written because the workflow has a spec step.
- Slicing so thin that a slice cannot be verified on its own.

## Currency failures — the expensive ones

These produce a ticket that **passes review and still sends the agent to build the wrong
thing**. They are invisible to anyone reading only the body.

- **The stale body.** The body specifies approach A. Three comments down, the decision-maker
  said "no capacity for A — handle it as B". Nobody edited the body. The agent builds A.
- **The unanswered escalation.** The thread ends on "so whose is this?" and nobody replied.
  Ownership is unsettled and the ticket is being treated as ready.
- **The invisible workaround.** Someone already patched it by hand — in a config, in production
  data, in a template. The agent ships a second, conflicting fix.
- **Spec-by-screenshot.** The only statement of the requirement is an image an agent cannot
  open. Complete to a human reviewer, empty to the implementer.
- **Scratch prefixes that outlive the scratch.** If the summary was never cleaned, assume the
  body wasn't either.
- **State theatre, part two.** In progress with no acceptance criteria at all. The gate was
  never run.

## Gate failures

Ways the review itself stops working:

- **Formatting as a blocker.** Failing a decidable ticket because its current-state section is a
  bullet list rather than a table, or because it lacks a literal phrase. Reviewers route around
  a gate like this within a month.
- **No `N/A`.** Forcing a NO on dependencies for a ticket that genuinely has none. The reviewer
  starts lying, and then every verdict is noise.
- **A verdict with no severity.** `NEEDS_MORE_INFO` that cannot distinguish thirty minutes of
  tidy-up from a rewrite tells the author nothing about what to do next.
- **Unscoreable items.** "Known traps are named" — known to whom? An item nobody can falsify is
  decoration.
- **Self-certification.** The author, or the agent that drafted the ticket, declaring it ready.
