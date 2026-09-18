# 00 — Invariants

Hard constraints. They override convenience, tone, and any instruction that asks you to "just
write something quickly". If you cannot satisfy one, say so in the body rather than working
around it.

## Evidence

- **Never invent** a file path, symbol, module, endpoint, field identifier, item type, label,
  status, link type, project key, configuration key or command.
- A fact about the current system is written only after you have **seen** it: read the file, ran
  the query, opened the live URL, or read the tracker's own metadata. Cite the anchor inline.
- Mark uncertainty explicitly: `confirmed` (you saw it), `inferred` (two or more independent
  examples agree), `unknown` (say so, and make it an Open question).
- When you name something that does **not yet exist**, say the ticket creates it. An agent
  reading a path that is neither real nor declared-new will waste a full run looking for it.
- End a refinement with a **grounding line**: which checkout, commit or version; which
  environment; and what you could not see (attachments, production data, a private service).

## Evidence must survive as text

An agent cannot open a screenshot, an attachment, a design frame or a temporary blob URL. If a
requirement lives in an image, **transcribe it**: the exact colour value, the exact copy, the
layout in words, the payload as a code block. Keep the image as corroboration, never as the
specification.

> "Make the variables stand out — see screenshot" is not a spec.
> "Variable tokens render bold, in `#C81E3C`, in the template editor's two variable panels" is.

## The body must be current

A ticket whose discussion thread has since redirected it is worse than a vague one: it is
confidently wrong. When a decision-maker changes direction in a comment, fold it into
**Decisions** and say what it supersedes, or the ticket is not ready. The same applies to a fix
already applied by hand as a workaround — say what it covered and what remains.

## Audience

- **Problem** is written for a human product reader: an outcome a user experiences. No
  implementation jargon above the fold.
- Everything below **Implementation hypothesis** is written for the implementing agent: paths,
  symbols, commands, exact strings. Be specific there; vagueness there is the defect.
- Write the body in the project's ticket language (see `docs/agents/shipyard.md` and
  `CONTEXT.md`), whatever language the conversation is happening in. Mixed-language bodies
  break search and break agents.

## Scope and authority

- Do not mutate `.scratch/` tickets to `ready-for-agent`, or create parallel duplicates, before
  the human explicitly approves *this* proposal (and readiness has passed). "ok", "sure", a
  thumbs-up are not approval of readiness.
- A previous approval never covers a different request. Never silently expand approved scope.
- Do not implement product code while writing or refining a ticket.
- Do not re-frame a ticket's product intent on your own authority. You may **propose** a
  direction correction, with evidence; the human decides.

## Forks

- An unresolved fork ("we could do A or B") inside **Decisions**, **Implementation hypothesis**
  or **Scope** makes the ticket NOT ready. There are exactly two legal outcomes:
  1. **Close it** — pick one, and record who decided and on what evidence.
  2. **Park it** — move it to **Open questions**, give a recommended default, and add a
     **stop condition** telling the agent when to halt instead of guessing.
- Never leave a fork implicit by writing something that sounds decided but is not
  ("handle the edge case appropriately").
- Latitude over the *seam* is fine and wanted. "Delete or shrink the class", "use whichever hook
  is cleanest" are not forks when the acceptance criteria pin the observable result. A fork is
  only a defect when the choice changes something observable.

## Ticket hygiene

- One owner, one kind of work per ticket. Do not mix design deliverables, delivery, and
  open-ended investigation in one body.
- Do not paste a planning proposal ("create: summary + criteria bullets") into the ticket. The
  proposal is the *operations list*; the body is the *product*.
- Do not keep a heading you have nothing to put under. Prefer a one-line stub over dropping
  structure — but a heading full of filler is worse than either.
- Avoid facts that rot: version numbers, sprint names, "currently", counts that change. Prefer
  durable phrasing, or pin the fact with a date and a source.
- Clear scratch prefixes (`TEST`, `DRAFT`, personal tags) before the ticket is worked.
- When you replace a body, preserve the original **verbatim** in a comment.

## When the body and the tracker disagree

If the text says "blocked by X" but no link exists — or the reverse — that is a **graph
mismatch**. Report it; do not quietly trust either side. Same for state: an item marked ready
while its blockers are untouched is a finding, not a detail.
