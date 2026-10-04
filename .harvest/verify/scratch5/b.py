from sympy import *
import itertools, numpy as np
x,y,t,s,l,p=symbols('x y t s l p')
A,B=symbols('A B',positive=True)
e=sqrt(5)/3; so=solve([16/A-9/B-1, B-A*(e**2-1)],[A,B],dict=True); print('110',so)
for q in so:
  aa=sqrt(q[A]); bb2=q[B]; L=2*bb2/aa; m=(e*4)**2-aa**2; print(L,m,simplify(9*L**2+6*m))
M=Matrix([[1,0,0],[1,0,1],[0,1,0]]); print('111',sum(M**50))
print('112',nsimplify(sum(Rational(4*k,4+3*k*k+k**4) for k in range(1,21))))
v=sum(k*k*binomial(15,k)**2 for k in range(1,16)); print('113',factorint(v))
for pp in [sqrt(7),-sqrt(7)]:
  print(solve([x**2/4+y**2/3-1,y-x-pp],[x,y]))
print(solve([x**2/4+y**2/3-1,y-x],[x,y]))
