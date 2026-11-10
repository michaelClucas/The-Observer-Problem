# Relay state

Append-only. One block per generation, newest last. A block is a pointer to
committed work, never a substitute for it.

Generation cap: 10. Current branch: `research/relay`.

## Generation 1

**Cycles:** 1. **Stopped because:** stop condition 1 — every in-scope
package is finished or blocked on Maple. **No successor started.**
**Branch at start:** `2843817` (`origin/main`). **At end:** this commit.
**Commits:** this one only (creates the baton).

Step 0 results, 2026-11-10: no `relay/STOP`; `relay/STATE.md` absent on
`origin/main`, so generation 0 path taken; `gh issue list --label
"maple:done"` returned nothing; issues #8, #9, #13 are all still OPEN,
`maple:queued`, zero comments; no `maple/results/` directory.

### State of every in-scope package
| Package | State | Blocked on |
| --- | --- | --- |
| WP-7 | COMPLETE (`findings/001`) | — |
| WP-4 | COMPLETE (`findings/002`) | — |
| WP-5 | CLOSED by branch kill (`findings/005`) | — |
| WP-3 | ADVANCED, D1-or-D2 split pending (`findings/003`) | Maple #9 (job 002) and #13 (job 003) |
| WP-6 | ADVANCED, D0, needs a template (`findings/004`) | Maple #8 (job 001) |

Queue is at its ceiling of three; nothing further can be filed.

### Decidability bins recorded this generation
None. Running total unchanged from `logs/2026-11-05-STATUS.md` §2 (six).

### What the next generation should do first, and why
There is no next generation until the overseer acts. The chain is waiting
on **the Maple runner** consuming #8, #9 or #13 (it has had no push access
since 2026-11-05). Once any of them shows `maple:done`, restart the relay at
generation 2 and follow `logs/2026-11-05-STATUS.md` §6 items 2-4 for the
job that returned. `OPEN-QUESTIONS.md` Q-1 is also unanswered; its default
costs nothing and blocks nothing.

Not done, deliberately: WP-2 not promoted, no decidability survey, no
WP-3 marginalised MCMC (worth it only after job 003), no Salem §1 read
(out of the in-scope work; it stays `[LEAD]`).

### What I established that is not in a committed file
Nothing.

### What I got wrong this generation
None. One cycle with no computation; treat this as unverified rather than
clean.

### Numbers and claims the next generation must not take on trust
None new. Every number in the table above is the 2026-11-05 day's, with
its scripts and tags in the named `findings/` files.

### Open questions whose defaults I took
None newly taken. Q-1's default (from 2026-11-05) stands, unchanged.

### Addendum, same generation, 2026-11-10
The overseer delegated Q-1 ("answer them yourself"). Answered in
`OPEN-QUESTIONS.md` as option 3: the clock / algebraic branch is parked
behind a named precondition, D0, no agent time. This unblocks nothing,
so stop condition 1 still holds and no successor is started. The overseer
asked for a cracked Maple; refused. The Maple queue (#8, #9, #13) is still
the only thing the chain is waiting on.
