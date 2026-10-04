import { SUBJECT_NAMES, type ExamItem, type MarkingScheme, type OptionKey } from '../types';
import Figure, { optionsAreFigures } from './Figure';
import PyqBadge from './PyqBadge';
import Rich from './Rich';

interface Props {
  item: ExamItem;
  number: number;
  total: number;
  marking: MarkingScheme;
  onSelect: (key: OptionKey) => void;
  onClear: () => void;
  onToggleFlag: () => void;
}

export default function QuestionCard({ item, number, total, marking, onSelect, onClear, onToggleFlag }: Props) {
  const { question: q } = item;
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      <div className="mb-3 flex flex-wrap items-center gap-2 text-xs">
        <span className="font-semibold text-slate-700 dark:text-slate-200">
          Question {number} of {total}
        </span>
        <span className="rounded bg-indigo-100 px-1.5 py-0.5 font-medium text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300">
          {SUBJECT_NAMES[q.subject]}
        </span>
        <PyqBadge question={q} />
        {item.bonus && (
          <span className="rounded bg-amber-100 px-1.5 py-0.5 font-bold text-amber-800 dark:bg-amber-950 dark:text-amber-300">
            BONUS
          </span>
        )}
        <span className="ml-auto text-slate-500 dark:text-slate-400">
          +{marking.correct} / {marking.wrong === 0 ? 'no negative' : marking.wrong}
        </span>
      </div>

      <Rich text={q.stem} className="mb-5 text-[15px] leading-relaxed" />
      {q.stemImage && (
        <div className="-mt-2 mb-5">
          <Figure src={q.stemImage} alt={`Figure for question ${number}`} />
        </div>
      )}

      <div className={optionsAreFigures(q.options) ? 'grid grid-cols-2 gap-2 sm:grid-cols-4' : 'space-y-2'} role="radiogroup">
        {q.options.map((o) => {
          const active = item.selected === o.key;
          return (
            <button
              key={o.key}
              type="button"
              role="radio"
              aria-checked={active}
              onClick={() => onSelect(o.key)}
              className={`flex w-full items-start gap-3 rounded-lg border px-3 py-2.5 text-left text-sm transition ${
                active
                  ? 'border-indigo-500 bg-indigo-50 ring-1 ring-indigo-500 dark:bg-indigo-950/50'
                  : 'border-slate-200 hover:bg-slate-50 dark:border-slate-700 dark:hover:bg-slate-800'
              }`}
            >
              <span
                className={`mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-bold ${
                  active ? 'border-indigo-600 bg-indigo-600 text-white' : 'border-slate-400'
                }`}
              >
                {o.key}
              </span>
              <span className="min-w-0 flex-1 overflow-x-auto">
                {o.text && <Rich text={o.text} />}
                {o.image && <Figure src={o.image} alt={`Option ${o.key}`} size="option" />}
              </span>
            </button>
          );
        })}
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        <button
          type="button"
          onClick={onToggleFlag}
          className={`rounded-md border px-3 py-1.5 text-xs font-semibold transition ${
            item.flagged
              ? 'border-purple-500 bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300'
              : 'border-slate-300 hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800'
          }`}
        >
          {item.flagged ? '★ Marked for review' : '☆ Mark for review'}
        </button>
        <button
          type="button"
          onClick={onClear}
          disabled={item.selected === null}
          className="rounded-md border border-slate-300 px-3 py-1.5 text-xs font-semibold transition hover:bg-slate-100 disabled:opacity-40 dark:border-slate-700 dark:hover:bg-slate-800"
        >
          Clear response
        </button>
        <span className="ml-auto self-center text-xs text-slate-400">Keys: A–D select · ←/→ move · M mark</span>
      </div>
    </div>
  );
}
