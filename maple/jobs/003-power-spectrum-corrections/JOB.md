# Job 003 - One parameterisation for the collapse and decoherence corrections to the curvature power spectrum

**Round trips: 1.** Gates **WP-3**, the plan's centrepiece, and **WP-4**
through it. Nothing gates this job: the mode equations it needs were read
at primary source level on 2026-11-05 and are reproduced in full below.

`maple/README.md` recorded this job as "not written" because its mode
equations "have not been read at that level of detail". They now have
been. The three sources, read as LaTeX source from `arxiv.org/e-print/`:

| Source | What was read | What it supplies |
| --- | --- | --- |
| `arXiv:1906.04405` Martin & Vennin 2020 | §II-III and the Supplementary Material's "The CSL Master Equations" and "Solving the CSL Equation" | the CSL third-order ODE, its source function, and `alpha_k`, `beta_k` for both epochs |
| `arXiv:1801.09949` Martin & Vennin 2018 | §2-3 and §5 | the open-EFT power-spectrum correction and its source function |
| `arXiv:1207.2086` Martin, Vennin & Peter 2012 | abstract and §VI | the two-branch validation target |

---

## The structural fact this job exists to exploit

**The two corrections are the same operator equation with different source
functions.** This was not known to Run 01 and it is why the job is
well-posed.

Martin & Vennin 2020 eq. (thirdvlinear): the CSL-modified two-point
function of the Mukhanov-Sasaki variable obeys

```
P_vv''' + 4 omega^2(k,eta) P_vv' + 4 omega (d omega / d eta) P_vv = S
```

solved through the Green function of the *free* theory, eq. (Green:def),

```
G(eta, etabar) = (1/W) [ g0*(etabar) g0(eta) - g0(etabar) g0*(eta) ] Theta(eta - etabar)
```

with `g0'' + omega^2 g0 = 0` the Mukhanov-Sasaki mode and `W` its
(constant) Wronskian.

Martin & Vennin 2018 eq. (exactsolquadratic:generic) solves the open-EFT
case in exactly the same form, which they state "is valid for any source
function":

```
P_vv = g0(eta) g0*(eta) + 2 Int_{-infinity}^{eta} S_n(eta') Im^2[ g0(eta') g0*(eta) ] d eta'
```

`Im^2[g0(eta') g0*(eta)]` is `(W/2)^2 G(eta,eta')^2` up to the normalisation
of `W`, so the two solution formulae are the same object. **Both
modifications therefore reduce to the same linear functional of a source.**

So the common parameterisation WP-3 needs is not a fitted ansatz. It is a
consequence: whatever the source, the correction is
`Delta P(k) = 2 Int S(eta') Im^2[g0(eta') g0*(eta)] d eta'`, and the two
approaches supply two different `S`.

**What Maple is for** is extracting the super-Hubble `k`-dependence of that
integral in closed form for each source, symbolically, and then eliminating
the underlying parameters to expose which combinations are degenerate. The
`k`-powers are quoted in the papers; the degeneracy structure is not stated
anywhere and is what WP-3's free-parameter count depends on.

---

## What is computed

### Part A. The CSL source, both epochs

Martin & Vennin 2020 eq. (source:def):

```
S_CSL = (gamma/m0^2) [ 2 a^4 (alpha_k^2 + omega^2 beta_k^2)
                       - 2 (a^4 alpha_k beta_k)'
                       + (a^4 beta_k^2)'' ]
```

with, during **inflation**, eqs. (alphainf) and (betainf):

```
alpha_k = (Mp^2 H^2 eps1 / z) exp(-k^2 rc^2/(2 a^2))
          * [ -8 - eps2 + 6 (a H / k)^2 eps1 (1 + eps2/2) ]

beta_k  = (2 Mp^2 H eps1 / (a z)) exp(-k^2 rc^2/(2 a^2))
          * [ -3 eps1 (a H / k)^2 + 1 ]
```

and during the **radiation era**, eqs. (alpharad) and (betarad):

```
alpha_k = (24 Mp^2 H^2 / z) exp(-k^2 rc^2/(2 a^2)) [ 3 (a H / k)^2 - 1 ]

beta_k  = (12 Mp^2 H / (a z)) exp(-k^2 rc^2/(2 a^2)) [ 1 - 6 (a H / k)^2 ]
```

Conventions, stated so the job is reproducible and so a disagreement is
locatable. Reduced Planck mass `Mp`; `z = a Mp sqrt(2 eps1)`;
`omega^2(k,eta) = cs^2 k^2 - z''/z`; `eps2 = d ln eps1 / d ln a`. De Sitter
inflation `a = -1/(H eta)` with `eta < 0`, constant `eps1`, and **`eps2 = 0`**
(a deliberate simplification, declared: the papers' quoted indices are
leading order in slow roll, and `eps2` enters `alpha_k` additively against
the constant `-8`, so it shifts the amplitude and not the `k`-power — the
job is asked to confirm that, not to assume it). Radiation era `a` linear in
`eta` so that `z''/z = 0` and `cs^2 = 1/3`.

