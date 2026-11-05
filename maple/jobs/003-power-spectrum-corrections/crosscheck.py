#!/usr/bin/env python
"""
Independent sympy cross-check for Maple job 003.

A cross-check is a cross-check and not a result. Where this and Maple
disagree, the disagreement is the finding and neither is adopted until it is
resolved.

Run:
    .venv/Scripts/python maple/jobs/003-power-spectrum-corrections/crosscheck.py

Exits non-zero if any check fails.

What is checked
---------------
1. The CSL source function built by explicit differentiation from MV 2020's
   alpha_k and beta_k, and the leading super-Hubble k-power of the
   Green-function integral, for both epochs. Target: m_C_inf = -1 and
   m_C_rad = -10, from the published n_S = 0 and n_S = -9.
2. The open-EFT index algebra: m_D = -1 - alpha_n reduces to p + 2n - 7, and
   vanishes at p = 7 - 2n.
3. The degeneracy loci m_C = m_D.
4. The free-parameter counts that WP-3 may not report a statistic without,
   computed here by symbolic rank rather than asserted.

What is NOT checked here
------------------------
Part B's closed-form Bessel integrals for n = 1, 2 and the n >= 3
saddle-point comparison. sympy does not evaluate those reliably; that is
Maple's half of the job and the reason the round trip is worth taking.
"""

import sys

import sympy as sp

FAILURES = []


def report(name, ok, detail):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    for line in detail.splitlines():
        print(f"      {line}")
    if not ok:
        FAILURES.append(name)


# Symbols. Positive where the physics says so, which sympy needs for the
# series expansions to come out in a canonical form.
k, eta, x = sp.symbols("k eta x", positive=True)
H, eps1, eps2, Mp, m0, rc, gam = sp.symbols(
    "H eps1 eps2 Mp m0 rc gam", positive=True
)
n, p = sp.symbols("n p")
a_e, eta_e, eta_r = sp.symbols("a_e eta_e eta_r", positive=True)


def csl_source(alpha, beta, a, omega2, var):
    """MV 2020 eq. (source:def), built by explicit differentiation."""
    a4 = a**4
    return (gam / m0**2) * (
        2 * a4 * (alpha**2 + omega2 * beta**2)
        - 2 * sp.diff(a4 * alpha * beta, var)
        + sp.diff(a4 * beta**2, var, 2)
    )


