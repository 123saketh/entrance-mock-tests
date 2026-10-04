import { useMemo, useState } from 'react';
import { paceMinutes, presetTests, type PresetTest } from '../exams';
import {
  SUBJECT_NAMES,
  type AttemptRecord,
  type ExamPattern,
  type SectionSpec,
  type SourceFilter,
  type SubjectId,
  type TimerMode,
} from '../types';

export interface StartOptions {
  title: string;
  kind: 'full' | 'subject' | 'custom';
  sections: SectionSpec[];
  withBonus: boolean;
  /** null = untimed. */
  minutes: number | null;
  allowPause: boolean;
  source: SourceFilter;
}

interface Props {
  pattern: ExamPattern;
  counts: Record<SourceFilter, Record<SubjectId, number>>;
  history: AttemptRecord[];
  hasSavedExam: boolean;
  hasLastResult: boolean;
  seenTotal: number;
  onStart: (opts: StartOptions) => void;
  onResume: () => void;
  onDiscardSaved: () => void;
  onOpenLast: () => void;
  onOpenAttempt: (record: AttemptRecord, then: 'review' | 'pdf') => void;
  onResetSeen: () => void;
  onClearHistory: () => void;
}

const btn = 'rounded-md px-4 py-2 text-sm font-semibold transition disabled:opacity-40';
const card = 'rounded-xl border border-slate-200 bg-white p-5 dark:border-slate-800 dark:bg-slate-900';

