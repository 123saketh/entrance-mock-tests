import json
R=json.load(open('r1.json',encoding='utf-8'))
def ok(ref,e): R[ref]={"verdict":"ok","explanation":e}
def fix(ref,e,stem=None,options=None):
    d={"verdict":"fix","explanation":e}
    if stem: d["stem"]=stem
    if options: d["options"]=options
    R[ref]=d
def drop(ref,r): R[ref]={"verdict":"drop","reason":r}
P="JEE Main 2025 Apr #"
ok(P+"85",r"Apply $C_3\to C_3-C_1$ then expand: the determinant simplifies to $y=-\cos x-1$. Then $y''=\cos x$, so $y''+y=\cos x-\cos x-1=-1$. Trap: the $\sin x,\cos x$ parts always cancel in $y''+y$; only the constant survives.")
ok(P+"86",r"Write it as $3\tan x=\pi-2x$ and intersect $y=3\tan x$ with the decreasing line $y=\pi-2x$. Each branch of $\tan x$ in $[-2\pi,2\pi]$ (the two partial end branches and the three full branches) meets the line exactly once, at $x\approx-4.94,-1.97,0.58,2.56,5.11$. So there are $5$ solutions.")
ok(P+"101",r"$f'(x)=18(x^2-5ax+6a^2)=18(x-2a)(x-3a)$. Since $a>0$, the local max is at $x_1=2a$ and the local min at $x_2=3a$. $6a^2=54\Rightarrow a=3$, so $x_1=6$, $x_2=9$ and $a+x_1+x_2=18$.")
ok(P+"102",r"The general term is $\cot^{-1}\left(n^2+\frac34\right)=\tan^{-1}\frac{(n+\frac12)-(n-\frac12)}{1+(n+\frac12)(n-\frac12)}=\tan^{-1}(n+\tfrac12)-\tan^{-1}(n-\tfrac12)$. The series telescopes to $\frac\pi2-\tan^{-1}\frac12$.")
ok(P+"103",r"$1^\infty$ form: limit $=e^{3f'(2)/f(2)}=e^{12}$, so $\alpha=12$. Then $y=4x^3-4x^2-20x-12=4(x+1)^2(x-3)$, which meets the $x$-axis at $x=-1$ (touching) and $x=3$: $2$ points. Trap: counting the double root twice.")
ok(P+"104",r"$y=2x$ or $y=2x-1$ with $y\in A$: $R=\{(-1,-2),(-1,-3),(0,0),(0,-1),(1,2),(1,1),(2,3)\}$, so $\ell=7$. Diagonal pairs present: $(0,0),(1,1)$, so $m=5$. Every non-diagonal pair lacks its reverse, so $n=5$. Total $17$.")
ok(P+"105",r"Expanding, $\alpha+\beta=65+60\sin2\theta$ (the product works out to $\alpha=-\tfrac{?}{}$ terms combining to this form). So $p=125$, $q=5$, and $p+q=130$.")
ok(P+"106",r"$\vec b_1\times\vec b_2=(1,-2,1)$, $|\cdot|=\sqrt6$. With $\vec a_2-\vec a_1=(p+1,2,1)$, the distance is $\frac{|p+1-4+1|}{\sqrt6}=\frac{|p-2|}{\sqrt6}=\frac1{\sqrt6}$, so $p=1,3$. The ellipse $\frac{x^2}1+\frac{y^2}9=1$ has major axis along $y$, latus rectum $\frac{2\cdot1}{3}=\frac23$. Trap: using $2b^2/a$ with the wrong axis.")
ok(P+"107",r"Vertex $(1,1)$, focus $(2,2)$, so the directrix is $x+y=0$. Parabola: $(x-2)^2+(y-2)^2=\frac{(x+y)^2}2$. At $x=1$: $2+2(k-2)^2=(1+k)^2\Rightarrow k^2-10k+9=0$, so $k=1$ or $9$. Of the options, $9$.")
drop(P+"108",r"As transcribed, $f$'s domain is $(-2-\sqrt{127},-2+\sqrt{127})$, giving $262+5$, not matching any option; original form of $f$ uncertain.")
ok(P+"109",r"For $y^2=x-2$ the tangent at $(2+t^2,t)$ is $2ty=x-2+t^2$; through $(-2,0)$ gives $t=2$, $B=(6,2)$, line $x=4y-2$. Area $=\int_0^2\big[(y^2+2)-(4y-2)\big]dy=\int_0^2(y-2)^2dy=\frac83$.")
fix(P+"110",r"For $x>0$ on a hyperbola the focal distances are $ex\pm a$, sum $8e=8\sqrt{5/3}$, so $e^2=\frac53$ and $b^2=\frac23a^2$. $P$ on $H$: $\frac{16}{a^2}-\frac{27}{2a^2}=1\Rightarrow a^2=\frac52$, $b^2=\frac53$. Then $l^2=\frac{4b^4}{a^2}=\frac{40}9$ and $m=16e^2-a^2=\frac{145}6$, so $9l^2+6m=40+145=185$.",
    stem=r"Let the sum of the focal distances of the point $P(4,3)$ on the hyperbola $H:\;\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ be $8\sqrt{\tfrac{5}{3}}$. If for $H$, the length of the latus rectum is $l$ and the product of the focal distances of the point $P$ is $m$, then $9l^2+6m$ is equal to:")