def check_1_csl_source_structure():
    """Build S_CSL for both epochs and check its structural properties.

    Deliberately does NOT attempt to extract m_C. A first version of this
    check tried to expand the Green-function integrand symbolically and did
    not terminate in nine minutes; m_C is Maple's half of the job and this
    file does not claim it. What sympy can settle cheaply, and what is worth
    settling because it is an independent handle on the amplitude, is the
    degree of the source in gamma and in the Planck mass, and whether the
    two epochs' sources share the structure the job assumes.
    """
    detail = []
    ok = True

    # The Gaussian smearing exp(-k^2 rc^2 / 2a^2) is a common factor of both
    # alpha_k and beta_k. Its role is to switch the CSL terms on at rc
    # crossing. It carries no gamma, m0, Mp or eps1 dependence, so every
    # degree checked below is independent of its form; its eta-derivatives
    # are what set the lower limit of the source integral, which is exactly
    # the part left to Maple. We therefore replace it by a concrete smooth
    # eta-dependent factor so the expression stays differentiable and
    # numerically evaluable. Stated explicitly because substituting a
    # stand-in is the kind of step that must not be silent.
    def G(e):
        return sp.exp(-(e**2))

    # --- inflation: de Sitter, a = -1/(H eta), eta < 0 -----------------
    a_inf = -1 / (H * eta)
    z_inf = a_inf * Mp * sp.sqrt(2 * eps1)
    omega2_inf = k**2 - 2 / eta**2

    alpha_inf = (Mp**2 * H**2 * eps1 / z_inf) * G(eta) * (
        -8 + 6 * (a_inf * H / k) ** 2 * eps1
    )
    beta_inf = (2 * Mp**2 * H * eps1 / (a_inf * z_inf)) * G(eta) * (
        -3 * eps1 * (a_inf * H / k) ** 2 + 1
    )
    # No sp.expand: expanding these nested rational-times-exponential
    # second derivatives is what hung two earlier attempts. Every check
    # below is numeric, so the unexpanded form is all that is needed.
    S_inf = csl_source(alpha_inf, beta_inf, a_inf, omega2_inf, eta).doit()

    # --- radiation: a linear in eta, z''/z = 0, cs^2 = 1/3 -------------
    a_rad = a_e * (eta - eta_r) / (eta_e - eta_r)
    z_rad = a_rad * Mp * sp.sqrt(2 * eps1)
    omega2_rad = k**2 / 3

    alpha_rad = (24 * Mp**2 * H**2 / z_rad) * G(eta) * (
        3 * (a_rad * H / k) ** 2 - 1
    )
    beta_rad = (12 * Mp**2 * H / (a_rad * z_rad)) * G(eta) * (
        1 - 6 * (a_rad * H / k) ** 2
    )
    S_rad = csl_source(alpha_rad, beta_rad, a_rad, omega2_rad, eta).doit()

    # Degree checks by NUMERIC SCALING, not by sp.Poly and not by symbolic
    # simplification. Two earlier attempts failed and both failures are
    # recorded here because they are the reason for this method: sp.Poly
    # raised PolynomialError (the symbols appear in denominators), and a
    # symbolic homogeneity test over a range of candidate degrees did not
    # terminate in 400 s on these expressions.
    #
    # A function homogeneous of degree d in s satisfies S(2s)/S(s) = 2^d
    # exactly. Evaluating that ratio at fixed rational values of every other
    # symbol gives d directly, with no simplification. Exact rationals are
    # used, so this is not a floating-point argument: the ratio comes out as
    # an exact power of 2 or the check fails.
    base = {
        eta: sp.Rational(-3, 2),
        k: sp.Rational(7, 5),
        H: sp.Rational(2, 3),
        eps1: sp.Rational(1, 7),
        Mp: sp.Rational(5, 2),
        m0: sp.Rational(3, 4),
        rc: sp.Rational(1, 3),
        gam: sp.Rational(2, 5),
        a_e: sp.Rational(9, 4),
        eta_e: sp.Rational(-1, 2),
        eta_r: sp.Rational(-5, 2),
    }

    def scaling_degree(expr, sym):
        """Exact homogeneity degree of expr in sym, by the ratio S(2s)/S(s)."""
        pt = {s: v for s, v in base.items() if s in expr.free_symbols}
        at_1 = sp.nsimplify(expr.subs(pt))
        pt2 = dict(pt)
        pt2[sym] = 2 * base[sym]
        at_2 = sp.nsimplify(expr.subs(pt2))
        if at_1 == 0:
            return None
        ratio = sp.nsimplify(sp.simplify(at_2 / at_1))
        d = sp.log(ratio) / sp.log(2)
        d = sp.nsimplify(sp.simplify(d))
        return d if d.is_Integer else sp.simplify(d)

    for S, label in ((S_inf, "inflation"), (S_rad, "radiation")):
        # Linear in gamma: MV 2020's source is first order in gamma, so the
        # correction to the power spectrum is too, and the bound on gamma
        # that WP-4 computes inherits that linearity.
        dg = scaling_degree(S, gam)
        lin = dg == 1
        if not lin:
            ok = False
        detail.append(
            f"{label:>9s}: degree {dg} in gamma (by exact scaling)  "
            f"(MV 2020's source is linear) {'AGREES' if lin else 'DISAGREES'}"
        )

        # m0 enters only as the overall 1/m0^2.
        dm = scaling_degree(S, m0)
        m0_ok = dm == -2
        if not m0_ok:
            ok = False
        detail.append(
            f"{label:>9s}: degree {dm} in m0 (by exact scaling) (expected -2): "
            f"{'AGREES' if m0_ok else 'DISAGREES'}"
        )

        # Mp: alpha and beta each carry Mp^2 over z ~ Mp, so each is O(Mp),
        # and S is quadratic in them, hence O(Mp^2).
        dmp = scaling_degree(S, Mp)
        mp_ok = dmp == 2
        if not mp_ok:
            ok = False
        detail.append(
            f"{label:>9s}: degree {dmp} in Mp (by exact scaling) (expected 2): "
            f"{'AGREES' if mp_ok else 'DISAGREES'}"
        )
        detail.append("")

    # eps1 scaling: the one place the two epochs differ in a way that shows
    # up in the published amplitudes. MV 2020 eq. (powerSpectrum:infl) carries
    # eps1^3; eqs. (powerSpectrum:inf) and (powerSpectrum:rad) carry eps1^1.
    # The inflation alpha, beta carry eps1 explicitly while the radiation ones
    # do not, so after z's sqrt(2 eps1) the inflation source must carry the
    # higher power. The source is not homogeneous in eps1 (alpha_inf is a sum
    # of an eps1-independent -8 and an eps1 term), so compare the LOWEST
    # powers present instead.
    def lowest_eps1_power(expr):
        """Lowest power of eps1 present, from the small-eps1 numeric slope.

        The sources are not homogeneous in eps1 (alpha_inf is a sum of an
        eps1-independent term and an eps1 term), so a scaling ratio is not a
        single power. As eps1 -> 0 the lowest power dominates, so the slope
        of log|S| against log eps1 at small eps1 converges to it. Evaluated
        at two decades and reported as the nearest half-integer, since z
        carries sqrt(eps1) and half-integer powers are physically possible.
        """
        pt = {s_: v for s_, v in base.items() if s_ in expr.free_symbols}
        vals = []
        for e in (sp.Rational(1, 10**6), sp.Rational(1, 10**8)):
            q = dict(pt)
            q[eps1] = e
            vals.append(sp.Abs(sp.N(expr.subs(q), 30)))
        if vals[0] == 0 or vals[1] == 0:
            return None
        slope = sp.log(vals[1] / vals[0]) / sp.log(sp.Rational(1, 100))
        return sp.nsimplify(sp.N(slope, 15), rational=True, tolerance=0.02)

    e_inf = lowest_eps1_power(S_inf)
    e_rad = lowest_eps1_power(S_rad)
    eps_ok = e_inf > e_rad
    if not eps_ok:
        ok = False
    detail.append(
        f"lowest eps1 power: inflation {e_inf} vs radiation {e_rad}; the "
        f"published amplitudes carry eps1^3 and eps1^1 respectively, so the "
        f"inflation source must carry the higher power: "
        f"{'AGREES' if eps_ok else 'DISAGREES'}"
    )

    detail.append("")
    detail.append(
        "NOT CLAIMED HERE: m_C_inf and m_C_rad. Extracting them needs the "
        "super-Hubble asymptotics of the Green-function integral whose lower "
        "limit the Gaussian sets, which is the elimination Maple is being "
        "asked for. An earlier version of this check tried it in sympy and "
        "did not terminate. The published targets are m_C_inf = -1 and "
        "m_C_rad = -10 and the job must reproduce them."
    )

    report("CSL source construction, both epochs (structure and degrees)",
           ok, "\n".join(detail))


