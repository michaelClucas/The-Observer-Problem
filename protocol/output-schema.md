# Output contract

Runs that produce structured output write `OUTPUT.json` alongside the prose
`OUTPUT.md`. The prose is for reading; the JSON is for comparing runs
mechanically. Both must agree; the prose is authoritative if they diverge,
and a divergence is a review finding.

## Schema (informal)

```json
{
  "run": "01-consolidate-approaches",
  "model": "string",
  "date": "YYYY-MM-DD",
  "scaffold_version": "v0",

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
            "S1": { "filler": "string", "status": "filled|empty|misfit",
                    "confidence": "SOURCED|LEAD|INFERENCE|UNKNOWN",
                    "sources": ["arXiv:xxxx.xxxxx", "doi:..."] },
            "S2": { "...": "..." },
            "S3": {}, "S4": {}, "S5": {}, "S6": {}, "S7": {}
          }
        }
      ]
    }
  ],

  "relations": [
    {
      "a": "A1", "b": "A2", "slot": "S4",
      "verdict": "notational_variant|genuine_conflict|non_competing|unresolved",
      "dictionary": "string, required when notational_variant",
      "differs_in": "records|probabilities|observables, required when genuine_conflict",
      "confidence": "SOURCED|LEAD|INFERENCE|UNKNOWN",
      "sources": []
    }
  ],

  "assumptions": [
    {
      "id": "X1",
      "statement": "string",
      "held_by": ["A1", "B2"],
      "denied_by": ["E4"],
      "load_bearing_for": ["P4"],
      "confidence": "...",
      "sources": []
    }
  ],

  "scaffold_misfits": [
    { "slot": "S3", "cluster": "F", "problem": "string", "proposed_fix": "string" }
  ],

  "open_questions": [
    { "question": "string", "why_it_matters": "string",
      "what_would_settle_it": "string", "priority": 1 }
  ],

  "unverified_leads": [
    { "claim": "string", "needed": "string" }
  ]
}
```

## Rules

- Every `slots` entry is present even when `status` is `empty`. Omission is
  not the same as emptiness, and the comparison tooling cannot tell them
  apart.
- `sources` is empty only when `confidence` is `LEAD`, `INFERENCE`, or
  `UNKNOWN`.
- `relations` need not be exhaustive over all pairs. Cover the pairs that
  the field treats as rivals, plus any pair the run finds surprisingly
  related.
- `unverified_leads` is where leads go to be picked up by a later run. A
  long list here is a good outcome, not a failure.
