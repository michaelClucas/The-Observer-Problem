# WP-3: can Planck separate the collapse and decoherence corrections?

**Package:** WP-3, the plan's centrepiece (`docs/RESEARCH-PLAN.md` §4).
**Day:** 2026-11-05, cycle 4. Branch `research/auto-2026-11-05`.
**Status:** the question Run 01 said nobody had asked is now asked and
answered at fixed background. The D1-versus-D2 split remains open and is
blocked on Maple job 002.
**Provisional on WP-1.**

Script: `verify/wp3_nested_comparison.py`, all checks PASS, exit 0.
Data provenance: `data/001-planck-2018-plik-lite/`.
Cuts: `data/001-planck-2018-plik-lite/cuts.md` **and its two same-day
addenda**, all three committed before the fit was run. The git log carries
the ordering: `a41a865`, `7c4b6c7`, `21575f7`, then the commit holding this
file.

---

## The verdict

**The C-versus-D pairing is not D3 and not D4.** Every pair of correction
shapes that survives its own derivation's perturbative domain is separable
by Planck at fixed background, with correlation coefficients between
`-0.053` and `-0.964`.

So Run 01's `genuine_conflict` on the predicted observable is real and the
data does bear on it. The pairing is **D1 or D2**, which is what the plan
recorded as its expected bin, and the expectation is scored as met.

**Which of D1 or D2 cannot be decided today.** That needs `sigma_floor`,
which is Maple job 002's output and has not returned. And `cuts.md` states
in advance that a fixed-background profile **cannot establish D1** at all,
because holding the six LCDM parameters fixed overstates the constraint —
in a full fit the background would move to absorb part of the correction,
`n_S` most of all. The profile can rule D3 and D4 out, and it has. It
cannot rule D1 in.

---

## The result that was not expected

**Two of the three published collapse branches cannot be tested against
the CMB at all, and the obstruction is their own derivation, not the
data.**

Both corrections are first-order results. So an amplitude large enough to
make the correction order unity somewhere the CMB measures is outside the
domain in which either was derived. Imposing that across the window the
CMB actually constrains, `k = 1.4e-4` to `0.2 Mpc^-1`, bounds the pivot
amplitude:

| Branch | index `m` | perturbativity bound on `|A|` at `k_* = 0.05 Mpc^-1` |
| --- | --- | --- |
| C, radiation-era crossing (`n_S = -9`) | -10 | **2.96e-26** |
| C, inflation-era crossing (`n_S = 0`) | -1 | **2.80e-03** |
| C, 2012 non-scale-invariant (`n_S = 4`) | +3 | **1.56e-02** |
| D, scale invariant | 0 | 1.00 |

A pivot amplitude of `3e-26` is not a constraint the CMB could improve on;
it is a statement that the `m = -10` branch, treated to first order,
cannot have an observable amplitude anywhere the CMB looks. **It is
excluded by its own derivation before Planck is consulted.** Every index
from `-12` to `-2` is excluded the same way; `m = -1` is the shallowest
negative index that survives.

This is why `cuts.md` insisted that exclusion-by-the-derivation and
exclusion-by-the-data be reported separately and never merged. They are
different claims and only one of them is about the sky.

### And the surviving branch is only just testable

For `m = -1`, the perturbativity bound is `2.80e-3` and Planck's
constraint is `sigma(A_C) = 0.9` to `1.1e-3`. **Those are the same order of
magnitude.** So the data's reach on the one collapse branch the CMB can
address sits just inside the domain where the first-order calculation is
valid, with a factor of about three to spare. Anyone pushing this
comparison harder — marginalising the background, adding data — will run
into the derivation's validity before running out of statistical power.

That is a fact about the state of the calculation, not about the
instrument, and it is the most useful thing this cycle produced for
whoever works WP-3 next.

---

## The numbers

Baseline, which must reproduce `verify/planck_likelihood.py` or nothing
downstream is reported:

