#!/usr/bin/env python3
"""Generate ORIGINAL figure-based Logical Reasoning questions (BITSAT non-verbal reasoning).

Every figure is drawn programmatically as SVG and every answer key is computed from the
same geometry that draws the options, so keys are correct by construction. Distractors are
classic traps (wrong rotation direction, mirror vs water image, a missed hole, off-by-one
counts) and are checked to be pairwise distinct from the key and from each other.

Run from anywhere:  python scripts/figures/generate_lr_figures.py
Requires: shapely (pip install shapely). Deterministic (fixed seed).
Outputs:  public/data/questions/reasoning-figures.json
          public/data/figures/lr/*.svg
"""
import itertools
import json
import math
import random
from pathlib import Path

from shapely import affinity
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / 'public' / 'data' / 'figures' / 'lr'
OUT = ROOT / 'public' / 'data' / 'questions' / 'reasoning-figures.json'

rng = random.Random(20261004)
SW = 2.5
GREY = '#9a9a9a'
SCALE_PX = 1.4  # width/height attributes = viewBox * this

# ---------------------------------------------------------------- answer keys
_keys = []
for _ in range(40):
    b = list('ABCD')
    rng.shuffle(b)
    _keys += b
_key_iter = iter(_keys)


def arrange(correct, distractors):
    """distractors: list of 3 (item, reason). Returns (answer_key, [(key, item, reason|None)])."""
    assert len(distractors) == 3
    ans = next(_key_iter)
    idx = 'ABCD'.index(ans)
    ds = distractors[:]
    rng.shuffle(ds)
    order = ds[:idx] + [(correct, None)] + ds[idx:]
    return ans, [(k, it, r) for k, (it, r) in zip('ABCD', order)]


def pick(correct, cands, same, n=3):
    """Pick first n candidates distinct from correct and from each other."""
    out = []
    for it, reason in cands:
        if same(it, correct) or any(same(it, o) for o, _ in out):
            continue
        out.append((it, reason))
        if len(out) == n:
            return out
    raise RuntimeError('not enough distinct distractors')


def traps(arr):
    return ' '.join(f'{k} is wrong: {r}.' for k, _, r in arr if r)


# ---------------------------------------------------------------- primitives
def circ(c, r, fill='black'):
    return {'k': 'circle', 'c': tuple(c), 'r': r, 'fill': fill}


def poly(pts, fill='white'):
    return {'k': 'poly', 'pts': [tuple(p) for p in pts], 'fill': fill}


def pline(pts, sw=SW, dash=False):
    return {'k': 'line', 'pts': [tuple(p) for p in pts], 'fill': 'none', 'sw': sw, 'dash': dash}


def tmap(fig, f, rs=1.0):
    out = []
    for p in fig:
        q = dict(p)
        if p['k'] == 'circle':
            q['c'] = f(p['c'])
            q['r'] = p['r'] * rs
        else:
            q['pts'] = [f(x) for x in p['pts']]
        out.append(q)
    return out


def Rf(deg, cx=50.0, cy=50.0):
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    return lambda p: (cx + (p[0] - cx) * c - (p[1] - cy) * s, cy + (p[0] - cx) * s + (p[1] - cy) * c)


def rot(fig, deg, cx=50.0, cy=50.0):  # positive = clockwise on screen (y down)
    return tmap(fig, Rf(deg, cx, cy))


def mirror(fig, cx=50.0):  # left-right flip (mirror held vertically)
    return tmap(fig, lambda p: (2 * cx - p[0], p[1]))


def water(fig, cy=50.0):  # top-bottom flip (water image)
    return tmap(fig, lambda p: (p[0], 2 * cy - p[1]))


def shift(fig, dx, dy):
    return tmap(fig, lambda p: (p[0] + dx, p[1] + dy))


def scl(fig, s, cx=0.0, cy=0.0):
    return tmap(fig, lambda p: (cx + (p[0] - cx) * s, cy + (p[1] - cy) * s), s)


def invert(fig):
    sw = {'black': 'white', 'white': 'black'}
    return [dict(p, fill=sw.get(p['fill'], p['fill'])) for p in fig]


def rn(v):
    r = round(v + 1e-7, 1)
    return 0.0 if r == 0 else r


def sig(fig):
    items = []
    for p in fig:
        if p['k'] == 'circle':
            items.append(('c', rn(p['c'][0]), rn(p['c'][1]), rn(p['r']), p['fill']))
        else:
            items.append((p['k'], p['fill'], tuple(sorted((rn(x), rn(y)) for x, y in p['pts']))))
    return tuple(sorted(items))


same_fig = lambda a, b: sig(a) == sig(b)


def fmt(v):
    s = f'{v:.2f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def render(fig, ox=0.0, oy=0.0, s=1.0):
    out = []
    for p in fig:
        sw = fmt(p.get('sw', SW))
        dash = ' stroke-dasharray="5 4"' if p.get('dash') else ''
        fill = GREY if p['fill'] == 'grey' else p['fill']
        if p['k'] == 'circle':
            x, y = p['c']
            out.append(f'<circle cx="{fmt(ox + x * s)}" cy="{fmt(oy + y * s)}" r="{fmt(p["r"] * s)}" '
                       f'fill="{fill}" stroke="black" stroke-width="{sw}"/>')
        else:
            pts = ' '.join(f'{fmt(ox + x * s)},{fmt(oy + y * s)}' for x, y in p['pts'])
            tag = 'polygon' if p['k'] == 'poly' else 'polyline'
            out.append(f'<{tag} points="{pts}" fill="{fill}" stroke="black" stroke-width="{sw}" '
                       f'stroke-linejoin="round" stroke-linecap="round"{dash}/>')
    return ''.join(out)


def doc(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" '
            f'width="{fmt(w * SCALE_PX)}" height="{fmt(h * SCALE_PX)}">'
            f'<rect width="{fmt(w)}" height="{fmt(h)}" fill="white"/>{body}</svg>')


def frame(ox, oy, w=100, h=100, dash=False):
    d = ' stroke-dasharray="4 3"' if dash else ''
    return (f'<rect x="{fmt(ox)}" y="{fmt(oy)}" width="{fmt(w)}" height="{fmt(h)}" fill="white" '
            f'stroke="#888" stroke-width="1.2"{d}/>')


def qmark(ox, oy, w=100, h=100):
    return (frame(ox, oy, w, h) + f'<text x="{fmt(ox + w / 2)}" y="{fmt(oy + h / 2 + 15)}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="44" font-weight="bold" '
            f'text-anchor="middle" fill="black">?</text>')


def strip(items, gap=12):
    """Row of 100x100 cells. items: fig | '?' | ':' | '::'."""
    x = 0.0
    body = []
    for it in items:
        if isinstance(it, str) and it in (':', '::'):
            n = 1 if it == ':' else 2
            w = 14 * n
            for j in range(n):
                cx = x + 7 + 14 * j
                body.append(f'<circle cx="{fmt(cx)}" cy="40" r="3.5" fill="black"/>'
                            f'<circle cx="{fmt(cx)}" cy="60" r="3.5" fill="black"/>')
            x += w + gap
        elif isinstance(it, str) and it == '?':
            body.append(qmark(x, 0))
            x += 100 + gap
        else:
            body.append(frame(x, 0) + render(it, x, 0))
            x += 100 + gap
    return doc(x - gap, 100, ''.join(body))


def fig_svg(fig, framed=True):
    return doc(100, 100, (frame(0, 0) if framed else '') + render(fig))


def save(name, content):
    (FIG_DIR / name).write_text(content, encoding='utf-8')
    return f'figures/lr/{name}'


QS = []


def nid():
    return f'lr-fig-{len(QS) + 1:04d}'


def add_q(qid, topic, diff, stem, ans, options, expl, stem_img=None, expl_img=None):
    q = {'id': qid, 'subject': 'reasoning', 'topic': topic, 'difficulty': diff, 'stem': stem}
    if stem_img:
        q['stemImage'] = stem_img
    q['options'] = options
    q['answer'] = ans
    q['explanation'] = expl
    if expl_img:
        q['explanationImage'] = expl_img
    q['source'] = {'kind': 'authored'}
    QS.append(q)


def fig_opts(qid, arr, renderer=fig_svg):
    return [{'key': k, 'text': '', 'image': save(f'{qid}-{k.lower()}.svg', renderer(it))} for k, it, _ in arr]


def text_opts(arr):
    return [{'key': k, 'text': str(it)} for k, it, _ in arr]


# ---------------------------------------------------------------- motifs
def _ang_pos(r, a):
    return (50 + r * math.sin(math.radians(a)), 50 - r * math.cos(math.radians(a)))


POS = [(0, 0)] + [(r, a) for r in (19, 32) for a in range(0, 360, 45)]


def element(kind, r, a, orient):
    x, y = (50.0, 50.0) if r == 0 else _ang_pos(r, a)
    if kind == 'dot':
        return [circ((x, y), 7.5, 'black')]
    if kind == 'ring':
        return [circ((x, y), 8.5, 'white')]
    if kind in ('tri', 'wtri'):
        base = [(0, -11), (-9.5, 7.5), (9.5, 7.5)]
        f = Rf(orient, 0, 0)
        return [poly([(x + q[0], y + q[1]) for q in map(f, base)], 'black' if kind == 'tri' else 'white')]
    if kind == 'sq':
        base = [(-8, -8), (8, -8), (8, 8), (-8, 8)]
        f = Rf(orient, 0, 0)
        return [poly([(x + q[0], y + q[1]) for q in map(f, base)], 'grey')]
    if kind == 'hand':
        return [pline([(50, 50), (x, y)])]
    raise ValueError(kind)


