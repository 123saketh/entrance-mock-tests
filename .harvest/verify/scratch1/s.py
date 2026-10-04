from sympy import *
# 3
A=Matrix([1,2,1]);B=Matrix([1,3,-2]);C=Matrix([2,1,-1])
n=(B-A).cross(C-A); area=n.norm()/2
h=Rational(1)*sqrt(805)/(6*sqrt(2))*3/area; h=simplify(h)
AE=sqrt(Rational(110,9)-h**2); M=(B+C)/2; u=(M-A)/(M-A).norm()
print('3',simplify(h),simplify(AE),(M-A).norm(), simplify(A+AE*u).T)
# 9
t=symbols('t'); L=Matrix([3+7*t,2-t,-2-2*t]); Q=Matrix([10,-3,-1]); R=Matrix([3,-2,1])
ts=solve((Q-L).dot(Matrix([7,-1,-2])),t)[0]; P=L.subs(t,ts)
print('9',P.T,(Q-P).dot(R-P),(Q-R).dot(P-R),(P-Q).dot(R-Q))
for X,Y,Z in [(P,Q,R)]: print(sqrt(((Y-X).cross(Z-X)).norm()**2)/2)
# 12
l=symbols('l');M=Matrix([[l-1,l-4,l],[l,l-1,l-4],[l+1,l+2,-(l+2)]]);bb=Matrix([5,7,9])
for r in solve(M.det(),l):
  Mr=M.subs(l,r); print('12',r,Mr.rank(),Mr.row_join(bb).rank(), r**2+r)
# 40
a,b=symbols('a b');M=Matrix([[1,1,2],[2,3,a],[-1,-3,b]]);bb=Matrix([6,a+1,2*b])
print('40',factor(M.det()))
for i in range(3):
  Mi=M.copy();Mi[:,i]=bb;print(factor(Mi.det()))
# 54
l,m=symbols('l m');M=Matrix([[2,-1,1],[5,l,3],[100,-47,m]]);bb=Matrix([4,12,212])
eqs=[M.det()]+[ (lambda Mi:(Mi.__setitem__((slice(None),i),bb),Mi.det())[1])(M.copy()) for i in range(3)]
print('54',solve(eqs,[l,m]))
# 53
a2,b2=symbols('a2 b2',positive=True)
sols=solve([3/a2+1/(4*b2)-1, a2-3*(1-b2/a2)-Rational(7,4)],[a2,b2],dict=True)
es=[]
for s in sols:
  if s[a2]>s[b2]: es.append(sqrt(1-s[b2]/s[a2])); print(s)
print('53',[nsimplify(e) for e in es], N(abs(es[0]-es[1])) if len(es)>1 else None, N((3-2*sqrt(2))/(2*sqrt(3))))
# 59
x=symbols('x'); r=solve(2*x**2-3*x-2*I,x); al,be=r
E=(al**19+be**19+al**11+be**11)/(al**15+be**15); E=nsimplify(N(E,50),rational=True)
print('59',E, 16*re(E)*im(E))
