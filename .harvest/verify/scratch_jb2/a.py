from math import comb
from itertools import combinations
from fractions import Fraction
# Q15
ways=[0]*6
for r in range(1,4):
  for b in range(1,3): ways[r+b]+=comb(3,r)*comb(2,b)
tot=0
import itertools
for t in itertools.product(range(6),repeat=4):
  if sum(t)==10: tot+=1 if False else ways[t[0]]*ways[t[1]]*ways[t[2]]*ways[t[3]]
print(tot)
# Q6
X=[(x,y) for x in range(-5,6) for y in range(-6,7) if Fraction(x*x,8)+Fraction(y*y,20)<1 and y*y<5*x]
print(len(X),X)
good=0;n=0
for P,Q,R in combinations(X,3):
  n+=1
  a2=abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))
  if a2>0 and a2%2==0: good+=1
print(Fraction(good,n))
