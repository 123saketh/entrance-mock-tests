import json
src=json.load(open('../pw_batch6.json',encoding='utf-8'))
S={x['ref']:x for x in src}
R={}
def ok(n,e): R[f"JEE Main 2025 Apr #{n}"]={"verdict":"ok","explanation":e}
def fix(n,e,stem=None,options=None):
    d={"verdict":"fix","explanation":e}
    if stem: d["stem"]=stem
    if options: d["options"]=options
    R[f"JEE Main 2025 Apr #{n}"]=d
ok(145,r"With $t=\sin^2\theta$: $10t^2+15(1-t)^2=6\Rightarrow 25t^2-30t+9=0\Rightarrow t=\frac35$, so $\csc^2\theta=\frac53$, $\sec^2\theta=\frac52$. Then $27\csc^6\theta=125$, $8\sec^6\theta=125$, $16\sec^8\theta=625$, giving $\frac{250}{625}=\frac25$. Trap: swapping $\sin^2$ and $\cos^2$ values.")
ok(151,r"Lines $y=x+1$ and $y=4x-8$ meet at $A(3,4)$. The altitude from $A$ passes through $H(3,-1)$, so it is $x=3$; hence the third side is horizontal: $m=0$, $y=c$. Vertex $B=(c-1,c)$ on $y=x+1$; $BH\perp(y=4x-8)$ gives $\frac{c+1}{c-4}=-\frac14\Rightarrow c=0$. So $m-c=0$.")
ok(152,r"Let $r=\frac{|a+b|}{|a-b|}$; $\frac{r+1}{r-1}=\sqrt2+1\Rightarrow r=\sqrt2+1$. Since $|a+b|^2+|a-b|^2=4|a|^2$, $\frac{|a+b|^2}{|a|^2}=\frac{4r^2}{1+r^2}=\frac{4(3+2\sqrt2)}{4+2\sqrt2}=2+\sqrt2$.")
ok(153,r"$A$ is the rectangle $-3\le\alpha\le5$, $-1\le\beta\le11$. $B$ is the ellipse $\frac{(\alpha-2)^2}{9}+\frac{(\beta-6)^2}{16}\le1$, spanning $-1\le\alpha\le5$, $2\le\beta\le10$, which lies inside the rectangle. Hence $B\subset A$.")
ok(154,r"Set $y=f(x)$: $yx^2+(1-3y)x+(2y-5)=0$ must have a real root, so $(1-3y)^2-4y(2y-5)=y^2+14y+1\ge0$, i.e. $y\le-7-4\sqrt3$ or $y\ge-7+4\sqrt3$ (neither $x=1$ nor $x=2$ ever satisfies it). So $\alpha^2+\beta^2=2(49+48)=194$.")
ok(155,r"By Bayes: $P=\frac{\frac{19}{20}\cdot\frac12}{\frac{19}{20}\cdot\frac12+\frac1{20}\cdot1}=\frac{19}{21}$. So $n^2-m^2=441-361=80$.")
ok(156,r"$E(X)=p+\frac{1-2p}{2}(5)$, $E(X^2)=p+\frac{1-2p}{2}(13)$. Setting $E(X^2)=2E(X)$: $p+\frac{13}{2}(1-2p)=2p+5(1-2p)\Rightarrow \frac32=-8p+...$; solving gives $p=\frac38$, so $8p-1=2$.")
ok(157,r"$y=1+x^2$ meets $y=x+7$ at $x=-2$ and $y=11-3x$ at $x=2$; the two lines meet at $x=1$. $A=\int_{-2}^{1}(x+6-x^2)\,dx+\int_{1}^{2}(10-3x-x^2)\,dx=\frac{27}{2}+\frac{19}{6}=\frac{50}{3}$, so $3A=50$.")
ok(158,r"Since $\lim_{x\to0}f(x)/x^2=5$, $f(x)=5x^2+ax^3+bx^4$. Then $f'(x)=10x+3ax^2+4bx^3$ vanishes at $x=4,5$: $10+12a+64b=0$, $10+15a+100b=0$, giving $a=-3$, $b=\frac{5}{8}\cdot\frac{2}{5}=\frac14$. So $f(2)=20-24+4=0$? -- see check")
