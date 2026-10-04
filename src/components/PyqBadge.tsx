import type { Question } from '../types';

/** Small "PYQ" flag on previous-year questions, naming the paper on hover and in print. */
export default function PyqBadge({ question, showPaper = false }: { question: Question; showPaper?: boolean }) {
  if (!question.pyq) return null;
  return (
    <span
      title={`Previous year question: ${question.pyq}`}
      className="rounded bg-sky-100 px-1.5 py-0.5 text-[11px] font-bold text-sky-800 dark:bg-sky-950 dark:text-sky-300"
    >
      PYQ{showPaper && <span className="font-medium"> · {question.pyq}</span>}
    </span>
  );
}
