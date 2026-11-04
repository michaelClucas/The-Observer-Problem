# Job 002 - The cosmic-variance floor, as a triage instrument

**Round trips: 1.** No gates; independent of job 001. Queue on day one.

## What is computed

Closed-form expressions for the irreducible variance of three classes of
statistic measured on one sky, as a function of multipole `l`, sky fraction
`fsky`, and the underlying angular power spectrum `Cl`:

1. The **power spectrum** estimator `Chat_l`.
2. A **one-point** statistic: the amplitude of a sky-averaged signal.
3. A **three-point** amplitude, from the count of available triangles.

Then, from each, the **minimum detectable amplitude** at a stated
significance, which is the quantity the triage actually needs.

## Why

This builds the instrument, not a result. The research plan sorts each
observer-problem question into *decidable now*, *decidable in principle*,
or *floor-limited* by comparing a predicted difference `Delta` against two
numbers: current measurement error `sigma_now`, and the irreducible floor
`sigma_floor`. Without `sigma_floor` computed here, the third bin is a
matter of opinion, and the whole point of the triage is that it is not.

There is already one worked case waiting for it.
`runs/01-consolidate-approaches-2026-11-04/OUTPUT.md` §2.3 records the
causal-patch and fat-geodesic measures as a **"genuine_conflict that is
empirically idle"**: both predict a one-point expectation value for the
gauge-invariant Newtonian potential and a related three-point
contribution, the detailed forms differ between the measures, and **both
lie well within cosmic variance**. That verdict is currently cited from a
source, not computed in this repository. Once this job returns, it is ours,
and the same threshold applies to every other candidate observable without
further argument.

Run 01's open question 9 is the other reason. It asked whether cosmic
variance and the measure problem are conceptually linked, searched twice,
and found only that cosmic variance is treated as **the noise floor that
masks measure dependence**. That is not a link between the problems, but it
is exactly the relationship this job quantifies.

## Expected output form

Eight blocks, exact symbolic expressions, no floating point:

```
[1] CHI2_MEAN:        <expr>    expected: nu
[2] CHI2_VAR:         <expr>    expected: 2*nu
[3] VAR_CL:           <expr>    expected: 2*Cl^2/((2*l+1)*fsky)
[4] FRAC_ERR_CL:      <expr>    expected: sqrt(2/((2*l+1)*fsky))
[5] NMODES_1PT:       <expr>    modes available to a one-point statistic
[6] MIN_DETECT_1PT:   <expr>    n_sigma * sqrt(variance), symbolic in n_sigma
[7] NTRIANGLES:       <expr>    count of closed (l1,l2,l3) with l_i <= lmax
[8] MIN_DETECT_3PT:   <expr>    the same threshold for a bispectrum amplitude
```

Blocks [1] to [4] are the pipeline check. They are textbook and must come
out exactly; `FRAC_ERR_CL = sqrt(2/((2l+1) fsky))` is the standard cosmic
variance formula and if Maple does not reproduce it, the setup is wrong and
blocks [5] to [8] mean nothing.

## The expected answer, cross-checked before queueing

Blocks [1] to [4] were verified in sympy 1.14.0 before this job was written
(`crosscheck.py`, committed beside `job.mpl`):

```
[1] CHI2_MEAN     = nu
[2] CHI2_VAR      = 2*nu
[3] VAR_CL        = 2*Cl**2/(fsky*(2*l + 1))
[4] FRAC_ERR_CL   = sqrt(2)*sqrt(1/(fsky*(2*l + 1)))
```

Blocks [5] and [6] are **not** cross-checked and are the job's actual
work, since they depend on the window convention.

Block [7] has no known closed form but does have an exact validation
table, counted brute force by `crosscheck.py`. Maple's closed form must
agree with every row:

| `lmax` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| triangles | 1 | 4 | 11 | 23 | 42 | 69 | 106 | 154 | 215 |

The leading scaling is cubic in `lmax`. The plan only needs that scaling,
so a closed form Maple will not simplify is acceptable **provided it
reproduces this table**; a closed form that disagrees with any row is
wrong, however elegant.

## What would be surprising or wrong

**Wrong, not surprising:** any departure in blocks [1] to [4]. The
chi-squared moments and the cosmic-variance formula are fixed. A mismatch
means the degrees-of-freedom convention is wrong — most likely `fsky`
applied to `Cl` rather than to the mode count.

**Surprising, and it would change the plan:** a one-point floor in block
[6] low enough that the measure-predicted signals in Run 01's §2.3 exceed
it. Run 01 reports them as well within cosmic variance, so the expectation
is that they do not. If they do, the measure literature contains a live
observational question and the plan's measure branch moves from
floor-limited to decidable, which is the single biggest change any early
result could make. **This expectation is stated so it can fail, not
because the plan needs it to hold.**

**Also informative:** a triangle count in [7] that grows fast enough that
the three-point floor falls below the one-point floor. Then a conflict
invisible in one-point statistics could still be decidable in the
bispectrum, and the plan's work package ordering changes.

## What this job does not establish

It gives a floor, not a measurement. It says what *cannot* be decided; it
never says a question *is* decided. A predicted difference above the floor
goes into *decidable in principle*, which is a statement about the
achievable, and then needs the actual measurement and its actual error
bars before anything is settled.

It also assumes Gaussian statistics and statistical isotropy for the
estimator variances. Both are assumptions about the field, and a question
whose whole content is a departure from isotropy is not triaged by this
instrument. The plan records that limit.

## Inputs

None. All three derivations are from the mode statistics written into
`job.mpl`.

## Status

**Written but not executed.** Maple is not installed on the authoring
machine, so `job.mpl` is untested beyond the sympy cross-check of blocks
[1] to [4]. Syntax fixes go in `NOTES.md`; a fix that changes the
mathematics makes this job 004.
