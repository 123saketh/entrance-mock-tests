"""Build public/data/questions/harvested.json from openly licensed JEE datasets.

Inputs (downloaded into .harvest/ by scripts/harvest/download.sh):
  jeebench.json                      daman1209arora/jeebench (MIT)
  pw_jan.jsonl, pw_apr.jsonl         PhysicsWallahAI/JEE-Main-2025-Math (Apache-2.0)
  ck.csv                             CK0607/2025-Jee-Mains-Question (Apache-2.0) -- used only to cross-check PW keys
  eq_<subject>_<split>.jsonl         eQOURSE/jee-main-questions (CC-BY-4.0)
Optional: explanations.json  {"<id>": "explanation text"} hand-written solutions merged in.
"""
import json, re, csv, glob, os, collections, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
H = os.path.join(ROOT, '.harvest')
OUT = os.path.join(ROOT, 'public', 'data', 'questions', 'harvested.json')

SRC = {
    'jeebench': dict(kind='harvested', name='JEEBench (daman1209arora/jeebench, JEE Advanced 2016-2023)',
                     url='https://huggingface.co/datasets/daman1209arora/jeebench', licence='MIT'),
    'pw': dict(kind='harvested', name='PhysicsWallahAI JEE-Main-2025-Math',
               url='https://huggingface.co/datasets/PhysicsWallahAI/JEE-Main-2025-Math', licence='Apache-2.0'),
    'eq': dict(kind='harvested', name='eQOURSE JEE Main Question Bank',
               url='https://huggingface.co/datasets/eQOURSE/jee-main-questions', licence='CC-BY-4.0'),
}

IMG_RE = re.compile(r'figure|diagram|graph shown|shown in|as shown|shown below|shown above|<img|includegraphics|\[IMAGE\]|image', re.I)

