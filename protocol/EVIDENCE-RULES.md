# Evidence rules

Binding on every agent run in this repository. Violations invalidate a run
as research.

## 1. Citations

- A citation is usable only if the agent has retrieved the source in this
  run, or can give a locator precise enough to be checked: DOI, arXiv id,
  or journal volume and page.
- Author plus year is a **lead**, not a citation. Leads are allowed, and
  must be tagged `[LEAD]`.
- Never convert a lead into a full citation by inference. If the arXiv
  number was not retrieved, it is not known. A plausible arXiv number is
  worse than none, because it looks checkable and is not.
- Attribute claims to the person who made them, in a source where they
  made them. Not to a review that describes them, unless the review is
  cited as the source.
- When a paper is cited for a specific claim, state where in the paper
  (section or equation) if that is available.

## 2. Confidence tags

Every substantive claim carries exactly one:

- `[SOURCED]` Retrieved a primary source in this run that states it.
- `[LEAD]` Believed from background knowledge; locator not verified.
- `[INFERENCE]` The agent's own reasoning from sourced material. Must name
  the premises.
- `[UNKNOWN]` Could not establish. Say what would settle it.

`[INFERENCE]` is permitted and useful. Disguising it as `[SOURCED]` is the
failure mode this whole document exists to prevent.

## 3. Empty is an answer

If an approach does not fill a scaffold slot, write that it does not. Do
not fill the slot with what the approach would probably say. "Cluster B2
has no S7" is a finding. An invented S7 is noise that later runs will
inherit.

## 4. Disagreement claims

- To claim two approaches are **notational variants**, exhibit the mapping.
  Term by term. "These are essentially the same" is not a claim, it is a
  gesture.
- To claim two approaches **genuinely conflict**, name what differs: an
  allowed record, a probability, or a predicted observable. Different
  vocabulary is not conflict.
- To claim an approach is **wrong**, cite the argument and the responses to
  it. Live disputes get reported as live.

## 5. Representing positions

Describe each approach as its proponents describe it, using their terms,
before any assessment. A position summarised only through its critics is
a misrepresentation regardless of whether the criticism is good.

Where a proponent has changed position over time, say so and date it.

## 6. No smoothing

Do not resolve a tension by choosing softer language. If two sources
contradict each other, report the contradiction and say which source says
what. A survey that reads as consensus when the field has none is a false
result, even when every individual sentence is defensible.

## 7. Uncertainty about the scaffold itself

The scaffold in `../docs/common-scaffold.md` is provisional. If an approach
fits it badly, say where it breaks and why. Forcing a bad fit silently is
worse than reporting the misfit. A run that returns "S3 is the wrong
abstraction for Cluster F, here is why" has produced a real result.
