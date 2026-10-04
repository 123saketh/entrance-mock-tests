/** Mock exam app — shared types. Exam-agnostic so other entrance exams can be added via configs. */

export const SUBJECTS = ['physics', 'chemistry', 'english', 'reasoning', 'mathematics'] as const;
export type SubjectId = (typeof SUBJECTS)[number];

export const SUBJECT_NAMES: Record<SubjectId, string> = {
  physics: 'Physics',
  chemistry: 'Chemistry',
  english: 'English Proficiency',
  reasoning: 'Logical Reasoning',
  mathematics: 'Mathematics',
};

export const SUBJECT_SHORT: Record<SubjectId, string> = {
  physics: 'PHY',
  chemistry: 'CHE',
  english: 'ENG',
  reasoning: 'LR',
  mathematics: 'MAT',
};

export type OptionKey = 'A' | 'B' | 'C' | 'D';
export type Difficulty = 'easy' | 'medium' | 'hard';

export interface QuestionOption {
  key: OptionKey;
  text: string;
  /** Figure path relative to public/data/, e.g. "figures/lr/x.svg". */
  image?: string;
}

export interface QuestionSource {
  kind: 'authored' | 'harvested';
  name?: string;
  url?: string;
  licence?: string;
}

export interface Question {
  id: string;
  subject: SubjectId;
  topic: string;
  difficulty: Difficulty;
  /** Plain text with $...$ / $$...$$ LaTeX, rendered by KaTeX. */
  stem: string;
  options: QuestionOption[];
  answer: OptionKey;
  explanation: string;
  /** Figures, as paths relative to public/data/. */
  stemImage?: string;
  explanationImage?: string;
  source: QuestionSource;
  /**
   * Exam ids this question is restricted to (e.g. ["eamcet-ts"]). Absent means
   * generic: usable by any exam that has the subject.
   */
  exams?: string[];
  /** Set on previous-year questions: the paper it appeared in, e.g. "JEE Main 2025 · January". */
  pyq?: string;
}

/** Marks awarded per response. `wrong` is negative for negative marking. */
export interface MarkingScheme {
  correct: number;
  wrong: number;
  skipped: number;
}

export interface SectionSpec {
  subject: SubjectId;
  count: number;
}

export interface BonusSpec {
  /** Questions per subject offered once every main question is attempted. */
  sections: SectionSpec[];
  /** Shown before the candidate commits. */
  rule: string;
}

/** A complete exam pattern, e.g. the BITSAT full paper. */
export interface ExamPattern {
  id: string;
  /** Short name for the side menu. */
  name: string;
  /** Official name shown as a subtitle. */
  fullName: string;
  /** 'coming-soon' shows the pattern but disables tests until the bank is ready. */
  status: 'ready' | 'coming-soon';
  durationMin: number;
  marking: MarkingScheme;
  sections: SectionSpec[];
  bonus?: BonusSpec;
  notes: string[];
}

/** 'pyq' = previous-year questions (`pyq` set); 'harvested' = other imports. */
export type SourceFilter = 'all' | 'authored' | 'harvested' | 'pyq';
export type TimerMode = 'exam' | 'custom' | 'untimed';

export interface ExamItem {
  question: Question;
  /** Selected option, or null when not answered. */
  selected: OptionKey | null;
  /** "Mark for review". */
  flagged: boolean;
  visited: boolean;
  bonus: boolean;
  /** Time spent on this question, for the review. */
  timeMs: number;
}

export interface ExamState {
  version: number;
  /** Which exam family and what kind of sitting. */
  examId: string;
  title: string;
  kind: 'full' | 'subject' | 'custom';
  marking: MarkingScheme;
  /** null = untimed. */
  durationMs: number | null;
  msRemaining: number;
  msElapsed: number;
  allowPause: boolean;
  paused: boolean;
  items: ExamItem[];
  currentIndex: number;
  /** Questions held back for the bonus round. Empty when the sitting has no bonus. */
  bonusPool: Question[];
  bonusRule?: string;
  /** Index where bonus items begin once taken; earlier items are then locked. */
  bonusStartIndex: number | null;
  startedAt: number;
  submitted: boolean;
}

export interface Tally {
  total: number;
  attempted: number;
  correct: number;
  incorrect: number;
  skipped: number;
  positive: number;
  /** Positive number: marks lost to negative marking. */
  negative: number;
  net: number;
  maxMarks: number;
  /** Percent of attempted that were correct. */
  accuracy: number;
  timeMs: number;
}

export interface SectionResult extends Tally {
  subject: SubjectId;
}

export interface ExamResult {
  overall: Tally;
  sections: SectionResult[];
  bonusTaken: boolean;
  bonus?: Tally;
  durationMs: number;
  topicStats: { subject: SubjectId; topic: string; correct: number; total: number }[];
}

export interface AttemptRecord {
  id: string;
  completedAt: number;
  examId: string;
  title: string;
  net: number;
  maxMarks: number;
  correct: number;
  incorrect: number;
  skipped: number;
  sectionNets: Partial<Record<SubjectId, number>>;
  durationMs: number;
  /**
   * Compact responses so any past attempt can be reviewed or exported later.
   * Questions are re-joined from the bank by id. Absent on old records.
   */
  responses?: AttemptResponse[];
  marking?: MarkingScheme;
  durationLimitMs?: number | null;
}

export interface AttemptResponse {
  id: string;
  selected: OptionKey | null;
  flagged: boolean;
  bonus: boolean;
  timeMs: number;
}

export interface SeenRecord {
  count: number;
  lastSeen: number;
}
export type SeenMap = Record<string, SeenRecord>;
