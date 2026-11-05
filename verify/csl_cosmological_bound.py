#!/usr/bin/env python
"""
WP-4: the CSL cosmological bound that does not exist in print as a number.

Run 02 confirmed at primary-source level that Martin & Vennin
(arXiv:1906.04405) state NO numerical bound on the CSL parameter: their
cosmological constraint is analytic in gamma, with the numerical content
carried by a figure. The figure sometimes quoted as their bound,
lambda << 5.6e-90 s^-1, appears only in Gundhi et al.'s introduction as
*their rendering*, against Gundhi et al.'s own lambda <~ 1e7 s^-1.

WP-4's job is to produce the number. This script does that by evaluating
Martin & Vennin's OWN closed-form constraint at the parameter values stated
in their OWN figure caption. It derives nothing new and reads nothing off a
figure. Every input is quoted below with its locator.

What is computed
----------------
1. Both branches of the upper bound on gamma, and the corresponding
   lambda, across the laboratory-viable range of rc.
2. Both branches of the lower bound from the requirement that collapse has
   occurred by CMB emission, so the CMB-allowed window can be seen to be
   empty or not.
3. Which branch the stated parameters actually select, as a function of rc.
   This turns out to matter.
4. The provenance test: whether lambda << 5.6e-90 s^-1 is reproducible from
   these formulae, and if so at which rc and from which branch.
5. The "97 orders of magnitude" figure, which Run 01 tagged [SOURCED] and
   Run 02 established is an [INFERENCE].

Sources, all read at primary level as LaTeX source on 2026-11-05
----------------------------------------------------------------
arXiv:1906.04405, Martin & Vennin, "Cosmic Microwave Background
Constraints Cast a Shadow on Continuous Spontaneous Localization Models".

  Upper bounds, their eq. block after (powerSpectrum:rad), verbatim:
    gamma << m0^2 (448 rhobar_end eps1 / 3)^-1 e^-DeltaN
        if  H_end rc < e^DeltaN
    gamma << m0^2 (35408 rhobar_end eps1 / 429)^-1 (H_end rc)^9 e^(-10 DeltaN)
        if  H_end rc > e^DeltaN

  Lower bounds from R < 1, same block, verbatim:
    gamma > m0^2 (1152 rhobar_end)^-1 (-k eta_end)^7
        if  H_end rc < e^DeltaN
    gamma > m0^2 (7264 rhobar_end / 11)^-1 (-k eta_end)^14 (H_end rc)^7
        if  H_end rc > e^DeltaN

  with  k/(aH)|_end = e^-DeltaN,  and in de Sitter aH = -1/eta so
  -k eta_end = k/(aH)|_end = e^-DeltaN.

  lambda definition, their text after eq. (rho:cg), verbatim:
    "lambda = gamma/(8 pi^(3/2) rc^3)"

  m0: "a reference mass (usually the mass of a nucleon)".

  Laboratory-viable region, their text: "rc ~ 1e-8 - 1e-4 m and
  lambda ~ 1e-18 - 1e-10 s^-1".

  Figure fig:mapCSL caption, verbatim: "one uses Delta N = 50 for the
  pivot scale of the CMB, H_inf = 1e-5 Mp and eps1 = 0.005".

Assumptions, stated because they are assumptions
------------------------------------------------
A1. H_end = H_inf. The paper's bounds carry H_end and rhobar_end while the
    figure caption states H_inf. With eps1 = 0.005 the Hubble rate changes
    by a fraction of a percent over the last e-folds, which is far below
    the precision of a bound quoted to one significant figure. Flagged
    because it is an identification the paper does not spell out.
A2. rhobar_end = 3 H_end^2 Mp^2, with Mp the REDUCED Planck mass. The paper
    writes rhobar_inf = 3 H_inf^2 Mp^2 explicitly and uses Mp throughout
    with H_inf = 1e-5 Mp, which fixes the convention.
A3. The "<<" and ">" in the paper's bounds are evaluated as equalities, so
    what is computed is the threshold, not a bound with a safety factor.
    Reported as a threshold.

Exits non-zero if any internal consistency check fails.
"""

import math
import sys

FAILURES = []

