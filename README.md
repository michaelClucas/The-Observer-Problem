# The Observer Problem

An open-source AI-research experiment targeting the observer problem on the
cosmological scale.

Quantum theory needs something outside the system to record an outcome.
Cosmology has no outside. That mismatch has been attacked for seventy years
by at least five research communities who rarely cite each other, in
notations that make it hard to tell whether they disagree or are answering
different questions.

This repository does not try to solve that. It tries to map it, using
language-model agents under a fixed protocol, with every prompt, output,
and review committed so the result can be checked and replicated.

## Status

Scaffolding only. No runs yet.

## Layout

| Path | What it is |
| --- | --- |
| `docs/problem-statement.md` | The problem, split into five sub-problems P1-P5 |
| `docs/common-scaffold.md` | Provisional shared notation: seven slots S1-S7 |
| `docs/approach-clusters.md` | Hand-written seed map of known approaches |
| `protocol/METHOD.md` | Experiment design, run structure, review rubric |
| `protocol/EVIDENCE-RULES.md` | Citation and confidence rules, binding on all runs |
| `protocol/output-schema.md` | The structured output contract |
| `prompts/` | Committed, versioned agent prompts |
| `runs/` | One append-only directory per agent run |
| `findings/` | Human-authored syntheses across runs |
| `sources/bibliography.md` | Shared bibliography with verification status |

## How a run works

1. Pick a prompt from `prompts/`. Prepend `prompts/00-system-researcher.md`.
2. Give the agent the seed docs the prompt lists, and nothing else.
3. Create `runs/<NN>-<slug>-<date>/`, fill `META.yaml`, save the agent's
   output verbatim as `OUTPUT.md` and `OUTPUT.json`.
4. Write `REVIEW.md` against the rubric in `protocol/METHOD.md`.
5. Never edit a committed output. Corrections go in the review or a later
   run.

Run 01 should be replicated on at least two different models, plus one
seed-withheld control, before anything is built on its conclusions.

## Two things are being measured

The research target is the map itself. The method target is whether an
agent under these constraints produces something a domain expert would
accept. A run can fail at one and succeed at the other, so reviews score
them separately.

## Design commitments

- Append-only runs. An edited output is not a data point.
- A fabricated citation invalidates a run, regardless of how good the rest
  is.
- Empty is an answer. An approach that says nothing about a question gets
  recorded as saying nothing.
- No synthesis before the map. The first runs are forbidden from proposing
  a resolution.
- Agreement across models is not evidence of correctness. Models share
  training data.

## Contributing

See `CONTRIBUTING.md`. Corrections to the seed docs are the most useful
thing to send, especially misattributions in `docs/approach-clusters.md`.
