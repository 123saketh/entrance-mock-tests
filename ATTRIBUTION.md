# Attribution: harvested questions

`public/data/questions/harvested.json` (691 questions) contains MCQs adapted from the openly licensed datasets listed below. Each question's `source` field records the dataset name, URL, licence and the original question reference (`source.ref`).

The questions were changed from the originals as follows:
- Converted to the BITSAT mock schema.
- LaTeX normalised to `$...$`.
- Options split out of the question text.
- Transcription typos and garbled text repaired (logged in `.harvest/verify/*.result.json`).
- Worked solutions rewritten or added.
- Topics re-inferred.

Every imported question was independently re-solved. A question was kept only when the solution matched the source answer key.

## Sources used

| Source | URL | Licence | Imported | Notes |
|---|---|---|---|---|
| JEEBench (Arora et al., EMNLP 2023), JEE Advanced 2016–2023 | https://huggingface.co/datasets/daman1209arora/jeebench (code: https://github.com/dair-iitd/jeebench) | MIT | 97 (Phy 25, Chem 26, Math 46) | Single-correct "MCQ" type only. Dropped 3 that need a figure and 6 with tables. 1 dropped on re-solve (disputed key) and 1 for ambiguous wording. Official answer keys. Difficulty: hard. |
| PhysicsWallahAI JEE-Main-2025-Math | https://huggingface.co/datasets/PhysicsWallahAI/JEE-Main-2025-Math | Apache-2.0 | 345 (Math) | JEE Main 2025, Jan and Apr sessions; MCQ only. The transcriptions have many typos: 82 were repaired, and 9 were dropped as unrecoverable. 3 more were dropped as doubtful. Keys cross-checked against CK0607 (100/100 agree). Difficulty: medium. |
| eQOURSE JEE Main Question Bank | https://huggingface.co/datasets/eQOURSE/jee-main-questions | CC-BY-4.0 | 249 (Phy 50, Chem 56, Math 143) | Mock / test-series papers at JEE Main level. Kept only single-correct, image-free questions whose key matches the source's own worked solution. Excluded about 93 with Hindi (Kruti Dev) mojibake. On re-solving, 175 were cleaned and 22 dropped, including 4 keys that were wrong in the source. Difficulty mapped from the source's Easy/Moderate/Tough. |