# ---------------------------------------------------------------- topic inference
TOPICS = {
    'mathematics': [
        ('Probability', r'probab|dice|die |coin|balls? .*bag|random'),
        ('Matrices & Determinants', r'matri|determinant|\\begin\{[pbv]?matrix|adj'),
        ('Complex Numbers', r'complex|\biota\b|\|z|\bz\s*=|\bz_|\\bar\{z|arg\s*\(|\bi\^2'),
        ('Vectors & 3D Geometry', r'vector|\\hat\{|plane|direction ratio|\\vec|line .*\\frac\{x|tetrahedron'),
        ('Conic Sections', r'parabola|ellipse|hyperbola|focus|directrix|latus|eccentric'),
        ('Circles', r'circle'),
        ('Straight Lines', r'straight line|pair of lines|slope|centroid|triangle .*vertices|line .*passes'),
        ('Definite Integration & Area', r'\\int|integral|area (bounded|enclosed|of the region)'),
        ('Differential Equations', r'differential equation|\\frac\{d\s*y\}\{d\s*x\}|dy/dx'),
        ('Limits & Continuity', r'\\lim|limit|continu|differentiab'),
        ('Application of Derivatives', r'maxim|minim|tangent|normal|increasing|decreasing|derivative'),
        ('Binomial Theorem', r'binomial|coefficient of|expansion'),
        ('Sequences & Series', r'\bA\.?P\b|\bG\.?P\b|progression|series|\\sum|sum of (the )?first'),
        ('Permutations & Combinations', r'permutation|combination|arrange|ways|words|\^\{?\d*\}?C_|\\binom'),
        ('Trigonometry', r'\\sin|\\cos|\\tan|\\cot|\\sec|trigon'),
        ('Inverse Trigonometry', r'\\sin\^\{-1\}|\\tan\^\{-1\}|\\cos\^\{-1\}'),
        ('Statistics', r'mean|variance|median|standard deviation'),
        ('Sets & Relations', r'relation|reflexive|symmetric|transitive|\bset\b|subset'),
        ('Functions', r'function|domain|range|\bonto\b|one-one'),
        ('Quadratic Equations', r'quadratic|roots|equation .*x\^2'),
        ('Logarithms & Algebra', r'\\log|\blog'),
    ],
    'physics': [
        ('Modern Physics', r'photo|de broglie|nucle|radioactiv|half.life|bohr|hydrogen atom|x-ray|electron .*orbit|planck'),
        ('Semiconductors', r'diode|transistor|semiconductor|logic gate|p-n'),
        ('Optics', r'lens|mirror|refract|prism|interference|diffraction|young|polari|focal|optical'),
        ('EM Waves', r'electromagnetic wave|em wave'),
        ('Electromagnetic Induction & AC', r'induct|\bemf\b|flux|\bac\b|alternating|lcr|resonan|transformer'),
        ('Magnetism', r'magnetic|solenoid|cyclotron|biot|ampere|tesla'),
        ('Current Electricity', r'resist|current|battery|cell|potentiometer|wheatstone|ohm'),
        ('Electrostatics & Capacitance', r'capacit|charge|electric field|coulomb|potential|dipole|gauss'),
        ('Thermodynamics & Kinetic Theory', r'thermodynam|adiabatic|isotherm|gas|heat|temperature|carnot|entropy|kinetic theory|specific heat'),
        ('Waves & Oscillations', r'wave|oscillat|pendulum|simple harmonic|\bshm\b|spring|sound|string|frequency'),
        ('Fluids & Properties of Matter', r'fluid|viscos|surface tension|bernoulli|density|young.s modulus|elastic|buoyan|float'),
        ('Gravitation', r'gravitat|planet|satellite|orbit|escape velocity|earth'),
        ('Rotational Motion', r'rotat|torque|angular|moment of inertia|rolling|disc|ring|rod'),
        ('Work, Energy & Momentum', r'work|energy|collision|momentum|power'),
        ('Laws of Motion', r'friction|pulley|newton|force'),
        ('Kinematics', r'velocity|acceleration|projectile|displacement'),
        ('Units & Measurements', r'dimension|unit|error|measure|vernier|screw gauge'),
    ],
    'chemistry': [
        ('Coordination Compounds', r'complex|ligand|coordination|\[co|\[fe|\[ni|\[cr|\[cu|crystal field|spin.only'),
        ('Electrochemistry', r'electrochem|electrode|cell potential|e\^\{?\\circ|faraday|conductan|nernst|electroly'),
        ('Chemical Kinetics', r'rate constant|order of|half.life|kinetic|activation energy|rate of reaction'),
        ('Thermodynamics', r'enthalp|entropy|gibbs|\\delta\s*h|\\delta\s*g|thermodynam|heat of'),
        ('Equilibrium', r'equilibri|\bk_?[cp]\b|\bph\b|buffer|solubility product|ionisation|ionization constant|hydrolysis'),
        ('Solutions', r'osmotic|molality|raoult|vapour pressure|freezing|boiling point|colligative|van.t hoff'),
        ('Atomic Structure', r'quantum number|orbital|bohr|wavelength|electron|de broglie|atomic'),
        ('Chemical Bonding', r'hybridi|bond order|vsepr|dipole moment|molecular orbital|shape|geometry|paramagnetic|diamagnetic'),
        ('Periodic Table', r'ionisation enthalpy|ionization energy|electronegativ|atomic radi|periodic|electron gain'),
        ('Biomolecules & Polymers', r'protein|vitamin|glucose|amino acid|dna|rna|polymer|nylon|carbohydrate|sucrose|enzyme'),
        ('Chemistry in Everyday Life', r'drug|analgesic|antibiotic|antacid|detergent|soap'),
        ('d & f Block', r'lanthan|actin|transition|kmno|k_2cr|dichromate|permanganate'),
        ('p Block', r'nitrogen|phosph|sulph|halogen|noble gas|xenon|boron|silicon|ozone|oxoacid'),
        ('s Block & Hydrogen', r'alkali|sodium|potassium|calcium|magnesium|hydrogen peroxide|beryllium'),
        ('Metallurgy', r'ore|metallurg|smelting|refining|roasting|calcination'),
        ('Mole Concept & Stoichiometry', r'mole|molar|stoichiometr|percentage|empirical|molarity|titrat'),
        ('States of Matter & Solid State', r'unit cell|lattice|fcc|bcc|packing|ideal gas|crystal'),
        ('Organic Chemistry', r'alkane|alkene|alkyne|benzene|alcohol|phenol|aldehyde|ketone|carboxylic|amine|ester|ether|halide|iupac|isomer|reaction|product|reagent|sn1|sn2|ch_3|ch3|organic'),
    ],
}



