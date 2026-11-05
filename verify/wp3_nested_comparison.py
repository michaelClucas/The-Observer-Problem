#!/usr/bin/env python
"""
WP-3: can Planck separate the collapse and decoherence corrections?

The plan's centrepiece. Run 01 recorded collapse (C) and decoherence (D)
as `genuine_conflict` in a predicted observable - both modify the curvature
power spectrum, with different functional forms - and found NO paper that
sets the two predictions against each other and asks which the data prefer.
This script asks.

It extends verify/planck_likelihood.py rather than building a second
pipeline, as the standing loop requires: the same three cobaya native
likelihood components, the same Planck 2018 best fit, and a baseline check
against the chi2 that script records, so a change anywhere shows up as a
failure rather than a different answer.

Governing cuts: data/001-planck-2018-plik-lite/cuts.md, committed BEFORE
this script was run, including its same-day addendum on the small-k
regularisation. Every choice below is fixed there and none was made after
seeing a result.

The model
---------
    P(k) = P_0(k) [ 1 + sum_i A_i (k/k_*)^(m_i) ]

with P_0 the base-LCDM power law, k_* = 0.05 Mpc^-1 the Planck pivot, and
m_i integers. The published indices, read at primary level 2026-11-05 and
recorded in maple/jobs/003-power-spectrum-corrections/JOB.md:

    C side, inflation-era crossing   m = -1    (Martin & Vennin 2020, n_S=0)
    C side, radiation-era crossing   m = -10   (Martin & Vennin 2020, n_S=-9)
    C side, 2012 non-SI branch       m = +3    (Martin, Vennin & Peter 2012)
    D side                           m = p+2n-7, any integer
                                     m = 0 at p = 7-2n (scale invariant)

Why a curvature matrix and not a sampler
----------------------------------------
P(k) is linear in each A_i and the transfer functions do not depend on the
A_i, so D_l is linear in the A_i and chi2 is EXACTLY quadratic in them. One
D_l response vector per index therefore determines the whole likelihood
surface, with no sampling. The script checks linearity explicitly and
refuses to report if the check fails.

What this is and is not
-----------------------
A PROFILE AT FIXED BACKGROUND. The six LCDM parameters are held at the
Planck best fit. cuts.md states the consequence in advance: this OVERSTATES
the constraint, because in a full fit the background would move to partially
absorb the correction, n_S most of all. So the profile can establish a D3 or
D4 verdict - if the shapes are inseparable with the background frozen,
marginalising cannot help - but it CANNOT establish a D1. That is written in
cuts.md before the result and is not revised here.

Free-parameter counts, computed in
maple/jobs/003-power-spectrum-corrections/crosscheck.py as symbolic
Jacobian ranks, not asserted:  C = 1, D = 2. Every statistic printed below
carries them.

Run:
    .venv/Scripts/python verify/wp3_nested_comparison.py
"""

import os
import sys

import numpy as np

PACKAGES_PATH = os.environ.get(
    "COSMO_PACKAGES", r"C:\Users\mluca\Documents\cosmo-packages"
)

# Planck 2018 TT,TE,EE+lowE base-LCDM best fit, identical to
# verify/planck_likelihood.py.
PARAMS = {
    "logA": 3.044,
    "ns": 0.9649,
    "H0": 67.36,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "tau": 0.0544,
    "mnu": 0.06,
}
A_PLANCK = 1.0
K_PIVOT = 0.05  # Mpc^-1, the Planck pivot; amplitudes are quoted here
LMAX = 2508

# Baseline chi2 recorded by verify/planck_likelihood.py on 2026-11-05.
BASELINE = {
    "plik_lite_TTTEEE": (583.935, 3.0),
    "lowl_TT": (23.419, 0.5),
    "lowl_EE_sroll2": (390.021, 3.0),
}

# Fixed in cuts.md before the fit.
C_INDICES = {-1: "C inflation-era crossing (n_S=0)",
             -10: "C radiation-era crossing (n_S=-9)",
             3: "C 2012 non-scale-invariant branch (n_S=4)"}
