# Known gaps in the seed

Candidate clusters and topics the hand-written seed map
(`approach-clusters.md`) does not develop. A run is asked to assess each
and say what it found; a gap reported as `[UNKNOWN]` is a fine outcome, a
gap silently dropped is not.

**This file exists so that the list can be checked without the seed.** It
was split out of `approach-clusters.md` because the adversary prompt
withholds that file — an adversary holding the seed cluster map mistakes
seed agreement for verification — while asking the adversary to check
coverage against this list. The two requirements were in direct conflict
as long as the list lived inside the withheld file, and Run 02 could not
work its S-7 surface at all. Splitting the file makes the file boundary
match the isolation boundary.

Nothing in the list is new; it is the same list, at the same wording, as
the `## Known gaps in this seed` section of `approach-clusters.md` at
commit `5fbc9af`.

---

- Wheeler-DeWitt and the problem of time as a cluster in its own right
  (Isham 1992; Kuchar; Anderson 2017) rather than background to A and B.
- Boundary-condition proposals for the wavefunction of the universe
  (Hartle & Hawking 1983; Vilenkin tunneling) and what they assume about
  observation.
- Self-locating uncertainty within Everettian branching as a bridge between
  A and E (Carroll & Sebens 2014).
- Thermal time and observer-dependent time (Connes & Rovelli; Rovelli &
  Smerlak).
- Information-theoretic and thermodynamic limits on physical record-keeping
  (Landauer-type constraints on what an internal observer can store).
- Observational cosmology's own treatment of the observer: cosmic variance,
  the single-realisation problem, and what "ensemble average" means when
  there is one sky.

---

## Adding to this list

A later run that finds a genuine gap adds it here rather than to
`approach-clusters.md`, and records which run found it. The list is
cumulative: an entry stays even after a run addresses it, because the
adversary's job is to check that a run said what it did about each entry,
not to work from a shrinking list.

A run that **resolves** an entry does not delete it. Note the run that
resolved it beside the entry.

## Entries added since the seed

(none yet)

## Citation warning

Every reference above is a lead, not a verified citation; several are given
by author and approximate year only. See `../protocol/EVIDENCE-RULES.md`.
