import { SUBJECTS, type Question, type SectionSpec, type SeenMap, type SourceFilter, type SubjectId } from '../types';

export interface Bank {
  questions: Question[];
}

async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to load ${url}: ${res.status} ${res.statusText}`);
  return (await res.json()) as T;
}

/**
 * Loads every question file listed in data/manifest.json (written by
 * `npm run validate`). Uses BASE_URL so it works under any deploy path.
 */
export async function loadBank(): Promise<Bank> {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  const manifest = await fetchJson<{ files: string[] }>(`${base}/data/manifest.json`);
  const perFile = await Promise.all(
    manifest.files.map(async (f) => {
      try {
        return await fetchJson<Question[]>(`${base}/data/questions/${f}`);
      } catch {
        return [] as Question[];
      }
    }),
  );
  // Drop anything malformed rather than crash mid-exam.
  const questions = perFile
    .flat()
    .filter(
      (q) =>
        q &&
        SUBJECTS.includes(q.subject) &&
        Array.isArray(q.options) &&
        q.options.length === 4 &&
        q.options.some((o) => o.key === q.answer),
    );
  return { questions };
}

/** Questions an exam may draw: untagged (generic) ones plus those tagged for it. */
export function allowedFor(q: Question, examId: string): boolean {
  return !q.exams || q.exams.includes(examId);
}

export function countBySubject(questions: Question[], examId: string, source: SourceFilter = 'all') {
  const out = Object.fromEntries(SUBJECTS.map((s) => [s, 0])) as Record<SubjectId, number>;
  for (const q of questions) if (allowedFor(q, examId) && matchesSource(q, source)) out[q.subject] += 1;
  return out;
}

const isPyq = (q: Question) => Boolean(q.pyq) || q.id.startsWith('pyq-');

export function matchesSource(q: Question, source: SourceFilter): boolean {
  if (source === 'all') return true;
  if (source === 'pyq') return isPyq(q);
  if (source === 'harvested') return q.source.kind === 'harvested' && !isPyq(q);
  return q.source.kind === 'authored';
}

/** Fisher-Yates, on a copy. */
export function shuffle<T>(input: readonly T[]): T[] {
  const arr = [...input];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j]!, arr[i]!];
  }
  return arr;
}

/** Least-seen first, then least-recently seen; shuffled first so ties vary. */
function preferUnseen(pool: readonly Question[], seen: SeenMap): Question[] {
  return shuffle(pool).sort((a, b) => {
    const ca = seen[a.id]?.count ?? 0;
    const cb = seen[b.id]?.count ?? 0;
    if (ca !== cb) return ca - cb;
    return (seen[a.id]?.lastSeen ?? 0) - (seen[b.id]?.lastSeen ?? 0);
  });
}

/** Target difficulty mix for a BITSAT-like paper. */
const MIX = { easy: 0.3, medium: 0.5, hard: 0.2 } as const;

/**
 * Draws `count` questions of one subject, aiming for the difficulty mix and
 * preferring unseen questions, topping up from whatever remains if a tier is thin.
 */
function drawSubject(
  pool: Question[],
  count: number,
  used: Set<string>,
  seen: SeenMap,
): Question[] {
  const ordered = preferUnseen(pool.filter((q) => !used.has(q.id)), seen);
  const picked: Question[] = [];
  const take = (q: Question) => {
    picked.push(q);
    used.add(q.id);
  };
  for (const tier of ['easy', 'medium', 'hard'] as const) {
    const want = Math.round(MIX[tier] * count);
    for (const q of ordered) {
      if (picked.filter((p) => p.difficulty === tier).length >= want) break;
      if (q.difficulty === tier && !used.has(q.id)) take(q);
    }
  }
  for (const q of ordered) {
    if (picked.length >= count) break;
    if (!used.has(q.id)) take(q);
  }
  return picked.slice(0, count);
}

export interface DrawResult {
  /** Questions in section order, each section shuffled internally. */
  main: Question[];
  bonus: Question[];
  shortfalls: string[];
}

export function drawPaper(
  bank: Bank,
  examId: string,
  sections: SectionSpec[],
  bonusSections: SectionSpec[],
  source: SourceFilter,
  seen: SeenMap,
): DrawResult {
  const used = new Set<string>();
  const shortfalls: string[] = [];
  const pool = (s: SubjectId) =>
    bank.questions.filter(
      (q) =>
        q.subject === s && matchesSource(q, source) && allowedFor(q, examId),
    );

  const main: Question[] = [];
  for (const s of sections) {
    const got = drawSubject(pool(s.subject), s.count, used, seen);
    if (got.length < s.count) shortfalls.push(`${s.subject}: ${got.length}/${s.count}`);
    // Easy-to-hard is not how BITSAT orders a section; shuffle.
    main.push(...shuffle(got));
  }
  const bonus: Question[] = [];
  for (const s of bonusSections) {
    bonus.push(...drawSubject(pool(s.subject), s.count, used, seen));
  }
  return { main, bonus, shortfalls };
}
