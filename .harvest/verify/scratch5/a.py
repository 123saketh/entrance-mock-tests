from sympy import *
import itertools, numpy as np
x,y,t,s,l=symbols('x y t s l')
# 77 test L2: x-6=y=-z+4
A=Matrix([1+2*t,2+3*t,3+4*t]); B=Matrix([6+s,s,4-s]); P=Matrix([4,1,0])
sol=solve(list((A-P).cross(B-P)),[t,s],dict=True); print('77',sol)
for so in sol:
  a=A.subs(so);b=B.subs(so); print(Matrix([[1,0,1],list(a),list(b)]).det())
# 80
S=range(-3,4); R=[(a,b) for a in S for b in S if 0<=a*a+2*b<=4]; print('80',len(R), len(R)+sum((a,a) not in R for a in S))
# 85
M=Matrix([[sin(x),cos(x),sin(x)+cos(x)+1],[27,28,27],[1,1,1]]); yy=M.det(); print('85',simplify(diff(yy,x,2)+yy))
# 86
f=lambda x:2*x+3*np.tan(x)-np.pi
xs=np.linspace(-2*np.pi,2*np.pi,2000001); v=f(xs); c=0
for i in range(len(xs)-1):
  if np.sign(v[i])!=np.sign(v[i+1]) and abs(v[i])<5 and abs(v[i+1])<5: c+=1
print('86',c)
# 89
z=symbols('z'); sols=solve(z**2+3*I-(2+3*I)*(z-2+I),z); print('89',sols, expand(sum(q**2 for q in sols)))
# 104
R=[(a,b) for a in S for b in S if 2*a-b in (0,1)]; Rs=set(R); print('104',len(R), sum((a,a) not in Rs for a in S), sum((b,a) not in Rs for a,b in R))
# 105
th=symbols('th'); w=((8+I)*sin(th)+(7+4*I)*cos(th))*((1+8*I)*sin(th)+(4+7*I)*cos(th)); e=expand(re(w)+im(w)); print('105',simplify(e))
