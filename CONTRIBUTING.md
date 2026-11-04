# Contributing

## Most useful contributions

1. **Corrections to `docs/approach-clusters.md`.** It was written by hand
   and from memory. Misattributions, missing approaches, and wrong cluster
   boundaries are all worth a PR, however small.
2. **Verified citations** for anything in `sources/bibliography.md` marked
   unverified. Add the DOI or arXiv id and move it up.
3. **Replication runs.** Run an existing prompt on a different model and
   commit the result as a new run directory. This is the single highest
   value contribution and requires no domain expertise.
4. **Reviews.** Score an existing run against the rubric in
   `protocol/METHOD.md`. Disagreeing with an existing review is fine;
   add yours rather than editing theirs.

## Rules

- **Never edit a committed `OUTPUT.md` or `OUTPUT.json`.** Runs are
  append-only. Corrections go in `REVIEW.md` or a later run.
- **Never edit a prompt that a run has used.** Fork it to a new number.
- **Follow `protocol/EVIDENCE-RULES.md`** in prose contributions too, not
  only in agent runs. Tag claims, cite primary sources, mark leads as
  leads.
- **One concern per PR.** A citation fix and a cluster restructure are two
  PRs.

## Submitting a run

Include `META.yaml` with the exact model id and the git sha of the prompt
as used. A run whose prompt cannot be reconstructed from the repository is
not a data point and will be closed.

Run the validator and record its result in your `REVIEW.md`:

    python protocol/validate.py runs/<run>/OUTPUT.json

A deliberate rule violation is acceptable when the contract gives you no
honest way to comply; say so in `REVIEW.md` and leave it visible. An
undeclared violation will be found, because the check is mechanical.

For an adversary run, stage the permitted inputs in their own directory and
give the agent no repository checkout. A withholding that depends on the
agent choosing not to read a file it holds is not a withholding, and the
run cannot then claim it did not see the seed. Record what was staged in an
`INPUTS.md` beside the run.

If the run was expensive, say so in `META.yaml` notes. Cost per usable
finding is part of what the method experiment is measuring.

## Disagreement

Open an issue, not a PR, for disputes about the scaffold or the problem
statement. Those shape every future run, so they get discussed before they
change.
