# Part 1 - Findings

Ten `CONFIRMED`, one `PLAUSIBLE`. Ordered by how much of the target run's
conclusion they damage.

Coverage statement, placed first because it bounds everything below.
Locator *existence and attribution* was swept exhaustively: all 133 distinct
arXiv identifiers and all 77 distinct DOIs in `OUTPUT.md` and `OUTPUT.json`
were resolved by me in this run, 210 of 210, with zero fabrications and zero
resolving to a different work. Locator *content* was sampled, not swept; the
method and the unsampled remainder are stated in Part 2 and carried into my
own axis 1 and axis 5 scores in Part 3.

---

## C-1. The one Cluster G rivalry is sourced to a result that says the opposite about the pair

`CONFIRMED` · S-1 (failure mode 2), S-6 · Damage: high

**The text attacked.** `OUTPUT.md` §2.3, row "G3a no-boundary ↔ G3b
tunneling" (line 2419):

> "With Picard-Lefschetz theory and no-boundary initial conditions the
> dominant saddle's exponential factor is precisely the inverse of the
> Hartle-Hawking result, so **the two proposals order the probability of
> inflation oppositely.** This is what makes them rivals rather than
> variants. `[SOURCED]` for layer 1"

Same claim at lines 2148-2159 and in Cluster G findings #1 (line 2300);
`OUTPUT.json` relation 36, `verdict: genuine_conflict`,
`differs_in: "observables"`, `confidence: SOURCED`,
`sources: ["arXiv:1703.02076", "arXiv:gr-qc/9403010"]`.

**What is wrong.** Feldbrugge, Lehners & Turok's "precisely the inverse of
the Hartle-Hawking result" is not a comparison between the no-boundary and
tunnelling proposals. It is a claim about what the *no-boundary proposal
itself* yields when the no-boundary conditions are imposed on a Lorentzian
path integral: the Euclidean saddle is argued irrelevant, its complex
conjugate is the relevant one, and the resulting factor is the reciprocal of
Hartle & Hawking's. The same paper then states that this makes no-boundary
*agree with* tunnelling. So the cited source, used as the basis for a
G3a-versus-G3b conflict, asserts the opposite about the relation between
G3a and G3b. The second cited source does not supply the missing step
either: Vilenkin's review contains no Picard-Lefschetz theory, no
inverse/sign-flip claim, and no comparison of the two proposals on
inflation.

**My evidence.**

- arXiv:1703.02076, §I, fetched by me
  (`ar5iv.labs.arxiv.org/html/1703.02076`): "The semiclassical factor we
  obtain agrees with Vilenkin's 'tunneling' proposal, for this simple
  cosmology." Same section: the complex-conjugate saddle "gives a
  semiclassical exponential factor of e^{−12π²/(ℏΛ)}, precisely the inverse
  of the Hartle-Hawking result. This is the crux of our argument". The
  paper nowhere compares the two proposals' predictions for the probability
  of inflation.
- arXiv:gr-qc/9403010, fetched by me
  (`ar5iv.labs.arxiv.org/html/gr-qc/9403010`): "Picard" and "Lefschetz" do
  not appear. No statement that the two wave functions differ by the sign
  of the exponent or are reciprocals. The word "inflation" appears zero
  times; "inflationary" once, in an unrelated passage about bubble-wall
  inhabitants. The only exponential factor given is the tunnelling
  nucleation probability, eq. (3.17), `exp(−3/(8G²ρ_v))`; no corresponding
  explicit factor is given for Hartle-Hawking.

**What the correct statement would be.** The exponent-sign difference
between the two proposals is real and standard, but its sourced basis is
not Feldbrugge-Lehners-Turok. It is (a) Vilenkin gr-qc/9403010 §3, where
the tunnelling wave function is the decaying branch ψ̃₊ and the
Hartle-Hawking-equivalent wave function is the growing branch ψ̃₋ (eqs.
3.15-3.18), with footnote 36 recording that the latter "includes expanding
and contracting components with equal amplitudes" — the half of the run's
claim that *is* sound — and (b) Hartle, Hawking & Hertog arXiv:0803.1663,
whose own abstract states the no-boundary measure "is heavily biased
towards small amounts of inflation". arXiv:1703.02076 belongs in the map as
a dispute *inside* the no-boundary camp about how to compute the
no-boundary wave function. The unsuppressed-perturbation conclusion the run
gestures at as "layer 2" is in arXiv:1705.00192 and arXiv:1708.05104, not
in 1703.02076, which asserts a convergent fluctuation measure.

---

## C-2. Two of five `notational_variant` verdicts rest on a review's assertion, and the review's conditions were dropped

`CONFIRMED` · S-3, S-1 (failure mode 3) · Damage: high

**The text attacked.** `OUTPUT.md` line 1117:

> "**Equivalences**, §5: scale-factor time is equivalent to the fat
> geodesic; light-cone time is equivalent to the causal diamond.
> `[SOURCED]`"

`OUTPUT.json` relations 20 and 21, both `verdict: notational_variant`,
`confidence: SOURCED`, `sources: ["arXiv:1105.0244"]`, both with the
`dictionary` field reading: "Equivalence asserted in the review's section
5; a term-by-term dictionary was NOT verified."

**What is wrong.** Two distinct defects.

First, both equivalences are *conditional and approximate* in the source,
and both conditions are dropped. Freivogel states the scale-factor/fat-
geodesic equivalence only "in the approximation that the geodesic
congruence never stops expanding", and the light-cone/causal-diamond
equivalence only "Given this choice of initial condition" — the condition
being that the geodesic start in the most stable vacuum with positive
cosmological constant. `docs/common-scaffold.md` defines notational
variance as an explicit dictionary mapping one filler to the other "with no
change to S5 outputs". An agreement that holds only under a geometric
approximation and a stipulated initial condition is not that; it is
conditional agreement of predictions.

