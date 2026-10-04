from sympy import *
l,mu,x,y=symbols('lambda mu x y')
M=Matrix([[2,3,5],[7,3,-2],[12,3,-(4+l)]]);ls=solve(M.det(),l);print(ls)
Mz=Matrix([[2,3,9],[7,3,8],[12,3,16-mu]]);ms=solve(Mz.det(),mu);print(ms)
L=ls[0];Mu=ms[0];print('192 r',abs(4*L-3*Mu)/5)
# 194
th=asin(sqrt(65)/9);c=cos(th);print(c)
ca=3+6*c;cb=3*c+6;print('194',simplify(9*ca-3*cb))
# 195
A=solve([3*y-x-2,x+y-2],[x,y]);print(A)
B=(-2,0);C=(2,0)
# orthocentre: x=A.x ; altitude from B perpendicular to AC (slope -1) => slope 1 through B
P=(A[x], A[x]+2);print(P, Rational(1,2)*4*abs(P[1]))
