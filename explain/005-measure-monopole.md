# A question about the universe that nobody can ever answer, and exactly why

Evidence: `verify/measure_monopole_vs_floor.py` and
`findings/005-wp5-measure-branch-closed.md`. Produced 2026-11-05 by work
package WP-5.

This one is a negative result. The honest version of a negative result is
not an apology, so here is the claim up front: **there is a real
disagreement between two theories about something real, and no measurement
anyone could ever make will settle it.** Not "has not yet settled it".
Ever. The rest of this explains the disagreement and then explains the
"ever", because the "ever" is the part that is actually a result.

## The disagreement

Some versions of inflation do not stop. The region we live in stopped
inflating, but in this picture inflation continues elsewhere forever,
producing an unlimited number of regions like ours. That is called eternal
inflation.

It creates a counting problem. If you want to ask "what should an observer
expect to see?", you have to count observers, and there are infinitely many
of them. Infinity divided by infinity is not a number, so the question has
no answer until you specify a rule for doing the counting. Such a rule is
called a **measure**.

Different measures are different rules. **The fat geodesic measure** picks
a single worldline through the spacetime and counts what happens along it.
**The causal patch measure** counts what lies inside the region that one
observer could ever receive a signal from. These are both reasonable, they
are not the same, and there is no agreed way to choose between them.

If the choice of measure had no observable consequences it would not
matter. It does have consequences, and that is the subject here.

## What the two measures predict

The relevant quantity is the **gravitational potential**, written `Psi`: a
number at each point describing how much the local gravity differs from the
average. It is what makes some regions denser than others, and it is what
the hot and cold patches in the cosmic microwave background are a map of.

In standard cosmology, the average of `Psi` over the whole sky is zero by
construction. There is no preferred value, because there is no preferred
place.

**Both measures predict that the average is not zero.** The reason is a
selection effect, and it is worth following because it is the actual
mechanism.

For the fat geodesic measure: the worldline that defines the counting is a
freely falling path, and freely falling paths drift toward denser regions,
because that is what gravity does. So the places the measure counts are
systematically slightly denser than a randomly chosen place. That bias
shows up as a non-zero average `Psi`.

For the causal patch measure: the same effect, plus a second one. The size
of the region an observer can see depends on the gravitational potential
around them, and the number of observations that happen inside a region
depends on its size. So denser regions get counted more heavily, again
biasing the average.

**The two biases are different in detail.** That is a genuine conflict in a
predicted observable, which in this research programme's terms is the
strongest kind of disagreement — both sides make a claim about the same
measurable thing and the claims differ.

Both measures also predict a related effect in a three-way correlation
between points, with the same structure.

## Why no measurement settles it

Now the result.

The predicted average `Psi` is what is called a **monopole**: it is the
same in every direction. A pattern on the sky can be broken into pieces by
how finely it varies with direction. The monopole is the coarsest piece,
the part that does not vary with direction at all. Then there is the
dipole, hotter on one side and colder on the other. Then the quadrupole,
and so on to finer and finer patterns.

Here is the thing that decides the question. **At each level of fineness
there are a certain number of independent patterns, and that number grows:
one at the monopole, three at the dipole, five at the quadrupole, and
`2l+1` at level `l`.**

That number is what makes measurement work. We cannot repeat the universe
to see how else it might have come out, so there is an unavoidable
uncertainty in any statement about the pattern — we have one sample.
But at a fine level of detail there are thousands of independent patterns,
and averaging over them shrinks the uncertainty. That is why the small-scale
cosmic microwave background is measured to a couple of percent while the
large-scale part is not.

Worked out, the unavoidable fractional uncertainty is:

| level `l` | independent patterns | unavoidable uncertainty |
| --- | --- | --- |
| 0 (monopole) | **1** | **141%** |
| 1 (dipole) | 3 | 82% |
| 2 | 5 | 63% |
| 100 | 201 | 10% |
| 1000 | 2001 | 3.2% |
| 2508 | 5017 | 2.0% |

**The measure prediction lives entirely at the top row.** And the top row
has one pattern in it. There is one monopole. We have measured it. There
will never be a second one to average with, because there is one sky and
one monopole on it.

So the uncertainty on the one quantity where the two measures disagree
cannot be reduced. Not by a better telescope, not by a longer observation,
not by a future mission. The thing that reduces the uncertainty elsewhere
— having many independent copies of the pattern — does not exist here and
cannot be made to exist.

That is the whole argument, and it is why this is a different claim from
"the effect is too small to see at present".

## A second, independent reason

There is also a size argument, and it closes the same door from the other
side.

The predicted average `Psi` is smaller than a typical `Psi` fluctuation by
a factor of about `10^-5` — the same one-part-in-a-hundred-thousand that
describes how smooth the microwave background is. But the prediction also
grows as you look at smaller scales, so in principle you could go to small
enough scales for the growth to cancel the suppression.

Working out where that happens: you would need to look at scales about
`10^10` times smaller than the observable universe, which means structures
of about `1.4 x 10^-6` megaparsecs. That is:

- about **6.6 orders of magnitude** beyond the smallest scale the microwave
  background measures, and
- about **6.6 orders of magnitude** inside the scale where the calculation
  that produced the prediction has stopped being valid.

The second point is the important one. On small enough scales, matter has
collapsed into galaxies and clusters and the gentle approximation behind
the whole calculation — that everything is a small ripple on a smooth
background — is simply false. The scale where the measure signal would
become visible is deep inside that region. So it is not that we need a
better instrument. **The prediction does not exist at the scale where it
would be large enough to see.** The paper's own author says so, in those
words.

## What this settles, and what it does not

**Settled:** the fat geodesic and causal patch measures cannot be
distinguished through this observable, by anyone, ever. This research
programme had a rule set in advance that when a question turns out to be
limited by the one-sky floor rather than by effort, it gets computed,
written up, and closed, and specifically that it must not be restated in
different language until it sounds answerable. That rule is being followed:
this is closed.

**Not settled, and worth being clear about:**

- The measure problem is not solved. This is one pair of measures compared
  through one observable. The paper's broader conclusion is actually
  reassuring for standard cosmology: both measures reproduce ordinary
  inflationary predictions up to effects too small to matter, which means
  the counting rule does not contaminate the things we do measure.
- The same paper mentions three other situations where the choice of
  measure has very large effects. Those were not examined here, and they
  are the place to look if anyone wants to reopen this. Not this door.
- One number is still missing: the precise ratio of the predicted signal to
  the floor. That is a symbolic calculation currently queued elsewhere and
  it has not come back. It is worth having, and it **cannot change the
  conclusion**, because no value of the floor changes the fact that there
  is one monopole.
- And as with everything in this programme, the framing rests on an earlier
  survey that has not yet been independently replicated. The arithmetic
  here would survive that; the way the question was grouped with others
  might not.

## Why a result like this is worth writing down

Because the field already believes it, and nobody had said why.

"Within cosmic variance" appears in the original paper's abstract. What was
missing was the distinction between *too small to see now* and *impossible
to see in principle*, and the reason for the second. The reason turns out
to be a counting fact — one monopole — that takes a paragraph to state and
is not in any source read for this work.

A question nobody can answer is a worse outcome than a question somebody
answers. It is a much better outcome than a question left open because
nobody checked.
