/**
 * Validates every question file and writes public/data/manifest.json.
 * Run: npm run validate
 */
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import katex from 'katex';
import { SUBJECTS, type Question } from '../src/types';

const DIR = join(import.meta.dirname, '..', 'public', 'data', 'questions');
const files = readdirSync(DIR).filter((f) => f.endsWith('.json')).sort();

const errors: string[] = [];
const warnings: string[] = [];
const ids = new Set<string>();
const bySubject: Record<string, { authored: number; harvested: number }> = {};
const answers: Record<string, number> = { A: 0, B: 0, C: 0, D: 0 };
const okFiles: string[] = [];

const MATH = /\$\$([\s\S]+?)\$\$|(?<!\\)\$((?:\\\$|[^$])+?)\$/g;
function checkMath(text: string, where: string) {
  const stripped = text.replace(MATH, '');
  if (/(?<!\\)\$/.test(stripped)) warnings.push(`${where}: unbalanced $`);
  for (const m of text.matchAll(MATH)) {
    try {
      katex.renderToString((m[1] ?? m[2])!, { throwOnError: true, strict: 'ignore' });
    } catch (e) {
      warnings.push(`${where}: KaTeX: ${(e as Error).message.slice(0, 90)}`);
    }
  }
}

for (const f of files) {
  let data: Question[];
  try {
    data = JSON.parse(readFileSync(join(DIR, f), 'utf8')) as Question[];
  } catch (e) {
    errors.push(`${f}: invalid JSON (${(e as Error).message})`);
    continue;
  }
  if (!Array.isArray(data)) {
    errors.push(`${f}: not an array`);
    continue;
  }
  okFiles.push(f);
  for (const q of data) {
    const at = `${f}:${q.id}`;
    if (!q.id) errors.push(`${f}: question without id`);
    if (ids.has(q.id)) errors.push(`${at}: duplicate id`);
    ids.add(q.id);
    if (!SUBJECTS.includes(q.subject)) errors.push(`${at}: bad subject ${q.subject}`);
    if (!Array.isArray(q.options) || q.options.length !== 4) errors.push(`${at}: needs 4 options`);
    const keys = (q.options ?? []).map((o) => o.key).join('');
    if (keys !== 'ABCD') errors.push(`${at}: option keys ${keys}`);
    if (!['A', 'B', 'C', 'D'].includes(q.answer)) errors.push(`${at}: bad answer ${q.answer}`);
    if (!q.stem?.trim()) errors.push(`${at}: empty stem`);
    if (!q.explanation?.trim()) warnings.push(`${at}: no explanation`);
    if (!['easy', 'medium', 'hard'].includes(q.difficulty)) errors.push(`${at}: bad difficulty`);
    if (new Set((q.options ?? []).map((o) => o.text.trim() + (o.image ?? ''))).size !== 4) warnings.push(`${at}: duplicate option text`);
    checkMath(q.stem ?? '', at);
    for (const o of q.options ?? []) checkMath(o.text, `${at}/${o.key}`);
    checkMath(q.explanation ?? '', `${at}/expl`);
    const images = [q.stemImage, q.explanationImage, ...(q.options ?? []).map((o) => o.image)].filter(Boolean) as string[];
    for (const img of images) {
      if (!existsSync(join(DIR, '..', img))) errors.push(`${at}: missing figure ${img}`);
    }
    for (const o of q.options ?? []) if (!o.text?.trim() && !o.image) errors.push(`${at}/${o.key}: option has neither text nor image`);
    const kind = q.source?.kind === 'harvested' ? 'harvested' : 'authored';
    (bySubject[q.subject] ??= { authored: 0, harvested: 0 })[kind]++;
    answers[q.answer] = (answers[q.answer] ?? 0) + 1;
  }
}

writeFileSync(join(DIR, '..', 'manifest.json'), JSON.stringify({ files: okFiles }, null, 2) + '\n');

console.log(`Files: ${okFiles.join(', ')}`);
console.log(`Questions: ${ids.size}`);
console.table(bySubject);
console.log('Answer distribution:', answers);
if (warnings.length) {
  console.log(`\n${warnings.length} warning(s):`);
  for (const w of warnings.slice(0, 60)) console.log('  ! ' + w);
  if (warnings.length > 60) console.log(`  ... ${warnings.length - 60} more`);
}
if (errors.length) {
  console.error(`\n${errors.length} error(s):`);
  for (const e of errors) console.error('  x ' + e);
  process.exit(1);
}
console.log('\nOK - manifest written.');
