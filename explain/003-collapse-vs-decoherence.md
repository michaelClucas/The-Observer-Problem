# Two competing explanations, one sky: can the data tell them apart?

Evidence: `verify/wp3_nested_comparison.py`,
`findings/003-wp3-collapse-vs-decoherence.md`, and the data provenance in
`data/001-planck-2018-plik-lite/`. Produced 2026-11-05 by work package
WP-3.

## The question behind the question

Quantum mechanics has a gap in it. Most of the time a system's state
evolves smoothly and can describe several possibilities at once. But when
we look, we find one outcome, not several. The theory does not say how the
several become one.

For most of physics you can ignore this, because you can point at the
measuring apparatus and say the switch happens there. **In cosmology you
cannot.** The lumpiness of the universe — the pattern of slightly hotter
and colder patches in the cosmic microwave background, which grew into
galaxies — is supposed to have started as quantum fluctuations in the first
fraction of a second. There was no apparatus. There was no observer. And
yet we see one definite pattern on the sky, not a superposition of
patterns.

So cosmology forces the question. Two families of answers have been worked
out in enough detail to make predictions.

**Collapse models** say the gap is a real flaw and the theory needs fixing.
They add a small random term to the equations so that spread-out states
collapse to definite ones on their own, with no observer required. This
write-up calls that the **C** side.

**Decoherence** says there is no flaw. A quantum system is never really
isolated; it interacts with everything else, and that interaction destroys
the ability of the possibilities to interfere with each other, which is
what makes them behave like separate definite alternatives. This write-up
calls that the **D** side.

These are genuinely different claims about the world. The programme this
work belongs to had already found that they are stated in such different
mathematical languages that most comparisons between them are arguments
rather than measurements — **but that here, on this one question, both
sides make a prediction about the same measurable thing**: both change the
pattern of lumpiness, and they change it differently.

The programme had also found something more pointed. **No published paper
sets the two predictions against each other and asks which the data
prefer.** That is what this work did.

## What "changing the pattern differently" means

The lumpiness is described by a function of scale. Write `P(k)` for the
amount of lumpiness at a scale set by `k`: large `k` means small patches,
small `k` means large patches. Standard inflation predicts `P(k)` is
almost exactly the same at every scale, and measurement agrees.

Both the C and D sides predict a correction on top of that. Both
corrections have the same mathematical form:

```
P(k)  =  (standard P(k))  x  [ 1  +  A x (k / k_ref)^m ]
```

Two numbers describe each correction. **`A`** is how big it is, measured at
a reference scale. **`m`** is how its size changes with scale: `m = 0`
means the correction is the same at every scale, a negative `m` means it is
larger on large patches, a positive `m` means larger on small patches.

The two sides predict **different values of `m`**, and `m` is the part the
data can see cleanly, because the CMB measures about two decades of scale.
A correction growing as the scale shrinks looks nothing like one shrinking
as the scale shrinks, if you can see across a wide enough range.

The published predictions, read directly from the original papers:

- C side, if the collapse scale is reached during inflation: `m = -1`
- C side, if it is reached after inflation: `m = -10`
- C side, a different branch from an earlier paper: `m = +3`
- D side: `m` can be any integer, depending on how the quantum system
  couples to its surroundings. `m = 0` is the case of a heavy field as the
  surroundings.

## What was done

The three Planck measurements already working in this programme were used:
the main small-scale spectrum and two large-scale ones. The modified `P(k)`
was fed through a standard cosmology code to get a predicted sky, and
compared against the real data.

One technical fact made this cheap. The predicted sky depends on the
correction's size `A` in the simplest way possible: double `A` and the
change to the prediction doubles exactly. That was checked, not assumed —
it holds to about one part in ten million. Because of it, the entire
goodness-of-fit surface can be worked out from a handful of calculations
rather than by searching, which is why a result that would normally cost a
day of computing cost minutes.

Every choice about which data to use, which `m` values to test, and how to
handle the edges was written down and committed to the project's record
**before** the comparison was run. The order is in the version history.
That is deliberate: it is very easy, after seeing an answer, to convince
yourself you would have chosen the settings that produced it.

## Result one: most of the collapse predictions cannot be tested at all

And the reason is not the telescope.

