# Research plan: the cosmological-observer route

**Status: proposed. Nothing here has been executed.** Written against
`main` at `b4a2bf5`, with Run 01 and Run 02 merged.

The question: **where should the cosmological-observer route go, judged
from the data rather than from which theories are widely accepted?**

The route in: sort the questions into **decidable now**, **decidable in
principle**, and **floor-limited**, and let that sorting decide where
everything after goes.

---

## 1. The triage, as a method

The triage is a **computation, not a judgement**. For any question posed as
a difference between two positions, three numbers settle it:

| Symbol | What it is | Where it comes from |
| --- | --- | --- |
| `Delta` | the predicted difference in some observable | theory, often via Maple |
| `sigma_now` | the error on that observable in current data | reanalysis |
| `sigma_floor` | the irreducible error on one sky | Maple job 002 |

and the bins are:

| Bin | Condition | Meaning |
| --- | --- | --- |
| **D1** decidable now | `Delta > sigma_now` | data in hand settles it |
| **D2** decidable in principle | `sigma_floor < Delta <= sigma_now` | better measurement settles it; say how much better |
| **D3** floor-limited | `Delta <= sigma_floor` | no measurement ever settles it |
| **D4** no differing observable | no `Delta` exists | the positions predict identically |
| **D0** not yet posed | `Delta` not computable as stated | the question is unformulated |

### D0 is a queue, not a verdict

**This is the plan's central guard against its own bias.** Most of Run 01's
map starts in D0: the positions are stated in incompatible formalisms and
no `Delta` can be computed without first putting them in a common form.

A question in D0 is **not** undecidable. It is unformulated. The honest
report of a D0 question is "nobody has posed this so that data could bear
on it", which is a statement about the literature, not about nature.
Scoring D0 as D3 would be the single easiest way to fake this plan's
headline result, and every work package below states which bin it expects
*before* it runs, so that substitution is visible if it happens.

### What the plan must not assume

Run 01 recorded 48% of its scaffold slots as empty or misfit. **That is a
fact about what approaches say, not evidence about what is measurable.** An
approach can be silent on six of seven slots and still make a sharp
prediction; an approach can fill every slot and predict nothing. The
scaffold count does not feed the triage and is not used as a proxy for it
anywhere in this plan.

Symmetrically: the plan does not assume the triage will come out mostly
D3. If most questions turn out to be D1 or D2, the field is far more
empirical than the map suggests and WP-2's result says so.

Standing in the literature carries no weight. A position held by one
author and a position held by a field enter the triage identically.

---

## 2. What the data actually is

Verified on this machine, not assumed. Python 3.14.7, pip 26.2.1.

| Package | Version | Status |
| --- | --- | --- |
| numpy | 2.5.4 | installs clean |
| scipy | 1.18.1 | installs clean |
| astropy | 8.0.2 | installs clean |
| matplotlib | 3.11.2 | installs clean |
| sympy | 1.14.0 | installs clean (arrives with camb) |
| **camb** | **2.0.5** | **installs and runs** |
| emcee | 3.1.6 | installs clean |
| getdist | 1.7.7 | installs clean |
| corner | 2.3.0 | installs clean |
| **classy** | — | **fails to build.** No C toolchain; `WinError 2` on the wheel build |

**The plan uses camb and does not use classy.** This is a verified
decision, not a preference. camb was run, not merely imported: a full
`lmax=2500` TT/TE/EE spectrum takes **0.8 s** and gives the first acoustic
peak at `l=220` as 5732 muK^2, which is correct. That benchmark sets the
cost estimates below: a 10^5-sample chain is roughly 22 core-hours, so
every MCMC in this plan is either parallelised or run at reduced `lmax`.

Datasets, with what each can and cannot settle:

| Dataset | Size | Settles | Does not settle |
| --- | --- | --- | --- |
| Planck 2018 TT/TE/EE, `plik_lite` binned + covariance | tens of MB | the shape of a correction to the primordial spectrum | anything at `l < 30`, where the floor dominates |
| Planck 2018 low-`l` | small | the large-angle anomalies | small-scale corrections |
| Planck non-Gaussianity constraints (`f_NL`) | published + templates | higher-order correlator amplitudes | anything two-point |
| Planck lensing | moderate | integrated growth | primordial phase information |