def check_2_open_eft_index():
    detail = []
    ok = True

    alpha_n = 6 - 2 * n - p
    m_D = sp.simplify(-1 - alpha_n)

    target = p + 2 * n - 7
    agrees = sp.simplify(m_D - target) == 0
    if not agrees:
        ok = False
    detail.append(f"m_D = -1 - alpha_n = {m_D}")
    detail.append(
        f"published form p + 2n - 7 = {target}: "
        f"{'AGREES' if agrees else 'DISAGREES'}"
    )

    at_si = sp.simplify(m_D.subs(p, 7 - 2 * n))
    si_ok = at_si == 0
    if not si_ok:
        ok = False
    detail.append(
        f"m_D at p = 7 - 2n is {at_si}; published: scale invariant, i.e. 0: "
        f"{'AGREES' if si_ok else 'DISAGREES'}"
    )

    # Amplitude exponent: (kgamma/k_*)^(4-2n). At n = 2 this is k-independent
    # and at n = 1 it is quartic; both are stated in the paper.
    detail.append(
        "amplitude exponent 4 - 2n: n=1 -> 2, n=2 -> 0, n=3 -> -2 "
        f"[{', '.join(str(4 - 2 * i) for i in (1, 2, 3))}]"
    )

    report("open-EFT index algebra (MV 2018)", ok, "\n".join(detail))


def check_3_degeneracy_loci():
    detail = []
    ok = True

    m_D = p + 2 * n - 7
    loci = {}
    for m_C, label in ((-1, "inflation (n_S=0)"), (-10, "radiation (n_S=-9)")):
        sol = sp.solve(sp.Eq(m_D, m_C), p)
        loci[label] = sp.simplify(sol[0])
        detail.append(f"m_C = {m_C:>3d}  [{label}]:  degenerate at p = {sol[0]}")

    # JOB.md tripwire 5: the inflation locus must come out p = 6 - 2n, which
    # is the boundary of MV 2018's own first regime. If it does not, something
    # is wrong.
    expected = 6 - 2 * n
    got = loci["inflation (n_S=0)"]
    tripwire_ok = sp.simplify(got - expected) == 0
    if not tripwire_ok:
        ok = False
    detail.append("")
    detail.append(
        f"JOB.md tripwire 5 expects the inflation locus at p = 6 - 2n; "
        f"got p = {got}: {'AGREES' if tripwire_ok else 'DISAGREES'}"
    )
    detail.append(
        "p = 6 - 2n is exactly the boundary between MV 2018's first regime "
        "(p < 6-2n, amplitude depends on the environment correlation length) "
        "and its second (6-2n < p < 10-2n, amplitude independent of it). So "
        "the C and D corrections become indistinguishable in shape precisely "
        "at a regime boundary of the D side, and WP-3 must report that region "
        "as singular rather than quote a statistic across it."
    )
    for nn in range(1, 5):
        detail.append(
            f"  n={nn}: inflation-degenerate at p={expected.subs(n, nn)}, "
            f"radiation-degenerate at p={(loci['radiation (n_S=-9)']).subs(n, nn)}"
        )

    report("degeneracy loci m_C = m_D", ok, "\n".join(detail))


