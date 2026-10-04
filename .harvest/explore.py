import json,re,collections,csv
d=[x for x in json.load(open('jeebench.json',encoding='utf-8')) if x['type']=='MCQ']
img=[x for x in d if re.search(r'figure|diagram|graph|shown|includegraphics|image',x['question'],re.I)]
print(len(d),len(img))
nolist=[x for x in d if not re.search(r'\(A\)',x['question'])]
print('no (A):',len(nolist))
for x in nolist[:3]: print(x['question'][-600:]);print('---')
pw=[json.loads(l) for f in ['pw_jan.jsonl','pw_apr.jsonl'] for l in open(f,encoding='utf-8')]
m=[x for x in pw if x['question_type']==1]
print(len(pw),len(m), collections.Counter(len(x['options']) for x in m), collections.Counter(len(x['correct_options']) for x in m))
print(pw[0]['metadata'], [x['metadata'] for x in pw if x['metadata']][:1])
print(sum(bool(re.search(r'figure|diagram|graph shown|<img|shown',x['question'],re.I)) for x in m))
ck=list(csv.DictReader(open('ck.csv',encoding='utf-8')))
print(len(ck), collections.Counter(r['Shift Name'] for r in ck), collections.Counter(r['Correct Option'] for r in ck))
