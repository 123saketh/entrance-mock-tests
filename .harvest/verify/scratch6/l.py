from sympy import *
x=symbols('x',real=True)
R=Rational
for fexpr in [lambda u: exp(u), lambda u: 1+u**2]:
  for (a,b) in [(-R(1,4),R(1,2)),(-R(1,2),1),(-R(1,4),R(3,4)),(-R(1,2),R(1,2))]:
    for (c,d) in [(-1,R(1,2)),(-1,2),(-R(1,2),R(3,2))]:
      I1=Integral(2*x*fexpr(2*x*(1-2*x)),(x,a,b)).evalf();I2=Integral(fexpr(x*(1-x)),(x,c,d)).evalf()
      print((a,b),(c,d),round(I2/I1,6))
