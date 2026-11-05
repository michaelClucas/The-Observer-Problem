# Standing loop: unattended research day

This is not a run prompt. It does not produce a numbered run under `runs/`,
though it may prepare one. It is the standing brief for a session that works
this repository's research plan for a whole day with nobody answering
questions.

Read `docs/RESEARCH-PLAN.md` first. It is the authority on what the work is.
This file is the authority on how to proceed when you are alone.

---

## The one hard rule

**Nobody will answer you today.** A question that stops your work costs the
whole day. So you never stop to ask. Every block has a route around it,
written below. Take the route, record the block, keep working.

The corollary is the rule that matters more: **you never route around a
block by inventing the answer.** A blocked computation stays blocked and
gets filed. It does not get estimated, approximated in your head, or
replaced by a plausible number. A result you cannot compute today is worth
exactly nothing to this repository; a result you fabricated today is worth
less than nothing, because it will be built on.

---

## Standing constraints, from the overseer

These came with the research plan and do not change.

1. **Do not assume any conclusions.** This is an experiment, not an attempt
   to show that the observer problem is empirically empty, nor that it is
   rich. Run 01's finding that 48% of slot entries are empty or misfit is a
   fact about what approaches **say**, not a fact about what is
   **measurable**. The plan's own §9 states its bias risk; read it.
2. **Follow the data, not the consensus.** Where an approach is widely held
   and makes no prediction, that is a fact about the approach. Where an
   unfashionable approach makes a computable one, it gets the same
   treatment. Ranking by citation count is not triage.
3. **Symbolic calculation happens in Maple**, on another machine, one round
   trip per day. See the queue protocol below.
4. **Proofs are verified in Lean**, and only if a proof-shaped claim
   appears. Do not start a Lean project speculatively. `docs/RESEARCH-PLAN.md`
   §3 holds the trigger.
5. **Data-driven.** Reanalyse the raw public data. A number taken from a
   paper's abstract is a `[LEAD]`, not a result.
6. **Any answer gets a natural-language write-up** a late-highschooler can
   follow, under `explain/`. No AI-slop analogies. An analogy of the
   fabric-and-gravity kind is allowed where the mechanism genuinely needs
   one; a decorative comparison is not.

---

## The cycle

You work in cycles. One cycle is one slice of one work package, ending in a
commit. Repeat until a stop condition fires.

### Step 1. Sync and ingest

```
git fetch origin
git merge origin/main        # on your day branch
gh issue list --label "maple:done" --state all --limit 30
gh issue list --label "maple:queued"
gh issue list --label "maple:blocked"
```

Any `maple:done` issue whose results landed since your last cycle unblocks
the package that filed it. **Resuming blocked work takes priority over
starting new work**, because a returned Maple result is the scarcest thing
in this process: one per day per job, and the queue goes idle if you do not
consume it.

Read the result from `maple/results/NNN-<slug>/RESULT.txt`, not from the
issue comment. The comment is a notification; the committed file is the
record. If they disagree, the file wins and you note the disagreement.

### Step 2. Pick the work

**Your scope is the empirical branch: four packages.** The research plan has
nine; the rest are out of scope for this loop and the reasons are below.
Work these, in this order, taking the first that is unblocked and
unfinished:

| | Package | Why it is in scope |
|---|---|---|
| 1 | **WP-7**, the two literature reads | Cheapest package in the plan and it decides whether the symbolic branch exists at all. Two reads: `arXiv:1912.00033` §V and §III.2 for the trinity equivalence's actual spectral hypothesis, and `arXiv:2601.07910` for whether the observer's energy bound is derived rather than imposed. Do this first. |
| 2 | **WP-6**, higher-order correlators | Maple job 001 is queued. Run 01 localised the question precisely: a zero-discord classically correlated state reproduces the power spectrum and every super-Hubble two-point correlator exactly, regardless of squeezing, so if the quantum state is distinguishable at all it is in the higher-order statistics and nowhere else. Compute the discriminating amplitude against Planck `f_NL` and the floor. |
| 3 | **WP-5**, measure predictions against the floor | Maple job 002 is queued. Cheap, and it either closes the measure branch or opens a live observational question. |
| 4 | **WP-3**, then **WP-4** | WP-3 is the plan's centrepiece and the one place in the map where a genuinely conflicting pair could be settled by data rather than argued. WP-4 then produces the CSL cosmological bound, which **does not exist in print**: Martin and Vennin state no numerical bound, the figure usually attributed to them is Gundhi et al.'s rendering, and it sits 97 orders of magnitude from Gundhi et al.'s own. Producing the number settles a provenance mess as well as a physics question. |

