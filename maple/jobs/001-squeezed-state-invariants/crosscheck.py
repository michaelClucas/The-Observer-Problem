#!/usr/bin/env python3
"""Cross-check of Maple job 001 in sympy, run before the job was queued.

    python crosscheck.py

Computes the same symplectic invariants as `job.mpl` in a second CAS, so
the Maple run has a stated target to confirm rather than an open question
to answer. The expected values this produces are recorded in `JOB.md`.

This is not a substitute for the Maple job. The repository's procedure puts
symbolic work in Maple; agreement between two independent CAS
implementations is worth more than either alone, and a disagreement between
them is a finding about the implementations that must be resolved before
either result is used.

Verified with sympy 1.14.0 on Python 3.14.7.
"""

import sympy as sp

# Conformal time, dimensionless: x = k*eta, negative during inflation,
# x -> 0- at late times (super-Hubble).
x = sp.symbols("x", real=True, negative=True)


def wronskian(v):
    """v v'* - v* v'. Equals i for a correctly normalised mode."""
    return sp.simplify(v * sp.conjugate(sp.diff(v, x))
                       - sp.conjugate(v) * sp.diff(v, x))


def cov_det(v):
    """det of the Gaussian covariance matrix built from mode function v.

    sigma = [[|v|^2, Re(v p*)], [Re(v p*), |p|^2]] with p = dv/dx.
    Equals 1/4 for a pure state (hbar = 1).
    """
    p = sp.diff(v, x)
    svv = sp.simplify(sp.Abs(v) ** 2)
    spp = sp.simplify(sp.Abs(p) ** 2)
    svp = sp.simplify(sp.re(sp.expand(v * sp.conjugate(p))))
    return sp.simplify(svv * spp - svp ** 2)


def main():
    # Exact de Sitter Mukhanov-Sasaki mode: growing and decaying together.
    v = (1 - sp.I / x) * sp.exp(-sp.I * x)

    w_raw = wronskian(v)
    n_const = sp.simplify(sp.sqrt(sp.I / w_raw))
    v0 = sp.simplify(n_const * v)

    print("[1] WRONSKIAN (unnormalised):", w_raw)
    print("    normalisation N          :", n_const)
    print("    WRONSKIAN (normalised)   :", sp.simplify(wronskian(v0)))

    det_exact = cov_det(v0)
    print("[2] DET_EXACT                :", det_exact,
          "   <-- must be exactly 1/4")
    assert det_exact == sp.Rational(1, 4), "pipeline check failed"

    print("[3] SYMPEIG_EXACT            :",
          [sp.sqrt(det_exact), sp.sqrt(det_exact)])

    quarter = sp.Rational(1, 4)
    print()
    for n in range(3):
        # Laurent series about x = 0: leading term plus n corrections.
        trunc = sp.simplify(sp.series(v0, x, 0, n + 2).removeO())
        det_t = cov_det(trunc)
        delta = sp.simplify(det_t - quarter)
        sign = ("zero" if delta == 0
                else "NEGATIVE (not a state)" if delta.subs(x, -1) < 0
                else "positive (mixed-like, but state asserted pure)")
        print("[4] n=%d  trunc v   : %s" % (n, trunc))
        print("         DET_TRUNC : %s" % det_t)
        print("[5]      DELTA_RS  : %s   -> %s" % (delta, sign))
        print()

    # Independent check: the flat-space limit must still be pure.
    print("[CHECK] DET at large |x|     :",
          sp.limit(cov_det(v0), x, -sp.oo), "  expected 1/4")


if __name__ == "__main__":
    main()
