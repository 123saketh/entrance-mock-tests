import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import Navigator from './components/Navigator';
import QuestionCard from './components/QuestionCard';
import PrintReport from './components/PrintReport';
import Results, { fmtTime } from './components/Results';
import ReviewList, { type ReviewFilter } from './components/ReviewList';
import StartScreen, { type StartOptions } from './components/StartScreen';
import { EXAMS, findExam } from './exams';
import { countBySubject, drawPaper, loadBank, type Bank } from './lib/bank';
import {
  appendHistory,
  clearExam,
  clearHistory,
  clearSeen,
  loadExam,
  loadHistory,
  loadLastSubmitted,
  loadSeen,
  loadSelectedExam,
  recordSeen,
  saveExam,
  saveLastSubmitted,
  saveSelectedExam,
  seenCount,
  STATE_VERSION,
} from './lib/persist';
import { scoreExam } from './lib/scoring';
import { SUBJECT_NAMES, type AttemptRecord, type ExamItem, type ExamState, type OptionKey } from './types';

type View = 'loading' | 'error' | 'start' | 'exam' | 'results' | 'review' | 'print';

const TICK_MS = 1000;

export default function App() {
  const [examId, setExamId] = useState(() => findExam(loadSelectedExam()).id);
  const pattern = findExam(examId);
  const [bank, setBank] = useState<Bank | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [view, setView] = useState<View>('loading');
  const [exam, setExam] = useState<ExamState | null>(null);
  const [history, setHistory] = useState<AttemptRecord[]>([]);
  const [savedExists, setSavedExists] = useState(false);
  const [lastExists, setLastExists] = useState(false);
  const [seenTotal, setSeenTotal] = useState(0);
  const [warning, setWarning] = useState<string | null>(null);
  const [reviewFilter, setReviewFilter] = useState<ReviewFilter>('all');
  const [confirmSubmit, setConfirmSubmit] = useState(false);
  const [bonusPrompt, setBonusPrompt] = useState(false);

  useEffect(() => {
    loadBank()
      .then((b) => {
        setBank(b);
        setView('start');
      })
      .catch((e: unknown) => {
        setLoadError(e instanceof Error ? e.message : String(e));
        setView('error');
      });
  }, []);

  // Per-exam state is reloaded whenever the selected exam changes.
  useEffect(() => {
    setHistory(loadHistory(examId));
    setSavedExists(loadExam(examId) !== null);
    setLastExists(loadLastSubmitted(examId) !== null);
    setSeenTotal(seenCount(examId));
    setWarning(null);
  }, [examId]);

  const switchExam = useCallback((id: string) => {
    saveSelectedExam(id);
    setExamId(id);
    setExam(null);
    setView((v) => (v === 'loading' || v === 'error' ? v : 'start'));
  }, []);

  const counts = useMemo(
    () =>
      bank
        ? {
            all: countBySubject(bank.questions, examId, 'all'),
            authored: countBySubject(bank.questions, examId, 'authored'),
            harvested: countBySubject(bank.questions, examId, 'harvested'),
            pyq: countBySubject(bank.questions, examId, 'pyq'),
          }
        : null,
    [bank, examId],
  );

  const persist = useCallback((next: ExamState) => {
    setExam(next);
    saveExam(next);
  }, []);

  const updateItem = useCallback(
    (fn: (it: ExamItem) => ExamItem) => {
      if (!exam || exam.paused) return;
      const items = exam.items.map((it, i) => (i === exam.currentIndex ? fn(it) : it));
      persist({ ...exam, items });
    },
    [exam, persist],
  );

  // --- start / resume ----------------------------------------------------------

  const handleStart = useCallback(
    (opts: StartOptions) => {
      if (!bank) return;
      const { main, bonus, shortfalls } = drawPaper(
        bank,
        pattern.id,
        opts.sections,
        opts.withBonus && pattern.bonus ? pattern.bonus.sections : [],
        opts.source,
        loadSeen(pattern.id),
      );
      if (main.length === 0) {
        setWarning('No questions available for that selection yet.');
        return;
      }
      const durationMs = opts.minutes === null ? null : opts.minutes * 60_000;
      const next: ExamState = {
        version: STATE_VERSION,
        examId: pattern.id,
        title: opts.title,
        kind: opts.kind,
        marking: pattern.marking,
        durationMs,
        msRemaining: durationMs ?? 0,
        msElapsed: 0,
        allowPause: opts.allowPause,
        paused: false,
        items: main.map((q, i) => ({ question: q, selected: null, flagged: false, visited: i === 0, bonus: false, timeMs: 0 })),
        currentIndex: 0,
        bonusPool: bonus,
        ...(pattern.bonus && bonus.length ? { bonusRule: pattern.bonus.rule } : {}),
        bonusStartIndex: null,
        startedAt: Date.now(),
        submitted: false,
      };
      recordSeen(pattern.id, main.map((q) => q.id));
      setSeenTotal(seenCount(pattern.id));
      setWarning(shortfalls.length ? `Question bank was short for: ${shortfalls.join(', ')}. The test runs with what is available.` : null);
      persist(next);
      setView('exam');
    },
    [bank, pattern, persist],
  );

  const handleResume = useCallback(() => {
    const saved = loadExam(examId);
    if (!saved) return setSavedExists(false);
    // Resume paused if pausing is allowed, so the clock doesn't run before they're ready.
    persist({ ...saved, paused: saved.allowPause });
    setView('exam');
  }, [persist, examId]);

  // --- submit --------------------------------------------------------------------

  // Latest exam state for submit, which may be called from the timer. Side effects
  // (history, storage) must not live inside a state updater: React may run
  // updaters twice, which recorded every attempt twice.
  const examRef = useRef(exam);
  examRef.current = exam;

  const submit = useCallback(() => {
    setConfirmSubmit(false);
    setBonusPrompt(false);
    const prev = examRef.current;
    if (!prev || prev.submitted) return;
    const done: ExamState = { ...prev, submitted: true, paused: false };
    examRef.current = done;
    const r = scoreExam(done);
    appendHistory({
      id: `attempt-${Date.now()}`,
      completedAt: Date.now(),
      examId: done.examId,
      title: done.title,
      net: r.overall.net,
      maxMarks: r.overall.maxMarks,
      correct: r.overall.correct,
      incorrect: r.overall.incorrect,
      skipped: r.overall.skipped,
      sectionNets: Object.fromEntries(r.sections.map((s) => [s.subject, s.net])),
      durationMs: done.msElapsed,
      responses: done.items.map((i) => ({
        id: i.question.id,
        selected: i.selected,
        flagged: i.flagged,
        bonus: i.bonus,
        timeMs: i.timeMs,
      })),
      marking: done.marking,
      durationLimitMs: done.durationMs,
    });
    saveLastSubmitted(done);
    clearExam(done.examId);
    setExam(done);
    setHistory(loadHistory(examId));
    setSavedExists(false);
    setLastExists(true);
    setView('results');
  }, [examId]);

  // --- clock ---------------------------------------------------------------------

  const submitRef = useRef(submit);
  submitRef.current = submit;

  useEffect(() => {
    if (view !== 'exam') return;
    const id = window.setInterval(() => {
      setExam((prev) => {
        if (!prev || prev.submitted || prev.paused) return prev;
        const items = prev.items.map((it, i) => (i === prev.currentIndex ? { ...it, timeMs: it.timeMs + TICK_MS } : it));
        const next: ExamState = {
          ...prev,
          items,
          msElapsed: prev.msElapsed + TICK_MS,
          msRemaining: prev.durationMs === null ? 0 : Math.max(0, prev.msRemaining - TICK_MS),
        };
        saveExam(next);
        if (next.durationMs !== null && next.msRemaining <= 0) {
          // Time's up: submit after this state lands.
          window.setTimeout(() => submitRef.current(), 0);
        }
        return next;
      });
    }, TICK_MS);
    return () => window.clearInterval(id);
  }, [view]);

  const togglePause = useCallback(() => {
    if (!exam || !exam.allowPause) return;
    persist({ ...exam, paused: !exam.paused });
  }, [exam, persist]);

  // Auto-pause when the tab is hidden, if pausing is allowed.
  useEffect(() => {
    const onHide = () => {
      if (document.hidden) {
        setExam((prev) => {
          if (!prev || prev.submitted || !prev.allowPause || prev.paused) return prev;
          const next = { ...prev, paused: true };
          saveExam(next);
          return next;
        });
      }
    };
    document.addEventListener('visibilitychange', onHide);
    return () => document.removeEventListener('visibilitychange', onHide);
  }, []);

  // --- navigation / answering ------------------------------------------------------

  const goTo = useCallback(
    (index: number) => {
      if (!exam || exam.paused) return;
      const min = exam.bonusStartIndex ?? 0;
      const clamped = Math.max(min, Math.min(exam.items.length - 1, index));
      const items = exam.items.map((it, i) => (i === clamped ? { ...it, visited: true } : it));
      persist({ ...exam, items, currentIndex: clamped });
    },
    [exam, persist],
  );

  const select = useCallback(
    (key: OptionKey) => updateItem((it) => ({ ...it, selected: it.selected === key ? null : key })),
    [updateItem],
  );
  const clear = useCallback(() => updateItem((it) => ({ ...it, selected: null })), [updateItem]);
  const toggleFlag = useCallback(() => updateItem((it) => ({ ...it, flagged: !it.flagged })), [updateItem]);

  const allMainAnswered = exam ? exam.items.filter((i) => !i.bonus).every((i) => i.selected !== null) : false;
  const bonusAvailable = Boolean(exam && exam.bonusPool.length > 0 && exam.bonusStartIndex === null && allMainAnswered);

  const takeBonus = useCallback(() => {
    if (!exam) return;
    const start = exam.items.length;
    const items = [
      ...exam.items,
      ...exam.bonusPool.map((q, i) => ({ question: q, selected: null, flagged: false, visited: i === 0, bonus: true, timeMs: 0 })),
    ];
    recordSeen(exam.examId, exam.bonusPool.map((q) => q.id));
    persist({ ...exam, items, bonusPool: [], bonusStartIndex: start, currentIndex: start });
    setBonusPrompt(false);
  }, [exam, persist]);

  // Keyboard shortcuts during the exam.
  useEffect(() => {
    if (view !== 'exam' || !exam) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.ctrlKey || e.metaKey || e.altKey) return;
      const k = e.key.toUpperCase();
      if (k === 'P' && exam.allowPause) return togglePause();
      if (exam.paused || confirmSubmit || bonusPrompt) return;
      if (['A', 'B', 'C', 'D'].includes(k)) select(k as OptionKey);
      else if (['1', '2', '3', '4'].includes(k)) select('ABCD'[Number(k) - 1] as OptionKey);
      else if (e.key === 'ArrowRight') goTo(exam.currentIndex + 1);
      else if (e.key === 'ArrowLeft') goTo(exam.currentIndex - 1);
      else if (k === 'M') toggleFlag();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [view, exam, select, goTo, toggleFlag, togglePause, confirmSubmit, bonusPrompt]);

  const result = useMemo(() => (exam?.submitted ? scoreExam(exam) : null), [exam]);

  // --- render ------------------------------------------------------------------------

  if (view === 'loading') return <Shell><p className="text-sm text-slate-500">Loading question bank…</p></Shell>;

  if (view === 'error')
    return (
      <Shell>
        <div className="rounded-lg border border-red-300 bg-red-50 p-5 dark:border-red-900 dark:bg-red-950/40">
          <h2 className="mb-2 font-semibold text-red-900 dark:text-red-200">Could not load the question bank</h2>
          <p className="mb-3 text-sm text-red-800 dark:text-red-300">{loadError}</p>
          <p className="text-xs text-red-700 dark:text-red-400">
            Browsers block JSON loading on <code>file://</code>. Double-click <code>start-exam.cmd</code> (or run <code>npm run dev</code>) and use the served URL.
          </p>
        </div>
      </Shell>
    );

  if (view === 'start' && bank && counts)
    return (
      <Shell nav={<SideNav current={examId} onSelect={switchExam} />}>
        {warning && <Banner>{warning}</Banner>}
        <StartScreen
          key={examId}
          pattern={pattern}
          counts={counts}
          history={history}
          hasSavedExam={savedExists}
          hasLastResult={lastExists}
          seenTotal={seenTotal}
          onStart={handleStart}
          onResume={handleResume}
          onDiscardSaved={() => {
            clearExam(examId);
            setSavedExists(false);
          }}
          onOpenAttempt={(record, then) => {
            const restored = rehydrate(record, bank);
            if (!restored) {
              setWarning('That attempt can no longer be opened: its questions are not in the current bank.');
              return;
            }
            setExam(restored);
            setReviewFilter('all');
            setView(then === 'pdf' ? 'print' : 'review');
          }}
          onOpenLast={() => {
            const last = loadLastSubmitted(examId);
            if (last) {
              setExam(last);
              setView('results');
            }
          }}
          onResetSeen={() => {
            clearSeen(examId);
            setSeenTotal(0);
          }}
          onClearHistory={() => {
            clearHistory(examId);
            setHistory([]);
          }}
        />
      </Shell>
    );

  if (view === 'results' && exam && result)
    return (
      <Shell wide nav={<SideNav current={examId} onSelect={switchExam} />}>
        <Results
          exam={exam}
          result={result}
          onReview={(f) => {
            setReviewFilter(f ?? 'all');
            setView('review');
            window.scrollTo(0, 0);
          }}
          onPdf={() => setView('print')}
          onRestart={() => {
            setWarning(null);
            setView('start');
          }}
        />
      </Shell>
    );

  if (view === 'print' && exam && result)
    return <PrintReport exam={exam} result={result} examName={pattern.name} onBack={() => setView('results')} />;

  if (view === 'review' && exam)
    return (
      <Shell>
        <ReviewList exam={exam} initialFilter={reviewFilter} onBack={() => setView('results')} onPdf={() => setView('print')} />
      </Shell>
    );

  if (view === 'exam' && exam && !exam.submitted) {
    const item = exam.items[exam.currentIndex]!;
    const answered = exam.items.filter((i) => i.selected !== null).length;
    const timed = exam.durationMs !== null;
    const low = timed && exam.msRemaining < 5 * 60_000;
    const inBonus = exam.bonusStartIndex !== null;

    return (
      <Shell wide>
        {warning && <Banner>{warning}</Banner>}
        <div className="mb-4 flex flex-wrap items-center gap-3">
          <div className="min-w-0">
            <p className="truncate text-sm font-semibold">
              {exam.title}
              {inBonus && <span className="ml-2 rounded bg-amber-100 px-1.5 py-0.5 text-xs font-bold text-amber-800 dark:bg-amber-950 dark:text-amber-300">BONUS ROUND</span>}
            </p>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              {answered} of {exam.items.length} answered · {SUBJECT_NAMES[item.question.subject]}
            </p>
          </div>
          <div className="ml-auto flex items-center gap-2">
            <div
              className={`rounded-md px-3 py-1.5 font-mono text-lg font-bold tabular-nums ${low ? 'bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300' : 'bg-slate-200 dark:bg-slate-800'}`}
              title={timed ? 'Time remaining' : 'Time elapsed (untimed)'}
            >
              {timed ? clock(exam.msRemaining) : `⏱ ${clock(exam.msElapsed)}`}
            </div>
            {exam.allowPause && (
              <button type="button" onClick={togglePause} className="rounded-md border border-slate-300 px-3 py-2 text-sm font-semibold hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800">
                {exam.paused ? '▶ Resume' : '❚❚ Pause'}
              </button>
            )}
            {bonusAvailable && (
              <button type="button" onClick={() => setBonusPrompt(true)} className="rounded-md bg-amber-500 px-3 py-2 text-sm font-semibold text-white hover:bg-amber-600">
                Bonus questions
              </button>
            )}
            <button type="button" onClick={() => setConfirmSubmit(true)} className="rounded-md bg-emerald-600 px-4 py-2 text-sm font-semibold text-white hover:bg-emerald-700">
              Submit
            </button>
          </div>
        </div>

        <div className="grid gap-5 lg:grid-cols-[1fr_280px]">
          <div className="space-y-4">
            <QuestionCard
              item={item}
              number={exam.currentIndex + 1}
              total={exam.items.length}
              marking={exam.marking}
              onSelect={select}
              onClear={clear}
              onToggleFlag={toggleFlag}
            />
            <div className="flex items-center gap-3">
              <button
                type="button"
                onClick={() => goTo(exam.currentIndex - 1)}
                disabled={exam.currentIndex <= (exam.bonusStartIndex ?? 0)}
                className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium hover:bg-slate-100 disabled:opacity-40 dark:border-slate-700 dark:hover:bg-slate-800"
              >
                ← Previous
              </button>
              <button
                type="button"
                onClick={() => goTo(exam.currentIndex + 1)}
                disabled={exam.currentIndex >= exam.items.length - 1}
                className="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700 disabled:opacity-40"
              >
                Save &amp; Next →
              </button>
              <p className="ml-auto hidden text-xs text-slate-500 sm:block">
                Negative marking: a wrong answer costs {Math.abs(exam.marking.wrong)}. Skip if unsure.
              </p>
            </div>
          </div>
          <aside className="lg:sticky lg:top-4 lg:self-start">
            <Navigator items={exam.items} currentIndex={exam.currentIndex} lockedBefore={exam.bonusStartIndex} onJump={goTo} />
          </aside>
        </div>

        {exam.paused && (
          <Modal>
            <h2 className="text-xl font-bold">Test paused</h2>
            <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
              The timer is stopped and questions are hidden.{' '}
              {timed ? `${fmtTime(exam.msRemaining)} remaining.` : `${fmtTime(exam.msElapsed)} elapsed.`}
            </p>
            <button type="button" onClick={togglePause} className="mt-4 rounded-md bg-indigo-600 px-5 py-2 font-semibold text-white hover:bg-indigo-700">
              ▶ Resume test
            </button>
            <button type="button" onClick={() => setView('start')} className="ml-2 mt-4 rounded-md border border-slate-300 px-4 py-2 text-sm dark:border-slate-700">
              Save &amp; exit
            </button>
          </Modal>
        )}

        {confirmSubmit && (
          <Modal>
            <h2 className="text-lg font-bold">Submit the test?</h2>
            <ul className="mt-2 text-sm text-slate-600 dark:text-slate-400">
              <li>Answered: {answered}</li>
              <li>Not answered: {exam.items.length - answered}</li>
              <li>Marked for review: {exam.items.filter((i) => i.flagged).length}</li>
              {bonusAvailable && <li className="text-amber-600">Bonus round still available.</li>}
            </ul>
            <div className="mt-4 flex gap-2">
              <button type="button" onClick={submit} className="rounded-md bg-emerald-600 px-4 py-2 text-sm font-semibold text-white hover:bg-emerald-700">
                Yes, submit
              </button>
              <button type="button" onClick={() => setConfirmSubmit(false)} className="rounded-md border border-slate-300 px-4 py-2 text-sm dark:border-slate-700">
                Keep going
              </button>
            </div>
          </Modal>
        )}

        {bonusPrompt && (
          <Modal>
            <h2 className="text-lg font-bold">Attempt bonus questions?</h2>
            <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">{exam.bonusRule}</p>
            <div className="mt-4 flex gap-2">
              <button type="button" onClick={takeBonus} className="rounded-md bg-amber-500 px-4 py-2 text-sm font-semibold text-white hover:bg-amber-600">
                Yes, lock my 130 answers
              </button>
              <button type="button" onClick={() => setBonusPrompt(false)} className="rounded-md border border-slate-300 px-4 py-2 text-sm dark:border-slate-700">
                Not now
              </button>
            </div>
          </Modal>
        )}
      </Shell>
    );
  }

  return (
    <Shell>
      <button type="button" onClick={() => setView('start')} className="text-sm underline">
        Back to tests
      </button>
    </Shell>
  );
}

