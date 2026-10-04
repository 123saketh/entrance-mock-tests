import {
  SUBJECTS,
  type ExamItem,
  type ExamResult,
  type ExamState,
  type MarkingScheme,
  type Tally,
} from '../types';

export type Outcome = 'correct' | 'incorrect' | 'skipped';

export function outcome(item: ExamItem): Outcome {
  if (item.selected === null) return 'skipped';
  return item.selected === item.question.answer ? 'correct' : 'incorrect';
}

export function marksFor(item: ExamItem, m: MarkingScheme): number {
  const o = outcome(item);
  return o === 'correct' ? m.correct : o === 'incorrect' ? m.wrong : m.skipped;
}

export function tally(items: ExamItem[], m: MarkingScheme): Tally {
  let correct = 0;
  let incorrect = 0;
  let skipped = 0;
  let timeMs = 0;
  for (const it of items) {
    const o = outcome(it);
    if (o === 'correct') correct++;
    else if (o === 'incorrect') incorrect++;
    else skipped++;
    timeMs += it.timeMs;
  }
  const positive = correct * m.correct;
  const negative = incorrect * Math.abs(m.wrong);
  const attempted = correct + incorrect;
  return {
    total: items.length,
    attempted,
    correct,
    incorrect,
    skipped,
    positive,
    negative,
    net: positive - negative + skipped * m.skipped,
    maxMarks: items.length * m.correct,
    accuracy: attempted === 0 ? 0 : Math.round((correct / attempted) * 100),
    timeMs,
  };
}

export function scoreExam(exam: ExamState): ExamResult {
  const m = exam.marking;
  const bonusTaken = exam.bonusStartIndex !== null;
  const mainItems = exam.items.filter((i) => !i.bonus);
  const bonusItems = exam.items.filter((i) => i.bonus);

  const sections = SUBJECTS.map((subject) => ({
    subject,
    ...tally(
      exam.items.filter((i) => i.question.subject === subject),
      m,
    ),
  })).filter((s) => s.total > 0);

  const topics = new Map<string, { subject: (typeof SUBJECTS)[number]; topic: string; correct: number; total: number }>();
  for (const it of exam.items) {
    const key = `${it.question.subject}|${it.question.topic}`;
    const t = topics.get(key) ?? { subject: it.question.subject, topic: it.question.topic, correct: 0, total: 0 };
    t.total++;
    if (outcome(it) === 'correct') t.correct++;
    topics.set(key, t);
  }

  const overall = tally(exam.items, m);
  // Max marks shown against the main paper; bonus marks are extra on top.
  overall.maxMarks = mainItems.length * m.correct;

  const result: ExamResult = {
    overall,
    sections,
    bonusTaken,
    durationMs: exam.msElapsed,
    topicStats: [...topics.values()].sort((a, b) => a.correct / a.total - b.correct / b.total),
  };
  if (bonusTaken) result.bonus = tally(bonusItems, m);
  return result;
}
