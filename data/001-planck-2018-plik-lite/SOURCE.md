# 001 - Planck 2018 `plik_lite` TTTEEE, low-l TT, and low-E sroll2

Obtained 2026-11-05 (the directory timestamps on this machine read
2026-11-05 11:28-11:29). Recorded against `data/README.md`'s seven fields.

The raw data is **not** committed, per `data/README.md`. What is committed
is this file, `fetch.sh`, `MANIFEST.sha256` and `cuts.md`.

**Location on this machine:** `C:\Users\mluca\Documents\cosmo-packages`,
which is what `verify/planck_likelihood.py` reads via the `COSMO_PACKAGES`
environment variable, defaulting to that path. The directory is outside the
repository and is not gitignored by it; it is cobaya's package tree.

---

## 1. The URL or archive, specific to the release

Not a direct download. Obtained through cobaya's installer, which fetches
from the Planck Legacy Archive and from the cobaya maintainers' mirrors of
the native-Python reimplementations:

```
python -m cobaya install planck_2018_highl_plik.TTTEEE_lite_native \
                         planck_2018_lowl.TT \
                         planck_2018_lowl.EE_sroll2 \
                         --packages-path C:\Users\mluca\Documents\cosmo-packages
```

Reproduced verbatim in `fetch.sh`.

**Why the indirection matters and is recorded rather than hidden.** These
are the `_native` likelihoods: pure-Python reimplementations distributed
with cobaya, not the Planck collaboration's own `clik` library. `clik` does
not build on this platform and `env/requirements.txt` records what was
tried. The underlying **data files** are Planck's; the **likelihood code**
evaluating them is cobaya's. Anyone reproducing a WP-3 result needs to know
that, because a disagreement could live in either.

Upstream data origin, for the record: Planck Legacy Archive,
`pla.esac.esa.int`, PR3 (2018) release, `COM_Likelihood_Data-baseline_R3.00`.
**Not verified by me against the PLA today** — I obtained the files through
cobaya and did not independently re-download from the archive. That is a
`[LEAD]` on the upstream provenance, and the `MANIFEST.sha256` in this
directory is the authority on what is actually on disk.

## 2. The release or version string, as the providers name it

- `plik_lite`: **v22**, named in the filenames themselves
  (`c_matrix_plik_v22.dat`, `cl_cmb_plik_v22.dat`,
  `plik_lite_v22.dataset`).
- All three directories carry `version.dat` containing `v1`, which is
  cobaya's packaging version for the native reimplementation, **not** a
  Planck release string. Both are recorded because they are different
  things and conflating them is how a dataset gets quietly reused.
- Planck release: **PR3**, the 2018 baseline likelihood.
- `EE_sroll2`: the SRoll2 low-E likelihood, Pagano et al. 2020. Its single
  file is a precomputed probability table; no internal version string.

## 3. Size on disk

19 MB total.

| Directory | Files | Bytes |
| --- | --- | --- |
| `planck_2018_pliklite_native` | 7 | 3,278,143 |
| `planck_2018_lowT_native` | 6 | 14,154,454 |
| `planck_sroll2_lowE_native` | 2 | 2,187,002 |

Per-file sizes and checksums are in `MANIFEST.sha256`.

## 4. The reference to cite

- **Planck 2018 results. V. CMB power spectra and likelihoods**, Planck
  Collaboration, arXiv:1907.12875, A&A 641 (2020) A5. The `plik_lite`
  construction and its marginalisation are described there.
- **Planck 2018 results. VI. Cosmological parameters**, arXiv:1807.06209,
  A&A 641 (2020) A6. Source of the best-fit parameter values that
  `verify/planck_likelihood.py` evaluates at.
- **SRoll2**, Pagano, Delouis, Mottet, Puget & Vibert, arXiv:1908.09856,
  A&A 635 (2020) A99, for the low-E likelihood.
- **cobaya**, Torrado & Lewis, arXiv:2005.05290, JCAP 05 (2021) 057, for
  the native likelihood implementations actually evaluated here.

## 5. What it can settle, in this repository's terms

**The shape of a correction to the primordial curvature power spectrum**,
which is exactly WP-3's question.

Specifically, it bears on **Run 01's open question 4** and the **C-versus-D
pairing** recorded in Run 01 §2.3 as `non_competing` on scope but
`genuine_conflict` in a predicted observable. Both the collapse (C) and
decoherence (D) corrections take the form
`P(k) = P_0(k)[1 + f(k/k_*; theta)]` with different `f`, and this dataset
constrains `f`.

The index values the two sides predict are published and were read at
primary level on 2026-11-05 (see
`maple/jobs/003-power-spectrum-corrections/JOB.md`): the C side gives
`f ~ (k/k_*)^-1` for inflation-era crossing and `(k/k_*)^-10` for
radiation-era crossing; the D side gives `f ~ (k/k_*)^(p+2n-7)`. The binned
TTTEEE spectrum spans `l = 30` to `2508`, roughly two decades in `k`, which
is enough lever arm to separate shapes differing by an integer power.

## 6. What it cannot settle

Written out, because `data/README.md` says this is the field most often
omitted and the one that stops a dataset being reused for a question it
cannot answer.

- **Anything at `l < 30` from `plik_lite`.** The high-l likelihood starts
  at `l = 30` (`bin_lmin_offset = 30` in `plik_lite_v22.dataset`). The low-l
  TT and EE likelihoods cover below that, and there cosmic variance
  dominates, which is the floor job 002 is computing. So the large-scale end
  of a steep correction like `(k/k_*)^-10` is constrained by the **low-l**
  components, whose error budget is irreducible, not by `plik_lite`.
