from sympy import *
x,l,m,t=symbols('x l m t',real=True)
# 6
a=Matrix([-3,2,4]);b=Matrix([2,1,3]);P=Matrix([7,6,2]);Q=Matrix([5,3,4])
n=a.cross(b);print('6',abs((P-Q).dot(n))/n.norm(), n.norm())
# 8
M=Matrix([[2,l,3],[3,2,-1],[4,5,m]]);B=Matrix([5,7,9])
eqs=[M.det()]+[M.copy().col_insert(0,B).col_del(i+1) for i in []]
d1=M.det();Mx=M.copy();Mx[:,0]=B;My=M.copy();My[:,1]=B;Mz=M.copy();Mz[:,2]=B
print('8',solve([d1,Mx.det(),My.det(),Mz.det()],[l,m]))
# 9
th=symbols('th')
c=symbols('c');print('9',solve(sqrt(3)*c**2-2*(sqrt(3)-1)*c-4,c))
import numpy as np
for cv in [2,-2/np.sqrt(3)]:
  sv=1/cv; xs=np.linspace(-7*np.pi/6,4*np.pi/3,2000001); f=np.sin(xs)-sv
  print(cv,np.sum(np.sign(f[1:])!=np.sign(f[:-1])), f[0],f[-1])
# 13
I=4*Integral(1/(sqrt(3+x**2)+sqrt(1+x**2)),(x,0,1)).evalf(30)-3*log(sqrt(3))
print('13',I,[N(2+s1*sqrt(2)+s2*log(1+sqrt(2))) for s1 in(1,-1) for s2 in (1,-1)])
# 15
S=sum(Rational(10**(r+1)-1,10**r)*binomial(11,r+1) for r in range(11))
for al in [15,11,24,20]: print('15',al,S==Rational(al**11-11**11,10**10))
# 18
c1,c2,c3=symbols('c1:4');C=Matrix([c1,c2,c3]);a=Matrix([2,-3,1]);b=Matrix([3,2,5])
sol=solve(list((a-C).cross(b)-Matrix([-18,-3,12]))+[a.dot(C)-3],[c1,c2,c3],dict=True);print('18',sol)
for s in sol: print(abs(a.dot(b.cross(C.subs(s)))))
# 20
print('20',rem(x**5,x**3-2*x**2-4*x+4,x))
# 30
al,be=symbols('al be')
for s in solve([(al-1)*be+6,al+be-1],[al,be],dict=True):
  if s[al]>0:
    A=Matrix([[s[al]-1,-1],[6,s[be]]]);print('30',s,(eye(2)+A)**8)
# 32
xs=np.linspace(-2*np.pi,2*np.pi,4000001);f=2*np.sqrt(2)*np.cos(xs)**2+(2-np.sqrt(6))*np.cos(xs)-np.sqrt(3)
print('32',np.sum(np.sign(f[1:])!=np.sign(f[:-1])),solve(2*sqrt(2)*c**2+(2-sqrt(6))*c-sqrt(3),c))
# 40
M=Matrix([[3,1,be],[2,al,-1],[1,2,1]]);B=Matrix([3,-3,4])
Mx=M.copy();Mx[:,0]=B;My=M.copy();My[:,1]=B;Mz=M.copy();Mz[:,2]=B
print('40',[(s,22*s[be]-9*s[al]) for s in solve([M.det(),Mx.det(),My.det(),Mz.det()],[al,be],dict=True)])
# 42
P=Matrix([0,2,3]);A0=Matrix([-3,1,-4]);d=Matrix([5,2,3])
h=(P-A0).cross(d).norm()/d.norm();ar=simplify(Rational(5,2)*h);print('42',ar,N(ar),N(5*sqrt(21)/2))