D_INDEX_RANGE = range(-12, 5)          # cuts.md: -12 .. +4
K_REG_VALUES = (1.0e-4, 3.0e-5)        # cuts.md addendum 1
K_REG_HI = 1.0                         # cuts.md addendum 2, Mpc^-1
K_GRID_MIN, K_GRID_MAX = 1.0e-6, 10.0  # camb integration range
PIVOT_STEP = 1.0e-3                    # correction at k_* for the response
# The window the CMB actually constrains: l = 2 to 2508 maps to roughly
# these comoving wavenumbers at the last-scattering distance. Used only to
# state where a correction has to be perturbative for the comparison to
# mean anything.
K_OBS_MIN, K_OBS_MAX = 1.4e-4, 0.2     # Mpc^-1

FAILURES = []


def report(name, ok, detail):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    for line in detail.splitlines():
        print(f"      {line}")
    if not ok:
        FAILURES.append(name)


# --------------------------------------------------------------- likelihoods

class Likelihoods:
    """The three cobaya native components, with their data loaded.

    Each exposes a clean entry point that takes D_l arrays (ell_factor=True,
    i.e. l(l+1)C_l/2pi in muK^2, indexed from l=0), so the chi2 can be
    evaluated on spectra this script computes rather than on spectra a
    cobaya provider computes. That is what makes a modified primordial
    spectrum possible without a custom theory class.
    """

    def __init__(self):
        from cobaya.model import get_model

        info = {
            "likelihood": {
                "planck_2018_highl_plik.TTTEEE_lite_native": None,
                "planck_2018_lowl.TT": None,
                "planck_2018_lowl.EE_sroll2": None,
            },
            "theory": {"camb": {"extra_args": {"halofit_version": "mead"}}},
            "params": dict(
                PARAMS,
                A_planck=A_PLANCK,
                # cobaya needs As derived from logA, exactly as
                # verify/planck_likelihood.py does it. Kept identical so the
                # baseline check below compares like with like.
                As={"value": "lambda logA: 1e-10*np.exp(logA)",
                    "derived": True},
            ),
            "packages_path": PACKAGES_PATH,
            "debug": False,
        }
        self.model = get_model(info)
        liks = self.model.likelihood
        self.plik = liks["planck_2018_highl_plik.TTTEEE_lite_native"]
        self.lowl_tt = liks["planck_2018_lowl.TT"]
        self.lowl_ee = liks["planck_2018_lowl.EE_sroll2"]

    def chi2(self, dl):
        """Total chi2 and the per-component breakdown, from D_l dict."""
        c_plik = self.plik.get_chi_squared(
            0, dl["tt"], dl["te"], dl["ee"], A_PLANCK
        )
        c_tt = -2.0 * self.lowl_tt.log_likelihood(dl["tt"], A_PLANCK)
        c_ee = -2.0 * self.lowl_ee.log_likelihood(dl["ee"], A_PLANCK)
        return {
            "plik_lite_TTTEEE": float(c_plik),
            "lowl_TT": float(c_tt),
            "lowl_EE_sroll2": float(c_ee),
            "total": float(c_plik + c_tt + c_ee),
        }


# ------------------------------------------------------------------- spectra

def primordial_factory(amplitudes, k_reg):
    """P(k)/P_0(k) = 1 + sum A_i (k/k_*)^m_i, regularised below k_reg.

    `amplitudes` maps index m -> amplitude A. Regularisation per cuts.md's
    addendum: the correction factor is evaluated as published for
    k >= k_reg and held at its k_reg value below, because the corrections
    are derived for super-Hubble modes of cosmological interest and not for
    k decades below anything observable.
    """
    a_s = np.exp(PARAMS["logA"]) / 1.0e10
    n_s = PARAMS["ns"]

    def p_scalar(k):
        k = np.atleast_1d(np.asarray(k, dtype=float))
        # cuts.md addenda 1 and 2: the correction is evaluated as published
        # only inside [k_reg, K_REG_HI] and held constant outside, because
        # that window contains everything the CMB measures and the
        # derivations do not cover modes outside it.
        k_eff = np.clip(k, k_reg, K_REG_HI)
        corr = np.zeros_like(k_eff)
        for m, amp in amplitudes.items():
            if amp != 0.0:
                corr += amp * (k_eff / K_PIVOT) ** float(m)
        p0 = a_s * (k / K_PIVOT) ** (n_s - 1.0)
        return p0 * (1.0 + corr)

    return p_scalar


