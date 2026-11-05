#!/usr/bin/env bash
# Obtain dataset 001: Planck 2018 plik_lite TTTEEE, low-l TT, low-E sroll2.
#
# This is the command that was actually run on 2026-11-05. It is runnable.
#
# The raw data is not committed to this repository; this script plus
# MANIFEST.sha256 is the record. Re-running it on a different machine and
# verifying against MANIFEST.sha256 is how a WP-3 fit is reproduced.
#
# These are the *_native likelihoods: pure-Python reimplementations
# distributed with cobaya, not the Planck collaboration's clik library.
# clik does not build on this platform; env/requirements.txt records what
# was tried. The data files are Planck's, the evaluating code is cobaya's,
# and a disagreement could live in either.

set -euo pipefail

PACKAGES_PATH="${COSMO_PACKAGES:-$HOME/cosmo-packages}"
PYTHON="${PYTHON:-.venv/Scripts/python}"

echo "Installing into: ${PACKAGES_PATH}"
echo "Using python:    ${PYTHON}"

"${PYTHON}" -m cobaya install \
    planck_2018_highl_plik.TTTEEE_lite_native \
    planck_2018_lowl.TT \
    planck_2018_lowl.EE_sroll2 \
    --packages-path "${PACKAGES_PATH}"

echo
echo "Installed. Expected layout under ${PACKAGES_PATH}/data :"
echo "  planck_2018_pliklite_native/   7 files, 3278143 bytes"
echo "  planck_2018_lowT_native/       6 files, 14154454 bytes"
echo "  planck_sroll2_lowE_native/     2 files, 2187002 bytes"
echo
echo "Verify against the committed manifest:"
echo "  cd ${PACKAGES_PATH}/data"
echo "  sha256sum -c <repo>/data/001-planck-2018-plik-lite/MANIFEST.sha256"
echo
echo "If every file reports FAILED, check for carriage returns in the"
echo "manifest before suspecting the data. See SOURCE.md and"
echo "michaelClucas/The-Observer-Problem#11."
echo
echo "Then check the likelihood evaluates:"
echo "  ${PYTHON} verify/planck_likelihood.py"
