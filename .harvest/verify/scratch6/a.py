from sympy import *
x,y,t,m,c,p=symbols('x y t m c p',real=True)
# 151 orthocentre (3,-1)
A=solve([y-x-1,y-4*x+8],[x,y]);print('151 vertex',A)
# third line y=mx+c; altitude from intersection vertex A=(3,4) to line mx+c passes through H(3,-1): line through A,H is x=3 vertical => third line horizontal m=0
# other: vertex B on y=x+1 and third line; altitude from B perpendicular to y=4x-8 passes H
# with m=0: y=c, B=(c-1,c); BH perpendicular to slope 4: slope (c+1)/(c-1-3)=-1/4
print(solve(Eq((c+1)*4,-(c-4)),c))
# 152
r=symbols('r',positive=True) # r=|a+b|/|a-b|
s=solve(Eq((r+1)/(r-1),sqrt(2)+1),r)[0];print('152 r',s)
# |a+b|^2+|a-b|^2=4|a|^2 -> |a+b|^2/|a|^2 = 4 r^2/(r^2+1)
print(nsimplify(simplify(4*s**2/(s**2+1))))
# 154
f=(5-x)/(x**2-3*x+2); print(solve(diff(f,x),x),[f.subs(x,v).simplify() for v in solve(diff(f,x),x)])
# 155
pr=Rational(19,2)/(Rational(19,2)+1); print('155',pr, pr.q**2-pr.p**2)
# 156
s156=solve(Eq(p+(1-2*p)/2*(4+9), 2*(p+(1-2*p)/2*5)),p);print('156',s156,[8*v-1 for v in s156])
# 157
print('157',solve(1+x**2-(x+7)),solve(1+x**2-(11-3*x)), solve(x+7-(11-3*x)))
A157=integrate(x+7-1-x**2,(x,-2,1))+integrate(11-3*x-1-x**2,(x,1,2));print(3*A157)
# 158
a,b,d=symbols('a b d');F=5*x**2+a*x**3+b*x**4
sol=solve([diff(F,x).subs(x,4),diff(F,x).subs(x,5)],[a,b]);print('158',F.subs(sol).subs(x,2))
