from sympy import *
x,y=symbols('x y')
x0=1+log(3)/2
g=(exp(x-1)+exp(1-x))/2; f=exp(x-1)-exp(1-x)
A=integrate(g,(x,0,1))+integrate(g-f,(x,1,x0))
print(N(A), N(2-sqrt(3)+(E-1/E)/2))
# region 45: for y in [0,1], x from max(3y,2-y) to 9/4
A2=integrate(Rational(9,4)-(2-y),(y,0,Rational(1,2)))+integrate(Rational(9,4)-3*y,(y,Rational(1,2),Rational(3,4)))
print(A2)
from itertools import combinations
from fractions import Fraction as F
E1={1,2,3};F1={1,3,4};G1={2,3,4,5}
num=F(0);den=F(0)
for S1 in combinations(E1,2):
  E2=E1-set(S1);F2=F1|set(S1)
  for S2 in combinations(sorted(F2),2):
    G2=G1|set(S2)
    for S3 in combinations(sorted(G2),2):
      p=F(1,3)/len(list(combinations(F2,2)))/len(list(combinations(G2,2)))
      if E2|set(S3)==E1:
        den+=p
        if set(S1)=={1,2}: num+=p
print(num/den)
