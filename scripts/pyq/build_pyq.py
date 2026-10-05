"""Assemble PYQ bank files from per-chunk transcriptions.

Inputs : .harvest/pyq/transcribed/<shift>_<chunk>.json (+ .drops.json) produced by transcribing the
         composites made by extract_ap.py; .harvest/pyq/tasks/<shift>_<chunk>.json (official keys).
Outputs: public/data/questions/pyq-ap-eamcet.json, pyq-ts-eamcet.json
usage: python scripts/pyq/build_pyq.py
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TR = ROOT / ".harvest/pyq/transcribed"
TASKS = ROOT / ".harvest/pyq/tasks"
OUT = ROOT / "public/data/questions"

AP_BASE = "https://cets.apsche.ap.gov.in/EAPCET/PDF/EXAM_PAPER/"
# shift code -> {year, url, label, key}. 2026 codes are "<day>-<shift>"; older years "<year>-<day>-<shift>"
# (registered in .harvest/pyq/papers.json, written by scripts/pyq/fetch_wayback.py).
PAPERS = {
    f"{d}-{s}": {"year": 2026, "url": AP_BASE + f"QPK_{d}TH_MAY2026_SHIFT_{s}.pdf",
                 "label": f"{d} May Shift {s}", "key": "preliminary"}
    for d in ("12", "13", "14", "15", "18") for s in ("1", "2")
}
_reg = ROOT / ".harvest/pyq/papers.json"
if _reg.exists():
    PAPERS.update(json.loads(_reg.read_text(encoding="utf-8")))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def build_ap():
    out, seen, dropped, dups, mism = [], {}, [], [], []
    files = sorted(p for p in TR.glob("*.json") if not p.name.endswith(".drops.json"))
    for p in files:
        shift, chunk = p.stem.split("_")
        task = {t["n"]: t for t in json.loads((TASKS / p.name).read_text(encoding="utf-8"))}
        P = PAPERS[shift]
        year, label = P["year"], P["label"]
        for q in json.loads(p.read_text(encoding="utf-8")):
            t = task.get(q["n"])
            if t is None or q.get("answer") != t["official_key"]:
                mism.append((shift, q["n"]))
                continue
            opts = q["options"]
            if [o["key"] for o in opts] != list("ABCD") or not all(o["text"].strip() for o in opts):
                mism.append((shift, q["n"], "options"))
                continue
            k = norm(q["stem"]) + "|" + "|".join(norm(o["text"]) for o in opts)
            if k in seen:
                dups.append((shift, q["n"], seen[k]))
                continue
            seen[k] = (shift, q["n"])
            d, s = shift.split("-")[-2:]
            out.append({
                "id": f"pyq-ap-{year}-{d}{s}-{q['n']:03d}",
                "subject": t["subject"],
                "topic": q["topic"],
                "difficulty": q["difficulty"],
                "stem": q["stem"],
                "options": [{"key": o["key"], "text": o["text"]} for o in opts],
                "answer": q["answer"],
                "explanation": q["explanation"],
                "exams": ["ap-eamcet"],
                "pyq": f"AP EAPCET {year} · {label}",
                "source": {
                    "kind": "harvested",
                    "name": f"AP EAPCET {year} (official master paper with {P['key']} key, {label}, Q{q['n']})"
                    + (" via Wayback Machine copy" if "web.archive.org" in P["url"] else ""),
                    "url": P["url"],
                    "licence": "Official exam-authority release; for personal practice",
                },
            })
        dp = TR / f"{p.stem}.drops.json"
        if dp.exists():
            for d in json.loads(dp.read_text(encoding="utf-8")):
                dropped.append((shift, d["n"], d["reason"]))
    return out, dropped, dups, mism


def main():
    ap, dropped, dups, mism = build_ap()
    (OUT / "pyq-ap-eamcet.json").write_text(json.dumps(ap, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "pyq-ts-eamcet.json").write_text("[]\n", encoding="utf-8")
    print("AP kept", len(ap))
    print(Counter((q["pyq"], q["subject"]) for q in ap))
    print("subject totals", Counter(q["subject"] for q in ap))
    print("answers", Counter(q["answer"] for q in ap), "difficulty", Counter(q["difficulty"] for q in ap))
    print("dropped", len(dropped), "dups", dups, "mismatch", mism)
    kd = [d for d in dropped if "disagree" in d[2].lower()]
    print("key disagreements:", len(kd))
    for d in kd:
        print("  ", d)
    reasons = Counter(re.split(r"[:(]", d[2])[0].strip().lower()[:40] for d in dropped)
    print(reasons.most_common(15))
    (ROOT / ".harvest/pyq/drop_log.json").write_text(json.dumps(dropped, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
