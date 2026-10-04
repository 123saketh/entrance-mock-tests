import json, re, sys, collections
d = json.load(open('public/data/questions/harvested.json', encoding='utf-8'))
ids = [q['id'] for q in d]
assert len(ids) == len(set(ids)), 'duplicate ids'
bad = []
for q in d:
    assert q['subject'] in ('physics', 'chemistry', 'mathematics', 'english', 'reasoning')
    assert q['difficulty'] in ('easy', 'medium', 'hard')
    assert [o['key'] for o in q['options']] == list('ABCD') and q['answer'] in 'ABCD'
    assert all(o['text'].strip() for o in q['options']) and q['stem'].strip() and q['explanation'].strip()
    assert q['source']['kind'] == 'harvested' and q['source']['licence']
    for t in [q['stem'], q['explanation']] + [o['text'] for o in q['options']]:
        if t.replace('$$', '').count('$') % 2 or '$$$' in t or (re.search(r'\[a-zA-Z]', t) and '$' not in t):
            bad.append(q['id']); break
    if len({o['text'] for o in q['options']}) < 4:
        bad.append(q['id'] + ':dupopt')
print('items', len(d), 'latex/format problems', len(bad), bad[:30])
print(collections.Counter(q['difficulty'] for q in d))