def dl_from_camb(amplitudes, k_reg):
    """D_l for TT, TE, EE in muK^2, from camb with the modified P(k).

    Returns None if the modified P(k) is non-positive anywhere on the grid,
    which cuts.md declares is exclusion by the DERIVATION's perturbative
    domain and not exclusion by the data. The two are reported separately.
    """
    import camb

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=PARAMS["H0"],
        ombh2=PARAMS["ombh2"],
        omch2=PARAMS["omch2"],
        mnu=PARAMS["mnu"],
        tau=PARAMS["tau"],
    )
    pars.set_for_lmax(LMAX, lens_potential_accuracy=1)

    p_scalar = primordial_factory(amplitudes, k_reg)
    k_test = np.logspace(-6, 1, 4000)
    if np.any(p_scalar(k_test) <= 0.0):
        return None

    # effective_ns_for_nonlinear is required by camb's splined initial
    # power: the halofit fitting formula needs a single effective tilt and
    # cannot read one off an arbitrary P(k). Set to the base-LCDM n_s, which
    # is correct to the order the correction is being treated at, since the
    # correction is a small perturbation on the power law.
    pars.set_initial_power_function(
        p_scalar, kmin=1e-6, kmax=10.0, N_min=400,
        effective_ns_for_nonlinear=PARAMS["ns"],
    )
    results = camb.get_results(pars)
    cl = results.get_cmb_power_spectra(
        pars, CMB_unit="muK", spectra=("total",), raw_cl=False
    )["total"]
    # camb returns columns TT, EE, BB, TE as l(l+1)C_l/2pi, index = l.
    n = min(LMAX + 1, cl.shape[0])
    return {
        "tt": np.ascontiguousarray(cl[:n, 0]),
        "ee": np.ascontiguousarray(cl[:n, 1]),
        "te": np.ascontiguousarray(cl[:n, 3]),
    }


# ------------------------------------------------------------------- the fit

def check_baseline(liks):
    """The direct-call route must reproduce verify/planck_likelihood.py."""
    detail = []
    ok = True
    dl0 = dl_from_camb({}, K_REG_VALUES[0])
    if dl0 is None:
        report("baseline reproduces verify/planck_likelihood.py", False,
               "baseline P(k) came out non-positive, which is impossible")
        return None, None
    c = liks.chi2(dl0)
    for name, (want, tol) in BASELINE.items():
        got = c[name]
        agree = abs(got - want) <= tol
        if not agree:
            ok = False
        detail.append(
            f"{name:<22s} chi2 = {got:9.3f}   recorded {want:9.3f} "
            f"+/- {tol:<4.1f} {'AGREES' if agree else 'DISAGREES'}"
        )
    detail.append(f"{'TOTAL':<22s} chi2 = {c['total']:9.3f}")
    detail.append("")
    detail.append(
        "This matters more than it looks: it shows that calling the three "
        "likelihoods' chi2 entry points on spectra computed here gives the "
        "same answer as routing them through a cobaya provider. Without it, "
        "a modified-spectrum result could differ from the baseline for a "
        "plumbing reason rather than a physical one."
    )
    report("baseline reproduces verify/planck_likelihood.py", ok,
           "\n".join(detail))
    return (dl0, c) if ok else (None, None)


def step_for(m):
    """Amplitude step: the correction is PIVOT_STEP at the pivot k_*.

    Normalising at the pivot, not at the regularisation scale. The first
    version normalised at k_reg, which for a steep negative index made the
    pivot amplitude about 1e-30 and the observable effect unmeasurably
    small - every pair then came back "degenerate" with curvature
    eigenvalues at the 1e-9 rounding level, which was an artefact of the
    normalisation and not a statement about the sky. cuts.md says the
    amplitudes are quoted at the pivot, so the step belongs there too.
    """
    return PIVOT_STEP


def perturbative_max_amplitude(m):
    """Largest pivot amplitude keeping |correction| <= 1 across the CMB window.

    This is a bound from the DERIVATION, not from the data: both
    corrections are first-order results, so an amplitude that makes the
    correction order unity somewhere the CMB measures is outside the domain
    in which either was derived. Reported separately from any data
    constraint, per cuts.md.
    """
    lo = (K_OBS_MIN / K_PIVOT) ** float(m)
    hi = (K_OBS_MAX / K_PIVOT) ** float(m)
    return 1.0 / max(abs(lo), abs(hi))


