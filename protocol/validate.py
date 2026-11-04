#!/usr/bin/env python3
"""Check a run's OUTPUT.json against protocol/output-schema.md.

    python protocol/validate.py runs/<run>/OUTPUT.json

Exits 0 when clean, 1 when any rule fails. It checks only whether the
contract was followed, never whether a claim is true: a file can pass this
and still be worthless, and that is what the adversary role is for.

A file declaring "schema_version": "v1" is checked against v1. Anything
else is read as v0, the schema Run 01 and Run 02 were written against. For
a v0 file the sourced-silence entries that v0 had no legal form for are
reported separately as SCHEMA GAP rather than as violations, so the v0 runs
can be validated without rewriting them.
"""

import json
import sys
from collections import Counter

SLOTS = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]
STATUS_V1 = {"filled", "empty", "denied", "misfit"}
STATUS_V0 = {"filled", "empty", "misfit"}
CONF = {"SOURCED", "LEAD", "INFERENCE", "UNKNOWN"}
VERDICT_V1 = {"notational_variant", "genuine_conflict", "non_competing",
              "unengaged", "unresolved"}
VERDICT_V0 = VERDICT_V1 - {"unengaged"}
DIFFERS = {"records", "probabilities", "observables"}
# A "dictionary" that says the mapping was not checked is not a dictionary.
NOT_A_DICTIONARY = ("not verified", "was not verified", "not been verified",
                    "unverified", "could not verify", "not checked")


def seq(x):
    return x if isinstance(x, list) else []


def text(x):
    return x if isinstance(x, str) else ""


class Report:
    def __init__(self):
        self.fail = []      # (rule, where, detail)
        self.gap = []       # (rule, where, detail) - v0 had no legal form
        self.note = []

    def bad(self, rule, where, detail):
        self.fail.append((rule, where, detail))

    def schema_gap(self, rule, where, detail):
        self.gap.append((rule, where, detail))


