# Output contract

**Schema version: v1.** v0 is frozen; Run 01 and Run 02 were written
against it. What changed and why is at the bottom.

Runs that produce structured output write `OUTPUT.json` alongside the prose
`OUTPUT.md`. The prose is for reading; the JSON is for comparing runs
mechanically. Both must agree; the prose is authoritative, and a divergence
is a review finding.

`protocol/validate.py` checks a file against the mechanical rules in this
document. Run it before committing a run. It cannot check whether a claim
is true, only whether the contract was followed.

## Schema

```json
{
  "run": "01-consolidate-approaches",
  "model": "string",
  "date": "YYYY-MM-DD",
  "scaffold_version": "v0",
  "schema_version": "v1",

  "counts": {
    "clusters": 0, "members": 0, "slot_entries": 0,
    "slots_filled": 0, "slots_empty": 0, "slots_denied": 0,
    "slots_misfit": 0, "relations": 0
  },

  "clusters": [
    {
      "id": "A",
      "label": "string",
      "subproblems": ["P1", "P2"],
      "members": [
        {
          "id": "A1",
          "label": "string",
          "proponents": ["string"],
          "slots": {
            "S1": {
              "filler": "string, or null when the slot is empty",
              "status": "filled|empty|denied|misfit",
              "confidence": "SOURCED|LEAD|INFERENCE|UNKNOWN",
              "sources": ["arXiv:xxxx.xxxxx", "doi:..."],
              "established_by": [
                { "locator": "arXiv:xxxx.xxxxx",
                  "read": "what was read, and that it contains no such rule" }
              ]
            },
            "S2": {}, "S3": {}, "S4": {}, "S5": {}, "S6": {}, "S7": {}
          }
        }
      ]
    }
  ],

  "relations": [
    {
      "a": "A1", "b": "A2", "slot": "S4",
      "verdict": "notational_variant|genuine_conflict|non_competing|unengaged|unresolved",
      "dictionary": "term-by-term; required when notational_variant",
      "dictionary_conditions": ["any approximation or initial condition the source attaches to the mapping"],
      "differs_in": "records|probabilities|observables; required when genuine_conflict",
      "inference_premises": ["required when unengaged, or when confidence is INFERENCE"],
      "non_engagement_check": "required when unengaged: what search established that no source puts the two to each other",
      "confidence": "SOURCED|LEAD|INFERENCE|UNKNOWN",
      "sources": []
    }
  ],

  "assumptions": [
    { "id": "X1", "statement": "string", "held_by": ["A1"],
      "denied_by": ["E4"], "load_bearing_for": ["P4"],
      "confidence": "...", "sources": [] }
  ],

  "scaffold_misfits": [
    { "slot": "S3", "cluster": "F", "problem": "string", "proposed_fix": "string" }
  ],

  "open_questions": [
    { "question": "string", "why_it_matters": "string",
      "what_would_settle_it": "string", "priority": 1,
      "is_candidate_synthesis": false }
  ],

  "known_gaps_addressed": [
    { "gap": "verbatim from docs/known-gaps.md", "outcome": "string",
      "status": "addressed|unknown|not_reached" }
  ],

  "unverified_leads": [ { "claim": "string", "needed": "string" } ]
}
```

## Sourced absence

The central fix in v1. `EVIDENCE-RULES.md` §3 requires a run to report that
an approach says nothing about a question, and to have read something to
know that. v0 then forbade the only honest way to record it: it said
`sources` may be empty only for `LEAD`, `INFERENCE` or `UNKNOWN`, so a
*sourced silence* had no legal form. Run 01 produced 109 entries in that
position and left the violation visible rather than citing a page number
for an absence, which was the right call.

v1 separates the two kinds of evidence:

- **`sources`** carries locators supporting a **positive** claim: this
  approach fills this slot with this object.
- **`established_by`** carries what was **read to establish an absence**:
  the work, and what part of it was read, such that the silence is a
  finding rather than a gap in the run's reading.

For a `SOURCED` entry exactly one of them is non-empty, and `status`
decides which:

| `status` | meaning | takes |
| --- | --- | --- |
| `filled` | the approach fills the slot | `sources` |
| `denied` | the approach positively asserts there is no such object | `sources` |
| `empty` | the approach says nothing about the slot | `established_by` |
| `misfit` | the slot is the wrong question for this approach | `established_by` |

`denied` is new in v1 and takes `sources`, not `established_by`, because a
denial is a doctrine someone argued for, not a silence. Run 01 used
`denied` once while v0's enum did not contain it; the value was right and
the enum was wrong.

An `empty` entry sets `filler` to `null`. An `empty` entry with a
non-null filler is a contradiction and the validator rejects it.

**`established_by` is not a licence to assert a silence cheaply.** Its
`read` field must say what was read. "The paper" is not a value; "§§1-4 and
the conclusions; no probability rule is stated anywhere" is. Where the read
was **truncated**, the entry is `LEAD`, not `SOURCED` — an emptiness-so-far
is not a sourced absence. Run 01's calibration score was marked down for
exactly this, on four entries whose underlying read cut off mid-section.

## The `unengaged` verdict

