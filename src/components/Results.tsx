import { SUBJECT_NAMES, type ExamResult, type ExamState, type Tally } from '../types';

interface Props {
  exam: ExamState;
  result: ExamResult;
  onReview: (filter?: 'incorrect' | 'skipped' | 'correct') => void;
  onPdf: () => void;
  onRestart: () => void;
}

export function fmtTime(ms: number): string {
  const s = Math.round(ms / 1000);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  return h > 0 ? `${h}h ${m}m` : `${m}m ${String(sec).padStart(2, '0')}s`;
}

export default function Results({ exam, result, onReview, onPdf, onRestart }: Props) {
  const o = result.overall;
  const m = exam.marking;
  const weakTopics = result.topicStats.filter((t) => t.correct < t.total).slice(0, 8);

  return (
    <div className="space-y-5">
      <div className="rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
        <p className="text-sm text-slate-500">{exam.title} · submitted</p>
        <div className="mt-1 flex flex-wrap items-end gap-x-6 gap-y-2">
          <p className="text-4xl font-bold">
            {o.net}
            <span className="text-xl font-medium text-slate-400"> / {o.maxMarks}</span>
          </p>
          {result.bonus && (
            <p className="text-sm text-amber-700 dark:text-amber-400">incl. bonus round: {result.bonus.net >= 0 ? '+' : ''}{result.bonus.net}</p>
          )}
          <p className="text-sm text-slate-500">
            Time used: {fmtTime(result.durationMs)}
            {exam.durationMs !== null && ` of ${fmtTime(exam.durationMs)}`}
          </p>
        </div>
        <p className="mt-1 text-xs text-slate-500">
          Marking: +{m.correct} correct, {m.wrong} wrong, {m.skipped} unattempted
        </p>

        <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-6">
          <Stat label="Questions" value={o.total} />
          <Stat label="Answered" value={o.attempted} />
          <Stat label="Correct" value={o.correct} tone="good" sub={`+${o.positive} marks`} onClick={() => onReview('correct')} />
          <Stat label="Incorrect" value={o.incorrect} tone="bad" sub={`−${o.negative} marks`} onClick={() => onReview('incorrect')} />
          <Stat label="Skipped" value={o.skipped} tone="muted" sub="0 marks" onClick={() => onReview('skipped')} />
          <Stat label="Accuracy" value={`${o.accuracy}%`} sub="of answered" />
        </div>

        <div className="mt-5 flex flex-wrap gap-2">
          <button type="button" onClick={() => onReview()} className="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700">
            Review all answers
          </button>
          <button type="button" onClick={() => onReview('incorrect')} className="rounded-md border border-rose-400 px-4 py-2 text-sm font-semibold text-rose-700 hover:bg-rose-50 dark:text-rose-300 dark:hover:bg-rose-950">
            Review mistakes
          </button>
          <button type="button" onClick={onPdf} className="rounded-md border border-indigo-500 px-4 py-2 text-sm font-semibold text-indigo-700 hover:bg-indigo-50 dark:text-indigo-300 dark:hover:bg-indigo-950">
            ⬇ Download PDF report
          </button>
          <button type="button" onClick={onRestart} className="rounded-md border border-slate-300 px-4 py-2 text-sm font-semibold hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800">
            Back to tests
          </button>
        </div>
      </div>

      <div className="rounded-xl border border-slate-200 bg-white p-5 dark:border-slate-800 dark:bg-slate-900">
        <h2 className="mb-3 font-semibold">Section-wise breakdown</h2>
        <div className="scroll-x">
          <table className="w-full min-w-[680px] text-sm">
            <thead>
              <tr className="text-left text-xs uppercase text-slate-500">
                <th className="py-1">Section</th>
                <th className="text-right">Qs</th>
                <th className="text-right">Answered</th>
                <th className="text-right">Correct</th>
                <th className="text-right">Incorrect</th>
                <th className="text-right">Skipped</th>
                <th className="text-right">+ Marks</th>
                <th className="text-right">− Negative</th>
                <th className="text-right">Net</th>
                <th className="text-right">Accuracy</th>
                <th className="text-right">Time</th>
              </tr>
            </thead>
            <tbody>
              {result.sections.map((s) => (
                <Row key={s.subject} label={SUBJECT_NAMES[s.subject]} t={s} />
              ))}
              <Row label="Total" t={o} bold />
            </tbody>
          </table>
        </div>
      </div>

      {weakTopics.length > 0 && (
        <div className="rounded-xl border border-slate-200 bg-white p-5 dark:border-slate-800 dark:bg-slate-900">
          <h2 className="mb-2 font-semibold">Topics to revise</h2>
          <ul className="grid gap-1 text-sm sm:grid-cols-2">
            {weakTopics.map((t) => (
              <li key={`${t.subject}-${t.topic}`} className="flex gap-2">
                <span className="text-slate-500">{SUBJECT_NAMES[t.subject]}:</span>
                <span>{t.topic}</span>
                <span className="ml-auto text-rose-600">
                  {t.correct}/{t.total}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

function Row({ label, t, bold }: { label: string; t: Tally; bold?: boolean }) {
  return (
    <tr className={`border-t border-slate-100 dark:border-slate-800 ${bold ? 'font-semibold' : ''}`}>
      <td className="py-1.5">{label}</td>
      <td className="text-right">{t.total}</td>
      <td className="text-right">{t.attempted}</td>
      <td className="text-right text-emerald-600">{t.correct}</td>
      <td className="text-right text-rose-600">{t.incorrect}</td>
      <td className="text-right text-slate-500">{t.skipped}</td>
      <td className="text-right text-emerald-600">+{t.positive}</td>
      <td className="text-right text-rose-600">−{t.negative}</td>
      <td className="text-right">{t.net}</td>
      <td className="text-right">{t.accuracy}%</td>
      <td className="text-right">{fmtTime(t.timeMs)}</td>
    </tr>
  );
}

function Stat({
  label,
  value,
  sub,
  tone,
  onClick,
}: {
  label: string;
  value: number | string;
  sub?: string;
  tone?: 'good' | 'bad' | 'muted';
  onClick?: () => void;
}) {
  const color =
    tone === 'good' ? 'text-emerald-600' : tone === 'bad' ? 'text-rose-600' : tone === 'muted' ? 'text-slate-500' : '';
  const Tag = onClick ? 'button' : 'div';
  return (
    <Tag
      {...(onClick ? { type: 'button' as const, onClick } : {})}
      className={`rounded-lg border border-slate-200 p-3 text-left dark:border-slate-800 ${onClick ? 'hover:bg-slate-50 dark:hover:bg-slate-800' : ''}`}
    >
      <p className="text-xs text-slate-500">{label}</p>
      <p className={`text-2xl font-bold ${color}`}>{value}</p>
      {sub && <p className={`text-xs ${color || 'text-slate-500'}`}>{sub}</p>}
    </Tag>
  );
}
