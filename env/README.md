# Environment

`requirements.txt` records versions that were **installed and actually
imported on this machine**, not versions that ought to work. It does not
exist yet; the first cycle that needs a package writes it, pinned to what
was run.

It exists and is verified as of 2026-11-05: every pin installed into a
clean `.venv` on Python 3.14.7, and camb run rather than merely imported
(`rdrag = 146.989`, `thetastar = 1.04465` - the same figures the sibling
repository recorded from an independently built venv).

`.venv/` is gitignored. Rebuild with:

```
python -m venv .venv
.venv/Scripts/python -m pip install -r env/requirements.txt
.venv/Scripts/python verify/planck_likelihood.py
```

**Three packages are unavailable here**, each tried and recorded in
`requirements.txt`: `classy` (no distribution for any version), `healpy`
(wheels fail to build; no Windows support) and `clik` (not attempted; does
not build on Windows). camb substitutes for CLASS and the pure-Python
cobaya components substitute for clik. Nothing substitutes for healpy, so
pixel-space map analysis does not run on this machine.

A plan resting on untested tooling is worthless, so a version here that was
not imported in this environment is a defect, not a convenience.
