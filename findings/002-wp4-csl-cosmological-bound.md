# WP-4: the CSL cosmological bound, and where the quoted figure came from

**Package:** WP-4 (`docs/RESEARCH-PLAN.md` §4).
**Day:** 2026-11-05, cycle 3. Branch `research/auto-2026-11-05`.
**Status:** complete, with one caveat stated in full below.
**Provisional on WP-1.**

Script backing every number: `verify/csl_cosmological_bound.py`, 5 of 5
checks PASS, exit 0, run before this file was committed.

---

## The result in one table

Martin & Vennin's own closed-form constraint, evaluated at the parameters
stated in their own figure caption. `m0` is the atomic mass unit; the
proton mass moves every entry by 1.5% and is tabulated by the script.

| `rc` [m] | branch that applies | `lambda_max` [s^-1] |
| --- | --- | --- |
| 1e-8 | 1, inflation crossing | 5.566e-87 |
| 1e-7 | **2, radiation crossing** | **2.471e-86** |
| 1e-6 | 2 | 2.471e-80 |
| 1e-5 | 2 | 2.471e-74 |
| 1e-4 | 2 | 2.471e-68 |

**This is the number WP-4 was commissioned to produce**, and it did not
exist in print: Run 02 confirmed at primary-source level that Martin &
Vennin state no numerical bound, their constraint being analytic in
`gamma` with the numerical content carried by a figure.

The bound falls **between the two printed figures** — `5.6e-90 s^-1`
attributed to Martin & Vennin and Gundhi et al.'s own `1e7 s^-1` — which
is what the plan recorded as its expectation. The expectation is scored
as met.

---

## WP-4's falsifier, and which way it went

The plan states it: *"reproducing neither camp's figure means the pipeline
is wrong; reproducing one vindicates that camp's operator choice on its own
terms, which is the root of the whole disagreement."*

**The attributed figure is reproduced to 0.6%.** Branch 1 of Martin &
Vennin's formula, at `rc = 1e-7 m`, `Delta N = 50`, `H_inf = 1e-5 Mp`,
`eps1 = 0.005` and `m0` the nucleon mass, gives

```
lambda_max = 5.5660e-90 s^-1     against the attributed  5.6e-90 s^-1
```

a ratio of 0.9939. The scan across seven decades of `rc` in the script
shows the match is not a coincidence of scale: every decade of `rc` moves
the answer by exactly three orders of magnitude, as `lambda ~ 1/rc^3`
requires, and only `rc = 1e-7 m` lands on the quoted value.

So the pipeline is validated, and the provenance question Run 01 and Run 02
left open is settled: **`5.6e-90 s^-1` is a correct evaluation of a formula
that appears in Martin & Vennin's paper.** It is not a number they state,
and it is not an invention. Gundhi et al. rendered their constraint, and
rendered it arithmetically right.

---

## The caveat, which is the actual finding

**At `rc = 1e-7 m`, branch 1 does not apply.**

Martin & Vennin give two bounds with an explicit condition selecting
between them:

```
gamma << m0^2 (448 rhobar_end eps1/3)^-1 e^-DeltaN            if H_end rc < e^DeltaN
gamma << m0^2 (35408 rhobar_end eps1/429)^-1 (H_end rc)^9 e^-10DeltaN
                                                              if H_end rc > e^DeltaN
```

At the figure caption's parameters, `H_end rc = 1.2342e22` while
`e^DeltaN = 5.1847e21`. So `H_end rc > e^DeltaN` and the **second** branch
is the one in force. It gives

```
lambda_max = 2.4710e-86 s^-1
```

which is weaker than the attributed figure by a factor 4412, i.e. **3.64
orders of magnitude**.