def motif(n=3, rot45=False, need_bw=False):
    angles = list(range(0, 360, 45)) if rot45 else [0, 90, 180, 270]
    while True:
        kinds = rng.sample(['dot', 'ring', 'tri', 'wtri', 'sq', 'hand', 'tri'], n)
        if kinds.count('hand') > 1:
            continue
        spots = rng.sample(POS, n)
        if 'hand' in kinds:
            hi = kinds.index('hand')
            if spots[hi][0] != 32 or any(s[0] == 0 for s in spots):
                continue
            if any(s[1] == spots[hi][1] for j, s in enumerate(spots) if j != hi):
                continue
        # keep elements apart
        pts = [(50, 50) if s[0] == 0 else _ang_pos(*s) for s in spots]
        if any(math.dist(p, q) < 21 for p, q in itertools.combinations(pts, 2)):
            continue
        m = []
        for k, (r, a) in zip(kinds, spots):
            m += element(k, r, a, rng.choice(range(0, 360, 90 if not rot45 else 45)))
        sigs = {sig(rot(m, t)) for t in angles} | {sig(rot(mirror(m), t)) for t in angles}
        if len(sigs) != 2 * len(angles):
            continue
        if need_bw and sig(invert(m)) == sig(m):
            continue
        return m


def turn_desc(deg):
    d = deg % 360
    if d == 0:
        return 'no turn'
    if d == 180:
        return '180°'
    return f'{d}° clockwise' if d < 180 else f'{360 - d}° anticlockwise'


# ================================================================ 1. FIGURE SERIES
def gen_series_rotation(theta, diff):
    qid = nid()
    m = motif(3, rot45=(theta % 90 != 0))
    frames = [rot(m, theta * i) for i in range(4)]
    correct = rot(m, 4 * theta)
    step = turn_desc(theta)
    cands = [
        (rot(m, 2 * theta), f'it turns the last figure back the other way ({turn_desc(-theta)}) — wrong direction'),
        (mirror(correct), 'it is the mirror image of the correct figure, not a rotation'),
        (rot(m, 5 * theta), 'it turns two steps instead of one'),
        (rot(m, 3 * theta), 'it simply repeats the last figure'),
    ]
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', strip(frames + ['?']))
    expl = (f'Each figure is the previous one rotated {step} as a whole (watch any one element, '
            f'e.g. the black piece). Rotating the fourth figure once more gives option {ans}. ' + traps(arr))
    add_q(qid, 'Figure Series', diff, 'Which figure comes next in the series?', ans, fig_opts(qid, arr), expl, stem_img)


DOT_LAYOUT = {
    1: [(50, 50)], 2: [(36, 36), (64, 64)], 3: [(36, 36), (50, 50), (64, 64)],
    4: [(36, 36), (64, 36), (36, 64), (64, 64)], 5: [(36, 36), (64, 36), (36, 64), (64, 64), (50, 50)],
    6: [(36, 34), (64, 34), (36, 50), (64, 50), (36, 66), (64, 66)],
    7: [(36, 34), (64, 34), (36, 50), (64, 50), (36, 66), (64, 66), (50, 50)],
    8: [(36, 34), (50, 34), (64, 34), (36, 50), (64, 50), (36, 66), (50, 66), (64, 66)],
    9: [(x, y) for y in (34, 50, 66) for x in (36, 50, 64)],
}
CORNER_NAMES = ['top-left', 'top-right', 'bottom-right', 'bottom-left']


def corner_tri(k):
    return rot([poly([(12, 12), (30, 12), (12, 30)], 'black')], 90 * k)


def outer_sq():
    return [poly([(12, 12), (88, 12), (88, 88), (12, 88)], 'white')]


def reg_poly(k, r=20, fill='white'):
    return poly([_ang_pos(r, 360 * i / k) for i in range(k)], fill)


def gen_series_count(variant, diff):
    qid = nid()
    c0 = rng.randrange(4)
    st = rng.choice([1, -1]) if variant != 'dots2' else rng.choice([1, -1])
    if variant == 'poly':
        n0 = 3

        def fr(n, c):
            return outer_sq() + corner_tri(c % 4) + [reg_poly(n)]
        what, unit = 'the inner polygon gains one side', 'sides'
    else:
        n0 = rng.choice([1, 2]) if variant == 'dots' else rng.choice([2, 3])
        dstep = 1 if variant == 'dots' else 1

        def fr(n, c):
            return outer_sq() + corner_tri(c % 4) + [circ(p, 4.5, 'black') for p in DOT_LAYOUT[n]]
        what, unit = 'one dot is added', 'dots'
    frames = [fr(n0 + i, c0 + st * i) for i in range(4)]
    n4, c4 = n0 + 4, (c0 + 4 * st) % 4
    correct = fr(n4, c4)
    dirw = 'clockwise' if st == 1 else 'anticlockwise'
    cands = [
        (fr(n4 - 1, c4), f'it has {n4 - 1} {unit} — one addition is missed'),
        (fr(n4, c0 + 3 * st - st), f'the black corner moves {"anticlockwise" if st == 1 else "clockwise"} (wrong direction)'),
        (fr(n4 + 1, c4), f'it has {n4 + 1} {unit} — one too many'),
        (fr(n4, c0 + 3 * st), 'the black corner has not moved'),
    ]
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', strip(frames + ['?']))
    expl = (f'Two changes happen at every step: {what}, and the black corner triangle moves one corner {dirw}. '
            f'So the fifth figure has {n4} {unit} with the black triangle at the {CORNER_NAMES[c4]} corner: option {ans}. '
            + traps(arr))
    add_q(qid, 'Figure Series', diff, 'Which figure comes next in the series?', ans, fig_opts(qid, arr), expl, stem_img)


BORDER = [(24, 24), (50, 24), (76, 24), (76, 50), (76, 76), (50, 76), (24, 76), (24, 50)]  # clockwise


def piece(kind, pos):
    x, y = BORDER[pos % 8]
    if kind == 'dot':
        return [circ((x, y), 8, 'black')]
    if kind == 'box':
        return [poly([(x - 8, y - 8), (x + 8, y - 8), (x + 8, y + 8), (x - 8, y + 8)], 'white')]
    if kind == 'tri':
        return [poly([(x, y - 9), (x - 8.5, y + 7), (x + 8.5, y + 7)], 'grey')]


def step_desc(s):
    s8 = s % 8
    if s8 == 0:
        return 'stays put'
    if s8 <= 4:
        return f'moves {s8} step{"s" if s8 > 1 else ""} clockwise'
    return f'moves {8 - s8} step{"s" if 8 - s8 > 1 else ""} anticlockwise'


def gen_series_move(n_el, diff):
    qid = nid()
    kinds = ['dot', 'box', 'tri'][:n_el]
    while True:
        starts = rng.sample(range(8), n_el)
        steps = [1, -2, 3][:n_el] if n_el > 1 else [rng.choice([1, -1])]
        if diff == 'hard':
            steps = [rng.choice([1, -1]), rng.choice([2, -3])]
        ok = all(len({(s + t * i) % 8 for s, t in zip(starts, steps)}) == n_el for i in range(6))
        if ok:
            break

    def fr(positions):
        f = [poly([(10, 10), (90, 10), (90, 90), (10, 90)], 'white')]
        for k, p in zip(kinds, positions):
            f += piece(k, p)
        return f

    def at(i, override=None):
        pos = [(s + t * i) % 8 for s, t in zip(starts, steps)]
        if override:
            j, p = override
            pos[j] = p % 8
        return pos

    frames = [fr(at(i)) for i in range(4)]
    cpos = at(4)
    correct = fr(cpos)
    names = {'dot': 'black circle', 'box': 'white square', 'tri': 'grey triangle'}
    cands = []
    for j, k in enumerate(kinds):
        s, t = starts[j], steps[j]
        cands.append((at(4, (j, s + 3 * t - t)), f'the {names[k]} moves the wrong way'))
        cands.append((at(4, (j, s + 3 * t)), f'the {names[k]} has not moved'))
        cands.append((at(4, (j, s + 4 * t + (1 if t > 0 else -1))), f'the {names[k]} moves one step too far'))
    cands = [(fr(p), r) for p, r in cands if len(set(p)) == n_el]
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', strip(frames + ['?']))
    rules = '; '.join(f'the {names[k]} {step_desc(t)}' for k, t in zip(kinds, steps))
    expl = (f'Positions go round the border in 8 steps (corners and side-midpoints). Each time, {rules}. '
            f'Applying this once more gives option {ans}. ' + traps(arr))
    add_q(qid, 'Figure Series', diff, 'The elements move round the square in a fixed way. Which figure comes next?',
          ans, fig_opts(qid, arr), expl, stem_img)


