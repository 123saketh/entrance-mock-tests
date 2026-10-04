import { describe, expect, it } from 'vitest';
import { BITSAT, presetTests } from '../exams';
import type { ExamItem, ExamState, Question, SubjectId } from '../types';
import { drawPaper } from './bank';
import { scoreExam, tally } from './scoring';
import { toHtml } from '../components/Rich';

function q(id: string, subject: SubjectId, answer: 'A' | 'B' | 'C' | 'D' = 'A', difficulty: Question['difficulty'] = 'medium'): Question {
  return {
    id,
    subject,
    topic: 't',
    difficulty,
    stem: 's',
    options: (['A', 'B', 'C', 'D'] as const).map((k) => ({ key: k, text: k })),
    answer,
    explanation: 'e',
    source: { kind: 'authored' },
  };
}
const item = (question: Question, selected: ExamItem['selected'], bonus = false): ExamItem => ({
  question,
  selected,
  flagged: false,
  visited: true,
  bonus,
  timeMs: 1000,
});

describe('BITSAT marking (+3 / -1 / 0)', () => {
  it('tallies correct, incorrect, skipped and negative marks', () => {
    const t = tally(
      [item(q('1', 'physics'), 'A'), item(q('2', 'physics'), 'B'), item(q('3', 'physics'), null), item(q('4', 'physics'), 'A')],
      BITSAT.marking,
    );
    expect(t).toMatchObject({ correct: 2, incorrect: 1, skipped: 1, attempted: 3, positive: 6, negative: 1, net: 5, maxMarks: 12, accuracy: 67 });
  });

  it('keeps max marks at the main paper and adds bonus marks on top', () => {
    const exam = {
      marking: BITSAT.marking,
      items: [item(q('1', 'physics'), 'A'), item(q('2', 'chemistry'), 'A'), item(q('b1', 'reasoning'), 'A', true)],
      bonusStartIndex: 2,
      msElapsed: 0,
    } as unknown as ExamState;
    const r = scoreExam(exam);
    expect(r.overall.net).toBe(9);
    expect(r.overall.maxMarks).toBe(6);
    expect(r.bonus?.net).toBe(3);
    expect(r.sections.map((s) => s.subject)).toEqual(['physics', 'chemistry', 'reasoning']);
  });
});

describe('paper pattern', () => {
  it('matches the 2026 brochure: 130 Qs, 180 min, bonus 3 each from P/C/M/LR', () => {
    expect(BITSAT.sections.reduce((n, s) => n + s.count, 0)).toBe(130);
    expect(BITSAT.durationMin).toBe(180);
    expect(BITSAT.bonus?.sections).toEqual([
      { subject: 'physics', count: 3 },
      { subject: 'chemistry', count: 3 },
      { subject: 'mathematics', count: 3 },
      { subject: 'reasoning', count: 3 },
    ]);
    const presets = presetTests(BITSAT);
    expect(presets.find((p) => p.id === 'bitsat-physics')?.minutes).toBe(42);
  });

  it('draws without repeats, keeps bonus disjoint, and respects exam tags', () => {
    const questions: Question[] = [];
    for (const s of ['physics', 'chemistry', 'english', 'reasoning', 'mathematics'] as const)
      for (let i = 0; i < 60; i++) questions.push(q(`${s}-${i}`, s, 'A', (['easy', 'medium', 'hard'] as const)[i % 3]));
    questions.push({ ...q('eamcet-only', 'physics'), exams: ['eamcet'] });
    const { main, bonus, shortfalls } = drawPaper({ questions }, 'bitsat', BITSAT.sections, BITSAT.bonus!.sections, 'all', {});
    expect(main).toHaveLength(130);
    expect(bonus).toHaveLength(12);
    expect(shortfalls).toEqual([]);
    const all = [...main, ...bonus].map((x) => x.id);
    expect(new Set(all).size).toBe(all.length);
    expect(all).not.toContain('eamcet-only');
    expect(main.slice(0, 30).every((x) => x.subject === 'physics')).toBe(true);
  });
});

describe('math rendering', () => {
  it('escapes plain text and renders $..$ with KaTeX', () => {
    const html = toHtml('<b>x</b> costs \\$5 and $x^2$');
    expect(html).toContain('&lt;b&gt;');
    expect(html).toContain('$5');
    expect(html).toContain('katex');
  });
});
