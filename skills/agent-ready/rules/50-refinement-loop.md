# 50 — The refinement loop

How a raw request becomes an agent-ready ticket.

## The loop

```
raw intake
  → 1 ground        (read the code / API / live environment — no writing yet)
  → 2 inventory     (duplicates, parents, related, closed-but-recurring)
  → 3 draft         (anatomy, rules/10)
  → 4 open questions (what you could not close)
  → 5 answers       (a human or new evidence closes them)
  → 6 fold          (answers become Decisions; questions disappear)
  → 7 gate          (rules/60 — READY or NEEDS_MORE_INFO)
  → 8 publish       (only after explicit human approval)
```

Maximum **3 passes** through 3–7 per ticket. What happens at pass 3 depends on what is still
failing — see `rules/60`.

## 1. Ground before you write

Refinement without grounding is fan-fiction. Before drafting, collect:

- the **code state**: the relevant modules, the precedent files, the tests, the current ordering,
  the current counts;
- the **live state** where the behaviour is observable: the failing URL, the real payload for a
  real entity, what a real page actually loads;
- the **history**: the closed item that already tried this, what its fix actually covered, and
  why the problem is back;
- the **tracker graph**: real blockers versus what the text claims.

Then state the grounding explicitly: checkout, commit, version, environment. If you could not
see something — attachments, production data, a private service — say so in a **Limitation**
line. A refinement that hides its blind spots is worse than one that names them.

## 2. Two legal output forms

**(a) Replace the body**, and post a comment containing:

- a one-line note that the body was replaced by a refinement pass;
- a **refinement summary** paragraph;
- the **Decisions** and **Assumptions** that changed the meaning;
- the original body, **verbatim**, under its own heading.

Use this when the body itself was the problem.

**(b) Leave the body, post a refinement comment** with the full refined content
(`templates/refinement-comment.md`). Use this when the body is someone else's artefact you
should not overwrite, or when the refinement is a proposal awaiting a decision.

Never do (a) without preserving the original. Never do (b) and then silently edit the body too.

## 3. Open questions are a deliverable

A good refinement *ends* in questions. Each one:

```markdown
1. **Upstream shape (BLOCKING).** Does the source separate external from internal descriptions,
   or is it one combined list? Recommended default: if not clearly separated, ship a single
   combined field and do not invent categories.
```

- numbered, so answers can cite them;
- marked `BLOCKING` or `NON-BLOCKING` — this is what the gate reads;
- each with a **recommended default**, so silence still leaves a path forward;
- never more than about six. If you have twelve, the ticket is not refinable yet — say that
  instead of pretending it is a ticket.

## 4. Answering questions is a structured act

The answer is not a chat reply. It is a document that closes forks
(`templates/open-questions-answer.md`): per question, the evidence, the ruling, and the
mechanical rule the implementer follows.

> **1. Upstream shape — the keys are separate. Keep them separate.**
>
> | Source key | Observed value | Maps to |
> | --- | --- | --- |
> | `descriptionsExternalList` | `""` — an empty **string**, not an empty list | `descriptionsExternal` |
>
> **Ruling:** keep them separate; the prior system stored the same two keys.
> **Implementer rules:** empty string, null, missing or wrong type → empty list. **Do not**
> cast the empty string to a list — that yields a list containing an empty string and
> fabricates a blank row.

The shape: **evidence → ruling → implementer rule → the trap to avoid.**

## 5. Fold answers back into the body

Answers living only in comments are how knowledge gets lost. Once a question is answered:

- move the ruling into **Decisions**, with its source;
- move the mechanical rule into **Implementation hypothesis**;
- delete the question from **Open questions**;
- add a criterion if the answer created a new observable behaviour.

The thread stays as the audit trail. The body stays the contract.

## 6. Direction corrections

Sometimes refinement discovers the ticket is aimed at the wrong target. Write a **direction
correction** comment, dated, with:

1. what you checked — code, prior system, a live environment, with the URL;
2. the **evidence** — what actually loads, the real configuration values, real payloads;
3. why the current direction cannot work — an access nobody has, a duplicated runtime, a
   constraint the plan ignores;
4. the **agreed target**, numbered;
5. what happens to the existing children: which stay, which get rewritten.

Then stop. Rewriting the parent and children is a separate, approved act.

## 7. What refinement must never do

- Invent a decision the business has not made and present it as settled.
- Delete the reporter's original words.
- Quietly resolve a contradiction between two sources — name both and rule explicitly.
- Change the kind of an item, or merge two disciplines into one, on its own authority.
- Mark a ticket ready on its own judgement — that is the gate's call (`rules/60`).
