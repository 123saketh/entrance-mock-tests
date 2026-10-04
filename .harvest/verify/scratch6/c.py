from sympy import *
x,y,t,b,a=symbols('x y t b a',real=True)
P=Matrix([5,1,-3])
def foot(A,d):
    tt=solve((A+t*d-P).dot(d),t)[0];return A+tt*d
Q=foot(Matrix([1,2,0]),Matrix([1,1,1]));R=foot(Matrix([2,2,1]),Matrix([1,1,1]))
ar=((Q-P).cross(R-P)).norm()/2;print('166',Q.T,R.T,simplify(4*ar**2))
# 167
print('167',[s for s in solve(x*abs(x-2)+3*abs(x-3)+1,x)])
for lo,hi,ex in [(-oo,2,x*(2-x)+3*(3-x)+1),(2,3,x*(x-2)+3*(3-x)+1),(3,oo,x*(x-2)+3*(x-3)+1)]:
    print(lo,hi,[r for r in solve(ex,x)])
# 168
# hyperbola e2^2=1+b^2/16; ellipse a<5? y-major: e1^2=1-a^2/25
for case in ['a<5']:
    e1s=1-a**2/25
