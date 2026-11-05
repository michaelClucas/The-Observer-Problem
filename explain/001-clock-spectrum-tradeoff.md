# Can a clock tell time perfectly and still leave the universe a finite amount of entropy?

Evidence: `findings/001-wp7-clock-spectrum-reads.md` and
`verify/clock_trace_finiteness.py` (3 of 3 checks pass). Produced
2026-11-05 by work package WP-7.

This write-up covers two things settled on the same day: a correction to
what this programme previously believed about a published theorem, and a
question that turns out to be real, published, and currently impossible to
test. The second is the result.

## The setting: physics without an outside

Almost all of physics is done from outside. You have a system, you have an
apparatus, and the apparatus is not part of the system. Time is read off a
clock that sits outside what is being timed.

Cosmology cannot do that. There is no outside the universe. If time is to
mean anything, it has to be read off something inside — some physical
subsystem that changes in a regular way, which you then treat as the clock.
Everything else is described relative to the clock's reading rather than
relative to an external time.

Two separate research communities have worked on what that costs.

## Community one: how to build a clock out of a quantum system

If the clock is a physical subsystem, it is a quantum system, and quantum
systems do not have perfectly definite properties. So "the clock reads
`t`" is not a sharp statement in general.

There is an old obstruction here, due to Pauli. A clock's reading and the
clock's energy are related the way position and momentum are: you cannot
have both sharp. Push it further and a theorem says that if the clock's
energy is **bounded below** — if there is a lowest possible energy, which
every real physical system has — then there cannot be a sharp,
well-behaved time observable conjugate to it at all. Unruh and Wald
sharpened this into an argument that any realistic clock which can run
forward must have some probability of running backward, and used it to
argue against the whole relational approach.

Höhn, Smith and Lock answered it by changing what counts as an observable.
Instead of requiring the clock's reading to be a sharp quantity, they let
it be a **generalised** measurement — one whose possible readings are not
perfectly distinguishable from each other. That weaker thing exists even
for a clock with a lowest energy, it runs forward properly, and it has a
consistent probability interpretation. The price is the fuzziness: two
nearby readings of the clock are not fully distinct states.

Their paper then proves that three different-looking formalisms for
relational time are in fact the same theory, which they call the trinity.

## Community two: how much entropy a region of space has

Separately, people studying quantum gravity in a region bounded by a
horizon — the inside of a black hole's exterior, or the patch of de Sitter
space one observer can see — found that the mathematics of observables in
such a region comes in different types, and which type you get decides
whether entropy is well defined.

The relevant distinction: one type has a **finite** total measure, which
means there is a state of maximum entropy and entropy has an absolute
scale. The other has an **infinite** one, which means no maximum-entropy
state and entropy defined only up to an undetermined constant.

Chandrasekaran, Longo, Penington and Witten found that for de Sitter space
you get the finite one — a maximum-entropy state, identified with empty de
Sitter — **provided you require the observer's energy to be bounded
below**. That requirement is what makes the total finite.

## The trade-off

Put the two together and the same property, the clock's or observer's
energy being bounded below, has opposite roles:

- community one: the bound is what **prevents** a sharp clock. Lift it, and
  the clock reads time perfectly.
- community two: the bound is what **produces** a finite entropy. Lift it,
  and entropy loses its absolute scale.

**So: a clock that tells time perfectly comes with no finite entropy scale,
and a finite entropy scale comes with a clock that cannot tell time
perfectly.** You appear not to be able to have both.

This programme's earlier survey work found that statement and recorded it
as its own inference, noting that no source it had retrieved stated the
trade-off in those terms.

## What was settled today, part one: a correction

The earlier work had attached the trade-off to the trinity theorem. It
reasoned: the trinity holds under a condition on the clock's energy
spectrum, so the question of whether the formalisms agree and the question
of the energy bound are linked.

**Reading the paper, that is wrong.** The trinity's condition is that the
clock's energy spectrum be **continuous** and **non-degenerate** — that it
take a continuous range of values and that no value occur twice. It says
nothing about being bounded.

And the independence is not merely a gap in the wording. Two of the three
example clocks the paper offers as satisfying its condition have bounded
energy. The paper raises boundedness at one point inside the relevant
section and explicitly sets it aside as not mattering there. The whole
construction exists in order to make bounded clocks work.

So the link was not there, and this programme has withdrawn that inference.
A previous critical review of the earlier work had flagged this as probable
and named exactly the check that would settle it; the check was run and it
settles it.

