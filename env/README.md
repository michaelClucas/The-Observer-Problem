# Environment

`requirements.txt` records versions that were **installed and actually
imported on this machine**, not versions that ought to work. It does not
exist yet; the first cycle that needs a package writes it, pinned to what
was run.

Verified on the sibling repository and expected to hold here: Python
3.14.7, numpy 2.5.4, scipy 1.18.1, sympy 1.14.0, astropy 8.0.2,
camb 2.0.5, cobaya 3.6.2, emcee, getdist, dynesty, iminuit.

**`classy` is unavailable on this platform.** pip reports no distribution
for any version. camb substitutes. Do not add a dependency on CLASS.

A plan resting on untested tooling is worthless, so a version here that was
not imported in this environment is a defect, not a convenience.
