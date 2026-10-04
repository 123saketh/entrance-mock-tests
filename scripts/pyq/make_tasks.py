import json,os
T='C:/Users/SakethDahagam/AppData/Local/Temp/pyq'
chunks=[]
for sh in ['12-1','12-2','13-1','13-2','14-1']:
  idx=json.load(open(f'{T}/ap/{sh}/index.json'))
  for lo,hi,name in [(1,40,'m1'),(41,80,'m2'),(81,120,'p'),(121,160,'c')]:
    items=[{'n':r['n'],'subject':r['subject'],'png':f"{T}/ap/{sh}/{r['png']}",'official_key':'ABCD'[r['key']-1]} for r in idx if lo<=r['n']<=hi and r['key']]
    fn=f'{T}/tasks/{sh}_{name}.json'; json.dump(items,open(fn,'w'),indent=1); chunks.append(fn)
print(len(chunks))