The condition has a clean physical reading, which is why it is worth
stating rather than treating as bookkeeping. A mode's physical wavelength
at the end of inflation is `a_end/k = e^DeltaN / H_end`. The CSL terms
switch on when that wavelength passes `rc`, which the Gaussian smearing
`exp(-k^2 rc^2 / 2a^2)` in `alpha_k` and `beta_k` enforces. So
`H_end rc < e^DeltaN` is exactly the statement *"the mode crossed `rc`
before inflation ended"*, and the two branches are the inflation-crossing
and radiation-crossing cases the paper describes in those words. At
`rc = 1e-7 m` and `Delta N = 50` the crossing happens **after** inflation,
so the radiation-era formula is the right one.

**The branch boundary sits inside the laboratory-viable range.**
`rc* = e^DeltaN / H_end = 4.201e-8 m`, against the paper's own stated
viable window `rc ~ 1e-8` to `1e-4 m`. So neither branch holds across that
window, and **a single number quoted as "the Martin-Vennin bound" without
an `rc` is ambiguous by construction** — not because anyone was careless,
but because the constraint genuinely is two formulae with a boundary in the
middle of the region of interest. That is a property of the physics and the
reason the paper published a figure rather than a number.

### What this does and does not change

It does **not** change Martin & Vennin's conclusion. `2.471e-86 s^-1` is
still roughly 68 orders of magnitude below the bottom of the
laboratory-viable window `1e-18` to `1e-10 s^-1`, so their finding that the
CMB-allowed and laboratory-allowed regions are disjoint stands, with room
to spare. Every entry in the table above is 50 to 80 orders below the lab
window.

It does change the **number**, and producing the number is what WP-4 is.

### What it is not

It is **not** a claim that Gundhi et al. made an error, and this file does
not say so. Their introduction renders a bound from a paper that states
two; which they intended, and whether the distinction mattered for their
purpose, is not established by anything read here. What is established is
that the figure matches branch 1 and that branch 2 is the one the stated
parameters select. `[INFERENCE]`, and the premises are: the branch
condition as written in arXiv:1906.04405, the figure caption's parameter
values, assumption A1 below, and the arithmetic in the script.

---

## The "97 orders of magnitude", finally with its arithmetic

Run 01 recorded the C-internal conflict as *"roughly 97 orders of
magnitude"* and tagged it `[SOURCED]`. Run 02 established that the tag is
wrong and the claim is an `[INFERENCE]`, because one side of the comparison
is Gundhi et al.'s rendering rather than a number Martin & Vennin state.
The plan's §4 names re-tagging it as WP-0 work and producing the number as
WP-4's.

The arithmetic, now from a committed script:

| Comparison | Gap |
| --- | --- |
| Gundhi et al. `1e7` against the attributed `5.6e-90` | **96.25** orders |
| Gundhi et al. `1e7` against the applicable branch-2 bound `2.471e-86` | **92.61** orders |

So "roughly 97" is right to within one order on the first reading and
within about four on the second. The claim's content survives; its tag does
not. Recorded here as `[INFERENCE]` with premises named, which is what Run
02 asked for.

**What this cannot settle, and does not claim to.** Which collapse operator
is correct. Run 01 established that the entire spread between the camps
comes from that choice, and the plan says in terms that no CMB measurement
selects it. Nothing in this file selects one. Reproducing Martin & Vennin's
arithmetic vindicates their arithmetic, not their operator.

---

## Method, and the three assumptions

The script evaluates published closed forms. It derives nothing and reads
nothing off a figure. Inputs, each with its locator in arXiv:1906.04405:

- the two upper bounds and the two lower bounds, from the equation block
  following eq. (powerSpectrum:rad), quoted verbatim in the script's
  docstring;
- `k/(aH)|_end = e^-DeltaN`, stated in the same block, and in de Sitter
  `aH = -1/eta` so `-k eta_end = e^-DeltaN`;
- `lambda = gamma/(8 pi^(3/2) rc^3)`, from the text after eq. (rho:cg);
- `m0` "a reference mass (usually the mass of a nucleon)";
- `Delta N = 50`, `H_inf = 1e-5 Mp`, `eps1 = 0.005`, from the caption of
  fig. (mapCSL);
