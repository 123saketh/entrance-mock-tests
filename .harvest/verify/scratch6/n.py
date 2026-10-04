from sympy import *
import math
acot=lambda v: math.atan(1/v) if v>0 else math.pi+math.atan(1/v)
t2=math.tan(2);th=math.tan(0.5)
v=acot((math.sqrt(1+t2**2)-1)/t2)-acot((math.sqrt(1+th**2)+1)/th);print('218',v,[math.pi-1.25,math.pi-1.5,math.pi+1.5,math.pi+2.5])
p,q=symbols('p q')
A=Matrix([[2,2+p,2+p+q],[4,6+2*p,8+3*p+2*q],[6,12+3*p,20+6*p+3*q]]);d=factor(A.det());print('219',d)
D=(3**3*d)**4;print(factorint(D))
