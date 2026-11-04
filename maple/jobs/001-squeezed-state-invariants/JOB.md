# Job 001 - Invariants of the squeezed inflationary state, exact and truncated

**Round trips: 1.** No gates; independent of job 002. Queue on day one.

## What is computed

For a single Mukhanov-Sasaki mode on a de Sitter background, the covariance
matrix of the two-mode squeezed vacuum, and its symplectic invariants,
computed twice:

1. **Exactly**, from the full mode function.
2. **Truncated**, by dropping the decaying mode — the step the standard
   squeezing-implies-classicality argument actually takes — at successive
   orders in `x = k*eta`.

The quantities reported are `det(sigma)`, the symplectic eigenvalues, and
the Robertson-Schrodinger deficit

    Delta_RS = det(sigma) - 1/4            (hbar = 1)

which is zero for a pure state and negative for an object that is not a
legitimate quantum state at all.

## Why

This adjudicates a live `genuine_conflict` in the map with no published
reply, recorded in `runs/01-consolidate-approaches-2026-11-04/OUTPUT.md`
§2.3 as `D1 <-> D5`.

- **D1** (Polarski & Starobinsky 1996, arXiv:gr-qc/9504030) establishes
  statistical equivalence of the perturbations to a classical stochastic
  field by setting the decaying mode to zero. The run records this as a
  *choice*, and the authors label it "decoherence without decoherence".
- **D5** (Hsiang & Hu 2022, arXiv:2112.04092, doi:10.3390/universe8010027)
  claims the argument rests on technical errors: that leading-order-only
  approximations discard quantum contributions and produce unphysical
  results, specifically violated Wigner-function bounds, negative
  eigenvalues, and a violated Robertson-Schrodinger relation for a pure
  state.

D5 attacks D1's **validity**, not its scope. If D5 is right, D1's record
rule is invalid as stated rather than merely restricted, and a position
much of Cluster D rests on needs restating. The run found **no published
reply**. This computation is self-contained enough to settle the specific
technical claim without waiting for one.

It is also the cheapest validation of the whole symbolic pipeline, because
the exact answer is known in advance and is forced by a one-line identity
(see the independent check below).

## Expected output form

Six blocks, printed with the labels given, each an exact symbolic
expression in `x` (and in `r` where the squeezing parameterisation is
used), with no floating point anywhere:

```
[1] WRONSKIAN:        <expression>          expected: I  (or -I by convention)
[2] DET_EXACT:        <expression>          expected: 1/4, independent of x
[3] SYMPEIG_EXACT:    <list>                expected: [1/2, 1/2]
[4] DET_TRUNC(n):     <expression per n>    for n = 0, 1, 2
[5] DELTA_RS(n):      <expression per n>    = DET_TRUNC(n) - 1/4
[6] LEADING_ORDER:    <power of x, sign>    first nonvanishing term of DELTA_RS
```

A result is only usable if block [1] returns the Wronskian constant and
block [2] returns exactly `1/4`. Those two are the pipeline check; if
either fails, nothing after it means anything and the job is wrong rather
than the papers.

## The expected answer, cross-checked before queueing

**These values were verified in sympy 1.14.0 before this job was written**
(`crosscheck.py`, committed beside `job.mpl`, reproducible with the stack
in `../../../docs/RESEARCH-PLAN.md`). The Maple run is independent
confirmation in the designated CAS, against a stated target rather than
into the dark — which is what the protocol's expected-output rule is for.

```
[1] WRONSKIAN:     2*I unnormalised;  N = sqrt(2)/2;  I after normalising
[2] DET_EXACT:     1/4                exactly, independent of x
[4] DET_TRUNC(0):  0                  DELTA_RS(0) = -1/4
[4] DET_TRUNC(1):  x^4/144 + x^2/12 + 1/4
                                      DELTA_RS(1) = x^2*(x^2+12)/144
[4] DET_TRUNC(2):  x^8/2304 + x^6/288 + x^4/36 + x^2/12 + 1/4
                                      DELTA_RS(2) = x^2*(x^6+8*x^4+64*x^2+192)/2304
```

**The structure of the answer matters more than the numbers**, and it is
not what was guessed before computing it. The truncations fail in **two
opposite directions**:

- **n = 0**, the literal "set the decaying mode to zero", gives
  `det = 0`. The covariance matrix is **degenerate**: zero phase-space
  area, one symplectic eigenvalue zero. That is not a quantum state, and
  it violates Robertson-Schrodinger maximally.
- **n = 1 and n = 2** overshoot: `DELTA_RS > 0` for all `x != 0`, so
  `det > 1/4`. That is permitted for a *mixed* state but wrong for a state
  the construction asserts is pure, and the excess vanishes only as
  `x -> 0`.

Only the exact mode gives `1/4`. So the truncation is never a pure state at
any order examined, which is the substance of D5's objection.

**One precision worth keeping.** D5 is reported as claiming *negative*
eigenvalues. What the n = 0 case actually produces is a **zero** symplectic
eigenvalue, not a negative one. The violated uncertainty relation is
confirmed; "negative eigenvalues" is not, and may refer to a different
quantity in their paper, such as a partial-transpose eigenvalue or a
Wigner-function value. The Maple run should report the eigenvalues
explicitly so this stays distinguishable, and the write-up must not
upgrade "zero" to "negative".

## What would be surprising or wrong

**Surprising, and it would mean the cross-check is wrong rather than the
papers:** any departure from the table above. Blocks [1] and [2] are forced
by the Wronskian identity, so a disagreement there is a convention slip in
one of the two implementations and must be resolved before the rest is
read.

**Surprising in a way that would matter:** `DELTA_RS(n) = 0` for some
`n >= 1`, meaning purity is exactly restored at a finite truncation order.
Then the standard argument has a legitimate stopping point and D5's
objection is much weaker than stated. Nothing in the cross-check suggests
this, but Maple reaching it would be the single most informative
disagreement available from this job.

**Wrong rather than surprising:** `DET_EXACT` depending on `x`, or the
Wronskian not constant. Both mean the mode function or the momentum
convention is wrong, not that anything has been learned. The most likely
cause is the momentum variable: see the note in `job.mpl`.

**Not settled by this job, and the job must not be read as settling it:**
whether statistical equivalence suffices for definiteness of outcomes.
Run 01 resolved that separately and cleanly — the primary sources decline
definiteness themselves — and no determinant computed here speaks to it.
This job is only about whether the truncation is a legitimate state.

## Independent check

Two, both doable by hand:

1. **The Wronskian forces the answer.** For any exactly normalised mode
   function, `v v'* - v* v' = i` is equivalent to `det(sigma) = 1/4`. So
   block [2] is not a discovery; it is the normalisation restated, and it
   must come out exactly. This is what makes the job a pipeline test.
2. **The unsqueezed limit.** Setting the squeezing to zero gives the vacuum
   with `sigma = I/2`, `det = 1/4`, symplectic eigenvalues `[1/2, 1/2]`.

## Inputs

None. The mode function is written into `job.mpl` from the standard de
Sitter form and the job is self-contained.

## Status

**Written but not executed.** Maple is not installed on the machine where
this job was authored, so the code is untested and may contain syntax
errors or convention slips. The runner should expect to fix small things;
`NOTES.md` is where any fix goes, and a fix that changes the mathematics
rather than the syntax makes this job 003 instead.
