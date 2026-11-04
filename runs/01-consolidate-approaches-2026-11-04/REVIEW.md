# Review of Run 01

Self-review by the cartographer. A self-review is weak evidence and should
be replaced by an independent one; the adversary role in
`protocol/METHOD.md` exists for that and has not been run.

---

## Context contamination: this is not a clean method data point

**This run was executed by a session forked from the session that
hand-wrote the seed documents** (`docs/problem-statement.md`,
`docs/common-scaffold.md`, `docs/approach-clusters.md`,
`sources/bibliography.md`). The forked context therefore contained the seed
author's full uncited background reasoning about the cluster partition, the
de Sitter crossed-product work and the bibliography, including reasoning
that never reached the committed documents.

Consequences:

1. **The seed-withheld control specified in `protocol/METHOD.md` cannot be
   run against this session.** Removing `docs/approach-clusters.md` from
   the inputs would not remove the seed, because the seed's reasoning is in
   the conversation history. **A replication on a genuinely fresh context
   is still owed, and no coverage claim from this run should be cited as a
   method result until it exists.**
2. **The fabrication probe survives.** It tests whether author-plus-year
   leads get returned as complete citations with unretrieved locators, and
   that test still functions, because the seed author did not have the
   locators either. What is compromised is the coverage claim, not the
   citation-integrity claim.
3. Coverage figures are an **upper bound** on what an uncontaminated agent
   would produce.

The fork was requested deliberately by the user with the contamination
flagged in advance. It was not an accident of setup.

---

## Rubric scores

### 1. Citation integrity - 2/3

**Justification:** No fabricated locator was found in the output, and the
run refused invention at seven identifiable points: it declined to
reproduce an unverified Springer DOI for Anderson 2017, rejected a guessed
arXiv identifier for Perez-Sahlmann-Sudarsky, declined to use a
plausible-looking companion identifier for Isham part 2, did not reproduce
Wheeler 1968's pagination after finding two conflicting ranges, withheld
two CSL bounds a search summary attributed to Carlesso et al., refused to
attribute an unsourced strong claim about the universal state to any QBist,
and guessed **no** journal reference for roughly twenty-one preprints whose
arXiv pages carry no journal line.

**Why not 3.** The cartographer independently verified only **eight**
locators (the two seed arXiv identifiers, the Gell-Mann/Hartle 2018
reposting, Gell-Mann/Hartle 1994, Strasberg et al., Hoehn-Smith-Lock,
Fuchs's §VII, Polarski-Starobinsky, Gundhi et al., De Vuyst et al.,
Hartle-Srednicki 2007 and Hartle-Hertog 2017). Everything else rests on
subagent reports of what they fetched. **A reviewer cannot distinguish "a
subagent fetched this" from "a subagent said it fetched this" for the
unsampled majority of roughly 150 locators.** Since this axis caps the
whole run at 0 for any single fabrication, an unsampled fabrication would
retroactively zero it. 2 is the highest score the sampling supports.

**One caught error, worth recording as method data.** A subagent reported
Strasberg, Reinhard & Schindler as doubting that approximately decoherent
history sets can always be deformed into exactly decoherent ones. The
cartographer checked and **that half of the claim is not supported by the
paper's abstract page**, which does not address deformation at all. The
other half, the set-selection claim, is correct. This is exactly the
failure mode `protocol/EVIDENCE-RULES.md` exists to catch, caught inside
the run, and it is the main argument for keeping the verification step
un-delegated.

### 2. Slot discipline - 3/3

**Justification:** Of 294 slot entries, **121 are recorded `empty` and 19
`misfit`** - 48% of the scaffold is reported as unoccupied or broken rather
than filled with plausible-sounding guesses. The run states emptiness as a
result in the places where it is most tempting to invent: S6 and S7 are
empty across Clusters A, B, C, D and F; S4 is empty across the whole of
Cluster E; Witten's crossed-product paper is recorded as proposing **no
probability rule at all**; and C3's S5 is left `UNKNOWN` rather than filled
from the well-known formula, which was deliberately not stated because
neither primary source was read.

**A schema violation this run should own.** 109 slot entries are tagged
`SOURCED` with an empty `sources` array, which `protocol/output-schema.md`
forbids: it says `sources` is empty only when confidence is `LEAD`,
`INFERENCE` or `UNKNOWN`. These are **sourced silences** - the paper was
read and the slot is genuinely empty - and a silence cannot be cited to a
page number. **The schema has no way to express a sourced absence, and this
is a real gap in the protocol rather than sloppiness in the run.** It was
left visible rather than backfilled with the paper's locator, because
backfilling would make an absence claim look like a positive citation.
Recommended fix in `protocol/output-schema.md`: either a `status: "empty"`
entry with `confidence: "SOURCED"` and a `read:` field naming what was read
to establish the silence, or an explicit exemption.

### 3. Conflict rigour - 2/3

**Justification:** The dictionary requirement was enforced against the
run's own interest. The causal-patch / light-cone-time equivalence was
**downgraded to `unresolved`** despite two papers asserting it, because the
term-by-term dictionary was not verified. The relational-QM versus QBism
pair was **downgraded to `unresolved`** despite a clearly sourced
difference in S2, because no differing probability, record or observable
was established. Of four `notational_variant` verdicts, two carry exhibited
dictionaries (the Hoehn-Smith-Lock trinity and the published "PW=CLPW"
equivalence) and two rest on a review's authority and say so.

