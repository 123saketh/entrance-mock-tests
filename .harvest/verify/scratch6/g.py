from sympy import *
x=symbols('x',positive=True);Y=Function('y')
ode=Eq(x*(x**2+exp(x))*Y(x).diff(x)+exp(x)*(x-2)*Y(x)-x**3,0)
s=dsolve(ode,Y(x),ics={Y(1):0});print('181',simplify(s.rhs.subs(x,2)))
v=Integral((x+3)*sin(x)/(1+3*cos(x)**2),(x,0,pi/2)).evalf();print('185',v,[ (pi/sqrt(3)*(pi+1)).evalf(),(pi/sqrt(3)*(pi+2)).evalf(),(pi/(3*sqrt(3))*(pi+6)).evalf(),(pi/(2*sqrt(3))*(pi+4)).evalf()])
# 187
n=100;S=40*100;SS=100*(5.1**2+1600)
S2=S-50+40;SS2=SS-2500+1600;mu=S2/n;sig=sqrt(SS2/n-mu**2);print('187',mu,sig,10*(mu+sig))