def responses(liks, dl0, k_reg, indices):
    """D_l response per unit amplitude, for each index. One camb run each."""
    out = {}
    excluded = {}
    steps = {}
    for m in indices:
        a_pert = perturbative_max_amplitude(m)
        if a_pert < PIVOT_STEP:
            excluded[m] = (
                f"perturbativity bounds the pivot amplitude at "
                f"|A| <= {a_pert:.3e}, below the {PIVOT_STEP:.0e} response "
                f"step; the branch is excluded by its own derivation's "
                f"domain before Planck is consulted"
            )
            continue
        h = step_for(m)
        try:
            dl_h = dl_from_camb({m: h}, k_reg)
        except Exception as exc:
            excluded[m] = f"camb failed at A = {h:.3e}: {type(exc).__name__}"
            continue
        if dl_h is None:
            excluded[m] = f"P(k) non-positive at A = {h:.3e}"
            continue
        out[m] = {key: (dl_h[key] - dl0[key]) / h for key in ("tt", "te", "ee")}
        steps[m] = h
    return out, excluded, steps


def check_linearity(liks, dl0, resp, k_reg, steps):
    """D_l must be linear in the amplitude or the quadratic form is invalid."""
    detail = []
    ok = True
    # Pick an index that is well inside the observable range so the test is
    # not dominated by the regularisation.
    m_test = 0 if 0 in resp else sorted(resp)[len(resp) // 2]
    h = steps[m_test]
    dl_2h = dl_from_camb({m_test: 2.0 * h}, k_reg)
    if dl_2h is None:
        report("D_l linear in the amplitude", False,
               f"could not evaluate at A = {2 * h:g} for m = {m_test}")
        return False
    worst = 0.0
    for key in ("tt", "te", "ee"):
        predicted = dl0[key] + 2.0 * h * resp[m_test][key]
        actual = dl_2h[key]
        scale = np.max(np.abs(actual)) or 1.0
        rel = np.max(np.abs(predicted - actual)) / scale
        worst = max(worst, rel)
        detail.append(f"{key.upper():>3s}: max relative departure = {rel:.3e}")
    agree = worst < 1.0e-6
    if not agree:
        ok = False
    detail.append(
        f"tested at m = {m_test}, A = {h:g} against A = {2 * h:g}; "
        f"worst = {worst:.3e}, tolerance 1e-6: "
        f"{'AGREES' if agree else 'DISAGREES'}"
    )
    detail.append(
        "Linear D_l means chi2 is exactly quadratic in the amplitudes, so "
        "the curvature matrix below is the whole likelihood surface and no "
        "sampler is needed. If this check fails the numbers are not reported."
    )
    report("D_l linear in the amplitude", ok, "\n".join(detail))
    return ok


def chi2_of(liks, dl0, resp, amps):
    """chi2 at a vector of amplitudes, from the cached responses. No camb."""
    dl = {key: dl0[key].copy() for key in ("tt", "te", "ee")}
    for m, a in amps.items():
        if a == 0.0:
            continue
        for key in ("tt", "te", "ee"):
            dl[key] += a * resp[m][key]
    return liks.chi2(dl)["total"]


def curvature(liks, dl0, resp, m_i, m_j, c0, steps):
    """Curvature of chi2 in SCALED amplitudes a_i = A_i / h_i.

    Scaling matters and the first version of this function got it wrong.
    The per-index steps h_i span thirty orders of magnitude, so a curvature
    matrix built in the raw amplitudes A_i has a condition number around
    1e60 and inverting it returns arithmetic noise - that version produced
    |rho| > 1 and non-positive-definite matrices, which are impossible and
    were the symptom. In the scaled variables every diagonal entry is O(1)
    by construction, because h_i was chosen to make the correction 1e-3 on
    the grid for every i.

    chi2 is exactly quadratic in the amplitudes (the linearity check above
    establishes it), so this is not an approximation: F is the whole
    likelihood surface. rho is invariant under the rescaling, and
    sigma(A_i) = h_i * sigma(a_i) recovers the physical units.
    """
    def c(ai, aj):
        return chi2_of(
            liks, dl0, resp, {m_i: ai * steps[m_i], m_j: aj * steps[m_j]}
        )

    cpp, cmm = c(1.0, 1.0), c(-1.0, -1.0)
    cpm, cmp_ = c(1.0, -1.0), c(-1.0, 1.0)
    cip, cim = c(1.0, 0.0), c(-1.0, 0.0)
    cjp, cjm = c(0.0, 1.0), c(0.0, -1.0)

    f_ii = (cip + cim - 2.0 * c0) / 2.0
    f_jj = (cjp + cjm - 2.0 * c0) / 2.0
    f_ij = (cpp + cmm - cpm - cmp_) / 8.0
    return np.array([[f_ii, f_ij], [f_ij, f_jj]])


def sigmas_and_rho(f, steps, m_i, m_j, cond_max=1.0e12):
    """sigma(A_i), sigma(A_j), rho from the scaled curvature matrix.

    Returns (None, None, None, reason) when the matrix is not usable. A
    matrix too ill-conditioned to invert is not a failure to report: it is
    the statement that the two shapes are degenerate in this data to within
    the precision available, which is a physical claim and is reported as
    one.
    """
    if not np.all(np.isfinite(f)):
        return None, None, None, "curvature matrix not finite"
    eig = np.linalg.eigvalsh(f)
    if eig[0] <= 0.0:
        return None, None, None, (
            f"curvature not positive definite (min eigenvalue "
            f"{eig[0]:.3e}); the pair is degenerate at this precision"
        )
    cond = eig[-1] / eig[0]
    if cond > cond_max:
        return None, None, None, (
            f"condition number {cond:.3e} exceeds {cond_max:.0e}; "
            f"degenerate at this precision"
        )
    cov = np.linalg.inv(f)
    s_i = float(np.sqrt(cov[0, 0])) * steps[m_i]
    s_j = float(np.sqrt(cov[1, 1])) * steps[m_j]
    rho = float(cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1]))
    rho = max(-1.0, min(1.0, rho))
    return s_i, s_j, rho, f"cond = {cond:.3e}"


