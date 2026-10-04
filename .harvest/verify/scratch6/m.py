from sympy import *
x=symbols('x',real=True)
v=integrate(pi**2*x*sin(pi*x),(x,-1,1))+integrate(-pi**2*x*sin(pi*x),(x,1,Rational(3,2)));print('211',simplify(v))
# 213
print('213',binomial(12,3)-binomial(5,3))
# 214
th=symbols('theta',real=True)
e=1+10*re(expand_complex((2*cos(th)+I*sin(th))/(cos(th)-3*I*sin(th))))
e=simplify(e);print(e)
import numpy as np
f=lambdify(th,e);T=np.linspace(0,2*np.pi,400001);vv=f(T)
idx=np.where(np.sign(vv[1:])!=np.sign(vv[:-1]))[0];print(T[idx]/np.pi, sum((T[idx]/np.pi)**2))
# 215
print('215',len([r for r in range(1017) if (1016-r)%2==0 and r%8==0]))