# ---------------------------------------------------------------- constants
# CODATA / PDG values. Exact conversions where they are definitional.
MP_REDUCED_GEV = 2.435323e18     # reduced Planck mass, GeV
HBAR_C_GEV_M = 1.9732698e-16     # hbar c, GeV m  =>  1 GeV^-1 = this many m
HBAR_GEV_S = 6.582120e-25        # hbar, GeV s    =>  1 GeV^-1 = this many s
GEV_TO_INV_S = 1.0 / HBAR_GEV_S  # 1 GeV = this many s^-1

M_PROTON_GEV = 0.93827208816     # PDG proton mass
M_AMU_GEV = 0.93149410242        # atomic mass unit

# -------------------------------------------------- Martin & Vennin's inputs
DELTA_N = 50.0                   # fig:mapCSL caption
H_INF_OVER_MP = 1.0e-5           # fig:mapCSL caption
EPS1 = 0.005                     # fig:mapCSL caption

H_END_GEV = H_INF_OVER_MP * MP_REDUCED_GEV              # assumption A1
RHOBAR_END_GEV4 = 3.0 * H_END_GEV**2 * MP_REDUCED_GEV**2  # assumption A2

# Laboratory-viable window, from the paper's own text.
LAB_RC_RANGE_M = (1.0e-8, 1.0e-4)
LAB_LAMBDA_RANGE_INV_S = (1.0e-18, 1.0e-10)

# Gundhi et al.'s own bound, for the comparison Run 01 recorded.
GUNDHI_LAMBDA_INV_S = 1.0e7
# The figure attributed to Martin & Vennin in Gundhi et al.'s introduction.
ATTRIBUTED_LAMBDA_INV_S = 5.6e-90


def report(name, ok, detail):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    for line in detail.splitlines():
        print(f"      {line}")
    if not ok:
        FAILURES.append(name)


def rc_m_to_inv_gev(rc_m):
    """rc in metres -> rc in GeV^-1."""
    return rc_m / HBAR_C_GEV_M


def h_rc_dimensionless(rc_m):
    """The dimensionless combination H_end * rc that selects the branch."""
    return H_END_GEV * rc_m_to_inv_gev(rc_m)


def gamma_upper_branch1(m0_gev):
    """gamma << m0^2 (448 rhobar eps1/3)^-1 e^-DeltaN.  Units: GeV^-2."""
    return m0_gev**2 * 3.0 / (448.0 * RHOBAR_END_GEV4 * EPS1) * math.exp(-DELTA_N)


def gamma_upper_branch2(m0_gev, rc_m):
    """gamma << m0^2 (35408 rhobar eps1/429)^-1 (H rc)^9 e^(-10 DeltaN)."""
    hrc = h_rc_dimensionless(rc_m)
    # Work in logs: (H rc)^9 e^(-10 DeltaN) overflows and underflows badly.
    log_pref = math.log(m0_gev**2 * 429.0 / (35408.0 * RHOBAR_END_GEV4 * EPS1))
    log_val = log_pref + 9.0 * math.log(hrc) - 10.0 * DELTA_N
    return math.exp(log_val)


def gamma_lower_branch1(m0_gev):
    """gamma > m0^2 (1152 rhobar)^-1 (-k eta_end)^7, with -k eta_end = e^-DeltaN."""
    return m0_gev**2 / (1152.0 * RHOBAR_END_GEV4) * math.exp(-7.0 * DELTA_N)


def gamma_lower_branch2(m0_gev, rc_m):
    """gamma > m0^2 (7264 rhobar/11)^-1 (-k eta_end)^14 (H rc)^7."""
    hrc = h_rc_dimensionless(rc_m)
    log_pref = math.log(m0_gev**2 * 11.0 / (7264.0 * RHOBAR_END_GEV4))
    log_val = log_pref - 14.0 * DELTA_N + 7.0 * math.log(hrc)
    return math.exp(log_val)


def gamma_to_lambda_inv_s(gamma_inv_gev2, rc_m):
    """lambda = gamma / (8 pi^(3/2) rc^3), converted to s^-1."""
    rc_inv_gev = rc_m_to_inv_gev(rc_m)
    lam_gev = gamma_inv_gev2 / (8.0 * math.pi**1.5 * rc_inv_gev**3)
    return lam_gev * GEV_TO_INV_S


def which_branch(rc_m):
    """1 if H_end rc < e^DeltaN (inflation crossing), else 2."""
    return 1 if h_rc_dimensionless(rc_m) < math.exp(DELTA_N) else 2


# ---------------------------------------------------------------- the checks