def analyse(liks, dl0, c0, k_reg):
    """The comparison, for every (m_C, m_D) pair cuts.md admits."""
    detail = []
    ok = True

    indices = sorted(set(C_INDICES) | set(D_INDEX_RANGE))
    detail.append(f"k_reg = {k_reg:g} Mpc^-1;  computing up to {len(indices)} "
                  f"D_l response vectors (one camb run each)")
    detail.append(
        f"Perturbativity bound on the pivot amplitude, across the window "
        f"the CMB constrains (k = {K_OBS_MIN:g} to {K_OBS_MAX:g} Mpc^-1). "
        f"This is a bound from the DERIVATION, not from the data."
    )
    for m in indices:
        detail.append(
            f"  m = {m:>3d}: |A| <= {perturbative_max_amplitude(m):.4e} "
            f"for the first-order treatment to hold"
        )
    detail.append("")
    resp, excluded, steps = responses(liks, dl0, k_reg, indices)
    for m, why in sorted(excluded.items()):
        detail.append(f"  m = {m:>3d}: EXCLUDED BY THE DERIVATION - {why}")
    if excluded:
        detail.append(
            "  Those are excluded by the perturbative domain the corrections "
            "were derived in, NOT by the data. cuts.md requires the two "
            "exclusions be kept separate and they are."
        )
    detail.append("")

    if not check_linearity(liks, dl0, resp, k_reg, steps):
        return False, []

    rows = []
    detail.append(
        "Pairwise comparison. sigma is the 1-sigma constraint on each "
        "amplitude at the pivot k_* = 0.05 Mpc^-1 from the 2x2 curvature "
        "matrix with the other amplitude free; rho is their correlation."
    )
    detail.append(
        "FREE PARAMETERS: C side 1, D side 2. Both counts attached to every "
        "row, per the standing loop. A statistic without them is "
        "uninterpretable, not a weak result."
    )
    detail.append("")
    detail.append(
        f"  {'m_C':>4s} {'m_D':>4s} {'sigma(A_C)':>12s} {'sigma(A_D)':>12s} "
        f"{'rho':>9s} {'1-|rho|':>10s}  verdict / reason"
    )

    for m_c in sorted(C_INDICES):
        if m_c not in resp:
            continue
        for m_d in D_INDEX_RANGE:
            if m_d not in resp:
                continue
            if m_d == m_c:
                detail.append(
                    f"  {m_c:>4d} {m_d:>4d} {'-':>12s} {'-':>12s} "
                    f"{'-':>9s} {'-':>10s}  SINGULAR: identical functions, "
                    f"no comparison has content"
                )
                continue
            f = curvature(liks, dl0, resp, m_c, m_d, c0, steps)
            s_c, s_d, rho, why = sigmas_and_rho(f, steps, m_c, m_d)
            if s_c is None:
                detail.append(
                    f"  {m_c:>4d} {m_d:>4d} {'-':>12s} {'-':>12s} "
                    f"{'-':>9s} {'-':>10s}  NOT SEPARABLE: {why}"
                )
                rows.append((m_c, m_d, None, None, None, k_reg))
                continue
            sep = 1.0 - abs(rho)
            verdict = (
                "NOT separable" if sep < 1.0e-3
                else "separable" if sep > 0.05
                else "marginal"
            )
            rows.append((m_c, m_d, s_c, s_d, rho, k_reg))
            detail.append(
                f"  {m_c:>4d} {m_d:>4d} {s_c:>12.4e} {s_d:>12.4e} "
                f"{rho:>9.5f} {sep:>10.3e}  {verdict}"
            )

    report(f"nested C-vs-D comparison at k_reg = {k_reg:g} Mpc^-1",
           ok, "\n".join(detail))
    return ok, rows


