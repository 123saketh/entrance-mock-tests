from sympy import *
from fractions import Fraction as F
import itertools, math
# pw2 dice
d1=[1,1,2,2,3,4]; d2=[1,2,2,3,3,4]
print('pw2', F(sum(a+b in (4,5) for a in d1 for b in d2),36))
# pw8: line 3x-2y+12=0, parabola 4y=3x^2
x=symbols('x'); xs=solve(Eq(4*(3*x+12)/2,3*x**2),x); pts=[(r,(3*r+12)/2) for r in xs]
(a,b),(c,d)=pts; ang=atan2(a*d-b*c, a*c+b*d); print('pw8', pts, simplify(tan(ang)))
# pw9
t=symbols('t'); P=Matrix([3+7*t,2-t,-2-2*t]); Q=Matrix([10,-3,-1]); ts=solve((Q-P).dot(Matrix([7,-1,-2])),t)[0]; P=P.subs(t,ts); R=Matrix([3,-2,1])
print('pw9', P.T, sqrt(((Q-P).cross(R-P)).dot((Q-P).cross(R-P)))/2)
# pw12
l=symbols('l'); M=Matrix([[l-1,l-4,l],[l,l-1,l-4],[l+1,l+2,-(l+2)]]); print('pw12 det roots', solve(M.det(),l), [r**2+r for r in solve(M.det(),l)])
# pw15: P(5,4) Q(-2,4) R(a,b) area 35, orthocentre (2,14/5)
a,b=symbols('a b'); H=Matrix([2,Rational(14,5)])
sol=solve([ (H-Matrix([a,b])).dot(Matrix([7,0])), (H-Matrix([5,4])).dot(Matrix([a+2,b-4]))],[a,b],dict=True)
for s in sol:
  A_=abs(Rational(1,2)*7*(s[b]-4)); 
  if A_==35: print('pw15', s, (5-2+s[a])/3 + 2*(8+s[b])/3)
# jee adv 2016 P1 Q39
xx=symbols('x'); f=sqrt(3)/cos(xx)+1/sin(xx)+2*(tan(xx)-cot(xx))
import numpy as np
roots=set()
for x0 in np.linspace(-3.1,3.1,400):
  try:
    r=nsolve(f,xx,x0); r=float(r)
    if -math.pi<r<math.pi and min(abs(r),abs(abs(r)-math.pi/2))>1e-3: roots.add(round(r,6))
  except Exception: pass
print('jee39', sorted(roots), sum(roots)/math.pi*9)
