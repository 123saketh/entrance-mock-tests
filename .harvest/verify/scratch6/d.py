from sympy import *
t=symbols('t')
P=Matrix([5,1,-3])
def foot(A,d):
    tt=solve((A+t*d-P).dot(d),t)[0];return A+tt*d
for A2 in [Matrix([2,0,1]),Matrix([2,2,1]),Matrix([2,1,1])]:
  for A1 in [Matrix([1,2,0])]:
    Q=foot(A1,Matrix([1,1,1]));R=foot(A2,Matrix([1,1,1]))
    ar=((Q-P).cross(R-P)).norm()/2;print(A2.T,Q.T,R.T,simplify(4*ar**2))
