# How strong can a collapse model be, if the early universe looked the way it did?

Evidence: `verify/csl_cosmological_bound.py` (5 of 5 checks pass) and
`findings/002-wp4-csl-cosmological-bound.md`. Produced 2026-11-05 by work
package WP-4.

## What was asked

There is a family of theories called **CSL**, for Continuous Spontaneous
Localization. They are attempts to fix something people find unsatisfying
about ordinary quantum mechanics.

In ordinary quantum mechanics there are two separate rules. Most of the
time, a system's state spreads out smoothly according to one equation. But
when you measure the system, the state stops spreading and jumps to a
single definite outcome, and that jump follows a different rule. Nothing in
the theory says what counts as a measurement or when the switch happens.

CSL replaces both rules with one. It adds a small random term to the
equation so that states never spread out very far in the first place: any
state that starts to develop into a spread-out mixture of different
positions gets continuously nudged back toward one position. For a single
atom the nudging is far too weak to notice. For anything the size of a
dust grain it is fast enough that you never see the spread. So definite
outcomes happen on their own, with no separate measurement rule.

The nudging has a strength, written `lambda`, measured in events per
second. It also has a length, written `rc`, which sets how far apart two
positions have to be before the theory treats them as genuinely different
places. These two numbers are the whole theory. **If `lambda` is zero you
get ordinary quantum mechanics back.** If `lambda` is large, collapse is
violent and would show up in experiments.

So the question is: how large can `lambda` be?

Laboratory experiments answer this one way. They watch for the tiny heating
and jitter that the random nudging would cause in very cold, very isolated
equipment, and find nothing, which rules out large `lambda`. The surviving
range they allow is roughly `lambda` between `1e-18` and `1e-10` per
second, with `rc` somewhere between a hundredth of a micrometre and a tenth
of a millimetre.

The early universe answers it another way, and that is this write-up.

## Why the early universe has anything to say

The cosmic microwave background is light left over from when the universe
was about 380,000 years old. It is almost perfectly uniform, but not quite:
it is slightly hotter in some directions and slightly colder in others, by
about one part in a hundred thousand. Those tiny differences grew into
every galaxy.

The standard account of where they came from is that they started as
quantum fluctuations during **inflation**, a brief period of very fast
expansion in the universe's first fraction of a second. The expansion
stretched microscopic quantum ripples up to the size of the visible
universe.

Two features of that picture matter here.

First, **the ripples are quantum**, so a theory that changes how quantum
states behave changes them. CSL adds random nudging to every quantum state,
including these.

Second, **we know the answer in detail.** The sizes of the hot and cold
patches have been measured very precisely, and they come out almost the
same at every angular scale. "Almost the same at every scale" is called a
**scale-invariant** spectrum, and it is what inflation predicts.

Put those together and you get a constraint. CSL's nudging adds an extra
contribution to the ripples. That extra contribution is **not** the same at
every scale: it depends on scale as a power law, and the power is not zero.
So if the nudging were strong, the measured spectrum would be tilted away
from scale invariance in a way that would have been obvious. It is not. So
the nudging was weak, and that puts a ceiling on `lambda`.

## What was actually done here, and what was not

Two physicists, Jérôme Martin and Vincent Vennin, worked this out in a 2020
paper. They wrote down how a CSL ripple spectrum depends on `lambda` and
`rc`, and they derived the ceiling.

But they published the ceiling as a **formula**, not as a number, and drew
the result as a figure. Other papers then quoted a number for it:
`lambda` must be less than about `5.6e-90` per second. That is the number
that circulates.

Tracing it back, that number appears first in the introduction of a
different paper, by Gundhi and collaborators, presented as their rendering
of Martin and Vennin's result. Martin and Vennin themselves never write it
down. So the number everyone quotes has no primary source.

**What this work did was evaluate Martin and Vennin's own formula, at the
parameter values stated in their own figure caption, and get the number
out.** No new physics. No reading values off a printed graph. Arithmetic on
a published expression, in a script anyone can run.

Two things came out.

## Result one: the circulating number is arithmetically right

Evaluating the formula gives

```
lambda  less than  5.566e-90 per second
```

against the quoted `5.6e-90`. That is a match to better than one percent.

