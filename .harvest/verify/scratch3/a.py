from sympy import *
from itertools import product
from math import comb
# 169
c=0
for d in product(range(8),repeat=5):
    n=int(''.join(map(str,d)))
    if n>50000 and d[0]+d[4]<=8: c+=1
print('169',c)
# 176
t=0
for b in range(6):
    g=5-b
    if g>3 or b>7: continue
    bb,gb=4-b,4-g
    if bb<0 or gb<0 or bb>6 or gb>5: continue
    t+=comb(7,b)*comb(3,g)*comb(6,bb)*comb(5,gb)
print('176',t)
# 177
l,m=symbols('l m')
M=Matrix([[1,2,-3],[2,l,5],[14,3,m]]); 
Mx=Matrix([[2,2,-3],[5,l,5],[33,3,m]])
print('177',solve([M.det(),Mx.det()],[l,m]))
# 187
a=Matrix([3,-1,2]); b=a.cross(Matrix([1,0,-2])); c=b.cross(Matrix([0,0,1]))
v=c-Matrix([0,2,0]); print('187',simplify(v.dot(a)/a.norm()))
# 194: focus = reflection: vertex midpoint of focus and foot on directrix
x,y=symbols('x y')
V=Matrix([Rational(3,2),3]); n=Matrix([1,2]); d=(V.dot(n))/5
foot=V-d*n; F=2*V-foot
eq=expand(5*((x-F[0])**2+(y-F[1])**2)-(x+2*y)**2)
print('194',F.T,eq)
# 226
P=Matrix([1,4,0]); t,s=symbols('t s'); Q=P+t*Matrix([4,2,3]); L=Matrix([2,6,3])+s*Matrix([2,3,4])
sol=solve(list(Q-L),[t,s]); print('226',sol, ((Q-P).subs(sol)).norm())
# 231
p1=Matrix([2,1,-3]);d1=Matrix([1,2,3]);p2=Matrix([-1,-3,-5]);d2=Matrix([2,4,5])
nn=d1.cross(d2); print('231',((p2-p1).dot(nn))**2/nn.dot(nn))
# 233
r=symbols('r',positive=True)
Pp=Matrix([-1,-1,2]);Qq=Matrix([5,5,10]);A=(r*Qq+Pp)/(r+1)
print('233',solve(Qq.dot(A)-Rational(1,5)*(Pp.cross(A)).dot(Pp.cross(A))-10,r))
# 234
xx=symbols('xx'); # chord: x/4 + y/4 = 1/4+1/8 -> x+y=3/2
sols=solve([x**2/4+y**2/2-1,x+y-Rational(3,2)],[x,y]); 
print('234',simplify(sqrt((sols[0][0]-sols[1][0])**2+(sols[0][1]-sols[1][1])**2)))
# 240
B=Matrix([[0,4,2],[1,1,1],[0,3,2]]); C=Matrix([[0,0,1],[0,1,0],[1,0,0]])
Am=C*B.inv(); print('240',Am, Am[1,2])
