import { subjectsInOrder } from '../lib/scoring';
import { SUBJECT_SHORT, type ExamItem, type SubjectId } from '../types';

interface Props {
  items: ExamItem[];
  currentIndex: number;
  /** Items before this index are locked (bonus taken). */
  lockedBefore: number | null;
  onJump: (index: number) => void;
}

function cellClass(item: ExamItem, current: boolean): string {
  let c = 'border-slate-300 bg-white text-slate-600 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300';
  if (item.visited && item.selected === null) c = 'border-rose-400 bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300';
  if (item.selected !== null) c = 'border-emerald-500 bg-emerald-500 text-white';
  if (item.flagged) c = item.selected !== null ? 'border-purple-600 bg-purple-600 text-white ring-2 ring-emerald-400' : 'border-purple-500 bg-purple-500 text-white';
  return `${c} ${current ? 'outline outline-2 outline-offset-2 outline-indigo-500' : ''}`;
}

export default function Navigator({ items, currentIndex, lockedBefore, onJump }: Props) {
  const groups: { label: string; subject: SubjectId | 'bonus'; indices: number[] }[] = [];
  for (const s of subjectsInOrder(items.filter((i) => !i.bonus))) {
    const indices = items.flatMap((it, i) => (!it.bonus && it.question.subject === s ? [i] : []));
    if (indices.length) groups.push({ label: SUBJECT_SHORT[s], subject: s, indices });
  }
  const bonus = items.flatMap((it, i) => (it.bonus ? [i] : []));
  if (bonus.length) groups.push({ label: 'BONUS', subject: 'bonus', indices: bonus });

  const answered = items.filter((i) => i.selected !== null).length;
  const flagged = items.filter((i) => i.flagged).length;
  const notAnswered = items.filter((i) => i.visited && i.selected === null).length;
  const notVisited = items.filter((i) => !i.visited).length;

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
      <div className="mb-3 grid grid-cols-2 gap-1.5 text-[11px]">
        <Legend cls="bg-emerald-500" label={`Answered (${answered})`} />
        <Legend cls="bg-rose-200 dark:bg-rose-900" label={`Not answered (${notAnswered})`} />
        <Legend cls="bg-white border border-slate-300 dark:bg-slate-900" label={`Not visited (${notVisited})`} />
        <Legend cls="bg-purple-500" label={`Marked (${flagged})`} />
      </div>
      <div className="max-h-[60vh] space-y-3 overflow-y-auto pr-1">
        {groups.map((g) => (
          <div key={g.subject}>
            <p className="mb-1 text-[11px] font-bold tracking-wide text-slate-500">{g.label}</p>
            <div className="grid grid-cols-6 gap-1.5">
              {g.indices.map((i) => {
                const locked = lockedBefore !== null && i < lockedBefore;
                return (
                  <button
                    key={i}
                    type="button"
                    disabled={locked}
                    onClick={() => onJump(i)}
                    className={`h-8 rounded border text-xs font-semibold transition disabled:cursor-not-allowed disabled:opacity-40 ${cellClass(items[i]!, i === currentIndex)}`}
                  >
                    {i + 1}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Legend({ cls, label }: { cls: string; label: string }) {
  return (
    <span className="flex items-center gap-1.5 text-slate-600 dark:text-slate-400">
      <span className={`inline-block h-3 w-3 rounded-sm ${cls}`} />
      {label}
    </span>
  );
}
