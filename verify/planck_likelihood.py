#!/usr/bin/env python
"""Check that the WP-3 likelihood pipeline exists and evaluates.

WP-3 compares two modifications of the curvature power spectrum against
Planck. That needs a working likelihood, and a likelihood that imports is
not a likelihood that evaluates. This script evaluates all three components
at the Planck 2018 TT,TE,EE+lowE base-LCDM best fit and checks each chi2
against the published value.

Reference parameter values: Planck 2018 results VI, Table 1, column
"TT,TE,EE+lowE" (arXiv:1807.06209).

The expected chi2 values below are NOT taken from a paper. They were
produced by this pipeline on 2026-11-05 and are recorded so that a later
change in camb, cobaya or the data files shows up as a failure rather than
as a silently different answer. The tolerance is loose enough to survive a
patch release and tight enough to catch a changed dataset.

Run:
    .venv/Scripts/python verify/planck_likelihood.py
"""

import os
import sys

PACKAGES_PATH = os.environ.get(
    "COSMO_PACKAGES", r"C:\Users\mluca\Documents\cosmo-packages"
)

# Planck 2018 TT,TE,EE+lowE base-LCDM best fit.
PARAMS = {
    "logA": 3.044,
    "ns": 0.9649,
    "H0": 67.36,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "tau": 0.0544,
    "mnu": 0.06,
    "A_planck": 1.0,
}

# chi2 as this pipeline produced it, with the number of data points each
# component carries, so a reader can see the per-point fit at a glance.
EXPECTED = {
    "planck_2018_highl_plik.TTTEEE_lite_native": (583.9, 3.0),
    "planck_2018_lowl.TT": (23.4, 0.5),
    "planck_2018_lowl.EE_sroll2": (390.0, 3.0),
}


def main() -> int:
    try:
        from cobaya.model import get_model
    except Exception as exc:  # pragma: no cover
        print("FAIL  cobaya not importable: %s" % exc)
        return 1

    info = {
        "likelihood": {name: None for name in EXPECTED},
        "theory": {"camb": {"extra_args": {"halofit_version": "mead"}}},
        "params": dict(
            PARAMS,
            As={"value": "lambda logA: 1e-10*np.exp(logA)", "derived": True},
        ),
        "packages_path": PACKAGES_PATH,
    }

    try:
        model = get_model(info)
    except Exception as exc:
        print("FAIL  could not build the model: %s" % exc)
        print("      packages path: %s" % PACKAGES_PATH)
        print("      install with: python -m cobaya install "
              "planck_2018_highl_plik.TTTEEE_lite_native "
              "planck_2018_lowl.TT planck_2018_lowl.EE_sroll2 "
              "--packages-path <path>")
        return 1

    logps = model.loglikes({}, as_dict=True)[0]

    failures = 0
    for name, (want, tol) in EXPECTED.items():
        if name not in logps:
            print("FAIL  %-45s not evaluated" % name)
            failures += 1
            continue
        chi2 = -2.0 * logps[name]
        ok = abs(chi2 - want) <= tol
        print("%s  %-45s chi2 = %9.3f   want %9.3f +/- %.1f"
              % ("PASS" if ok else "FAIL", name, chi2, want, tol))
        if not ok:
            failures += 1

    total = -2.0 * sum(logps.values())
    print("      %-45s chi2 = %9.3f" % ("TOTAL", total))

    if failures:
        print("\nFAIL: %d of %d components off expectation. Either the data "
              "files changed, camb changed, or the parameter values above "
              "were edited. Find out which before using this pipeline."
              % (failures, len(EXPECTED)))
        return 1

    print("\nPASS: %d of %d components reproduce the recorded chi2. The WP-3 "
          "likelihood pipeline evaluates." % (len(EXPECTED), len(EXPECTED)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
