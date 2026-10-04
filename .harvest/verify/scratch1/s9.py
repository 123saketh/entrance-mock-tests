from sympy import *
t=symbols('t')
R=Matrix([3,-2,1])
for Q in [Matrix([10,-3,-1]),Matrix([5,-3,-1])]:
 for p0 in [(3,2,-2),(3,-2,1),(3,2,-1),(3,-2,-2),(3,2,1)]:
  for d in [(7,-1,-2),(7,-1,2),(7,1,-2)]:
   L=Matrix(p0)+t*Matrix(d)
   ts=solve((Q-L).dot(Matrix(d)),t)[0];P=L.subs(t,ts)
   ar=simplify(((Q-P).cross(R-P)).norm()/2)
   print(Q.T,p0,d,P.T,ar)
