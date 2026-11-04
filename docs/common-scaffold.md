# The common scaffold (provisional, v0)

There is no agreed common formalism for the approaches in
`approach-clusters.md`. This document proposes a minimal one, purely so
that approaches can be filled into the same slots and compared. It is
**scaffolding, not a theory**. It is expected to be revised or discarded by
the runs that use it.

An approach is described by what it puts in seven slots.

---

### S1. Global object

What is the fundamental mathematical object describing the universe as a
whole?

Possible fillers: a normalised state vector in a global Hilbert space; a
solution of a constraint equation with no normalisability; a density
operator; an algebra of observables with no preferred state; *nothing*
(the approach denies a global object exists).

Record: the object, and whether it is unique.

### S2. Observer representation

How is the observer represented inside S1?

Possible fillers: a tensor factor of the Hilbert space; a subalgebra of the
global algebra; a set of coarse-grained projectors; a worldline with a
clock degree of freedom; a primitive agent not represented in the
formalism at all.

Record: the representation, and whether it is derived or postulated.

### S3. Clock / frame

What plays the role of time or reference frame for that observer, and is it
internal or external?

Possible fillers: external background time; a quantised clock subsystem; a
matter field used as a relational clock; the observer's own proper time
promoted to an operator; modular flow.

Record: the clock, whether it is quantised, and what its spectrum is. The
spectrum matters: several results turn on whether the clock Hamiltonian is
bounded below.

### S4. Record rule

What links S1-S3 to the existence of a definite record?

Possible fillers: decoherence of a preferred basis via environment tracing;
a consistency condition on histories; a stochastic modification of the
dynamics; a conditional-probability construction; agent-relative
subjective assignment with no dynamical account; nothing (records are
primitive).

Record: the rule, and whether it is exact or approximate. If approximate,
what controls the error.

### S5. Probability rule

What assigns probabilities to the observer's records?

Possible fillers: Born rule on the global state; Born rule restricted to a
branch; decoherence-functional diagonal; conditional probability given a
clock reading; a personalist coherence constraint; a frequency over an
ensemble of observer-instances.

Record: the rule, and what argument (if any) is given for it rather than
an alternative.

### S6. Self-location rule

When multiple observer-instances in the description have identical
evidence, what fixes which one the prediction is about?

Possible fillers: uniform sampling over instances; sampling weighted by
amplitude; sampling over observer-moments; a free parameter fixed by
fitting data; an explicit refusal to assume typicality; the question is
declared meaningless.

Record: the rule, and whether it is derived from S1-S5 or added by hand.
This slot is empty for most approaches, which is itself a finding.

### S7. Measure / regularisation

If the number of observer-instances is infinite, how are ratios defined?

Possible fillers: a spacetime cutoff (causal patch, light-cone time,
scale-factor, stationary); a global time slicing; a finite-volume
restriction; no regularisation needed because the approach does not count
instances.

Record: the cutoff, whether it is covariant, and what it predicts about
the dominance of thermally-fluctuated observers.

---

## Comparison rules

Two approaches **genuinely disagree** when they fill the same slot with
objects that cannot be mapped to each other by a change of notation, *and*
the difference changes at least one of: the set of allowed records, a
probability, or a predicted observable.

Two approaches are **notational variants** in a slot when an explicit
dictionary maps one filler to the other with no change to S5 outputs.
Claiming this requires exhibiting the dictionary.

Two approaches are **non-competing** when they fill disjoint slots. Much of
the apparent disagreement in this field is of this kind: an approach to P1
is compared with an approach to P4 as though they were rivals.

An empty slot is a result, not an omission to be papered over. Record it as
empty.

## Known weaknesses of this scaffold

- It presumes the observer can be localised in the formalism at all, which
  is exactly what relational and agent-centred approaches contest. Those
  approaches will fill S2 with "not represented", and the scaffold should
  not be read as counting that against them.
- It separates S4 from S5, which several approaches deny is separable.
- It has no slot for the *emergence* of spacetime, so approaches where the
  observer is prior to geometry will fit badly. Flag that rather than
  forcing them in.
- S7 presupposes instance-counting, which is a substantive commitment.
