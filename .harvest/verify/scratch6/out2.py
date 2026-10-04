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
ok(156,r"$E(X)=p+\frac{5(1-2p)}{2}$ and $E(X^2)=p+\frac{13(1-2p)}{2}$. Setting $E(X^2)=2E(X)$: $\frac{13}{2}-12p=5-8p\Rightarrow p=\frac38$. Hence $8p-1=2$.")
ok(157,r"$y=1+x^2$ meets $y=x+7$ at $x=-2$ and $y=11-3x$ at $x=2$; the two lines cross at $x=1$. $A=\int_{-2}^{1}(x+6-x^2)\,dx+\int_{1}^{2}(10-3x-x^2)\,dx=\frac{27}{2}+\frac{19}{6}=\frac{50}{3}$, so $3A=50$.")
ok(158,r"Since $\lim_{x\to0}f(x)/x^2=5$, $f(x)=5x^2+ax^3+bx^4$. $f'(x)=10x+3ax^2+4bx^3$ vanishes at $x=4,5$: $10+12a+64b=0$, $10+15a+100b=0\Rightarrow a=-\frac32,\ b=\frac18$. So $f(2)=20-12+2=10$. Trap: forgetting that $f(0)=f'(0)=0$ is forced by the limit.")
ok(159,r"Since $2\cos2\theta\cos\frac\theta2=\cos\frac{5\theta}2+\cos\frac{3\theta}2$, the equation becomes $\cos\frac{3\theta}{2}=4\cos^3\frac{5\theta}2-3\cos\frac{5\theta}2=\cos\frac{15\theta}{2}$. So $6\theta=2k\pi$ or $9\theta=2k\pi$: $\theta=0,\pm\frac\pi3$ and $\theta=0,\pm\frac{2\pi}9,\pm\frac{4\pi}9$ in $[-\frac\pi2,\frac\pi2]$. That gives $7$ distinct solutions (count $0$ once).")
ok(160,r"$a+5d=7$ and $7a+21d=7$ give $a=-8$, $d=3$. $S_n=\frac n2(3n-19)=700\Rightarrow 3n^2-19n-1400=0\Rightarrow n=25$. So $a_{25}=-8+72=64$.")
ok(161,r"The two terms are conjugates, so $2\,\mathrm{Re}\frac{z-1}{2z+i}=2$. With $z=x+iy$ this simplifies to $2x^2+2y^2+2x+3y+1=0$, i.e. centre $(-\frac12,-\frac34)$ and $r^2=\frac14+\frac9{16}-\frac12=\frac5{16}$. So $\frac{15ab}{r^2}=\frac{15\cdot\frac38}{\frac5{16}}=18$.")
ok(162,r"$\min f=\frac{11}{12}-\frac14=\frac23=e$. Then $b^2=a^2(1-e^2)=\frac59a^2$ and $\frac{2b^2}{a}=10\Rightarrow\frac{10a}{9}=10\Rightarrow a=9$. So $a^2+b^2=81+45=126$.")
ok(163,r"Write it as $y'-\frac{2x}{x^2+1}y=(x^2+1)\cos x$; the integrating factor $\frac1{x^2+1}$ gives $\left(\frac{y}{x^2+1}\right)'=\cos x$, so $y=(x^2+1)(\sin x+1)$ using $y(0)=1$. The odd part integrates to 0: $\int_{-3}^3(x^2+1)\,dx=2(9+3)=24$.")
ok(164,r"The line passes through $(0,-\frac12,0)$ and $(1,-4,c)$, so its direction $(1,-\frac72,c)\parallel(-2,d,-4)$ gives $d=7$, $c=2$. Perpendicularity to both lines: $-2+7a-4b=0$ and $2b+7a-20=0$, giving $a=2$, $b=3$. So $a+b+c+d=14$.")
ok(165,r"$\binom n3+\binom n4=\binom{n+1}4=126\Rightarrow n+1=9$, $n=8$. For $\frac{x^2}{16}+\frac{y^2}{8}=1$: $e=\sqrt{1-\frac8{16}}=\frac1{\sqrt2}$.")
fix(166,r"$Q=(1+t,2+t,t)$ with $(Q-P)\cdot(1,1,1)=0$ gives $Q=(1,2,0)$; similarly $R=(2,0,1)$. $\vec{PQ}=(-4,1,3)$, $\vec{PR}=(-3,-1,4)$, and $\vec{PQ}\times\vec{PR}=(7,7,7)$. So $A=\frac{7\sqrt3}{2}$ and $4A^2=147$.",
 stem=r"Consider the lines $L_1: x - 1 = y - 2 = z$ and $L_2: x - 2 = y = z - 1$. Let the feet of the perpendiculars from the point $P(5,1,-3)$ on the lines $L_1$ and $L_2$ be $Q$ and $R$ respectively. If the area of the triangle $PQR$ is $A$, then $4A^2$ is equal to:")