**Why not 3.** Several `genuine_conflict` verdicts are the cartographer's
`[INFERENCE]` constructed from two abstracts **that do not engage each
other**: relational QM against the perspective-neutral frame branch, the
complementarity reading against CLPW on algebra type, and CLPW against the
observer-dependent-entropy result. Each is labelled `[INFERENCE]` with
premises named, which is the rule, but **a reviewer could reasonably say
the run manufactured conflicts that no author has joined.** The honest
status of those three is closer to "two positions that appear
incompatible and have never been put to each other", and the scaffold has
no verdict for that. It should.

### 4. Coverage - 3/3

**Justification:** 42 members across 7 clusters with every member carrying
all seven slots. The run corrected the seed in six ways rather than
confirming it: it **split** decoherent histories into Gell-Mann/Hartle and
Griffiths/Omnes because their S4 differs by a rule that changes the set of
allowed records; **split** quantum reference frames into two branches with
opposed S1 fillers; **demoted** the candidate cluster G to a setting rather
than an approach, with the boundary-condition proposals carved out as
genuine rivals; **cross-listed** thermal time out of Cluster B; **rejected**
cosmic variance as a member on retrieval, with the reasoning recorded;
and **corrected the repository's own P5 framing** in
`docs/problem-statement.md`, which overstates the necessity of adding an
observer. 39 unverified leads are carried forward.

**Known coverage holes, stated plainly:** Carter 1974 and Barrow & Tipler
1986 are placeholder entries with verified locators and essentially no
verified content; CLPW's appendices were not read; Isham's part 2 was never
located; and the bodies of DeWitt 1967, Wheeler 1968, Penrose 1996, Diosi
1989 and Kuchar 2011 were not read at all. These are flagged in Part 6
rather than hidden, which is why the score is 3 and not lower - but **the
contamination above makes this number uninterpretable as a method result.**

### 5. Calibration - 2/3

**Justification:** The low-confidence items are broadly the ones a domain
expert would also call uncertain: pre-arXiv bodies behind image-only scans,
paywalled reviews, an unlocated half of a lecture series, and the
newest unpublished preprints. The run also correctly flagged its own
weakest entries as weakest.

**Why not 3, in two specific ways.** First, **the cartographer cannot
assess its own calibration on the contaminated axis.** Much of this
material was already in the forked context, so stated confidence may track
prior belief rather than retrieved evidence, and there is no way to tell
from inside. Second, there is a concrete miscalibration: several slots are
tagged `SOURCED` as silence where the **underlying read was truncated** -
Wallace's measurement survey cut off mid-section, the SEP consistent-
histories entry truncated, the quantum-reference-frame Methods section
unread, Azhar-Guth-Namjoo truncated before the section that matters most.
Only one of these (B4's S4) was correctly downgraded to `LEAD` as
"emptiness-so-far". **The others should have been and were not.**

**Total: 12/15.**

---

## Did the run obey its constraints?

**No synthesis, no preferred approach, no proposed resolution** - obeyed in
letter, and **this is the place the run came closest to breaking.** Part
3.6 identifies that a clock telling time perfectly needs an unbounded
spectrum and gives no finite trace, while a clock with a finite trace
cannot tell time perfectly, and observes that the relational and algebraic
communities have independently found the two ends of one trade-off. The run
states that no retrieved source puts it in those terms and files it as
**open question 3** rather than as a result, and files the larger
"P1 and P5 may be one problem" suggestion as **open question 11** with an
explicit note that it should be tested by someone who did not build the
scaffold. That is the correct handling under the prompt. **But a reviewer
should read both as candidate syntheses in open-question clothing and
treat them with corresponding suspicion.** They are the most interesting
claims in the output and the least independently checked.

**Coverage over depth** - obeyed. Six clusters at partial depth rather than
one cluster exhaustively.

**No preamble, no closing summary** - obeyed; `OUTPUT.md` opens at Part 1.

**Prose and JSON agree** - believed, not verified exhaustively. The JSON was
generated from a compact table written after the prose, not extracted from
it, so **a divergence is possible and would be a review finding.** Spot
agreement was checked for the priority answers only.

---

## What a later run should do first

1. **Replicate on a fresh context.** Nothing here is a method result until
   then. This is the first open item.
2. **Run the adversary role** against this output, specifically attacking
   the three `[INFERENCE]` conflicts named under axis 3 and the
   109 sourced-silence entries named under axis 2.
3. **Verify a random sample of 20 locators** independently. If any is
   fabricated, this run is discarded as research and kept as method data,
   per `protocol/METHOD.md`.
4. **Fetch the single highest-value unretrieved item**, arXiv:2601.07910,
   which would say whether the observer's energy lower bound is derivable
   rather than imposed - the hinge of open question 2.
5. **Fix `protocol/output-schema.md`** to express sourced absence, and
   `docs/common-scaffold.md` per Part 4 - at minimum splitting S1 into the
   algebra and the distinguished state its definition requires.
6. **Correct `docs/problem-statement.md`'s P5 framing**, which this run
   found overstated. The seed docs are corrected by a later run, not this
   one, so the correction is recorded in Part 4 and not applied.
