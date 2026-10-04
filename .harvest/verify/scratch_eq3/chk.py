from sympy import *
x,y,t,th=symbols('x y t theta',real=True)
# 17 orthocentre
A=solve([4*x+5*y-20,3*x-2*y+6],[x,y]);print('A',A)
B=solve([4*x+5*y-20,2*x+3*y-5],[x,y]);C=solve([3*x-2*y+6,5*x-4*y-1],[x,y]);print(B,C)
m=(C[y]-B[y])/(C[x]-B[x]);print('slope',m)
# check H: AH perp BC
print('AH.BC', (A[x]-1)*(C[x]-B[x])+(A[y]-1)*(C[y]-B[y]))
# 43
print(integrate(x*sin(x)**6*cos(x)**4,(x,0,2*pi)).simplify())
# 48
area=Rational(1,2)*Abs(Matrix([[4,-4,1],[9,6,1],[t**2,2*t,1]]).det())
print(simplify(Matrix([[4,-4,1],[9,6,1],[t**2,2*t,1]]).det()))
# 52
yy=10*x**6-24*x**5+15*x**4-40*x**2+108
print([r.evalf() for r in real_roots(diff(yy,x))], [diff(yy,x,2).subs(x,r).evalf() for r in real_roots(diff(yy,x))])
# 64
e=3*(sin(th)-cos(th))**4+6*(sin(th)+cos(th))**2+4*sin(th)**6
print(simplify(e-(13-4*cos(th)**6)))
for o in [13-4*cos(th)**4+2*sin(th)**2*cos(th)**2,13-4*cos(th)**4+6*sin(th)**2*cos(th)**2,13-4*cos(th)**2+6*cos(th)**4]:
  print(N((e-o).subs(th,1.0)))
# 68
print(Poly(expand((1+x-2*x**2)**9),x).coeff_monomial(x**5))
# 11-Q3 numerically
import math
n=10**6
s1=sum(math.sqrt(r) for r in range(1,2*n+1));s2=sum(1/math.sqrt(r) for r in range(1,2*n+1))
print(3*s1*s2/(4*n*(n+1)/2))
# 7 tautology
import itertools
imp=lambda a,b:(not a) or b
print([ (p,q,r) for p,q,r in itertools.product([0,1],repeat=3) if not imp(imp(p,imp(q,r)),imp(imp(p,q),r))])
# 18 numerically greatest
from math import comb
for xv in [0.83,0.84,1.0,1.19,1.21]:
  ts=[comb(21,r)*xv**r for r in range(22)];print(xv,ts.index(max(ts)))