## What was settled today, part two: the trade-off is published after all

The earlier work said no retrieved source stated the trade-off. Searching
further, one does.

De Vuyst, Eccles, Höhn and Kirklin state it directly as a dichotomy: a
clock whose energy spectrum is the whole real line is the sharp,
perfectly-readable case, and gives the infinite-measure type with no
maximum-entropy state; a clock whose energy is bounded below is the fuzzy
case, and gives the finite-measure type with a maximum-entropy state. They
also note that the de Sitter energy bound of community two is *equivalent*
to starting from a fuzzy clock in community one's sense — which is the
bridge the earlier work had been looking for in the wrong place.

They even set the two ends against each other explicitly: if one observer
carries a sharp clock and another a bounded one, the two assign different
entropies to the same region, and only the second has a maximum.

So the trade-off is real and in print. **The earlier work's "no source
states this" was a gap in its searching, not a gap in the literature.**
That is worth saying plainly, because it is the second time in this
programme's short history that a claim about what the literature does not
contain turned out to be a claim about what had not been read.

## And a second question, answered the unhelpful way

A separate paper was expected to show that the observer's energy bound in
de Sitter is **derived** rather than assumed. If it were, the maximum
entropy of de Sitter would be physics rather than a modelling choice.

It is not derived. The authors put the bound in by hand and say so: having
placed an observer in the spacetime themselves, they write that they
therefore "need to bound its physical properties", and that bounding the
energy from below is "physically reasonable". The restriction appears
explicitly in their algebra as a projection, exactly as in the earlier
work.

What the paper does establish is more interesting and points the other way.
Including the full set of constraints that gravitational backreaction
imposes, the finite-measure property **fails** — extra quantities can
fluctuate freely and the total becomes infinite again. What rescues it is
modelling the observer as a compact body held together by
non-gravitational forces, so that distorting its shape costs energy and the
fluctuations are suppressed. The authors argue it must be such a body,
since anything held together by its own gravity would come apart in the
limit they are working in.

**So the maximum entropy of de Sitter space depends, in this construction,
on the stiffness of an observer's internal chemistry.** That makes the
modelling dependence sharper than before, not weaker. The authors state the
conclusion as an argument and as "appears likely", not as a proof.

## The verdict: real, published, and currently untestable

Where does that leave the trade-off?

It is a genuine, published statement with a theorem behind it. And this
programme sorts questions by whether data can bear on them, with the
bins being: settleable with data in hand, settleable with better
measurement, settleable by nothing because the one-sky limit is in the way,
no difference in predictions at all, and **not yet posed** — meaning nobody
has stated the question in a form where a measurement could address it.

The trade-off is in the last bin.

What differs between its two ends is which **type** a collection of
mathematical operators belongs to, and whether a maximum-entropy state
exists. Nothing in anything read for this work — across two earlier passes
and today — connects either of those to a number anyone could measure on
the sky. The nearest thing is the observation above, that the finite total
picks up a contribution from an observer's internal stiffness, which makes
the entropy depend on laboratory-scale physics but still supplies no
cosmological observable.

This is important to state carefully, because "not yet posed" is routinely
mistaken for "undecidable", and they are opposite claims. Undecidable would
mean nature does not distinguish the two cases. Not yet posed means
**nobody has written down what measurement would distinguish them.** The
first is a fact about the universe. The second is a fact about the
literature, and it can change tomorrow if someone does the work.

**What the work would be**, stated as precisely as it can be: a derivation
taking the finite total measure, and the maximum-entropy state that comes
with it, to a statistic of some field on the sky. How hard that is, nobody
knows — and "cost unknown" is the honest entry rather than a guess.

## What is still open

- Everything here rests on the earlier survey's grouping of approaches,
  which has not been independently replicated. The quotations and the
  convergence check would survive; the claim that this question sits at the
  junction of three particular families of approach might not.
- Whether the trade-off is a theorem with the hypotheses this programme
  would need is now arguable, since it is stated precisely enough to
  enumerate them. It was not formalised, for two reasons recorded in the
  findings document: it is already a theorem of a mature branch of
  mathematics, so verifying it buys this programme no physics, and the
  mathematical libraries available do not contain the concepts it is
  stated in.
- One numerical detail could not be reproduced. A counting factor in one
  of the papers appears to this reader to be off by a multiplicity, and
  rather than assert that, the convergence was checked both ways: the
  conclusion holds either way, but the numerical value of one entropy
  contribution does not, and it is therefore recorded as unknown and used
  nowhere.