def check(doc, rep):
    v1 = doc.get("schema_version") == "v1"
    statuses = STATUS_V1 if v1 else STATUS_V0
    verdicts = VERDICT_V1 if v1 else VERDICT_V0
    rep.note.append("schema_version read as " + ("v1" if v1 else "v0"))

    clusters = seq(doc.get("clusters"))
    members = [(c.get("id"), m) for c in clusters for m in seq(c.get("members"))]

    # 15. member ids unique
    ids = [m.get("id") for _, m in members]
    for mid, n in Counter(ids).items():
        if n > 1:
            rep.bad(15, str(mid), "member id appears %d times" % n)
    known = {i for i in ids if i is not None}

    tally = Counter()
    for cid, m in members:
        mid = m.get("id") or "?"
        slots = m.get("slots") or {}

        # 1. all seven slot keys present
        for s in SLOTS:
            if s not in slots:
                rep.bad(1, "%s/%s" % (mid, s), "slot key absent")

        for s, e in slots.items():
            where = "%s/%s" % (mid, s)
            if not isinstance(e, dict):
                rep.bad(1, where, "slot entry is not an object")
                continue
            st, cf = e.get("status"), e.get("confidence")
            src, est = seq(e.get("sources")), seq(e.get("established_by"))
            tally[st] += 1

            # 2, 3. enums
            if st not in statuses:
                rep.bad(2, where, "status %r not in %s" % (st, sorted(statuses)))
            if cf not in CONF:
                rep.bad(3, where, "confidence %r not in %s" % (cf, sorted(CONF)))

            # 4. empty implies a null filler
            if st == "empty" and e.get("filler") not in (None, ""):
                rep.bad(4, where, "status empty but filler is non-null")

            if cf == "SOURCED":
                if st in ("filled", "denied"):
                    # 5. positive claim needs sources
                    if not src:
                        rep.bad(5, where, "SOURCED %s with no sources" % st)
                elif st in ("empty", "misfit"):
                    # 6. absence needs established_by
                    if not est:
                        if v1:
                            rep.bad(6, where, "SOURCED %s with no established_by" % st)
                        else:
                            rep.schema_gap(
                                6, where,
                                "sourced silence: v0 had no field for what was "
                                "read to establish an absence")
                    else:
                        for i, r in enumerate(est):
                            if not isinstance(r, dict) or not text(r.get("locator")):
                                rep.bad(6, "%s[%d]" % (where, i), "established_by entry has no locator")
                            elif not text(r.get("read")).strip():
                                rep.bad(6, "%s[%d]" % (where, i), "established_by entry has no 'read' field")
            elif cf in ("LEAD", "INFERENCE", "UNKNOWN"):
                # 7. no evidence alongside a disclaimer of evidence
                if src:
                    rep.bad(7, where, "%s with a non-empty sources" % cf)
                if est:
                    rep.bad(7, where, "%s with a non-empty established_by" % cf)

    # relations
    rels = seq(doc.get("relations"))
    for i, r in enumerate(rels):
        where = "relations[%d] %s~%s" % (i, r.get("a"), r.get("b"))
        v = r.get("verdict")
        if v not in verdicts:
            rep.bad(8, where, "verdict %r not in %s" % (v, sorted(verdicts)))
        if v == "notational_variant":
            d = text(r.get("dictionary")).strip()
            if not d:
                rep.bad(9, where, "notational_variant with no dictionary")
            elif any(p in d.lower() for p in NOT_A_DICTIONARY):
                rep.bad(9, where,
                        "dictionary states the mapping was not verified; "
                        "this verdict is unresolved")
        if v == "genuine_conflict" and r.get("differs_in") not in DIFFERS:
            rep.bad(10, where, "genuine_conflict differs_in=%r not in %s"
                    % (r.get("differs_in"), sorted(DIFFERS)))
        if v == "unengaged":
            if not seq(r.get("inference_premises")):
                rep.bad(11, where, "unengaged with no inference_premises")
            if not text(r.get("non_engagement_check")).strip():
                rep.bad(11, where, "unengaged with no non_engagement_check")
        if r.get("confidence") == "INFERENCE" and not seq(r.get("inference_premises")):
            rep.bad(12, where, "INFERENCE relation with no inference_premises")
        # 14. referential integrity
        for side in ("a", "b"):
            ref = r.get(side)
            if ref is not None and ref not in known:
                rep.bad(14, where, "%s=%r names no member" % (side, ref))

    for i, a in enumerate(seq(doc.get("assumptions"))):
        for key in ("held_by", "denied_by"):
            for ref in seq(a.get(key)):
                if ref not in known:
                    rep.bad(14, "assumptions[%d].%s" % (i, key),
                            "%r names no member" % ref)

    # 13. counts block
    counts = doc.get("counts")
    if counts is None:
        if v1:
            rep.bad(13, "counts", "v1 requires a counts block")
    else:
        actual = {
            "clusters": len(clusters),
            "members": len(members),
            "slot_entries": sum(tally.values()),
            "slots_filled": tally["filled"],
            "slots_empty": tally["empty"],
            "slots_denied": tally["denied"],
            "slots_misfit": tally["misfit"],
            "relations": len(rels),
        }
        for k, want in actual.items():
            if k in counts and counts[k] != want:
                rep.bad(13, "counts." + k, "declared %r, actual %d" % (counts[k], want))

    rep.note.append("clusters %d, members %d, slot entries %d  (%s)" % (
        len(clusters), len(members), sum(tally.values()),
        ", ".join("%s %d" % (k, v) for k, v in sorted(tally.items()) if k)))
    rep.note.append("relations %d  (%s)" % (
        len(rels), ", ".join("%s %d" % (k, v) for k, v in
                             sorted(Counter(r.get("verdict") for r in rels).items()) if k)))


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        doc = json.load(fh)

    rep = Report()
    check(doc, rep)

    for n in rep.note:
        print("   " + n)

    if rep.gap:
        print("\nSCHEMA GAP (%d) - v0 had no legal form for these; not the run's fault"
              % len(rep.gap))
        by = Counter(r for r, _, _ in rep.gap)
        for rule, n in sorted(by.items()):
            print("  rule %d: %d entries" % (rule, n))
        for rule, where, detail in rep.gap[:5]:
            print("    e.g. %s - %s" % (where, detail))
        if len(rep.gap) > 5:
            print("    ... and %d more" % (len(rep.gap) - 5))

    if rep.fail:
        print("\nVIOLATIONS (%d)" % len(rep.fail))
        for rule, where, detail in sorted(rep.fail, key=lambda x: (x[0], x[1])):
            print("  rule %-2d  %-28s %s" % (rule, where, detail))
        print("\nFAIL: %d violations, %d schema gaps" % (len(rep.fail), len(rep.gap)))
        return 1

    print("\nPASS: no violations" + (", %d schema gaps" % len(rep.gap) if rep.gap else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
