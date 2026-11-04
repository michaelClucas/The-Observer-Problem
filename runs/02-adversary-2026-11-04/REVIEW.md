# Operator verification of Run 02

**This is not an independent rubric review.** `protocol/METHOD.md` asks for
one per run, and Run 02 has not had one. What follows is only what the
operator checked mechanically before committing, so a reader knows which of
the run's claims about itself have been confirmed and which are still its
own word.

An independent review of Run 02 is still owed, and it should be written by
someone who did not stage its inputs.

## Checked and confirmed

- **All five parts present**, in order, in `OUTPUT.md`: Findings, What you
  verified and found sound, Your own rubric scores, Divergence from the
  self-review, Verdict. No preamble before Part 1.
- **`OUTPUT.json` parses.** 11 findings, 10 `CONFIRMED` and 1 `PLAUSIBLE`,
  distributed across surfaces S-1, S-3, S-4, S-6, S-8 and S-9.
- **Every finding carries quoted text and a corrected statement.** The role
  card requires four parts per finding; the two that are mechanically
  checkable are present on all 11.
- **Scores were not revised after Part 4.** The run reported 2 / 3 / 1 / 3 /
  2 to the operator before `target/REVIEW.md` was supplied, and
  `OUTPUT.json` records the same five values with
  `formed_before_reading_target_review: true`. No upward drift after
  reading the target's 12/15.
- **Surfaces returning zero findings are recorded** rather than omitted,
  which is what the role card asks for and the opposite of padding.

## Isolation, and its limits

Isolation was enforced by file staging, not by instruction. The run had no
git access and no repository checkout, only the directory recorded in
`INPUTS.md`. It therefore could not have read `docs/approach-clusters.md`,
`sources/bibliography.md`, or the target's `REVIEW.md` before Part 4. That
claim is structural rather than something the run asks to be believed.

Two limits the operator introduced and should own:

1. **`target/META.yaml` was staged with a known anchoring risk.** It
   asserts that two arXiv identifiers are correct, with titles, authors and
   DOIs. It was left in place rather than stripped, on the view that
   doctoring a staged input is worse than disclosing one, and the run was
   told to re-fetch both. It reports that it did, before reading the
   cluster those identifiers belong to.
2. **S-7 was uncheckable because of a defect in the prompt.**
   `prompts/02-adversary.md` asks the adversary to check the target against
   the known-gaps list, and withholds the only file that contains it. The
   run was told not to work around this and to file it as a prompt defect.
   The prompt needs a new version that either stages the known-gaps section
   alone or drops S-7. This is a finding Run 02 produced about the
   protocol, not a shortfall in Run 02.

## What the operator confirmed about the *target* independently

Computed from `runs/01-consolidate-approaches-2026-11-04/OUTPUT.json`
before Run 02 began, so Run 02's agreement with these is not circular:

- 7 clusters, 42 members, 294 slot entries, no member missing a slot.
- 121 `empty`, 19 `misfit`, 1 `denied`, 153 `filled`. 47.6%, matching the
  target's stated 48%.
- 109 entries tagged `SOURCED` with an empty `sources` array.
- 41 relations: 5 `notational_variant`, 24 `genuine_conflict`, 9
  `non_competing`, 3 `unresolved`.
- The target's `prompt_commit` matches the real blob sha of
  `prompts/01-consolidate-approaches.md` at `d137e6d`.

So the target's self-reported numbers are accurate. Run 02's findings are
about what those numbers mean, which the operator did not attempt to judge.

## Not checked

- **The 210-locator sweep was not re-run.** This is the run's central
  claim and the whole basis of its verdict that the target is not
  discarded. It rests on the run's own word.
- **None of the 11 findings was independently confirmed.** The operator
  read them; that is not verification.
- **Content sampling.** The run states it checked locator *content* at
  claim level for about 9% of distinct works, purposively rather than
  randomly, and carried the unsampled remainder into its own axis 1 and
  axis 5 scores. That self-limitation was not audited.

## What a later run should do first

1. **Independently review Run 02** against the rubric, by someone who did
   not stage its inputs.
2. **Re-run a random sample of the 210-locator sweep.** A purposive sweep
   confirmed by a random sample is much stronger than either alone.
3. **Fix `prompts/02-adversary.md`** so S-7 is checkable, as a new numbered
   prompt rather than an edit.
4. **Fix `protocol/output-schema.md`** to express a sourced absence. Run 02
   splits the 109 entries 96/13 into schema gap and real violation, which
   is the sharpest statement of the problem so far and should drive the
   fix.
5. **Act on the five mis-verdicted relations and two mis-sourced ones** in
   a later cartography run, not by editing Run 01's output.