export default function StartScreen(p: Props) {
  const { pattern } = p;
  const presets = useMemo(() => presetTests(pattern), [pattern]);
  const [source, setSource] = useState<SourceFilter>('all');
  const total = (f: SourceFilter) => Object.values(p.counts[f]).reduce((n, c) => n + c, 0);
  const sourceOptions = (
    [
      ['all', 'All sources'],
      ['authored', `${pattern.name}-style originals`],
      ['pyq', 'Previous year questions (PYQ)'],
      ['harvested', 'Other imported practice sets'],
    ] as const
  ).filter(([v]) => v === 'all' || total(v) > 0);
  const [timerMode, setTimerMode] = useState<TimerMode>('exam');
  const [customMin, setCustomMin] = useState(60);
  const [allowPause, setAllowPause] = useState(true);

  // Custom test builder.
  const [custom, setCustom] = useState<Record<SubjectId, number>>(
    () => Object.fromEntries(pattern.sections.map((s) => [s.subject, 0])) as Record<SubjectId, number>,
  );
  const customSections = pattern.sections
    .map((s) => ({ subject: s.subject, count: custom[s.subject] ?? 0 }))
    .filter((s) => s.count > 0);
  const customTotal = customSections.reduce((n, s) => n + s.count, 0);

  const avail = p.counts[source];
  const minutesFor = (paceMin: number) =>
    timerMode === 'untimed' ? null : timerMode === 'custom' ? customMin : paceMin;

  const startPreset = (t: PresetTest) =>
    p.onStart({
      title: t.title,
      kind: t.kind,
      sections: t.sections,
      withBonus: t.withBonus,
      minutes: minutesFor(t.minutes),
      allowPause,
      source,
    });

  const shortOf = (sections: SectionSpec[]) => sections.some((s) => (avail[s.subject] ?? 0) < s.count);

  if (pattern.status === 'coming-soon') {
    return (
      <div className="space-y-5">
        <header>
          <h1 className="text-2xl font-bold tracking-tight">{pattern.name} Mock Tests</h1>
          <p className="text-sm text-slate-500">{pattern.fullName}</p>
        </header>
        <section className={card}>
          <h2 className="mb-2 font-semibold">Exam pattern</h2>
          <ul className="space-y-0.5 text-sm text-slate-600 dark:text-slate-400">
            {pattern.notes.map((n) => (
              <li key={n}>• {n}</li>
            ))}
          </ul>
          <p className="mt-4 rounded-md bg-amber-50 p-3 text-sm text-amber-900 dark:bg-amber-950/40 dark:text-amber-200">
            The {pattern.name} question bank is being prepared. Mock tests will appear here once it is ready.
          </p>
        </section>
      </div>
    );
  }

  return (
    <div className="space-y-5">
      <header>
        <h1 className="text-2xl font-bold tracking-tight">{pattern.name} Mock Tests</h1>
        <p className="text-sm text-slate-500">{pattern.fullName}</p>
        <ul className="mt-2 space-y-0.5 text-sm text-slate-600 dark:text-slate-400">
          {pattern.notes.map((n) => (
            <li key={n}>• {n}</li>
          ))}
        </ul>
      </header>

      {p.hasSavedExam && (
        <div className="flex flex-wrap items-center gap-3 rounded-xl border border-indigo-300 bg-indigo-50 p-4 dark:border-indigo-800 dark:bg-indigo-950/40">
          <p className="text-sm font-medium">You have an unfinished test.</p>
          <div className="ml-auto flex gap-2">
            <button type="button" onClick={p.onResume} className={`${btn} bg-indigo-600 text-white hover:bg-indigo-700`}>
              Resume
            </button>
            <button
              type="button"
              onClick={p.onDiscardSaved}
              className={`${btn} border border-slate-300 hover:bg-white dark:border-slate-700 dark:hover:bg-slate-800`}
            >
              Discard
            </button>
          </div>
        </div>
      )}

      <section className={card}>
        <h2 className="mb-3 font-semibold">Test settings</h2>
        <div className="grid gap-4 sm:grid-cols-3">
          <fieldset>
            <legend className="mb-1 text-xs font-semibold uppercase text-slate-500">Timer</legend>
            {(
              [
                ['exam', 'Exam pace (real timing)'],
                ['custom', 'Custom minutes'],
                ['untimed', 'No time limit (stopwatch)'],
              ] as const
            ).map(([v, l]) => (
              <label key={v} className="flex items-center gap-2 text-sm">
                <input type="radio" name="timer" checked={timerMode === v} onChange={() => setTimerMode(v)} />
                {l}
              </label>
            ))}
            {timerMode === 'custom' && (
              <input
                type="number"
                min={1}
                max={600}
                value={customMin}
                onChange={(e) => setCustomMin(Math.max(1, Number(e.target.value) || 1))}
                className="mt-1 w-24 rounded border border-slate-300 bg-transparent px-2 py-1 text-sm dark:border-slate-700"
              />
            )}
          </fieldset>
          <fieldset>
            <legend className="mb-1 text-xs font-semibold uppercase text-slate-500">Pause</legend>
            <label className="flex items-center gap-2 text-sm">
              <input type="checkbox" checked={allowPause} onChange={(e) => setAllowPause(e.target.checked)} />
              Allow pausing the timer
            </label>
            <p className="mt-1 text-xs text-slate-500">The real exam has no pause. Turn this off for exam-day practice.</p>
          </fieldset>
          <fieldset>
            <legend className="mb-1 text-xs font-semibold uppercase text-slate-500">Questions from</legend>
            {sourceOptions.map(([v, l]) => (
              <label key={v} className="flex items-center gap-2 text-sm">
                <input type="radio" name="source" checked={source === v} onChange={() => setSource(v)} />
                {l} <span className="text-xs text-slate-400">({total(v)})</span>
              </label>
            ))}
          </fieldset>
        </div>
      </section>

      <section>
        <h2 className="mb-2 font-semibold">Tests</h2>
        <div className="grid gap-3 sm:grid-cols-2">
          {presets.map((t) => {
            const total = t.sections.reduce((n, s) => n + s.count, 0);
            const mins = minutesFor(t.minutes);
            const short = shortOf(t.sections);
            return (
              <div key={t.id} className={`${card} flex flex-col ${t.kind === 'full' ? 'sm:col-span-2 border-indigo-300 dark:border-indigo-800' : ''}`}>
                <div className="flex items-baseline gap-2">
                  <h3 className="font-semibold">{t.title}</h3>
                  <span className="ml-auto text-xs text-slate-500">
                    {total} Q · {mins === null ? 'untimed' : `${mins} min`} · max {total * pattern.marking.correct}
                  </span>
                </div>
                <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">{t.description}</p>
                {t.withBonus && <p className="mt-1 text-xs text-amber-700 dark:text-amber-400">Includes the 12-question bonus round.</p>}
                {short && (
                  <p className="mt-1 text-xs text-rose-600">
                    Bank is short for this test with the current source filter; it will run with fewer questions.
                  </p>
                )}
                <button
                  type="button"
                  onClick={() => startPreset(t)}
                  className={`${btn} mt-3 self-start ${t.kind === 'full' ? 'bg-indigo-600 text-white hover:bg-indigo-700' : 'border border-indigo-500 text-indigo-700 hover:bg-indigo-50 dark:text-indigo-300 dark:hover:bg-indigo-950'}`}
                >
                  Start
                </button>
              </div>
            );
          })}
        </div>
      </section>

      <section className={card}>
        <h2 className="mb-1 font-semibold">Custom test</h2>
        <p className="mb-3 text-sm text-slate-600 dark:text-slate-400">
          Pick how many questions from each subject. Exam-pace timing scales to the size ({paceMinutes(pattern, 1)} min ≈ per question).
        </p>
        <div className="grid gap-3 sm:grid-cols-5">
          {pattern.sections.map((s) => (
            <label key={s.subject} className="text-sm">
              <span className="block text-xs font-medium text-slate-600 dark:text-slate-400">
                {SUBJECT_NAMES[s.subject]} <span className="text-slate-400">({avail[s.subject] ?? 0})</span>
              </span>
              <input
                type="number"
                min={0}
                max={avail[s.subject] ?? 0}
                value={custom[s.subject] ?? 0}
                onChange={(e) =>
                  setCustom((c) => ({
                    ...c,
                    [s.subject]: Math.max(0, Math.min(avail[s.subject] ?? 0, Number(e.target.value) || 0)),
                  }))
                }
                className="mt-1 w-full rounded border border-slate-300 bg-transparent px-2 py-1 dark:border-slate-700"
              />
            </label>
          ))}
        </div>
        <button
          type="button"
          disabled={customTotal === 0}
          onClick={() =>
            p.onStart({
              title: 'Custom test',
              kind: 'custom',
              sections: customSections,
              withBonus: false,
              minutes: minutesFor(paceMinutes(pattern, customTotal)),
              allowPause,
              source,
            })
          }
          className={`${btn} mt-3 bg-slate-800 text-white hover:bg-slate-900 dark:bg-slate-200 dark:text-slate-900`}
        >
          Start custom test ({customTotal} Q
          {customTotal > 0 && timerMode !== 'untimed' ? `, ${minutesFor(paceMinutes(pattern, customTotal))} min` : ''})
        </button>
      </section>

      <section className={card}>
        <div className="mb-2 flex flex-wrap items-center gap-2">
          <h2 className="font-semibold">Your attempts</h2>
          <div className="ml-auto flex gap-2">
            {p.hasLastResult && (
              <button type="button" onClick={p.onOpenLast} className="text-xs font-semibold text-indigo-600 hover:underline">
                Review last test
              </button>
            )}
            {p.history.length > 0 && (
              <button
                type="button"
                onClick={() => confirm('Clear all attempt history?') && p.onClearHistory()}
                className="text-xs text-slate-500 hover:underline"
              >
                Clear history
              </button>
            )}
          </div>
        </div>
        {p.history.length === 0 ? (
          <p className="text-sm text-slate-500">No attempts yet.</p>
        ) : (
          <div className="scroll-x">
            <table className="w-full min-w-[520px] text-sm">
              <thead>
                <tr className="text-left text-xs uppercase text-slate-500">
                  <th className="py-1">Date</th>
                  <th>Test</th>
                  <th className="text-right">Score</th>
                  <th className="text-right">✓</th>
                  <th className="text-right">✗</th>
                  <th className="text-right">Skip</th>
                  <th className="text-right">Time</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {[...p.history].reverse().slice(0, 20).map((h) => (
                  <tr key={h.id} className="border-t border-slate-100 dark:border-slate-800">
                    <td className="py-1.5">{new Date(h.completedAt).toLocaleDateString()}</td>
                    <td>{h.title}</td>
                    <td className="text-right font-semibold">
                      {h.net}/{h.maxMarks}
                    </td>
                    <td className="text-right text-emerald-600">{h.correct}</td>
                    <td className="text-right text-rose-600">{h.incorrect}</td>
                    <td className="text-right text-slate-500">{h.skipped}</td>
                    <td className="text-right">{Math.round(h.durationMs / 60000)}m</td>
                    <td className="whitespace-nowrap pl-3 text-right">
                      {h.responses ? (
                        <>
                          <button type="button" onClick={() => p.onOpenAttempt(h, 'review')} className="text-xs font-semibold text-indigo-600 hover:underline">
                            Review
                          </button>
                          <button type="button" onClick={() => p.onOpenAttempt(h, 'pdf')} className="ml-2 text-xs font-semibold text-indigo-600 hover:underline">
                            PDF
                          </button>
                        </>
                      ) : (
                        <span className="text-xs text-slate-400">—</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
        <p className="mt-3 text-xs text-slate-500">
          {p.seenTotal} distinct questions seen so far — new tests prefer questions you haven't seen.{' '}
          {p.seenTotal > 0 && (
            <button type="button" onClick={p.onResetSeen} className="underline">
              Reset
            </button>
          )}
        </p>
      </section>
    </div>
  );
}
