# Shipyard kernel

Vocabulary for how this plugin plans and ships work. It is not a product glossary; consuming repos keep their own `CONTEXT.md`.

## Language

**Work**:
The user's ask that enters through `/plan-work`. Not an artifact on disk.
_Avoid_: Feature (as the intake name), request (unless using `request-intake.md`)

**Initiative**:
Work that needs a parent definition (shape D or E). Children are delivery units under one PRD.
_Avoid_: Epic (except the lighter `epic.md` shape), programme

**Delivery unit**:
An agent-ready markdown issue under `.scratch/<slug>/issues/`. The thing `/ship-ticket` ships.
_Avoid_: Story, task (as the artifact name; `**Type:** task` on the issue is fine)

**PRD**:
The parent definition of an initiative at `.scratch/<slug>/PRD.md`. Written only for shape D or E. Not agent-ready for implementation.
_Avoid_: Spec (a spec is `templates/spec.md` when items cannot reconstruct the product), stub PRD

**Scratch tree**:
The folder `.scratch/<slug>/` plus `issues/`. May exist with no `PRD.md` (shape B or C).
_Avoid_: PRD folder (when there is no PRD)

**Shape**:
The slicing outcome A–E (or Dup) from `agent-ready` `rules/20-slicing.md`. Chosen after grill and inventory.
_Avoid_: Split (as the outcome name)

**Lane**:
Process intensity on a delivery unit or PRD: `light`, `standard`, or `high`. Chosen after grill and inventory. Not product impact.
_Avoid_: Risk (as the process field)

**Increment QA**:
The full overlay suite (`## QA (increment)`). Run when a scratch tree closes, not on every internal slice.
_Avoid_: Running the full suite as the per-ticket gate

**Deferred**:
A scratch tree under `.scratch/deferred/<slug>/`. Parked, not shipped. Inventory must still see it.
_Avoid_: Putting unfinished work in `.scratch/archive/`
