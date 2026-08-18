---
name: frontend-surfaces
description: UI implementation workflow. Read design-system first; stop on DS gap; follow overlay stack (Vite/React/shadcn if those packs are on); manual QA 375/768/1280 light+dark; stack skills ecc-react-patterns and ecc-vite-patterns.
---

# Frontend surfaces (this repo)

Workflow for implementing product UI in `src/routes/`, `src/components/`, and `src/styles.css`.

## When to use

- `Surface: frontend` tickets
- Fixing copy or chrome findings routed from `copywriter` or `designer` review
- Any change to user-visible layout, components, or token usage in `src/`

## On start, read (in order)

1. Ticket + parent PRD under `.scratch/<feature>/`
2. `design-system/MASTER.md` and relevant `design-system/pages/*.md`
3. `.cursor/skills/design-system/SKILL.md` — token and control rules
4. `.cursor/skills/copy-voice/SKILL.md` — Spanish copy checklist
5. `CONTEXT.md` — glossary for labels and messages
6. Stack: `.cursor/skills/ecc-react-patterns/SKILL.md`, `.cursor/skills/ecc-vite-patterns/SKILL.md`
7. Matt `/implement` and `/tdd` (global)

## Read design system first — stop on gap

Before writing UI:

1. Confirm every token, radius, shell rule, and control variant you need is documented in MASTER or a page override.
2. If a piece is **missing** (new color, layout chrome, control variant, page-specific rule) → **stop** and hand back to orchestrator for a `designer` / `Surface: design-system` ticket. **Do not invent** tokens or components.
3. If MASTER and `src/styles.css` disagree, flag it — do not silently pick one.

## Stack

Read `docs/agents/shipyard.md` for this repo's surfaces. When `react` + `vite` packs are on, typical defaults:

- **Vite** + React — not Next.js App Router unless the overlay says otherwise
- **shadcn / Radix** primitives under `src/components/ui/` when that tree exists — extend, don't replace with ad-hoc markup
- Server data and forms: follow patterns already in the repo (do not introduce a new data layer)

## Manual QA (when ticket or PRD requires it)

Check **375 / 768 / 1280** viewports in **light and dark**:

- No unintended horizontal page scroll
- Shell and navigation usable on narrow widths
- Overlays match tokens in both themes
- Touch targets remain tappable on mobile

No visual-regression suite unless a ticket adds tests at a seam.

## Workflow

Follow Matt **`/implement`** → **`/tdd`** at pre-agreed seams only. Run `npx tsc --noEmit` before handoff.

**Stop before** `/code-review`, commit, or `/livingdocs-record` — orchestrator runs those after review.

## Related

- Rules: `.cursor/rules/design-system.mdc`, `.cursor/rules/copy-voice.mdc`, `.cursor/rules/react-coding-style.mdc`
- Agent: `frontend-developer`
- DS specs: `designer` owns `design-system/**`
