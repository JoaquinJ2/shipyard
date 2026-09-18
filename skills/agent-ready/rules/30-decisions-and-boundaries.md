# 30 — Decisions, boundaries and stop conditions

This is where the 95% comes from. Anatomy gives the ticket a skeleton; this file is what makes
it *decidable*.

## The decision-closure test

Read the ticket as the implementing agent. At every point where you could reasonably do two
different things, ask: **does the ticket tell me which?**

- Yes → fine.
- No, but it is an Open question with a default and a stop condition → fine.
- No → **defect**. Fix it before the ticket ships.

Run the test on: data shape, naming, empty and boundary behaviour, ordering, where code lives,
which layer owns presentation, error handling, what to do when an upstream source is missing,
and whether to touch adjacent code that looks wrong.

Apply it only to choices with **observable consequences**. A choice between two equivalent
seams, with the output contract pinned by the criteria, is latitude — leave it to the agent.
Over-specifying the HOW is its own failure mode: it produces tickets nobody can follow and
diffs nobody can improve.

## Closing a fork properly

A closed decision has four parts:

1. **The assertion** — written as fact, not discussion.
2. **The source** — a person's answer, a thread, a live payload, prior behaviour, a linked
   item, a regulation, a metadata call.
3. **What it supersedes** — the earlier text, criterion or item that is now wrong.
4. **The blast radius** — what else changes because of it.

> **A restoration cost of `0` counts as empty.** The previous interface used a truthiness check,
> so zero was hidden, and the derived "has damage" flag counts only values above zero.
> Normaliser: `<= 0` → absent. Output: empty string. Never render `0` or `"0"`.

Compare with the version that fails: *"handle zero cost appropriately."*

## Empty, null and boundary behaviour is a decision

The most expensive ambiguities are empty-value semantics. Every field you introduce needs an
explicit answer to:

- absent / null / empty string / empty list / zero — which of these count as "empty"?
- what is emitted for empty: nothing, an empty collection, an empty string, a hidden section?
- is a placeholder ever fabricated? (Almost always **no** — say it.)
- does a cast, coercion or default silently convert one into another? Name the trap. Casting an
  empty string to a list yields a list containing an empty string, and that is how a blank row
  appears in production.

## Drawing the boundary

Three layers, all required.

**In scope** — the deliverables, including tests and fixtures.

**Out of scope** — the plausible over-reads, each with an owner:

> - the derived flag and the formatter → **ABC-222**
> - the visibility condition → **ABC-226** (closed — do not re-add)
> - authoring the interface chrome → **ABC-228 / ABC-229**
> - changing bindings outside the new panel → **never**

**Do-not list** — the specific destructive moves this codebase has already suffered:

> - Do not strip existing bindings outside the new panel.
> - Do not patch third-party source in place.
> - Do not disable the whole integration to achieve a per-request skip.
> - Do not persist a request-scoped flag in a cookie or a shared cache key.

## Stop conditions

An agent's worst behaviour is confident invention under uncertainty. Stop conditions convert
that into a cheap, visible halt.

Shape: **`If <detectable condition>, stop and <action>.`**

- The condition must be **detectable by the agent while working**. "If the requirements are
  unclear" is not detectable. "If the response has no `descriptionsInternal` key" is.
- The action must be concrete: stop, document X beside the mapping, ship the reduced field set,
  flag it on the ticket. Not "ask the product owner".
- Cover at minimum: an upstream contract that differs from the one assumed; a precedent that
  does not exist; a proof command that cannot run; a choice that would require inventing a
  product rule. Escalate via overlay **Agent profile** `escalation.product` / `escalation.env`
  when the stop action is "ask a human".
- Every unknown the body itself admits — a key list marked "historically", a hook "to be
  chosen after inspection" — needs one beside it.

## Decisions the agent may never make

Say this out loud when it applies. The agent may **not** decide:

- user-facing copy, especially legally constrained copy — paste exact strings, or stop;
- which markets, tenants or segments a behaviour applies to;
- whether a compliance or safety gate can be bypassed;
- pricing, fee or rate semantics;
- whether to delete or migrate user data;
- how something behaves when a product rule is simply absent. That is a product answer.

## Risks vs stop conditions

Different, and both belong in the ticket.

- **Risk** = something that could make a *correct-looking* implementation wrong.
  → the agent should design against it.
- **Stop condition** = something that means the agent *cannot* proceed correctly.
  → the agent should halt.

A third-party script overwriting your callback is a Risk. An upstream API that does not expose
the field the ticket is built on is a Stop condition.
