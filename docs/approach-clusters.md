# Approach clusters (seed map, v0)

This is a **seed**, written by hand to give Run 01 a starting partition. It
is deliberately incomplete and may be wrong about attributions. Run 01 is
expected to correct, split, merge, and extend it.

Sub-problem labels P1-P5 are defined in `problem-statement.md`.
Slot labels S1-S7 are defined in `common-scaffold.md`.

---

## Cluster A - No-collapse formulations of a closed universe

Targets P1, P2. Largely silent on P4.

- **Everettian / relative-state**, with decoherence supplying the preferred
  basis. Observer is a subsystem; records are branch-relative.
  Everett 1957; Zeh 1970; Joos & Zeh 1985; Zurek 2003; Wallace 2012.
- **Decoherent (consistent) histories.** Built explicitly for closed
  systems; no measurement primitive. Quasiclassical realms emerge from a
  consistency condition on coarse-grained histories.
  Griffiths 1984; Omnes; Gell-Mann & Hartle 1990; Hartle 1993; Halliwell.
- **Quantum Darwinism / existential interpretation.** Objectivity from
  redundant imprinting of pointer states in many environment fragments.
  Zurek 2009.

Open question for Run 01: whether A1 and A2 differ in S4 beyond notation.
Hartle and Wallace have both commented on this; find out what each
actually claims.

## Cluster B - Relational and agent-centred formulations

Targets P1, P2 by denying a global observer-independent state.

- **Page-Wootters conditional probability / timeless QM.** Time from a
  clock subsystem; dynamics as correlation within a static constraint
  solution. Page & Wootters 1983; revived by Giovannetti, Lloyd & Maccone;
  Hoehn, Smith & Lock.
- **Relational quantum mechanics.** States are relative to a physical
  system, not absolute. Rovelli 1996.
- **QBism.** Quantum states are an agent's personal expectations; the
  universal wavefunction is rejected as a category error. Fuchs, Mermin
  & Schack 2014. Note: the QBist stance on cosmology is a live dispute and
  should be reported from primary sources, not from critics.
- **Quantum reference frames.** Superposition and entanglement are
  frame-dependent. Giacomini, Castro-Ruiz & Brukner 2019.

Open question: whether B1 is a *formalism* compatible with several of the
interpretations in A and B, rather than a rival to them.

## Cluster C - Dynamical reduction (observer eliminated)

Targets P2 directly by modifying the dynamics, which makes P1 and P3
easier and leaves P4 untouched.

- **GRW / CSL spontaneous collapse.** Ghirardi, Rimini & Weber 1986;
  Bassi & Ghirardi 2003.
- **Gravitationally induced collapse.** Penrose 1996; Diosi.
- **Collapse applied to inflationary perturbations.** This is the one place
  the cosmological observer problem becomes numerically constrained:
  collapse parameters feed into the primordial power spectrum.
  Martin, Vennin & Peter 2012 and follow-ups.

Open question: the strongest existing observational bound on collapse
parameters from CMB data, with the assumptions it rests on.

## Cluster D - The quantum-to-classical transition of cosmological perturbations

Targets P2 in a concrete, calculable setting, with no interpretive
commitment stated. Often ignored by the foundations literature even though
it is the sharpest instance of the problem.

- Squeezing of the inflationary two-mode state and the resulting
  indistinguishability from a classical stochastic field.
  Polarski & Starobinsky 1996; Kiefer & Polarski 2009.
- Decoherence from gravitational nonlinearities and from unobserved modes.
  Burgess, Nelson and others; also an effective-field-theory line of work
  on cosmological decoherence.

Open question: whether the standard result establishes definiteness of
outcomes, or only the *statistical* equivalence to a classical ensemble.
These are not the same claim and are frequently conflated.

## Cluster E - Measure and self-location

Targets P3, P4. Nearly disjoint from A-D in both methods and citations.

- **Anthropic / self-sampling frameworks.** Carter 1974; Barrow & Tipler
  1986; Bostrom 2002 (SSA, SIA, observer-moments).
- **Measures for eternal inflation.** Causal patch (Bousso 2006),
  light-cone time, scale-factor cutoff (De Simone, Guth, Linde, Noorbala,
  Salem & Vilenkin 2010), stationary measure; global vs local measure
  distinction. Garriga & Vilenkin on prediction in the multiverse.
- **Boltzmann brains as a selection criterion.** Dyson, Kleban & Susskind
  2002; Albrecht & Sorbo 2004; Page. A measure is rejected if it predicts
  that typical observers are thermal fluctuations.
- **Rejection of typicality.** Hartle & Srednicki 2007 (Are we typical?)
  and Srednicki & Hartle 2010 argue that typicality is an extra,
  unjustified assumption, and introduce a distribution over which system
  in the universe is us, which must be fit rather than assumed.

Open question: E4 is the most direct conflict in the whole field, because
it denies the premise that E1-E3 share. Report the exchange accurately,
including the replies.

## Cluster F - Algebraic and holographic: the observer as kinematics

Targets P5, and arguably P1. The newest cluster and the least connected to
the others.

- **Horizon observer-dependence.** Unruh 1976; Gibbons & Hawking 1977.
  Particle content and entropy are frame-relative before any
  interpretation is chosen.
- **Complementarity.** Susskind, Thorlacius & Uglum 1993 for black holes;
  de Sitter complementarity as its cosmological analogue.
- **Crossed-product / von Neumann algebra constructions.** Including an
  observer with a clock changes the operator algebra from type III to a
  type with a well-defined trace, making density matrices and entropies
  meaningful. Witten, Gravity and the crossed product (arXiv:2112.12828);
  Chandrasekaran, Longo, Penington & Witten, An algebra of observables for
  de Sitter space (arXiv:2206.10780); Chandrasekaran, Penington & Witten on
  large-N algebras and generalized entropy; Jensen, Sorce & Speranza.
- **Static-patch holography.** Observer-centric holographic descriptions of
  de Sitter. Narovlansky & Verlinde on double-scaled SYK and de Sitter;
  related Susskind work.

Open questions for Run 01, in priority order:
1. Precisely what the de Sitter algebra result requires of the observer:
   which properties of the clock are load-bearing (in particular whether
   the clock Hamiltonian must be bounded below), and what is assumed
   versus derived.
2. Whether "observer" in Cluster F means the same thing as in Clusters A-E,
   or is a distinct technical notion that happens to share a word. This is
   the single highest-value question in the run.

---

## Known gaps in this seed

**Moved to `known-gaps.md`.** The list itself is unchanged; only its
location is. It was split out because the adversary prompt withholds this
file while asking the adversary to check coverage against the gap list, so
the list had to live somewhere a run can be given without the seed. See
`known-gaps.md` for why, and add new gaps there rather than here.

## Citation warning

Every reference above is a lead, not a verified citation. Several are given
by author and approximate year only. A reference that cannot be verified
against a primary source must be dropped, not paraphrased. See
`../protocol/EVIDENCE-RULES.md`.