# ================================================================ 2. FIGURE ANALOGY
TRANSFORMS = {
    'r90': (lambda f: rot(f, 90), 'rotated 90° clockwise'),
    'r-90': (lambda f: rot(f, -90), 'rotated 90° anticlockwise'),
    'r180': (lambda f: rot(f, 180), 'rotated 180°'),
    'r45': (lambda f: rot(f, 45), 'rotated 45° clockwise'),
    'r-45': (lambda f: rot(f, -45), 'rotated 45° anticlockwise'),
    'mir': (mirror, 'flipped left-right (mirror image)'),
    'wat': (water, 'flipped top-bottom (water image)'),
    'inv': (invert, 'colour-swapped (black ↔ white)'),
    'id': (lambda f: f, 'left unchanged'),
}


def comp(*names):
    def f(x):
        for n in names:
            x = TRANSFORMS[n][0](x)
        return x
    return f


ANALOGY_PLANS = [
    (('r90',), [('r-90',), ('mir',), ('r180',), ('id',)], 'easy'),
    (('mir',), [('wat',), ('r180',), ('r90',), ('id',)], 'easy'),
    (('inv',), [('id',), ('r180', 'inv'), ('mir', 'inv'), ('mir',)], 'easy'),
    (('wat',), [('mir',), ('r180',), ('r-90',), ('id',)], 'medium'),
    (('r180',), [('mir',), ('wat',), ('r90',), ('id',)], 'medium'),
    (('r-45',), [('r45',), ('r-90',), ('mir', 'r45'), ('id',)], 'medium'),
    (('r-90', 'inv'), [('r-90',), ('inv',), ('r90', 'inv'), ('mir', 'inv')], 'hard'),
    (('mir', 'inv'), [('mir',), ('wat', 'inv'), ('inv',), ('r180', 'inv')], 'hard'),
]


def tdesc(names):
    return ' and then '.join(TRANSFORMS[n][1] for n in names)


def gen_analogy(plan):
    tr, dist, diff = plan
    qid = nid()
    r45 = any('45' in n for n in tr + tuple(x for d in dist for x in d))
    bw = 'inv' in tr
    A = motif(3, rot45=r45, need_bw=bw)
    C = motif(3, rot45=r45, need_bw=bw)
    while same_fig(A, C):
        C = motif(3, rot45=r45, need_bw=bw)
    B = comp(*tr)(A)
    correct = comp(*tr)(C)
    cands = [(comp(*d)(C), f'it is the third figure {tdesc(d)}, not {tdesc(tr)}') for d in dist]
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', strip([A, ':', B, '::', C, ':', '?']))
    expl = (f'The second figure is the first figure {tdesc(tr)}. Doing the same to the third figure gives option {ans}. '
            + traps(arr))
    add_q(qid, 'Figure Analogy', diff,
          'The first two figures are related in a certain way. Choose the figure that is related to the third figure in the same way.',
          ans, fig_opts(qid, arr), expl, stem_img)


# ================================================================ 3. ODD ONE OUT
def gen_odd_mirror(diff, r45=False):
    qid = nid()
    m = motif(3, rot45=r45)
    pool = list(range(0, 360, 45)) if r45 else [0, 90, 180, 270]
    angs = rng.sample(pool, 4)
    odd = rot(mirror(m), angs[3])
    others = [(rot(m, a), 'it can be turned to match the other two of its kind (it is just a rotation)') for a in angs[:3]]
    ans, arr = arrange(odd, others)
    expl = (f'Three figures are the same figure turned through different angles. Option {ans} cannot be obtained by any '
            f'rotation — it is a mirror image (the elements appear in the reverse order going round). '
            f'Rotate any of the others: they all coincide, so they are not odd.')
    add_q(qid, 'Figure Classification', diff,
          'Three of the following four figures are alike in a certain way and one is different. Choose the odd one out.',
          ans, fig_opts(qid, arr), expl)


def dots_in(n, r=11):
    if n == 1:
        return [circ((50, 50), 3.5, 'black')]
    return [circ(_ang_pos(r, 360 * i / n + 20), 3.5, 'black') for i in range(n)]


def gen_odd_count(diff):
    qid = nid()
    sides = rng.sample([3, 4, 5, 6], 4)
    figs = []
    for k in sides[:3]:
        f = [reg_poly(k, 34)] + dots_in(k)
        figs.append((rot(f, rng.choice([0, 90, 180, 270])), f'its {k} sides match its {k} dots'))
    ko = sides[3]
    nd = ko + rng.choice([-1, 1])
    odd = rot([reg_poly(ko, 34)] + dots_in(nd), rng.choice([0, 90, 180]))
    ans, arr = arrange(odd, figs)
    expl = (f'In three figures the number of dots inside equals the number of sides of the polygon. Option {ans} has '
            f'{ko} sides but {nd} dots, so it is the odd one. ' + traps(arr))
    add_q(qid, 'Figure Classification', diff,
          'Three of the following four figures are alike in a certain way and one is different. Choose the odd one out.',
          ans, fig_opts(qid, arr), expl)


# ================================================================ 4. FIGURE MATRIX
def shape_at(shape, cx, cy, r, fill):
    if shape == 'circle':
        return circ((cx, cy), r, fill)
    k, off = {'square': (4, 45), 'triangle': (3, 0), 'diamond': (4, 0), 'hexagon': (6, 30), 'pentagon': (5, 0)}[shape]
    rr = r * (1.25 if shape in ('square', 'triangle') else 1.12)
    return poly([(cx + rr * math.sin(math.radians(off + 360 * i / k)), cy + 2 - rr * math.cos(math.radians(off + 360 * i / k)))
                 for i in range(k)], fill)


def cell_fig(shape, count, fill):
    xs = [50 + 28 * (i - (count - 1) / 2) for i in range(count)]
    return [shape_at(shape, x, 50, 10, fill) for x in xs]


def gen_matrix(diff, attrs3):
    qid = nid()
    shapes = rng.sample(['circle', 'square', 'triangle', 'diamond', 'hexagon'], 3)
    fills = ['white', 'grey', 'black']
    rng.shuffle(fills)
    abs_ = [(1, 1), (1, 2), (2, 2), (2, 1)]
    a_s, a_c, a_f = rng.sample(abs_, 3)
    o = [rng.randrange(3) for _ in range(3)]
    val = lambda ab, off, r, c: (ab[0] * r + ab[1] * c + off) % 3
    grid = {}
    for r in range(3):
        for c in range(3):
            grid[r, c] = (shapes[val(a_s, o[0], r, c)], val(a_c, o[1], r, c) + 1,
                          fills[val(a_f, o[2], r, c)] if attrs3 else 'white')
    miss = (2, 2) if diff != 'hard' else rng.choice([(1, 1), (0, 2), (2, 0), (1, 2), (2, 1)])
    s, n, f = grid[miss]
    correct = cell_fig(s, n, f)
    other_n = [x for x in (1, 2, 3) if x != n]
    other_s = [x for x in shapes if x != s]
    cands = [(cell_fig(s, other_n[0], f), f'it has {other_n[0]} shape(s), but the count rule needs {n}'),
             (cell_fig(other_s[0], n, f), f'it uses {other_s[0]}s; that shape already appears in this row/column')]
    if attrs3:
        of = [x for x in fills if x != f]
        cands.append((cell_fig(s, n, of[0]), f'its shading is {of[0]}, which is already used in this row/column'))
    cands.append((cell_fig(s, other_n[1], f), f'it has {other_n[1]} shape(s) instead of {n}'))
    cands.append((cell_fig(other_s[1], n, f), f'it uses {other_s[1]}s instead of {s}s'))
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    body = []
    for r in range(3):
        for c in range(3):
            if (r, c) == miss:
                body.append(qmark(c * 100, r * 100))
            else:
                body.append(frame(c * 100, r * 100) + render(cell_fig(*grid[r, c]), c * 100, r * 100))
    stem_img = save(f'{qid}-q.svg', doc(300, 300, ''.join(body)))
    feat = 'shape, number of shapes' + (' and shading' if attrs3 else '')
    expl = (f'Every row and every column contains each {feat} exactly once (e.g. one, two and three shapes). '
            f'The missing cell must therefore hold {n} {s}{"s" if n > 1 else ""}'
            + (f', {f}' if attrs3 else '') + f': option {ans}. ' + traps(arr))
    add_q(qid, 'Figure Matrix', diff, 'Which figure fits in the empty cell of the matrix?', ans, fig_opts(qid, arr),
          expl, stem_img)


# ================================================================ 5. MIRROR / WATER IMAGES
def gen_mirror_fig(kind, diff):
    qid = nid()
    m = motif(4 if diff != 'easy' else 3)
    if kind == 'mirror':
        correct = mirror(m)
        body = frame(0, 0) + render(m) + render([pline([(112, -2), (112, 102)], sw=2, dash=True)])
        stem_img = save(f'{qid}-q.svg', doc(122, 100, body))
        cands = [(water(m), 'it is the water image (top-bottom flip), not the mirror image'),
                 (rot(m, 180), 'it is the figure turned 180° — a rotation, not a reflection'),
                 (rot(m, 90), 'it is merely a 90° rotation'),
                 (m, 'it is the original figure unchanged')]
        stem = 'Choose the correct mirror image of the given figure when the mirror is held along the dashed line on its right.'
        rule = 'In a mirror held vertically, left and right are exchanged while top and bottom stay the same'
    else:
        correct = water(m)
        body = frame(0, 0) + render(m) + render([pline([(-2, 112), (102, 112)], sw=2, dash=True)])
        stem_img = save(f'{qid}-q.svg', doc(100, 120, body))
        cands = [(mirror(m), 'it is the mirror image (left-right flip), not the water image'),
                 (rot(m, 180), 'it is the figure turned 180° — that flips both ways'),
                 (rot(m, -90), 'it is merely a 90° rotation'),
                 (m, 'it is the original figure unchanged')]
        stem = 'Choose the correct water image of the given figure (water surface along the dashed line below it).'
        rule = 'In a water image, top and bottom are exchanged while left and right stay the same'
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    expl = f'{rule}: each element keeps its distance from the line but moves to the other side. That gives option {ans}. ' + traps(arr)
    add_q(qid, 'Mirror and Water Images', diff, stem, ans, fig_opts(qid, arr), expl, stem_img)


