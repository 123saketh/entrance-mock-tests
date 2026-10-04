from sympy import *
l,m=symbols('l m')
for L,Mv in [(-1,13),(Rational(-10,3),Rational(-9,2))]:
    M=Matrix([[1,2,-3],[2,L,5],[14,3,Mv]]); b=Matrix([2,5,33])
    print([M.det()]+[(lambda K:(K.__setitem__((slice(None),i),b),K.det())[1])(M.copy()) for i in range(3)])
x,y,t,s=symbols('x y t s')
P=Matrix([1,4,0])
for d in [(1,2,3),(4,2,3),(2,2,3),(4,1,3)]:
    Q=P+t*Matrix(d); L=Matrix([2,6,3])+s*Matrix([2,3,4])
    sol=solve(list(Q-L),[t,s]); print(d,sol, ((Q-P).subs(sol)).norm() if sol else None)
# 230: A on x-y+2=0: A=(a,a+2), B=(b,-2). P=(A+2B)/3
a,b=symbols('a b')
X=(a+2*b)/3; Y=(a+2-4)/3
asol=solve(Y-y,a)[0]; bsol=solve(X.subs(a,asol)-x,b)[0]
eq=expand(((asol-bsol)**2+(asol+2+2)**2-64)*9/ 9)
print(eq, expand(eq*Rational(9,10)))
