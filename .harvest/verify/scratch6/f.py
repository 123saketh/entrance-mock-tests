from sympy import *
x,y,al,a,b=symbols('x y alpha a b',real=True)
# 177
A1=Matrix([1,2,3]);d1=Matrix([2,3,4]);A2=Matrix([0,0,5]);d2=Matrix([1,al,1])
n=d1.cross(d2);sd=(A2-A1).dot(n)/n.norm()
s=solve(Eq(((A2-A1).dot(n))**2*6,25*n.dot(n)),al);print('177',s,sum(s))
# 178
f=x**3+a*x**2+b*log(abs(x),2)+1
fp=3*x**2+2*a*x+b/(x*log(2))
s=solve([fp.subs(x,-1),fp.subs(x,2)],[a,b]);print(s)
F=f.subs(s)
# with log 2 =0.7 ; sub log(2)->0.7 in b and log
Fn=x**3+s[a]*x**2+(s[b]).subs(log(2),0.7)*log(-x)/0.7+1
Fn=simplify(Fn);print(Fn)
pts=[-2,-1,-0.5]+[r for r in solve(diff(Fn,x),x) if r.is_real and -2<=r<=-0.5]
vals=[Fn.subs(x,p).evalf() for p in pts];print(pts,vals,abs(max(vals)+min(vals)))