**Compute:** the leading super-Hubble behaviour of

```
Delta P_CSL(k) = 2 Int_{eta_c}^{eta} S_CSL(eta') Im^2[ g0(eta') g0*(eta) ] d eta'
```

as a power of `k`, for each epoch, with `eta_c` the conformal time at which
the mode crosses `rc` — i.e. where the Gaussian `exp(-k^2 rc^2/(2a^2))`
turns on. Report it as `A_C * (k/k_star)^(m_C)` with `A_C` fully explicit in
`gamma, m0, rc, eps1, H, Mp, Delta N`.

### Part B. The open-EFT source

Martin & Vennin 2018 eq. (Pvv:modified:generic) with eq. (I2n). The paper
already reduces the relative correction to

```
Delta P_k  ~  C(n,p) (kgamma/k_star)^(4-2n) (k/k_star)^(p+2n-7) * L^(n-1)
```

in three regimes of `p`, where `L = N_T - Delta N_star + ln(... k/k_star)`
and `C(n,p)` is the stated ratio of Gamma functions in the middle regime,
`1/[2(6-2n-p)] (H_star lE)^(p+2n-6)` in the first, and the stated
`exp`-dependent prefactor in the third.

**Compute:** `C(n,p)` symbolically from the `I_{2n-1}, I_{2n}` integrals for
`n = 1` and `n = 2` — where the paper says they are generalised
hypergeometric and gives them in closed form — and **confirm or contradict**
the saddle-point form eq. (I2n:appr) that the paper uses for `n >= 3`.
Report `A_D * (k/k_star)^(m_D)` with `m_D = p + 2n - 7`, plus the logarithmic
factor's exponent `n - 1` kept explicit and not absorbed into `A_D`.

### Part C. The joint nested form and its degeneracies

**This is the part that is not in any paper and the reason the job is worth
a round trip.**

Write both as one nested model

```
P(k) = P_0(k) [ 1 + A_C (k/k_star)^(m_C) + A_D (k/k_star)^(m_D) L^(n-1) ]
```

and compute, symbolically:

1. **The parameter map.** `(A_C, m_C)` as explicit functions of
   `(gamma, rc, eps1, H, Mp, m0, Delta N)`, and `(A_D, m_D)` of
   `(kgamma, p, n, H_star lE, N_T, Delta N_star)`.
2. **The rank of each map's Jacobian** with respect to its own underlying
   parameters. This is the number that decides WP-3's free-parameter count:
   if the Jacobian of `(A_C, m_C)` has rank 2 in seven underlying
   parameters, then five combinations are unidentifiable from the power
   spectrum alone and the C side contributes **2** free parameters to the
   comparison, not seven. The analogous statement for the D side.
3. **The degenerate directions explicitly** — the null space of each
   Jacobian, as a list of invariant combinations. A reader must be able to
   see which physical parameters the CMB power spectrum cannot separate.
4. **Whether `m_C` and `m_D` can coincide**, and on what locus of
   `(p, n)`. If they can, the nested comparison is singular there and WP-3
   must say so rather than quoting a statistic across it. Solve
   `m_C = m_D` for `p` at each `m_C` from Part A and each integer
   `n >= 1`.

---

## Expected output form

A job without this section is refused by the runner. Exactly this, in this
order, printed one item per line as `label = value`:

```
PART_A_INFLATION_INDEX     m_C_inf      = <integer or exact rational>
PART_A_INFLATION_AMPLITUDE A_C_inf      = <exact expression in gamma, m0, rc, eps1, H, Mp, DeltaN>
PART_A_RADIATION_INDEX     m_C_rad      = <integer or exact rational>
PART_A_RADIATION_AMPLITUDE A_C_rad      = <exact expression>
PART_B_INDEX               m_D          = <expression in p and n>
PART_B_AMPLITUDE_N1        A_D(n=1)     = <exact expression>
PART_B_AMPLITUDE_N2        A_D(n=2)     = <exact expression>
PART_B_SADDLE_N3_AGREES    <TRUE or FALSE, and if FALSE the discrepancy>
PART_C_JACOBIAN_RANK_C     <integer>
PART_C_JACOBIAN_RANK_D     <integer>
PART_C_NULLSPACE_C         <list of invariant combinations>
PART_C_NULLSPACE_D         <list of invariant combinations>
PART_C_DEGENERACY_LOCUS    <solutions of m_C = m_D in p, per n and per epoch>
FREE_PARAMETERS_C          <integer: rank of the C map>
FREE_PARAMETERS_D          <integer: rank of the D map>
```

