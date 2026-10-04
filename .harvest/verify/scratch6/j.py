from sympy import *
l,a,b,m,n,x,y=symbols('lambda a b m n x y')
A1=Matrix([1,2,3]);d1=Matrix([2,3,4]);A2=Matrix([l,4,5]);d2=Matrix([3,4,5])
N=d1.cross(d2);ls=solve(Eq(((A2-A1).dot(N))**2*6,N.dot(N)),l);print(ls)
L1,L2=ls
D,E,F=symbols('D E F')
eqs=[L1**2+L2**2+D*L1+E*L2, L1**2+L2**2+D*L2+E*L1]
s=solve(eqs,[D,E]);print('201 r',sqrt((s[D]/2)**2+(s[E]/2)**2))
# 202
M=Matrix([[1,16,13],[-1,-1,2],[-2,-14,-8]])
s=solve(list(Matrix([[4,a,b]])*M),[a,b]);print(s)
w=(-1+sqrt(3)*I)/2
# guess: 4/alpha^4 + a/alpha + b/alpha^2 =3 ? 
print(simplify(expand(4/w**4+s[a]/w+s[b]/w**2)))
