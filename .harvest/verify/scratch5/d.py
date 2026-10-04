from sympy import *
from math import comb
x,y,t,s,a,b,l,m=symbols('x y t s a b l m')
# 126
f=lambda x:(2*x+3)/(5*x+2); g=lambda x:(2-3*x)/(1-x)
vals=[f(g(Rational(v))) for v in [2,4]]; print('126',vals, 1/abs(vals[0]-vals[1]))
# 127
C=[(i,j) for i in range(-3,4) for j in range(-3,4) if 2*i*i+j*j<=4]; print('127 |C|',len(C))
# D: x^2+9y^2=144 and x^2+y^2>=25 -> whole ellipse (min dist 4 <5?) infinite? 
# 128
A=set(1+5*k for k in range(2025)); B=set(9+7*k for k in range(2025)); print('128',len(A|B))
# 129
tot=comb(16,12); fav=sum(comb(4,e)*comb(2,d)*comb(10,12-e-d) for e in (3,4) for d in (1,2)); print('129',Rational(fav,tot))
# 130
for n in range(2,20):
  if Rational(2**(2*n-3),2*n-2)==16: print('130 n',n, abs((2*n-1)+(n*n-4*n)-8)/sqrt(2))
# 131
al,be=symbols('al be')
a1=Matrix([3,al,3]);b1=Matrix([3,-1,1]);a2=Matrix([-3,-7,be]);b2=Matrix([-3,2,4]); nn=b1.cross(b2)
print('131', nn, nn.norm(), expand((a2-a1).dot(nn)))