def text_svg(s, mode, w=180, h=100):
    t = (f'<text x="{w / 2}" y="{h / 2 + 15}" font-family="Arial, Helvetica, sans-serif" font-size="44" '
         f'font-weight="bold" text-anchor="middle" fill="black">{s}</text>')
    tr = {'orig': '', 'mir': f'translate({w},0) scale(-1,1)', 'wat': f'translate(0,{h}) scale(1,-1)',
          'rot': f'translate({w},{h}) scale(-1,-1)'}[mode]
    g = f'<g transform="{tr}">{t}</g>' if tr else t
    return doc(w, h, frame(0, 0, w, h) + g)


def gen_mirror_text(s, kind, diff):
    qid = nid()
    rev = s[::-1]
    want = 'mir' if kind == 'mirror' else 'wat'
    other = 'wat' if kind == 'mirror' else 'mir'
    items = {'mir': ('mir', s), 'wat': ('wat', s), 'rot': ('rot', s), 'revtext': ('orig', rev), 'orig': ('orig', s)}
    correct = items[want]
    cands = [(items[other], f'it is the {"water" if kind == "mirror" else "mirror"} image instead'),
             (items['revtext'], 'only the order of the characters is reversed; each character must also be flipped'),
             (items['rot'], 'it is the string turned upside-down (180° rotation), which flips both ways')]
    if kind == 'water':
        cands[1] = (items['revtext'], 'reversing the order of characters belongs to a mirror image, and even then each character must be flipped')
    ans, arr = arrange(correct, cands)
    if kind == 'mirror':
        body = frame(0, 0, 180, 100) + (f'<text x="90" y="65" font-family="Arial, Helvetica, sans-serif" font-size="44" '
                                        f'font-weight="bold" text-anchor="middle" fill="black">{s}</text>')
        body += render([pline([(194, -2), (194, 102)], sw=2, dash=True)])
        stem_img = save(f'{qid}-q.svg', doc(200, 100, body))
        stem = f'Choose the mirror image of the given character group when the mirror is held along the dashed line on its right.'
        rule = ('A vertical mirror reverses left and right: the character order is reversed AND every character is '
                'flipped left-right, while nothing turns upside-down.')
    else:
        body = frame(0, 0, 180, 100) + (f'<text x="90" y="65" font-family="Arial, Helvetica, sans-serif" font-size="44" '
                                        f'font-weight="bold" text-anchor="middle" fill="black">{s}</text>')
        body += render([pline([(-2, 114), (182, 114)], sw=2, dash=True)])
        stem_img = save(f'{qid}-q.svg', doc(180, 120, body))
        stem = 'Choose the water image of the given character group (water surface along the dashed line below it).'
        rule = ('A water image reverses top and bottom only: the characters stay in the same order and each one is '
                'flipped upside-down (not rotated).')
    opts = [{'key': k, 'text': '', 'image': save(f'{qid}-{k.lower()}.svg', text_svg(t, md))} for k, (md, t), _ in arr]
    add_q(qid, 'Mirror and Water Images', diff, stem, ans, opts, f'{rule} That is option {ans}. ' + traps(arr), stem_img)


# ================================================================ 6/7. PAPER FOLDING & CUTTING
S2 = 1 / math.sqrt(2)
FOLD_DESC = {'R2L': 'right half folded over onto the left', 'L2R': 'left half folded over onto the right',
             'T2B': 'top half folded down onto the bottom', 'B2T': 'bottom half folded up onto the top',
             'DTR': 'top-right triangle folded onto the bottom-left along a diagonal',
             'DBL': 'bottom-left triangle folded onto the top-right along a diagonal',
             'ATL': 'top-left triangle folded onto the bottom-right along a diagonal',
             'ABR': 'bottom-right triangle folded onto the top-left along a diagonal'}
ALT = {'R2L': 'T2B', 'L2R': 'B2T', 'T2B': 'R2L', 'B2T': 'L2R', 'DTR': 'ATL', 'DBL': 'ABR', 'ATL': 'DTR', 'ABR': 'DBL'}
LINE_NAME = {'R2L': 'vertical centre line', 'L2R': 'vertical centre line', 'T2B': 'horizontal centre line', 'B2T': 'horizontal centre line',
             'DTR': 'top-left-to-bottom-right diagonal', 'DBL': 'top-left-to-bottom-right diagonal',
             'ATL': 'bottom-left-to-top-right diagonal', 'ABR': 'bottom-left-to-top-right diagonal'}


def make_fold(kind, region):
    x0, y0, x1, y1 = region.bounds
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    t = {'R2L': ((mx, y0), (0, 1), 1), 'L2R': ((mx, y0), (0, 1), -1),
         'T2B': ((x0, my), (1, 0), 1), 'B2T': ((x0, my), (1, 0), -1),
         'DTR': ((x0, y0), (S2, S2), 1), 'DBL': ((x0, y0), (S2, S2), -1),
         'ATL': ((x0, y1), (S2, -S2), 1), 'ABR': ((x0, y1), (S2, -S2), -1)}
    p, d, k = t[kind]
    return {'kind': kind, 'p': p, 'd': d, 'keep': k}


def halfplane(f, keep=True):
    (px, py), (dx, dy) = f['p'], f['d']
    nx, ny = -dy, dx
    sg = f['keep'] if keep else -f['keep']
    L = 10
    return Polygon([(px - dx * L, py - dy * L), (px + dx * L, py + dy * L),
                    (px + dx * L + sg * nx * L, py + dy * L + sg * ny * L),
                    (px - dx * L + sg * nx * L, py - dy * L + sg * ny * L)])


def reflect_pt(q, f):
    (px, py), (dx, dy) = f['p'], f['d']
    t = (q[0] - px) * dx + (q[1] - py) * dy
    fx, fy = px + t * dx, py + t * dy
    return (2 * fx - q[0], 2 * fy - q[1])


def reflect_geom(g, f):
    (px, py), (dx, dy) = f['p'], f['d']
    a, b, d, e = dx * dx - dy * dy, 2 * dx * dy, 2 * dx * dy, dy * dy - dx * dx
    return affinity.affine_transform(g, [a, b, d, e, px - (a * px + b * py), py - (d * px + e * py)])


def run_folds(kinds):
    region = box(0, 0, 1, 1)
    regions, folds = [region], []
    for k in kinds:
        f = make_fold(k, region)
        keep = region.intersection(halfplane(f, True))
        move = region.intersection(halfplane(f, False))
        assert reflect_geom(move, f).symmetric_difference(keep).area < 1e-9, 'fold halves not congruent'
        folds.append(f)
        region = keep
        regions.append(region)
    return folds, regions


def unfold_pts(pts, lines):
    cur = list(pts)
    for f in reversed(lines):
        cur = cur + [reflect_pt(q, f) for q in cur]
    out = {}
    for q in cur:
        out[(round(q[0], 4), round(q[1], 4))] = q
    return tuple(sorted(out))


def unfold_geom(g, lines):
    cur = g
    for f in reversed(lines):
        cur = unary_union([cur, reflect_geom(cur, f)])
    return cur


def P(ox, x, y):
    return (ox + 10 + 80 * x, 10 + 80 * y)


def poly_path(g, ox=0.0):
    geoms = [g] if g.geom_type == 'Polygon' else list(getattr(g, 'geoms', []))
    d = []
    for pg in geoms:
        if pg.geom_type != 'Polygon' or pg.is_empty:
            continue
        for ring in [pg.exterior] + list(pg.interiors):
            cs = list(ring.coords)[:-1]
            d.append('M' + ' L'.join(f'{fmt(P(ox, x, y)[0])} {fmt(P(ox, x, y)[1])}' for x, y in cs) + ' Z')
    return ' '.join(d)


def geom_svg(g, ox=0.0, fill='white', stroke=SW, dash=False):
    ds = ' stroke-dasharray="5 4"' if dash else ''
    fl = GREY if fill == 'grey' else fill
    return (f'<path d="{poly_path(g, ox)}" fill="{fl}" fill-rule="evenodd" stroke="black" '
            f'stroke-width="{stroke}" stroke-linejoin="round"{ds}/>')


def line_in(f, region):
    (px, py), (dx, dy) = f['p'], f['d']
    seg = LineString([(px - dx * 5, py - dy * 5), (px + dx * 5, py + dy * 5)]).intersection(region)
    if seg.is_empty:
        return []
    if seg.geom_type == 'LineString':
        return [list(seg.coords)]
    return [list(s.coords) for s in seg.geoms if s.geom_type == 'LineString']


