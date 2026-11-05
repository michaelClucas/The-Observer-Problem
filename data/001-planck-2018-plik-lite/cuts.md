# Cuts applied to dataset 001, and why

**Written 2026-11-05, cycle 4, BEFORE any WP-3 result was seen.** That is
the rule in `data/README.md` and the reason this file exists. The fit it
governs was run after this file was committed; the commit order is in the
git log and is the evidence.

---

## The three components used, and nothing else

| Component | `l` range | Data points | Why included |
| --- | --- | --- | --- |
| `planck_2018_highl_plik.TTTEEE_lite_native` | 30 - 2508 | 613 bandpowers (215 TT, 199 TE, 199 EE) | the lever arm in `k` that separates power-law corrections |
| `planck_2018_lowl.TT` | 2 - 29 | 28 | the only handle on the large-scale end, where a steep negative index puts its weight |
| `planck_2018_lowl.EE_sroll2` | 2 - 29 | 28 | fixes `tau`, which is degenerate with the amplitude of a low-`l` correction |

Bin counts from `plik_lite_v22.dataset` as committed to
`MANIFEST.sha256`, not from a paper.

### Excluded, with reasons

- **The full `plik` likelihood**, in favour of `plik_lite`. The plan's §2
  states this and it is not revisited: `plik` adds foreground nuisance
  parameters none of WP-3's questions touch, at a large cost in sampling
  dimension. The consequence is recorded in `SOURCE.md` field 7 and is a
  real bound on WP-3's claim, not a free choice: a correction large enough
  to shift the preferred foreground amplitudes is not correctly constrained
  by `plik_lite`, because the compression assumed it away.
- **Planck lensing.** Constrains integrated growth, which neither
  correction form modifies at the order being compared. Including it would
  tighten the LCDM parameters slightly and change nothing about `f`.
- **Planck non-Gaussianity / `f_NL`.** This is WP-6's dataset, not WP-3's,
  and will get its own `SOURCE.md` when obtained. A two-point dataset
  cannot address WP-6's question by construction.
- **BAO, SNe, any non-CMB data.** The question is about the primordial
  spectrum's shape; adding late-time distance data does not constrain `f`
  and does import a different systematics literature.
- **Any `l > 2508` extension.** `lmax = 2508` is the dataset's own limit.

## The parameters varied, and the ones held fixed

**Held fixed** at the Planck 2018 TT,TE,EE+lowE base-LCDM best fit
(arXiv:1807.06209 Table 1), the same values
`verify/planck_likelihood.py` already validates against:

```
logA 3.044   ns 0.9649   H0 67.36   ombh2 0.02237
omch2 0.1200   tau 0.0544   mnu 0.06   A_planck 1.0
```

**Varied:** the correction amplitudes only.

### Why the LCDM parameters are held fixed, stated as a limitation

This is a **profile at fixed background**, not a marginalised constraint.
Holding the six LCDM parameters fixed while varying a correction amplitude
**overstates** the constraint on that amplitude, because in a full fit the
background parameters would move to partially absorb the correction — `ns`
most of all, since a correction `(k/k_*)^m` with small `m` is partially
degenerate with a shift in the tilt.

It is done anyway, today, for a reason that is stated rather than hidden:
a marginalised constraint needs an MCMC, the plan's own benchmark puts a
1e5-sample chain at roughly 22 core-hours, and that is not a thing an
unattended day can start and finish. The fixed-background profile is
computable in minutes and is **a valid upper bound on how well the data
can distinguish the two shapes** — if the shapes are indistinguishable even
with the background frozen, marginalising cannot help. If they are
distinguishable, the number is an overstatement and the marginalised
version is required before any D1 verdict.

**So the profile can establish a D3 or D4 verdict but cannot establish a
D1.** Written down before the result, so that a D1-looking number cannot be
reported as one.

## The correction forms compared, with their indices fixed in advance

The nested model is

```
P(k) = P_0(k) [ 1 + A_C (k/k_*)^(m_C) + A_D (k/k_*)^(m_D) ]
```

with `k_*` the Planck pivot `0.05 Mpc^-1`.

Indices **fixed at their published values**, read at primary level on
2026-11-05 and recorded in
`maple/jobs/003-power-spectrum-corrections/JOB.md`:

| Label | `m` | Source |
| --- | --- | --- |
| C, inflation-era crossing | **-1** | Martin & Vennin 2020, `n_S = 0` |
| C, radiation-era crossing | **-10** | Martin & Vennin 2020, `n_S = -9` |
| C, 2012 non-scale-invariant branch | **+3** | Martin, Vennin & Peter 2012, `n_S = 4` |
| D, scale-invariant case | **0** | Martin & Vennin 2018 at `p = 7 - 2n` |
| D, general | `p + 2n - 7` | Martin & Vennin 2018 |

The D side's index is a **free integer** in principle, so the comparison is
run at each integer `m_D` in `-12 .. +4`, a range chosen to cover every
C-side index plus a margin either side. Fixing the range now is the point
of this file: a range chosen after seeing which `m_D` fits best would be a
different and much weaker statement.

## Free-parameter counts, fixed in advance

The standing loop forbids reporting a comparison statistic without both
counts, and says no validator here will catch it. Computed, not asserted,
in `maple/jobs/003-power-spectrum-corrections/crosscheck.py` as symbolic
Jacobian ranks:

