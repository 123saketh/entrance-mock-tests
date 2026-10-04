import json,random,sys
d=json.load(open('public/data/questions/harvested.json',encoding='utf-8'))
src=sys.argv[1]; n=int(sys.argv[2]); random.seed(int(sys.argv[3]))
xs=[q for q in d if q['id'].startswith('h-'+src)]
for q in random.sample(xs,n):
    print(q['id'],q['topic'],q['difficulty'],'| ANS',q['answer'],'|',q['source']['ref']); print(q['stem']);
    for o in q['options']: print(' ',o['key'],o['text'])
    print('  EXPL:',q['explanation'][:400]); print()