def arrow(a, b, ox):
    (x1, y1), (x2, y2) = P(ox, *a), P(ox, *b)
    ang = math.atan2(y2 - y1, x2 - x1)
    h1 = (x2 - 7 * math.cos(ang - 0.45), y2 - 7 * math.sin(ang - 0.45))
    h2 = (x2 - 7 * math.cos(ang + 0.45), y2 - 7 * math.sin(ang + 0.45))
    return (f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="black" stroke-width="1.6"/>'
            f'<polygon points="{fmt(x2)},{fmt(y2)} {fmt(h1[0])},{fmt(h1[1])} {fmt(h2[0])},{fmt(h2[1])}" fill="black"/>')


def fold_panels(folds, regions, final_body, final_region=None):
    """final_body(ox) -> svg for last panel contents (drawn on top of final region)."""
    body = []
    ox = 0.0
    for f, reg in zip(folds, regions):
        body.append(frame(ox, 0) + geom_svg(reg, ox))
        for seg in line_in(f, reg):
            (x1, y1), (x2, y2) = P(ox, *seg[0]), P(ox, *seg[-1])
            body.append(f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="black" '
                        f'stroke-width="2.2" stroke-dasharray="6 4"/>')
        move = reg.intersection(halfplane(f, False))
        cm = move.centroid.coords[0]
        tm = reflect_pt(cm, f)
        a = (cm[0] + (tm[0] - cm[0]) * 0.15, cm[1] + (tm[1] - cm[1]) * 0.15)
        b = (cm[0] + (tm[0] - cm[0]) * 0.8, cm[1] + (tm[1] - cm[1]) * 0.8)
        body.append(arrow(a, b, ox))
        ox += 116
    body.append(frame(ox, 0) + geom_svg(final_region if final_region is not None else regions[-1], ox) + final_body(ox))
    return doc(ox + 100, 100, ''.join(body))


HR = 0.05


def holes_svg(holes, ox=0.0, fill='black'):
    return ''.join(f'<circle cx="{fmt(P(ox, x, y)[0])}" cy="{fmt(P(ox, x, y)[1])}" r="{fmt(HR * 80)}" fill="{fill}" '
                   f'stroke="black" stroke-width="1.5"/>' for x, y in holes)


def creases(folds, regions):
    segs = []
    for j, f in enumerate(folds):
        cur = line_in(f, regions[j])
        for g in reversed(folds[:j]):
            cur = cur + [[reflect_pt(q, g) for q in s] for s in cur]
        segs += cur
    return segs


def crease_svg(segs, ox=0.0):
    out = []
    for s in segs:
        (x1, y1), (x2, y2) = P(ox, *s[0]), P(ox, *s[-1])
        out.append(f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="#777" '
                   f'stroke-width="1.4" stroke-dasharray="4 3"/>')
    return ''.join(out)


def sheet_holes_svg(holes):
    return doc(100, 100, frame(0, 0) + geom_svg(box(0, 0, 1, 1)) + holes_svg(holes))


def fold_distractor_lines(folds, regions):
    cands = []
    n = len(folds)
    for j in range(n):
        alt = make_fold(ALT[folds[j]['kind']], regions[j])
        cands.append((folds[:j] + [alt] + folds[j + 1:],
                      f'fold {j + 1} is along the {LINE_NAME[folds[j]["kind"]]}, but this unfolds it about the '
                      f'{LINE_NAME[alt["kind"]]}'))
    for j in reversed(range(n)):
        cands.append((folds[:j] + folds[j + 1:], f'it forgets to unfold fold {j + 1}, so half the holes are missing'))
    return cands


def gen_punch(kinds, n_punch, diff):
    qid = nid()
    folds, regions = run_folds(kinds)
    final = regions[-1]
    grid = [(i / 16, j / 16) for i in range(1, 16) for j in range(1, 16)]
    inner = final.buffer(-0.085)
    alts = [make_fold(ALT[f['kind']], regions[j]) for j, f in enumerate(folds)]
    lines = [LineString([(f['p'][0] - f['d'][0] * 5, f['p'][1] - f['d'][1] * 5),
                         (f['p'][0] + f['d'][0] * 5, f['p'][1] + f['d'][1] * 5)]) for f in folds + alts]
    cand_pts = [g for g in grid if inner.contains(Point(g)) and all(l.distance(Point(g)) > 0.085 for l in lines)]
    for _ in range(500):
        punches = rng.sample(cand_pts, n_punch)
        holes = unfold_pts(punches, folds)
        if all(math.dist(a, b) > 0.15 for a, b in itertools.combinations(holes, 2)):
            break
    else:
        raise RuntimeError('no punch')
    correct = holes
    cands = []
    for ls, why in fold_distractor_lines(folds, regions):
        h = unfold_pts(punches, ls)
        if all(0.06 < x < 0.94 and 0.06 < y < 0.94 for x, y in h):
            cands.append((h, why))
    rot90 = tuple(sorted((round(1 - y, 4), round(x, 4)) for x, y in correct))
    cands.append((rot90, 'right number of holes, but not where the reflections put them'))
    cands.append((tuple(sorted((round(x, 4), round(y, 4)) for x, y in punches)), 'it shows only the punched layer, ignoring the unfolding'))
    cands.append((tuple(sorted((round(x, 4), round(1 - y, 4)) for x, y in correct)), 'the holes are reflected to the wrong side'))
    ds = pick(correct, cands, lambda a, b: a == b)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', fold_panels(folds, regions, lambda ox: holes_svg(punches, ox)))
    x_img = save(f'{qid}-x.svg', doc(100, 100, frame(0, 0) + geom_svg(box(0, 0, 1, 1)) + crease_svg(creases(folds, regions))
                                     + holes_svg(correct) + holes_svg(punches, fill=GREY)))
    steps = '; '.join(f'fold {i + 1}: {FOLD_DESC[k]}' for i, k in enumerate(kinds))
    expl = (f'Unfold in reverse order, reflecting every hole across each crease ({steps}). Each fold doubles the holes: '
            f'{n_punch} punch{"es" if n_punch > 1 else ""} × {2 ** len(kinds)} layers = {len(correct)} holes, placed symmetrically about the creases '
            f'(grey = punched position in the figure). Option {ans}. ' + traps(arr))
    add_q(qid, 'Paper Folding', diff,
          'A square sheet of paper is folded as shown (dashed line = fold, arrow = direction) and then punched where '
          'the black circle(s) appear in the last figure. How will the sheet look when unfolded?',
          ans, fig_opts(qid, arr, sheet_holes_svg), expl, stem_img, x_img)


def clean(g):
    return g.buffer(-1e-4, join_style=2).buffer(1e-4, join_style=2)


def diamond(c, r):
    x, y = c
    return Polygon([(x, y - r), (x + r, y), (x, y + r), (x - r, y)])


def gen_cut(kinds, cut_kinds, diff):
    for _ in range(60):
        try:
            return _gen_cut(kinds, cut_kinds, diff)
        except RuntimeError:
            pass
    raise RuntimeError('cut failed')


def _gen_cut(kinds, cut_kinds, diff):
    qid = nid()
    folds, regions = run_folds(kinds)
    final = regions[-1]
    sheet = box(0, 0, 1, 1)
    verts = list(final.exterior.coords)[:-1]
    verts = [v for v in verts if all(math.dist(v, w) > 1e-6 for w in verts if w is not v)]
    cuts = []
    used = []
    for ck in cut_kinds:
        if ck == 'corner':
            v = rng.choice([v for v in verts if v not in used])
            used.append(v)
            cuts.append(final.intersection(diamond(v, 0.2)))
        elif ck == 'notch':
            cs = list(final.exterior.coords)
            edges = [(cs[i], cs[i + 1]) for i in range(len(cs) - 1)]
            e = rng.choice(edges)
            t = rng.choice([0.3, 0.7])
            m = (e[0][0] + (e[1][0] - e[0][0]) * t, e[0][1] + (e[1][1] - e[0][1]) * t)
            cuts.append(final.intersection(diamond(m, 0.14)))
        else:  # hole
            c = final.buffer(-0.12).representative_point().coords[0]
            cuts.append(box(c[0] - 0.06, c[1] - 0.06, c[0] + 0.06, c[1] + 0.06))
    if any(a.distance(b) < 0.08 for a, b in itertools.combinations(cuts, 2)) or any(c.area < 0.004 for c in cuts):
        raise RuntimeError('cuts too close')
    cut = unary_union(cuts)
    removed = unfold_geom(cut, folds)
    correct = clean(sheet.difference(removed))
    same_g = lambda a, b: a.symmetric_difference(b).area < 0.003
    cands = []
    for ls, why in fold_distractor_lines(folds, regions):
        r = unfold_geom(cut, ls)
        if r.within(sheet.buffer(1e-6)):
            cands.append((clean(sheet.difference(r)), why.replace('half the holes are missing', 'some cut-outs are missing')))
    cands.append((affinity.rotate(correct, 90, origin=(0.5, 0.5)), 'the cut-outs are in the wrong places'))
    cands.append((clean(sheet.difference(cut)), 'only the top layer is cut — it ignores the hidden layers'))
    cands.append((affinity.scale(correct, -1, 1, origin=(0.5, 0.5)), 'it is the correct sheet flipped left-right — the cut-outs end up on the wrong side'))
    cands.append((affinity.scale(correct, 1, -1, origin=(0.5, 0.5)), 'it is the correct sheet flipped top-bottom — the cut-outs end up on the wrong side'))
    ds = pick(correct, cands, same_g)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', fold_panels(folds, regions, lambda ox: geom_svg(cut, ox, fill='grey', stroke=1.6, dash=True), clean(final.difference(cut))))
    sheet_svg = lambda g: doc(100, 100, frame(0, 0) + geom_svg(g))
    x_img = save(f'{qid}-x.svg', doc(100, 100, frame(0, 0) + geom_svg(correct) + crease_svg(creases(folds, regions))))
    steps = '; '.join(f'fold {i + 1}: {FOLD_DESC[k]}' for i, k in enumerate(kinds))
    expl = (f'The cut goes through every layer, so on unfolding the cut-out is reflected across each crease in turn '
            f'({steps}). A cut touching a crease opens into a shape symmetric about that crease. Result: option {ans}. '
            + traps(arr))
    add_q(qid, 'Paper Cutting', diff,
          'A square sheet of paper is folded as shown (dashed line = fold, arrow = direction) and the grey part is cut '
          'away in the last figure. How will the sheet look when unfolded?',
          ans, fig_opts(qid, arr, sheet_svg), expl, stem_img, x_img)