**CC-BY-4.0 attribution:** questions from "JEE Main — Question Bank" by eQOURSE (https://huggingface.co/datasets/eQOURSE/jee-main-questions), licensed CC BY 4.0. Modified as described above.

## Used for verification only (not imported)

| Source | URL | Licence | Why |
|---|---|---|---|
| CK0607/2025-Jee-Mains-Question | https://huggingface.co/datasets/CK0607/2025-Jee-Mains-Question | Apache-2.0 | 250 JEE Main 2025 Jan maths questions, fully overlapping the PhysicsWallahAI Jan set. Used only to cross-check answer keys. |

## Examined and rejected

| Source | Reason |
|---|---|
| soughed/jee-main-questions, Grass-G/jee-main-questions | Mirrors of eQOURSE (duplicates). |
| nirantk/jeebench, macabdul9/jeebench_math, guanning-ai/jeebench-math, daman1209arora/jeebench_numeric | Mirrors or subsets of JEEBench, or numeric-only. |
| Reja1/jee-neet-benchmark (MIT) | Questions are page images (PNG), not text. |
| dipikakhullar/jee_mains_mm, dipikakhullar/jee_adjvanced_exams_mm | Multimodal (image) data; no usable text files. |
| rmahesh/JEE_Main_Hindi_Exams, rmahesh/JEE_Advanced_Hindi, rmahesh/JEE_Main_Hindi_Multimodal | Licence "unknown"; Hindi or image-based. |
| ruh-ai/grafite-jee-mains-qna-no-img, UtkarshM005/grafite-jee-mains-qna-no-img | No licence declared. |
| Aakali/jee, archit11/jee_math | No licence declared. |
| hymanshu/jee_mains_2025_shift1*, Optimus-Prym/Jee_main_2025_m_22, Naman712/Sad707/Jyotiradityaaaa/x128ga57 "2025-Jee-Mains-Question", Ajaysaini231/JEE-Main-2025-Math | Small re-uploads or duplicates of the 2025 maths papers already covered. |
| EduDevCommons/JEE-MAINS-ADVANCED, EduDevCommons/JEE-Mains-Dataset-includes-2026-Jan-Attempt, samyakbayar/JEEMainsDataset | Exam statistics (cutoffs, toppers), not questions. |
| toloka/JEEM | Not JEE: an Arabic visual QA benchmark. |
| GitHub search (`bitsat`, `bitsat questions`, `jee questions`, `jee mains dataset`, `jee main json`) | No openly licensed question banks found. Hits were quiz apps without licences, Java EE ("JEE") interview repos, or answer-key scrapers. |
| Coaching sites (Embibe, ExamSide, Vedantu, etc.) | Copyrighted; not scraped, per policy. |

**No open BITSAT-specific question dataset exists**, and no openly licensed English-proficiency or logical-reasoning datasets at BITSAT level were found. Those sections must be authored.

## Reproducing
`bash scripts/harvest/download.sh`, then `python scripts/harvest/build_harvested.py`, then `python scripts/harvest/validate.py`. The verification results in `.harvest/verify/` are needed to rebuild the same set.

## Past-year questions (PYQ): AP EAPCET / TS EAPCET

Files: `public/data/questions/pyq-ap-eamcet.json` (tagged `ap-eamcet`) and `pyq-ts-eamcet.json` (empty for now, see below).
Licence: official exam-authority releases, used for personal practice. Each question links to its source PDF.
Method: `scripts/pyq/extract_ap.py` reads each official TCS-iON master paper. Stems and options are images, and the key is the green tick icon. The script builds one image per question. The English text was transcribed into LaTeX, then every question was re-solved independently. Questions were dropped when they needed a figure, could not be read, were ill-posed, or the re-solved answer disagreed with the official key. The drop log is in `.harvest/pyq/drop_log.json`. To rebuild, run `python scripts/pyq/build_pyq.py`.

### AP EAPCET 2026 Engineering, APSCHE/JNTUK master papers with **preliminary** keys (no final keys published)
| Shift | URL | Status |
|---|---|---|
| 12 May S1/S2, 13 May S1/S2, 14 May S1/S2 | https://cets.apsche.ap.gov.in/EAPCET/PDF/EXAM_PAPER/QPK_{12,13,14}TH_MAY2026_SHIFT_{1,2}.pdf | used (all sections) |
| 15 May S1/S2, 18 May S1/S2 | https://cets.apsche.ap.gov.in/EAPCET/PDF/EXAM_PAPER/QPK_{15,18}TH_MAY2026_SHIFT_{1,2}.pdf | extracted, queued |

### AP EAPCET 2024 / 2025 Engineering: Wayback Machine copies of the official cets.apsche.ap.gov.in PDFs (registered in `.harvest/pyq/papers.json`)
- 2024 (the exam-papers page said "Preliminary Keys"): 18 May S1, 19 May S2, 20 May S1/S2, 21 May S1/S2, 22 May S1/S2, 23 May S1. All 9 are extracted (160 questions each) and queued.
- 2025 (the archive has no copy of the 2025 page, so the key status is unknown; labelled "official (preliminary/final not stated)"): 23 May S2, 24 May S1, 26 May S1/S2, 27 May S1 are complete. 21 May S1/S2 and 22 May S1/S2 are archived copies truncated at 5 MB, so only Q1 to about Q100-120 are usable. All are extracted and queued.
- Not usable: 2025 23 May S1 and 2025 19/20 May (truncated captures; 19/20 May are Agriculture anyway), and the 2024 16/17 May papers (Agriculture & Pharmacy).

### Skipped or blocked
| Source | Reason |
|---|---|
| TS (TG) EAPCET, all years | `eapcet.tsche.ac.in` no longer resolves (NXDOMAIN). The new site `eapcet.tgche.ac.in` only serves the 2026 "Master Question Paper With Final Key" after a candidate logs in with hall ticket number, registration number and date of birth. No older papers are linked, and the Wayback Machine has no PDFs from either host. **No TS questions were imported.** |
| AP EAPCET 2023 (`QPK_S1..S13.pdf`) | Not examined yet (Wayback copies exist). |
| Coaching or aggregator compilations | Not used, per policy. |
| Open datasets (GitHub/HF) | None found with EAMCET/EAPCET questions under an open licence. |
