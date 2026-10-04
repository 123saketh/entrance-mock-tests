import csv, json, re, difflib
def strip(s):
    s=re.sub(r'\[a-zA-Z]+','',s); return re.sub(r'[^a-z0-9]','',s.lower())
def digits(s):
    s=re.sub(r'\[a-zA-Z]+','',s); return re.findall(r'\d+',s)
ck=[]
for r in csv.DictReader(open('ck.csv',encoding='utf-8')):
    q=r['Question Text']
    m=re.search(r'\n\s*\(?1[\).]\s',q)
    stem=q[:m.start()] if m else q
    opts=re.split(r'\n\s*\(?[1-4][\).]\s*|\(\d\)\s*',q[m.start():]) if m else []
    ck.append((strip(stem),digits(stem),sorted(''.join(digits(o)) for o in opts if o.strip()),r['Correct Option']))
pw=[json.loads(l) for l in open('pw_jan.jsonl',encoding='utf-8')]
res={'match':0,'stemdiff':0,'optdiff':0,'nock':0}
keys=[c[0] for c in ck]
out={}
for n,x in enumerate(pw):
    if x['question_type']!=1: continue
    s=strip(x['question'])
    best=difflib.get_close_matches(s,keys,n=1,cutoff=0.6)
    if not best: res['nock']+=1; continue
    c=ck[keys.index(best[0])]
    sd=digits(x['question'])==c[1]
    od=sorted(''.join(digits(o)) for o in x['options'])==c[2]
    ka=c[3] in '1234' and len(c[3])==1 and int(c[3])-1==x['correct_options'][0]
    k='match' if sd and od and ka else ('stemdiff' if not sd else 'optdiff')
    res[k]+=1; out[n+1]=k
print(res)
json.dump(out,open('pw_xcheck.json','w'))
