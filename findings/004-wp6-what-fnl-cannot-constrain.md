# WP-6: the quantum-versus-classical discriminator is not a bispectrum, so `f_NL` cannot bound it

**Package:** WP-6 (`docs/RESEARCH-PLAN.md` §4), the unblocked half.
**Day:** 2026-11-05, cycle 5. Branch `research/auto-2026-11-05`.
**Status:** the dataset question is answered and it changes the package's
specification. The amplitude remains blocked on Maple job 001.
**Provisional on WP-1.**

No script: this cycle produced no number of its own. Every claim below is a
template definition or a shape statement read at primary level, and the
finding is structural rather than numerical — which is why it does not rest
on any quoted value.

---

## The finding

**All three-point correlation functions vanish in both states, so
Planck's `f_NL` constraints cannot discriminate between them at all.**

Martin & Vennin 2016 (`arXiv:1510.04038`), read as LaTeX source
(`discord.tex`), state it directly:

> All three-point correlation functions vanish in both the two-mode
> squeezed and classical states; hence one has to [go to the four-point
> function]

The discriminating statistic is therefore the **four-point** function, and
the paper characterises its shape:

> This one is not of the local type and, in fact, corresponds to a scale
> dependent `g_NL`, notably due to the presence of the `delta` terms.
> Therefore, it remains to generate templates corresponding to this
> structure in order to determine whether such a four-point function is
> already excluded or not.

`[SOURCED]`

### What Planck actually constrains

`data/README.md` poses exactly the right question for WP-6: *"which
template the quoted `f_NL` is a constraint on. A bound on the local
template is not a bound on an arbitrary higher-order correlator, and the
difference is the whole of WP-6."* Answered, from Planck 2018 results IX
(`arXiv:1905.05697`), abstract and §7 read as LaTeX source.

**Bispectrum** templates constrained: local, equilateral, orthogonal, plus
scale-dependent feature and resonance shapes, isocurvature and
parity-breaking cases.

**Trispectrum** templates constrained — §7 in full:

| Shape | What it is |
| --- | --- |
| `g_NL^local` | a cubic local transformation, `zeta = zeta_G + (9/25) g_NL zeta_G^3` |
| `g_NL^{pidot^4}` | an EFT-of-inflation operator shape |
| `g_NL^{(partial pi)^4}` | the other EFT operator shape at the same order |
| `g_NL^B` | a further shape at the same order in the EFT expansion |

**All four are scale-independent amplitudes on fixed shapes. The string
"scale-dependent" does not occur anywhere in §7.** `[SOURCED]`

So the discriminating four-point structure — a *scale-dependent* `g_NL`,
not of the local type — matches none of them.

**Conclusion: no published Planck non-Gaussianity constraint applies to
the quantum-versus-classical discriminator.** Not the `f_NL` bounds, which
are bispectrum amplitudes for a statistic that is identically zero on both
sides; and not the `g_NL` bounds, which are template-specific and whose
templates have the wrong shape.

This is the `data/README.md` warning coming true in the strongest available
form, and it was worth checking before any amplitude arrived to be compared
against the wrong number.

---

## This changes WP-6's specification, and the change is recorded not acted on

The plan's §4 instructs WP-6 to *"compute the discriminating correlator's
amplitude, and compare against Planck's `f_NL` constraints and the floor"*,
and the standing loop repeats it.

**The `f_NL` half of that instruction is void.** `f_NL` parameterises a
bispectrum; the bispectrum is identically zero in both the two-mode
squeezed state and the classical state, so there is nothing for an `f_NL`
bound to constrain. Comparing a trispectrum amplitude against an `f_NL`
limit would be a category error, and it is the sort that produces a
confident wrong number.

Per the standing loop, a rule I think is wrong gets argued against in the
log and left for the overseer rather than edited. `docs/RESEARCH-PLAN.md`
is **not** modified. The corrected target is: the four-point function,
against a template that does not yet exist.

---

## Decidability bin: D0, and the reason is not the instrument

**Run 01's quantum-versus-classical-ensemble question for perturbations:
D0, not yet posed.** Explicitly **not** D3 and **not** D4.

- Not D4: a differing observable **does** exist. The two states differ in
  the four-point function, and Martin & Vennin derive the difference. The
  positions do not predict identically.
- Not D3: nothing has been compared to the floor, and the obstruction is
  not that the signal is small. It is that the signal has no template.
- D0: `Delta` is not computable **as stated**, because the quantity it
  would be compared against does not exist. Nobody has posed this so that
  data could bear on it — which is a statement about the literature, not
  about nature, and is exactly what the plan's §1 says a D0 is.

### What would make it computable, which §6 calls the ledger's most valuable column

Two steps, in order, and the first is named by the source itself:

1. **Generate the template** for the scale-dependent `g_NL` structure
   Martin & Vennin derive. Their own sentence — "it remains to generate
   templates corresponding to this structure" — is the research queue entry.
   This is analytic work plus a shape computation. Cost: substantial but
   bounded, and it is the kind of thing a Maple round trip plus a
   numerical shape evaluation could do.
2. **Run Planck's trispectrum estimator against that template.** This is
   where the cost becomes concrete and where it stops on this machine:
   the trispectrum estimators in Planck 2018 IX are pixel-space, and
   **`healpy` is unavailable on this platform** with nothing substituting
   for it, as `env/requirements.txt` records. So step 2 **does not run
   here**, and saying the work does not run on this machine is the
   instructed response rather than writing a replacement.

**Cost to formulate: step 1 is tractable, step 2 is not available on this
platform.** That is the honest entry and it is more informative than a
single word would be.

---

## One thing read that is worth flagging but not building on

In the same passage, discussing a thermal state, Martin & Vennin note that
a factor in the non-Gaussian contribution is `(cosh beta_k1 - 1)^-1`, and:

> On super-Hubble scales, `beta_k1 -> 0` and this term blows up.

Taken at face value that suggests the classical state's intrinsic
non-Gaussianity grows without bound on exactly the scales the CMB measures,
which would make the discriminator large rather than small. **I am not
building on it.** I read the sentence and not the derivation around it, the
divergence is of a term in braces and not obviously of the observable, and
the paper draws no such conclusion. Recorded as `[LEAD]` with the locator
so a later cycle can read it properly, which is precisely the discipline
Run 02's sharpest finding was about.

If it survives reading, it would matter: the plan's WP-6 falsifier is *"if
the discriminating amplitude clears current constraints, this is D1 and
becomes the plan's new centrepiece"*, and a divergence on super-Hubble
scales is the shape of thing that could do that. It is not evidence yet.

---

## The kill criterion did not fire

`docs/RESEARCH-PLAN.md` §5: *"WP-6 dies if the discriminating correlator is
below the floor."*

It does not fire, and not because the correlator is large. The amplitude is
not computed — job 001 has not returned — and even with it, the comparison
could not be made, because the obstruction is the missing template rather
than the floor. A package cannot be killed by a criterion that has not been
evaluated, and reporting it as killed would be the substitution the plan's
§1 warns about: scoring a D0 as a D3.

---

## What remains blocked

Maple job 001 (`maple:queued`, issue michaelClucas/The-Observer-Problem#8)
settles whether the standard truncation of the squeezed state is a
legitimate state at all, which is Hsiang & Hu's unanswered objection, and
feeds the amplitude. It has not returned. So WP-6's numerical half is
blocked exactly as it was at the start of the day.

What is no longer blocked, and what this cycle bought: **when job 001
returns, the amplitude must not be compared against `f_NL`.** Without this
read, the next cycle would have done precisely that.
