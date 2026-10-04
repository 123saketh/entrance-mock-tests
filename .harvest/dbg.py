import sys; sys.path.insert(0,'scripts/harvest')
import build_harvested as b
for it in b.load_jeebench()+b.load_pw()+b.load_eq():
    if any(not o.strip() for o in it['options']): print(it['_ref'], it['options'], it['stem'][-300:])
