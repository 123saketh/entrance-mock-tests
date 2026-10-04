import type { AttemptRecord, ExamState, SeenMap } from '../types';

/** Each exam keeps its own in-progress test, last result, history and seen set. */
const examKey = (examId: string) => `mock.${examId}.exam.v1`;
const historyKey = (examId: string) => `mock.${examId}.history.v1`;
const seenKey = (examId: string) => `mock.${examId}.seen.v1`;
const lastKey = (examId: string) => `mock.${examId}.lastResult.v1`;
const SELECTED_KEY = 'mock.selectedExam';
export const STATE_VERSION = 1;

/** localStorage throws in private windows / blocked storage; never let that break the app. */
function readRaw(key: string): string | null {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
}
function writeRaw(key: string, value: string): void {
  try {
    localStorage.setItem(key, value);
  } catch {
    /* storage unavailable or full */
  }
}
function removeRaw(key: string): void {
  try {
    localStorage.removeItem(key);
  } catch {
    /* no-op */
  }
}
function readJson<T>(key: string, fallback: T): T {
  const raw = readRaw(key);
  if (!raw) return fallback;
  try {
    return JSON.parse(raw) as T;
  } catch {
    return fallback;
  }
}

export function saveExam(state: ExamState): void {
  writeRaw(examKey(state.examId), JSON.stringify(state));
}

export function loadExam(examId: string): ExamState | null {
  const s = readJson<ExamState | null>(examKey(examId), null);
  if (!s || s.version !== STATE_VERSION || !Array.isArray(s.items) || s.items.length === 0) return null;
  return s;
}

export function clearExam(examId: string): void {
  removeRaw(examKey(examId));
}

/** The last submitted sitting, so its review survives a page reload. */
export function saveLastSubmitted(state: ExamState): void {
  writeRaw(lastKey(state.examId), JSON.stringify(state));
}
export function loadLastSubmitted(examId: string): ExamState | null {
  return readJson<ExamState | null>(lastKey(examId), null);
}

export function loadHistory(examId: string): AttemptRecord[] {
  const h = readJson<AttemptRecord[]>(historyKey(examId), []);
  return Array.isArray(h) ? dedupe(h) : [];
}

/** Drops the duplicate records an earlier bug wrote: same result within 2 seconds. */
function dedupe(records: AttemptRecord[]): AttemptRecord[] {
  const out: AttemptRecord[] = [];
  for (const r of records) {
    const prev = out[out.length - 1];
    const same =
      prev &&
      prev.title === r.title &&
      prev.net === r.net &&
      prev.correct === r.correct &&
      prev.incorrect === r.incorrect &&
      prev.skipped === r.skipped &&
      Math.abs(prev.completedAt - r.completedAt) < 2000;
    if (!same) out.push(r);
  }
  return out;
}

export function appendHistory(record: AttemptRecord): void {
  writeRaw(historyKey(record.examId), JSON.stringify([...loadHistory(record.examId), record].slice(-100)));
}

export function clearHistory(examId: string): void {
  removeRaw(historyKey(examId));
}

export function loadSeen(examId: string): SeenMap {
  const s = readJson<SeenMap>(seenKey(examId), {});
  return s && typeof s === 'object' ? s : {};
}

export function recordSeen(examId: string, ids: string[]): void {
  const seen = loadSeen(examId);
  const now = Date.now();
  for (const id of ids) seen[id] = { count: (seen[id]?.count ?? 0) + 1, lastSeen: now };
  writeRaw(seenKey(examId), JSON.stringify(seen));
}

export function clearSeen(examId: string): void {
  removeRaw(seenKey(examId));
}

export function seenCount(examId: string): number {
  return Object.keys(loadSeen(examId)).length;
}

export function loadSelectedExam(): string | null {
  return readRaw(SELECTED_KEY);
}
export function saveSelectedExam(examId: string): void {
  writeRaw(SELECTED_KEY, examId);
}
