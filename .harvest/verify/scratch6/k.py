from sympy import *
x,y=symbols('x y',real=True)
r1=solve(Abs(x+2)**2+Abs(x-2)-2,x);r2=solve(x**2-2*Abs(x-3)-5,x);print('206',r1,r2,sum(v**2 for v in r1)+sum(v**2 for v in r2))
r1b=solve(Abs(x+2)**2+Abs(x+2)-2,x);print('206b',r1b, sum(v**2 for v in r1b)+sum(v**2 for v in r2))
# 207 diag intersection
s=solve([(sqrt(3)+1)*x+(sqrt(3)-1)*y,(sqrt(3)-1)*x-(sqrt(3)+1)*y+8*sqrt(3)],[x,y]);print(s)
d=sqrt(s[x]**2+s[y]**2);print('207 a^2',simplify((2*d)**2/2), simplify(abs(8*sqrt(3))/sqrt((sqrt(3)-1)**2+(sqrt(3)+1)**2)))
f=lambda u: exp(u)  # positive
I1=Integral(2*x*f(2*x*(1-2*x)),(x,-Rational(1,2),1)).evalf()
I2=Integral(f(x*(1-x)),(x,-1,Rational(1,2))).evalf()
print('208',I1,I2,I2/I1)