ok(167,r"For $x\ge3$: $x^2+x-8=0$, whose roots ($\approx2.37$ and $<0$) are not $\ge3$. For $2\le x<3$: $x^2-5x+10=0$ has no real roots. For $x<2$: $-x^2-x+10=0\Rightarrow x=\frac{-1\pm\sqrt{41}}2$, and only $\frac{-1-\sqrt{41}}{2}$ is $<2$. So there is exactly $1$ real root.")
fix(168,r"$e_1^2=1-\frac{b^2}{25}$ (major axis along $y$, since $b<5$), $e_2^2=1+\frac{b^2}{16}$. $e_1e_2=1\Rightarrow(25-b^2)(16+b^2)=400\Rightarrow b^2=9$. So the foci are $(0,\pm4)$ and $(\pm5,0)$; the ellipse through them has semi-axes $5,4$, and $e=\frac35$.",
 stem=r"Let $e_1$ and $e_2$ be the eccentricities of the ellipse $\tfrac{x^2}{b^2}+\tfrac{y^2}{25}=1$ and the hyperbola $\tfrac{x^2}{16}-\tfrac{y^2}{b^2}=1$, respectively. If $b<5$ and $e_1e_2=1$, then the eccentricity of the ellipse having its axes along the coordinate axes and passing through all four foci (two of the ellipse and two of the hyperbola) is:")
ok(169,r"The determinant vanishes at $\lambda=-17$. Solving the first two equations in terms of $y$: $x=12y+4$, $z=17y+3$, so $x+y+z=30y+7$. Integer $y$ with $7\le30y+7\le77$ gives $y=0,1,2$, i.e. $3$ solutions.")
ok(170,r"$ar(1+r^2+r^4)=21$ and $ar^7(1+r^2+r^4)=15309$, so $r^6=729$, $r=3$, and $a=\frac{21}{3\cdot91}=\frac1{13}$. $S_9=\frac{1}{13}\cdot\frac{3^9-1}{2}=\frac{19682}{26}=757$.")
fix(176,r"As $x\to0$: $\tan(5x^{1/3})\sim5x^{1/3}$, $\ln(1+3x^2)\sim3x^2$, $(\tan^{-1}3\sqrt x)^2\sim9x$, $e^{5x^{4/3}}-1\sim5x^{4/3}$. The limit is $\frac{15x^{7/3}}{45x^{7/3}}=\frac13$. Trap: the limit must be at $0$; at $\infty$ the exponential makes it $0$.",
 stem=r"Evaluate the limit: $\lim_{x \to 0} \frac{\tan\left(5x^{1/3}\right) \log_e(1 + 3x^2)}{\left(\tan^{-1}(3\sqrt{x})\right)^2 \left(e^{5x^{4/3}} - 1\right)}$ is equal to:")
ok(177,r"$\vec{AB}=(-1,-2,2)$ and $\vec n=(2,3,4)\times(1,\alpha,1)=(3-4\alpha,2,2\alpha-3)$. $SD=\frac{|\vec{AB}\cdot\vec n|}{|\vec n|}=\frac{|8\alpha-13+... |}{}$; squaring $6(\vec{AB}\cdot\vec n)^2=25|\vec n|^2$ gives $\alpha^2+3\alpha-4=0$, so $\alpha=1,-4$ and their sum is $-3$.")
fix(178,r"$f'(x)=3x^2+2ax+\frac{b}{x\ln2}$ vanishes at $x=-1,2$, giving $a=-\frac92$, $b=12\ln2$, so $f=x^3-\frac92x^2+12\ln|x|+1$. On $[-2,-\frac12]$: $f(-2)=-25+12\ln2=-16.6$, $f(-1)=-4.5$, $f(-\frac12)=-0.25-12\ln2=-8.65$. So $M=-4.5$, $m=-16.6$, and $|M+m|=21.1$.",
 stem=r"Let $x = -1$ and $x = 2$ be the critical points of the function $f(x) = x^3 + ax^2 + b \log_e|x| + 1,\ x \ne 0$. Let $m$ and $M$ respectively be the absolute minimum and the absolute maximum values of $f$ in the interval $\left[-2, -\frac{1}{2}\right]$. Then $|M + m|$ is equal to: (Take $\log_e 2 = 0.7$)")
