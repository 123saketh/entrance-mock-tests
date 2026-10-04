from sympy import *
a,r,p,n,x=symbols('a r p n x')
s=solve([2*(a*r-7)-(a-2)-(a*r**2-9), 2*(a*r**2-9)-(a*r-7)-(a*r**3-5)],[a,r],dict=True);print('188',s,[ (v[a]**4*v[r]**6/24) for v in s])
# 189 both roots negative: D>=0, sum<0, prod>0
print(solve((p+2)**2-4*(2*p+9),p))
# 190: |adj adj adj A| = |A|^8 =81 -> |A|^2 = 3? |A|^(2^3)=81 -> |A|=±sqrt3 ; |adj adj A|=|A|^4=9
d=sqrt(3)
for dd in [sqrt(3),-sqrt(3)]:
  S=[k for k in range(-50,50) if simplify((dd**4)**Rational((k-1)**2,2)-dd**(3*k**2-5*k-4))==0]
  print('190',dd,S,sum(abs(dd**(k*k+k)) for k in S))
# 191
xs=solve(4-x**2/4-(x-4)/2,x);print(xs,6*integrate(4-x**2/4-(x-4)/2,(x,min(xs),max(xs))))