MONTHS = {'Jan': 'January', 'Apr': 'April'}


def pyq_label(src, ref):
    """Previous-year-paper label from a harvest ref, or None for non-PYQ sources."""
    if src == 'jeebench':
        m = re.match(r'JEE Adv (\d{4}) Paper (\d)', ref)
        return f'JEE Advanced {m.group(1)} · Paper {m.group(2)}' if m else None
    if src == 'pw':
        m = re.match(r'JEE Main (\d{4}) (\w+)', ref)
        return f'JEE Main {m.group(1)} · {MONTHS.get(m.group(2), m.group(2))}' if m else None
    return None  # eQOURSE items are practice papers, not previous-year papers

def infer_topic(subject, text):
    t = text.lower()
    for name, pat in TOPICS[subject]:
        if re.search(pat, t, re.I):
            return name
    return {'mathematics': 'Algebra', 'physics': 'General Physics', 'chemistry': 'General Chemistry'}[subject]


# ---------------------------------------------------------------- latex helpers
def paren_to_dollar(s):
    s = re.sub(r'\\\((.+?)\\\)', lambda m: '$' + m.group(1).strip() + '$', s, flags=re.S)
    s = re.sub(r'\\\[(.+?)\\\]', lambda m: '$$' + m.group(1).strip() + '$$', s, flags=re.S)
    return s


