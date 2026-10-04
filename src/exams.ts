import type { ExamPattern, SectionSpec, SubjectId } from './types';

/**
 * BITSAT-2026, per the official admissions brochure (section 4, "Test Format"):
 *  - 130 MCQs, 3 hours, no per-part time limit, answers can be changed freely.
 *  - +3 correct, -1 wrong, 0 unattempted. One option only.
 *  - Answer all 130 (no skips) with time left -> optional 12 extra questions,
 *    3 each from Physics, Chemistry, Mathematics and Logical Reasoning. Once taken,
 *    the 130 cannot be revisited.
 */
export const BITSAT: ExamPattern = {
  id: 'bitsat',
  name: 'BITSAT',
  fullName: 'BITS Admission Test',
  status: 'ready',
  durationMin: 180,
  marking: { correct: 3, wrong: -1, skipped: 0 },
  sections: [
    { subject: 'physics', count: 30 },
    { subject: 'chemistry', count: 30 },
    { subject: 'english', count: 10 },
    { subject: 'reasoning', count: 20 },
    { subject: 'mathematics', count: 40 },
  ],
  bonus: {
    sections: [
      { subject: 'physics', count: 3 },
      { subject: 'chemistry', count: 3 },
      { subject: 'mathematics', count: 3 },
      { subject: 'reasoning', count: 3 },
    ],
    rule:
      'You have answered all 130 questions. You may attempt 12 extra questions (3 each from Physics, Chemistry, Mathematics and Logical Reasoning). Once you opt in you can NOT go back to change any of the 130 earlier answers. Negative marking still applies.',
  },
  notes: [
    '130 questions · 180 minutes · no sectional time limit',
    '+3 for correct, −1 for wrong, 0 for unattempted',
    'Answer all 130 to unlock 12 bonus questions (3 each P, C, M, LR). After opting in, earlier answers are locked.',
    'No calculators in the real exam — practise mental arithmetic.',
    'Tie-break order: Maths, then Physics, then Chemistry.',
  ],
};

/**
 * TG EAPCET (TS EAMCET), Engineering stream. 160 MCQs in 3 hours on the TG
 * Intermediate syllabus (TS-EAMCET_Syllabus-E.pdf); +1 per correct answer, no
 * negative marking, so every question should be attempted.
 */
export const TS_EAMCET: ExamPattern = {
  id: 'ts-eamcet',
  name: 'TS EAMCET',
  fullName: 'TG EAPCET (Engineering)',
  status: 'coming-soon',
  durationMin: 180,
  marking: { correct: 1, wrong: 0, skipped: 0 },
  sections: [
    { subject: 'mathematics', count: 80 },
    { subject: 'physics', count: 40 },
    { subject: 'chemistry', count: 40 },
  ],
  notes: [
    '160 questions · 180 minutes · Maths 80, Physics 40, Chemistry 40',
    '+1 for correct, no negative marking — never leave a question blank',
    'Syllabus: Telangana Intermediate (1st & 2nd year)',
  ],
};

/** AP EAPCET (AP EAMCET), Engineering stream. Same shape as TG, AP Intermediate syllabus. */
export const AP_EAMCET: ExamPattern = {
  id: 'ap-eamcet',
  name: 'AP EAMCET',
  fullName: 'AP EAPCET (Engineering)',
  status: 'coming-soon',
  durationMin: 180,
  marking: { correct: 1, wrong: 0, skipped: 0 },
  sections: [
    { subject: 'mathematics', count: 80 },
    { subject: 'physics', count: 40 },
    { subject: 'chemistry', count: 40 },
  ],
  notes: [
    '160 questions · 180 minutes · Maths 80, Physics 40, Chemistry 40',
    '+1 for correct, no negative marking — never leave a question blank',
    'Syllabus: AP Intermediate (1st & 2nd year)',
  ],
};

/**
 * Registered exams, in side-menu order. Subject pools are shared; tag
 * exam-specific questions with `exams: ["<id>"]`. Flip `status` to 'ready' once an
 * exam's question bank has been reviewed.
 */
export const EXAMS: ExamPattern[] = [BITSAT, TS_EAMCET, AP_EAMCET];

export function findExam(id: string | null | undefined): ExamPattern {
  return EXAMS.find((e) => e.id === id) ?? BITSAT;
}

/** Minutes per question at full-paper pace (180 / 130 ≈ 1.38). */
export function paceMinutes(pattern: ExamPattern, questionCount: number): number {
  const total = pattern.sections.reduce((n, s) => n + s.count, 0);
  return Math.max(1, Math.round((pattern.durationMin / total) * questionCount));
}

export interface PresetTest {
  id: string;
  title: string;
  description: string;
  sections: SectionSpec[];
  /** Minutes at exam pace. */
  minutes: number;
  withBonus: boolean;
  kind: 'full' | 'subject';
}

/** Full mock plus one sectional test per subject at real-paper size and pace. */
export function presetTests(pattern: ExamPattern): PresetTest[] {
  const full: PresetTest = {
    id: `${pattern.id}-full`,
    title: `Full ${pattern.name} mock`,
    description: pattern.sections.map((s) => `${s.count} ${short(s.subject)}`).join(' · '),
    sections: pattern.sections,
    minutes: pattern.durationMin,
    withBonus: Boolean(pattern.bonus),
    kind: 'full',
  };
  const sectional = pattern.sections.map<PresetTest>((s) => ({
    id: `${pattern.id}-${s.subject}`,
    title: `${label(s.subject)} sectional`,
    description: `${s.count} questions, same as the real paper (${pattern.marking.wrong === 0 ? 'no negative marking' : `+${pattern.marking.correct} / ${pattern.marking.wrong}`})`,
    sections: [s],
    minutes: paceMinutes(pattern, s.count),
    withBonus: false,
    kind: 'subject',
  }));
  const combos: PresetTest[] = [];
  const pick = (subjects: SubjectId[]) => pattern.sections.filter((s) => subjects.includes(s.subject));
  const count = (ss: SectionSpec[]) => ss.reduce((n, s) => n + s.count, 0);
  // Combined tests only make sense when they are a strict subset of the paper.
  const pcm = pick(['physics', 'chemistry', 'mathematics']);
  if (pcm.length === 3 && pcm.length < pattern.sections.length) {
    combos.push({
      id: `${pattern.id}-pcm`,
      title: 'PCM combined',
      description: `Physics + Chemistry + Maths only (${count(pcm)} questions)`,
      sections: pcm,
      minutes: paceMinutes(pattern, count(pcm)),
      withBonus: false,
      kind: 'subject',
    });
  }
  const engLr = pick(['english', 'reasoning']);
  if (engLr.length === 2) {
    combos.push({
      id: `${pattern.id}-englr`,
      title: 'English + Reasoning',
      description: `Part III of the paper (${count(engLr)} questions)`,
      sections: engLr,
      minutes: paceMinutes(pattern, count(engLr)),
      withBonus: false,
      kind: 'subject',
    });
  }
  return [full, ...sectional, ...combos];
}

function short(s: SubjectId): string {
  return { physics: 'Phy', chemistry: 'Chem', english: 'Eng', reasoning: 'LR', mathematics: 'Maths' }[s];
}
function label(s: SubjectId): string {
  return {
    physics: 'Physics',
    chemistry: 'Chemistry',
    english: 'English',
    reasoning: 'Logical Reasoning',
    mathematics: 'Mathematics',
  }[s];
}
