from sympy import *
x,y,t,s,lam,n=symbols('x y t s lam n')
# 134
L=Matrix([6+3*t,7+2*t,7-2*t]); P=Matrix([1,2,3]); d=Matrix([3,2,-2])
t0=solve((L-P).dot(d),t)[0]; F=L.subs(t,t0); print('134 foot',F)
k=2*sqrt(17)/d.norm(); A=F+k*d; B=F-k*d; print(simplify(A.dot(B)))
# 136
print('136', sum((4*k-3)**2 for k in range(1,21))+sum(4*k-1 for k in range(1,21)))
# 137 terms: T_{r+1}=C(n,r) a^{n-r} b^r ; ratio T15/T15end = (a/b)^{n-28}
a=sqrt(2)/3; b=1/sqrt(3)
for N in range(28,80):
  if simplify((a/b)**(N-28)-Rational(1,6))==0: print('137',N,binomial(N,3))
# alt with 2^{1/3}
a2=2**Rational(1,3); b2=1/3**Rational(1,3)
for N in range(28,80):
  if simplify((a2/b2)**(N-28)-Rational(1,6))==0 or simplify((a2/b2)**(28-N)-Rational(1,6))==0: print('137alt',N,binomial(N,3))
# 139
u=Matrix([3,-1,0]); v=Matrix([2,1,-lam])
ls=solve(Eq((u.dot(v))**2/(u.dot(u)*v.dot(v)),Rational(5,28)),lam); print('139',ls)
for L_ in ls:
  if L_>0: vv=v.subs(lam,L_); v1=(u.dot(vv)/u.dot(u))*u; v2=vv-v1; print(v1.dot(v1)+v2.dot(v2), vv.dot(vv))
# 140
lines=[(4,-7,10),(1,1,-5),(7,4,-15)]
def inter(l1,l2):
  return solve([l1[0]*x+l1[1]*y+l1[2], l2[0]*x+l2[1]*y+l2[2]],[x,y])
V=[inter(lines[0],lines[1]),inter(lines[1],lines[2]),inter(lines[0],lines[2])]; print('140',V)
# 141
f=((1+sqrt(Abs(x))-x)*exp(x)+(sqrt(Abs(x))-x)*exp(-x))/(exp(x)+exp(-x))
print('141',N(Integral(f,(x,-1,1))), N(1+2*sqrt(2)/3), N(3-2*sqrt(2)/3),N(1-2*sqrt(2)/3))