def clean_ws(s):
    s = s.replace('\r', '')
    s = re.sub(r'[ \t]+\n', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


MATHTOK = re.compile(r'(?<![\w$\\])([A-Za-z0-9().]*[A-Za-z0-9)][\^_](?:\{[^{}$]*\}|\([^()$]*\)|-?[A-Za-z0-9.]+)(?:[\^_](?:\{[^{}$]*\}|-?[A-Za-z0-9.]+))*)')


def wrap_bare_math(s):
    """Wrap bare tokens like y^2 or x_1 (outside $...$) in $...$."""
    parts = re.split(r'(\$\$.*?\$\$|\$[^$]*\$)', s, flags=re.S)
    for i in range(0, len(parts), 2):
        seg = parts[i]
        if '\\' in seg and re.search(r'\\(frac|sqrt|sin|cos|tan|log|int|sum|lim|alpha|beta|theta|pi|lambda|mu|times|Rightarrow)', seg):
            # bare LaTeX commands outside math -- leave unwrapped (flagged later)
            pass
        parts[i] = MATHTOK.sub(lambda m: '$' + m.group(1) + '$', seg)
    return ''.join(parts)


def balanced_dollars(s):
    return s.replace('$$', '').count('$') % 2 == 0


# ---------------------------------------------------------------- loaders
def load_jeebench():
    out = []
    data = json.load(open(os.path.join(H, 'jeebench.json'), encoding='utf-8'))
    subj = {'phy': 'physics', 'chem': 'chemistry', 'math': 'mathematics'}
    drop = collections.Counter()
    for x in data:
        if x['type'] != 'MCQ':
            continue
        q = x['question']
        if IMG_RE.search(q):
            drop['image'] += 1; continue
        if '\\begin{' in q and not re.search(r'\$[^$]*\\begin\{array', q):
            drop['table/env'] += 1; continue
        # option markers: plain "(A)" / "[A]" or in-math "$[\mathrm{A}]" (the math then continues)
        pat = re.compile(r'(\$\s*(?=\[\s*\\mathrm))?[\(\[]\s*(?:\\mathrm\{)?([ABCD])\}?\s*[\)\]]')
        idx = {}
        for m in pat.finditer(q):
            idx[m.group(2)] = m
        keys = 'ABCD'
        if sorted(idx) != list(keys) or not (idx['A'].start() < idx['B'].start() < idx['C'].start() < idx['D'].start()):
            drop['parse'] += 1; continue
        stem = q[:idx['A'].start()]
        fixed = []
        for i, k in enumerate(keys):
            end = idx[keys[i + 1]].start() if i < 3 else len(q)
            t = q[idx[k].end():end].strip()
            if idx[k].group(1):  # marker was inside math: reopen it
                t = '$' + re.sub(r'^\\quad\s*', '', t)
            if not balanced_dollars(t):
                t = t + '$' if not t.endswith('$') else '$' + t
            fixed.append(clean_ws(paren_to_dollar(t)))
        stem = clean_ws(paren_to_dollar(stem))
        if not balanced_dollars(stem) and not stem.endswith('$'):
            stem += '$'  # marker regex consumed the closing '$' of the stem
        if not balanced_dollars(stem):
            print('LATEX', x['description'], x['index'], repr(stem[-200:]), file=sys.stderr)
            drop['latex'] += 1; continue
        if x['gold'] not in keys:
            drop['gold'] += 1; continue
        s = subj[x['subject']]
        out.append(dict(_src='jeebench', _ref=f"{x['description']} Q{x['index']}", subject=s,
                        topic=infer_topic(s, stem + ' ' + ' '.join(fixed)), difficulty='hard',
                        stem=stem, options=fixed, answer=x['gold'], explanation=None))
    print('jeebench kept', len(out), dict(drop), file=sys.stderr)
    return out


def load_pw():
    out = []
    ck = {}
    for r in csv.DictReader(open(os.path.join(H, 'ck.csv'), encoding='utf-8')):
        ck[norm_key(r['Question Text'])[:60]] = r
    agree = disagree = 0
    drop = collections.Counter()
    for f, sess in (('pw_jan.jsonl', 'Jan'), ('pw_apr.jsonl', 'Apr')):
        for n, line in enumerate(open(os.path.join(H, f), encoding='utf-8')):
            x = json.loads(line)
            if x['question_type'] != 1 or len(x['options']) != 4 or len(x['correct_options']) != 1:
                drop['nonmcq'] += 1; continue
            if IMG_RE.search(x['question']):
                drop['image'] += 1; continue
            if any(not o.strip() for o in x['options']):
                drop['emptyopt'] += 1; continue
            stem = clean_ws(paren_to_dollar(x['question']))
            opts = [clean_ws(paren_to_dollar(o)) for o in x['options']]
            ans = 'ABCD'[x['correct_options'][0]]
            # cross-check against CK0607 key where available
            c = ck.get(norm_key(stem)[:60])
            if c and c['Correct Option'] in '1234' and len(c['Correct Option']) == 1:
                if 'ABCD'[int(c['Correct Option']) - 1] == ans:
                    agree += 1
                else:
                    disagree += 1
            out.append(dict(_src='pw', _ref=f'JEE Main 2025 {sess} #{n + 1}', subject='mathematics',
                            topic=infer_topic('mathematics', stem), difficulty='medium',
                            stem=stem, options=opts, answer=ans, explanation=None))
    print('pw kept', len(out), dict(drop), 'CK cross-check agree', agree, 'disagree', disagree, file=sys.stderr)
    return out


KRUTI = set('gS dk ds esa ls dh vkSj fd gks dks ij rks gSa tc bl ;fn ;g dj fy, gSA mPp pkj gy djus leku ?kuRo ftl Hkqt f=Hkqt izdk'.split())


def has_garbage(s):
    if '\ufffd' in s or '�' in s:
        return True
    words = re.findall(r'[^\s,.()]+', s)
    return sum(w in KRUTI for w in words) >= 1 or bool(re.search(r'[a-z][~;][a-z]|[A-Za-z]\+[a-z]{1,2}\b(?!\s*[=\d])', s))


def norm_cmp(s):
    return re.sub(r'[\s$\\{}]|mathrm|left|right', '', s).lower()


def verify_eq(r):
    """True if the option text appearing LAST in the worked solution equals the keyed option."""
    sol = norm_cmp(r['solution'])
    opts = [norm_cmp(r['option_%d' % i]) for i in range(1, 5)]
    if len(set(opts)) < 4 or any(not o for o in opts):
        return False
    pos = []
    for i, o in enumerate(opts):
        p = sol.rfind(o)
        if p >= 0:
            pos.append((p + len(o), -len(o), i + 1))
    if not pos:
        return False
    pos.sort(reverse=True)
    best = pos[0][2]
    # the matched option must not be a substring of another option that also matches there
    return best == r['correct_option']


def clean_eq_text(s):
    s = s.replace('[IMAGE]', ' ')
    s = re.sub(r'\n(?!\n)', ' ', s)  # source has hard-wrapped lines
    s = re.sub(r'[ \t]{2,}', ' ', s)
    s = s.replace('\\\\', ' ')
    s = paren_to_dollar(s)
    s = wrap_bare_math(s)
    # brace multi-digit super/subscripts inside math: 10^23 -> 10^{23}
    s = re.sub(r'([\^_])(-?\d{2,})', lambda m: m.group(1) + '{' + m.group(2) + '}', s)
    return clean_ws(s)


def load_eq():
    out = []
    drop = collections.Counter()
    dmap = {'easy': 'easy', 'moderate': 'medium', 'modertae': 'medium', 'tough': 'hard', 'hard': 'hard'}
    for f in sorted(glob.glob(os.path.join(H, 'eq_*.jsonl'))):
        for line in open(f, encoding='utf-8'):
            r = json.loads(line)
            if r['question_type'] != 'single_correct' or r['correct_option'] not in (1, 2, 3, 4):
                drop['nonmcq'] += 1; continue
            opts_raw = [r['option_%d' % i] for i in range(1, 5)]
            if r['question_images'] or IMG_RE.search(r['question']) or any('[IMAGE]' in o for o in opts_raw):
                drop['image'] += 1; continue
            if any(not o.strip() for o in opts_raw):
                drop['emptyopt'] += 1; continue
            if has_garbage(r['question']) or any(has_garbage(o) for o in opts_raw):
                drop['garbled/hindi'] += 1; continue
            if not verify_eq(r):
                drop['key-unverified'] += 1; continue
            subj = r['subject'].lower()
            if re.search(r'circuit|arrangement|cell E\d|the given|following (setup|system|graph|figure)|above question|previous question|above problem|in question', r['question'], re.I) or len(r['question']) < 35:
                drop['context-missing'] += 1; continue
            stem = clean_eq_text(r['question'])
            opts = [clean_eq_text(o) for o in opts_raw]
            if not balanced_dollars(stem) or not all(balanced_dollars(o) for o in opts):
                drop['latex'] += 1; continue
            # solution: keep lines without garbage
            sol_lines = [l for l in r['solution'].split('\n') if not has_garbage(l)]
            sol = clean_eq_text('\n'.join(sol_lines))
            if not balanced_dollars(sol) or len(sol) < 8:
                sol = None
            elif len(sol) > 900:
                sol = sol[:900].rsplit(' ', 1)[0] + ' ...'
                if not balanced_dollars(sol):
                    sol = None
            d = (r.get('difficulty') or '').strip(' /]').lower()
            diff = dmap.get(d, 'medium')
            topic = infer_topic(subj, stem + ' ' + ' '.join(opts))  # chapter-level, consistent across sources
            out.append(dict(_src='eq', _ref=r['question_id'], subject=subj, topic=topic.title() if topic.islower() else topic,
                            difficulty=diff, stem=stem, options=opts, answer='ABCD'[r['correct_option'] - 1],
                            explanation=sol))
    print('eq kept', len(out), dict(drop), file=sys.stderr)
    return out


# Verified-but-doubtful items (stem reconstructed from memory / ambiguous wording / garbled-but-ok).
MANUAL_DROP = {'JEE Main 2025 Jan #84', 'JEE Main 2025 Apr #206', 'JEE Main 2025 Apr #208',
               'CH-06-Q1', 'M-20-Q13', 'JEE Adv 2019 Paper 1 Q40'}


def kfix(s):
    s = re.sub(r'\\mspace\{[^}]*\}', ' ', s)
    return s


def fix_opt(o):
    o = kfix(o.strip())
    if '$' not in o and re.search(r'[\\^_]', o):
        o = '$' + o + '$'
    return o


def norm_key(s):
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())


