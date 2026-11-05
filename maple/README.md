# Maple jobs

Symbolic computation runs on a different machine, under a different
account, with roughly one turnaround per day. Maple is therefore a **batch
service**, not a tool anyone calls interactively, and the plan is shaped
around that: see the round-trip budget in `../docs/RESEARCH-PLAN.md`.

This convention is shared with the sibling repository
`michaelClucas/Timescape-Experiment`. Changes to it belong in both.

## Layout

```
maple/
  README.md                  this file
  jobs/NNN-<slug>/
    JOB.md     what is computed, why, the exact expected output form,
               and what result would be surprising or wrong
    job.mpl    self-contained, no network, no interactive input,
               runnable with one command, printing results in the
               stated format
    inputs/    any data the job needs, committed
  results/NNN-<slug>/
    RESULT.txt verbatim Maple output
    META.yaml  Maple version, machine, date, operator, runtime
    NOTES.md   the runner's notes, including any error
```

## Running a job

    maple -q jobs/NNN-<slug>/job.mpl > results/NNN-<slug>/RESULT.txt

`-q` suppresses the banner. A job that needs anything else says so in its
`JOB.md`. Create the results directory, save the output verbatim, fill
`META.yaml`, and write `NOTES.md` even when the run was uneventful — "ran
clean, 41 s" is a useful note.

## Rules

**Results are append-only**, like runs. A committed `RESULT.txt` is never
edited. If a job was wrong, fix the job as a new number and leave the old
result and its notes in place; the wrong answer and the reason it was wrong
are part of the record.

**A job states its expected output form before it runs.** This is the rule
that does the work. If `JOB.md` cannot say what a correct answer looks
like, then a wrong answer would not be recognisable, and the job is not
ready to queue. Writing that section is usually where an underspecified job
falls apart, which is the point.

**A job states what would be surprising.** Not a prediction to be defended
— a tripwire. If the result matches a published value the job was built to
reproduce, the pipeline is validated; if it does not, either the job or the
paper is wrong, and the job says which checks distinguish those.

**A job is self-contained.** No network, no interactive input, no reliance
on a worksheet left open. One command, from a clean Maple. Any data it
needs is committed under `inputs/`, with its provenance in `JOB.md`.

**Floating point is declared.** A job that leaves exact arithmetic says
where and why, and states the precision used. A symbolic result that
silently became numeric is not a symbolic result.

**Every job names an independent check where one exists.** A limit that
reproduces a known case, a special value computable by hand, a
dimensional-consistency test. A result with no independent check is
reported with that stated.

## What belongs here, and what does not

Maple is for symbolic derivation: mode equations solved in closed form,
covariance matrices and their invariants, series expansions, spectral
indices extracted from an asymptotic limit, algebraic identities that a
paper asserts without showing.

Maple is **not** for:

- **Numerical likelihood fitting.** That is Python, with the stack recorded
  in `../docs/RESEARCH-PLAN.md`. A daily round trip is the wrong cadence
  for a sampler.
- **Operator-algebraic structure.** Type classification of von Neumann
  algebras, crossed products, modular theory. Maple has no natural handle
  on these, and a plausible-looking Maple manipulation of them would be
  worse than nothing. See the plan's note on why the clock-spectrum
  question is a literature read and not job 001.
- **Anything whose answer is a yes/no about what a paper says.** Read the
  paper.

## The queue is GitHub issues

Jobs are dispatched as issues labelled `maple`. The repository is the
record; issues are only dispatch.

| Label | Meaning |
| --- | --- |
| `maple:queued` | ready to run, the runner picks these up |
| `maple:running` | claimed by the runner |
| `maple:blocked` | specified but not runnable yet, and the issue says why |
| `maple:done` | result committed under `maple/results/` |

File one with the **Maple job** issue template, which refuses a job whose
`JOB.md` lacks an expected output form.

**The spec never goes in the issue body.** An issue body can be edited
after the fact and carries no sha, so it cannot be the record of what was
run. The issue names a job directory and a commit sha; the runner checks
out that sha. Where the issue body and `JOB.md` disagree, `JOB.md` at that
sha wins.

Queue order comes from the issue's **Blocks** field: a job blocking a work
package outranks one blocking nothing, then lowest job number first.

An issue is closed by the commit that adds its results directory. An issue
closed with nothing under `maple/results/` looks exactly like work that was
done, and is not.

The runner is an agent on the machine that has Maple. Its standing brief is
`RUNNER.md` in this directory, written to be handed over whole. The short
version of it: run the job exactly as written, bring back exactly what came
out, and never fix a job that looks broken.

## Ready jobs


| Job | Status | Round trips | Gates |
| --- | --- | --- | --- |
| `001-squeezed-state-invariants` | **ready**, sympy cross-checked | 1 | nothing; independent |
| `002-cosmic-variance-floor` | **ready**, sympy cross-checked | 1 | nothing; independent |
| `003-power-spectrum-corrections` | **ready**, sympy cross-checked | 1 | nothing; the mode equations were read 2026-11-05 |

001 and 002 are ready and independent, so they queue together on day one.

**003 was written on 2026-11-05**, after the three papers it needs were
read at primary source level as LaTeX source: `arXiv:1906.04405` for the
CSL third-order ODE, its source function and `alpha_k`, `beta_k` in both
epochs; `arXiv:1801.09949` for the open-EFT correction; `arXiv:1207.2086`
for the two-branch validation target. The equations are reproduced in full
in its `JOB.md`, so the job stands on what was read and not on what the
papers were reported to say.

The structural fact that makes it well-posed was not known when this file
said the job could not be specified: **both corrections are the same
third-order ODE for `P_vv` with the same free-theory Green function, and
differ only in the source function.** The common parameterisation WP-3
needs is therefore a consequence rather than a fitted ansatz, and what
Maple is asked for is the super-Hubble asymptotics of one integral per
source plus the degeneracy structure of the parameter maps.

Its validation target is the published set of spectral indices: `m = -1`
(MV 2020, inflation crossing, `n_S = 0`), `m = -10` (MV 2020, radiation
crossing, `n_S = -9`), `m = 3` (MVP 2012's non-scale-invariant branch,
`n_S = 4`), and `m_D = p + 2n - 7` with scale invariance at `p = 7 - 2n`
(MV 2018).

Nothing in the plan blocks on more than one round trip per day.