Both corrections are **first-order** results: they are the leading term of
an expansion, and the expansion is only trustworthy while the correction
stays small compared to what it corrects. If the correction grows to be as
big as the thing it modifies, the calculation that produced it has stopped
being valid — not because the data disagrees, but because the mathematics
no longer applies.

Now take the `m = -10` branch. A correction growing as the tenth power of
the inverse scale grows very fast. Over the range the CMB covers, going
from the smallest patches to the largest multiplies the correction by about
`10^26`. So for the correction to stay small everywhere the CMB looks, its
size at the reference scale has to be below about `3 x 10^-26`.

That is not a limit the CMB imposes. **It is a limit the calculation
imposes on itself.** And it is so tiny that no measurement of the sky could
ever be the thing that rules this branch in or out. Every steeper branch is
worse.

So of the three published collapse predictions, **one is testable against
the CMB**: the `m = -1` branch, whose own validity limit is about
`2.8 x 10^-3`. The `m = +3` branch survives too, at about `1.6 x 10^-2`.

This is worth being clear about, because it is the kind of result that is
easy to state misleadingly. It does **not** mean the `m = -10` branch is
wrong. It means that if that branch is what happens, its effect on the CMB
is far too small to see, and a first-order calculation is the wrong tool
for asking anything else about it.

## Result two: where the data can speak, it separates the two cleanly

For every remaining pair of predictions — one C value of `m` against one D
value — the question is whether the data can tell them apart, or whether a
bit more of one looks the same as a bit less of the other.

That has a precise answer: fit both corrections at once and ask how
strongly their two sizes trade off against each other. If they trade off
perfectly, the shapes are indistinguishable and no amount of data helps. If
they barely trade off, the shapes are distinct and the data is choosing
between them.

**Every admissible pair came out separable.** The trade-off ranges from
very weak — for `m = -1` against `m = +4`, almost none at all — to strong
but still incomplete for the closest pair, `m = +3` against `m = +2`, which
is reported as marginal rather than rounded in either direction. Adjacent
powers over two decades of scale are the hardest case, and that is where
the one marginal entry sits, which is what you would expect.

So **the data does bear on this disagreement.** That is the answer to the
question Run 01 said nobody had asked.

## Result three, and the useful one: the calculation is the bottleneck

For the one collapse branch the CMB can address, two numbers turn out to be
about the same size:

- the limit from the calculation's own validity: about `2.8 x 10^-3`
- what Planck can currently measure: about `1.0 x 10^-3`

A factor of three apart. The data has just barely enough reach to probe the
region where the prediction is still trustworthy.

That means something concrete for anyone continuing this. **Better data
will not help much.** Push harder on this comparison — more sky, lower
noise, a future experiment — and you run out of theory before you run out
of measurement. The next real gain is a second-order calculation of the
correction, which is work with a pen, not with a telescope.

Finding that out is more useful than the limit itself, and it was not
something anyone had written down.

## What is still open, and it is a lot

- **This is not yet a verdict on which side the data prefers.** It
  establishes that the data *can* choose. Turning that into a statement
  about collapse models versus decoherence needs the link from these
  correction sizes back to the quantities the two theories are actually
  written in, and that link is a symbolic calculation currently queued and
  not yet returned.
- **The background was held fixed.** Six standard numbers describing the
  universe — its expansion rate, its contents, and so on — were frozen at
  their measured values rather than being allowed to adjust. In a full
  treatment they would shift slightly to absorb part of any correction,
  which would weaken the limits quoted here. So these limits are an
  optimistic bound. They are strong enough to establish that the two shapes
  are separable, which is a statement that only gets more true if the
  limits weaken, but they are not the final numbers.
- **Whether this counts as "settled now" or "settleable with better
  measurement"** depends on a third number: the irreducible uncertainty
  that comes from having only one sky to look at. We cannot repeat the
  universe, so there is a floor below which no measurement can go. That
  floor is being computed separately and has not come back.
- **Everything here is provisional on a planned replication** of this
  programme's earlier survey work. If that replication sorts the approaches
  differently, the labels "C side" and "D side" might not carve things
  where this work assumes they do. The arithmetic would survive; the framing
  might not.
- **The large-scale end of the data has systematics this work cannot
  inspect.** One of the three measurements used is supplied as a
  precomputed table, with its treatment of instrumental effects entirely
  upstream and not visible from the file. Anything resting on the largest
  patches inherits that treatment without being able to check it.