**Not worth the compute, and why.** The full `plik` likelihood, in favour
of `plik_lite`: it adds foreground nuisance parameters that none of these
questions touch, at a large cost in sampling dimension. Raw time-ordered
data: no question here reaches below the released spectra. CMB-S4 or
LiteBIRD forecasts: useful for D2 thresholds, but a forecast is not data
and nothing in this plan is concluded from one.

---

## 3. Symbolic work: Maple as a daily batch service

Maple runs on another machine, roughly one turnaround a day. The
convention is in `../maple/README.md` and is shared with the sibling
repository.

**No work package blocks on more than one round trip per day.** Round-trip
counts are stated per package in §4 and total **4** across the whole plan.

Jobs 001 and 002 are written, cross-checked in sympy, and ready; they are
independent and queue together on day one.

### Why the clock-spectrum question is not job 001

The brief named it as a plausible first candidate. **It was assessed and
rejected**, for two reasons.

First, it may not be well posed. Run 02's finding P-1 (`PLAUSIBLE`) is
that the trinity equivalence's spectral condition is probably about
**non-degeneracy and continuity**, not about **boundedness**, and the two
are logically independent. Boundedness is the axis of Run 01's Part 3.6
trade-off. If P-1 is right, the trade-off loses the published link that
elevates it from one run's inference to something two communities found
independently, and there is nothing yet to compute.

Second, even if well posed, it is **not Maple work**. The content is von
Neumann algebra type classification, crossed products and covariant POVMs.
Maple has no natural handle on these, and a plausible-looking Maple
manipulation of an operator algebra would be worse than no result.

So it becomes **WP-7**, a literature read of `arXiv:1912.00033` §V and
§III.2, costing one agent-run and gating any later work on the trade-off.
Promoting it to job 001 because it is the most interesting item in the map
is exactly the error the plan is built to avoid.

### Lean

No Lean infrastructure up front, and none is set up here.

**The trigger.** A claim goes to `lean/` when it has explicit hypotheses
and a conclusion that follows **by proof rather than by measurement**, and
when it has been *stated* precisely enough that the hypotheses are
enumerable. Both conditions; the second is what fails today.

This repository is likelier than its sibling to produce such claims, since
the measure and operator-algebra material is mathematical. The live
candidate is the clock trade-off, and it is **not yet proof-shaped**: Run
01 states it as an inference across three clusters, and WP-7 may find its
link does not hold. Formalising a claim whose hypotheses are unsettled
would produce a verified theorem about the wrong thing.

Note for whoever reaches the trigger: mathlib has limited differential
geometry and no general relativity. A proof-shaped claim here will be
measure-theoretic or algebraic, not geometric.

---

## 4. Work packages

Dependencies are stated; nothing else is implied. Cost is in agent-runs
plus compute, roughly.

### WP-0. Apply Run 02's corrections and migrate to schema v1

**Establishes:** a map that can be built on. **Depends on:** nothing.
**Data:** none. **Maple:** none. **Cost:** 1 run.

Run 02 established five mis-verdicted relations (3, 9, 10, 11, 34 should be
`unresolved`; 40 needs the new verdict or `unresolved`), two mis-sourced
items, 13 real schema violations, and 112 entries needing `established_by`
under schema v1. The `[SOURCED]` tag on "97 orders of magnitude" must
become `[INFERENCE]` with Run 02's named premises.

**Expected bin:** not applicable; this is hygiene. **Falsifier:** if
applying the corrections changes the slot-complementarity result in Run
01 §2.1, that result was resting on the bad verdicts and the plan's
understanding of the map is wrong. Check this explicitly.

**This is Run 03 and it comes first.** Everything downstream reads the map.

### WP-1. Replicate Run 01 on a fresh context

**Establishes:** whether any coverage claim in Run 01 is a method result.
**Depends on:** nothing. **Data:** none. **Maple:** none. **Cost:** 1 run,
comparable to Run 01.

Ranked first in both reviews. Run 01 ran on a context forked from the seed
author, so its coverage figure is an upper bound and the seed-withheld
control cannot be run against it.

**Expected bin:** not applicable. **Falsifier:** if the replication's
cluster set differs materially, the seed was doing the work and Run 01's
structural result is an artefact.

Runs in parallel with WP-0; they touch different things.

### WP-2. Build the decidability ledger

**Establishes:** the bin for every pairing and open question in the map.
**Depends on:** WP-0, and job 002 for `sigma_floor`. **Data:** published
error bars initially. **Maple:** job 002 (1 round trip, already queued).
**Cost:** 1-2 runs.

