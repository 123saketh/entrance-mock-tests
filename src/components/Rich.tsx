import katex from 'katex';
import 'katex/dist/katex.min.css';
import { memo, useMemo } from 'react';

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderMath(tex: string, displayMode: boolean): string {
  try {
    return katex.renderToString(tex, { displayMode, throwOnError: false, strict: 'ignore' });
  } catch {
    return escapeHtml(tex);
  }
}

/**
 * Converts text with $...$ / $$...$$ / \(...\) / \[...\] into HTML. Non-math text
 * is escaped, so question content can never inject markup. `\$` is a literal dollar.
 */
export function toHtml(text: string): string {
  const out: string[] = [];
  const re = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<!\\)\$((?:\\\$|[^$])+?)\$/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) {
    out.push(plain(text.slice(last, m.index)));
    const display = m[1] ?? m[2];
    out.push(display !== undefined ? renderMath(display, true) : renderMath((m[3] ?? m[4])!, false));
    last = m.index + m[0].length;
  }
  out.push(plain(text.slice(last)));
  return out.join('');
}

function plain(s: string): string {
  return escapeHtml(s.replace(/\\\$/g, '$')).replace(/\n/g, '<br/>');
}

interface Props {
  text: string;
  className?: string;
  as?: 'div' | 'span';
}

/** Renders question/option/explanation text with KaTeX math. */
function RichImpl({ text, className, as = 'div' }: Props) {
  const html = useMemo(() => toHtml(text), [text]);
  const Tag = as;
  return <Tag className={className} dangerouslySetInnerHTML={{ __html: html }} />;
}

export default memo(RichImpl);
