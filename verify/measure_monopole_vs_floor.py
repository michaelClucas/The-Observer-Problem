#!/usr/bin/env python
"""
WP-5: the measure-predicted signal against the single-sky floor.

Run 01 recorded the causal-patch and fat-geodesic measures as predicting a
one-point expectation value for the gauge-invariant Newtonian potential and
a related three-point contribution, with forms that differ between the
measures but both "well within cosmic variance" - and recorded that as
CITED, not computed. This script checks the arithmetic of the suppression
and the structure of the floor it is being compared against.

WHAT THIS IS NOT: it is not a substitute for Maple job 002. Job 002
computes closed-form irreducible variances for three classes of statistic
as functions of multipole, sky fraction and the underlying C_l. That job is
queued (issue michaelClucas/The-Observer-Problem#9) and has not returned,
and the standing loop forbids substituting a cross-check for a filed job.

What this script does instead is narrower and does not need job 002: the
measure signal lives entirely in the MONOPOLE, l = m = 0, and the mode
count at l = 0 is one. That is combinatorics, not a symbolic computation,
and it is an INPUT to whatever formula job 002 returns rather than its
output. The conclusion that follows from it - that no better measurement
lifts this signal above the floor - therefore does not depend on job 002's
value, only on its structure. The numeric ratio Delta / sigma_floor does
depend on job 002 and is NOT computed here.

Source, read at primary level 2026-11-05 as LaTeX source from
arxiv.org/e-print/1204.1569 (`c.tex`): Salem, "The CMB and the measure of
the multiverse", JHEP 06 (2012) 153.

The three statements taken from it, each quoted in the findings document:

S1. The prediction, from the conclusions: the one-point expectation value
    is a scale-dependent monopole,
        <Psi_{k l m}>_obs = Psibar_{k00} k delta_{l0} delta_{m0}
    with the precise form of Psibar_{k00} differing between the measures
    but in both cases the dominant behaviour
        Psibar_{k00} ~ k^2 rCMB^2 P(k).

S2. The suppression, from section 5: the result "differs by a factor of
    order k^(1/2) [k^3 P(k)]^(1/2)", the bracket gives "an order 10^-5
    suppression", and compensating for it with the k^(1/2) factor "would
    require examining extremely small scales, k rCMB ~ 10^10, well beyond
    the validity of our analysis and beyond any foreseeable observation".

S3. The irreducibility, from section 5, which is the statement that makes
    this a D3 rather than a small number: "even in a map of perturbations
    with more three-dimensional resolution, we expect the 3-point
    correlator to fall within cosmic variance, since restricting to the
    single l = m = 0 mode does not allow one to reduce the uncertainty as
    is usually done by averaging over many m at large l".

Exits non-zero if any check fails.
"""

import math
import sys

FAILURES = []

# Comoving distance to last scattering, Planck 2018 base-LCDM.
# Planck 2018 results VI, Table 2: comoving angular diameter distance to
# last scattering D_A = 13869 Mpc for the TT,TE,EE+lowE+lensing column.
R_CMB_MPC = 13869.0

# Dimensionless curvature perturbation amplitude: [k^3 P(k)]^(1/2) is of
# order the CMB's one-part-in-100000 anisotropy. Salem's "order 10^-5".
DELTA_ZETA = 1.0e-5

# The largest wavenumber Planck constrains, from the data's own lmax = 2508
# and k ~ l / D_A.
K_MAX_PLANCK = 2508.0 / R_CMB_MPC

# Where linear perturbation theory stops being usable at z = 0.
K_NONLINEAR_MPC = 0.2


def report(name, ok, detail):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    for line in detail.splitlines():
        print(f"      {line}")
    if not ok:
        FAILURES.append(name)


def check_1_mode_count_and_floor_structure():
    """The signal is a monopole, and a monopole has exactly one mode."""
    detail = []
    ok = True

    # Independent modes at multipole l on a full sky: 2l+1.
    # The standard single-sky fractional uncertainty on a power spectrum
    # estimate at multipole l, full sky, is sqrt(2/(2l+1)).
    detail.append(
        "Independent modes at multipole l on the full sky: 2l+1. "
        "Single-sky fractional uncertainty on C_l: sqrt(2/((2l+1) f_sky))."
    )
    detail.append("")
    detail.append(f"  {'l':>6s} {'modes':>8s} {'frac. sigma (f_sky=1)':>24s}")
    for ell in (0, 1, 2, 10, 100, 1000, 2508):
        modes = 2 * ell + 1
        frac = math.sqrt(2.0 / modes)
        detail.append(f"  {ell:>6d} {modes:>8d} {frac:>24.4f}")

    monopole_modes = 2 * 0 + 1
    monopole_frac = math.sqrt(2.0 / monopole_modes)
    exact = monopole_modes == 1
    if not exact:
        ok = False
    detail.append("")
    detail.append(
        f"At l = 0 the mode count is {monopole_modes} and the fractional "
        f"uncertainty is {monopole_frac:.4f}, i.e. "
        f"{100 * monopole_frac:.0f} per cent."
    )
    detail.append(
        "The 2l+1 averaging that shrinks the uncertainty at high l has "
        "nothing to average: there is one monopole on the sky and there will "
        "only ever be one. This is Salem's statement S3, and it is why the "
        "measure signal is floor-limited in the strongest sense rather than "
        "merely small."
    )
    detail.append("")
    detail.append(
        "NOT CLAIMED: the numeric value of sigma_floor for a one-point or "
        "three-point statistic. That is Maple job 002's output, it is still "
        "queued, and the standing loop forbids substituting for a filed job. "
        "What is claimed is the mode count, which is arithmetic, and which "
        "is an input to job 002 rather than its result."
    )

    report("the signal is a monopole and a monopole has one mode",
           ok, "\n".join(detail))