# ================================================================ 8. EMBEDDED FIGURES
NB = [(1, 0), (0, 1), (1, 1), (1, -1)]


def seg(a, b):
    return frozenset([a, b])


def norm_segs(S):
    pts = [p for s in S for p in s]
    mx, my = min(p[0] for p in pts), min(p[1] for p in pts)
    return frozenset(frozenset((p[0] - mx, p[1] - my) for p in s) for s in S)


def tf_segs(S, f):
    return norm_segs([frozenset(f(p) for p in s) for s in S])


def contains(F, X, N=4):
    pts = [p for s in X for p in s]
    w, h = max(p[0] for p in pts), max(p[1] for p in pts)
    for tx in range(0, N - w + 1):
        for ty in range(0, N - h + 1):
            if all(frozenset((p[0] + tx, p[1] + ty) for p in s) in F for s in X):
                return True
    return False


def all_segs(N=4):
    out = []
    for x in range(N + 1):
        for y in range(N + 1):
            for dx, dy in NB:
                q = (x + dx, y + dy)
                if 0 <= q[0] <= N and 0 <= q[1] <= N:
                    out.append(seg((x, y), q))
    return out


def segs_fig(S, off=10, sp=20, sw=2.6):
    return [pline([(off + sp * a[0], off + sp * a[1]), (off + sp * b[0], off + sp * b[1])], sw=sw)
            for a, b in (tuple(s) for s in S)]


def gen_embedded(n_extra, diff):
    qid = nid()
    while True:
        cur = (rng.randrange(3), rng.randrange(3))
        X = set()
        for _ in range(rng.choice([4, 5])):
            opts = []
            for dx, dy in NB + [(-1, 0), (0, -1), (-1, -1), (-1, 1)]:
                q = (cur[0] + dx, cur[1] + dy)
                if 0 <= q[0] <= 2 and 0 <= q[1] <= 2 and seg(cur, q) not in X:
                    opts.append(q)
            if not opts:
                break
            q = rng.choice(opts)
            X.add(seg(cur, q))
            cur = q
        X = norm_segs(X)
        dirs = {(abs(tuple(s)[0][0] - tuple(s)[1][0]), abs(tuple(s)[0][1] - tuple(s)[1][1])) for s in X}
        if len(X) < 4 or (1, 0) not in dirs or (0, 1) not in dirs or (1, 1) not in dirs:
            continue
        variants = {tf_segs(X, f) for f in [lambda p: (-p[0], p[1]), lambda p: (p[0], -p[1]), lambda p: (p[1], -p[0]),
                                           lambda p: (-p[1], p[0]), lambda p: (-p[0], -p[1])]}
        if X in variants or len(variants) < 4:
            continue
        break
    ALL = all_segs()

    def build(Y, must_not=None):
        for _ in range(2000):
            pts = [p for s in Y for p in s]
            w, h = max(p[0] for p in pts), max(p[1] for p in pts)
            tx, ty = rng.randrange(0, 5 - w), rng.randrange(0, 5 - h)
            F = {frozenset((p[0] + tx, p[1] + ty) for p in s) for s in Y}
            F |= set(rng.sample(ALL, n_extra))
            F = frozenset(F)
            if must_not is not None and contains(F, must_not):
                continue
            return F
        raise RuntimeError('embed build failed')

    correct = build(X)
    mir = tf_segs(X, lambda p: (-p[0], p[1]))
    r90 = tf_segs(X, lambda p: (-p[1], p[0]))
    wat = tf_segs(X, lambda p: (p[0], -p[1]))
    # X with one segment moved
    lst = list(X)
    broken = None
    for s in lst:
        for t in ALL:
            Y = norm_segs([u for u in lst if u != s] + [t])
            pts = [p for u in Y for p in u]
            if max(p[0] for p in pts) <= 2 and max(p[1] for p in pts) <= 2 and Y != X and not contains(Y, X, 2):
                broken = Y
                break
        if broken:
            break
    cands = [(build(mir, X), 'it hides the mirror image of the figure, not the figure itself'),
             (build(r90, X), 'it hides a rotated copy; the figure must appear in the same orientation'),
             (build(wat, X), 'it hides an upside-down (water-image) copy'),
             (build(broken, X), 'one line of the figure is missing from it, though it looks close')]
    rng.shuffle(cands)
    ds = pick(correct, cands, lambda a, b: a == b)
    for F, _ in ds:
        assert not contains(F, X)
    assert contains(correct, X)
    ans, arr = arrange(correct, ds)
    stem_img = save(f'{qid}-q.svg', doc(100, 100, frame(0, 0) + render(segs_fig(X, off=30))))
    # explanation: highlight X inside correct option
    pts = [p for s in X for p in s]
    w, h = max(p[0] for p in pts), max(p[1] for p in pts)
    hl = ''
    for tx in range(0, 5 - w):
        for ty in range(0, 5 - h):
            Xt = [frozenset((p[0] + tx, p[1] + ty) for p in s) for s in X]
            if all(s in correct for s in Xt) and not hl:
                hl = render(segs_fig(Xt, sw=8)).replace('stroke="black"', f'stroke="{GREY}"')
    x_img = save(f'{qid}-x.svg', doc(100, 100, frame(0, 0) + hl + render(segs_fig(correct))))
    expl = (f'Trace the given figure, same size and same orientation, inside each option. It fits exactly in option {ans} '
            f'(highlighted grey). ' + traps(arr))
    add_q(qid, 'Embedded Figures', diff,
          'In which option is the given figure (left) hidden? The figure must appear with the same size and orientation.',
          ans, fig_opts(qid, arr, lambda F: doc(100, 100, frame(0, 0) + render(segs_fig(F)))), expl, stem_img, x_img)


# ================================================================ 9. COUNTING FIGURES
def merge_segments(segs):
    groups = {}
    for a, b in segs:
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        if ux < -1e-9 or (abs(ux) < 1e-9 and uy < 0):
            ux, uy = -ux, -uy
        off = ux * a[1] - uy * a[0]
        key = (round(ux, 6), round(uy, 6), round(off, 4))
        ta, tb = sorted((a[0] * ux + a[1] * uy, b[0] * ux + b[1] * uy))
        groups.setdefault(key, (ux, uy, off, []))[3].append([ta, tb])
    out = []
    for ux, uy, off, iv in groups.values():
        iv.sort()
        merged = [iv[0]]
        for s, e in iv[1:]:
            if s <= merged[-1][1] + 1e-6:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])
        for s, e in merged:
            # point = t*u + off*n where n=(-uy,ux)
            nx, ny = -uy, ux
            out.append(((s * ux + off * nx, s * uy + off * ny), (e * ux + off * nx, e * uy + off * ny)))
    return out


def on_seg(p, s, eps=1e-6):
    (x1, y1), (x2, y2) = s
    cr = (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1)
    if abs(cr) > eps * max(1, math.dist(s[0], s[1])):
        return False
    return min(x1, x2) - eps <= p[0] <= max(x1, x2) + eps and min(y1, y2) - eps <= p[1] <= max(y1, y2) + eps


def count_shapes(raw):
    segs = merge_segments(raw)
    pts = {}

    def addp(p):
        pts[(round(p[0], 4), round(p[1], 4))] = p
    for s in segs:
        addp(s[0]); addp(s[1])
    for s, t in itertools.combinations(segs, 2):
        (x1, y1), (x2, y2) = s
        (x3, y3), (x4, y4) = t
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(den) < 1e-12:
            continue
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        if on_seg((px, py), s) and on_seg((px, py), t):
            addp((px, py))
    P_ = list(pts.values())
    conn = {}
    for i, j in itertools.combinations(range(len(P_)), 2):
        conn[i, j] = conn[j, i] = any(on_seg(P_[i], s) and on_seg(P_[j], s) for s in segs)
    tris = []
    for i, j, k in itertools.combinations(range(len(P_)), 3):
        if conn[i, j] and conn[j, k] and conn[i, k]:
            a = abs((P_[j][0] - P_[i][0]) * (P_[k][1] - P_[i][1]) - (P_[k][0] - P_[i][0]) * (P_[j][1] - P_[i][1])) / 2
            if a > 1e-6:
                tris.append(round(a, 2))
    key = {k: i for i, k in enumerate(pts)}
    sqs = set()
    for i, j in itertools.permutations(range(len(P_)), 2):
        if not conn[i, j]:
            continue
        a, b = P_[i], P_[j]
        v = (b[0] - a[0], b[1] - a[1])
        c = (b[0] - v[1], b[1] + v[0])
        d = (a[0] - v[1], a[1] + v[0])
        kc, kd = (round(c[0], 4), round(c[1], 4)), (round(d[0], 4), round(d[1], 4))
        if kc in key and kd in key:
            ic, id_ = key[kc], key[kd]
            if conn[j, ic] and conn[ic, id_] and conn[id_, i]:
                sqs.add((frozenset([i, j, ic, id_]), round(math.dist(a, b) ** 2, 2)))
    return tris, [s[1] for s in sqs]


