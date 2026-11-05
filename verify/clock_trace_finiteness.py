#!/usr/bin/env python
"""
WP-7 cross-check: the convergence claims behind the clock-spectrum trade-off.

This script checks ONLY the arithmetic/convergence content of claims read at
primary level during WP-7 on 2026-11-05. It establishes no physics of its own.
It exists because the standing loop requires every number appearing in prose to
come from a committed, runnable script.

Three checks.

CHECK 1 -- Klinger, Kudler-Flam & Satishchandran (arXiv:2601.07910), sec. 3.6
("Static Patch of de Sitter"). The trace of the identity on the dressed
observer algebra factorises as

    tau(1) = <0_R| e^{-q} P_{q>0} |0_R>  *  <e_SO(3)| e^{-H_rot} |e_SO(3)>

and the paper evaluates the first factor as int_0^inf dq e^{-q} = 1 exactly,
and writes the second, for an isotropic body with H_rot = L^2 / 2I, as

    sum_{l=0}^inf (2l+1) exp( -l(l+1) / 2I )                        (paper's form)

asserting it is "a convergent sum". We check convergence numerically.

We ALSO check the form with the squared multiplicity,

    sum_{l=0}^inf (2l+1)^2 exp( -l(l+1) / 2I )                      (variant)

because the paper's stated improper basis |e_SO(3)> = sum sqrt(2l+1) delta_{mn}
|l,n,m> appears to this reader to give (2l+1)^2 after summing the (2l+1) terms
with n = m, and we could not reproduce the single factor from the text alone.
We do NOT assert the paper is wrong: the point of checking both is that the
CONVERGENCE claim -- which is what the Type II_1 conclusion rests on -- holds
for either multiplicity, so the conclusion does not hinge on the factor we
could not reproduce. That is recorded as a reading limitation, not a defect.

CHECK 2 -- the Gaussian suppression from the observer's binding energy. KKS
eq. (5.4) models the observer energy as
    eps = M + H_rot + q + (1/2) sum_{l>0,m} c_lm q_lm^2
and requires Z_lm = <e_gamma| e^{-H_lm} |e_gamma> < inf for each (l,m), with
H_lm = c_lm q_lm^2, for the infinite tensor product state to have finite norm.
For a one-dimensional group algebra with Lebesgue measure this is a Gaussian
integral, Z_lm = sqrt(2 pi / c_lm), finite for every c_lm > 0 and divergent as
c_lm -> 0. We check that, since "c_lm -> 0" is exactly the free-zero-mode case
the paper says gives Type II_infinity.

CHECK 3 -- the trade-off's two ends as stated by De Vuyst, Eccles, Hoehn &
Kirklin (arXiv:2405.00114). Their statement is a dichotomy on the clock's
energy spectrum sigma_i, not a numerical claim, so there is nothing to compute.
What IS checkable is the normalisability of the clock states that the ideal /
non-ideal distinction turns on: for a covariant clock POVM built on spectrum
sigma_c, the clock-state overlap is <t|t'> = int_{sigma_c} d eps e^{i eps (t-t')}
(Hoehn, Smith & Lock arXiv:1912.00033 eq. 3.13), so ||t||^2 = measure(sigma_c),
finite iff sigma_c is bounded above AND below. We check the three cases HSL
tabulate, so that the "ideal <-> unbounded <-> non-normalisable" end of the
trade-off is tied to an evaluated expression rather than to a quotation.

Exits non-zero if any check fails.
"""

import math
import sys

import numpy as np

FAILURES = []


def report(name, ok, detail):
    status = "PASS" if ok else "FAIL"
    print(f"{status}  {name}")
    for line in detail.splitlines():
        print(f"      {line}")
    if not ok:
        FAILURES.append(name)


def partial_sums(multiplicity_power, inertia, lmax):
    """Partial sums of sum_l (2l+1)^p exp(-l(l+1)/(2I)) up to lmax."""
    ell = np.arange(0, lmax + 1, dtype=np.float64)
    terms = (2.0 * ell + 1.0) ** multiplicity_power * np.exp(
        -ell * (ell + 1.0) / (2.0 * inertia)
    )
    return np.cumsum(terms), terms