WP-3 needs job 003 and roughly 30 core-hours; it will span days. File job
003 early so the round trips overlap the cheap packages.

**On WP-3, report the free-parameter count on both sides of every
comparison statistic, always.** A comparison statistic without both counts
is recorded as uninterpretable, not as a weak result. The sibling repository
quoted a Bayes factor with null counts and its validator now catches that;
the same discipline binds here and no validator here will catch it for you.

### Out of scope, and why

Do not work these. If you believe one has become necessary, write it to
`OPEN-QUESTIONS.md` with the argument and carry on with what is in scope.

- **WP-1** (replicate Run 01 on a fresh context). The point of it is that
  the replication must not have seen the seed. You hold a checkout
  containing `docs/approach-clusters.md`, so you cannot run it honestly.
- **WP-0** (apply Run 02's corrections, migrate to schema v1). It is
  hygiene on a map whose research value is itself the open question, and a
  day spent on it buys no physics. The corrections stay recorded in Run 02
  where a later run can apply them.
- **WP-2** (build the decidability ledger over all 34 pairings and 12 open
  questions). **This is the largest slop risk in this repository.** Its
  expected output is a long document saying that almost everything is
  undecidable, and producing it is a prose-generating exercise an agent with
  a day to fill will do enthusiastically and uselessly. Instead: **record
  the bin for only the pairings the four in-scope packages actually touch**,
  in the package's own output. That satisfies every dependency WP-3 and WP-6
  have on WP-2 and skips the survey.
- **WP-8** (write-ups) applies only to results you actually obtained. See
  the write-ups section.

**When all four in-scope packages are finished or blocked, stop.** Do not
promote an out-of-scope package to fill the day. That instruction is the
main thing this scoping is for.

Every conclusion you reach is `provisional on WP-1`, including in the commit
message. If the replication later produces a different cluster set, work
built on Run 01's structure has to be findable.

### Step 3. Do the work

Rules that apply to everything you produce:

- **Every number in prose comes from a committed, runnable script or from a
  Maple `RESULT.txt`.** Scripts go in `verify/<topic>.py`, exit non-zero on
  failure, and are run before you commit them. No exceptions, including for
  arithmetic you are confident about. The "97 orders of magnitude" claim in
  Run 01 was tagged `[SOURCED]` and is an `[INFERENCE]`; that is the whole
  problem in one line.
- **Every dataset gets `data/NNN-<dataset>/` with `SOURCE.md`, `fetch.sh`,
  `MANIFEST.sha256` and `cuts.md`** before any analysis touches it. The cuts
  file is written before you see the result, not after.
- **Confidence tags on every claim**: `[SOURCED]` means you fetched and read
  the source; `[LEAD]` means you have a pointer you did not verify;
  `[INFERENCE]` means you derived it and must name the premises;
  `[UNKNOWN]` means you do not know. A citation you did not fetch is never
  `[SOURCED]`.
- **Schema v1 discipline.** `sources` supports a positive claim;
  `established_by` records what you read to establish an absence, and its
  `read` field has to say what was read. Where the read was truncated the
  entry is `LEAD`, not `SOURCED` — an emptiness-so-far is not a sourced
  absence. `denied` is a doctrine someone argued for and takes `sources`;
  `empty` is a silence and takes `established_by`. `unengaged` is for two
  positions that look incompatible where no source puts them to each other,
  and it is a finding about the field, not a weaker conflict.
- **Record the negative.** A pairing you could not make computable, a
  literature read that turned up nothing, an approach you abandoned after an
  hour: all of it goes in the day log. A day's work that reports only what
  succeeded is a day's work nobody can trust.

### Step 4. Run the validator if you touched run output

```
python protocol/validate.py runs/<run-dir>/OUTPUT.json
```

It reports **112 schema gaps and 54 violations** against Run 01 as it
stands. Those are WP-0's to fix and WP-0 is out of your scope, so that
baseline does not change today. What binds you: **any run output you
produce must validate clean at schema v1**, and you say so in the log with
the command and its output. Your packages mostly produce analysis under
`verify/` and `data/` rather than run output, in which case say that.

**Never change a rule in `protocol/validate.py` to make a hit disappear.**
If you believe a rule is wrong, the finding is "rule N is wrong, here is the
hit it produced and why the run is right" — written into the day log and
left for the overseer. Four of the six violation classes that file finds were
missed by a careful adversary with a full budget, so the prior is that a hit
is real.

### Step 5. Commit

One commit per cycle, on the day branch, message naming the package:

```
WP-2: decidability ledger, pairings 1-12, sigma_floor pending job 002
```

Push every cycle. An unpushed day is a lost day if the session dies.

### Step 6. Log

Append to `logs/YYYY-MM-DD.md` — cycle number, package, what you did, what
you concluded, what blocked, what you filed. Append only; never rewrite an
earlier cycle's entry. If a later cycle overturns an earlier one, the later
entry says so.

Then go to step 1.

---

## Blocks, and the route around each

### Block: it needs a symbolic computation

File a Maple job. This is the whole reason the queue exists.

1. Write `maple/jobs/NNN-<slug>/JOB.md` and `job.mpl`, following
   `maple/README.md`. `JOB.md` **must** state the expected output form. A
   job without one is refused by the runner, and rightly: at a day's latency
   a wrong answer that arrives looking like a right one costs a week.
2. Write `crosscheck.py` where a numerical check is possible. A Maple result
   with no independent check is one machine's word.
3. Commit and push. Note the sha.
4. Open the issue with the `maple-job` template, label `maple:queued`,
   naming the job directory and **that sha**. The spec never goes in the
   issue body.
5. Move to the next package. **Do not wait.** Do not estimate what Maple
   would have said. Do not substitute sympy for a job you have filed — a
   cross-check is a cross-check, not a result.

Ceiling: **three open `maple:queued` issues**. The plan budgets four round
trips in total and the runner does one pass a day; a longer queue is a
backlog pretending to be progress. At three, stop filing and work something
unblocked.

If a filed job's spec turns out wrong, **do not edit the job directory** —
the runner checks out a sha and your edit is invisible to it. Comment on the
issue saying the spec is wrong and why, label it `maple:blocked`, then file a
new numbered job directory and a new issue. You cannot close issues; the
runner closes them, and only with a committed results directory.

### Block: it needs a decision only the overseer can make

Write it to `OPEN-QUESTIONS.md`: the question, the options, the consequence
of each, and your recommendation. Then **take the reversible default** and
carry on, marking the output `provisional on Q-n`. A choice you can undo
tomorrow is not worth a day of idleness. A choice you cannot undo — deleting
data, rewriting history, changing a frozen prompt — is not a default and you
stop that branch instead.

### Block: it needs a paper you cannot fetch

Record the claim as `[LEAD]` with the locator and what you needed from it.
Do not infer the content from the title, the abstract, or what the citing
paper says it says. Run 02's sharpest finding was a conflict sourced to a
paper whose own introduction says the two proposals agree, which is exactly
what reading-about rather than reading produces.

### Block: it needs a proof

If a claim is proof-shaped — a statement that something follows necessarily,
not that it fits — write the statement precisely under the Lean trigger in
`docs/RESEARCH-PLAN.md` §3, with the hypotheses explicit, and record it in
the day log. Starting the Lean project is a separate decision and not a
default. Most of what looks proof-shaped here is a `SCHEME` or a
`POSTULATE` and the trigger does not fire.

### Block: a pairing lands in D3 or D4

That is a result. Compute it, write it up, close it.

**Do not reformulate.** The plan's anti-kill criterion is explicit about
this: the temptation in this field is to restate an undecidable question
until it sounds decidable, and a D3 verdict reached honestly is worth more
than a D1 verdict reached by moving the goalposts. The ledger's most
valuable column is "what would make this computable", and filling it is the
correct output for a D0 — not finding a vocabulary in which the question
already sounds answered.

### Block: a kill criterion fired

Stop that branch. The branch kills and the whole-programme kill are in
`docs/RESEARCH-PLAN.md` §5. If one fires:

1. Write the evidence up immediately, in the clearest form you can, while
   you still have the context.
2. Say in the day log that it fired, which one, and on what evidence.
3. If it is the **whole-programme** kill — WP-2 finds no question in the map
   can be moved out of D0 at reasonable cost, C-versus-D included — stop the
   day there and leave the write-up as the day's output. The plan says in
   terms that it does not expect this, does not want it, and **must not be
   run in a way that manufactures work to avoid it.** That instruction binds
   you specifically, because manufacturing work is the easiest thing in the
   world for a session with a day to fill.

---

## What you must not do

- **Do not push to `main`** or merge your own PR. You work on
  `research/auto-YYYY-MM-DD`, one PR for the day, updated as you go.
- **Do not rewrite history.** No force-push, no amend of a pushed commit, no
  rebase of the day branch.
- **Do not edit anything under `runs/01-*` or `runs/02-*`.** Runs are
  append-only, including runs that are wrong. WP-0's corrections are a new
  run, not an edit of an old one.
- **Do not edit `prompts/01-consolidate-approaches.md` or
  `prompts/02-adversary.md`.** They are frozen; a run's `prompt_commit` has
  to stay resolvable and a one-character change breaks the sha. That is also
  why neither carries a deprecation banner.
- **Do not relax a protocol rule, a validator rule, or a kill criterion.**
  Argue against it in the log if you think it is wrong.
- **Do not close a Maple issue**, and do not write anything under
  `maple/results/`. That is the runner's half of the contract.
- **Do not start a second long-running agent** against this repository. One
  session, one branch, one day. Two writers on the same files produce a diff
  nobody can review.
- **Do not fill a day.** If you run out of legitimate work, stop. See below.

---

## Stop conditions

Stop and write the day up when any of these holds:

1. **Every in-scope package is finished or blocked** — blocked on a Maple
   round trip, on WP-1, or on a question in `OPEN-QUESTIONS.md` whose
   reversible default you have already taken as far as it goes. Four
   packages is the whole day's scope and finishing them early is a good
   outcome, not an idle one.
2. **A branch kill or the whole-programme kill criterion fired.** The
   measure branch dying on WP-5, or WP-6's discriminating correlator
   landing below the floor, each closes a package for good: report the
   computation, write it up, and do not keep working it.
3. **You have spent the day's budget**: roughly 12 cycles, or any single
   package past 3 cycles with nothing committed. A package that cannot
   produce a commit in three cycles is mis-specified; say so in the log and
   move on.
4. **You caught yourself reformulating.** If you are restating a question in
   new vocabulary because the old vocabulary gave an answer you did not
   want, that is the end of the day's useful work. Log it and stop.

On stopping, write `logs/YYYY-MM-DD-STATUS.md`:

- which packages advanced, and to what state
- the decidability ledger's bin counts as they now stand, with the previous
  counts beside them
- which kill criteria were tested and what the evidence was
- every Maple issue filed, with its number and what it blocks
- every `OPEN-QUESTIONS.md` entry added, with the default you took
- what tomorrow's first cycle should pick up, and why
- **what you would have done differently with one question answered.** This
  is the most useful line in the file for the overseer.

Then update the day's PR body with that status and stop. Do not merge it.

---

## Write-ups

If the day settles a pairing or an open question, it gets
`explain/NNN-<slug>.md` written for a late-highschooler: what was asked,
what was done, what came out, and what it does and does not settle. Plain
words for the mechanism. No analogy unless the mechanism needs one, and then
one that carries real structure rather than atmosphere.

A D3 or D4 verdict gets a write-up too, and it is the harder one to write
honestly: "here is a question about the universe that nobody can currently
answer, and here is exactly what you would need to answer it" is a real
result and should read like one.

The write-up is not a summary of your work. It is an explanation of the
result to somebody who will never read your work.

---

## Why this prompt is shaped like this

Two failure modes have already happened in this repository and this file is
mostly about them.

Run 01's schema had no legal form for a sourced absence, so 109 entries sat
in violation of the repository's own rules while looking like ordinary
output. Nothing caught it, and nothing caught 54 further violations, until a
checker was written — and a careful adversary with a full budget had already
missed four of their six classes. Hence: every number from a committed
script, and the validator runs before the commit.

And a session told not to read a file, while holding a checkout containing
it, cannot honestly claim it did not. Hence WP-1 is not yours, and hence the
Maple spec lives at a sha rather than in an editable issue body. Where the
protocol depends on what you will not do, it is weaker than where it depends
on what you cannot do.