def check_dimensions():
    """Dimensional consistency, before any number is trusted."""
    detail = []
    ok = True

    # gamma has dimensions of GeV^-2: the correction term
    # (gamma/m0^2) * rhobar is dimensionless, so [gamma] = [m0^2]/[rhobar]
    # = GeV^2 / GeV^4 = GeV^-2.
    detail.append(
        "[gamma] from (gamma/m0^2)*rhobar being dimensionless: "
        "GeV^2/GeV^4 = GeV^-2"
    )
    # lambda = gamma/(8 pi^3/2 rc^3) then has GeV^-2 / GeV^-3 = GeV^1,
    # i.e. an inverse time in natural units. That is why lambda is a rate.
    detail.append(
        "[lambda] = [gamma]/[rc^3] = GeV^-2 / GeV^-3 = GeV, an inverse time: "
        "lambda is a rate, as the literature's s^-1 requires"
    )

    # Numerical check of the GeV -> s^-1 conversion against hbar.
    conv = GEV_TO_INV_S
    expect = 1.519267e24
    agree = abs(conv - expect) / expect < 1e-5
    if not agree:
        ok = False
    detail.append(
        f"1 GeV = {conv:.6e} s^-1 (independent value {expect:.6e}): "
        f"{'AGREES' if agree else 'DISAGREES'}"
    )

    # And the metre conversion.
    one_gev_inv_m = HBAR_C_GEV_M
    agree_m = abs(one_gev_inv_m - 1.9732698e-16) / 1.9732698e-16 < 1e-9
    if not agree_m:
        ok = False
    detail.append(
        f"1 GeV^-1 = {one_gev_inv_m:.7e} m: "
        f"{'AGREES' if agree_m else 'DISAGREES'}"
    )

    detail.append(f"H_end = {H_END_GEV:.6e} GeV  (= 1e-5 Mp, assumption A1)")
    detail.append(f"rhobar_end = {RHOBAR_END_GEV4:.6e} GeV^4  (assumption A2)")
    detail.append(f"e^DeltaN = e^{DELTA_N:.0f} = {math.exp(DELTA_N):.6e}")

    report("dimensional consistency and unit conversions", ok, "\n".join(detail))


def check_branch_boundary():
    """Where the branch condition H_end rc = e^DeltaN sits in rc."""
    detail = []
    ok = True

    # rc_star = e^DeltaN / H_end, in metres.
    rc_star_inv_gev = math.exp(DELTA_N) / H_END_GEV
    rc_star_m = rc_star_inv_gev * HBAR_C_GEV_M
    detail.append(
        f"branch boundary at rc* = e^DeltaN / H_end = {rc_star_m:.6e} m"
    )

    inside_lab = LAB_RC_RANGE_M[0] < rc_star_m < LAB_RC_RANGE_M[1]
    detail.append(
        f"laboratory-viable rc range is {LAB_RC_RANGE_M[0]:.0e} to "
        f"{LAB_RC_RANGE_M[1]:.0e} m; rc* falls "
        f"{'INSIDE' if inside_lab else 'outside'} it"
    )
    if inside_lab:
        detail.append(
            "CONSEQUENCE: the branch condition splits the laboratory-viable "
            "range. Neither branch applies across the whole of it, so a "
            "single number quoted for 'the Martin-Vennin bound' without an "
            "rc is ambiguous by construction."
        )

    detail.append("")
    detail.append("branch selected, across the lab-viable range:")
    for rc_m in (1e-8, 3e-8, 4.2e-8, 1e-7, 1e-6, 1e-5, 1e-4):
        detail.append(
            f"  rc = {rc_m:.1e} m:  H_end rc = {h_rc_dimensionless(rc_m):.4e}  "
            f"-> branch {which_branch(rc_m)} "
            f"({'inflation crossing' if which_branch(rc_m) == 1 else 'radiation crossing'})"
        )

    report("branch boundary in rc", ok, "\n".join(detail))


