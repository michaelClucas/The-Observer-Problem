# Datasets: provenance and what is committed

Aligned with the sibling repository's `data/README.md`. Raw data is **not**
committed; the record of what was obtained and the code that obtained it
is, so a fit can be reproduced without the repository carrying gigabytes.

```
data/
  README.md              this file
  NNN-<dataset>/
    SOURCE.md            where it came from, exactly
    fetch.sh             the command that downloads it, runnable
    MANIFEST.sha256      checksums of every file used
    cuts.md              the selection applied, and why
```

`cuts.md` is written **before** the result is seen, not after.

## SOURCE.md must answer

1. **The URL or archive**, specific to the release, not a project homepage.
2. **The release or version string**, as the providers name it.
3. **Size on disk.**
4. **The reference to cite**, with a DOI or arXiv identifier.
5. **What it can settle**, in this repository's terms — which pairing or
   open question in the map it bears on.
6. **What it cannot settle.** Most often omitted, and the field that stops
   a dataset being quietly reused for a question it cannot answer.
7. **What model assumptions it was reduced under**, and which.

Field 7 is the one that bites here. `plik_lite` is a compressed likelihood:
the foreground and calibration nuisance parameters have already been
marginalised, under a model. For WP-3, which compares two modifications of
the curvature power spectrum, what was marginalised and under what
assumptions determines whether the comparison means anything. Record it
with the data, because it is a property of the data as obtained and not of
the analysis that follows.

For non-Gaussianity constraints (WP-6), the analogous question is which
template the quoted `f_NL` is a constraint on. A bound on the local
template is not a bound on an arbitrary higher-order correlator, and the
difference is the whole of WP-6.
