"""Register Wayback-archived official AP EAPCET papers (2024/2025) and write transcription task chunks.
Run after extract_ap.py has produced %TEMP%/pyq/wb/<snapshot>/index.json for each PDF in .harvest/pyq/ap_wb."""
import json, os, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
WB = Path(os.environ["TEMP"]) / "pyq" / "wb"
PAPERS = {  # snapshot file stem -> (year, key status)
    "20240525220116_QPK_18TH_MAY_SHIFT_1": (2024, "preliminary"),
    "20240525221301_QPK_19TH_MAY_SHIFT_2": (2024, "preliminary"),
    "20240525220507_QPK_20TH_MAY_SHIFT_1": (2024, "preliminary"),
    "20240525220254_QPK_20TH_MAY_SHIFT_2": (2024, "preliminary"),
    "20240525220521_QPK_21ST_MAY_SHIFT_1": (2024, "preliminary"),
    "20240525221206_QPK_21ST_MAY_SHIFT_2": (2024, "preliminary"),
    "20240525220800_QPK_22ND_MAY_SHIFT_1": (2024, "preliminary"),
    "20240525221124_QPK_22ND_MAY_SHIFT_2": (2024, "preliminary"),
    "20240525220202_QPK_23RD_MAY_SHIFT_1": (2024, "preliminary"),
    "20250528171503_QPK_23RD_MAY_SHIFT_2": (2025, "official (preliminary/final not stated)"),
    "20250528171539_QPK_24th_MAY_SHIFT_1": (2025, "official (preliminary/final not stated)"),
    "20250528171457_QPK_26th_MAY_SHIFT_1": (2025, "official (preliminary/final not stated)"),
    "20251101202017_QPK_26th_MAY_SHIFT_2": (2025, "official (preliminary/final not stated)"),
    "20250528171428_QPK_27th_MAY_SHIFT_1": (2025, "official (preliminary/final not stated)"),
    # archived copies truncated at 5 MB: only the questions before the cut are usable
    "20250717055637_QPK_21ST_MAY_SHIFT_1": (2025, "official (preliminary/final not stated)"),
    "20250717064841_QPK_21ST_MAY_SHIFT_2": (2025, "official (preliminary/final not stated)"),
    "20250717053336_QPK_22ND_MAY_SHIFT_1": (2025, "official (preliminary/final not stated)"),
    "20250717063340_QPK_22ND_MAY_SHIFT_2": (2025, "official (preliminary/final not stated)"),
}
reg = {}
for stem, (year, key) in PAPERS.items():
    ts, rest = stem.split("_", 1)
    m = re.match(r"QPK_(\d+)\w\w_MAY_SHIFT_(\d)", rest)
    day, sh = m.group(1), m.group(2)
    code = f"{year}-{day}-{sh}"
    reg[code] = {"year": year, "key": key, "label": f"{int(day)} May Shift {sh}",
                 "url": f"https://web.archive.org/web/{ts}/https://cets.apsche.ap.gov.in/EAPCET/PDF/EXAM_PAPER/{rest}.pdf"}
    idx = json.loads((WB / stem / "index.json").read_text())
    good = [r for r in idx if r["ok"] and r["key"]]
    truncated = len(good) < len(idx)
    if truncated:  # drop the last complete-looking question before the cut, to be safe
        lastok = max(r["n"] for r in good if all(x["ok"] for x in idx if x["n"] <= r["n"]))
        good = [r for r in good if r["n"] < lastok]
    reg[code]["usable"] = len(good)
    for lo, hi, name in [(1, 40, "m1"), (41, 80, "m2"), (81, 120, "p"), (121, 160, "c")]:
        items = [{"n": r["n"], "subject": r["subject"], "png": str(WB / stem / r["png"]).replace("\\", "/"),
                  "official_key": "ABCD"[r["key"] - 1]} for r in good if lo <= r["n"] <= hi]
        if items:
            for d in (ROOT / ".harvest/pyq/tasks", Path(os.environ["TEMP"]) / "pyq" / "tasks"):
                (d / f"{code}_{name}.json").write_text(json.dumps(items, indent=1))
(ROOT / ".harvest/pyq/papers.json").write_text(json.dumps(reg, indent=1))
for c, v in reg.items():
    print(c, v["usable"])
