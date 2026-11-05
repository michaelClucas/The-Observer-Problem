# WP-5: the measure branch dies, and the reason is that there is only one monopole

**Package:** WP-5 (`docs/RESEARCH-PLAN.md` §4).
**Day:** 2026-11-05, cycle 6. Branch `research/auto-2026-11-05`.
**Status:** **a branch kill criterion fired.** The measure branch is closed.
**Provisional on WP-1.**

Script: `verify/measure_monopole_vs_floor.py`, all checks PASS, exit 0.
Source: `arXiv:1204.1569`, Salem, *"The CMB and the measure of the
multiverse"*, JHEP 06 (2012) 153, read at primary level as LaTeX source
(`c.tex`) — §5, §6 and the conclusions.

---

## The kill criterion, and that it fired

`docs/RESEARCH-PLAN.md` §5: *"The measure branch dies if WP-5 shows every
measure-predicted signal below the floor. Report the computation, close the
questions, write them up, and do not keep working them."*

**It fired.** Both measure-predicted signals, for both measures, are below
the floor, and the reason is structural rather than a matter of the number
being small.

The plan's expected bin for WP-5 was **D3** and the verdict is **D3**. The
plan also attached a falsifier that mattered: *"if any measure-predicted
signal exceeds the floor, the measure literature has a live observational
question, this package's expectation is wrong, and the measure branch moves
from closed to active. The package is written to find that out, not to
confirm D3."* It was looked for. It is not there, and the three statements
below are why.

---

## What Salem actually predicts

Run 01 recorded this as **cited, not computed**. It is now read at primary
level, and the prediction is in closed form.

**S1, the prediction** (conclusions, verbatim):

> Both measures predict a 1-point expectation value for the gauge-invariant
> Newtonian potential `Psi`. This takes the form of a scale-dependent
> monopole, `<Psi_{k l m}>_obs = Psibar_{k00} k delta_{l0} delta_{m0}`,
> where the precise form of `Psibar_{k00}` differs between the two
> measures, but in both cases the dominant behavior is
> `Psibar_{k00} ~ k^2 rCMB^2 P(k)` [...] Each measure also predicts a
> contribution to the expectation value of the 3-point correlation
> function, when one of the three field insertions is the monopole.

`[SOURCED]`

So Run 01's §2.3 entry is confirmed exactly: two genuinely different
predicted observables, and the difference is in `Psibar_{k00}`'s detailed
form while the dominant scaling is shared.

**S2, the suppression** (§5, verbatim):

> Our result (mean1) differs by a factor of order
> `k^(1/2) [k^3 P(k)]^(1/2)`. The term in brackets provides an order
> `10^-5` suppression. To compensate for this suppression with the factor
> of `k^(1/2)` would require examining extremely small scales,
> `k rCMB ~ 10^10`, well beyond the validity of our analysis and beyond any
> foreseeable observation.

`[SOURCED]`

**S3, the irreducibility, which is the statement that decides the bin**
(§5, verbatim):

> even in a map of perturbations with more three-dimensional resolution, we
> expect the 3-point correlator to fall within cosmic variance, since
> restricting to the single `l = m = 0` mode does not allow one to reduce
> the uncertainty as is usually done by averaging over many `m` at large
> `l`.

`[SOURCED]`

---

## Why this is D3 and not merely a small number

The difference matters, because "below current error bars" would be D2 and
would mean a better measurement settles it. It does not.

**The entire signal lives in the monopole.** `delta_{l0} delta_{m0}` in S1,
and S3 for the three-point piece. There is exactly one monopole mode on the
sky.

The cosmic-variance uncertainty on a multipole shrinks as more independent
modes become available, `2l+1` of them at multipole `l`, which is why the
fractional uncertainty falls from 141% at `l = 0` to 2.0% at `l = 2508`:

```
     l    modes    fractional sigma (f_sky = 1)
     0        1              1.4142
     1        3              0.8165
     2        5              0.6325
    10       21              0.3086
   100      201              0.0998
  1000     2001              0.0316
  2508     5017              0.0200
```

**At `l = 0` the count is one, and there is nothing to average.** No
instrument, no survey, no amount of integration time changes that. There is
one monopole, we have measured it, and there will never be a second. That
is what makes this floor-limited in the strongest available sense rather
than a question of precision.

### And the scale that would beat the suppression is inside the regime where the prediction fails

S2's `k rCMB ~ 10^10` is arithmetically correct — the script confirms the
exponent to two decimal places from `[k^3 P(k)]^(1/2) ~ 10^-5` — and
translating it:

| Quantity | Value |
| --- | --- |
| `rCMB` (Planck 2018 base-LCDM) | 13869 Mpc |
| `k` needed | **7.21e5 Mpc^-1** |
| Planck's reach, `k ~ lmax/rCMB` at `lmax = 2508` | 1.81e-1 Mpc^-1 |
| factor beyond Planck | 4.0e6, i.e. **6.6 orders of magnitude** |
| where linear perturbation theory stops | `k ~ 0.2 Mpc^-1` |
| factor inside the nonlinear regime | 3.6e6, i.e. **6.6 orders of magnitude** |

