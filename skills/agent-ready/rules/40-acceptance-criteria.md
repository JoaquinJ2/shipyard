# 40 — Acceptance criteria and proof

Acceptance criteria are the contract. They are the only part of the ticket that says,
unambiguously, whether the agent is finished.

## The three tests every criterion must pass

1. **Observable** — it describes something visible from outside the code: a rendered string, a
   status code, a payload field, an emitted event, a file that is or is not committed.
2. **Falsifiable** — there exists a concrete state of the world in which it is false.
3. **Not the HOW** — it does not restate the implementation. If deleting a criterion would not
   change what a reviewer checks, it is noise.

| Bad | Why | Fix |
| --- | --- | --- |
| `The pricing module is refactored` | not observable | `Given a cart with a expired promotion, the total shown excludes the discount` |
| `Add the normaliser to the pipeline` | restates the HOW | `Given an item with photos, the response exposes them in the gallery item shape` |
| `Handles edge cases` | not falsifiable | `Given an item with no data, the list is empty, the total is an empty string, and no placeholder row is rendered` |
| `Performance is acceptable` | no threshold | name the metric and the number, or drop it |

## Form

Checkbox list. Given / When / Then, in the product's own vocabulary.

```markdown
### Acceptance criteria

- [ ] Given a listing URL whose category segment is the "all categories" sentinel, when the
      title template renders the category variable, then the output is a single value or is
      omitted — never a comma-joined list of case variants.
- [ ] Given a real category slug, when the same template renders, then there is no regression.
- [ ] Given template text with leading or trailing spaces around a conditional, when the title
      is emitted, then those spaces survive.
- [ ] Given the existing sentinel fixtures, when the suite runs, then they still pass.
```

Every set must include:

- the **happy path** with real values;
- the **empty / absent** case — what is *not* rendered, emitted or fabricated;
- at least one **no-regression** criterion naming the behaviour or test it protects;
- a **negative** criterion when the ticket forbids something ("no new generated assets are
  committed"; "bindings outside the new panel are unchanged").

Keep it under ~8–10. More than 12 means the ticket needs slicing (`rules/20-slicing.md`).

## Exact strings

Anything a machine compares is pasted **exactly**, in code formatting, in a table when there are
several:

| When | Emit (exact name) | Channel |
| --- | --- | --- |
| measurement consent granted | `consent_given` | analytics queue |
| measurement consent granted | `ConsentGiven` | DOM event |
| marketing consent granted | `ConsentGivenAdvertising` | DOM event |

Add the near-miss warning when one exists: *"do not rename `consent_given` — it is not
`consent_giver`"*. Typos in event names ship, and they ship silently.

## Proof plan

Criteria say *what*; the proof plan says *how the agent shows it* before a human looks.

```markdown
### Proof plan

Commands (see docs/agents/shipyard.md Agent profile): <targeted test command with filter>, <type check>, <lint>.

Fixtures: full / partial / images-only / empty.
Update the suite that asserts the registered-handler count: 18 → 20.

Manual: on <environment>, open <entity with data> and <entity without data>; the section renders
for the first and is absent for the second.

Precondition: disable the background reconciliation job for the duration, or it will mask the
fix by correcting the data instead.
```

Rules:

- Commands must be **real and runnable in this project**. Take them from
  `docs/agents/shipyard.md` **Agent profile** (`proof_commands`) or the overlay QA list.
  Prefer machine-checkable criteria: a command that **fails on current base** and passes after.
  Never invent a gate the project does not have.
- Name the tests that will need updating, especially any asserting hard-coded counts.
- For anything user-visible, give an environment **and** an entity — a URL, a record id, an
  account.
- State preconditions where an unrelated job, cron or cache could mask the result. Without this
  the agent proves the wrong thing and everyone believes it.
- Where no automated gate exists, say so and give the manual check. "Unit tests cover it" is not
  proof.

## Verification walkthrough (large tickets)

For a ticket changing runtime behaviour across several surfaces, add a numbered **Verification**
walkthrough separate from the criteria: a script someone follows on a real environment, each
step with its expected observation. The criteria stay the contract; verification is the
reproduction.

## Marker discipline and AC freeze

Acceptance criteria are frozen when the ticket moves to `claimed` under `/ship-ticket`. Do not
silently edit AC mid-loop to make a failing proof pass — escalate to `ready-for-human` instead.
