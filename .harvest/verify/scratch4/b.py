from sympy import *
import numpy as np
a=symbols('a')
M=Matrix([[1,a,1],[2,1,0],[a,1,2]])-eye(3)
print('44',solve(M.det()+4,a))
for av in solve(M.det()+4,a):
  A=M.subs(a,av); X=(av+1)*((av-1)*A).adjugate(); print(av,factorint(X.det()))
# 45
t=symbols('t',positive=True)
# P=(t^2,2t), slope 2/t = sqrt3
tv=2/sqrt(3);P=(tv**2,2*tv);C=((P[0]+1)/2,P[1]/2);print('45',C,simplify(5*C[1]**2))
# 65
xs=np.linspace(-2*np.pi,2.5*np.pi,4000001);f=(4-np.sqrt(3))*np.sin(xs)-2*np.sqrt(3)*np.cos(xs)**2+4/(1+np.sqrt(3))
print('65',np.sum(np.sign(f[1:])!=np.sign(f[:-1])),f[0],f[-1])
s=symbols('s');print(solve((4-sqrt(3))*s-2*sqrt(3)*(1-s**2)+4/(1+sqrt(3)),s))
# 66
ts=np.linspace(-10,10,2000001);d=np.sqrt(4*ts**4+(4*ts+6)**2);print('66',d.min()-1,2*np.sqrt(2)-1)
# 68
l=symbols('l');Pt=Matrix([7,10,11])+l*Matrix([2,-3,6])
sol=solve([(Pt[0]-4)/1-(Pt[2]-2)/3, Pt[1]-4],l);print('68',sol)