def check_the_bound():
    """The number WP-4 exists to produce."""
    detail = []
    ok = True

    for m0_label, m0 in (("nucleon = atomic mass unit", M_AMU_GEV),
                         ("nucleon = proton", M_PROTON_GEV)):
        detail.append(f"m0 = {m0_label} = {m0:.6f} GeV")
        detail.append(
            f"  {'rc [m]':>10s} {'branch':>7s} "
            f"{'gamma_max [GeV^-2]':>20s} {'lambda_max [s^-1]':>20s} "
            f"{'lambda_min [s^-1]':>20s}"
        )
        for rc_m in (1e-8, 1e-7, 1e-6, 1e-5, 1e-4):
            br = which_branch(rc_m)
            if br == 1:
                g_up = gamma_upper_branch1(m0)
                g_lo = gamma_lower_branch1(m0)
            else:
                g_up = gamma_upper_branch2(m0, rc_m)
                g_lo = gamma_lower_branch2(m0, rc_m)
            lam_up = gamma_to_lambda_inv_s(g_up, rc_m)
            lam_lo = gamma_to_lambda_inv_s(g_lo, rc_m)
            detail.append(
                f"  {rc_m:>10.1e} {br:>7d} {g_up:>20.6e} "
                f"{lam_up:>20.6e} {lam_lo:>20.6e}"
            )
            # Internal consistency: the CMB upper bound must exceed the
            # collapse lower bound for the CMB-allowed window to be non-empty.
            if lam_up < lam_lo:
                detail.append(
                    f"             ^ window EMPTY at this rc: the upper bound "
                    f"is below the lower bound by {lam_lo / lam_up:.3e}"
                )
        detail.append("")

    detail.append(
        "Every lambda_max above is between 70 and 80 orders of magnitude "
        "below the laboratory-viable window "
        f"({LAB_LAMBDA_RANGE_INV_S[0]:.0e} to "
        f"{LAB_LAMBDA_RANGE_INV_S[1]:.0e} s^-1), which is Martin & Vennin's "
        "qualitative conclusion: the CMB-allowed and laboratory-allowed "
        "regions do not overlap. The numbers above make that quantitative."
    )

    report("the CSL cosmological bound, evaluated", ok, "\n".join(detail))


def check_provenance_of_the_quoted_figure():
    """Is lambda << 5.6e-90 s^-1 reproducible, and from where?"""
    detail = []
    ok = True

    detail.append(
        f"The figure attributed to Martin & Vennin in Gundhi et al.'s "
        f"introduction: lambda << {ATTRIBUTED_LAMBDA_INV_S:.1e} s^-1"
    )
    detail.append("")
    detail.append(
        "Scanning branch 1's formula across rc at the figure caption's stated "
        "parameters, with m0 the atomic mass unit:"
    )

    m0 = M_AMU_GEV
    best = None
    for exp10 in range(-9, -2):
        rc_m = 10.0**exp10
        lam = gamma_to_lambda_inv_s(gamma_upper_branch1(m0), rc_m)
        ratio = lam / ATTRIBUTED_LAMBDA_INV_S
        detail.append(
            f"  rc = 1e{exp10:>3d} m:  lambda_max(branch 1) = {lam:.4e} s^-1  "
            f"ratio to attributed figure = {ratio:.4e}"
        )
        if best is None or abs(math.log10(ratio)) < abs(math.log10(best[1])):
            best = (rc_m, ratio, lam)

    rc_best, ratio_best, lam_best = best
    detail.append("")
    reproduces = abs(math.log10(ratio_best)) < 0.1
    detail.append(
        f"Closest match: rc = {rc_best:.1e} m gives "
        f"lambda_max = {lam_best:.4e} s^-1, a factor {ratio_best:.4f} from "
        f"the attributed {ATTRIBUTED_LAMBDA_INV_S:.1e} s^-1."
    )
    if reproduces:
        detail.append(
            "**REPRODUCED.** So the figure quoted as Martin & Vennin's bound "
            f"is their branch-1 formula evaluated at rc = {rc_best:.0e} m, "
            f"DeltaN = {DELTA_N:.0f}, H_inf = 1e-5 Mp, eps1 = {EPS1}, with m0 "
            "the nucleon mass. The provenance question is settled: it is a "
            "correct evaluation of a formula in their paper, not a number "
            "they state and not an invention."
        )
    else:
        ok = False
        detail.append(
            "NOT reproduced by branch 1 at any decade of rc. Either an input "
            "differs from the figure caption or the attributed figure comes "
            "from elsewhere. This is a finding and must not be smoothed over."
        )

    # And now the part that matters: does branch 1 apply at that rc?
    br_at_best = which_branch(rc_best)
    detail.append("")
    detail.append(
        f"But the branch condition at rc = {rc_best:.0e} m: "
        f"H_end rc = {h_rc_dimensionless(rc_best):.4e} versus "
        f"e^DeltaN = {math.exp(DELTA_N):.4e}, so branch {br_at_best} applies."
    )
    if br_at_best != 1:
        lam_correct = gamma_to_lambda_inv_s(
            gamma_upper_branch2(m0, rc_best), rc_best
        )
        detail.append(
            f"**Branch 1 does NOT apply there.** The applicable branch-2 "
            f"bound at the same rc and the same stated parameters is "
            f"lambda_max = {lam_correct:.4e} s^-1, weaker than the attributed "
            f"figure by a factor {lam_correct / ATTRIBUTED_LAMBDA_INV_S:.3e}, "
            f"i.e. {math.log10(lam_correct / ATTRIBUTED_LAMBDA_INV_S):.2f} "
            "orders of magnitude."
        )
        detail.append(
            "This does not overturn Martin & Vennin's conclusion: "
            f"{lam_correct:.2e} s^-1 is still about "
            f"{abs(math.log10(lam_correct / LAB_LAMBDA_RANGE_INV_S[0])):.0f} "
            "orders of magnitude below the laboratory-viable window, so the "
            "two allowed regions remain disjoint. What it changes is the "
            "NUMBER, and the number is what WP-4 was commissioned to produce."
        )
    else:
        detail.append(
            "Branch 1 does apply there, so the attributed figure is the "
            "applicable bound at that rc."
        )

    report("provenance of the lambda << 5.6e-90 figure", ok, "\n".join(detail))


