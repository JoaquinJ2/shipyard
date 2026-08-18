---
name: design-system
description: Design system capture and maintenance. Generate/update MASTER via ui-ux-pro-max --design-system --persist anchored to src/styles.css; when to write design-system/pages/; Do/Don't for tokens and branded controls.
---

# Design system (this repo)

Owns `design-system/**` specs. **Do not redesign the brand** — mirror what already exists in `src/styles.css` and feature docs.

## When to use

- Creating or updating `design-system/MASTER.md`
- Adding `design-system/pages/<route>.md` overrides
- `/plan-prd` UI step (designer writes specs before frontend tickets)
- `Surface: design-system` tickets
- Reviewing UI diffs for token/chrome drift (designer reviewer axis)

## On start, read

- `src/styles.css` — `:root`, `.dark`, `@theme` (canonical token source until MASTER is updated)
- `features/ui-responsive/ui-responsive.md` — shells, breakpoints, full-bleed
- `features/ui-branded-controls/ui-branded-controls.md` — `SelectField`, overlay scrim, no native `<select>`
- Global `ui-ux-pro-max` skill — **invoke only**; do not duplicate in-repo

## Generate or update MASTER

Use the global skill's persist flow **anchored to existing tokens** (no invented palette, radius, font, or spacing):

```bash
python3 ~/.cursor/skills/ui-ux-pro-max/scripts/search.py \
  "fitness coaching app minimal Inter existing tokens" \
  --design-system --persist -p "the product"
```

After generation:

1. **Reconcile** `design-system/MASTER.md` with `src/styles.css` — every color, radius, font, and spacing in MASTER must exist in `:root` / `.dark` / `@theme`
2. **Map** documented tokens to CSS variables and Tailwind theme keys (e.g. `--primary` → `bg-primary`, `--radius` → `rounded-2xl` scale)
3. Document **Inter** as the app font (`--font-sans`, `--font-display`)
4. Document breakpoints from `ui-responsive`: manual QA at **375 / 768 / 1280**; Tailwind `md` 768, `lg` 1024; full-bleed mobile shells

Do **not** run persist to invent a new brand — edit MASTER to match the codebase.

## When to create `design-system/pages/`

| Create `pages/<slug>.md` | Use MASTER only |
| --- | --- |
| Layout or chrome differs from global rules (auth split, workout fullscreen, agenda week grid) | Standard shell pages that follow MASTER |
| Token usage override for one route (intentional `max-w-md` dialog rail, etc.) | Shared components with no page-specific deviation |
| `/plan-prd` or ticket explicitly calls for a page spec | One-off UI that still fits global tokens and shells |

Page files **override** MASTER for that route; they must not introduce tokens absent from `src/styles.css`.

## Branded controls (from `ui-branded-controls`)

- Dropdowns: `SelectField` (`pill` | `default` | `plain`) — **never** native `<select>` in product UI
- Overlays (Dialog, Sheet, Drawer): scrim `bg-foreground/50`, panel `bg-card` + `border-border`, dialog `rounded-2xl`, drawer top `rounded-t-3xl`
- Empty select: `placeholder` and/or `__none__` sentinel — never `SelectItem` with `value=""`

## Do / Don't

| Do | Don't |
| --- | --- |
| Use semantic tokens (`bg-card`, `text-muted-foreground`, `border-border`) | Loose hex (`#fff`, `#1a1a1a`) or arbitrary `oklch(...)` in components |
| Use `--radius` scale (`rounded-2xl`, `rounded-3xl` per MASTER) | Invent new radius values per component |
| Use `bg-foreground/50` for modal scrims | `bg-black/80` or other template overlay defaults |
| Use `SelectField` for product dropdowns | Native `<select>` |
| Stop and spec in `design-system/` when a token or control is missing | Patch `src/` with undocumented values (`frontend-developer` must not invent) |

## Related

- Rule: `.cursor/rules/design-system.mdc`
- Agent: `designer` (writes `design-system/**`; reviews UI diffs in separate launch)
- Implementation: `frontend-developer` reads MASTER + pages before coding UI
