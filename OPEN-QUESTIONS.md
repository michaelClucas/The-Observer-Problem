# Open questions for the overseer

Questions an unattended session could not answer and did not stop for.

Append an entry, take the reversible default, mark the affected output
`provisional on Q-n`, and carry on. The overseer answers these between
days. **Append-only**: an answered question is marked answered in place,
with the answer and the date, never deleted.

```
## Q-n. <the question in one line>

**Raised:** YYYY-MM-DD, cycle N, WP-x
**Blocks:** what is provisional until this is answered
**Options:** each with its consequence
**Default taken:** which, and why it is reversible
**Answer:** (overseer, YYYY-MM-DD)
```

An entry whose default is **not** reversible does not belong here. Those
are stop conditions: the session halts that branch and says so in the day
log, because taking an irreversible default on nobody's authority is worse
than losing a day.

---

<!-- entries below, newest last -->
## Q-1. P-1 is confirmed but the trade-off IS stated in print. Does the clock / algebraic branch die?

**Raised:** 2026-11-05, cycle 1, WP-7
**Blocks:** whether the clock / algebraic branch is live. Nothing else; no
Maple job and no compute depends on the answer, for the reason under
"Default taken".

**The situation.** `docs/RESEARCH-PLAN.md` §5 reads: *"The clock /
algebraic branch dies if WP-7 confirms P-1. The trade-off then has no
published basis, is one run's inference, and gets no Maple time until
someone states it in print."* Both clauses were checked today at primary
source level and they came apart:

- **The trigger fired.** arXiv:1912.00033 §V states the trinity
  equivalence's hypothesis as a *continuous non-degenerate* spectrum, with
  boundedness raised in §V and explicitly discharged, and two of its three
  admissible clock examples bounded. P-1 is `CONFIRMED` by the settlement
  condition P-1 itself named. Run 01 relation 7's inference "so the
  compatibility claim and the spectrum question are not independent" is
  withdrawn.
- **The rationale is false.** arXiv:2405.00114 (De Vuyst, Eccles, Höhn &
  Kirklin) states the trade-off in print, both ends and the dichotomy: an
  ideal clock has spectrum `R`, tells time sharply, and gives
  Type II_infinity with no maximum entropy state; a clock bounded below
  tells time fuzzily and gives Type II_1 with a finite trace and a maximum
  entropy state. They further state that CLPW's imposed lower bound is
  *equivalent* to starting from non-ideal clocks with non-trivial
  projectors. Run 01's open question 3 is thereby answered yes.

So the provenance Run 01 gave for the trade-off was wrong, and the
trade-off has a better provenance than Run 01 claimed. The kill criterion
did not anticipate that combination and I cannot resolve it from the plan
as written. Quotations and locators are in
`findings/001-wp7-clock-spectrum-reads.md`.

**Options:**

1. **Branch dies, as the trigger says.** Consequence: the clock trade-off
   closes as a D0 with its publication recorded, and no further agent time
   goes to it. Cost: closes a question whose stated reason for closing is
   now known to be false, which is the kind of move this repository's
   protocol exists to prevent.
2. **Branch lives, because the rationale failed.** Consequence: the
   trade-off is a published dichotomy and the live question becomes "what
   would connect an operator-algebra type to a sky observable", which is
   the D0 column. Cost: that question has no identified route and no cost
   estimate, so the branch would be live without being workable — the
   condition under which a programme manufactures work.
3. **Branch is reclassified rather than killed or revived:** the trade-off
   is recorded as published, real, and **D0 with unknown cost to
   formulate**, and the branch is neither live nor dead but parked behind
   a named precondition (someone exhibits a cosmological observable
   sensitive to the algebra type). Consequence: no agent time, no claim
   that the question is undecidable, and a condition that would reopen it.
   **Recommended.** It is the only option that keeps both of today's
   findings true.

**Default taken:** option 3's *operational content only* — no Maple job is
filed for the clock trade-off and no symbolic work is started on it, while
the branch's formal status in the plan is left unchanged pending this
answer. Reversible in full, and it costs nothing, because
`docs/RESEARCH-PLAN.md` §3 already rejects the clock-spectrum question as
Maple work on grounds independent of Q-1 — "Maple has no natural handle on
these, and a plausible-looking Maple manipulation of an operator algebra
would be worse than no result". So the Maple queue and the day's compute
are unaffected by either answer, and nothing downstream has been built on
the default.

**Note on what I did not do.** I did not edit §5's kill criterion, and I
did not restate the trade-off in a vocabulary where it sounds decidable.
The D0 verdict with an unknown formulation cost is the honest entry and it
is recorded as such.

**Answer:** (overseer, 2026-11-10; written by relay generation 1 on the
overseer's explicit delegation, "answer them yourself") **Option 3.** The
trade-off is recorded as published (arXiv:2405.00114) and real, and binned
**D0, cost to formulate unknown**. The clock / algebraic branch is neither
killed nor revived: it is **parked** behind one named precondition, that
someone exhibits a cosmological observable sensitive to the algebra type
(II_1 versus II_infinity). Until then it gets no agent time and no Maple
job. `docs/RESEARCH-PLAN.md` §5 is not edited by this answer; the branch's
kill criterion is read as superseded for this branch by the parking
condition. Reason: it is the only option under which both 2026-11-05
findings in `findings/001` stay true, and it changes no work already done,
since the default taken was operationally identical.

---