So the number that circulates is not a mistake and not an invention. It is
a correct evaluation of a real formula. That settles a question this
research programme had flagged as unresolved: where the figure came from.

It also means the calculation here is trustworthy, because reproducing
somebody else's number from their own starting point is how you check that
you have not misunderstood their starting point.

## Result two: it is the wrong one of two formulas

Martin and Vennin do not give one ceiling. They give **two**, with a rule
for choosing between them.

The reason there are two is physical and worth following, because it is the
whole point.

CSL's nudging only acts on differences in position bigger than the length
`rc`. A ripple in the early universe starts out tiny and gets stretched by
the expansion. So early on, a given ripple is smaller than `rc` and the
nudging ignores it. Later, after enough stretching, it is bigger than `rc`
and the nudging starts acting on it.

**When** that switch-over happens decides which formula applies. If the
ripple grows past `rc` while inflation is still going on, you use the first
formula. If it only grows past `rc` later, after inflation has ended and
the universe has settled into its next phase, you use the second. The two
give different answers because the universe is expanding at very different
rates in the two phases.

Checking the condition at the values in the figure caption: the switch-over
happens **after** inflation ends. So the second formula applies. The
circulating number comes from the first.

Using the formula that applies:

```
lambda  less than  2.47e-86 per second
```

That is about 3.6 orders of magnitude, a factor of about four thousand,
weaker than the circulating number.

## What that does and does not change

It does not change Martin and Vennin's conclusion at all.

Their point was that the ceiling from the early universe and the range
allowed by laboratory experiments **do not overlap**. The laboratory range
starts at about `1e-18` per second. The corrected ceiling is `2.47e-86`.
That is sixty-eight orders of magnitude below the bottom of the laboratory
range. The gap was enormous before and it is still enormous.

What it changes is the number. And the number is what this work package
existed to produce, because the number is what anyone comparing CSL against
a different collapse model has to compare against.

There is a further reason the number needs an `rc` attached to it. The
boundary between the two formulas, expressed as a value of `rc`, falls at
about `4.2e-8` metres — **inside** the range of `rc` that laboratory
experiments still allow. So for some allowed values of `rc` the first
formula is right and for others the second is, and there is no single
number that is "the early-universe ceiling on CSL" without saying which
`rc` you mean. That is not anybody's oversight. It is a real feature of the
physics, and it is why Martin and Vennin drew a figure instead of quoting a
number.

## What this cannot settle

A lot, and it matters.

The same Martin and Vennin paper is in disagreement with the Gundhi paper
about something much larger than a factor of four thousand. Gundhi and
collaborators get a ceiling of around `1e7` per second — about ninety-three
orders of magnitude weaker, so weak that the early universe would be
telling us nothing that the laboratory has not already told us better.

That disagreement is **not** about arithmetic. Both sides calculate
correctly from their own starting points; this work confirms one side's
arithmetic directly. The disagreement is about a choice made before any
calculating starts: **what, exactly, the random nudging acts on.** CSL says
collapse is driven by mass density, but in a universe where the density is
itself a fluctuating quantum field there is more than one reasonable way to
write that down, and the two camps write it down differently. Gundhi and
collaborators additionally argue that Martin and Vennin's version is
internally inconsistent as a calculation, which is an argument about
mathematics and not about data.

**No measurement of the sky distinguishes the two choices.** That is the
honest statement and it is the one this programme's earlier work had already
reached by reading the literature. Nothing computed today changes it. This
work produced a number inside one camp's framework; it did not and cannot
say that framework is the right one.

## What is still open

- Everything here is **provisional on WP-1**, a planned replication of this
  programme's earlier mapping work on a fresh start. If that replication
  comes out differently, conclusions built on the earlier map have to be
  re-examined. This write-up's arithmetic would survive; its placement in
  the programme might not.
- The identification of the end-of-inflation expansion rate with the rate
  during inflation is an assumption. It is a very good one — they differ by
  a fraction of a percent — but the branch determination above turns on a
  factor of 2.4, not on orders of magnitude, so the margin is real and is
  recorded in the findings document rather than buried.
- Which collapse operator is correct remains open and is not the kind of
  thing the cosmic microwave background can answer.
