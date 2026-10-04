from sympy import *
from itertools import permutations
import numpy as np
x,y=symbols('x y')
print('82',N(sum(1/(sin(pi/4+(r-1)*pi/6)*sin(pi/4+r*pi/6)) for r in range(1,14))), N(2*sqrt(3)-2))
s=solve([x**2/12+y**2/8-1,x**2/6+y**2/9-1],[x,y]); print('110',s[0], N(4*abs(s[0][0]*s[0][1])), N(24*sqrt(6)/5))
n=3000; xs=np.linspace(-3,3,n); ys=np.linspace(-3,6,n); XX,YY=np.meshgrid(xs,ys)
m=(2*YY<=XX**2+3)&(YY+abs(XX)<=3)&(YY>=abs(XX-1)); print('120',6*m.sum()*(xs[1]-xs[0])*(ys[1]-ys[0]))
w=sorted(''.join(p) for p in permutations('KANPUR')); print('132',w[439])
print('137',pow(7,103,23))
