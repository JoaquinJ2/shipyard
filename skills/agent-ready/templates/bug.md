# Template — Bug

A bug is agent-ready when the agent can reproduce it, knows which layer owns it, and knows which
adjacent fix would mask it.

---

## Environment

- Environment: <URL or name>
- Exact failing address or entity: <URL, id, account>
- Build / version / commit: <…>
- Affected segment: <market, tenant, plan, provider>
- Related: <KEY> — <same class of issue? previously closed? see "Why this is not X">

## Steps to reproduce

1. <step, with the real value or address>
2. <step>
3. <step — say if it is intermittent, and how many attempts it took>

## Expected result

- <observable, specific>

## Actual result

- <observable, specific — status codes, payload fields, rendered strings>
- <what happens next: recovers / stays broken / desyncs>
- <exact error copy, verbatim>

## Evidence

<Requests and responses, payload excerpts, log output, screenshots described **in words**.
Paste the actual strings — an agent cannot search a paraphrase, and cannot open an image.>

## Technical notes

<What the evidence implies about the mechanism. Name the layer: routing, mapping, template
configuration, a background job, caching. Name the likely seam — and say it is a hypothesis if
you did not confirm it.>

## Why this is not <related KEY>

<The highest-value section in a bug report. Spell out the difference in **trigger**, not in
symptom. Two bugs that look identical can have unrelated causes; without this, the agent
"fixes" it by waiting for the other item's deploy.>

<If the related item is closed and the symptom is back: say the earlier fix was incomplete, and
what exactly it did and did not cover.>

## Diagnosis precondition

<When the remediation depends on which branch is true, require the diagnosis first:>

> Before any code change, run <query / check> on <environment>.
> - Branch A — <condition> → <remediation A>
> - Branch B — <condition> → <remediation B>

## Impact

- Users: <who sees it, how often>
- Data / compliance / discoverability: <…>
- Test suites: <what stays flaky until this is fixed>

## Out of scope

- <the adjacent defect that belongs elsewhere> → **<KEY>**

## Acceptance criteria

- [ ] Given <the reproduction above>, when <action>, then <the expected result>.
- [ ] Given <the sibling case that must keep working>, then no regression.
- [ ] Given <the masking job / adjacent fix> is disabled, then the fix still holds.
- [ ] A regression test covering <the exact failing input> is added at `<path>`.

## Notes for QA

<How to prove *this* fix rather than an adjacent one. Name what to disable — a scheduler, a
cron, a cache — what to mutate, and what to restore afterwards.>

## Workaround (if one is being applied in production)

<The exact steps, in a transaction where applicable, with the verification check before and
after. Say explicitly what must NOT be set, and why.>