```
plik_lite_TTTEEE   chi2 = 583.919   recorded 583.935 +/- 3.0   AGREES
lowl_TT            chi2 =  23.417   recorded  23.419 +/- 0.5   AGREES
lowl_EE_sroll2     chi2 = 390.021   recorded 390.021 +/- 3.0   AGREES
TOTAL              chi2 = 997.358
```

This check does more work than it looks like. It establishes that calling
the three likelihoods' `chi2` entry points on spectra computed in this
script gives the same answer as routing them through a cobaya provider.
Without it, a modified-spectrum result could differ from the baseline for a
plumbing reason rather than a physical one.

`D_l` is linear in each amplitude to a maximum relative departure of
`1.0e-7`, tested at `A = 1e-3` against `A = 2e-3`. So `chi2` is **exactly**
quadratic in the amplitudes and the curvature matrix is the whole
likelihood surface — no sampler, and no approximation in saying so.

### Pairwise separability

`sigma` is the 1-sigma constraint on each pivot amplitude with the other
amplitude free. `rho` is their correlation.

**Free parameters: C side 1, D side 2.** Computed as symbolic Jacobian
ranks in `maple/jobs/003-power-spectrum-corrections/crosscheck.py`, not
asserted. Both counts attach to every row. A statistic without them is
recorded as uninterpretable, not as a weak result — and the asymmetry is
the point: the C side moves only in amplitude at fixed epoch, the D side
moves in amplitude and shape, so this is **not** a like-for-like comparison
of two one-parameter models.

| `m_C` | `m_D` | `sigma(A_C)` | `sigma(A_D)` | `rho` | `1-|rho|` | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| -1 | -1 | - | - | - | - | **singular**: identical functions |
| -1 | 0 | 1.099e-3 | 1.972e-3 | -0.5905 | 0.410 | separable |
| -1 | 1 | 9.598e-4 | 1.144e-3 | -0.3812 | 0.619 | separable |
| -1 | 2 | 9.211e-4 | 5.983e-4 | -0.2682 | 0.732 | separable |
| -1 | 3 | 9.026e-4 | 2.891e-4 | -0.1829 | 0.817 | separable |
| -1 | 4 | 8.886e-4 | 1.619e-4 | -0.0535 | 0.947 | separable |
| 3 | -1 | 2.891e-4 | 9.026e-4 | -0.1829 | 0.817 | separable |
| 3 | 0 | 3.732e-4 | 2.090e-3 | -0.6480 | 0.352 | separable |
| 3 | 1 | 5.410e-4 | 2.014e-3 | -0.8509 | 0.149 | separable |
| 3 | 2 | 1.074e-3 | 2.179e-3 | -0.9644 | 0.036 | **marginal** |
| 3 | 3 | - | - | - | - | **singular**: identical functions |
| 3 | 4 | 5.428e-4 | 3.088e-4 | -0.8520 | 0.148 | separable |

The singular rows are the ones `cuts.md` identified in advance, where
`m_C = m_D` makes the two corrections the same function. Excluding them is
not goalpost-moving: a comparison between two identical functions has no
content, and saying so before running is what `cuts.md` is for.

`crosscheck.py` separately found a shape degeneracy at `p = 6 - 2n`, which
is where `m_D = m_C = -1`, and which is **exactly a regime boundary of the
D side's own calculation**. That prediction is confirmed here as the
`(-1, -1)` singular row.

The one marginal entry, `(m_C, m_D) = (3, 2)`, is adjacent indices at the
steep positive end, where two decades of lever arm separates `k^3` from
`k^2` least well. It is reported as marginal rather than rounded either way.

### The regularisation is not doing the work

`cuts.md`'s addenda required this test, and stated in advance that a
constraint depending on an unobservable regularisation is not a constraint
on the sky. Repeating the whole fit at `k_reg = 3e-5` instead of `1e-4`:

| Branch | worst fractional change in `sigma(A_C)` | verdict |
| --- | --- | --- |
| `m = -1` | 4.63e-4 | **stable** |
| `m = +3` | 1.37e-5 | **stable** |