def check_2_suppression_arithmetic():
    """Salem's k rCMB ~ 1e10 requirement, checked."""
    detail = []
    ok = True

    # Salem S2: the one-point function differs from a typical perturbation
    # by a factor of order k^(1/2) [k^3 P(k)]^(1/2). Writing k in units of
    # 1/rCMB, the k^(1/2) factor is (k rCMB)^(1/2), so the signal reaches a
    # typical perturbation's size when
    #     (k rCMB)^(1/2) * DELTA_ZETA ~ 1
    #  => k rCMB ~ DELTA_ZETA^-2.
    k_rcmb_needed = DELTA_ZETA ** (-2)
    detail.append(
        f"Suppression from the bracket: [k^3 P(k)]^(1/2) ~ {DELTA_ZETA:.0e}"
    )
    detail.append(
        f"Compensating with (k rCMB)^(1/2) requires "
        f"(k rCMB)^(1/2) ~ 1/{DELTA_ZETA:.0e}, i.e. "
        f"k rCMB ~ {k_rcmb_needed:.3e}"
    )
    agrees = abs(math.log10(k_rcmb_needed) - 10.0) < 0.01
    if not agrees:
        ok = False
    detail.append(
        f"Salem states k rCMB ~ 1e10: "
        f"{'AGREES' if agrees else 'DISAGREES'} "
        f"(computed exponent {math.log10(k_rcmb_needed):.2f})"
    )
    detail.append("")

    # Translate that into a physical wavenumber and compare against what is
    # observable and against where perturbation theory stops.
    k_needed = k_rcmb_needed / R_CMB_MPC
    detail.append(f"rCMB = {R_CMB_MPC:.0f} Mpc (Planck 2018 base-LCDM)")
    detail.append(f"k needed = {k_needed:.4e} Mpc^-1")
    detail.append(
        f"Planck's reach, k ~ lmax/rCMB with lmax = 2508: "
        f"{K_MAX_PLANCK:.4e} Mpc^-1"
    )
    ratio_obs = k_needed / K_MAX_PLANCK
    detail.append(
        f"  -> a factor {ratio_obs:.3e} beyond Planck, i.e. "
        f"{math.log10(ratio_obs):.1f} orders of magnitude"
    )
    ratio_nl = k_needed / K_NONLINEAR_MPC
    detail.append(
        f"Linear perturbation theory stops being usable around "
        f"k ~ {K_NONLINEAR_MPC:g} Mpc^-1"
    )
    detail.append(
        f"  -> the required scale is a factor {ratio_nl:.3e} inside the "
        f"nonlinear regime, {math.log10(ratio_nl):.1f} orders of magnitude"
    )
    detail.append("")
    detail.append(
        "So the scale at which the measure signal would become comparable "
        "to a typical perturbation is not merely unobserved. It is about "
        f"{math.log10(ratio_nl):.0f} orders of magnitude inside the regime "
        "where the linear calculation that produced the prediction has "
        "stopped applying. Salem says this in words - 'well beyond the "
        "validity of our analysis' - and the arithmetic agrees."
    )
    deep = ratio_nl > 1.0e6
    if not deep:
        ok = False
    detail.append(
        f"Check that the required scale is at least 1e6 beyond the "
        f"nonlinear scale: {'AGREES' if deep else 'DISAGREES'}"
    )

    report("the suppression arithmetic and what scale would beat it",
           ok, "\n".join(detail))


def check_3_what_job_002_would_add():
    """State precisely what is still missing, so nothing is overclaimed."""
    detail = []
    detail.append(
        "What this script establishes, and what it does not, written out so "
        "the verdict in findings/005 can be read against it."
    )
    detail.append("")
    detail.append("ESTABLISHED here:")
    detail.append(
        "  - the measure signal is confined to l = m = 0, on Salem's "
        "statement S1 and S3;"
    )
    detail.append(
        "  - the mode count at l = 0 is exactly 1, so the averaging that "
        "reduces cosmic variance at high l is unavailable, whatever the "
        "floor's numeric value turns out to be;"
    )
    detail.append(
        "  - Salem's k rCMB ~ 1e10 requirement is arithmetically correct, "
        "and that scale is ~6 orders of magnitude inside the nonlinear "
        "regime where the prediction's own derivation fails."
    )
    detail.append("")
    detail.append("NOT established here, and needing Maple job 002:")
    detail.append(
        "  - the numeric value of sigma_floor for a one-point statistic;"
    )
    detail.append("  - therefore the numeric ratio Delta / sigma_floor.")
    detail.append("")
    detail.append(
        "The distinction matters for the bin. A D3 verdict needs "
        "Delta <= sigma_floor. The three established points give that "
        "inequality's DIRECTION without its magnitude: the signal sits in "
        "the one place on the sky where the floor cannot be beaten down by "
        "averaging, and reaching a typical-perturbation amplitude would "
        "require a scale where the prediction does not hold. Job 002 "
        "supplies the ratio, which is worth having, but cannot reverse the "
        "direction, because no value of sigma_floor changes the fact that "
        "l = 0 has one mode."
    )
    report("what is established and what still needs job 002", True,
           "\n".join(detail))


def main():
    print("WP-5: the measure-predicted monopole against the single-sky floor")
    print("=" * 78)
    print("Source read at primary level: arXiv:1204.1569 (Salem, JHEP 2012).")
    print("This script does NOT substitute for Maple job 002; see the")
    print("docstring and check 3.")
    print()
    check_1_mode_count_and_floor_structure()
    print()
    check_2_suppression_arithmetic()
    print()
    check_3_what_job_002_would_add()
    print()
    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {', '.join(FAILURES)}")
        return 1
    print("PASS: all checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