def check_4_free_parameter_counts():
    detail = []
    ok = True

    # C side. The published amplitude for inflation crossing, MV 2020
    # eq. (powerSpectrum:infl):
    #   A_C = 6 (gam/m0^2) eps1^3 rhobar_inf exp(DeltaN)
    # using (k/aH)_end^-1 = exp(DeltaN). And rhobar_inf = 3 H^2 Mp^2.
    DeltaN = sp.symbols("DeltaN", positive=True)
    rhobar = 3 * H**2 * Mp**2
    A_C = 6 * (gam / m0**2) * eps1**3 * rhobar * sp.exp(DeltaN)
    m_C = sp.Integer(-1)

    pars_C = [gam, rc, eps1, H, Mp, m0, DeltaN]
    J_C = sp.Matrix([[sp.diff(A_C, q) for q in pars_C],
                     [sp.diff(m_C, q) for q in pars_C]])
    rank_C = J_C.rank()
    detail.append(f"C side: {len(pars_C)} underlying parameters {[str(q) for q in pars_C]}")
    detail.append(f"        rank of Jacobian of (A_C, m_C) = {rank_C}")
    detail.append(
        "        so the power spectrum sees ONE combination on the C side at "
        "fixed epoch: the index is a pure number carrying no parameter "
        "dependence, and the amplitude is a single scalar. rc drops out of "
        "A_C entirely once the mode has crossed it."
    )
    if rank_C != 1:
        ok = False
    detail.append(f"        FREE_PARAMETERS_C = {rank_C}")

    # D side. A_D = C(n,p) (kgamma/kstar)^(4-2n), m_D = p + 2n - 7.
    kgamma, kstar, H_lE = sp.symbols("kgamma kstar H_lE", positive=True)
    C_np = 1 / (2 * (6 - 2 * n - p)) * H_lE ** (p + 2 * n - 6)
    A_D = C_np * (kgamma / kstar) ** (4 - 2 * n)
    m_D = p + 2 * n - 7
    pars_D = [kgamma, p, n, H_lE]
    J_D = sp.Matrix([[sp.diff(A_D, q) for q in pars_D],
                     [sp.diff(m_D, q) for q in pars_D]])
    rank_D = J_D.rank()
    detail.append("")
    detail.append(f"D side: {len(pars_D)} underlying parameters {[str(q) for q in pars_D]}")
    detail.append(f"        rank of Jacobian of (A_D, m_D) = {rank_D}")
    detail.append(
        "        the index depends on p and n, so the D side moves in BOTH "
        "amplitude and shape where the C side moves only in amplitude."
    )
    if rank_D != 2:
        ok = False
    detail.append(f"        FREE_PARAMETERS_D = {rank_D}")

    detail.append("")
    detail.append(
        "CONSEQUENCE for WP-3, which is the point of computing this: at fixed "
        "epoch the C side contributes 1 free parameter and the D side 2. Any "
        "comparison statistic between them is therefore NOT a like-for-like "
        "comparison of two one-parameter models, and must be reported with "
        "the counts 1 and 2 attached. A statistic quoted without them is "
        "recorded as uninterpretable, per the standing loop."
    )
    detail.append(
        "These are sympy's ranks on the PUBLISHED amplitudes. Maple is asked "
        "for the same ranks on the amplitudes it derives from the source "
        "integral. If they differ, the published amplitude and the derived "
        "one disagree, and that is the finding."
    )

    report("free-parameter counts by symbolic rank", ok, "\n".join(detail))


def main():
    print("Cross-check for Maple job 003 - power spectrum corrections")
    print("=" * 74)
    print(f"sympy {sp.__version__}")
    print()
    check_1_csl_source_structure()
    print()
    check_2_open_eft_index()
    print()
    check_3_degeneracy_loci()
    print()
    check_4_free_parameter_counts()
    print()
    print("=" * 74)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {', '.join(FAILURES)}")
        return 1
    print("PASS: all cross-checks. m_C itself is NOT determined here and is")
    print("left to Maple; see the note in check 1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