/** Rebuilds a submitted sitting from a history record by re-joining questions from the bank. */
function rehydrate(record: AttemptRecord, bank: Bank): ExamState | null {
  if (!record.responses || !record.marking) return null;
  const byId = new Map(bank.questions.map((q) => [q.id, q]));
  const items: ExamItem[] = [];
  for (const r of record.responses) {
    const question = byId.get(r.id);
    if (question) items.push({ question, selected: r.selected, flagged: r.flagged, visited: true, bonus: r.bonus, timeMs: r.timeMs });
  }
  if (items.length === 0) return null;
  const firstBonus = items.findIndex((i) => i.bonus);
  return {
    version: STATE_VERSION,
    examId: record.examId,
    title: record.title,
    kind: 'full',
    marking: record.marking,
    durationMs: record.durationLimitMs ?? null,
    msRemaining: 0,
    msElapsed: record.durationMs,
    allowPause: false,
    paused: false,
    items,
    currentIndex: 0,
    bonusPool: [],
    bonusStartIndex: firstBonus === -1 ? null : firstBonus,
    startedAt: record.completedAt - record.durationMs,
    submitted: true,
  };
}

function clock(ms: number): string {
  const s = Math.ceil(ms / 1000);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  return `${h > 0 ? `${h}:` : ''}${String(m).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
}

/** Exams in the side menu. Hidden during a sitting so the test has the full screen. */
function SideNav({ current, onSelect }: { current: string; onSelect: (id: string) => void }) {
  return (
    <nav aria-label="Exams" className="flex gap-2 overflow-x-auto md:flex-col md:gap-1 md:overflow-visible">
      <p className="hidden px-3 pb-2 text-xs font-bold uppercase tracking-wider text-slate-500 md:block">Mock tests</p>
      {EXAMS.map((e) => {
        const active = e.id === current;
        return (
          <button
            key={e.id}
            type="button"
            onClick={() => onSelect(e.id)}
            aria-current={active ? 'page' : undefined}
            className={`shrink-0 rounded-lg px-3 py-2 text-left transition ${
              active
                ? 'bg-indigo-600 text-white'
                : 'text-slate-700 hover:bg-slate-200 dark:text-slate-300 dark:hover:bg-slate-800'
            }`}
          >
            <span className="block text-sm font-semibold">{e.name}</span>
            <span className={`block text-[11px] ${active ? 'text-indigo-100' : 'text-slate-500'}`}>
              {e.status === 'ready' ? e.fullName : 'Coming soon'}
            </span>
          </button>
        );
      })}
    </nav>
  );
}

function Shell({ children, wide = false, nav }: { children: React.ReactNode; wide?: boolean; nav?: React.ReactNode }) {
  if (!nav) {
    return (
      <div className="min-h-screen px-4 py-6">
        <div className={wide ? 'mx-auto max-w-6xl' : 'mx-auto max-w-4xl'}>{children}</div>
      </div>
    );
  }
  return (
    <div className="min-h-screen md:flex">
      <aside className="border-b border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900 md:sticky md:top-0 md:h-screen md:w-56 md:shrink-0 md:border-b-0 md:border-r md:py-6">
        {nav}
      </aside>
      <main className="min-w-0 flex-1 px-4 py-6">
        <div className={wide ? 'mx-auto max-w-6xl' : 'mx-auto max-w-4xl'}>{children}</div>
      </main>
    </div>
  );
}

function Banner({ children }: { children: React.ReactNode }) {
  return (
    <div className="mb-4 rounded-md border border-amber-300 bg-amber-50 p-3 text-sm text-amber-900 dark:border-amber-800 dark:bg-amber-950/40 dark:text-amber-200">
      {children}
    </div>
  );
}

function Modal({ children }: { children: React.ReactNode }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/70 p-4 backdrop-blur-md">
      <div className="w-full max-w-md rounded-xl bg-white p-6 shadow-xl dark:bg-slate-900">{children}</div>
    </div>
  );
}