def math_sqrt(x):
    import math
    return math.sqrt(x)


def main():
    print("WP-3: can Planck separate the collapse and decoherence corrections?")
    print("=" * 78)
    print("Governing cuts: data/001-planck-2018-plik-lite/cuts.md, committed")
    print("before this script was run, addendum included.")
    print("Profile at FIXED background: can establish D3/D4, cannot establish")
    print("D1. That is stated in cuts.md in advance, not here in hindsight.")
    print()

    try:
        liks = Likelihoods()
    except Exception as exc:
        print(f"FAIL  could not build the likelihoods: {exc}")
        print(f"      packages path: {PACKAGES_PATH}")
        return 1

    dl0, c = check_baseline(liks)
    if dl0 is None:
        print()
        print("Baseline failed; nothing downstream is reported.")
        return 1
    c0 = c["total"]
    print()

    all_rows = []
    for k_reg in K_REG_VALUES:
        ok, rows = analyse(liks, dl0, c0, k_reg)
        all_rows.extend(rows)
        print()

    # The k_reg sensitivity test cuts.md requires.
    detail = []
    ok = True
    by_key = {}
    for m_c, m_d, s_c, s_d, rho, k_reg in all_rows:
        by_key.setdefault((m_c, m_d), {})[k_reg] = (s_c, s_d, rho)
    detail.append(
        "cuts.md requires this: a constraint that depends on an unobservable "
        "regularisation is not a constraint on the sky. Ratio of sigma(A_C) "
        "between the two k_reg values, per C index."
    )
    detail.append("")
    worst_by_mc = {}
    for (m_c, m_d), d in sorted(by_key.items()):
        if len(d) < 2:
            continue
        k1, k2 = K_REG_VALUES
        if d[k1][0] is None or d[k2][0] is None:
            # One or both k_reg values gave a degenerate pair; that is
            # itself maximal sensitivity and is recorded as such.
            worst_by_mc.setdefault(m_c, []).append(float("inf"))
            continue
        r_c = d[k2][0] / d[k1][0]
        worst_by_mc.setdefault(m_c, []).append(abs(r_c - 1.0))
    for m_c in sorted(worst_by_mc):
        worst = max(worst_by_mc[m_c])
        stable = worst < 0.05
        detail.append(
            f"  m_C = {m_c:>3d} [{C_INDICES[m_c]}]: worst fractional change "
            f"in sigma(A_C) across k_reg = {worst:.3e}  "
            f"{'STABLE' if stable else 'SENSITIVE'}"
        )
        if not stable:
            detail.append(
                f"       So the constraint on this branch is NOT a constraint "
                f"on the sky: it is set by the regularisation, i.e. by modes "
                f"the CMB does not measure. Reported as such, not as a number."
            )
    report("k_reg sensitivity, per cuts.md", ok, "\n".join(detail))
    print()

    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {', '.join(FAILURES)}")
        return 1
    print("PASS: all checks. Free-parameter counts: C = 1, D = 2.")
    print("Fixed-background profile; D1 is NOT established by this, per cuts.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