- the viable laboratory region `rc ~ 1e-8 - 1e-4 m`,
  `lambda ~ 1e-18 - 1e-10 s^-1`, from the text.

Three assumptions, flagged because they are assumptions:

**A1. `H_end = H_inf`.** The bounds carry `H_end` and `rhobar_end`; the
figure caption states `H_inf`. At `eps1 = 0.005` the Hubble rate changes by
a fraction of a percent over the last e-folds, far below the precision of a
bound quoted to one significant figure. **This one is load-bearing for the
branch determination**, because `H_end rc` and `e^DeltaN` differ by only a
factor 2.4 at `rc = 1e-7 m`. A change in `H_end` of a factor 2.4 would move
the boundary across that `rc`. A change that large is not available from
slow-roll evolution at `eps1 = 0.005`, so the determination holds, but the
margin is a factor of 2.4 and not orders of magnitude, and anyone building
on it should know that.

**A2. `rhobar_end = 3 H_end^2 Mp^2` with `Mp` the reduced Planck mass.**
Fixed by the paper writing `rhobar_inf = 3 H_inf^2 Mp^2` explicitly and
using `H_inf = 1e-5 Mp`.

**A3. `<<` and `>` evaluated as equalities.** What is computed is the
threshold, not a bound with a safety factor, and is reported as a
threshold.

Dimensional consistency is checked in the script before any number is
trusted: `[gamma] = GeV^-2` follows from `(gamma/m0^2) * rhobar` being
dimensionless, and `[lambda] = [gamma]/[rc^3] = GeV`, an inverse time,
which is why `lambda` is a rate quoted in `s^-1`. Both unit conversions are
checked against independent values.

---

## The lower bounds, and a window that is empty

The script also evaluates the collapse-has-occurred lower bounds, which
Martin & Vennin give from the criterion `R < 1`. At every `rc` in the
table, `lambda_min` comes out around `1e-220` to `1e-208 s^-1`, which is
**far below** `lambda_max`. So the CMB-allowed window in `lambda` is wide
and non-empty, sitting between roughly `1e-220` and `1e-86 s^-1` at
`rc = 1e-7 m`.

That is worth saying plainly because it locates the incompatibility: the
CMB does not exclude CSL by leaving no room for it. It leaves an enormous
amount of room, in a region of `lambda` that is 68 orders of magnitude
below where the laboratory bounds allow. The two constraints are not in
tension about a parameter value; they are disjoint in a way that means one
of them is constraining something the other is not. Run 01's identification
of the collapse-operator choice as the whole of the disagreement is
consistent with that, and this computation does not go beyond it.

---

## Decidability bin, for the pairing WP-4 touched

Recorded only for the pairing in hand, per the standing loop. WP-2 is not
started.

**Run 01's C-internal pairing** (Martin & Vennin ↔ Gundhi et al., slot S4,
Run 01 verdict `genuine_conflict`): **D4**, no differing observable, under
§6's **reading 1** — the dispute is about which collapse operator the
theory should use, and the two camps do not disagree about what the CMB
says given an operator.

The evidence for calling it D4 rather than D1 or D2 is this computation:
both camps' numbers follow from correct arithmetic on their own premises,
and the premise that differs is the operator, not anything the data
measures. Run 01 reached the same conclusion by reading; it is now backed
by reproducing one camp's number from its own formula.

**What non-empirical criterion the camps use**, which §6 requires a D4
entry to state: Gundhi et al. argue Martin & Vennin's power-spectrum
correction is *perturbatively inconsistent*, which is a criterion of
internal consistency rather than of fit. That is recorded in Run 01 §2.3
and is not re-litigated here; nothing read today bears on it. Whether the
criterion is satisfied is a question about the derivation and not about the
sky, so the honest entry is that **data does not bear on this pairing** and
the field should stop implying it does.

This is a D4 and the plan's anti-kill criterion applies: it is **not** a
reason to keep working the pairing in a different vocabulary. It is
computed, written up, and closed.