So the surviving constraints are set by modes the CMB measures, not by the
regularisation. The branches where the regularisation *would* have
dominated are precisely the ones perturbativity already excluded, so the
question does not arise for them.

---

## Method, and what it deliberately is not

Extends `verify/planck_likelihood.py` rather than building a second
pipeline, as the standing loop requires: the same three cobaya native
components, the same Planck 2018 best fit, the same recorded `chi2` as a
tripwire.

The model is `P(k) = P_0(k)[1 + sum_i A_i (k/k_*)^(m_i)]`, with the indices
fixed at their **published** values, read at primary level on 2026-11-05
and recorded in `maple/jobs/003-power-spectrum-corrections/JOB.md`. The
D-side index is scanned over the integer range `-12` to `+4`, fixed in
`cuts.md` before the fit; a range chosen after seeing which `m_D` fits best
would be a much weaker statement.

**What this is not:**

- **Not a marginalised constraint.** Fixed background. Overstates the
  constraint. Can establish D3 or D4, cannot establish D1. Stated in
  `cuts.md` in advance, not here in hindsight. A marginalised version needs
  an MCMC and the plan's own benchmark puts a 1e5-sample chain at roughly
  22 core-hours, which an unattended day cannot start and finish.
- **Not a model comparison between the two camps' physics.** The amplitudes
  here are phenomenological: the map from `A_C` to the CSL parameter
  `gamma`, and from `A_D` to the coupling `k_gamma`, is what Maple job 003
  supplies and job 003 has not returned. So this cycle answers "can the
  data tell the two **shapes** apart", which is the prior question and the
  one Run 01 said nobody had asked. It does not yet answer "which does the
  data prefer, in the theories' own parameters".
- **Not a statement about the `l < 30` end's systematics.** `SOURCE.md`
  field 7 records that the low-E component is a precomputed probability
  table whose reduction is entirely upstream and opaque from the file.
  Anything here that leans on `l < 30` inherits Pagano et al.'s systematics
  treatment wholesale.
- **Not valid for large corrections.** `plik_lite`'s foreground
  marginalisation was performed assuming a base-LCDM CMB spectrum, so a
  correction large enough to shift the preferred foreground amplitudes is
  not correctly constrained here. `SOURCE.md` field 7 records this as a
  bound on the claim rather than a caveat on it. The amplitudes that come
  out are of order `1e-3`, comfortably inside it.

---

## What the next cycle on WP-3 should do, and why

1. **Wait for job 002** and split D1 from D2 by comparing `sigma(A_C)`
   against `sigma_floor`. That is one comparison and it closes the bin.
2. **Wait for job 003** and convert the amplitude constraints into
   constraints on `gamma` and `k_gamma`, which is what makes the result a
   statement about the two theories rather than about two shapes.
3. **Then marginalise**, not before. A marginalised constraint is only
   worth 22 core-hours once there is something to put in it, and the
   fixed-background profile already establishes that the answer is not D3
   or D4, which was the cheap half of the question.
4. **Flag to whoever does step 3**: the `m = -1` branch's perturbativity
   bound is only a factor of three above Planck's current reach. A
   marginalised fit will weaken the data constraint, which *helps* here, but
   any attempt to push the comparison with better data will hit the
   derivation's validity first. The next real gain on this branch is a
   second-order calculation, not a better instrument.

---

## Decidability bin

**Run 01 open question 4 / the C-versus-D pairing on the predicted
observable:** **D1 or D2**, not D3, not D4.

`Delta` exists and is computable: the two shapes differ, and Planck
separates them with `1-|rho|` from 0.036 to 0.947 across the admissible
index pairs. `sigma_now` is the `sigma(A)` column, of order `1e-3` at the
pivot. `sigma_floor` is pending job 002.

Recorded for this pairing only. WP-2 is not started and no ledger survey
was produced.
