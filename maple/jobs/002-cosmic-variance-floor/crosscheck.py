#!/usr/bin/env python3
"""Cross-check of Maple job 002 blocks [1]-[4] in sympy, plus the triangle
count in [7] by brute force.

    python crosscheck.py

Blocks [1]-[4] are textbook and are the Maple job's pipeline check; this
script fixes their expected values. Blocks [5]-[6] are not cross-checked
here (they depend on the window convention the plan chooses). Block [7] is
counted brute force at small lmax so Maple's closed form has something to
agree with.

Verified with sympy 1.14.0 / numpy 2.5.4 on Python 3.14.7.
"""

import sympy as sp

l, fsky, Cl, n_sigma = sp.symbols("l fsky Cl n_sigma", positive=True)
nu = sp.symbols("nu", positive=True)


def chi2_moments():
    """Mean and variance of chi^2(nu), derived from the pdf, not quoted."""
    t = sp.symbols("t", positive=True)
    pdf = t ** (nu / 2 - 1) * sp.exp(-t / 2) / (2 ** (nu / 2) * sp.gamma(nu / 2))
    mean = sp.simplify(sp.integrate(t * pdf, (t, 0, sp.oo)))
    second = sp.simplify(sp.integrate(t ** 2 * pdf, (t, 0, sp.oo)))
    return mean, sp.simplify(second - mean ** 2)


def main():
    mean, var = chi2_moments()
    print("[1] CHI2_MEAN   =", mean, "   expected nu")
    print("[2] CHI2_VAR    =", var, "   expected 2*nu")
    assert sp.simplify(mean - nu) == 0
    assert sp.simplify(var - 2 * nu) == 0

    # Chat_l = (Cl/nu_l) * X  with nu_l = (2l+1) fsky
    nu_l = (2 * l + 1) * fsky
    var_cl = sp.simplify((Cl / nu_l) ** 2 * var.subs(nu, nu_l))
    frac = sp.simplify(sp.sqrt(var_cl) / Cl)
    print("[3] VAR_CL      =", var_cl)
    print("[4] FRAC_ERR_CL =", frac)

    target = sp.sqrt(2 / ((2 * l + 1) * fsky))
    assert sp.simplify(frac - target) == 0, "cosmic variance formula mismatch"
    print("    matches sqrt(2/((2l+1) fsky)):", True)

    # Block [7]: closed, parity-even triangles with each l_i <= lmax.
    print()
    print("[7] NTRIANGLES brute force (parity-even, triangle inequality):")
    for lmax in range(0, 9):
        n = 0
        for a in range(lmax + 1):
            for b in range(lmax + 1):
                for c in range(lmax + 1):
                    if (a + b >= c and b + c >= a and c + a >= b
                            and (a + b + c) % 2 == 0):
                        n += 1
        print("      lmax=%d: %d" % (lmax, n))
    print()
    print("    These are what Maple's closed form in block [7] must match.")
    print("    The leading scaling is cubic in lmax; the plan only needs")
    print("    that scaling, so a closed form that will not simplify is")
    print("    acceptable provided it agrees with this table.")


if __name__ == "__main__":
    main()
