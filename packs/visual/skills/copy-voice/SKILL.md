---
name: copy-voice
description: Spanish product copy checklist for this repo. Tuteo, CONTEXT.md glossary, length, errors/toasts/empty states, no structural emoji, no demo framing in new copy. Use when writing or reviewing visible UI strings.
---

# Copy voice (this repo)

Canonical checklist for product copy in `src/routes/`, `src/components/`, and related UI strings.

## When to use

- Writing or reviewing user-visible strings in TS/TSX
- `/ship-ticket` or `/review-diff` when the diff touches copy
- `/audit-ui` (copywriter axis)
- Planning UI tickets that introduce labels, errors, or empty states

## On start, read

- `CONTEXT.md` — domain glossary (canonical Spanish terms; `_Avoid_` lists)
- This skill — tone and checklist below

## Voice

- **Spanish** with **tuteo** (*tú*, not *usted*)
- Clear, direct, product voice — not internal/dev language
- Prefer glossary terms over anglicisms or synonyms marked `_Avoid_` in `CONTEXT.md`
- New product copy must not use **"demo"** framing (badges, placeholders, or copy that implies a sandbox session)

## Checklist

| Area | Rule |
| --- | --- |
| Glossary | Match `CONTEXT.md` (Usuario, Profesional, Empresa, Relación profesional, etc.) |
| Tuteo | Imperatives and labels address the user as *tú* (`Guarda`, `Elige`, not `Guarde` / `Elija`) |
| Length | Headings short; buttons 1–3 words when possible; helper text one idea per sentence |
| Errors | Actionable, human — what failed and what to do next; no stack traces or codes in UI |
| Toasts | Confirm outcome in plain Spanish; avoid jargon |
| Empty states | Say what is missing and the next step (CTA when relevant) |
| Emoji | No structural emoji in product UI (not as bullets, section markers, or status icons) |
| English | No English product strings — technical ids and code stay in code, not user copy |

## Examples

| Avoid | Prefer |
| --- | --- |
| `Save changes` | `Guardar cambios` |
| `Demo session` / badge "Sesión demo" in new copy | Product framing without demo language |
| `Error: fetch failed` | `No pudimos cargar los datos. Intenta de nuevo.` |
| `📋 Tu plan` | `Tu plan` |

## Related

- Rule: `.cursor/rules/copy-voice.mdc`
- Agent: `copywriter` (read-only review; `antes → después` per finding)
- UI implementation: `frontend-developer` applies copy fixes in `src/`
