from sympy import *
from itertools import product
x,y,t,m=symbols('x y t m')
# 92
P=Matrix([Rational(10,7),Rational(22,7),7]);d=Matrix([1,4,7])
Q=P+t*d; s=solve([ (Q[0]+1)*5-(Q[1]+3)*3, (Q[0]+1)*7-(Q[2]+5)*3],t); print('92',s, [ (t*d).dot(t*d).subs(t,v) for v in ([s[t]] if isinstance(s,dict) else s)])
# 94
r=solve(x**2-(3-2*I)*x-(2*I-2),x); r=[nsimplify(expand(v)) for v in r]; print('94',r, re(r[0])*re(r[1])+im(r[0])*im(r[1]))
# 95
sol=solve(((m-Rational(1,2))/(1+m/2))**2-((m+1)/(1-m))**2,m); print('95',sol, sum(sol))
# 105
sl=solve([(x-4)**2+(y-3)**2-y**2,(x-4)**2+(y-3)**2-x**2],[x,y]); print('105',sl)
if len(sl)==2: print(simplify((sl[0][0]-sl[1][0])**2+(sl[0][1]-sl[1][1])**2))
# 106
print('106',sum(1 for p in product([1,2,3],repeat=7) if sum(p)==11))
# 107
l,u=symbols('l u'); a=Matrix([1,2,1]);b=Matrix([2,7,3])
s=solve(list(Matrix([-1,2,1])+l*a-Matrix([0,1,1])-u*b),[l,u]); print('107',s)
if s:
  X=Matrix([-1,2,1])+s[l]*a; dd=a+b; print(X.T,dd.T)
  for pt in [(5,17,4),(2,8,5),(8,26,12),(-1,-1,1)]:
    v=Matrix(pt)-X; print(pt, v.cross(dd).T)
# 109
th=symbols('th'); print('109',N(80*Integral((sin(th)+cos(th))/(9+16*sin(2*th)),(th,0,pi/2))), N(4*log(3)),N(3*log(4)))
# 111
A=Matrix([[log(128,5),log(5,4)],[log(8,5),log(25,4)]]); C=A*A.adjugate().T*0; 
Cof=A.adjugate().T
C=Matrix(2,2,lambda i,j: sum(A[i,k]*Cof[j,k] for k in range(2)))
print('111',N(8*C.det()))
# 113
L1p=Matrix([1,2,1]);d1=Matrix([1,1,2]);d2=Matrix([1,2,4]); n=d1.cross(d2); print('113 n',n.T)
for pt in [L1p]:
  pass
# L3 passes through point on L1 with direction n: any point (alpha,beta,gamma)= L1p+l d1 + u n ; 5a-11b-8g
al=L1p+l*d1+u*n; print(expand(5*al[0]-11*al[1]-8*al[2]))
# 114
M=Matrix([[1+sin(x)**2,cos(x)**2,4*sin(4*x)],[sin(x)**2,1+cos(x)**2,4*sin(4*x)],[sin(x)**2,cos(x)**2,1+4*sin(4*x)]]); print('114',simplify(M.det()))
# 116
k=symbols('k',integer=True); print('116',N(Sum((k**3+6*k**2+11*k+6)/factorial(k+3),(k,1,80)).doit()), N(Rational(5,3)))
