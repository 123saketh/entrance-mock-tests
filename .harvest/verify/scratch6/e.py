from sympy import *
x,y,z,l,mu,r,a,t=symbols('x y z lambda mu r a t',real=True)
# 169
M=Matrix([[1,5,-1],[4,3,-3],[24,1,l]]);print(solve(M.det(),l))
sol=solve([x+5*y-z-1,4*x+3*y-3*z-7],[x,z]);print(sol, simplify(sol[x]+y+sol[z]))
cnt=[]
for yy in range(-200,200):
    xx=sol[x].subs(y,yy);zz=sol[z].subs(y,yy)
    if xx.is_integer and zz.is_integer and 7<=xx+yy+zz<=77: cnt.append((xx,yy,zz))
print('169',len(cnt),cnt)
# 170
rr=solve(Eq(r**6,15309/21),r);print(rr)
# 176 numeric
import mpmath as mp
f=lambda X: mp.tan(5*X**(mp.mpf(1)/3))*mp.log(1+3*X**2)/((mp.atan(3*mp.sqrt(X)))**2*(mp.exp(5*X**(mp.mpf(4)/3))-1))
mp.mp.dps=50
print('176 at inf',f(mp.mpf('1e6')))
g=lambda X: mp.tan(5*X**(mp.mpf(1)/3))*mp.log(1+3*X**2)/((mp.atan(3*mp.sqrt(X)))**2*(mp.exp(5*X**(mp.mpf(4)/3))-1))
print('176 at 0',g(mp.mpf('1e-12')))
