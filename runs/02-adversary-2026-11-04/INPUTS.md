# Staged inputs for Run 02 (adversary)

This directory is the adversary's entire view of the project. Isolation is
**enforced by file staging**, not by instruction, so the run can state
plainly that it could not have read the withheld material.

Target: Run 01 of `michaelClucas/The-Observer-Problem`, on branch
`run-01-consolidate` (PR #3, unmerged at staging time). Repo `main` was at
`5fbc9af`.

## Staged

| Path | Source |
| --- | --- |
| `target/OUTPUT.md` | the target run's output, verbatim |
| `target/OUTPUT.json` | the target run's structured output, verbatim |
| `target/META.yaml` | the target run's metadata |
| `docs/problem-statement.md` | repo `main` |
| `docs/common-scaffold.md` | repo `main` |
| `protocol/EVIDENCE-RULES.md` | repo `main` |
| `protocol/output-schema.md` | repo `main` |
| `protocol/METHOD.md` | repo `main` |
| `prompts/00-system-adversary.md` | repo `main` |
| `prompts/02-adversary.md` | repo `main` |

## Withheld, deliberately

- **`docs/approach-clusters.md`** — the hand-written seed cluster map the
  target run was asked to correct. Per `prompts/02-adversary.md`, an
  adversary holding the seed will mistake seed agreement for verification.
- **`target/REVIEW.md`** — the target's self-review. The adversary forms
  its own rubric scores first; the self-review is supplied separately only
  once Parts 1-3 are written, for Part 4.
- **`sources/bibliography.md`** — the unverified seed bibliography. It is
  part of the seed and would supply unretrieved leads as though they were
  a reading list.

The adversary has no git access and no repository checkout, so it cannot
reach the withheld files. Its output is committed by the operator after
the fact.

## Known anchoring risk in a staged input

`target/META.yaml` contains a section headed `CARTOGRAPHER-OWNED
VERIFICATION` in which the target run asserts that two arXiv identifiers
(2206.10780 and 2112.12828) are correct, with titles, authors and DOIs.

This was left in place rather than stripped, because doctoring a staged
input is worse than disclosing one. The adversary is instructed to treat
those assertions as claims to be checked, not as established, and to
re-fetch both itself. If it accepts them without checking, that is a
finding about this run.

`target/META.yaml` also discloses that the target ran on a **forked
context** carrying the seed author's uncited reasoning. The adversary needs
this, because it bears directly on whether the target's stated confidence
tracks retrieved evidence or prior belief.
