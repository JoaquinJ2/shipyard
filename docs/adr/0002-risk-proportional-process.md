# Risk-proportional ship (lanes, reviews, QA)

Always-on security review, full QA per ticket, livingdocs per slice, and optional parallel writers on `/ship-prd` made small changes expensive without extra safety. We kept writer ≠ reviewer, author ≠ gate, frozen AC, loop caps, and CORE.

**Lane** (`light` | `standard` | `high`) routes intensity. Security review is always-on only for `high`; otherwise it follows the diff. Ticket QA uses `proof_commands`; increment QA runs when a tree closes. Livingdocs records at contract close (last ticket or no-PRD tree). `/ship-prd` runs **one writer at a time** on the increment branch — worktrees were rejected as fragile (especially on Windows/OneDrive).

Unfinished trees go to `.scratch/deferred/`; `.scratch/archive/` is shipped only.