def size_breakdown(areas):
    from collections import Counter
    c = Counter(areas)
    parts = [str(c[a]) for a in sorted(c)]
    return ' + '.join(parts)


def L(a, b):
    return (a, b)


def counting_figures():
    figs = []
    # F1 triangle with 2 cevians + one cross line
    A, B, C = (50, 10), (10, 90), (90, 90)
    figs.append(('triangles', 'easy', [L(A, B), L(B, C), L(C, A), L(A, (37, 90)), L(A, (63, 90)), L((30, 50), (70, 50))]))
    # F2 square with diagonals and midlines
    s = [(10, 10), (90, 10), (90, 90), (10, 90)]
    figs.append(('triangles', 'medium', [L(s[0], s[1]), L(s[1], s[2]), L(s[2], s[3]), L(s[3], s[0]), L(s[0], s[2]), L(s[1], s[3]),
                                         L((50, 10), (50, 90)), L((10, 50), (90, 50))]))
    # F3 rectangle of two squares, each with both diagonals
    r = [(10, 30), (90, 30), (90, 70), (10, 70)]
    figs.append(('triangles', 'medium', [L(r[0], r[1]), L(r[1], r[2]), L(r[2], r[3]), L(r[3], r[0]), L((50, 30), (50, 70)),
                                         L((10, 30), (50, 70)), L((50, 30), (10, 70)), L((50, 30), (90, 70)), L((90, 30), (50, 70))]))
    # F4 triangle with three medians
    A, B, C = (50, 10), (10, 85), (90, 85)
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    figs.append(('triangles', 'hard', [L(A, B), L(B, C), L(C, A), L(A, mid(B, C)), L(B, mid(A, C)), L(C, mid(A, B))]))
    # F5 squares in 3x3 grid
    g = [10 + 80 * i / 3 for i in range(4)]
    figs.append(('squares', 'medium', [L((g[0], y), (g[3], y)) for y in g] + [L((x, g[0]), (x, g[3])) for x in g]))
    # F6 triangles: square + diagonals + diamond joining side midpoints
    figs.append(('triangles', 'hard', [L(s[0], s[1]), L(s[1], s[2]), L(s[2], s[3]), L(s[3], s[0]), L(s[0], s[2]), L(s[1], s[3]),
                                       L((50, 10), (90, 50)), L((90, 50), (50, 90)), L((50, 90), (10, 50)), L((10, 50), (50, 10))]))
    return figs


def gen_counting(what, diff, raw):
    qid = nid()
    tris, sqs = count_shapes(raw)
    areas = tris if what == 'triangles' else sqs
    c = len(areas)
    cands = [(c - 1, 'it misses one of the larger shapes formed by combining smaller pieces'),
             (c + 2, 'it double-counts shapes or counts non-closed outlines'),
             (c - 2, 'it counts only the obvious shapes and misses the composite ones'),
             (c + 1, 'one shape is counted twice')]
    ds = pick(c, cands, lambda a, b: a == b)
    ans, arr = arrange(c, ds)
    stem_img = save(f'{qid}-q.svg', doc(100, 100, render([pline(s) for s in raw])))
    expl = (f'Count systematically by size, smallest first: {size_breakdown(areas)} = {c} {what}. '
            f'Option {ans}. ' + traps(arr).replace('it ', 'that count '))
    add_q(qid, 'Counting Figures', diff, f'How many {what} are there in the given figure?', ans, text_opts(arr), expl, stem_img)


# ================================================================ 10. PATTERN COMPLETION
D4_LOCAL = {
    'id': lambda p: p, 'r90': lambda p: (50 - p[1], p[0]), 'r180': lambda p: (50 - p[0], 50 - p[1]),
    'r270': lambda p: (p[1], 50 - p[0]), 'mv': lambda p: (50 - p[0], p[1]), 'mh': lambda p: (p[0], 50 - p[1]),
    'tr': lambda p: (p[1], p[0]), 'atr': lambda p: (50 - p[1], 50 - p[0]),
}
QUAD = {'TL': (0, 0), 'TR': (50, 0), 'BR': (50, 50), 'BL': (0, 50)}
QNAME = {'TL': 'top-left', 'TR': 'top-right', 'BR': 'bottom-right', 'BL': 'bottom-left'}


def quad_piece():
    G = [0, 12.5, 25, 37.5, 50]
    while True:
        els = []
        for _ in range(3):
            t = rng.choice(['tri', 'tri', 'seg', 'dot'])
            if t == 'tri':
                x, y = rng.choice(G[:-1]), rng.choice(G[:-1])
                k = 12.5 * rng.choice([1, 2])
                if x + k > 50 or y + k > 50:
                    continue
                corners = [(x, y), (x + k, y), (x + k, y + k), (x, y + k)]
                drop = rng.randrange(4)
                els.append(poly([c for i, c in enumerate(corners) if i != drop], rng.choice(['black', 'grey'])))
            elif t == 'seg':
                a, b = (rng.choice(G), rng.choice(G)), (rng.choice(G), rng.choice(G))
                if math.dist(a, b) < 20 or (a[0] == b[0] and a[0] in (0, 50)) or (a[1] == b[1] and a[1] in (0, 50)):
                    continue
                els.append(pline([a, b]))
            else:
                els.append(circ((rng.choice(G[1:-1]), rng.choice(G[1:-1])), 4.5, rng.choice(['black', 'white'])))
        if len(els) < 3:
            continue
        sigs = {sig(tmap(els, f)) for f in D4_LOCAL.values()}
        if len(sigs) == 8:
            return els


def gen_pattern(symm, diff):
    qid = nid()
    B = quad_piece()
    if symm == 'mirror':
        glob = {'TL': lambda f: f, 'TR': mirror, 'BL': water, 'BR': lambda f: rot(f, 180)}
    else:
        glob = {'TL': lambda f: f, 'TR': lambda f: rot(f, 90), 'BR': lambda f: rot(f, 180), 'BL': lambda f: rot(f, 270)}
    full = {q: glob[q](B) for q in QUAD}
    miss = rng.choice(['TR', 'BR', 'BL'])
    local = lambda q: shift(full[q], -QUAD[q][0], -QUAD[q][1])
    correct = local(miss)
    cands = []
    for q in QUAD:
        if q != miss:
            cands.append((local(q), f'it copies the {QNAME[q]} quarter without reflecting/rotating it'))
    for f in D4_LOCAL.values():
        cands.append((tmap(B, f), 'it is turned or flipped the wrong way, so its lines do not meet the neighbours'))
    rng.shuffle(cands)
    cands.sort(key=lambda c: 0 if 'copies' in c[1] else 1)
    ds = pick(correct, cands, same_fig)
    ans, arr = arrange(correct, ds)
    body = [f'<rect x="0" y="0" width="200" height="200" fill="white" stroke="black" stroke-width="2"/>']
    for q in QUAD:
        if q == miss:
            body.append(qmark(QUAD[q][0] * 2, QUAD[q][1] * 2, 100, 100))
        else:
            body.append(render(full[q], 0, 0, 2))
    stem_img = save(f'{qid}-q.svg', doc(200, 200, ''.join(body)))
    piece_svg = lambda f: doc(100, 100, frame(0, 0) + render(f, 0, 0, 2))
    if symm == 'mirror':
        rule = ('The pattern is symmetric about both the vertical and the horizontal centre lines: each quarter is the '
                'mirror image of the quarter beside it')
    else:
        rule = 'The pattern has quarter-turn symmetry: each quarter is the previous one rotated 90° clockwise about the centre'
    expl = f'{rule}. Applying this to the {QNAME[miss]} quarter gives option {ans}. ' + traps(arr)
    add_q(qid, 'Pattern Completion', diff, 'Which option completes the pattern (replaces the "?" quarter)?', ans,
          fig_opts(qid, arr, piece_svg), expl, stem_img)


# ================================================================ 11. CUBES & DICE
def hexominoes():
    def canon(cells):
        forms = []
        for t in range(8):
            cs = []
            for x, y in cells:
                if t & 4:
                    x, y = y, x
                if t & 1:
                    x = -x
                if t & 2:
                    y = -y
                cs.append((x, y))
            mx, my = min(c[0] for c in cs), min(c[1] for c in cs)
            forms.append(tuple(sorted((x - mx, y - my) for x, y in cs)))
        return min(forms)
    shapes = {canon([(0, 0)])}
    for _ in range(5):
        new = set()
        for s in shapes:
            for x, y in s:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (x + dx, y + dy)
                    if c not in s:
                        new.add(canon(list(s) + [c]))
        shapes = new
    return sorted(shapes)