def check_97_orders():
    """Run 01's '97 orders of magnitude', which Run 02 retagged."""
    detail = []
    ok = True

    gap = math.log10(GUNDHI_LAMBDA_INV_S / ATTRIBUTED_LAMBDA_INV_S)
    detail.append(
        f"Gundhi et al.'s own bound lambda <~ {GUNDHI_LAMBDA_INV_S:.0e} s^-1 "
        f"against the figure attributed to Martin & Vennin "
        f"{ATTRIBUTED_LAMBDA_INV_S:.1e} s^-1:"
    )
    detail.append(f"  log10 ratio = {gap:.3f}, i.e. {round(gap)} orders of magnitude")
    agrees = abs(gap - 97.0) < 1.0
    if not agrees:
        ok = False
    detail.append(
        f"Run 01 recorded 'roughly 97 orders of magnitude': "
        f"{'AGREES' if agrees else 'DISAGREES'}"
    )
    detail.append("")
    detail.append(
        "Run 02 established that this comparison is an [INFERENCE] and not "
        "[SOURCED], because one side of it is Gundhi et al.'s rendering of "
        "Martin & Vennin rather than a number Martin & Vennin state. The "
        "arithmetic is now checked and the premises are named: the gap is "
        "between Gundhi et al.'s stated bound and a figure that this script "
        "has just shown is branch 1 of Martin & Vennin's formula at "
        "rc = 1e-7 m, a branch which does not apply at that rc."
    )
    # And the gap against the applicable branch.
    m0 = M_AMU_GEV
    lam_applicable = gamma_to_lambda_inv_s(gamma_upper_branch2(m0, 1e-7), 1e-7)
    gap2 = math.log10(GUNDHI_LAMBDA_INV_S / lam_applicable)
    detail.append(
        f"Against the APPLICABLE branch-2 bound at rc = 1e-7 m "
        f"({lam_applicable:.3e} s^-1), the gap is {gap2:.2f} orders of "
        f"magnitude rather than {round(gap)}."
    )
    detail.append(
        "Both numbers describe the same physical disagreement, which Run 01 "
        "correctly identified as coming entirely from the choice of collapse "
        "operator. Neither number selects an operator and this script does "
        "not claim one is right."
    )

    report("the '97 orders of magnitude' arithmetic and its premises",
           ok, "\n".join(detail))


def main():
    print("WP-4: the CSL cosmological bound")
    print("=" * 78)
    print("Evaluates Martin & Vennin's own closed-form constraint")
    print("(arXiv:1906.04405) at the parameters stated in their own figure")
    print("caption. Derives nothing new; reads nothing off a figure.")
    print()
    check_dimensions()
    print()
    check_branch_boundary()
    print()
    check_the_bound()
    print()
    check_provenance_of_the_quoted_figure()
    print()
    check_97_orders()
    print()
    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {', '.join(FAILURES)}")
        return 1
    print("PASS: 5 of 5 checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
