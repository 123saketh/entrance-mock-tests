from sympy import *
from itertools import product
for s in product([1,-1],repeat=6):
    p1=Matrix([2,1,-3]);d1=Matrix([1*s[0],2*s[1],3*s[2]]);p2=Matrix([-1,-3,-5]);d2=Matrix([2*s[3],4*s[4],5*s[5]])
    nn=d1.cross(d2); v=((p2-p1).dot(nn))**2/nn.dot(nn); v=nsimplify(v)
    print(s, v, fraction(v)[0]+fraction(v)[1])