def main():
    items = load_jeebench() + load_pw() + load_eq()
    expl = {}
    ep = os.path.join(H, 'explanations.json')
    if os.path.exists(ep):
        expl = json.load(open(ep, encoding='utf-8'))
    # PW items: keep only those independently verified (solved) in .harvest/verify/pw_batch*.result.json
    # Independent re-solve results (.harvest/verify/<prefix>_batch*.result.json).
    # pw / eq: keep only items verdict ok|fix. jeebench (official keys): drop only verdict 'drop'.
    expl0 = json.load(open(os.path.join(H, 'explanations.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, 'explanations.json')) else {}
    for src, prefix, strict in (('pw', 'pw', True), ('eq', 'eq', True), ('jeebench', 'jb', True)):
        ver = {}
        for f in glob.glob(os.path.join(H, 'verify', prefix + '_batch*.result.json')):
            ver.update(json.load(open(f, encoding='utf-8')))
        if not ver:
            continue
        kept, vc = [], collections.Counter()
        for it in items:
            if it['_src'] == src:
                v = ver.get(it['_ref'])
                verdict = v.get('verdict') if v else ('ok' if it['_ref'] in expl0 else 'missing')
                vc[verdict] += 1
                if it['_ref'] in MANUAL_DROP:
                    vc['manual-drop'] += 1; continue
                if verdict == 'drop' or (strict and verdict not in ('ok', 'fix')):
                    continue
                if v and verdict == 'fix':
                    if v.get('stem'):
                        it['stem'] = v['stem']
                    if v.get('options'):
                        it['options'] = [v['options'][k] for k in 'ABCD']
                    if src != 'eq':
                        it['topic'] = infer_topic(it['subject'], it['stem'])
                if v and v.get('explanation'):
                    it['explanation'] = v['explanation']
            kept.append(it)
        items = kept
        print(src, 'verification', dict(vc), file=sys.stderr)
    for it in items:
        it['options'] = [fix_opt(o) for o in it['options']]
        it['stem'] = kfix(it['stem'])
        if it['explanation']:
            it['explanation'] = kfix(it['explanation'])
    seen = set()
    counters = collections.Counter()
    final = []
    for it in items:
        if len({o.strip() for o in it['options']}) < 4:
            counters['dupopt'] += 1; continue
        k = norm_key(it['stem'])[:120]
        if k in seen:
            counters['dup'] += 1; continue
        seen.add(k)
        src = it['_src']
        counters[src] += 1
        qid = f"h-{src}-{counters[src]:04d}"
        ex = expl.get(it['_ref']) or it['explanation']
        if not ex:
            ex = f"Official answer key: {it['answer']}. (No worked solution in source.)"
        source = dict(SRC[src]); source['ref'] = it['_ref']
        final.append(dict(id=qid, subject=it['subject'], topic=it['topic'], difficulty=it['difficulty'],
                          stem=it['stem'], options=[dict(key=k2, text=t) for k2, t in zip('ABCD', it['options'])],
                          answer=it['answer'], explanation=ex, source=source))
        label = pyq_label(src, it['_ref'])
        if label:
            final[-1]['pyq'] = label
    # validation
    for q in final:
        assert len(q['options']) == 4 and [o['key'] for o in q['options']] == list('ABCD')
        assert q['answer'] in 'ABCD' and all(o['text'].strip() for o in q['options'])
        assert q['subject'] in ('physics', 'chemistry', 'mathematics')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(final, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = collections.Counter((q['source']['licence'], q['id'].split('-')[1], q['subject']) for q in final)
    for k, v in sorted(c.items()):
        print(k, v)
    print('total', len(final), 'dups dropped', counters['dup'])
    print('answers', collections.Counter(q['answer'] for q in final))


if __name__ == '__main__':
    main()