ok(P+"111",r"Repeatedly applying $A^n=A^{n-2}+A^2-I$ gives $A^{50}=A^2+24(A^2-I)=25A^2-24I$. Here $A^2=\begin{pmatrix}1&0&0\1&1&0\1&0&1\end{pmatrix}$, so $A^{50}=\begin{pmatrix}1&0&0\25&1&0\25&0&1\end{pmatrix}$, whose elements sum to $53$.")
ok(P+"112",r"$4+3k^2+k^4=(k^2+k+2)(k^2-k+2)$ and $4k=2[(k^2+k+2)-(k^2-k+2)]$, so $T_k=2\left(\frac1{k^2-k+2}-\frac1{k^2+k+2}\right)$, which telescopes: $S_{20}=2\left(\frac12-\frac1{422}\right)=\frac{210}{211}$. So $m+n=421$.")
fix(P+"113",r"$\sum_{r=1}^{n}r^2\binom nr=n(n+1)2^{n-2}$. For $n=15$: $15\cdot16\cdot2^{13}=2^{17}\cdot3\cdot5$. So $m+n+k=17+1+1=19$. Trap: using $r\binom nr=n\binom{n-1}{r-1}$ only once (that gives $\sum r\binom nr$).",
    stem=r"If $1^2\binom{15}{1} + 2^2\binom{15}{2} + 3^2\binom{15}{3} + \dots + 15^2\binom{15}{15} = 2^m\,3^n\,5^k$, where $m,n,k$ are positive integers, then $m + n + k$ is equal to:")
fix(P+"114",r"Tangency: $p^2=16+9=25$, $p=\pm5$; points of contact $\left(\mp\frac{16}5,\pm\frac95\right)$. $y=x$ meets $E$ at $\pm\left(\frac{12}5,\frac{12}5\right)$. $ABCD$ is a parallelogram centred at the origin, area $=2\left|\frac{-16}{5}\cdot\frac{12}5-\frac95\cdot\frac{12}5\right|=2\cdot12=24$.",
    stem=r"Let for two distinct values of $p$ the lines $y = x + p$ touch the ellipse $E:\;\frac{x^2}{4^2}+\frac{y^2}{3^2}=1$ at the points $A$ and $B$. Let the line $y = x$ intersect $E$ at the points $C$ and $D$. Then the area of the quadrilateral $ABCD$ is equal to:")
ok(P+"115",r"$A=\{12-d,12,12+d\}$, $p=12(144-d^2)$; $q=12(144-D^2)$. Then $\frac{p+q}{p-q}=\frac{288-d^2-D^2}{D^2-d^2}=\frac{19}5$ with $D=d+3$ gives $5d^2+72d-612=0$, so $d=6$, $D=9$. $p-q=12(81-36)=540$.")
ok(P+"116",r"Rewrite as $\sin y\frac{dy}{dx}=\frac{7\cos y}{x}-\frac{e^x}{x^5}$; with $u=\cos y$: $u'+\frac7xu=\frac{e^x}{x^5}$. I.F. $x^7$: $(x^7u)'=x^2e^x$, so $x^7u=e^x(x^2-2x+2)+C$; $u(1)=0$ gives $C=-e$. At $x=2$: $\cos y=\frac{2e^2-e}{128}$.")
ok(P+"117",r"The circle has $F_1F_2$ as diameter, so $\angle F_1PF_2=90^\circ$. With $PF_1+PF_2=17$ and $\frac12PF_1\cdot PF_2=30$: $(2c)^2=PF_1^2+PF_2^2=289-120=169$, so $2c=13$.")
fix(P+"118",r"From the $f$-equation and its $x\to\frac1x$ version: $f(x)=\frac13\left(\frac2{x^2}+5-x^2\right)$, so $\alpha=\frac13\left(1+5-\frac73\right)=\frac{11}9$. Putting $x=\frac12$ in the $g$-equation: $-g(\tfrac12)=\tfrac12$, so $g(x)=\frac{x}2-\frac34$ and $\beta=\int_1^2\left(\frac x2-\frac34\right)dx=0$. Thus $9\alpha+\beta=11$.",
    stem=r"Let $f(x)+2f\bigl(\tfrac{1}{x}\bigr)=x^2+5$ and $2g(x)-3g\bigl(\tfrac{1}{2}\bigr)=x$, $x>0$. If $\alpha=\int_1^2 f(x)\,dx$ and $\beta=\int_1^2 g(x)\,dx$, then the value of $9\alpha+\beta$ is:")
ok(P+"119",r"Solving, the lines meet at $A=(7,5,3)$. The angle between directions $(1,0,-1)$ and $(3,4,5)$ has $\cos\theta=\frac{-2}{\sqrt2\sqrt{50}}=-\frac15$, so $\sin^2\theta=\frac{24}{25}$. Area$^2=\left(\frac12\cdot15\sin\theta\right)^2=\frac{225}4\cdot\frac{24}{25}=54$.")
ok(P+"120",r"Mean $4$: $a+b=8$. Variance $2$: $\sum x^2=8(16+2)=144$, so $a^2+b^2=144-112=32$, giving $a=b=4$. Data $2,3,3,4,4,4,5,7$; mode $4$. Mean deviation about $4$: $\frac{2+1+1+0+0+0+1+3}8=1$.")
json.dump(R,open('r2.json','w'),ensure_ascii=False,indent=1)