For each of Run 01's 34 pairings and 12 open questions: is `Delta`
computable as stated? If yes, compute it and compare against `sigma_now`
and `sigma_floor`. If no, record **D0** and state **what would make it
computable** — that statement is the ledger's most valuable column, because
it is the queue for everything after.

**Expected bin distribution:** mostly D0, with the C-vs-D pairing in D1 or
D2 and the causal-patch-vs-fat-geodesic pairing in D3. **Stated so it can
fail.**

**Falsifier:** if many pairings have computable `Delta` already, the plan
is mis-shaped and should pivot to measurement rather than formulation. If
*no* pairing has one, including C-vs-D, the programme has no empirical
content at present and §5's whole-programme kill criterion applies.

### WP-3. Collapse against decoherence in the curvature power spectrum

**The centrepiece.** Run 01's open question 4, and on its evidence the only
place in the entire map where a genuinely conflicting pair of approaches to
definiteness could be settled observationally rather than argued.

**Establishes:** which of the two the data prefer, or that neither is
distinguishable. **Depends on:** WP-2 for the bin, job 003 for a common
parameterisation. **Data:** Planck `plik_lite` TT/TE/EE. **Maple:** job 003
(1 round trip). **Cost:** 2-3 runs plus ~30 core-hours.

Run 01 §2.3 records C and D as `non_competing` on scope but
`genuine_conflict` in a predicted observable: both modify the curvature
power spectrum with different functional forms. **No paper was found that
sets the two predictions against each other and asks which the data
prefer.** Run 02's C-4 does not touch this verdict, so it stands.

The method: job 003 reduces both corrections to one parameterisation
`P(k) = P_0(k)[1 + f(k/k_*; theta)]`, with the CSL branch structure
(Martin, Vennin & Peter 2012: one scale-invariant branch, one of spectral
index 4; Martin & Vennin 2020: index -9 in one regime) as the validation
target. Then one joint fit containing both forms, nested so they can be
compared.

**Report the free-parameter count on both sides, always.** The sibling
repository's Run 01 quoted a Bayes factor with null parameter counts and
its validator now catches that; the same discipline binds here. A
comparison statistic without both counts is recorded as uninterpretable.

**Expected bin:** D1 or D2. **Falsifier:** if the two forms cannot be
jointly parameterised, or if no parameter values let the data distinguish
them, that is a D3 or D4 verdict on the field's one empirically live
conflict. **That is a major result either way and the package does not
need the model comparison to come out any particular way.**

### WP-4. Recompute the Martin-Vennin cosmological constraint

**Establishes:** the number that does not currently exist in print.
**Depends on:** WP-3's pipeline. **Data:** Planck. **Maple:** none beyond
job 003. **Cost:** 1-2 runs.

Run 02 confirmed at primary-source level that Martin & Vennin
(arXiv:1906.04405) state **no numerical bound on the CSL parameter**: the
cosmological constraint is analytic in `gamma` with the numerical content
in a figure. The figure sometimes quoted as their bound,
`lambda << 5.6e-90 s^-1`, appears only in Gundhi et al.'s introduction as
*their rendering*, against Gundhi et al.'s own `lambda <~ 1e7 s^-1`.

So reanalysis here means producing the number, which also resolves the
provenance problem properly rather than re-tagging it.

**Expected:** a bound somewhere between the two printed figures.
**Falsifier:** reproducing neither camp's figure means the pipeline is
wrong; reproducing one vindicates that camp's operator choice on its own
terms, which is the root of the whole disagreement.

**What this cannot settle, and must not claim to:** which collapse operator
is correct. Run 01 established that the entire spread between the camps
comes from that choice, and no CMB measurement selects it.

### WP-5. The measure literature against the floor

**Establishes:** whether any measure-predicted signal clears
`sigma_floor`. **Depends on:** job 002. **Data:** Planck low-`l`.
**Maple:** job 002. **Cost:** 1 run.

Run 01 §2.3 records the causal-patch and fat-geodesic measures predicting a
one-point expectation of the gauge-invariant Newtonian potential and a
three-point contribution, with forms that differ, **both well within cosmic
variance**. That is cited, not computed here. Job 002 makes it ours.

**Expected bin:** D3. **Falsifier, and it matters:** if any
measure-predicted signal exceeds the floor, the measure literature has a
live observational question, this package's expectation is wrong, and the
measure branch moves from closed to active. **The package is written to
find that out, not to confirm D3.**

### WP-6. Higher-order correlators as the quantum-classical discriminator

