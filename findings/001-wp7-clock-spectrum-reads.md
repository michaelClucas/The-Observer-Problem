# WP-7: the two literature reads that gate the symbolic branch

**Package:** WP-7 (`docs/RESEARCH-PLAN.md` §4).
**Day:** 2026-11-05, cycle 1. Branch `research/auto-2026-11-05`.
**Status:** complete. Both commissioned reads done at primary level, plus one
further read that the branch-kill criterion turns on.
**Provisional on WP-1** (Run 01's cluster structure is unreplicated).

Script backing every number below: `verify/clock_trace_finiteness.py`,
run before this file was committed, 3 of 3 checks PASS.

---

## Summary of outcomes

| Question | Answer | Consequence |
| --- | --- | --- |
| Read 1. What is the trinity equivalence's actual spectral hypothesis? | **Continuous and non-degenerate spectrum of `H_C`.** Boundedness is not a hypothesis. | Run 02's **P-1 is CONFIRMED**. Run 01 relation 7's inference is withdrawn. |
| Read 2. Is the observer's energy bound derived rather than imposed? | **No. It is imposed, in the authors' own words.** | WP-7's second gate **does not open**. The de Sitter entropy normalisation remains a modelling choice. |
| The kill criterion's own question: has anyone stated the Part 3.6 trade-off in print? | **Yes.** De Vuyst, Eccles, Höhn & Kirklin, arXiv:2405.00114, state both ends and the dichotomy explicitly. | The branch kill's **trigger fires but its stated rationale is false.** Overseer decision, logged as Q-1. |

The three outcomes do not line up the way either the plan or Run 02
anticipated, and the disagreement is the substance of this document.

---

## Read 1. arXiv:1912.00033 §V and §III.2

Höhn, Smith & Lock, *The Trinity of Relational Quantum Dynamics*.
Retrieved as LaTeX source via `arxiv.org/e-print/1912.00033`
(`trinity_v3.tex`, 2859 lines; the arXiv listing resolves to the title and
author list quoted here). Read at primary level: §III in full
(lines 488-739 of the source) and §V (lines 1006-1424). `[SOURCED]`

### The hypothesis, as the paper states it

§V's opening paragraph, verbatim and in full on this point:

> We establish the equivalence between these three relational dynamics
> under the condition that the clock Hamiltonian `\hat H_C` has a
> continuous non-degenerate spectrum (this is generalized to a doubly
> degenerate spectrum in [HLSrelativistic] and to periodic i.e.
> discrete-spectrum clocks in [HLS2]).

§III.2 sets up the same restriction before the classification:

> For simplicity, we will only consider non-degenerate clock Hamiltonians
> with spectra that are either entirely continuous or entirely discrete in
> the following two subsections.

So the hypothesis is **continuity and non-degeneracy**. `[SOURCED]`

### Boundedness is not merely absent, it is raised and discharged

This is stronger than silence, and it is why P-1 confirms rather than
merely survives.

1. **§III exists in order to admit bounded clock Hamiltonians.** Its stated
   purpose is to answer Pauli's and Unruh & Wald's objection that no
   *self-adjoint* time operator is conjugate to a bounded Hamiltonian. The
   paper's route is to drop self-adjointness for a covariant POVM:
   "this will permit us to define *monotonic* (covariant) time observables
   with a well-defined probability interpretation even for bounded clock
   Hamiltonians." A construction whose selling point is making bounded
   clocks work cannot also be imposing boundedness. `[SOURCED]`
2. **Two of the paper's three worked examples of admissible clocks are
   bounded.** §III.2.3 gives `H_C = p^2/2m + a_1 e^{a_2 q}` with spectrum
   bounded below (`sigma_c = R^+`), and `H_C = q/c` on `L^2(0,a)` with a
   doubly bounded spectrum `sigma_c = (0, a/c)`. Both are offered as
   non-degenerate continuous-spectrum clocks, i.e. inside the equivalence's
   hypothesis. `[SOURCED]`
3. **Where `spec(H_C) = R` does appear inside §V, the paper explicitly says
   it does not matter.** At source line 1258: the trivialisation map
   `T_T` is unitary on the *kinematical* Hilbert space only if
   `spec(H_C) = R`, and "if `\hat H_C` is bounded and `\hat H_S` is
   unbounded, then `\hat C_H` and `\hat H_C - eps_*` will have distinct
   spectra." The paper then discharges it: "However, this is of no concern
   to us since we are not interested in the full spectrum of `\hat C_H` on
   `H_kin`, but only in its zero-eigenspace" — on which invertibility
   requires only `eps_* \in spec(H_C)`. `[SOURCED]`

### What boundedness *does* control in this paper

Not the equivalence. A separate and weaker list, all of which fail once
`spec(H_C) != R`:

- clock states are orthogonal only for `sigma_c = R`;
- `\hat T` is self-adjoint, and forms a Heisenberg pair with `\hat H_C`,
  only for `sigma_c = R`;
- clocks with `sigma_c = R` are the ones the paper names **ideal**.

`||t||^2 = measure(sigma_c)`, from the clock-state overlap
`<t|t'> = int_{sigma_c} d eps e^{i eps (t-t')}`, so clock states are
normalisable only when the spectrum is bounded **both** above and below.
Evaluated in check 3 of `verify/clock_trace_finiteness.py`. `[SOURCED]`

### Verdict on P-1

Run 02's P-1 named its own settlement condition: *"If the hypothesis is
'non-degenerate, continuous spectrum' with boundedness explicitly
immaterial, this becomes `CONFIRMED`."* That condition is met.

**P-1 moves `PLAUSIBLE` -> `CONFIRMED`.** Run 02's corrected statement is
adopted: the trinity equivalence holds under a non-degeneracy and
continuity condition which is independent of the boundedness question, and
Run 01 relation 7's trailing inference — *"so the compatibility claim and
the spectrum question are not independent"* — **does not follow and is
withdrawn**.

Per protocol, Run 01 is append-only and is **not edited**. The correction
is recorded here and in `logs/2026-11-05.md`.

---

## Read 2. arXiv:2601.07910

Klinger, Kudler-Flam & Satishchandran, *Generalized Entropy is von Neumann
Entropy II: The complete symmetry group and edge modes*. Retrieved as
LaTeX source via `arxiv.org/e-print/2601.07910` (`final_draft.tex`). Read
at primary level: abstract, §1, §3.6 and §5 in full. `[SOURCED]`

**Run 01 flagged this as its highest-value unretrieved item and it is
retrievable.** Run 01's characterisation of it was *"reported to argue that
proper accounting of the observer's energy implies Type II_1"*, which is
close to the abstract's wording but describes a different paper from the
one that exists: the paper's subject is the **edge modes and boost
supertranslations** of the horizon, and the de Sitter observer appears in
§5 as one application.

### The answer to WP-7's question is no

The paper puts the energy bound in by hand and says so. §3.6, verbatim:

> Finally, we note that since the observer was put into the spacetime "by
> hand" we need to bound its physical properties. In particular, as in
> sec. 2.1, it is physically reasonable to bound the energy `eps` of the
> observer from below.

and the resulting physical algebra carries the projector explicitly,
`A^{+,obs.}_{dress.} := P_{q>0} A^{obs.}_{dress.} P_{q>0}`. In §5 the same
projector reappears unchanged in `A^{obs.,+}_{dress.}(R;G)`. The
description of CLPW is the same: "imposing the physical condition that the
energy of the observer be bounded from below bounds the area from above
yielding a Type II_1 algebra." `[SOURCED]`

So **the energy bound is imposed in this paper exactly as it was in CLPW**,
and the conditional in WP-7's brief — *"If so, the energy bound is derived
rather than imposed, and the de Sitter entropy normalisation is physics
rather than a modelling choice"* — has a false antecedent. The de Sitter
entropy normalisation remains a modelling choice. `[SOURCED]`

### What the paper does establish, which is a different and sharper thing

The Type II_1 classification is **not robust** to including the full
constraint set, and what rescues it is the observer's internal
non-gravitational physics.

1. Gravitational backreaction perturbs the horizon area in an
   angle-dependent way, turning on an infinite family of boost
   supertranslation charges `q_lm` matching the observer's mass multipole
   moments. These cannot be set to zero: by the paper's theorem 1 no state
   but the vacuum, and no operator but the identity, is invariant under all
   horizon boost supertranslations. `[SOURCED]`
2. If the `q_lm` are independent they are free zero modes: "They can
   fluctuate freely without any suppression from decreasing the horizon
   area. In this case, the algebra is Type II_infinity and there would be
   no maximum entropy state." `[SOURCED]`
3. They are not independent *if* the observer is a compact body held
   together by non-gravitational binding energy — and the paper argues it
   must be, since gravitational binding is `O(G_N)` and unbinds as
   `G_N -> 0`: "any object, e.g., a star or a galaxy, whose binding energy
   is dominated by gravitational effects is not a good semiclassical
   observer." The model is a quadratic expansion about a local energy
   minimum, `eps = M + H_rot + q + (1/2) sum c_lm q_lm^2`, with model-
   dependent stiffnesses `c_lm`. `[SOURCED]`
4. Finiteness of the trace then requires `Z_lm = <e_gamma|e^{-H_lm}|e_gamma>
   < infinity` for each `(l,m)`. Check 2 of
   `verify/clock_trace_finiteness.py` evaluates this as the Gaussian
   `Z_lm = sqrt(pi / c_lm)`, finite for every `c_lm > 0` and divergent as
   `c_lm -> 0`, confirming numerically that the limit which destroys the
   finite trace is precisely the free-zero-mode limit the paper names.
   `[INFERENCE]`; premise: the group algebra carries Lebesgue measure, as
   the paper's `gamma` for the one-dimensional group von Neumann algebra.

**So the maximum-entropy state of de Sitter is contingent, in this paper's
own construction, on the stiffness of the observer's non-gravitational
internal forces.** That is a sharper statement of the modelling dependence
than Run 01 had, and it points the opposite way from "the normalisation is
physics".

### The strength of the claim is "argue", not "prove"

Stated for the Lean trigger and for the record. The abstract says "We
*argue* that a proper account of the observer's rotational kinetic energy
and (non-gravitational) binding energy implies that the algebra is of Type
II_1". §5 says "it *appears likely* that the norm [...] is finite so that
the algebra [...] is Type II_1 for a large class of physical observers in
de Sitter". §3.6 says "It *appears likely* that, for a large class of
physical bodies, `A^{+,obs.}_{dress.}(R; R x SO(3))` is a Type II_1
algebra." `[SOURCED]`

The one place the paper computes rather than argues is the isotropic rigid
body, where `H_rot = L^2/2I` and the trace of the identity factorises as
`<0_R|e^{-q}P_{q>0}|0_R> * <e_SO(3)|e^{-H_rot}|e_SO(3)>`, the first factor
being `int_0^inf dq e^{-q} = 1` exactly and the second being written as
`sum_l (2l+1) exp(-l(l+1)/2I)`.

Check 1 of `verify/clock_trace_finiteness.py` confirms this converges, for
`I` from 0.1 to 1000. **One reading limitation, recorded rather than
papered over:** the paper's improper basis
`|e_SO(3)> = sum sqrt(2l+1) delta_{mn} |l,n,m>` appears to this reader to
give multiplicity `(2l+1)^2` rather than `(2l+1)` after summing the
`(2l+1)` terms with `n = m`, and I could not reproduce the single factor
from the text alone. I do not assert the paper is wrong. The script
therefore evaluates **both** multiplicities and both converge at every `I`
tested, so the convergence claim — which is what the Type II_1 conclusion
rests on — does not depend on the factor I could not reproduce. The
numerical value of the entropy contribution does: at `I = 1` the sums are
2.370337 and 5.680765 respectively, giving `log tau` of 0.863032 and
1.737055. **Any use of that number is `[UNKNOWN]` until the multiplicity is
settled**, and nothing in this repository uses it.

---

## The third read, and why it was in scope

Run 01's **open question 3** asks, verbatim: *"Is the clock trade-off in
Part 3.6 a real theorem, and has anyone stated it?"* and names as what
would settle it *"the De Vuyst et al. papers' later sections on degenerate
and non-ideal clocks"*. The plan's branch kill (§5) reads: *"The clock /
algebraic branch dies if WP-7 confirms P-1. The trade-off then has no
published basis, is one run's inference, and gets no Maple time until
someone states it in print."*

Determining whether it is stated in print is therefore not scope creep; it
is the condition the kill criterion itself names. One fetch.

### arXiv:2405.00114 states the trade-off in print

De Vuyst, Eccles, Höhn & Kirklin, *Gravitational entropy is
observer-dependent*. Retrieved as LaTeX source via
`arxiv.org/e-print/2405.00114` (`shortversion.tex`). Read at primary level:
the passages quoted below, located by search, not the whole paper — so this
is a **targeted** read and anything outside these passages is unread.
`[SOURCED]` for the quoted statements.

The definition, their §2:

> For the simple kind of QRF we are considering, a clock is ideal if its
> energy spectrum is the whole real line, and non-ideal otherwise.

The dichotomy, their §3:

> When the trace is finite, which by Eq. (normal2) occurs when `sigma_i` is
> bounded below, it is Type II_1; otherwise it is Type II_infinity.

and earlier in the same section:

> if `C_i` is a non-ideal clock with a lower bound on its energy,
> `A^H_{U C_i}` is of Type II_1 [...] Physically speaking, this is due to
> the existence of a maximally mixed state on this algebra.

The two ends set against each other, their §5:

> For instance, Alice may carry an ideal clock, while Bob carries one with
> bounded spectrum. Depending on the presence of other observers,
> `r(A^H_{U C_Alice})` may be of Type II_infinity, while
> `r(A^H_{U C_Bob})` is of Type II_1, so that there will exist a maximal
> entropy state for the regional QFT for Bob but not for Alice.

And the identification with CLPW's move:

> While initially, the projectors `Pi_1, Pi_2` are trivial because the
> clocks are ideal, CLPW later impose lower bounds on their energies and
> this is equivalent to starting like us with non-ideal clocks and
> non-trivial projectors from the outset.

That is Run 01's Part 3.6 trade-off, in print, with both ends named and
joined: a clock whose spectrum is all of `R` tells time sharply
(orthogonal, perfectly distinguishable readings, per HSL) and gives
Type II_infinity with no maximum entropy state; a clock bounded below tells
time fuzzily and gives Type II_1 with a finite trace and a maximum entropy
state.

**Run 01's open question 3 is answered: yes, stated in print, at
arXiv:2405.00114.** The `[INFERENCE]` tag on Part 3.6's synthesis is
correct as a description of what Run 01 did, but the finding is no longer
unpublished, and Run 01's *"No retrieved source states the trade-off in
these terms"* was a retrieval gap, not a gap in the literature.

### Which leaves the kill criterion in two minds, and that is Q-1

P-1 is confirmed, so the kill criterion's **trigger** has fired. But its
**rationale** — "the trade-off then has no published basis" — is false on
primary-source evidence read today. Both halves are now established, and
they point opposite ways. The provenance Run 01 gave was wrong (the trinity
theorem does not underwrite the trade-off); the trade-off itself has a
better provenance than Run 01 claimed (De Vuyst et al. state it directly).

Whether the branch is live is an overseer decision and is logged as **Q-1**
in `OPEN-QUESTIONS.md`.

**The reversible default taken:** no Maple job is filed for the clock
trade-off, and no symbolic work is started on it. This default costs
nothing and is reversible tomorrow, because the plan's §3 already rejects
the clock-spectrum question as Maple work on independent grounds — "Maple
has no natural handle on these, and a plausible-looking Maple manipulation
of an operator algebra would be worse than no result" — so the Maple queue
is unaffected by either answer to Q-1. The day's remaining budget goes to
the empirical packages as scoped.

---

## Decidability bins recorded, for the pairings WP-7 touched only

Per `prompts/standing-loop.md`, the bin is recorded only for pairings an
in-scope package actually touches. WP-7 touches two. Neither bin is
reported as a survey result and WP-2 is not started.

**Run 01 relation 7** (B1 Page-Wootters ↔ Dirac relational observables ↔
relational Heisenberg picture, slots S3 and S5): **D4**, no differing
observable. The three formulations are related by invertible quantum
reduction maps which are isometries, so they predict identically by
construction wherever the hypothesis holds. Under §6's two readings of D4
this is reading 1 — the equivalence is a theorem, not a dispute, and no
non-empirical criterion is in contest either. `Delta = 0` exactly, from the
isometry. The verdict `notational_variant` stands; only the trailing
inference about the spectrum is withdrawn.

**The clock trade-off** (Cluster B ↔ Cluster F, Run 01 open question 3):
**D0**, not yet posed — explicitly *not* D3. No `Delta` in any cosmological
observable is computable from it as stated, because the quantity that
differs between the two ends is the **type** of an operator algebra and the
existence of a maximum-entropy state, and no step connects either to a
measurable number on the sky. De Vuyst et al. do exhibit a difference
between observers — Alice sees Type II_infinity where Bob sees Type II_1,
hence different entropies — but that is a difference between two
*descriptions*, not between two predictions for one measurement.

**What would make it computable**, which §6 says is the ledger's most
valuable column: a derivation that takes the finite trace `tau(1)` and the
maximum-entropy state to a statistic of a field on the sky. The obstruction
is not precision; it is that no such derivation exists in anything read in
Runs 01, 02 or today. The nearest live thread is KKS's own observation that
`tau(1)` acquires an additive contribution from the observer's multipole
stiffnesses `c_lm`, which are properties of a laboratory-scale body; that
makes the de Sitter entropy normalisation depend on non-gravitational
physics, but supplies no cosmological observable. **Cost to formulate:
unknown, and that is the honest entry.**

This is a D0 and must not be reported as an undecidable bin.

---

## Lean trigger: stated, not fired

`docs/RESEARCH-PLAN.md` §3 requires both explicit hypotheses and a
conclusion following by proof rather than measurement, *and* that the claim
be stated precisely enough for the hypotheses to be enumerable. The second
condition was what failed before today. It now arguably holds, because
De Vuyst et al. state the claim as a dichotomy:

> For a clock QRF `C_i` with energy spectrum `sigma_i`, the dressed
> algebra `A^H_{U C_i}` — a compression of the crossed product
> `A_U rtimes_alpha R` by the modular automorphism group of `|psi_S>` — has
> finite trace, and is therefore Type II_1, when `sigma_i` is bounded
> below; otherwise it is Type II_infinity.

**The trigger does not fire, and starting Lean is refused.** Two reasons,
both recorded so a later run can re-decide:

1. The claim is cited to Takesaki's duality theorem and is **already a
   theorem of operator algebra**, not a conjecture of this programme.
   Formalising someone else's published theorem buys this repository no
   physics.
2. The plan's own note applies with force: mathlib has no Tomita-Takesaki
   modular theory and no crossed products of von Neumann algebras, so the
   statement's primitive notions do not exist to formalise against. The
   obstruction is infrastructural, not a question of effort.

No `lean/` directory is created.

---

## What WP-7 decided about the symbolic branch

The package was commissioned to answer "does a whole branch exist?" It
answers: **the branch's one candidate result is real and published, and it
is in D0 — it has no route to a number on the sky that anyone has written
down.** Both of the plan's hopes for it fail: the trinity theorem does not
underwrite it (read 1), and the observer's energy bound is not derived
(read 2). What survives is a published dichotomy about operator-algebra
types whose connection to data nobody has made.

Recorded as a fact about the literature, which is what a D0 is. Not as
evidence that nothing is measurable.
