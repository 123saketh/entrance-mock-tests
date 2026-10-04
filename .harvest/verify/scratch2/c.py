from sympy import *
from itertools import permutations
import numpy as np
x,y=symbols('x y')
# 82
print('82',N(sum(1/(sin(pi/4+(r-1)*pi/6)*sin(pi/4+r*pi/6)) for r in range(1,14))), N(2*sqrt(3)-2))
# 110
s=solve([x**2/12+y**2/8-1,x**2/6+y**2/9-1],[x,y]); print('110',s[0], simplify(4*abs(s[0][0]*s[0][1])), N(24*sqrt(6)/5))
# 118
X=symbols('X'); Y=Function('Y')
# dy/dx = -(sin x - 3y sin x ln cos x)/(cos x (ln cos x)^2)
sol=dsolve(Eq(Y(X).diff(X), -(sin(X)-3*Y(X)*sin(X)*log(cos(X)))/(cos(X)*log(cos(X))**2)),Y(X)); print(sol)
C1=symbols('C1'); e=sol.rhs; c=solve(e.subs(X,pi/4)+1/log(2),C1)[0]; v=e.subs(C1,c).subs(X,pi/6); print('118',N(v), N(1/(log(3)-log(4))))
# 120 grid
n=4000; xs=np.linspace(-3,3,n); ys=np.linspace(-3,6,n); XX,YY=np.meshgrid(xs,ys)
m=(2*YY<=XX**2+3)&(YY+abs(XX)<=3)&(YY>=abs(XX-1)); print('120',6*m.sum()*(xs[1]-xs[0])*(ys[1]-ys[0]))
# 128
sol=dsolve(Eq(Y(X).diff(X)+tan(X)*Y(X),(2+sec(X))/(1+2*sec(X))**2),Y(X)); e=sol.rhs; c=solve(e.subs(X,pi/3)-sqrt(3)/10,C1)[0]; v=e.subs(C1,c).subs(X,pi/4); print('128',N(v),N((4-sqrt(2))/14))
# 132
w=sorted(''.join(p) for p in permutations('KANPUR')); print('132',w[439])
print('137',pow(7,103,23))