So the scale at which the measure signal would become comparable to a
typical perturbation is not merely unobserved. It is about six and a half
orders of magnitude inside the regime where the **linear calculation that
produced the prediction has stopped applying.** Salem says this in words —
"well beyond the validity of our analysis" — and the arithmetic agrees.

**Two independent obstructions, then.** The mode count makes the floor
unbeatable; the validity of the derivation makes the compensating scale
unreachable even in principle. Either alone gives D3.

---

## What was not computed, stated so nothing is overclaimed

**The numeric ratio `Delta / sigma_floor` is not computed here**, and this
script is explicitly **not** a substitute for Maple job 002 (issue
michaelClucas/The-Observer-Problem#9, still `maple:queued`). The standing
loop forbids substituting a cross-check for a filed job and that rule is
respected.

What the script computes is the **mode count at `l = 0`**, which is
arithmetic and is an *input* to whatever formula job 002 returns rather
than its output. So the inequality's **direction** is established without
its **magnitude**:

- established: the signal sits in the one place on the sky where the floor
  cannot be reduced by averaging, and reaching a typical-perturbation
  amplitude needs a scale where the prediction does not hold;
- pending job 002: the numeric value of `sigma_floor` for a one-point
  statistic, and therefore the ratio.

**Job 002 cannot reverse the verdict**, because no value of `sigma_floor`
changes the fact that `l = 0` has one mode. It will supply a number worth
having, and it should still be run — it is the triage's instrument for
every other package. But WP-5 does not wait for it, because waiting for a
number that cannot change the conclusion is exactly the manufactured work
the plan's §5 says must not be used to avoid a kill.

---

## Decidability bin

**Run 01's E3 causal-patch ↔ fat-geodesic pairing, on the predicted
observable** (Run 01 verdict: `genuine_conflict that is empirically idle`):
**D3, floor-limited.**

Run 01's own phrase turns out to be exactly right, and now has its
mechanism: the conflict is real — the two measures predict different
`Psibar_{k00}` — and it is idle, because the difference is confined to a
single-mode observable whose uncertainty no measurement reduces.

Per §6, a D3 entry records `Delta`, `sigma_floor` and the ratio. `Delta` is
S1's `Psibar_{k00} k` with the measure-dependent form; `sigma_floor` and
the ratio are pending job 002. The entry is recorded as **D3 with the ratio
pending**, which is a complete verdict with an incomplete number, not an
incomplete verdict.

### §6 on what D3 is worth

> The strongest possible outcome short of a measurement, because it is a
> computed impossibility rather than an absence of effort. [...] Worth
> publishing on its own: "this distinction is below the one-sky floor by a
> factor of N" is a real contribution, and the field currently asserts such
> things without the number.

The field does assert it: Salem's own abstract says "well within cosmic
variance". What this cycle adds is **why it cannot be improved** — the mode
count — which is the part that turns "currently unobservable" into
"unobservable in principle", and which no source read in Runs 01, 02 or
today states in those terms.

---

## The branch is closed. What that means and does not mean

Closed per §5: the computation is reported, the questions are closed, and
**the branch is not worked further**. The anti-kill criterion applies with
full force — a D3 verdict is not a reason to restate the question in a
vocabulary where it sounds decidable, and no attempt is made here to find
one.

What it does **not** mean:

- It does not mean the measure problem is solved or empty. It means **this
  particular pair of measures, compared through this particular
  observable**, cannot be separated by data. Salem's own conclusion makes
  the wider point, that the two measures "validate the standard
  inflationary predictions", which is a result about the measures' harmless-
  ness here and not about measures in general.
- It does not close Salem's §1 "three phenomenological tests", which he
  says "demonstrate how the choice of measure can have very large effects".
  Those are a different route and were not read today. Recorded as a
  `[LEAD]` for whoever revisits measures: if the measure branch is ever
  reopened, that is the door, not this one.
- It does not touch Run 01's open question 9, on whether cosmic variance
  and the measure problem are conceptually continuous. The plan's §8
  excludes that identification and uses cosmic variance **as an
  instrument**, which is what was done here.

---

## What would reopen it

Stated, because a kill with no reopening condition is an assertion rather
than a result:

1. A measure-predicted signal at `l > 0`. Everything above turns on the
   prediction being a monopole. A measure whose selection effect broke
   statistical isotropy, rather than appearing as a scale-dependent
   monopole, would have `2l+1` modes to average and would not be
   floor-limited by this argument.
2. A derivation valid at `k rCMB ~ 10^10`. Salem's suppression is
   compensated at that scale, and his own analysis does not reach it. A
   nonlinear treatment that did would need checking against this verdict.
3. Salem's §1 phenomenological tests, above.

None of these is available today and none is pursued.