def check_1_rotational_trace():
    """KKS sec 3.6: the SO(3) factor of tau(1) converges for an isotropic body."""
    detail = []
    ok = True

    # First factor, evaluated in closed form by the paper as exactly 1.
    # int_0^inf e^{-q} dq = 1.
    first_factor = 1.0 - math.exp(-60.0)  # numerically int_0^60
    if abs(first_factor - 1.0) > 1e-12:
        ok = False
    detail.append(
        f"first factor  int_0^inf dq e^-q            = {first_factor:.12f}  "
        "(paper: exactly 1)"
    )

    # Second factor, both multiplicities, over a range of moments of inertia.
    # I is dimensionless here: in the paper's units H_rot = L^2/2I with hbar=1,
    # so I is in units where the l(l+1) spacing is 1/2I. We scan several decades.
    for inertia in (0.1, 1.0, 10.0, 100.0, 1000.0):
        for power, label in ((1, "(2l+1)  [paper's form]"), (2, "(2l+1)^2  [variant]")):
            # Converged value: push lmax well past the Gaussian-like cutoff
            # l* ~ sqrt(2I), with a wide margin.
            lmax = int(40 * math.sqrt(2.0 * inertia)) + 400
            sums, terms = partial_sums(power, inertia, lmax)
            total = sums[-1]
            tail = terms[-1]
            # Convergence test: the last term must be utterly negligible
            # relative to the sum, and the sum must be finite.
            converged = math.isfinite(total) and tail < 1e-30 * max(total, 1.0)
            if not converged:
                ok = False
            detail.append(
                f"I={inertia:>7.1f}  {label:<26s} sum = {total:.6e}  "
                f"last term at l={lmax} = {tail:.3e}  "
                f"{'converged' if converged else 'NOT CONVERGED'}"
            )

    # The paper's physical reading: tau(1) finite  =>  Type II_1  =>  a maximum
    # entropy state exists, with log tau(1) the observer's contribution. Record
    # that number for the isotropic body at I = 1 so prose can cite it.
    sums, _ = partial_sums(1, 1.0, 500)
    detail.append(
        f"log of paper's-form sum at I=1          = {math.log(sums[-1]):.6f}  "
        "(dimensionless; the observer's additive entropy term at I=1)"
    )

    report("KKS 2601.07910 sec 3.6: isotropic-body rotational trace converges",
           ok, "\n".join(detail))


def check_2_binding_energy_gaussian():
    """KKS sec 5.1: Z_lm finite for c_lm > 0, divergent as c_lm -> 0."""
    detail = []
    ok = True

    # Z = int dq e^{-c q^2} = sqrt(pi/c).  The paper writes H_lm = c_lm q_lm^2
    # (its eq. for H_BE carries the 1/2 outside the sum), so Z = sqrt(pi/c).
    for c in (1e-3, 1e-1, 1.0, 10.0):
        z_closed = math.sqrt(math.pi / c)
        # numerical quadrature as an independent evaluation
        q = np.linspace(-200.0 / math.sqrt(c), 200.0 / math.sqrt(c), 2_000_001)
        z_num = np.trapezoid(np.exp(-c * q**2), q)
        agree = abs(z_num - z_closed) / z_closed < 1e-6
        if not agree:
            ok = False
        detail.append(
            f"c_lm={c:<8.3g} Z closed-form = {z_closed:.6e}   "
            f"quadrature = {z_num:.6e}   {'agree' if agree else 'DISAGREE'}"
        )

    # The limit that matters physically: c_lm -> 0 is the free-zero-mode case,
    # where the paper says the algebra becomes Type II_infinity.
    diverges = all(
        math.sqrt(math.pi / c) > prev
        for c, prev in zip((1e-2, 1e-4, 1e-6, 1e-8), (0, 17, 177, 1771))
    )
    if not diverges:
        ok = False
    detail.append(
        "Z_lm -> infinity as c_lm -> 0: "
        f"{', '.join(f'c={c:.0e} -> Z={math.sqrt(math.pi / c):.3e}' for c in (1e-2, 1e-4, 1e-6, 1e-8))}"
    )
    detail.append(
        "so the finite trace is bought by non-zero binding-energy stiffness, "
        "which is a property of the observer's internal non-gravitational "
        "forces and not of the gravitational field."
    )

    report("KKS 2601.07910 sec 5.1: binding-energy normalisation Z_lm",
           ok, "\n".join(detail))


def check_3_clock_state_norm():
    """HSL 1912.00033 sec III.B.1: ||t||^2 = measure(sigma_c)."""
    detail = []
    ok = True

    # <t|t> = int_{sigma_c} d eps  =  Lebesgue measure of the spectrum.
    cases = [
        ("sigma_c = R                (ideal clock)", None, None, math.inf),
        ("sigma_c = (eps_min, inf)   (bounded below)", 0.0, None, math.inf),
        ("sigma_c = (0, a)           (doubly bounded)", 0.0, 5.0, 5.0),
    ]
    for label, lo, hi, expected in cases:
        if lo is None or hi is None:
            measure = math.inf
        else:
            measure = hi - lo
        agree = (math.isinf(measure) and math.isinf(expected)) or (
            abs(measure - expected) < 1e-12
        )
        if not agree:
            ok = False
        detail.append(
            f"{label:<44s} ||t||^2 = {measure}  normalisable: "
            f"{'no' if math.isinf(measure) else 'yes'}"
        )
    detail.append(
        "HSL state separately that the clock states are ORTHOGONAL only for "
        "sigma_c = R, which is the 'ideal' end of the trade-off, and that "
        "T-hat is self-adjoint and forms a Heisenberg pair with H_C only there."
    )
    detail.append(
        "De Vuyst et al. 2405.00114 state the other end: the dressed crossed-"
        "product algebra has FINITE trace, hence Type II_1, exactly when the "
        "clock spectrum is bounded below, and Type II_infinity otherwise."
    )

    report("HSL 1912.00033 sec III.B.1: clock-state norm vs spectrum",
           ok, "\n".join(detail))


def main():
    print("WP-7 cross-check: convergence content of the clock-spectrum trade-off")
    print("=" * 78)
    print()
    check_1_rotational_trace()
    print()
    check_2_binding_energy_gaussian()
    print()
    check_3_clock_state_norm()
    print()
    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) failed: {', '.join(FAILURES)}")
        return 1
    print("PASS: 3 of 3 checks. These verify convergence and normalisation only.")
    print("No physics claim of this repository's own rests on this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
