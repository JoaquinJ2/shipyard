# Template — answering open questions

An answer is a document that closes forks, not a chat reply. One block per question, numbered to
match. See `rules/50-refinement-loop.md` §4.

---

## Answers to open questions (<what you verified against>)

Verified against <module / codebase>, <prior implementation>, and <live service or environment,
with address>.

---

### <n>. <Question restated as a ruling.>

<Evidence first. A table when the evidence is data:>

| Source key | Observed value | Maps to |
| --- | --- | --- |
| `<key>` | `<literal observed value — note the type>` | `<target field>` |

**Ruling:** <the assertion>

**Implementer rules:**

- <rule>
- **Do not** <the trap>: <why it breaks>.

<Then, if relevant, what this supersedes and what it unblocks.>

---

### <n+1>. <Next question.> **<Short verdict: Yes / No / Option C.>**

…

---

## Recommended sequence

1. **Now:** <…>
2. **After that lands:** <…>
3. **After <KEY>:** <…>

## Proof

Commands: <…>. Fixtures: <cases>.
