from sympy import *
x,y,t,s,a,b,u=symbols('x y t s a b u')
# 116: (7x^4 cot y - e^x csc y) dx/dy = x^5 -> dx/dy ... treat as x as func of y? try u=cos y
Y=Function('Y')
# rewrite: dy/dx = (7x^4 cot y - e^x csc y)/x^5 ; multiply sin y: sin y dy/dx = (7x^4 cos y - e^x)/x^5 ; let u=cos y: -u' = 7u/x - e^x/x^5
U=Function('U')
sol=dsolve(Eq(-U(x).diff(x),7*U(x)/x-exp(x)/x**5),U(x),ics={U(1):0}); print('116',sol, simplify(sol.rhs.subs(x,2)))
# 118
f=Function('f'); 
F=solve([Eq(a+2*b,x**2+5),Eq(b+2*a,1/x**2+5)],[a,b])[a]; G=solve([Eq(2*a-3*b,x),Eq(2*b-3*a,1/x)],[a,b])[a]
al=integrate(F,(x,1,2)); be=integrate(G,(x,1,2)); print('118',simplify(9*al+be))
# 119
A=Matrix([7+t,5,3-t]); B=Matrix([1+3*s,-3+4*s,-7+5*s]); so=solve(list(A-B),[t,s],dict=True); print('119',so, A.subs(so[0]))
d1=Matrix([1,0,-1]);d2=Matrix([3,4,5]); c=d1.dot(d2)/(d1.norm()*d2.norm()); sn=sqrt(1-c**2); print(simplify((Rational(1,2)*15*sn)**2))
# 120
so=solve([2+3+3+4+5+7+a+b-32, sum(v**2 for v in [2,3,3,4,5,7,a,b])/8-16-2],[a,b]); print('120',so)