- **Which collapse operator is correct.** Established in
  `findings/002-wp4-csl-cosmological-bound.md` and in Run 01: the entire
  spread between the CSL camps comes from the operator choice, and no CMB
  measurement selects it. This dataset does not and WP-3 must not claim it
  does.
- **Anything about higher-order correlators.** This is a two-point dataset.
  WP-6's question is specifically about what two-point statistics
  **cannot** see — Martin & Vennin 2016 show a zero-discord classical state
  reproduces every super-Hubble two-point correlator exactly — so WP-6
  needs the non-Gaussianity constraints, which are not in this directory
  and are a separate dataset with a separate `SOURCE.md` when it is
  obtained.
- **Foreground or calibration physics.** Marginalised out before this data
  exists. See field 7.
- **Anything requiring pixel-space analysis.** `healpy` is unavailable on
  this platform and `env/requirements.txt` records that nothing substitutes
  for it.

## 7. What model assumptions it was reduced under

**`data/README.md` says this is the field that bites here, and it does.**
WP-3 compares two modifications of the curvature power spectrum, so what
was marginalised, and under what model, decides whether the comparison
means anything.

### `plik_lite` is a compressed, pre-marginalised likelihood

The `plik_lite` construction takes the full `plik` likelihood, which has
foreground and calibration nuisance parameters, and **marginalises them
out**, leaving a binned CMB-only spectrum with a covariance that carries
their residual uncertainty. What is on disk is the end of that process:

- `cl_cmb_plik_v22.dat` — the binned CMB bandpowers.
- `c_matrix_plik_v22.dat` — the binary covariance, 3,006,160 bytes, which
  for a 613 x 613 symmetric double matrix is the expected size
  (613^2 x 8 = 3,006,152 plus an 8-byte header). The bin counts are stated
  in `plik_lite_v22.dataset`: `nbintt = 215`, `nbinte = 199`,
  `nbinee = 199`, total **613 bandpowers**.
- `blmin.dat`, `blmax.dat`, `bweight.dat` — the binning operator.

**One nuisance parameter survives**: the overall Planck calibration
`A_planck`, which `verify/planck_likelihood.py` sets to 1.0. Everything
else is gone.

### The three assumptions that matter for WP-3, named

1. **The foreground marginalisation was performed assuming the underlying
   CMB spectrum is the base-LCDM one**, over the `plik` nuisance
   parameters' priors. A correction `f(k/k_*)` large enough to change which
   foreground amplitudes the data prefers is therefore **not** correctly
   constrained by `plik_lite`: the compression assumed it away. This bounds
   WP-3's claim to **small** corrections, and WP-3 must state that bound
   rather than quote a limit as if it held for arbitrary `f`.
2. **The binning is fixed and was chosen for a smooth spectrum.** A
   correction with structure narrower than a bin is averaged over and
   cannot be distinguished from a smooth one of the same bandpower. Both
   of WP-3's candidate `f` are smooth power laws, so this is not binding
   here — but it would be for an oscillatory correction, and recording it
   is what stops someone reusing this directory for one.
3. **The covariance includes the residual foreground and calibration
   uncertainty but assumes Gaussian bandpower likelihoods.** Standard at
   `l >= 30`, and the reason the low-l components use separate,
   non-Gaussian treatments (`cl2x` tables for TT, a probability table for
   EE) rather than being folded into the same covariance.

### For the low-l components

- `planck_2018_lowl.TT` uses precomputed `cl2x` transform tables plus a
  covariance, i.e. a non-Gaussian likelihood in a transformed variable,
  reduced under the assumption that the transform was calibrated on
  base-LCDM-like spectra.
- `planck_2018_lowl.EE_sroll2` is a **precomputed probability table**:
  `sroll2_prob_table.txt`, 2.19 MB. Its reduction is entirely upstream and
  opaque from the file. Anything WP-3 concludes from the low-E component
  inherits Pagano et al.'s systematics treatment wholesale, and this file
  gives no handle on it. **That is a real limitation on the `l < 30` end
  of WP-3's constraint and is recorded as one.**

### The consequence for WP-3, stated before any fit

WP-3's constraint on `f(k/k_*)` is valid for corrections small enough not
to have altered the foreground marginalisation, over `l = 30` to `2508`
from `plik_lite`, with the `l < 30` end carried by two likelihoods whose
own reductions assume base-LCDM. A quoted limit must say that. The
`(k/k_*)^-10` C-side branch puts most of its weight at low `l`, which is
exactly where the data's own reduction is least transparent and the floor
is largest — so that branch is expected to be the weaker-constrained of the
two, and saying so now rather than after the fit is what `cuts.md` is for.

---

## Verifying the manifest

```
cd C:\Users\mluca\Documents\cosmo-packages\data
sha256sum -c <repo>/data/001-planck-2018-plik-lite/MANIFEST.sha256
```

**If every file reports FAILED, check for carriage returns before
suspecting the data.** Git's CRLF conversion corrupts `.sha256` manifests;
this is a known defect with a fix pending in
michaelClucas/The-Observer-Problem#11, not yet on `main`. A
`data/.gitattributes` in this repository marks `*.sha256` as `-text` to
prevent it locally, scoped to `data/` so a root-level fix does not conflict.
