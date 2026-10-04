interface Props {
  /** Path relative to public/data/, e.g. "figures/lr/q1.svg". */
  src: string;
  alt: string;
  size?: 'stem' | 'option' | 'explanation';
}

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

const SIZE: Record<NonNullable<Props['size']>, string> = {
  stem: 'max-h-72 max-w-full',
  option: 'max-h-32 max-w-[160px]',
  explanation: 'max-h-60 max-w-full',
};

/**
 * Question figures. Loaded via <img> so an SVG can never run script, and shown
 * on a white tile because figures are drawn black-on-white (dark mode too).
 */
export default function Figure({ src, alt, size = 'stem' }: Props) {
  return (
    <span className="figure inline-block rounded-md border border-slate-200 bg-white p-2 dark:border-slate-700">
      <img src={`${BASE}/data/${src}`} alt={alt} loading="lazy" className={`block h-auto ${SIZE[size]}`} />
    </span>
  );
}

/** Picture-only options read best side by side, as on the real exam screen. */
export function optionsAreFigures(options: { text: string; image?: string }[]): boolean {
  return options.every((o) => o.image && !o.text.trim());
}