**Establishes:** whether the quantum-versus-classical-ensemble question for
perturbations is decidable at all. **Depends on:** WP-2, job 001.
**Data:** Planck non-Gaussianity. **Maple:** job 001 (already queued).
**Cost:** 2 runs.

Run 01 found the sharpest statement in the field: Martin & Vennin 2016
(arXiv:1510.04038) show a zero-discord, purely classically correlated state
reproduces the power spectrum **exactly**, and any two-point correlator on
super-Hubble scales exactly, **regardless of squeezing** — so squeezing
only affects higher-order correlators.

That localises the question precisely. If the quantum state is
distinguishable from a classical ensemble at all, it is in the higher-order
statistics and nowhere else. So: compute the discriminating correlator's
amplitude, and compare against Planck's `f_NL` constraints and the floor.

Job 001 feeds this by settling whether the standard truncation is even a
legitimate state, which is Hsiang & Hu's live and unanswered objection.

**Expected bin:** D2 or D3. **Falsifier:** if the discriminating amplitude
clears current constraints, this is D1 and becomes the plan's new
centrepiece.

### WP-7. The two literature reads that gate everything symbolic

**Establishes:** whether the clock trade-off is well posed, and whether the
observer's energy bound is derivable. **Depends on:** nothing. **Data:**
none. **Maple:** none. **Cost:** 1 run, cheap.

Two reads, both named by the existing runs:

1. `arXiv:1912.00033` §V and §III.2 — the trinity equivalence's actual
   spectral hypothesis, settling Run 02's P-1. If the condition is
   non-degeneracy and continuity rather than boundedness, Run 01's Part
   3.6 trade-off is one run's inference with no published link, and no
   symbolic work on it is justified.
2. `arXiv:2601.07910` (Klinger, Kudler-Flam & Satishchandran) — **the
   single highest-value unretrieved item in Run 01**, reported to argue
   that proper accounting of the observer's energy implies Type II_1. If
   so, the energy bound is derived rather than imposed, and the de Sitter
   entropy normalisation is physics rather than a modelling choice.

Do this early. It is the cheapest package in the plan and it decides
whether a whole branch exists.

### WP-8. Write-ups

**Establishes:** nothing; it is the obligation. **Depends on:** any package
producing an answer. **Cost:** 0.5 run per answer.

One document per answer or partial answer, in `findings/`, written **when
that answer lands**, not batched at the end.

Rules, binding:

- Explain the actual mechanism in literal terms, at a level a
  late-highschooler can follow.
- **No invented analogies**, and specifically none of the
  comparison-to-everyday-objects register. An analogy is permitted only
  where established physics exposition already uses that specific one —
  curved fabric for spacetime is the canonical case — and only after the
  literal mechanism has been stated.
- If a step cannot be explained literally, **say the step is not yet
  understood well enough to explain.** That is a finding and it goes in
  the document.
- **The hazard specific to this repository:** most of its subject matter is
  interpretive, and interpretive material is exactly what fluent prose can
  fake. A write-up that reads clearly while saying nothing checkable is
  worse than none. Every write-up names the number, the dataset or the
  computation its claim rests on; where there is none, it says so in the
  first paragraph.

---

## 5. Kill criteria

Stated in advance, so stopping is a decision the plan already made.

**Branch kills:**

- **The clock / algebraic branch dies** if WP-7 confirms P-1. The trade-off
  then has no published basis, is one run's inference, and gets no Maple
  time until someone states it in print. Record it as an open question and
  stop.
- **The measure branch dies** if WP-5 shows every measure-predicted signal
  below the floor. Report the computation, close the questions, write them
  up, and do not keep working them.
- **WP-3 dies** if the two correction forms cannot be jointly
  parameterised and no data distinguishes them. Report D3 or D4 and stop.
- **WP-6 dies** if the discriminating correlator is below the floor.

**Whole-programme kill.** If WP-2 finds that **no** question in the map can
be moved out of D0 at reasonable cost — including C-versus-D, the one
pairing with a genuinely conflicting observable — then the cosmological
observer problem has no current empirical content, and the honest output is
to say exactly that, with the ledger as evidence, and stop. **The plan does
not expect this and does not want it, and must not be run in a way that
manufactures work to avoid it.**

**An anti-kill criterion**, which matters as much. A question landing in D3
or D4 is **not** a reason to keep working it in a different vocabulary. The
temptation in this field is to reformulate an undecidable question until it
sounds decidable. A D3 verdict is a result: it gets computed, written up,
and closed.

