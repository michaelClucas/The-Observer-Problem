# Local verification

One runnable script per topic: `verify/<topic>.py`.

Rules, and they are not negotiable:

- **Every number that appears in prose anywhere in this repository comes
  from a script here, or from a Maple `RESULT.txt`.** Including arithmetic
  you are confident about. Run 01 tagged its own arithmetic `[SOURCED]`,
  which is how a derived figure acquires the appearance of a measurement.
- A script **exits non-zero on failure** and prints what failed.
- A script is **run before it is committed**, and its output goes in the
  day log.
- A script takes no hidden state: no edited constants between runs, no
  commented-out branches that were used to get the committed number.

A Maple result with a `crosscheck.py` here is worth considerably more than
one without, because otherwise it is one machine's word.
