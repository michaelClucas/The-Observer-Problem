# Experiment design

## What is being tested

Two things, separately.

**The research target.** Whether the approaches to the cosmological-scale
observer problem (see `../docs/problem-statement.md`) can be stated in one
notation, and where they actually conflict.

**The method.** Whether a language-model agent, given a fixed scaffold,
strict evidence rules, and a structured output contract, produces a map a
domain expert would accept. This is why runs are versioned, prompts are
committed, and outputs are never edited in place.

Keeping these separate matters. A run can fail as research while still
being a useful data point about the method, and vice versa. Report both.

## Unit of work: the run

A run is one agent invocation against one committed prompt, producing one
directory under `runs/`. Runs are append-only.

```
runs/<NN>-<slug>-<YYYY-MM-DD>/
  META.yaml          what model, what prompt commit, what tools, what cost
  OUTPUT.md          the agent's output, verbatim and unedited
  OUTPUT.json        the structured part, if the prompt asked for one
  REVIEW.md          human assessment, written after reading OUTPUT
  DIFF.md            what this run changed about the seed docs, if anything
```

`OUTPUT.md` is never edited. Corrections go in `REVIEW.md` or in a later
run. An edited output destroys the method data.

## Run numbering

- `01` Consolidate approaches and map to the common scaffold.
  Prompt: `prompts/01-consolidate-approaches.md`.
- `02` Adversarial pass over 01. Prompt: `prompts/02-adversary.md`, role
  card `prompts/00-system-adversary.md`. Runs on a fresh context, never a
  fork of the target run.
- `03+` Decided after 02 is reviewed. Candidates: per-cluster deep dives,
  a replication of 01 with the seed docs withheld.

Replication is the point of the numbering. Run 01 should be re-run on at
least two different models before any of its conclusions are built on.

## Roles

A run uses one or both:

- **Cartographer.** Fills the scaffold, builds the map, reports
  conflicts. Rewarded for coverage and traceability, not for insight.
- **Adversary.** Reads a completed run and attacks it: unverifiable
  citations, slots filled on no evidence, conflicts asserted without a
  dictionary, approaches misattributed. Runs against 01 before any 03
  starts.

Run 01 is Cartographer only.

## Controls

- **Seed-withheld control.** A second instance runs the same prompt with
  `docs/approach-clusters.md` removed. If the seeded and unseeded runs
  produce very different cluster sets, the seed is doing the work rather
  than the agent, and the seeded run's coverage claims mean little.
- **Fabrication probe.** The seed deliberately contains references given
  only by author and approximate year. An agent that returns them as
  complete verified citations has fabricated the detail. Check for this
  explicitly in `REVIEW.md`.

## Review rubric

Score each 0-3 in `REVIEW.md`, with one sentence of justification each:

1. **Citation integrity.** Does every reference exist and say what the run
   claims it says? Any single fabricated citation caps the whole run at 0
   on this axis.
2. **Slot discipline.** Are empty slots reported as empty rather than
   filled with plausible-sounding guesses?
3. **Conflict rigour.** Is every claimed notational-variant backed by an
   explicit dictionary, and every claimed genuine conflict backed by a
   difference in records, probabilities, or observables?
4. **Coverage.** How many of the clusters and known gaps are addressed with
   primary sources?
5. **Calibration.** Do the confidence tags track reality? Specifically,
   are the low-confidence items the ones a domain expert would also call
   uncertain?

A run with a 0 on axis 1 is discarded as research and kept as method data.

## What is not part of the method

- No voting between agents to settle a question of fact.
- No treating agreement across runs as evidence of correctness. Models
  share training data; agreement is cheap.
- No editing a prompt after a run has used it. Fork it to a new number.