`FREE_PARAMETERS_C` and `FREE_PARAMETERS_D` are the two numbers WP-3 is
forbidden to report a comparison statistic without. If the job cannot
produce them it has failed, whatever else it printed.

Indices are expected to be **integers**. A non-integer index means the
super-Hubble expansion was taken wrongly or `eps2` was not handled as
declared, and the result should be treated as a failure, not as a finding.

---

## The validation target, stated before the job runs

The `k`-powers are published and the job must reproduce them. In the
convention `n_S - 1 = m` for the correction's contribution to the scalar
spectral index:

| Source | Published claim | Required Maple output |
| --- | --- | --- |
| MV 2020 eq. (powerSpectrum:infl), inflation crossing | "acquires a spectral index `n_S = 0`" | `m_C_inf = -1` |
| MV 2020 eq. (powerSpectrum:inf), settled after the transition | "a correction with a spectral index `n_S = 0`" | `m_C_inf = -1` (same) |
| MV 2020 eq. (powerSpectrum:rad), radiation crossing | "the CSL correction now has spectral index `n_S = -9`" | `m_C_rad = -10` |
| MVP 2012 abstract | "two branches, one which remains scale invariant and one with `n_S = 4`" | `m = 3` must appear as a branch of the same ODE |
| MV 2018 | correction scales as `k^(p+2n-7)` | `m_D = p + 2n - 7` |
| MV 2018 | `p = 7 - 2n` "preserves the quasi scale invariance" | `m_D = 0` at `p = 7 - 2n` |

MVP 2012's `n_S = 4` branch is the one cross-epoch check in the set: it
comes from a different paper and a different treatment, so recovering
`m = 3` from the same ODE is evidence the ODE is being solved rather than
the answer being pattern-matched.

## What would be surprising, and what to do about it

A tripwire list, not a prediction to defend.

1. **An index that is not an integer.** The expansion is wrong. Do not
   report it as a finding.
2. **`m_C_inf != -1` or `m_C_rad != -10`.** Either the job is wrong or MV
   2020 is. The check that distinguishes them: the collapse criterion,
   which MV 2020 state independently as `1/R - 1 = 1152 gamma rhobar_end
   (-k eta_end)^(-7) / m0^2` for inflation crossing and `1/R - 1 = 7264
   gamma (k eta_end)^(-14) (H_end rc)^(-7) / (11 m0^2)` for radiation
   crossing. These come from `Re Omega_k` and not from the source integral,
   so they are an independent handle on the same `gamma` scaling. If the
   job reproduces the `R` expressions but not the indices, the error is in
   the asymptotics of the integral; if it reproduces neither, the error is
   in `alpha_k`, `beta_k` or the conventions. **Report which.**
3. **`m = 3` does not appear as a branch.** Then either the de Sitter
   simplification is hiding it (check by restoring `eps2`), or MVP 2012's
   branch arises from a structure this job's ODE does not contain. The
   second would be a real finding about the two papers and must be reported
   as such, not smoothed over.
4. **`FREE_PARAMETERS_C = 1`.** Possible and would be important: it would
   mean the CSL power-spectrum correction is a one-parameter family, so the
   C-versus-D comparison is 1 against however many D has, and WP-3's
   statistic is much simpler than the plan assumed. Do not round it up to
   look safer.
5. **The degeneracy locus is non-empty at integer `n` and physical `p`.**
   Then WP-3 has a singular region and must report it. This is expected to
   happen at least once, since `m_C_inf = -1` and `m_D = p + 2n - 7` give
   `p = 6 - 2n`, which is the boundary of the paper's own first regime.
   **If the job does not find `p = 6 - 2n`, something is wrong.**

## Independent check

`crosscheck.py` in this directory, runnable with the repository venv:

```
.venv/Scripts/python maple/jobs/003-power-spectrum-corrections/crosscheck.py
```

It does three things in sympy, independently of Maple:

1. Builds `S_CSL` from `alpha_k`, `beta_k` by explicit differentiation and
   extracts the leading `k`-power of the source integral, for both epochs.
2. Checks the `m_D = p + 2n - 7` scaling and the `p = 7 - 2n`
   scale-invariance condition algebraically.
3. Solves `m_C = m_D` and reports the degeneracy loci.

It does **not** attempt Part C's Jacobian ranks, which is the part that
needs Maple's elimination. A cross-check is a cross-check and not a result:
where `crosscheck.py` and Maple disagree, the disagreement is the finding
and neither is adopted until it is resolved.

## Floating point

**None.** Every quantity in this job is exact. If any part of the output
has become numeric, say where and why; a symbolic result that silently
became numeric is not a symbolic result. The one permitted exception is the
`n >= 3` saddle-point comparison in Part B, which may be evaluated at
`Digits = 20` to decide `PART_B_SADDLE_N3_AGREES`, and if so must print the
precision used and the two values compared.