```
FREE_PARAMETERS_C = 1      amplitude only; the index is a pure number
FREE_PARAMETERS_D = 2      amplitude and index
```

Every statistic reported from this dataset carries **1 and 2**. A statistic
without them is recorded as uninterpretable, not as a weak result.

## The singular region, identified in advance

`crosscheck.py` found the C/D shape degeneracy at `p = 6 - 2n`, which makes
`m_D = m_C = -1`. So **`m_D = -1` is excluded from the comparison** and
reported as singular rather than scored: at that index the two corrections
are the same function and no data can separate them. At integer `n` the
locus is `p = 4, 2, 0, -2` for `n = 1..4`, all physical values.

Likewise `m_D = -10` and `m_D = +3` coincide with the other two C branches
and are reported as singular at those branches.

Excluding them is not goalpost-moving. It is stating that a comparison
between two identical functions has no content, before running it.

## What is expected, stated so it can fail

The plan's §4 records WP-3's expected bin as **D1 or D2**, and this file
does not overwrite that. My own expectation before running, recorded
separately so both can be scored:

- The amplitudes `A_C` and `A_D` will be constrained to be small, of order
  `1e-2` or below at the pivot, since the spectrum is measured to better
  than a percent over much of the range.
- The two shapes **will** be separable where `|m_C - m_D| >= 2`, because
  two decades of lever arm in `k` resolves an integer power difference
  easily. So the pairing is not D4.
- Whether it is D1 or D2 depends on `sigma_floor`, which is Maple job
  002's and has not returned. **So a D1-versus-D2 split cannot be made
  today**, and the honest output is a `Delta` and a `sigma_now` with the
  third number pending.
- The `m_C = -10` branch will be much the weaker constrained, because its
  weight sits at low `l` where the data's own reduction is least
  transparent and the floor is largest.

If instead the shapes come out inseparable at the fixed background, that is
a D3-or-D4 result on the field's one empirically live conflict, and the
plan says in terms that the package does not need the comparison to come
out any particular way.

---

## Addendum, same day, still before any fit result was seen

Written while implementing the fit, committed before it was run. The git
log shows this addendum's commit preceding the commit that carries the
result. Recorded as an addendum rather than edited into the text above,
because the text above is what was committed first and rewriting it would
destroy the evidence of ordering.

**The small-k regularisation, which the cuts above failed to anticipate.**

A correction `(k/k_*)^m` with `m` negative diverges as `k -> 0`. camb
integrates the primordial spectrum from `k_min ~ 1e-6 Mpc^-1`, far below
anything the CMB measures, and at `k = 1e-6` the factor `(k/k_*)^-10` is
about `1e47`. So the uncorrected form cannot be handed to camb: it would
either make `P(k)` negative or be dominated by modes outside the domain on
which the papers derive it. Martin & Vennin derive these corrections for
super-Hubble modes of cosmological interest, not for `k` forty decades
below the horizon.

**The choice:** the correction factor is evaluated as published for
`k >= k_reg` and held at its `k_reg` value for `k < k_reg`, with
`k_reg = 1e-4 Mpc^-1`. That is about a decade below the largest scale the
CMB constrains, so it is outside the window the data speaks to and inside
the window the derivation covers.

**Why `1e-4` and not something tuned:** `l ~ 2` corresponds to
`k ~ l / D_A ~ 1.4e-4 Mpc^-1` at the last-scattering distance, so `1e-4`
sits just below the largest observable scale. Fixed now, not after seeing
which value gives a tidier answer.

**And it is tested rather than asserted.** The fit is run at
`k_reg = 1e-4` and again at `k_reg = 3e-5`, and both are reported. For the
shallow indices the answer must be insensitive to `k_reg`, since those
corrections put no weight at small `k`; for `m = -10` it will be sensitive,
and **the size of that sensitivity is itself the result** for that branch:
a constraint that depends on an unobservable regularisation is not a
constraint on the sky, and if that is what comes out it will be reported as
such rather than as a number.

**Positivity:** `P(k)` is required positive everywhere. Any amplitude that
violates it is outside the perturbative domain in which both corrections
were derived, and is reported as excluded by the derivation rather than by
the data. The two exclusions are different things and are not merged.

**The amplitude's reference scale** is `k_*= 0.05 Mpc^-1`, the Planck
pivot, so `A_C` and `A_D` are the fractional corrections at the pivot.
Stated because a constraint on an amplitude is meaningless without the
scale it is quoted at.

**One further method note, so the statistic is interpretable.** `P(k)` is
linear in each amplitude and the transfer functions do not depend on them,
so `D_l` is linear in the amplitudes and `chi^2` is exactly quadratic in
them. The fit therefore computes one `D_l` response vector per index and
builds the curvature matrix from those, rather than sampling. Linearity is
checked in the script by comparing the response at `2h` against twice the
response at `h`; if that check fails the quadratic form is not valid and
the numbers are not reported.

**What the correlation coefficient will be used for.** For each pair of
indices the two-amplitude curvature matrix gives `sigma(A_C)`,
`sigma(A_D)` and their correlation `rho`. A `|rho|` very close to 1 means
the data cannot separate the two shapes, which is a D3-or-D4 statement; a
modest `|rho|` means it can. The threshold is **not** fixed here, because
the honest output is the number itself and a threshold chosen now would
add nothing the number does not say.
