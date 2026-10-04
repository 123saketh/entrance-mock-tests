from sympy import *
import numpy as np
x,y,t,th=symbols('x y t theta',real=True)
# 159 count roots numerically
f=lambda T: np.cos(2*T)*np.cos(T/2)+np.cos(5*T/2)-2*np.cos(5*T/2)**3
# exact: lhs = cos2θcosθ/2 + cos5θ/2 ; 2cos2θ cos θ/2 = cos5θ/2+cos3θ/2
expr=cos(2*th)*cos(th/2)+cos(5*th/2)-2*cos(5*th/2)**3
T=np.linspace(-np.pi/2,np.pi/2,2000001);v=f(T)
print('159 sign changes',np.sum(np.sign(v[1:])!=np.sign(v[:-1])), 'near zeros', T[np.abs(v)<1e-9][:20])
# 160
a,d,n=symbols('a d n')
s=solve([a+5*d-7, 7*a+21*d-7],[a,d]);print(s)
nn=solve(Eq(n/2*(2*s[a]+(n-1)*s[d]),700),n);print(nn,[s[a]+(k-1)*s[d] for k in nn])
# 161
X,Y=symbols('X Y',real=True);z=X+I*Y
e=re(expand_complex((z-1)/(2*z+I)))*2-2
num=simplify(together(e));print('161',factor(numer(together(expand_complex(e)))))
