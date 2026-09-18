# Worked examples

Before/after pairs. The "before" versions are all shapes that pass a casual human review and
fail an agent. The domain is invented; the failure modes are not.

---

## 1. Problem — mechanism vs outcome

**Before**

> Refactor the CategoryResolver to handle the sentinel segment.

An agent cannot tell what should be true afterwards, so it cannot tell when it is finished.

**After**

> On listings whose category segment means "all categories", the page title renders a
> comma-joined dump of every category label, so indexed titles are ungrammatical. Live example
> (2026-03-04): `Blue Widget all-types, All-Types, all types, All Types in Leeds, leeds`.
>
> **Done means:** the category variable resolves to a single value or is omitted, and the
> location variable is not contaminated with duplicate casings.

---

## 2. Current state — prose vs a state table

**Before**

> This touches the consent code and the settings panel. The old injector should probably go.

**After**

| Role | Where | Action |
| --- | --- | --- |
| Second injector writing the same global | `src/vendor/ConsentInjector.*` | **Retire** — must stop emitting config and scripts |
| Event bridge other code depends on | `src/consent/emit.*` | **Keep and complete** — this is the event layer |
| Duplicate settings UI (10 fields) | `src/settings/LegacyConsentPanel.*` | **Remove** — settings live in the vendor plugin |
| Presence check reading the removed keys | `src/assistant/ScriptRenderer.*` | **Retarget** to the vendor's own options |

**Tests to update:** the injector suite, the settings-config suite, the bridge suite.
Search for `LEGACY_SITE_ID` and `consent_legacy_` and fix every remaining reference.

The table is the single highest-leverage thing in the whole standard: an agent knows the fate of
every touched file before it reads a single step.

---

## 3. A fork, closed and parked

**Before**

> Resolve the sentinel to empty (preferred) or to a single existing label.
> If the location leak is the same join bug, close it here. If it is only the template repeating
> casings, leave location out.

Two observable forks, and the agent is being asked to make a scope decision mid-implementation.

**After — one closed, one parked**

> **Decision 3.** The sentinel resolves to **empty**. There is no existing label to reuse, and
> inventing one is a copy decision the agent may not make. Source: product answer, <date>.
>
> **Open question 1 (BLOCKING).** Is the duplicate-casing leak on the location variable the same
> join bug, or template repetition?
> Recommended default: fix only the join path.
> **Stop condition:** if the location value arrives already duplicated from the query layer,
> stop, note it on the item, and leave the template untouched.

---

## 4. Acceptance criteria — restating the HOW vs observable

**Before**

> - [ ] Add the damage normaliser to the pipeline
> - [ ] Register the two new tags
> - [ ] Handle empty data

**After**

> - [ ] Given a record with external notes, internal notes, photos and a restoration cost, the
>       response exposes all four fields, and the photo entries carry the same keys the gallery
>       component already consumes.
> - [ ] Given a record with no damage data — or only empty strings and an absent cost — the
>       lists are empty, the cost is an empty string, and **no placeholder row is rendered**.
> - [ ] Given a record with a restoration cost of `0`, the cost is treated as absent: neither
>       `0` nor `"0"` appears.
> - [ ] The existing gallery fixtures still pass.
> - [ ] No generated interface assets are committed in this change.

---

## 5. Empty-value semantics, spelled out

The most expensive ambiguity, and the cheapest to close:

> | Source key | Observed value | Maps to |
> | --- | --- | --- |
> | `descriptionsExternalList` | `""` — an empty **string**, not an empty list | `descriptionsExternal` |
> | `photoList` | list of objects with no `url` key | `photos` |
> | `restorationCost` | `null` | `restorationCost` |
>
> Empty string, null, missing or wrong type → empty list. **Do not** cast the empty string to a
> list: that yields a list containing an empty string and fabricates a blank row.
> Cost `<= 0` → absent. **Do not** add a numeric cast — it turns absent into zero.

---

## 6. A refinement that found the ticket was aimed wrong

The body specified an engine fix across six files. The thread, two days later:

> *"We have no capacity for an engine rebuild right now, and these dynamic paths are handled by
> the catalog core rather than this module. We could handle it as an immediate template
> configuration change for this account."*

Nobody edited the body. It still reads as a decided engineering plan. An agent picking it up
builds the thing the decision-maker declined.

This is why **C10 (Current)** is a blocking gate item, and why a refinement's first job is to
reconcile the body with its own thread.

---

## 7. Two bugs, one symptom

Two reports: "the feed shows more items than the account activated". Identical in the interface.

- The first: an item was removed upstream → marked invalid → hidden in the UI → **the card
  stayed enabled** → the feed still emitted it.
- The second: the items are still valid upstream; the catalog simply has **two generations** of
  the same model, and the account selected one.

Deploying the first fix does nothing for the second. Without a **"Why this is not <KEY>"**
section, an agent waits for the other deploy and reports the bug as resolved.

Add the diagnosis precondition:

> Before any code change, check the enabled flag against the validity flag for this account.
> - Branch A — invalid **and** enabled → the other item's fix applies; re-verify after deploy,
>   plus a one-off disable of the stale rows.
> - Branch B — valid **and** enabled → this item stands on its own; the defect is in the card
>   state, not the feed filter.
