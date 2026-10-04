from sympy import *
t=symbols('t')
for P0 in [(Rational(10,7),Rational(22,7),7),(Rational(15,7),Rational(32,7),7)]:
  P=Matrix(P0);d=Matrix([1,4,7]);Q=P+t*d
  s=solve([ (Q[0]+1)*5-(Q[1]+3)*3, (Q[0]+1)*7-(Q[2]+5)*3],t,dict=True); print(P0,s,[ (d*v[t]).dot(d*v[t]) for v in s])
