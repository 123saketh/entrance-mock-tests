import { useEffect } from 'react';
import { marksFor, outcome } from '../lib/scoring';
import { SUBJECT_NAMES, type ExamResult, type ExamState, type Tally } from '../types';
import Figure, { optionsAreFigures } from './Figure';
import PyqBadge from './PyqBadge';
import { fmtTime } from './Results';
import Rich from './Rich';

interface Props {
  exam: ExamState;
  result: ExamResult;
  examName: string;
  onBack: () => void;
}

/**
 * Print-optimised report of a submitted test: summary, section table and every
 * question with the chosen answer, the correct answer and the explanation.
 * Opens the browser's print dialog, where "Save as PDF" produces the file.
 */
export default function PrintReport({ exam, result, examName, onBack }: Props) {
  const o = result.overall;
  const when = new Date(exam.startedAt);

  useEffect(() => {
    const prevTitle = document.title;
    // Becomes the suggested PDF file name.
    document.title = `${examName} ${exam.title} ${when.toISOString().slice(0, 10)} - ${o.net} of ${o.maxMarks}`;
    // Give KaTeX fonts and figures a moment to load before printing.
    const t = window.setTimeout(() => window.print(), 800);
    return () => {
      window.clearTimeout(t);
      document.title = prevTitle;
    };
    // Print once per mount.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="print-report mx-auto max-w-4xl bg-white px-6 py-6 text-[13px] text-slate-900">
      <div className="no-print mb-4 flex flex-wrap items-center gap-2 rounded-md border border-indigo-200 bg-indigo-50 p-3 text-sm">
        <span>
          In the print dialog choose <b>Save as PDF</b> as the destination. Tip: turn on "Background graphics" to keep the colours.
        </span>
        <div className="ml-auto flex gap-2">
          <button type="button" onClick={() => window.print()} className="rounded-md bg-indigo-600 px-3 py-1.5 font-semibold text-white">
            Print / Save PDF
          </button>
          <button type="button" onClick={onBack} className="rounded-md border border-slate-300 bg-white px-3 py-1.5">
            Back
          </button>
        </div>
      </div>

      <header className="mb-4 border-b border-slate-300 pb-3">
        <h1 className="text-xl font-bold">
          {examName} · {exam.title}
        </h1>
        <p className="text-slate-600">
          {when.toLocaleString()} · Time used {fmtTime(result.durationMs)}
          {exam.durationMs !== null && ` of ${fmtTime(exam.durationMs)}`} · Marking +{exam.marking.correct} / {exam.marking.wrong} / {exam.marking.skipped}
        </p>
      </header>

      <section className="mb-4 grid grid-cols-6 gap-2 text-center">
        <Box label="Score" value={`${o.net} / ${o.maxMarks}`} />
        <Box label="Answered" value={o.attempted} />
        <Box label="Correct" value={`${o.correct} (+${o.positive})`} cls="text-emerald-700" />
        <Box label="Incorrect" value={`${o.incorrect} (−${o.negative})`} cls="text-rose-700" />
        <Box label="Skipped" value={o.skipped} />
        <Box label="Accuracy" value={`${o.accuracy}%`} />
      </section>
      {result.bonus && (
        <p className="mb-3 text-amber-700">Bonus round taken: {result.bonus.correct} correct, {result.bonus.incorrect} incorrect, net {result.bonus.net}.</p>
      )}

      <table className="mb-6 w-full border-collapse text-[12px]">
        <thead>
          <tr className="border-b border-slate-400 text-left">
            {['Section', 'Qs', 'Answered', 'Correct', 'Incorrect', 'Skipped', '+Marks', '−Negative', 'Net', 'Accuracy', 'Time'].map((h) => (
              <th key={h} className="py-1 pr-2">
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {result.sections.map((s) => (
            <Row key={s.subject} label={SUBJECT_NAMES[s.subject]} t={s} />
          ))}
          <Row label="Total" t={o} bold />
        </tbody>
      </table>

      <h2 className="mb-2 text-base font-bold">All questions</h2>
      {exam.items.map((item, i) => {
        const q = item.question;
        const oc = outcome(item);
        const marks = marksFor(item, exam.marking);
        const badge =
          oc === 'correct' ? 'bg-emerald-100 text-emerald-800' : oc === 'incorrect' ? 'bg-rose-100 text-rose-800' : 'bg-slate-200 text-slate-700';
        return (
          <article key={q.id} className="print-q mb-3 rounded border border-slate-300 p-3">
            <div className="mb-1 flex flex-wrap items-center gap-2 text-[11px]">
              <b>Q{i + 1}</b>
              <span className={`rounded px-1.5 py-0.5 font-bold ${badge}`}>
                {oc === 'correct' ? 'Correct' : oc === 'incorrect' ? 'Incorrect' : 'Skipped'} ({marks > 0 ? `+${marks}` : marks})
              </span>
              <PyqBadge question={q} showPaper />
              {item.bonus && <span className="font-bold text-amber-700">BONUS</span>}
              {item.flagged && <span className="text-purple-700">★ marked</span>}
              <span className="text-slate-500">
                {SUBJECT_NAMES[q.subject]} · {q.topic} · {q.difficulty} · {fmtTime(item.timeMs)}
              </span>
            </div>
            <Rich text={q.stem} className="mb-2" />
            {q.stemImage && (
              <div className="mb-2">
                <Figure src={q.stemImage} alt={`Figure for question ${i + 1}`} />
              </div>
            )}
            <ul className={`mb-2 grid gap-1 ${optionsAreFigures(q.options) ? 'grid-cols-4' : ''}`}>
              {q.options.map((opt) => {
                const isAns = opt.key === q.answer;
                const isSel = opt.key === item.selected;
                return (
                  <li
                    key={opt.key}
                    className={`flex items-start gap-2 rounded border px-2 py-1 ${isAns ? 'border-emerald-600 bg-emerald-50' : isSel ? 'border-rose-600 bg-rose-50' : 'border-slate-200'}`}
                  >
                    <b>{opt.key}.</b>
                    <span className="min-w-0 flex-1">
                      {opt.text && <Rich as="span" text={opt.text} />}
                      {opt.image && <Figure src={opt.image} alt={`Option ${opt.key}`} size="option" />}
                    </span>
                    <span className="shrink-0 text-[11px] font-bold">
                      {isAns && isSel && <span className="text-emerald-700">✓ Your answer · Correct</span>}
                      {isAns && !isSel && <span className="text-emerald-700">✓ Correct answer</span>}
                      {!isAns && isSel && <span className="text-rose-700">✗ Your answer</span>}
                    </span>
                  </li>
                );
              })}
            </ul>
            <p className="mb-1 text-[11px]">
              Your answer: <b>{item.selected ?? 'Not answered'}</b> · Correct answer: <b>{q.answer}</b>
            </p>
            <div className="rounded bg-slate-50 p-2">
              <span className="text-[11px] font-bold uppercase text-slate-500">Explanation </span>
              <Rich text={q.explanation} />
              {q.explanationImage && <Figure src={q.explanationImage} alt="Explanation figure" size="explanation" />}
            </div>
          </article>
        );
      })}
    </div>
  );
}

function Box({ label, value, cls = '' }: { label: string; value: string | number; cls?: string }) {
  return (
    <div className="rounded border border-slate-300 p-2">
      <div className="text-[11px] text-slate-500">{label}</div>
      <div className={`text-base font-bold ${cls}`}>{value}</div>
    </div>
  );
}

function Row({ label, t, bold }: { label: string; t: Tally; bold?: boolean }) {
  return (
    <tr className={`border-b border-slate-200 ${bold ? 'font-bold' : ''}`}>
      <td className="py-1 pr-2">{label}</td>
      <td>{t.total}</td>
      <td>{t.attempted}</td>
      <td>{t.correct}</td>
      <td>{t.incorrect}</td>
      <td>{t.skipped}</td>
      <td>+{t.positive}</td>
      <td>−{t.negative}</td>
      <td>{t.net}</td>
      <td>{t.accuracy}%</td>
      <td>{fmtTime(t.timeMs)}</td>
    </tr>
  );
}