Also new in v1. Three of Run 01's 24 `genuine_conflict` verdicts were the
run's own inference from two sources whose authors never addressed each
other, and Run 02 confirmed it. v0 had no verdict for that, so the run had
to call them conflicts or call them nothing.

`unengaged` means: the two positions appear incompatible, the
incompatibility is the run's inference, and no retrieved source puts them to
each other. It requires `inference_premises` and `non_engagement_check`,
the second naming the search that failed to find an engagement. A bounded
negative needs its search terms, or it is not a negative.

This is not a weaker `genuine_conflict`. It is a different claim, and often
a more interesting one: two literatures holding incompatible positions
without having noticed is a finding about the field, not about the
positions.

## Validation rules

All mechanically checkable, all implemented in `protocol/validate.py`.

1. Every member has all seven slot keys present. Omission and emptiness are
   different.
2. `status` is one of `filled`, `empty`, `denied`, `misfit`.
3. `confidence` is one of `SOURCED`, `LEAD`, `INFERENCE`, `UNKNOWN`.
4. `status: "empty"` requires `filler: null`.
5. `confidence: "SOURCED"` with `status` `filled` or `denied` requires a
   non-empty `sources`.
6. `confidence: "SOURCED"` with `status` `empty` or `misfit` requires a
   non-empty `established_by`, each entry carrying `locator` and `read`.
7. `confidence` `LEAD`, `INFERENCE` or `UNKNOWN` requires both `sources`
   and `established_by` to be empty. Evidence and a disclaimer of evidence
   do not go together.
8. `verdict` is one of the five listed values.
9. `notational_variant` requires a non-empty `dictionary`. A `dictionary`
   whose text states that the mapping was **not** verified is rejected: that
   is `unresolved`. Run 02 found two verdicts in exactly that state.
10. `genuine_conflict` requires `differs_in` to be one of `records`,
    `probabilities`, `observables`.
11. `unengaged` requires `inference_premises` and `non_engagement_check`.
12. `confidence: "INFERENCE"` on a relation requires `inference_premises`.
13. `counts` matches the arrays it describes, exactly.
14. Every `a` and `b` in `relations`, and every id in `assumptions`, names a
    member that exists. Run 02 found 17 dangling cross-references and three
    prose members absent from the JSON; the validator finds 20.

    **There is no external-position form, deliberately.** Run 01's dangling
    references are mostly real approaches it related to without mapping:
    the fat-geodesic measure, the causal-diamond measure, SIA, the
    Dirac-Heisenberg presentation of Page-Wootters. The fix is to promote
    each to a member with its own seven slots, not to add a way to point at
    something unmapped. If a position is worth a relation, it is worth a
    row; a relation to an unmapped position is a coverage gap wearing a
    reference.
15. Member ids are unique across all clusters.

A run may fail a rule deliberately, as Run 01 did on the sourced-silence
rule it had no legal way to satisfy. Then say so in `REVIEW.md` and leave
the failure visible. Silent compliance by backfilling a locator for an
absence is worse than a declared violation.

## What changed from v0, and who found it

| Change | Found by |
| --- | --- |
| `established_by`, and the `sources` exemption for absences | Run 01, axis 2; diagnosed 96/13 by Run 02 |
| `denied` added to the status enum | operator pass over Run 01's JSON, confirmed by Run 02 |
| `unengaged` verdict | Run 01, axis 3; confirmed by Run 02 |
| `dictionary_conditions` | Run 02, which found two dictionaries dropping the source's stated approximation and initial condition |
| `counts` block and rule 13 | Run 02, which found three mutually inconsistent relation counts |
| Rule 14 on dangling references | Run 02 |
| `known_gaps_addressed`, keyed to `docs/known-gaps.md` | Run 02, whose S-7 surface was uncheckable |
| `is_candidate_synthesis` on open questions | Run 01, which flagged two of its own open questions as candidate syntheses |
| `protocol/validate.py` | operator: none of the above is enforceable by prose alone |

## What the validator found on Run 01

Run against `runs/01-consolidate-approaches-2026-11-04/OUTPUT.json`, read
as v0: **112 schema gaps and 54 violations.**

The 112 are every `SOURCED` entry with status `empty` or `misfit`. Run 02
reported 96 for the narrower class of `empty` with an empty filler, so the
two partitions differ and neither is wrong; 112 is the full set that v0
could not express.

The 54 split into six classes, of which Run 02's manual pass found three:

| Rule | Count | Found by Run 02 |
| --- | --- | --- |
| 14 dangling references | 20 | yes, 17 of them |
| 5 `SOURCED` `filled` with no sources | 12 | yes, as its 13 real violations |
| 12 `INFERENCE` relation with no premises | 11 | no |
| 7 evidence alongside `LEAD`/`INFERENCE`/`UNKNOWN` | 5 | no |
| 4 `empty` with a non-null filler | 3 | no |
| 9 a dictionary stating it was not verified | 2 | yes |
| 2 `denied` outside the v0 enum | 1 | no, found in an operator pass |

Four classes went unseen by a careful adversary with a full budget. That is
the argument for the validator: the sourced-absence gap was a missing field,
but the other 54 were only ever a missing check.

Run 01 and Run 02 are not amended for these. Runs are append-only, and the
corrections belong to a later cartography run.

v0 remains in the history. A run states its `schema_version`, and a run
written against v0 is read against v0.
