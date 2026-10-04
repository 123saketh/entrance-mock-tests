# Question JSON schema (BITSAT mock)

Each file under `public/data/questions/` is a JSON array of Question objects:

```json
{
  "id": "phy-a-0001",
  "subject": "physics",
  "topic": "Rotational Motion",
  "difficulty": "medium",
  "stem": "A disc of mass $M$ and radius $R$ rolls without slipping... Find $v$.",
  "options": [
    { "key": "A", "text": "$\sqrt{gh}$" },
    { "key": "B", "text": "$\sqrt{\frac{4gh}{3}}$" },
    { "key": "C", "text": "$\sqrt{2gh}$" },
    { "key": "D", "text": "$\sqrt{\frac{gh}{2}}$" }
  ],
  "answer": "B",
  "explanation": "Energy conservation: $Mgh = \frac12 Mv^2 + \frac12 \cdot \frac12 MR^2 \cdot \frac{v^2}{R^2}$ ... Why others are wrong: A ... C ignores rotational KE ... D ...",
  "source": { "kind": "authored" }
}
```

Rules
- `subject`: one of `physics`, `chemistry`, `mathematics`, `english`, `reasoning`.
- `difficulty`: `easy` | `medium` | `hard`. Aim for roughly 30% easy, 50% medium, 20% hard (BITSAT level: NCERT class 11+12, speed-oriented, slightly easier than JEE Main).
- Exactly 4 options, keys A-D, exactly one correct, `answer` is that key. Distribute correct answers evenly across A/B/C/D.
- Math: LaTeX inside `$...$` (inline) or `$$...$$` (display). Rendered with KaTeX. In JSON, backslashes must be escaped (`\frac`). Chemical formulas: `H$_2$SO$_4$` or `$\mathrm{H_2SO_4}$`. Use `\n` for line breaks (e.g. passage paragraphs).
- No images. Questions must be fully answerable from text. For reasoning figure-series type questions, use text/letter/number patterns instead.
- `explanation`: worked solution PLUS a short note on why each wrong option is wrong (common trap). Keep under ~120 words unless a calculation needs more.
- `source.kind`: `authored` for original questions; `harvested` for imported ones, with `name`, `url`, `licence`.
- `id` must be globally unique. Use the prefix you were given.
- Every answer key MUST be verified (compute it, e.g. with `node -e`), wrong keys are the worst possible defect.

## Figures (images)

Questions may carry figures. Put image files (SVG preferred, PNG ok) under
`public/data/figures/<subfolder>/` and reference them by path relative to `public/data/`:

```json
{
  "stem": "Which option completes the series?",
  "stemImage": "figures/lr/lr-fig-0001-q.svg",
  "options": [
    { "key": "A", "text": "", "image": "figures/lr/lr-fig-0001-a.svg" },
    ...
  ],
  "explanationImage": "figures/lr/lr-fig-0001-x.svg"
}
```

- `stemImage` (optional): shown under the stem text.
- `options[].image` (optional): shown inside the option; `text` may be empty when the image is the option.
- `explanationImage` (optional): shown with the explanation.
- SVGs must be self-contained (no external refs, no scripts), with a `viewBox`, black strokes on a
  transparent/white background, and readable at ~300px wide (options ~140px). The app shows them on a white tile, so they work in dark mode too.

## Exam tags

`exams` (optional): restrict a question to specific exams, e.g. `["ts-eamcet", "ap-eamcet"]`.
Untagged questions are generic and can be drawn by any exam that has the subject.
Tag a question when its topic is outside another exam's syllabus (e.g. hyperbolic functions are
in the TS/AP Intermediate syllabus but not BITSAT).

## Previous-year questions

`pyq` (optional): set on questions taken from a real past paper, with a short label of the paper,
e.g. `"JEE Main 2025 · January"` or `"TS EAPCET 2024 · 9 May Shift 1"`. The app shows a **PYQ**
badge (paper name on hover, in the review and in the PDF) and offers a "Previous year questions" source filter.