def fold_cube(cells):
    """Return dict cell -> outward normal, or None if not a cube net."""
    cells = list(cells)
    start = cells[0]
    st = {start: ((0, 0, 1), (1, 0, 0), (0, 1, 0))}
    neg = lambda v: tuple(-a for a in v)
    queue = [start]
    while queue:
        c = queue.pop()
        n, u, v = st[c]
        for (dx, dy), f in (((1, 0), lambda: (u, neg(n), v)), ((-1, 0), lambda: (neg(u), n, v)),
                            ((0, 1), lambda: (v, u, neg(n))), ((0, -1), lambda: (neg(v), u, n))):
            q = (c[0] + dx, c[1] + dy)
            if q in cells and q not in st:
                st[q] = f()
                queue.append(q)
    normals = [st[c][0] for c in cells]
    if len(set(normals)) != 6:
        return None
    return {c: st[c][0] for c in cells}


def net_svg_body(cells, pips=None):
    w = max(c[0] for c in cells) + 1
    h = max(c[1] for c in cells) + 1
    s = min(84 / w, 84 / h)
    ox, oy = (100 - s * w) / 2, (100 - s * h) / 2
    out = []
    for c in cells:
        x, y = ox + c[0] * s, oy + c[1] * s
        out.append(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(s)}" height="{fmt(s)}" fill="white" stroke="black" stroke-width="2"/>')
        if pips:
            for px, py in PIPS[pips[c]]:
                out.append(f'<circle cx="{fmt(x + px * s)}" cy="{fmt(y + py * s)}" r="{fmt(s * 0.08)}" fill="black"/>')
    return ''.join(out)


PIPS = {1: [(.5, .5)], 2: [(.27, .27), (.73, .73)], 3: [(.25, .25), (.5, .5), (.75, .75)],
        4: [(.27, .27), (.73, .27), (.27, .73), (.73, .73)], 5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)],
        6: [(.28, .22), (.72, .22), (.28, .5), (.72, .5), (.28, .78), (.72, .78)]}


def rand_orient(cells):
    t = rng.randrange(8)
    cs = []
    for x, y in cells:
        if t & 4:
            x, y = y, x
        if t & 1:
            x = -x
        if t & 2:
            y = -y
        cs.append((x, y))
    mx, my = min(c[0] for c in cs), min(c[1] for c in cs)
    return tuple(sorted((x - mx, y - my) for x, y in cs))


def why_not_net(cells):
    s = set(cells)
    if any({(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)} <= s for x, y in s):
        return 'it contains a 2×2 block of squares, which would close up with gaps and overlaps'
    for x, y in s:
        if all((x + i, y) in s for i in range(5)) or all((x, y + i) in s for i in range(5)):
            return 'it has five squares in a row; the fifth would overlap the first'
    return 'on folding, two of its squares land on the same face and one face stays open'


def gen_net_valid(diff):
    qid = nid()
    hexes = hexominoes()
    valid = [h for h in hexes if fold_cube(h)]
    invalid = [h for h in hexes if not fold_cube(h)]
    assert len(valid) == 11 and len(invalid) == 24
    if diff == 'hard':
        invalid = [h for h in invalid if '2×2' not in why_not_net(h)]
    good = rand_orient(rng.choice(valid))
    bads = [rand_orient(h) for h in rng.sample(invalid, 3)]
    ans, arr = arrange(good, [(b, why_not_net(b)) for b in bads])
    expl = (f'Fold option {ans} mentally: keep one square as the base; the four squares around it (in the net) become the '
            f'side walls and the last square becomes the lid — all six faces are covered exactly once. ' + traps(arr))
    add_q(qid, 'Cube and Dice', diff, 'Which of the following sheets can be folded along the lines to form a closed cube?',
          ans, fig_opts(qid, arr, lambda c: doc(100, 100, net_svg_body(c))), expl)


def gen_dice_opposite(diff, straight):
    qid = nid()
    valid = [h for h in hexominoes() if fold_cube(h)]
    if straight:
        valid = [h for h in valid if any(all((x + i, y) in h for i in range(4)) for x, y in h)]
    else:
        valid = [h for h in valid if not any(all((x + i, y) in h or (x, y + i) in h for i in range(4)) for x, y in h)
                 or not any(all((x + i, y) in h for i in range(4)) for x, y in h)]
        valid = [h for h in valid if not any(all((x + i, y) in h for i in range(4)) or all((x, y + i) in h for i in range(4)) for x, y in h)]
    net = rand_orient(rng.choice(valid))
    normals = fold_cube(net)
    nums = list(range(1, 7))
    rng.shuffle(nums)
    pips = dict(zip(net, nums))
    target = rng.choice(net)
    opp = [c for c in net if normals[c] == tuple(-a for a in normals[target])][0]
    adj = [c for c in net if c not in (target, opp)]
    ds = [(f'{pips[c]} dots', f'the face with {pips[c]} dots shares an edge with the {pips[target]}-dot face') for c in rng.sample(adj, 3)]
    ans, arr = arrange(f'{pips[opp]} dots', ds)
    pairs = []
    seen = set()
    for c in net:
        if c in seen:
            continue
        o = [d for d in net if normals[d] == tuple(-a for a in normals[c])][0]
        seen |= {c, o}
        pairs.append(f'{pips[c]}–{pips[o]}')
    stem_img = save(f'{qid}-q.svg', doc(100, 100, net_svg_body(net, pips)))
    expl = (f'Folding the net gives the opposite-face pairs {", ".join(pairs)} (in a net, two faces with exactly one '
            f'square between them in a straight line are opposite; any two squares sharing an edge are adjacent). '
            f'So {pips[opp]} dots is opposite {pips[target]} dots: option {ans}. ' + traps(arr))
    add_q(qid, 'Cube and Dice', diff,
          f'The sheet below is folded to form a cube. Which face will be opposite the face with {pips[target]} dots?',
          ans, text_opts(arr), expl, stem_img)


# ================================================================ main
def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    for f in FIG_DIR.glob('lr-fig-*.svg'):
        f.unlink()

    # 1 series (9)
    gen_series_rotation(90, 'easy')
    gen_series_rotation(45, 'medium')
    gen_series_rotation(-135, 'hard')
    gen_series_count('dots', 'easy')
    gen_series_count('poly', 'medium')
    gen_series_count('dots2', 'medium')
    gen_series_move(1, 'easy')
    gen_series_move(2, 'medium')
    gen_series_move(2, 'hard')
    # 2 analogy (8)
    for plan in ANALOGY_PLANS:
        gen_analogy(plan)
    # 3 odd one out (7)
    gen_odd_mirror('easy')
    gen_odd_mirror('medium')
    gen_odd_mirror('medium')
    gen_odd_mirror('medium', r45=True)
    gen_odd_mirror('hard', r45=True)
    gen_odd_count('easy')
    gen_odd_count('medium')
    # 4 matrix (8)
    gen_matrix('easy', False)
    gen_matrix('easy', False)
    gen_matrix('medium', True)
    gen_matrix('medium', True)
    gen_matrix('medium', True)
    gen_matrix('medium', True)
    gen_matrix('hard', True)
    gen_matrix('hard', True)
    # 5 mirror / water (8)
    gen_mirror_fig('mirror', 'easy')
    gen_mirror_fig('water', 'easy')
    gen_mirror_fig('mirror', 'medium')
    gen_mirror_fig('water', 'medium')
    gen_mirror_fig('mirror', 'medium')
    gen_mirror_text('FR47', 'mirror', 'easy')
    gen_mirror_text('J2PG', 'water', 'medium')
    gen_mirror_text('K5RL', 'mirror', 'hard')
    # 6 paper folding (8)
    gen_punch(['R2L'], 1, 'easy')
    gen_punch(['T2B'], 1, 'easy')
    gen_punch(['DTR'], 1, 'easy')
    gen_punch(['R2L', 'T2B'], 1, 'medium')
    gen_punch(['DTR', 'ATL'], 1, 'medium')
    gen_punch(['L2R', 'B2T'], 1, 'medium')
    gen_punch(['T2B', 'R2L'], 2, 'hard')
    gen_punch(['R2L', 'T2B', 'DTR'], 1, 'hard')
    # 7 paper cutting (4)
    gen_cut(['R2L'], ['notch'], 'easy')
    gen_cut(['R2L', 'T2B'], ['corner'], 'medium')
    gen_cut(['DBL'], ['notch', 'corner'], 'medium')
    gen_cut(['T2B', 'L2R'], ['corner', 'notch'], 'hard')
    # 8 embedded (4)
    gen_embedded(6, 'easy')
    gen_embedded(9, 'medium')
    gen_embedded(10, 'medium')
    gen_embedded(13, 'hard')
    # 9 counting (6)
    for what, diff, raw in counting_figures():
        gen_counting(what, diff, raw)
    # 10 pattern completion (4)
    gen_pattern('mirror', 'easy')
    gen_pattern('mirror', 'medium')
    gen_pattern('rotation', 'medium')
    gen_pattern('rotation', 'hard')
    # 11 cubes (4)
    gen_dice_opposite('easy', True)
    gen_dice_opposite('medium', False)
    gen_net_valid('medium')
    gen_net_valid('hard')

    OUT.write_text(json.dumps(QS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    from collections import Counter
    print('questions:', len(QS))
    print('topics:', dict(Counter(q['topic'] for q in QS)))
    print('difficulty:', dict(Counter(q['difficulty'] for q in QS)))
    print('answers:', dict(sorted(Counter(q['answer'] for q in QS).items())))


if __name__ == '__main__':
    main()
