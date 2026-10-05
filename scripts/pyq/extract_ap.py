"""Extract questions from AP EAPCET master question papers (TCS iON "Online Question Paper
PDF Preview" format, published by APSCHE at cets.apsche.ap.gov.in/EAPCET).

In these PDFs every stem and option is an image (bilingual English/Telugu); the correct option
is marked by a green tick icon (16x16 image) and wrong ones by a red cross icon.

For each question we build a composite PNG (stem + options labelled 1-4) for transcription,
and record the official (preliminary) key from the tick icon.

usage: python scripts/pyq/extract_ap.py <pdf> <outdir>
"""
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont
import io

SUBJECTS = {"Mathematics": "mathematics", "Physics": "physics", "Chemistry": "chemistry"}


def pix_to_pil(doc, xref):
    pix = fitz.Pixmap(doc, xref)
    if pix.alpha or pix.n > 3:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


def decode(txt):
    """Some 2025 papers use a CID font whose text extracts as glyph ids (with NULs) offset by 29."""
    if chr(0) not in txt:
        return txt
    return "".join(c if c == chr(10) else chr(ord(c) + 29) for c in txt.replace(chr(0), ""))


def classify_icons(doc, xrefs):
    """Return {xref: 'tick'|'cross'} by colour (tick is green)."""
    out = {}
    for x in xrefs:
        im = pix_to_pil(doc, x)
        px = list(im.get_flattened_data()) if hasattr(im, "get_flattened_data") else list(im.getdata())
        g = sum(1 for r, gg, b in px if gg > r + 40 and gg > b + 20)
        rd = sum(1 for r, gg, b in px if r > gg + 60 and r > b + 40)
        out[x] = "tick" if g > rd else "cross"
    return out


def main(pdf, outdir):
    doc = fitz.open(pdf)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    # Gather events in reading order
    events = []  # (page, y, kind, payload)
    icon_xrefs = set()
    for pno in range(doc.page_count):
        page = doc[pno]
        for b in page.get_text("blocks"):
            txt = decode(b[4])
            y = b[1]
            mq = re.search(r"Question Number :\s*(\d+)", txt)
            if mq:
                events.append((pno, y, "q", int(mq.group(1))))
            elif "Options :" in txt:
                events.append((pno, y, "opts", None))
            else:
                for name in SUBJECTS:
                    if f"\n{name}\nSection Id" in "\n" + txt.replace("\xa0", "").strip() + "\n" or (
                        name in txt and "Section Id" in txt
                    ):
                        events.append((pno, y - 0.5, "sec", SUBJECTS[name]))
                        break
                for line in txt.split("\n"):
                    s = line.strip()
                    if s in ("1.", "2.", "3.", "4."):
                        events.append((pno, y, "optlabel", int(s[0])))
                        break
        for info in page.get_image_info(xrefs=True):
            x0, y0, x1, y1 = info["bbox"]
            if info["width"] <= 20 and info["height"] <= 20:
                icon_xrefs.add(info["xref"])
                events.append((pno, y1 - 0.2, "icon", info["xref"]))
            else:
                events.append((pno, y1, "img", (info["xref"], x0)))
    icons = classify_icons(doc, icon_xrefs)
    events.sort(key=lambda e: (e[0], e[1], {"sec": 0, "q": 1, "opts": 2, "icon": 3, "optlabel": 4, "img": 5}[e[2]]))

    questions = []
    cur = None
    subject = None
    state = None
    for pno, y, kind, payload in events:
        if kind == "sec":
            subject = payload
        elif kind == "q":
            cur = {"n": payload, "subject": ("mathematics" if payload <= 80 else "physics" if payload <= 120 else "chemistry"), "stem": [], "options": {}, "marks": {}}
            questions.append(cur)
            state = "stem"
            curopt = 0
        elif cur is None:
            continue
        elif kind == "opts":
            state = "opts"
        elif kind == "icon" and state == "opts":
            curopt += 1
            cur["marks"][curopt] = icons[payload]
            cur["options"].setdefault(curopt, [])
        elif kind == "img":
            xref, x0 = payload
            if state == "stem":
                cur["stem"].append(xref)
            elif state == "opts" and curopt:
                cur["options"][curopt].append(xref)
    index = []
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    for q in questions:
        ok = len(q["options"]) == 4 and all(q["options"].get(i) for i in range(1, 5)) and q["stem"]
        ticks = [i for i, m in q["marks"].items() if m == "tick"]
        rec = {"n": q["n"], "subject": q["subject"], "key": ticks[0] if len(ticks) == 1 else None,
               "nticks": len(ticks), "ok": bool(ok), "stem_imgs": len(q["stem"])}
        if ok:
            parts = []
            for x in q["stem"]:
                parts.append(("Q", pix_to_pil(doc, x)))
            for i in range(1, 5):
                for j, x in enumerate(q["options"][i]):
                    parts.append((f"({i})" if j == 0 else "", pix_to_pil(doc, x)))
            W = max(im.width for _, im in parts) + 70
            H = sum(im.height + 12 for _, im in parts) + 50
            canvas = Image.new("RGB", (W, H), "white")
            dr = ImageDraw.Draw(canvas)
            dr.text((5, 5), f"Q{q['n']}", fill="blue", font=font)
            yy = 40
            for lab, im in parts:
                if lab and lab != "Q":
                    dr.line([(0, yy - 6), (W, yy - 6)], fill=(200, 200, 200))
                    dr.text((5, yy + 5), lab, fill="blue", font=font)
                canvas.paste(im, (65, yy))
                yy += im.height + 12
            fn = f"q{q['n']:03d}.png"
            canvas.save(outdir / fn)
            rec["png"] = fn
        index.append(rec)
    (outdir / "index.json").write_text(json.dumps(index, indent=1))
    bad = [r for r in index if not r["ok"] or r["key"] is None]
    from collections import Counter
    print(pdf, len(index), Counter(r["subject"] for r in index), "bad:", [(r["n"], r["nticks"], r["ok"]) for r in bad])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
