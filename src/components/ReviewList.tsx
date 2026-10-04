import { useMemo, useState } from 'react';
import { marksFor, outcome, type Outcome } from '../lib/scoring';
import { SUBJECTS, SUBJECT_NAMES, type ExamState, type SubjectId } from '../types';
import { fmtTime } from './Results';
import Figure, { optionsAreFigures } from './Figure';
import PyqBadge from './PyqBadge';
import Rich from './Rich';

export type ReviewFilter = 'all' | Outcome | 'flagged';

interface Props {
  exam: ExamState;
  initialFilter: ReviewFilter;
  onBack: () => void;
  onPdf: () => void;
}

const BADGE: Record<Outcome, string> = {
  correct: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300',
  incorrect: 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300',
  skipped: 'bg-slate-200 text-slate-700 dark:bg-slate-800 dark:text-slate-300',
};

export default function ReviewList({ exam, initialFilter, onBack, onPdf }: Props) {
  const [filter, setFilter] = useState<ReviewFilter>(initialFilter);
  const [subject, setSubject] = useState<SubjectId | 'all'>('all');

  const numbered = useMemo(() => exam.items.map((item, i) => ({ item, n: i + 1 })), [exam]);
  const counts = useMemo(() => {
    const c = { all: numbered.length, correct: 0, incorrect: 0, skipped: 0, flagged: 0 };
    for (const { item } of numbered) {
      c[outcome(item)]++;
      if (item.flagged) c.flagged++;
    }
    return c;
  }, [numbered]);

  const shown = numbered.filter(({ item }) => {
    if (subject !== 'all' && item.question.subject !== subject) return false;
    if (filter === 'all') return true;
    if (filter === 'flagged') return item.flagged;
    return outcome(item) === filter;
  });
  const subjectsPresent = SUBJECTS.filter((s) => exam.items.some((i) => i.question.subject === s));

  return (
    <div className="space-y-4">
      <div className="sticky top-0 z-10 -mx-4 border-b border-slate-200 bg-slate-50/95 px-4 py-3 backdrop-blur dark:border-slate-800 dark:bg-slate-950/95">
        <div className="flex flex-wrap items-center gap-2">
          <button type="button" onClick={onBack} className="rounded-md border border-slate-300 px-3 py-1.5 text-sm font-medium hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800">
            ← Results
          </button>
          {(
            [
              ['all', 'All'],
              ['correct', 'Correct'],
              ['incorrect', 'Incorrect'],
              ['skipped', 'Skipped'],
              ['flagged', 'Marked'],
            ] as const
          ).map(([v, l]) => (
            <button
              key={v}
              type="button"
              onClick={() => setFilter(v)}
              className={`rounded-full px-3 py-1 text-xs font-semibold ${filter === v ? 'bg-indigo-600 text-white' : 'bg-slate-200 text-slate-700 hover:bg-slate-300 dark:bg-slate-800 dark:text-slate-300'}`}
            >
              {l} ({counts[v]})
            </button>
          ))}
          <button
            type="button"
            onClick={onPdf}
            className="ml-auto rounded-md border border-indigo-500 px-3 py-1 text-xs font-semibold text-indigo-700 hover:bg-indigo-50 dark:text-indigo-300 dark:hover:bg-indigo-950"
          >
            ⬇ PDF
          </button>
          <select
            value={subject}
            onChange={(e) => setSubject(e.target.value as SubjectId | 'all')}
            className="rounded border border-slate-300 bg-transparent px-2 py-1 text-sm dark:border-slate-700"
          >
            <option value="all">All subjects</option>
            {subjectsPresent.map((s) => (
              <option key={s} value={s}>
                {SUBJECT_NAMES[s]}
              </option>
            ))}
          </select>
        </div>
      </div>

      {shown.length === 0 && <p className="text-sm text-slate-500">No questions match this filter.</p>}

      {shown.map(({ item, n }) => {
        const q = item.question;
        const o = outcome(item);
        const marks = marksFor(item, exam.marking);
        return (
          <article key={q.id} className="rounded-xl border border-slate-200 bg-white p-5 dark:border-slate-800 dark:bg-slate-900">
            <div className="mb-3 flex flex-wrap items-center gap-2 text-xs">
              <span className="font-bold">Q{n}</span>
              <span className={`rounded px-1.5 py-0.5 font-bold ${BADGE[o]}`}>
                {o === 'correct' ? 'Correct' : o === 'incorrect' ? 'Incorrect' : 'Skipped'} · {marks > 0 ? `+${marks}` : marks}
                {o === 'incorrect' && ' (negative)'}
              </span>
              <PyqBadge question={q} showPaper />
              {item.bonus && <span className="rounded bg-amber-100 px-1.5 py-0.5 font-bold text-amber-800 dark:bg-amber-950 dark:text-amber-300">BONUS</span>}
              {item.flagged && <span className="text-purple-600">★ marked</span>}
              <span className="text-slate-500">
                {SUBJECT_NAMES[q.subject]} · {q.topic} · {q.difficulty}
              </span>
              <span className="ml-auto text-slate-400">time spent {fmtTime(item.timeMs)}</span>
            </div>

            <Rich text={q.stem} className="mb-4 text-[15px] leading-relaxed" />
            {q.stemImage && (
              <div className="-mt-2 mb-4">
                <Figure src={q.stemImage} alt={`Figure for question ${n}`} />
              </div>
            )}

            <ul className={optionsAreFigures(q.options) ? 'grid grid-cols-2 gap-2 sm:grid-cols-4' : 'space-y-2'}>
              {q.options.map((opt) => {
                const isAnswer = opt.key === q.answer;
                const isChosen = opt.key === item.selected;
                const cls = isAnswer
                  ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40'
                  : isChosen
                    ? 'border-rose-500 bg-rose-50 dark:bg-rose-950/40'
                    : 'border-slate-200 dark:border-slate-700';
                return (
                  <li key={opt.key} className={`flex items-start gap-3 rounded-lg border px-3 py-2 text-sm ${cls}`}>
                    <span className="mt-0.5 font-bold">{opt.key}.</span>
                    <span className="min-w-0 flex-1 overflow-x-auto">
                      {opt.text && <Rich text={opt.text} />}
                      {opt.image && <Figure src={opt.image} alt={`Option ${opt.key}`} size="option" />}
                    </span>
                    <span className="shrink-0 text-xs font-bold">
                      {isAnswer && isChosen && <span className="text-emerald-700 dark:text-emerald-400">✓ Your answer · Correct</span>}
                      {isAnswer && !isChosen && <span className="text-emerald-700 dark:text-emerald-400">✓ Correct answer</span>}
                      {!isAnswer && isChosen && <span className="text-rose-700 dark:text-rose-400">✗ Your answer · Wrong</span>}
                    </span>
                  </li>
                );
              })}
            </ul>
            {o === 'skipped' && <p className="mt-2 text-xs text-slate-500">You did not answer this question.</p>}

            <div className="mt-4 rounded-lg bg-slate-50 p-3 text-sm leading-relaxed dark:bg-slate-800/60">
              <p className="mb-1 text-xs font-bold uppercase text-slate-500">Explanation</p>
              <Rich text={q.explanation} />
              {q.explanationImage && (
                <div className="mt-2">
                  <Figure src={q.explanationImage} alt="Explanation figure" size="explanation" />
                </div>
              )}
              {q.source.kind === 'harvested' && (
                <p className="mt-2 text-xs text-slate-500">
                  Source: {q.source.url ? <a className="underline" href={q.source.url} target="_blank" rel="noreferrer">{q.source.name}</a> : q.source.name}
                  {q.source.licence && ` (${q.source.licence})`}
                </p>
              )}
            </div>
          </article>
        );
      })}
    </div>
  );
}