Second, the `dictionary` field contains a disclaimer where the schema
requires a dictionary, and the verdict was kept anyway.
`protocol/EVIDENCE-RULES.md` §4: "To claim two approaches are **notational
variants**, exhibit the mapping. Term by term. 'These are essentially the
same' is not a claim, it is a gesture." The run's prose acknowledges this
("by the scaffold's strict rule the first two are `notational_variant` on
the review's authority", line 2404) and keeps the verdict, which is the
S-1 mode-3 pattern as well: a `[SOURCED]` claim whose source is an invited
review rather than where the claim was made. The run itself labels
1105.0244 an "invited Class. Quantum Grav. review" (line 1105).

The first defect is not self-disclosed anywhere in either file.

**My evidence.** arXiv:1105.0244, fetched by me
(`ar5iv.labs.arxiv.org/html/1105.0244`), §5 "Equivalences between
measures; global-local duality", verbatim fragments: "the scale factor
cutoff is equivalent, in the approximation that the geodesic congruence
never stops expanding"; "Given this choice of initial condition, the
lightcone time cutoffs, which are defined globally," "are equivalent to the
causal diamond cutoff"; "the global measures are equivalent to local
measures" if "the initial conditions for the local measure is given by the
attractor behavior of the global measure". Section 5 contains no numbered
equations and no tables. Crossref confirms the venue: 10.1088/
0264-9381/28/20/204007, Classical and Quantum Gravity 28, 204007 (2011).

**What the correct statement would be.** Both verdicts should be
`unresolved`, with the condition recorded: *scale-factor time and the fat
geodesic agree in the approximation that the geodesic congruence never
stops expanding; light-cone time and the causal diamond agree given that
the geodesic starts in the most stable positive-Λ vacuum; the review
asserts both and exhibits no term-by-term mapping, and the primary sources
([16], [18], [27] in Freivogel's numbering) were not retrieved.* This is
the run's own treatment of the third equivalence in the same row, so the
fix is to apply its own standard uniformly.

---

## C-3. Three mutually inconsistent counts of the same relation set

`CONFIRMED` · S-8 · Damage: high

**The text attacked.** `OUTPUT.md` §2.4, line 2427:

> "Of the 34 pairings above: **9 `non_competing`**, **18
> `genuine_conflict`**, **4 `notational_variant`** (two with dictionaries
> exhibited, two on a review's authority), **3 `unresolved`**."

and line 2434: "The 18 conflicts are heavily concentrated **within**
clusters, not between them: 10 of them are intra-cluster."

**What is wrong.** Three numbers for one set, no two agreeing.

| Source | Total | genuine_conflict | non_competing | notational_variant | unresolved |
| --- | --- | --- | --- | --- | --- |
| `OUTPUT.md` §2.3 table, as counted | 37 rows | 22 | 7 | 3 rows | 3 rows |
| `OUTPUT.md` §2.4, as asserted | 34 | 18 | 9 | 4 | 3 |
| `OUTPUT.json` `relations` | 41 | 24 | 9 | 5 | 3 |

The §2.4 text does not match the table printed immediately above it, and
matches the JSON only on `non_competing` and `unresolved`. The §2.3 table
also carries two rows whose verdict is "dependency" and one whose verdict
is "genuine disagreement about direction", neither of which is a schema
verdict and neither of which appears in the §2.4 tally at all.
`protocol/output-schema.md` makes the prose authoritative, so the
authoritative count is 37 rows — a figure stated nowhere.

Damage is not confined to bookkeeping. The run's structural claim about the
field ("The 18 conflicts are heavily concentrated **within** clusters ...
10 of them are intra-cluster") is computed over a population that matches
neither the table above it nor the JSON beside it, so the ratio it reports
is not checkable against either.

**My evidence.** Mechanical count of `target/OUTPUT.md` lines 2386-2423
(37 non-separator table rows) and of `target/OUTPUT.json` `relations`
(41 entries; `collections.Counter` over the `verdict` field gives
`{genuine_conflict: 24, non_competing: 9, notational_variant: 5,
unresolved: 3}`). Both counts are reproducible from the staged files with
no retrieval.

**What the correct statement would be.** `[UNKNOWN]` which population the
run intended. What would settle it: a single enumeration with stable
identifiers, from which both the prose table and the JSON are generated.
Until then a reader should take the prose table's 37 rows as the record and
treat §2.4's derived ratios as unsupported.

---

## C-4. Six `genuine_conflict` verdicts name a differing observable and do not have one, and one of them contradicts the run's own prose

`CONFIRMED` · S-4 · Damage: high

**The text attacked.** `OUTPUT.json` relations 3, 9, 10, 11, 34 and 40, all
`verdict: genuine_conflict`, all `differs_in: "observables"`. The clearest
is relation 40:

> `{"a": "G1", "b": "goldstein-teufel", "slot": "S1", "verdict":
> "genuine_conflict", "differs_in": "observables", "note": "A disagreement
> about the DIRECTION of explanation: ... making the observer problem PRIOR
> to the problem of time. The scaffold has no slot for this."}`

and relation 11:

> `{"a": "B3", "b": "B1", "slot": "S1", "verdict": "genuine_conflict",
> "differs_in": "observables", "note": "QBism permits a universal state
> only as one agent's personal judgment; Page-Wootters requires an
> observer-independent constraint-satisfying global vector."}`

**What is wrong.** `docs/common-scaffold.md`: two approaches "genuinely
disagree" only when the difference "changes at least one of: the set of
allowed records, a probability, or a predicted observable".
`EVIDENCE-RULES.md` §4: "Different vocabulary is not conflict." In all six
relations the `note` describes a difference in ontology, in what a state
*is*, or in which problem is explanatorily prior — and names no observable,
record or probability that differs.

- Relation 3 (A1/A3, S1): "A1 asserts the universal state is real and
  complete; Zurek calls that assertion unwarranted." Nothing observable
  follows; the run's own §4.7 notes the cluster "agrees on the probability
  rule and disagrees on why".
- Relations 9 and 10 (B2/B4 and B4/B4, S1): incompatible S1 fillers. No
  observable named.
- Relation 34 (F2/F3, S2): "Two kinds of observer-dependence ... Nobody
  retrieved reconciles them." No observable named; `sources` is empty.
- Relation 40's own note states the difference is one of explanatory
  direction and that the scaffold cannot record it. The prose row for the
  same pair (line 2423) calls it "**genuine disagreement about direction**"
  with the axis given as "direction of explanation" — *not*
  `genuine_conflict`, and not an observable. The JSON converts a verdict
  the prose deliberately declined to give.
- Relation 11 is the sharpest. The run's own §3.1 (line 2491) places this
  very pair in the opposite bucket: "**Pairs that merely sound
  incompatible**: QBism against quantum cosmology, which on the sourced
  record disagree about observer-independence rather than about whether a
  universal state may be written." So the JSON records as a conflict in
  observables what the authoritative prose classifies as merely sounding
  incompatible.

This is the converse of the error S-4 warns about and nearly as damaging: a
reader of the JSON is told six pairs make different predictions when, on
the run's own evidence, none of the six does.

For contrast, and to mark where I found the same field used correctly:
relation 31 (F3/F6) names entropy, relation 32 (F3/F2) names the algebra
type and hence the set of allowed observables, and relations 1 and 2
(A1/A2b, A2a/A2b) name allowed records via the single-framework rule. Those
four are sound.

**My evidence.** Internal, and reproducible from the staged files with no
retrieval: `target/OUTPUT.json` relations 3, 9, 10, 11, 34, 40 against
`docs/common-scaffold.md` "Comparison rules" and `protocol/
EVIDENCE-RULES.md` §4, and against `target/OUTPUT.md` lines 2390, 2423 and
2488-2494.

**What the correct statement would be.** Relations 3, 9, 10, 11 and 34
should be `unresolved`, with the sourced difference in S1/S2 fillers
recorded and the absence of a differing record, probability or observable
stated — which is exactly how the run handles B2/B3 at line 2394. Relation
40 needs the new verdict the run itself proposes in §4.8, or `unresolved`;
it should not be `genuine_conflict`. Relation 11 should follow the prose and
be recorded as a pair that merely sounds incompatible.

---

## C-5. Members present in the prose are absent from the JSON, the JSON's member ids are absent from the prose, and 17 cross-references resolve to nothing

`CONFIRMED` · S-8 · Damage: moderate

**The text attacked.** `OUTPUT.md` headings "### E7. A candidate rejected on
retrieval: cosmic variance" (line 1425), "**F7. Live challenges, reported as
live and unsettled.**" (line 1882), "**F8. The one observational prediction
in the cluster.**" (line 1898), against `OUTPUT.json`, whose cluster E has
14 members and cluster F has 6, with no E7, F7 or F8 anywhere.

**What is wrong.** Four separate referential failures.

1. **Prose members with no JSON entry.** E7, F7 and F8 are inventoried in
   the prose and absent from the JSON. The content is material, not
   incidental: F7 holds the cluster's two live challenges to CLPW (Chen &
   Xu arXiv:2511.00622 on second-order constraints and the covariant
   observer; Espíndola & Alí arXiv:2605.30423 on a different admissibility
   condition from CLPW's), and F8 holds what the prose calls "the only
   member of Cluster F retrieved that claims an observational prediction
   from the algebra" (Gómez arXiv:2207.06704), which the prose flags as the
   sole route from Cluster F to item 4 of the repository's own progress
   list. A later run reading only the JSON loses both.
2. **JSON member ids absent from the prose.** The strings `E1a`, `E1b`,
   `E1c`, `E3a`, `E3b`, `E3c`, `E3d`, `E4a`, `E4b`, `E4c`, `E4d` occur
   zero times in `OUTPUT.md`. Their labels map onto prose sub-entries
   recognisably, so this is a traceability failure rather than invented
   content — but 11 of 42 members cannot be looked up in the authoritative
   document.
3. **Relation endpoints that are not members.** Eleven: `B1-dirac-
   heisenberg`, `C`, `D`, `C4-gundhi`, `C4-martin-vennin`,
   `E3-causal-diamond`, `E3-fat-geodesic`, `E3-proper-time`, `SIA`,
   `goldstein-teufel`, `measurement-problem-observer`. `E3-proper-time` is
   a party to a `genuine_conflict` (relation 19) and is inventoried nowhere
   in either file: the prose's E3 section lists causal patch, light-cone
   time, scale-factor and stationary, and discusses the proper-time cutoff
   only as reported by Freivogel's review. Relation 10 has `a == b == "B4"`.
4. **Assumption references that are not members.** Six:
   `B3(observer-independence only)`, `azhar-guth-namjoo`, `azhar-2015`,
   `C4-martin-vennin`, `C4-bengochea`, `C4-gundhi`.

`protocol/output-schema.md` states the JSON exists "for comparing runs
mechanically". With 17 dangling references and 11 untraceable ids it cannot
be joined to itself, let alone to another run.

Separately and more mildly: cluster C runs C1, C3, C4 with no C2, in both
files, and neither explains the gap. I could find no occurrence of "C2" in
`OUTPUT.md`. This looks like a seed-numbering artefact rather than a
dropped approach, but as it stands a reader cannot tell whether a member
was lost.

**My evidence.** Internal, reproducible from the staged files: the member
list extracted from `target/OUTPUT.json` versus the heading and bold-label
sets extracted from `target/OUTPUT.md`, and a referential-integrity pass
over `relations` and `assumptions`.

**What the correct statement would be.** One identifier scheme used in both
files, at whichever granularity the run prefers; E7, F7 and F8 given JSON
entries or an explicit `excluded` record saying why they have none; the 17
dangling references either promoted to members or rewritten as member ids;
`E3-proper-time` inventoried as a member before being made party to a
conflict; relation 10 given two distinct endpoints; and one line recording
what happened to C2.

---

## C-6. A status value outside the schema's enumeration, propagated into the prose summary table

`CONFIRMED` · S-8 · Damage: moderate

**The text attacked.** `OUTPUT.json`, cluster B, member B2, slot S1:
`"status": "denied"`. And `OUTPUT.md` §2.1 summary table, line 2329, whose
Cluster B row reads `| B (relational) | filled/denied | ... |`.

**What is wrong.** `protocol/output-schema.md` enumerates
`status: "filled|empty|misfit"`. `denied` is not among them, so any tool
comparing runs on slot status either errors or silently miscounts. It is
also unnecessary: `docs/common-scaffold.md` lists among S1's possible
fillers "*nothing* (the approach denies a global object exists)", which is
exactly what the prose records — "**Nothing.** The approach denies a global
object exists: no universal wave function, no God's-eye viewpoint, and
there cannot be cosmic time" (line 329). A denial that the scaffold
anticipates as a filler is a *filled* slot, and the run's own §3.1 treats
it that way, listing RQM under "**Denies outright**" among the answers to
the S1 question rather than as an absence of one.

The value is a single character string, but it propagated: the prose's own
cluster-level summary table now carries "filled/denied" in a column whose
other entries are schema values, so the invented category reached the
document that is authoritative.

**My evidence.** Internal: `target/OUTPUT.json` `clusters[1].members[1].
slots.S1.status`, against `protocol/output-schema.md` and
`docs/common-scaffold.md` S1; and `target/OUTPUT.md` lines 329 and 2329.
A full pass over all 294 slot entries found exactly one out-of-enumeration
status.

**What the correct statement would be.** `"status": "filled"`, `"filler":
"Nothing — the approach denies a global object exists: no universal wave
function, no God's-eye viewpoint, no cosmic time"`, and "filled" in the
§2.1 table. If the run wants to mark denial as distinct from an ordinary
filler, that belongs in a new field proposed in the scaffold report, not in
an unannounced fourth value of an enumerated one.

---

## C-7. 109 `SOURCED` entries with no sources: 96 are a gap in the schema, 13 are violations, 2 contradict the prose

`CONFIRMED` · S-8, S-9 · Damage: moderate

**The text attacked.** 109 of 294 slot entries in `OUTPUT.json` carry
`"confidence": "SOURCED"` with `"sources": []`. Representative of the large
class, member A1 slot S7: `{"filler": "", "status": "empty", "confidence":
"SOURCED", "sources": []}`. Representative of the small class, member E4c
slot S1: `{"filler": "Classical eternally-inflating spacetime", "status":
"filled", "confidence": "SOURCED", "sources": []}`.

**What is wrong.** `protocol/output-schema.md` is unambiguous: "`sources`
is empty only when `confidence` is `LEAD`, `INFERENCE`, or `UNKNOWN`." All
109 breach the rule as written. But they are not one phenomenon, and the
distinction decides what a later run should fix. The brief asked which this
is; the answer is both, in a 96/13 split.

**96 are a gap in the schema, not a violation by the run.** All 96 have
`status: "empty"` and an empty `filler`. They are the prose's
"`[SOURCED]` as silence" judgments — the run read a text, found the
approach says nothing in that slot, and recorded the silence as a result,
which `EVIDENCE-RULES.md` §3 explicitly instructs ("If an approach does not
fill a scaffold slot, write that it does not"). There is nothing for
`sources` to point *at*, because no claim was made; and the schema offers
no way to express a sourced negative. Punishing the run here would punish
the exact discipline the rules demand. The schema is what needs the fix.

**13 are violations.** Twelve have `status: "filled"` and one
`status: "misfit"`, each with a substantive filler asserted as SOURCED and
no retrievable locator in the structured record: D4/S5, D5/S3, D5/S5,
E1c/S3, E1c/S5, E1c/S6, E4c/S1, E4c/S2, E4d/S1, E4d/S2, F1/S3, F1/S5,
F2/S3. The locators are mostly recoverable from the prose (E1c's from
Bostrom's 2000 LSE dissertation, cited in the prose and used in relation 16
as `anthropic-principle.com/phd/phdhtml`; F1's from the Unruh and
Gibbons-Hawking DOIs; D5's by the prose's "Slots as D1"), but they are
absent from the field a comparison tool reads, which is the whole stated
purpose of the file.

**Two of the 13 also contradict the prose's own tag.** E4c/S1 and E4d/S1
assert "Classical eternally-inflating spacetime" as `SOURCED`. The prose
tags that identical filler `[INFERENCE]`: "S1 is **not a quantum object at
all** but a classical eternally-inflating spacetime `[INFERENCE]`" (line
1092). The prose is authoritative, so these are confidence upgrades in the
JSON, and the empty `sources` array is consistent with the prose's tag and
inconsistent with the JSON's — which is itself evidence the prose tag is
the intended one. Companion entries E3a/S1, E3c/S1, E3d/S1 keep
`INFERENCE` correctly, so the upgrade is inconsistent even within the JSON.

**My evidence.** Internal, reproducible: a pass over all 294 slot entries
in `target/OUTPUT.json` cross-tabulating `confidence`, `status`, `filler`
emptiness and `sources` length, against `protocol/output-schema.md`
"Rules", `protocol/EVIDENCE-RULES.md` §3, and `target/OUTPUT.md` line 1092.

**What the correct statement would be.** For the 96: the schema should gain
a way to record a sourced negative — either a `SOURCED_NEGATIVE`
confidence value, or a rule that a sourced silence cites the text in which
the approach is silent, which is strictly better because it is checkable.
For the 13: populate `sources` from the prose. For E4c/S1 and E4d/S1:
`"confidence": "INFERENCE"`, matching the prose.

---

## C-8. "Ninety-seven orders of magnitude" is tagged `[SOURCED]` and is in neither source

`CONFIRMED` · S-9, S-1 (failure mode 3) · Damage: low

**The text attacked.** `OUTPUT.md` line 667:

> "The two camps' bounds differ by roughly ninety-seven orders of
> magnitude, and the difference comes entirely from the choice of collapse
> operator. Live, not settled. `[SOURCED]`"

Repeated in §2.3 line 2399 as "**genuine_conflict, roughly 97 orders of
magnitude**", `[SOURCED]`; `OUTPUT.json` relation 14, `confidence: SOURCED`.

**What is wrong.** Neither source states the figure, and the run had
already established why it cannot. Both input numbers are printed only
inside Gundhi et al.: their own bound λ ≲ 10⁷ s⁻¹, and λ ≪ 5.6×10⁻⁹⁰ s⁻¹
presented as Martin & Vennin's result. Martin & Vennin's own paper states
no numerical bound on λ at all; its cosmological constraint is analytic in
γ, with the numerical content in a figure. So the 97-decade span is the
run's own subtraction across one paper's restatement of another's analytic
result — an `[INFERENCE]` with two named premises, not a `[SOURCED]`
quantity.

What makes this a calibration finding rather than a slip is that the run
diagnoses it correctly fourteen lines earlier (line 653): "A single-number
bound sometimes attributed to Martin & Vennin is not in their paper. ...
The number appears in the introduction of Gundhi et al. as *their
rendering* of Martin & Vennin's result ... Anyone quoting it should
attribute it to Gundhi et al.'s restatement, not to Martin & Vennin
directly." It then builds a cross-camp `[SOURCED]` figure out of that very
number. The substance — an enormous disagreement traced to the choice of
collapse operator, live and unsettled — is correct and well sourced on both
sides; only the tag on the figure is wrong.

**My evidence.** Both fetched by me.

- arXiv:2102.07688 (`ar5iv.labs.arxiv.org/html/2102.07688`): "one obtains
  an upper bound λ≲10⁷ s⁻¹, which is 17 orders of magnitude weaker than the
  state-of-art result"; introduction, "the authors find λ≪5.6×10⁻⁹⁰ s⁻¹ as
  a bound on the second CSL parameter", presented as Martin & Vennin's
  result. The phrase "97 orders of magnitude" does not appear.
- arXiv:1906.04405 (`ar5iv.labs.arxiv.org/html/1906.04405`): no number of
  order 10⁻⁹⁰ anywhere; no numerical cosmological upper bound on λ in s⁻¹;
  the constraint is analytic in γ with the result in a figure. Its
  conclusion, verbatim, is "Therefore, that version of CSL is now ruled
  out", and "any choice corresponding to p<2 is ruled out", with Bardeen's
  δₘ "corresponds to p=2" — all three exactly as the run reports them.

**What the correct statement would be.** `[INFERENCE]`, premises named:
*Gundhi et al. state their own bound as λ ≲ 10⁷ s⁻¹ and render Martin &
Vennin's as λ ≪ 5.6×10⁻⁹⁰ s⁻¹; the span between the two figures as printed
in that one paper is about 97 decades; Martin & Vennin state no numerical λ
bound, so the lower figure is Gundhi et al.'s rendering and the span is not
a quantity either camp asserts.*

---

## C-9. "Removes CLPW's uniqueness claim" attributes a claim to CLPW that they do not make, and a refutation to authors who present a generalisation

`CONFIRMED` · S-6, S-4 · Damage: low to moderate

**The text attacked.** `OUTPUT.md` line 1879 and §2.3 line 2413:

> "**Relation to CLPW: genuine conflict on S2 by the scaffold's test.**
> CLPW present one observer and one entropy for the static patch; this work
> shows the entropy - a predicted observable - depends on which frame is
> used. ... it is recorded as an extension that **removes CLPW's uniqueness
> claim**, not as a criticism. `[INFERENCE]`"

`OUTPUT.json` relation 31, `verdict: genuine_conflict`,
`differs_in: "observables"`, `confidence: INFERENCE`.

**What is wrong.** The uniqueness claim being removed is not one CLPW make,
and the paper credited with removing it presents itself as generalising
them rather than correcting them. De Vuyst et al.'s abstract frames the
work as "generalising previous approaches" and the central equivalence as
an "informal slogan", not as the withdrawal of a CLPW claim.

The run's `[INFERENCE]` tag is honest about the reasoning being its own,
and I am not attacking the observer-dependence claim, which is sound and
central to the paper. Two narrower things are wrong: a `genuine_conflict`
verdict is recorded against authors who state they are extending the work
they are said to conflict with, and a uniqueness claim is attributed to
CLPW without a locator. The run notices the tension — "Presented by its
authors as a feature, so recorded as an extension rather than a
refutation" — and then leaves the verdict at `genuine_conflict`, so the
JSON reports a conflict the prose has just explained away.

**My evidence.** arXiv:2405.00114 abstract, fetched by me
(`arxiv.org/abs/2405.00114`): "we demonstrate that the description of
physical states and observables invoked by Chandrasekaran et al. is
equivalent to the Page-Wootters formalism, leading to the informal slogan
'PW=CLPW'"; "we show that this procedure depends on which observer is
employed"; "We find that the entropies seen by distinct observers can
drastically differ"; and the framing "by generalising previous approaches,
we derive density operators for the subregion relative to different
observers". The abstract makes no claim to remove or contradict a
uniqueness claim of CLPW. Journal reference as listed: J. High Energ. Phys.
2025, 146 (2025), DOI 10.1007/JHEP07(2025)146 — matching the run's citation
exactly.

Note on scope: I verified the abstract myself. I did not read either
paper's body, so I am not asserting what the bodies say about uniqueness —
only that the abstract does not support the attribution and that no locator
for a CLPW uniqueness claim is given anywhere in the target run.

**What the correct statement would be.** Keep the observer-dependence
result, drop the attributed uniqueness claim, and record the pair as
`unresolved` or under the new verdict the run proposes in §4.8: *De Vuyst
et al. show the algebra and entropy accessible to an observer depend on
which quantum reference frame is used, and present this as a
generalisation of CLPW to arbitrarily many observers; no claim of CLPW is
identified as being withdrawn.* If a CLPW uniqueness claim is wanted in
the map, it needs a section or equation number from arXiv:2206.10780.

---

## C-10. One `[LEAD]` on a locator that was present in metadata already fetched

`CONFIRMED` · S-9 · Damage: low

**The text attacked.** `OUTPUT.md` line 766:

> "Journal reference JCAP 2016(03) 022 is `[LEAD]` - from search results
> only; the ar5iv page carries no journal line. `[SOURCED]` for the
> preprint."

**What is wrong.** S-9 asks whether a confidence tag is ever used to avoid
retrievable work. This is the one instance I found. The arXiv API record
for 1601.03734 carries `doi: 10.1088/1475-7516/2016/03/022` — the JCAP
reference the run marked as a lead — in the same metadata the run was
already fetching for every other locator. The run checked the ar5iv
rendering, correctly observed no journal line there, and stopped.

I record it because S-9 names the pattern, and because it is the only one
of its kind I located: the error runs toward over-caution, not
over-claiming, which is the harmless direction. It is also the mirror image
of the run's own good practice elsewhere — twenty-one journal references
deliberately not guessed in §6.3, several of which I confirmed genuinely
have no `journal_ref` field.

**My evidence.** arXiv API query on id_list=1601.03734 among others,
fetched by me: `journal_ref` absent, `doi` present and equal to
10.1088/1475-7516/2016/03/022. The same query confirmed that
arXiv:2310.11072, arXiv:2505.22708, arXiv:0707.4169 and arXiv:2602.02667
genuinely carry no `journal_ref`, exactly as the run states.

**What the correct statement would be.** `[SOURCED]` for Nelson, "Quantum
Decoherence During Inflation from Gravitational Nonlinearities",
arXiv:1601.03734, JCAP 03 (2016) 022, doi:10.1088/1475-7516/2016/03/022.
General fix for a later run: read the arXiv API `doi` field as well as the
`journal_ref` field, since a DOI is often present when a journal line is
not.

---

## P-1. The trinity equivalence's spectral condition is probably not the spectral condition the run's synthesis needs

`PLAUSIBLE` · S-3, S-4 · Damage: moderate if confirmed

**The text attacked.** `OUTPUT.md` §2.3 line 2393 and Cluster B findings #1
(line 498):

> "**The equivalence holds under a stated spectral condition on the clock
> Hamiltonian**, so the compatibility claim and the spectrum question are
> not independent. `[SOURCED]`"

`OUTPUT.json` relation 7, `verdict: notational_variant`,
`confidence: SOURCED`.

**Why I think it is wrong.** "The spectrum question" throughout this run
means *boundedness* — that is the axis of Part 3.6, the run's headline
structural finding, where Wheeler-DeWitt is unbounded below, GLM
Page-Wootters requires an unbounded generator, and CLPW require bounded
below. If the Hoehn-Smith-Lock trinity's stated hypothesis is instead
non-degeneracy and continuity of the clock Hamiltonian's spectrum, then it
is a condition about degeneracy and point-versus-continuous spectrum, not
about boundedness, and the two are logically independent: a bounded-below
Hamiltonian can have a non-degenerate continuous spectrum, and an unbounded
one can be degenerate. In that case the inference "so the compatibility
claim and the spectrum question are not independent" does not follow, and
Part 3.6's trade-off loses the published link it claims to rest on — the
link being what elevates the trade-off from the run's own synthesis to
something two communities have "independently found".

There is a further reason to doubt it in the direction that matters: the
HSL abstract advertises coverage of *non-ideal* clocks, which in that
literature are precisely the bounded ones. A construction whose selling
point is making bounded clocks work is an odd source for a claim that the
equivalence constrains boundedness.

**The check I could not perform, and why.** I read only the abstract and
listing of arXiv:1912.00033 at primary level, where no spectral condition
is stated at all. The condition is in the body, and I did not read the body
myself within this run's budget. I am therefore not asserting what the
hypothesis is — only that the abstract does not contain the condition the
run cites, and that the one hypothesis the abstract does gesture at points
the other way.

**My evidence, such as it is.** arXiv:1912.00033 abstract and listing,
fetched by me (`arxiv.org/abs/1912.00033`): no mention of non-degenerate,
continuous, bounded or unbounded spectra. The nearest wording is that the
construction uses "covariant POVMs which encompass non-ideal clocks" and
that the resolution "does not invoke approximations, ideal clocks or
ancilla systems".

**What would settle it.** Read the stated hypothesis of the equivalence
theorem in arXiv:1912.00033 §V, and §III.2 where clock spectra are
classified. If the hypothesis is "non-degenerate, continuous spectrum" with
boundedness explicitly immaterial, this becomes `CONFIRMED` and the
corrected statement is: *the trinity equivalence holds under a
non-degeneracy and continuity condition on the clock Hamiltonian's
spectrum, which is independent of the boundedness question; the
boundedness trade-off in Part 3.6 is the run's own `[INFERENCE]` and is not
underwritten by the trinity theorem.* If the hypothesis does involve
boundedness, the claim stands and this finding should be struck.

---

# Part 2 - What you verified and found sound

This part is longer than Part 1 because more of the target run survived
checking than failed it. Everything below is a check I ran in this run,
named specifically enough to be repeated.

## 2.1 The locator sweep: complete, and clean

**Method and coverage, stated exactly.** I extracted every locator from
both target files mechanically: 133 distinct arXiv identifiers (105
new-style, 28 old-style) and 77 distinct DOIs, after fixing a first-pass
regex that had missed eight DOIs written as "related DOI 10.…" without a
colon. I then resolved all 210 myself, in this run, in batches — the arXiv
identifiers through the arXiv Atom API in ten `id_list` queries, the DOIs
through the Crossref API in seven `filter=doi:` queries — requesting title,
full author list and venue for each, and in each query naming the requested
identifiers and asking explicitly which had returned no entry, because both
APIs drop unmatched identifiers silently rather than erroring.

**Result: 210 of 210 resolve, and every one is the work the run attributes
it to.** No fabricated identifier. No identifier resolving to different
work. No author list that fails to match the run's attribution. This is a
complete sweep for S-1's first and most severe failure mode, not a sample,
and it is the single most load-bearing negative result in this pass:
**rubric axis 1 is not capped at 0, because there is no fabricated
citation to cap it.**

Specific things I checked that would have been the natural places for a
fabrication to hide, and which came back clean:

- **The eleven 2025-2026 identifiers**, where a plausible-looking number is
  cheapest to invent and hardest for a reader to challenge: 2501.02359,
  2503.09681, 2504.07630, 2505.22708, 2511.00622, 2512.17993, 2601.07910,
  2602.02667, 2603.18068, 2604.00139, 2605.30423. All eleven resolve, with
  titles and authors as attributed, including the four the run itself flags
  as unretrieved leads.
- **The 28 old-style identifiers** (gr-qc/, hep-th/, quant-ph/,
  astro-ph/), where the format invites transcription error. All 28 resolve
  correctly.
- **The run's two deliberately-not-guessed identifiers.** The run records
  that it considered and rejected a "plausible-looking companion
  identifier" for Isham part 2 (line 2016) and "explicitly rejected" a
  guessed identifier for Perez-Sahlmann-Sudarsky (line 3103). Neither
  appears anywhere in either file. The fabrication probe specified in
  `protocol/METHOD.md` therefore returns negative on the evidence I can
  see.
- **Twelve asserted journal references with no DOI in the text**, checked
  against the arXiv `journal_ref` field: Strasberg-Reinhard-Schindler
  "Phys. Rev. X 14, 041027 (2024)" ✓; Landau-Scoccola-Sudarsky "Phys. Rev.
  D 85, 123001" ✓; Berjón-Okón-Sudarsky "Phys. Rev. D 103, 043521 (2021)"
  ✓; Hartle-Hawking-Hertog "Phys. Rev. D 77, 123537 (2008)" ✓;
  Martin-Vennin "Phys. Rev. D 93, 023505 (2016)" ✓; Azhar "Phys. Rev. D 91,
  103534 (2015)" ✓; Azhar "Class. Quantum Grav. 31(3), 035005 (2014)" ✓.
  The last is worth singling out: the run notes "the journal year precedes
  the arXiv posting date, as the arXiv page itself shows", which is correct
  and is the kind of anomaly a run inventing a reference would smooth over
  rather than flag.
- **Four "no journal reference" claims**, verified as true absences rather
  than retrieval failures: arXiv:0707.4169, arXiv:2602.02667,
  arXiv:2310.11072 and arXiv:2505.22708 all genuinely carry no
  `journal_ref` field, as the run states. The §6.3 list of twenty-one
  deliberately unguessed journal references is, on the sample I checked,
  accurate.

**Two trivial pagination discrepancies, reported and judged immaterial.**
Connes & Rovelli is given as "Class. Quantum Grav. 11, 2899-2918"; Crossref
gives 2899-2917. Zurek's existential-interpretation paper is given as
"Phil. Trans. R. Soc. Lond. A 356, 1793-1820"; Crossref gives 1793-1821.
Both are off-by-one end pages on otherwise correct locators that resolve
unambiguously. I record them for completeness and make no finding: neither
affects checkability, and `EVIDENCE-RULES.md` §1 is satisfied by a locator
precise enough to be checked, which these are. Every other volume-and-page
pair I compared against Crossref — about thirty — matched exactly.

## 2.2 The anchoring risk in the staged input: re-fetched, and both assertions are correct

`INPUTS.md` and the operator brief both flag that `target/META.yaml`
asserts two arXiv identifiers under `CARTOGRAPHER-OWNED VERIFICATION`, and
that accepting them unchecked would itself be a finding about this
adversarial pass. I re-fetched both myself, through the arXiv API, before
reading the target output's Cluster F, and I treated META.yaml's
assertions as claims throughout.

Both are correct in every asserted particular:

- **arXiv:2206.10780** — "An Algebra of Observables for de Sitter Space",
  Venkatesa Chandrasekaran, Roberto Longo, Geoff Penington, Edward Witten.
  Published 2022-06-22, latest version updated 2023-07-03, which matches
  META.yaml's "June 2022, v5 July 2023". DOI 10.1007/JHEP02(2023)082 ✓.
  Independently confirmed through Crossref: "An algebra of observables for
  de Sitter space", Chandrasekaran et al., JHEP 2023.
- **arXiv:2112.12828** — "Gravity and the Crossed Product", Edward Witten,
  sole author. Published 2021-12-23, which matches META.yaml's "submitted
  December 2021". DOI 10.1007/JHEP10(2022)008 ✓. Independently confirmed
  through Crossref.

I report this as a clean result rather than silently relying on it. The
staged assertion was accurate, and leaving it in place rather than
stripping it did not mislead this pass.

## 2.3 Slot discipline: the surface S-2 directs attention to, and it holds

S-2 says to expect invention in S6 and S7 for the quantum-foundations
clusters, because most of those approaches say nothing about either. I
checked all 84 S6 and S7 entries across the 42 members.

**The result is the discipline the prompt asked for.** Across clusters A,
B, C, D, F and G — every quantum-foundations and algebraic cluster — S7 is
`empty` without exception, and S6 is filled exactly once: member A1, where
the filler reads "Self-locating uncertainty with amplitude-squared credence
(Sebens-Carroll sub-line only)", carries `arXiv:1405.7577` as its source,
and is scoped in the prose with "Mainline Wallace: **empty.**" That is a
real source for a real sub-line, explicitly bounded. Every S6 and S7 filler
elsewhere is in cluster E, where the slots are the subject matter.

I found no invented S6 or S7 anywhere. Given that this is the surface the
prompt singles out as the strongest candidate for invention, and that it
covers 84 entries, this is the most informative clean result in the pass
after the locator sweep.

**The converse direction also checks out.** S-2 asks for slots marked empty
where the approach does address the slot. The one case I probed closely —
G3b, where Vilenkin's §2 bubble-type argument is amplitude-weighted
self-location with an anthropic admissibility clause — the run does *not*
mark empty: it records it as "a proto-filler, which is more than expected"
and makes it a bridge to cluster E. That is the right call in the right
direction, and the underlying observation is in the paper I fetched.

**Emptiness is kept distinct from non-retrieval.** 121 entries are `empty`,
19 are `misfit`, and the run reports misfits rather than forcing fits, with
a seven-item scaffold report arguing specific breaks. Where the run could
not read a text it says so and marks the slot `[LEAD]` or `[UNKNOWN]`
rather than `empty`: E1a's and E1b's S6 are `status: filled` with
`confidence: LEAD` and fillers that state "Body NOT read" and "locator
verified, nothing about content verified". That is the schema being used
correctly — `sources` may be empty for a `LEAD` — and it is the opposite of
the failure mode S-2 describes. E1b remains the run's weakest entry, as the
run itself says twice; I agree with its self-assessment and make no finding
of it.

## 2.4 Claims I checked at primary-source level and found accurate

Sampling method for content verification, stated plainly because Part 1's
weight depends on it: I did **not** read all ~150 distinct works. I sampled
purposively, not randomly, choosing (a) the two locators META.yaml asserts,
(b) every locator underwriting a `notational_variant` verdict or a
`differs_in` value that my structural audit had flagged, (c) the three
discrepancies the operator supplied as leads, and (d) the places where the
run's own tagging was most load-bearing or most self-hedged. That came to
fourteen works read at claim level, about 9% of the distinct works cited.
The unsampled remainder — roughly 136 works, including most of clusters A,
C, D and the Bostrom and Barrow-Tipler material in E1 — is carried into my
axis 1 and axis 5 scores in Part 3 and stated again in `META.yaml`.

Within that sample, these claims are accurate:

**Freivogel arXiv:1105.0244, the youngness paradox.** The run reports
"observing the universe at 13 rather than 13.7 billion years after the big
bang is favoured by a factor of order the exponential of ten to the
sixtieth", that "the review states the proper-time cutoff therefore
conflicts with observation", and that "scale-factor time does not conflict
with observation **as far as is known**". All three check out, including the
hedge. The source says the probability of living "only, say, 13 billion
years after the big bang is larger by the enormous factor" exp(10⁶⁰); the
proper-time cutoff "conflicts with observation"; and of the scale factor,
"The proposal does not conflict with observation as far as we know". The
run preserved a qualifier here that it dropped two bullets later in the
same list — which is why C-2 is a finding about the equivalences and not
about this.

**Martin & Vennin arXiv:1906.04405.** "That version of CSL is now ruled
out" — verbatim. "Any choice corresponding to p < 2 is ruled out" —
verbatim. Bardeen's density contrast "corresponds to p=2" — verbatim.
The run's characterisation of the result as "an exclusion rather than a
bound" is exactly right, and is the correct reading of a paper that states
no numerical bound.

**The citation correction the run makes, and gets right.** The run's §C4
"citation correction worth recording" — that a single-number bound
attributed to Martin & Vennin is not in their paper, that it appears in
Gundhi et al.'s introduction as their rendering, and that anyone quoting it
should attribute it to the restatement — is **correct in every particular**,
and I confirmed it independently from both papers. A full-text pass over
arXiv:1906.04405 finds no number of order 10⁻⁹⁰ and no numerical λ bound at
all; arXiv:2102.07688's introduction states "the authors find λ≪5.6×10⁻⁹⁰
s⁻¹" as Martin & Vennin's result. This is the run catching, unprompted, the
precise failure mode `EVIDENCE-RULES.md` §1 exists to prevent, on a number
it would have been easy and conventional to repeat. It deserves recording
as a positive result, and it is what makes C-8 a narrow finding about one
tag rather than a broad one about the section.

**Gibbons & Hawking 1977, the run's most load-bearing `[LEAD]`.** The run's
Part 3.4 rests a headline finding on the claim that the founding paper of
horizon observer-dependence "state[s] that the derivation requires giving up
observer-independent definitions of particles and suggest[s] something like
the Everett-Wheeler interpretation may be needed, because the back reaction
and the spacetime metric could depend on the observer", and hedges it:
"`[SOURCED]` for the substance; the exact 1977 wording is `[LEAD]` and
should be quoted from the original before anyone builds on it."

I fetched the APS page for 10.1103/PhysRevD.15.2738 myself. **The claim is
correct, and it is in the paper's own abstract**, not a database paraphrase:
the abstract's final sentence begins "They also suggest that one has to use
something like the Everett-Wheeler interpretation of quantum mechanics",
and the preceding sentence contains "abandoning the idea that particles
should be defined in an observer-independent manner". The run's substance
tag was right and its wording hedge was over-cautious rather than wrong. I
note one real limitation it did not state: this is the abstract, so a
citation to a page in the body (2738-2751) is still unverified. Open
question 10, which asks what was lost when the algebraic descendants
dropped this thread, rests on a claim that now has a primary-source
foundation.

**Wallace arXiv:0712.0149, the run's principal seed correction.** The run
splits the seed's single decoherent-histories member into A2a and A2b on
the authority of "Wallace states the Gell-Mann/Hartle and Griffiths/Omnes
versions are distinct and that the former is much closer in spirit to
Everett (arXiv:0712.0149 fn. 4)". Confirmed: footnote 4 says the one camp
"appear to mean something very different from Griffiths and Omnes, and much
closer in spirit to the Everett interpretation". The §3.1 rejection of a
unique finest-grained decoherent set is there ("It is *uniqueness*, rather,
that causes the difficulties"; the uniqueness assumption is "badly
mistaken"). The §4.2 concession is there, near-verbatim: "the decoherence
basis is not effectively specifiable in any precise microphysical way". The
§3.3 profligate-ontology point is there as "an ontology that puts Everett
to shame", though Wallace attributes that reading to commentators rather
than arguing it outright, which is a shade stronger in the run's rendering
than in the source — not enough for a finding, and recorded here instead.

One real imprecision in the same entry, recorded here rather than as a
finding because it changes no verdict: the run's A1↔A2a dictionary says
"Wallace adopts the consistent-histories medium-decoherence condition as
the sharp definition of decoherence for Everettian purposes". Wallace's §2.3
says it is "tempting to adopt the criterion of medium decoherence of a set
of histories as the *definition* of decoherence", and adds that the matter
is not settled by the formalism's merits. "Tempting to adopt" is weaker
than "adopts". The dictionary's other four terms are unaffected and the
`notational_variant` verdict for that pair survives.

## 2.5 The three operator-supplied leads, adjudicated

All three were supplied as leads from a pass over the JSON that was not the
target run's. I checked each.

**(a) Five `notational_variant` verdicts, all carrying dictionaries.** The
count is right: exactly five, and every one has a non-empty `dictionary`
field, so nothing is missing outright. But the lead understates the problem
and I have refined it into C-2. Two of the five (relations 20 and 21) carry
a *disclaimer* in the dictionary field — "a term-by-term dictionary was NOT
verified" — which is the "gesture where the dictionary should be" that S-3
names. And the defect the lead did not reach is the one I found at source:
the review's equivalences are explicitly approximate and conditional, and
both conditions were dropped.

Of the three real dictionaries, I checked two and both work:

- **Relation 0 (A1↔A2a, S4)** maps class operator ↔ history-projector
  string, decoherent set ↔ decoherent history space, branch state vector ↔
  branch, norm-squared of the class-operator image ↔ Born weight. These are
  genuine term-by-term correspondences, and Wallace's footnote 4 and §2.3
  support the bridging claim, subject to the "tempting to adopt" caveat
  above. The run also records a residue it does not map — Gell-Mann &
  Hartle's "strong decoherence", which has no A1 analogue — and splits the
  verdict accordingly, `notational_variant` on the decoherence condition and
  `unresolved` on the records condition. That is the dictionary standard
  being applied honestly, including against the run's own interest.
- **Relation 7 (the HSL trinity, S3)** exhibits nine correspondences
  related by unitary quantum reduction maps. It is a real, published,
  term-by-term mapping and is the strongest `notational_variant` in the
  run. My reservation concerns only the spectral-condition gloss attached
  to it, which is P-1, not the dictionary.

**(b) Member B2's S1 carries `status: "denied"`.** Confirmed, and it is the
only out-of-enumeration status among all 294 slot entries. I verified the
enumeration against `protocol/output-schema.md` and confirmed the value
propagated into the prose's §2.1 summary table. Written up as C-6; the lead
is correct as stated and I found one consequence it did not mention.

**(c) The prose and JSON were produced separately, so S-8 is live.**
Confirmed, and this was the most productive surface in the pass. A
field-by-field comparison produced C-3 (three inconsistent relation counts),
C-5 (members and 17 cross-references that do not resolve), C-6 and C-7 (the
`SOURCED`-with-no-sources population and two confidence upgrades against the
prose). The operator's reading of the output's shape was right: the two
files diverge wherever they were not mechanically derived from each other.

Three things I checked for under S-8 and did **not** find, which bound the
damage: no slot entry is omitted anywhere — all 42 members carry all seven
slots, 294 of 294, so the schema rule the run was explicitly warned about is
satisfied exactly; no cluster label, sub-problem assignment or proponent
list diverges between the files; and no slot `filler` in the JSON states
something the prose contradicts on the substance. The divergences are in
counts, identifiers and confidence tags, not in content.

## 2.6 Things the run did that I checked and want on the record

These are not findings. They are practices I verified and that a later run
should preserve, because they are the reason this pass found what it found
rather than drowning in unverifiable claims.

- **It caught one of its own subagents misreporting a paper and recorded
  the catch in the output.** The Strasberg-Reinhard-Schindler deformation
  claim is reported as unsupported by the paper, the half that is supported
  is kept, and the episode is logged in §6.7 as "an instance of the failure
  mode the evidence rules exist to catch, caught inside this run". The
  paper's journal reference, which the same passage asserts, checks out
  (Phys. Rev. X 14, 041027 (2024)).
- **It declined to paraphrase texts it could not read.** Carter 1974's
  weak and strong anthropic principles are `[UNKNOWN]` and explicitly not
  paraphrased because the Cambridge PDF is a scan; the Diósi-Penrose
  reduction-timescale formula is withheld as background knowledge rather
  than stated; DeWitt 1967's two commonly repeated claims are left as leads
  and not asserted. Each of these is a place where a plausible-sounding
  sentence was available and was not written.
- **It refused a claim that the seed's framing invited.** The QBism entry
  records that a formulation of the form "the universe has no quantum state
  in any sense, since there is nobody outside it" surfaced in a search
  summary, could not be sourced to any QBist, and "**is not attributed to
  Fuchs, Mermin or Schack**" — and then corrects the seed in the other
  direction, that the sourced position permits a universal state and denies
  only its observer-independence. That correction is internally consistent
  with the §3.1 classification I relied on in C-4.
- **It bounded its own negative results.** The clean negative on any
  published link between the algebraic observer and the measurement problem
  comes with §6.6, a list of four search-term families *not* tried, and the
  instruction that "the negative is bounded by this list and should not be
  cited as absolute". That is the correct form for a negative result and it
  is what let me take the negative seriously without re-running the search.
- **It reported both sides of a contradiction inside its own camp.** On
  no-boundary normalisability it records Halliwell-Hartle-Hertog 2019
  claiming a normalisable time-neutral state and Kiefer reporting the
  tree-level inflaton density matrix is not normalisable, with "**Both are
  reported; this is not smoothed.**" I checked for smoothing under S-5 and
  found none to report: the run flags live disputes as live
  (Linde-Page, Dyson-Kleban-Susskind against Albrecht-Sorbo, Martin-Vennin
  against Gundhi et al., D1 against D5, Chua-Callender against
  Huggett-Thébault), names the terminological trap where "global" and
  "local" carry opposite verdicts, and declines to settle the no-boundary
  perturbation dispute in either direction. **S-5 returns zero findings.**
  I looked specifically for the tell the prompt describes — a sentence both
  sides of a live dispute would accept — in Part 3's six assumption
  sections, and did not find one I could substantiate to the standard the
  prompt sets for this surface.
- **It declined the synthesis it was best placed to make.** Part 5's open
  question 11 states the P1/P5 unification hypothesis and then refuses to
  pursue it, adding that "it should be tested by someone who did not build
  the scaffold". Given the forked-context contamination disclosed in
  META.yaml, that is the right call, and it is the restraint most likely to
  have been skipped.

## 2.7 Surfaces that returned zero findings

Stated explicitly so a reader knows these were worked and not skipped.

- **S-5 (smoothing): zero.** Reasoning above, §2.6.
- **S-7 (silent coverage gaps): zero.** I could not assess this to the
  depth the surface deserves, because `docs/approach-clusters.md` — the seed
  carrying the known-gaps list — was withheld from me by design. What I
  could check: the run addresses gaps by name throughout (whether Cluster G
  deserves a cluster, whether the thermal time hypothesis belongs in
  Cluster B, whether cosmic variance is continuous with the measure
  problem, the Landauer-type limits question, the G3b-to-E bridge the seed's
  gaps section was looking for), and each is answered or recorded as
  `[UNKNOWN]` with what would settle it. No gap I can identify from the
  staged files is dropped in silence. A reader holding the seed should
  re-run this surface; I flag it as the one surface my isolation genuinely
  weakened, and carry that into axis 4 in Part 3.
- **S-1 failure mode 1 (fabrication): zero**, across a complete 210-locator
  sweep. This is the finding the pass was most worth running for, and it is
  negative.
- **S-2 (invented fillers): zero**, across all 84 S6/S7 entries and the
  wider slot audit.

---

# Part 3 - Your own rubric scores

Scored against the five axes in `protocol/METHOD.md`, formed before reading
the target run's `REVIEW.md`, which I have not seen. Each score carries the
coverage limits of my own pass, stated in Part 2 §2.4: a complete sweep for
locator existence, a purposive ~9% sample for locator content, and no
access to the withheld seed.

**1. Citation integrity — 2/3.** All 210 identifier locators resolve to the
work attributed, with no fabrication, so the axis-1 cap does not apply and
the fabrication probe returns negative; against that, C-1 is a locator that
resolves and does not support the claim it is cited for, and C-2 and C-8 are
`[SOURCED]` tags carried by a review's unqualified assertion and by the
run's own arithmetic. Not 3, because C-1 damages a verdict; not 1, because
nothing is invented and the run volunteered a misattribution correction I
confirmed.

**2. Slot discipline — 3/3.** S7 is empty throughout clusters A, B, C, D, F
and G and S6 is filled exactly once there, scoped to a named sub-line with a
real source, so the surface most likely to carry invention carries none
across 84 entries; misfits are reported rather than forced, unread texts are
marked `LEAD` or `UNKNOWN` rather than `empty`, and all 294 slot entries are
present. The thirteen filled `SOURCED` slots with no sources (C-7) are a
defect of the structured record rather than of the slot judgments, whose
locators survive in the prose.

**3. Conflict rigour — 1/3.** Two of five `notational_variant` verdicts rest
on a disclaimer where the dictionary should be and on a source whose
equivalences are approximate and conditional in ways the run drops (C-2),
and six `genuine_conflict` verdicts assert `differs_in: "observables"`
without naming an observable, one of them contradicting the run's own prose
classification of that very pair (C-4). Not 0, because the two genuine
dictionaries are real and term-by-term, the run splits one verdict honestly
against its own interest, and four `differs_in` values are properly earned;
not 2, because this is the axis the evidence rules are most explicit about
and the failures are in its two named requirements.

**4. Coverage — 3/3.** Seven clusters, 42 members, 294 slot entries and
~210 verified locators, with every gap I can identify from the staged files
either answered or recorded as `[UNKNOWN]` with what would settle it, a long
and specific Part 6, and negatives bounded by an explicit list of untried
search terms. Two qualifications that do not change the score: C-5 means
part of this coverage is reachable only through the prose, and I could not
fully work S-7 because the known-gaps seed was withheld from me. Coverage as
a *method* result remains capped by the forked-context contamination, which
META.yaml states plainly and which I take at its word.

**5. Calibration — 2/3.** The tags mostly track reality and the run is
unusually willing to tag against its own interest: it caught a subagent's
misreport, refused to paraphrase three unread scans, declined twenty-one
journal references and two plausible arXiv identifiers, named its own
weakest entry twice, and bounded its negatives. Against that, C-8 tags its
own subtraction `[SOURCED]` fourteen lines after explaining why it cannot be,
C-2 tags a review's unqualified assertion `[SOURCED]`, C-7 upgrades two
`[INFERENCE]` fillers to `SOURCED` in the JSON, and C-10 leaves one
retrievable locator as a `[LEAD]`. The errors are concentrated in the
`SOURCED`/`INFERENCE` boundary and run in both directions, which is a
systematic boundary problem rather than a pattern of inflation.

---

# Part 4 - Divergence from the self-review

I read `target/REVIEW.md` only after Parts 1-3 were written and saved to
`out/`. My scores were formed against `protocol/METHOD.md` from the
target's output alone. Nothing below revises a score upward; the one place
where reading the self-review bears on a score is stated explicitly, with
the reason.

## 4.1 The scores side by side

| Axis | Self-review | This pass | Divergence |
| --- | --- | --- | --- |
| 1. Citation integrity | 2 | 2 | none in the number, substantial in the grounds |
| 2. Slot discipline | 3 | 3 | none in the number; its diagnosis is incomplete |
| 3. Conflict rigour | 2 | **1** | **the divergence that matters** |
| 4. Coverage | 3 | 3 | none in the number, non-overlapping evidence |
| 5. Calibration | 2 | 2 | none in the number, near-disjoint reasons |
| **Total** | **12/15** | **11/15** | **minus 1** |

## 4.2 The headline result: this self-review is not generous

The role card says a run that scored itself generously is a method data
point. **This one did not, and that is the finding.** It scored itself
12/15 where an independent pass scores it 11/15 — one point on one axis,
with four axes matching exactly.

More to the point than the arithmetic is what it volunteered unprompted: a
schema violation of its own, a caught subagent error preserved in the
output, two named coverage holes, a specific calibration failure it could
have left buried, the context contamination that invalidates its own best
score as a method result, a warning that its two most interesting claims
are "candidate syntheses in open-question clothing" deserving
"corresponding suspicion", and this:

> "**Prose and JSON agree** - believed, not verified exhaustively. The JSON
> was generated from a compact table written after the prose, not extracted
> from it, so **a divergence is possible and would be a review finding.**"

That sentence predicts C-3, C-5, C-6 and C-7 — four of my ten confirmed
findings, and three of the four highest-damage ones — before I found them. A
run that names in advance the surface on which it will be found wanting is
not inflating itself. On the method question the role card poses, the answer
is that self-review added real value here, and the specific value was
telling a reader where not to trust it.

## 4.3 Where we agree, and whether the agreement is worth anything

Agreement between this pass and the self-review is weaker evidence than it
feels: the target ran on a forked context carrying the seed author's
reasoning, and my staged inputs came from that same author's repository. So
for each agreement I state whether I hold it from my own retrieval or from
the self-review's argument.

**Axis 1, both 2 — but the self-review's reason no longer holds, and mine
is a different defect.** This is the most useful thing in Part 4. It caps
itself at 2 for one stated reason:

> "**A reviewer cannot distinguish 'a subagent fetched this' from 'a
> subagent said it fetched this' for the unsampled majority of roughly 150
> locators.** Since this axis caps the whole run at 0 for any single
> fabrication, an unsampled fabrication would retroactively zero it. 2 is
> the highest score the sampling supports."

**That gap is now closed, in the run's favour.** I fetched all 210
identifier locators myself — 133 arXiv ids and 77 DOIs — and every one
resolves to the work the target attributes it to. The fabrication risk the
self-review could not rule out from inside is ruled out from outside. By
its own reasoning, axis 1 would now go to 3.

It does not, because I found a defect it does not name: C-1, a locator that
resolves and does not support the claim it is cited for, plus C-2 and C-8,
two `[SOURCED]` tags carried by a review's unqualified assertion and by the
run's own arithmetic. So we land on the same number from opposite
directions — its uncertainty resolved favourably, replaced by a confirmed
error. The number is a coincidence; the grounds are the result. **Held from
my own retrieval**, not from its argument.

One slip in that passage, recorded because the whole axis-1 argument turns
on the count: the text says the cartographer independently verified
"**eight**" locators, and the parenthetical then lists twelve. Neither
figure changes my score.

**Axis 2, both 3, and we reach the 109-entry diagnosis independently and
identically — but its version is incomplete, in the direction that flatters
it.** The self-review calls the 109 entries "**sourced silences** - the
paper was read and the slot is genuinely empty", concludes "**The schema has
no way to express a sourced absence, and this is a real gap in the protocol
rather than sloppiness in the run**", and proposes a `read:` field naming
what was read to establish the silence.

I reached the same diagnosis from the JSON before reading this, and
proposed nearly the same fix. **Held from my own inspection** — but I
discount the agreement: it is the obvious inference available to anyone who
looks at the data, and the operator had supplied the 109 count as a lead.
This is convergence on an easy inference, not independent corroboration.

What I add is the part it gets wrong. **Not all 109 are silences.** 96 are
`status: empty` with an empty `filler`, and for those its defence is
right. The other 13 carry a substantive filler asserted as `SOURCED` with
no locator anywhere in the structured record, and two of them (E4c/S1,
E4d/S1) upgrade the prose's own `[INFERENCE]` tag to `SOURCED`. By
describing all 109 as a protocol gap the self-review exempts 13 entries
that are plain violations. I keep axis 2 at 3 — the slot *judgments* are
sound and the 13 are a defect of the structured record whose locators
survive in the prose — but its account of its own violation needs the
96/13 split to be accurate.

**Axis 4, both 3, from evidence bases that do not overlap.** Neither of us
can check the other. It scores coverage knowing the seed; I score it from
the staged files with `docs/approach-clusters.md` withheld, which is why
S-7 returned zero with a stated limit rather than a worked result. We agree
on 3 with almost no shared basis for agreeing. I also take the
contamination disclosure at face value from `META.yaml` and `OUTPUT.json`,
which the self-review restates — a shared input, not independent
confirmation; I did not and could not verify the forked-context claim.
**Our agreement on axis 4 should carry close to no weight.**

**Axis 5, both 2, for near-disjoint reasons, and here the self-review has a
finding I do not.** Its two reasons are that the cartographer cannot assess
its own calibration on the contaminated axis, and this:

> "several slots are tagged `SOURCED` as silence where the **underlying
> read was truncated** - Wallace's measurement survey cut off mid-section,
> the SEP consistent-histories entry truncated, the quantum-reference-frame
> Methods section unread, Azhar-Guth-Namjoo truncated before the section
> that matters most. Only one of these (B4's S4) was correctly downgraded
> to `LEAD` as 'emptiness-so-far'. **The others should have been and were
> not.**"

**That is a real, specific, self-caught miscalibration and I did not find
it.** I audited the 84 S6/S7 entries for invented fillers and the
`SOURCED`/`INFERENCE` boundary for upgrades; I did not cross-check which
sourced silences rested on reads the run itself records as truncated. I
have not verified the claim and am not asserting it, but it is the right
shape, it is checkable from Part 6's own retrieval-failure list, and it cuts
against the run. On this axis the self-review found something the adversary
missed.

My reasons for 2 are different — C-8, C-2, C-7's two upgrades, C-10 — and
only C-7 touches the same ground. The union of the two lists is larger than
either, which is the argument for running both roles rather than treating
one as a substitute for the other.

## 4.4 Axis 3: conflict rigour, 1 against 2

This is the divergence that matters, and the one the self-review could not
have reached from inside.

**Its reasons for 2.** It credits itself, correctly, with two downgrades
made against its own interest: the causal-patch / light-cone-time
equivalence to `unresolved` for want of a verified dictionary, and
relational QM against QBism to `unresolved` for want of a differing
probability, record or observable. Both check out; I confirmed both in Part
2. Its reason for not reaching 3 is a manufactured-conflict worry:

> "Several `genuine_conflict` verdicts are the cartographer's `[INFERENCE]`
> constructed from two abstracts **that do not engage each other**:
> relational QM against the perspective-neutral frame branch, the
> complementarity reading against CLPW on algebra type, and CLPW against
> the observer-dependent-entropy result. ... **a reviewer could reasonably
> say the run manufactured conflicts that no author has joined.**"

**Why 1.** Four things, in increasing order of how badly they cut.

First, **the criterion is the wrong one, and it mis-sorts its own
examples.** The self-review selects suspects by whether the authors engaged
each other. `EVIDENCE-RULES.md` §4 and `common-scaffold.md` do not require
engagement; they require a named difference in an allowed record, a
probability, or a predicted observable. Judged by the rule that actually
binds, the sort comes out differently. Its second example — complementarity
against CLPW on algebra type, relation 32 — **I checked and judged sound**:
type I against Type II-1 is a difference in the set of allowed observables,
exactly what the scaffold asks for, and the non-engagement is irrelevant to
that. Meanwhile six relations that *do* fail the binding test go unflagged
(C-4: relations 3, 9, 10, 11, 34, 40), each asserting
`differs_in: "observables"` with no observable named. The self-review
worries about one verdict that is fine and misses six that are not.

Second, **it cannot see the case that most damages this axis, because
seeing it requires comparing its own two files.** Relation 11 records QBism
against Page-Wootters as `genuine_conflict` differing in observables. The
target's own prose §3.1 puts that very pair in the opposite bucket:
"**Pairs that merely sound incompatible**: QBism against quantum cosmology,
which on the sourced record disagree about observer-independence rather than
about whether a universal state may be written." The authoritative document
classifies as merely-sounding-incompatible what the structured record
reports as a conflict in observables. A self-review that treats prose/JSON
agreement as "believed, not verified exhaustively" is by construction unable
to catch this.

Third, **it misses C-1 and C-2 entirely, and these bear hardest on this
axis.** On C-2 it is actively reassuring: "two rest on a review's authority
**and say so**", presented as adequate disclosure. The disclosure covers the
missing dictionary. It does not cover what I found at source — that
Freivogel's equivalences are explicitly approximate and conditional ("in the
approximation that the geodesic congruence never stops expanding"; "Given
this choice of initial condition") and that both conditions were dropped.
Finding that required re-reading the source, which is what an adversary is
for. And C-1 — the one Cluster G rivalry resting on a paper whose §I says
its factor "agrees with Vilenkin's 'tunneling' proposal" — appears nowhere
in the self-review. It is a `genuine_conflict` whose cited basis asserts
agreement.

Fourth, smaller but telling: **the self-review computes this axis over the
wrong population.** It says "Of **four** `notational_variant` verdicts".
`OUTPUT.json` has five. It has inherited the miscount from prose §2.4 that
I report as C-3, so C-3's damage has propagated into the run's own
self-assessment — a worked example of why a count divergence is not mere
bookkeeping.

**I do not move this score after reading the self-review.** Two of the
axis's five `notational_variant` verdicts fail its explicit dictionary
requirement and drop conditions that bound the source claim; six of its
`genuine_conflict` verdicts fail its explicit named-difference requirement,
one of them against the run's own prose; and the one Cluster G conflict is
mis-sourced. Not 0, because the two real dictionaries are genuine and
term-by-term, the A1/A2a verdict is split honestly against the run's own
interest, four `differs_in` values are properly earned, and the two
downgrades it claims credit for are real. But this is the axis the evidence
rules are most explicit about, and the failures are in both of its two named
requirements.

## 4.5 The self-review's next-steps list, scored against what this pass did

Recorded because it is method data about whether a self-review's priorities
survive contact with an adversary.

- **Item 2, "Run the adversary role ... specifically attacking the three
  `[INFERENCE]` conflicts named under axis 3 and the 109 sourced-silence
  entries."** Done, and both attacks returned something other than
  expected. Of its three named conflicts, one is sound (relation 32), one is
  confirmed defective (relation 9, inside C-4), and one is confirmed
  defective on a different ground than anticipated (relation 31, C-9: the
  problem is an unlocated uniqueness claim attributed to CLPW, not the
  non-engagement). On the 109, the split is 96 schema gap / 13 violation,
  not 109 schema gap.
- **Item 3, "Verify a random sample of 20 locators independently. If any is
  fabricated, this run is discarded as research."** Discharged beyond what
  was asked: 210 of 210 rather than a sample of 20, none fabricated, so the
  disqualifier does not fire. The sampling question has moved rather than
  closed — it now sits entirely on whether a cited work *says* what the
  target claims, for the roughly 136 works I did not read.
- **Item 5, "Fix `protocol/output-schema.md` to express sourced absence."**
  Endorsed, with the 96/13 correction, and with two additions: the `status`
  enumeration needs enforcing (C-6) and the identifier scheme needs to be
  shared between the two files (C-5).
- **Item 1, "Replicate on a fresh context. Nothing here is a method result
  until then."** Untouched by this pass and still owed. I could not test
  the contamination claim and did not try.

---

# Part 5 - Verdict

**The target run passes as research under `protocol/METHOD.md`, with a
bounded list of corrections. It does not yet count as a method result, and
that is its own disclosure rather than my finding.**

The disqualifier in `METHOD.md` is a fabricated citation: "A run with a 0 on
axis 1 is discarded as research and kept as method data." **There is no
fabricated citation.** All 210 identifier locators in the output were
resolved in this run and every one is the work the target attributes it to.
That is a complete sweep, not a sample, and it is the single most
load-bearing result of this pass. Axis 1 is 2, not 0; the run is not
discarded.

Separately, `METHOD.md` distinguishes the research target from the method.
On the method side the run is not usable and says so: it ran on a context
forked from the session that wrote the seed, so the seed-withheld control
cannot be run against it and its coverage figure is an upper bound. I could
not test that claim and did not try. A replication on a genuinely fresh
context is still owed, and no coverage number here should be cited as a
method result until it exists.

## What survives

- **The locator base.** 210 of 210 resolve and are correctly attributed,
  including all eleven 2025-2026 identifiers and all 28 old-style ones, and
  twelve asserted journal references with no DOI in the text. The two
  identifiers the run was tempted to guess appear nowhere. This is now
  independently established and is the most reusable thing the run produced.
- **The emptiness map, and the structural result that rests on it.** All 294
  slot entries present, 48% recorded empty or misfit, no invented filler
  across the 84 S6/S7 entries where invention was likeliest. The
  slot-complementarity claim in §2.1 — that one half of the field fills
  S4/S5 and leaves S6/S7 empty while Cluster E does the reverse — rests on
  that map and survives with it. It is the run's main result and I found
  nothing against it.
- **The seed corrections.** The A2a/A2b split, which I verified against
  Wallace's footnote 4 myself; the QBism correction, whose primary quotations
  check out at the point I verified and which is internally consistent with
  the §3.1 classification I later used against the run in C-4; the
  thermal-time cross-listing; the cosmic-variance rejection recorded as a
  result; the demotion of Cluster G to a setting with the
  boundary-condition proposals carved out; and the correction to the
  repository's own P5 framing in `docs/problem-statement.md`.
- **The two real dictionaries**, A1/A2a on S4 and the Hoehn-Smith-Lock
  trinity, both genuine and term-by-term, with the A1/A2a verdict split
  honestly and its unmapped residue recorded.
- **The run's own citation correction** on the number misattributed to
  Martin & Vennin, which I confirmed in every particular from both papers.
  It is the precise failure mode the evidence rules exist to prevent, caught
  unprompted on a number it would have been conventional to repeat.
- **The Gibbons & Hawking finding**, which now has a primary-source
  foundation it did not have: the Everett-Wheeler sentence is in the
  paper's own published abstract, so the run's substance tag was right and
  its wording hedge was over-cautious.
- **The negatives, as bounded.** The clean negative on any published link
  between the algebraic observer and the measurement problem stands as a
  bounded negative, because §6.6 lists the search terms not tried. That is
  the correct form for a negative result.
- **Part 6.** 39 leads with what would confirm each, three texts explicitly
  not paraphrased, twenty-one journal references not guessed, and a claim
  explicitly not attributed to any QBist. It is the most directly actionable
  part of the output and nothing in my pass damages it.

## What does not survive

- **Relation 36, G3a against G3b, as sourced** (C-1). The conflict is real;
  the citation is not. Its one sourced basis is a paper that asserts the two
  proposals agree.
- **Relations 20 and 21 as `notational_variant`** (C-2). Both should be
  `unresolved`, with the source's approximation and initial-condition
  clauses restored.
- **The `differs_in` values on relations 3, 9, 10, 11, 34 and 40** (C-4).
  Six conflicts in observables with no observable; relation 11 contradicts
  the run's own prose.
- **The §2.4 counts and the derived intra-cluster concentration claim**
  (C-3). Three inconsistent counts of one set; the authoritative figure, 37,
  is stated nowhere.
- **`OUTPUT.json` as a mechanically comparable artefact** (C-5, C-6, and
  the 13 of C-7). Three prose members missing, eleven member ids
  untraceable to the prose, seventeen dangling cross-references, one
  self-relation, one out-of-enumeration status value that propagated into
  the prose, and thirteen sourceless `SOURCED` fillers. The file's stated
  purpose is mechanical comparison and it cannot currently be joined to
  itself. The prose is unaffected and remains authoritative.
- **"Roughly ninety-seven orders of magnitude" as `[SOURCED]`** (C-8). It
  is the run's own arithmetic across one paper's restatement, which the run
  had itself warned against relying on.
- **"Removes CLPW's uniqueness claim"** (C-9). No locator, and the authors
  credited with removing it present their work as a generalisation.
- **Part 3.6's claim that the trinity equivalence ties the compatibility
  question to the boundedness question** (P-1), pending one check I could
  not perform. If it falls, the run's most unexpected structural finding
  reverts from something two communities independently found to the run's
  own synthesis — which is where its own self-review already suggests a
  reader should keep it.

## Surfaces this pass could not cover

Stated so the next run knows what remains unattacked rather than cleared.

- **S-7, silent coverage gaps: not covered, and the cause is the prompt.**
  `prompts/02-adversary.md` withholds `docs/approach-clusters.md` while S-7
  asks the adversary to check which of a list of known gaps the target
  dropped — and that list exists only inside the withheld file. The surface
  is unworkable as specified, for any adversary obeying the prompt, at any
  budget. I did not work around it and did not request the file. What I
  could check is in Part 2 §2.7: no gap identifiable from the staged files
  is dropped in silence. **This is a finding about the method, not about the
  target run**, and the fix belongs in a forked prompt: either stage the
  gaps list separately from the seed's cluster map, or drop S-7 from the
  adversary's remit and give it to the human reviewer.
- **Locator content for roughly 136 of about 150 cited works.** Existence
  and attribution are settled for all of them; whether each says what the
  target claims is settled for 14. The sample was purposive, not random,
  and chosen to hit the load-bearing and self-hedged claims, which is why it
  found C-1, C-2 and C-8 — but a content-level error in an ordinary,
  unremarkable citation in Cluster A, C or D would not have been caught.
  `METHOD.md`'s axis-1 cap means the cost of that remainder is asymmetric,
  so a later pass should sample it randomly rather than purposively, to get
  an unbiased estimate rather than a hit list.
- **The contamination claim itself.** I had no access to the target's
  conversation history and took `META.yaml` at its word.

## The one-line answer

It passes as research, its citation base is sound and now independently
verified, its emptiness map and slot-complementarity result stand, and its
conflict verdicts are the part a later run must fix: five of the forty-one
relations are mis-verdicted, two are mis-sourced, and the structured file
needs repair before any run can be compared with it mechanically.
