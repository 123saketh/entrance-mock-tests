# PYQ transcription task (AP EAPCET 2026 official master paper, Engineering)

You are given a task file (JSON array). Each item: {n, subject, png, official_key}. `png` is an image of one
question from the official APSCHE master question paper: the stem and options (1)-(4) each appear in English
followed by a Telugu translation. Options (1),(2),(3),(4) map to keys A,B,C,D. `official_key` is the
official (preliminary) key letter.

For EACH item:
1. Read the PNG with the Read tool (you can see images). Transcribe the ENGLISH text only (ignore Telugu).
2. DROP the question (log reason) if: it needs a figure/diagram/graph/circuit/table-image to answer; any
   part is illegible; you cannot faithfully reconstruct the math; or it is a "match the following"/
   assertion-type whose text is too garbled. (Match-the-list / statement questions are fine if they
   transcribe cleanly as text; use `\n` line breaks.)
3. Write math in LaTeX inside $...$ (KaTeX). Chemistry formulas like $\mathrm{H_2SO_4}$. Transcribe
   faithfully - do NOT fix or change numbers. Fix only obvious typography (e.g. "10-19" -> $10^{-19}$).
4. SOLVE it yourself independently (use python/sympy via Bash for any numerical/symbolic work; your own
   temp folder is given below). If your answer != official_key: re-check your transcription against the
   image; if still different, DROP with reason "key disagreement: mine X vs official Y (...)".
   If two options are both correct, or none is, DROP.
5. Keep: write an explanation (<100 words): concise worked solution + why the main distractors are wrong
   (common trap). LaTeX in $...$.
6. topic: short chapter label (e.g. "Matrices", "Definite Integrals", "Current Electricity",
   "Chemical Kinetics"). difficulty: easy|medium|hard by your judgement.

OUTPUT: write a JSON file (UTF-8, valid JSON, backslashes escaped as JSON requires) to the output path given,
an array of objects:
{"n": 7, "subject": "mathematics", "topic": "...", "difficulty": "medium",
 "stem": "...", "options": [{"key":"A","text":"..."},{"key":"B","text":"..."},{"key":"C","text":"..."},{"key":"D","text":"..."}],
 "answer": "B", "explanation": "..."}
`answer` MUST equal official_key. And write the drop log to the drops path: [{"n": 12, "reason": "..."}].
Write the JSON with python (json.dump(..., ensure_ascii=False)) to avoid escaping mistakes, and re-load it
to check it parses. Every input item must appear in exactly one of the two files.
Work steadily; correctness beats speed. Do not use any website. Do not edit any other files.
Final message: counts kept/dropped and list of key disagreements.

IMPORTANT (resumability): save progress incrementally. Keep your builder script in your temp folder and
re-run it to (re)write the output + drops files after every ~8 questions, so partial work survives an
interruption. If the output file already exists when you start, load it and continue from the first
unprocessed item instead of redoing work.