---

## 6. What to do with the undecidable bins

**D3, floor-limited.** The strongest possible outcome short of a
measurement, because it is a computed impossibility rather than an absence
of effort. Record `Delta`, `sigma_floor` and the ratio; write it up; close
the question. Worth publishing on its own: "this distinction is below the
one-sky floor by a factor of N" is a real contribution, and the field
currently asserts such things without the number.

**D4, no differing observable.** State the identity of predictions
explicitly, with the sources. Then one of two honest readings, and the
ledger must say which:

1. The dispute is about **explanation, not prediction**. Legitimate, and
   not settled by data. Say so, say what non-empirical criterion its
   proponents use (consistency, derivability, parsimony), and stop
   pretending data bears on it. Run 01 found a worked example: Everettian
   decision theory versus Zurek's envariance give identical Born
   probabilities from different premises, and the scaffold **cannot see**
   the disagreement at all.
2. **Nobody has looked for the observable.** Different, and it stays open.
   The test for which: has anyone tried and failed, or has nobody tried?

**D0, not yet posed.** Not an undecidable bin and must never be reported as
one. The ledger's "what would make `Delta` computable" column is the
research queue, ordered by cost. A D0 question with a cheap route to
formulation is the most valuable thing in this plan.

---

## 7. Sequence and round-trip budget

| Day | Maple queue | Agent work |
| --- | --- | --- |
| 1 | jobs 001, 002 | WP-0, WP-1, WP-7 in parallel |
| 2 | job 003 | WP-2 begins once 002 returns |
| 3 | — | WP-5 (needs 002), WP-3 begins |
| 4+ | as needed | WP-3, WP-4, WP-6 |

**4 Maple round trips** in total: 001 and 002 together on day one, 003 on
day two, one spare. Nothing blocks on more than one per day.

WP-0 and WP-1 gate anything that reads the map. WP-7 gates the symbolic
branch and is cheap, so it goes early. WP-2 is the first real result.

---

## 8. What this plan does not cover

- **Laboratory collapse-model bounds.** Named in the brief as a candidate.
  Excluded: they constrain the same parameters as WP-4 but the apparatus is
  a different literature and a different expertise, and WP-4's CMB route
  reaches the same question. Revisit if WP-4 produces a bound competitive
  with the laboratory one.
- **Large-angle CMB anomalies.** Named in the brief, and deliberately
  deferred to a later run rather than dropped. They are a genuine
  data-first entry point, but Run 01 found **no** approach in the map that
  predicts them, so there is no `Delta` to triage. The honest sequence is
  WP-2 first; if any position turns out to bear on the anomalies, they
  become a package.
- **The single-sky problem as a conceptual question.** Run 01 searched
  twice and found no literature treating cosmic variance as continuous with
  the measure problem, and rejected it as a cluster member on retrieval.
  This plan uses cosmic variance **as an instrument** (job 002) and does not
  reopen the conceptual identification. Run 01's open question 9 states
  what would overturn that.
- **Landauer-type limits on record-keeping.** Run 01 recorded a clean
  negative: nothing exists that does the job. No package, because there is
  no literature to reanalyse. The citation search that would overturn it is
  in Run 01's Part 6.
- **Forecasts for future experiments.** Used only to set D2 thresholds,
  never to conclude anything.
- **Anything in the sibling repository.** Timescape has its own plan.
- **Extensions or new proposals.** This plan triages and measures. It
  proposes no new account of the observer, and no package is permitted to
  produce one as a side effect; if one appears, it goes in an open-questions
  list for a later run to assess, as Run 01 did with its own two candidate
  syntheses.

---

## 9. Honest statement of this plan's own bias risk

Written by a session forked from the one that wrote the seed documents,
the protocol, and the validators, and that verified both runs. So:

- The triage criterion in §1 was built by someone who had already read Run
  01's finding that the causal-patch/fat-geodesic conflict sits below
  cosmic variance. The criterion may be shaped to fit that one example.
  **A reviewer should check whether the three-number test is natural or
  reverse-engineered.**
- The expected bins in §4 are this author's guesses and are recorded so
  they can be scored against outcomes. If most come out right, that is
  weak evidence the plan is sound and equally weak evidence it was
  tailored. If several come out wrong, the plan was at least not fitted.
- WP-2 should ideally be run on a fresh context, not a fork of this one,
  for the same reason the adversary is. That is a recommendation this plan
  makes against itself.
