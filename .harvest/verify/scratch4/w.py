import json
d={x['ref']:x for x in json.load(open('pw_batch4.json',encoding='utf-8'))}
R={}
def ok(r,e): R['JEE Main 2025 '+r]={'verdict':'ok','explanation':e}
def fix(r,e,stem=None,options=None):
    v={'verdict':'fix','explanation':e}
    if stem: v['stem']=stem
    if options: v['options']=options
    R['JEE Main 2025 '+r]=v
J=lambda r:d['JEE Main 2025 '+r]
ok('Jan #243',r"For $P(t^2,2t)$, $D^2=(t^2-a)^2+4t^2$ is minimised at $t^2=a-2$ (when $a>2$), giving $D^2=4a-4=16$, so $a=5$. A circle through $(5,0)$ and focus $(1,0)$ with centre on the x-axis has centre $(3,0)$, radius 2: $x^2+y^2-6x+5=0$. Trap: the nearest point is not the vertex when $a>2$.")
ok('Jan #244',r"Coefficient of $x$: $p-q=1$. Coefficient of $x^2$: $\binom p2+\binom q2-pq=\frac{(p-q)^2-(p+q)}{2}=-2$, so $p+q=5$. Hence $p=3,q=2$ and $p^2+q^2=13$.")
fix('Jan #245',r"Area $=\int_{-1}^{1}(a+e^{|x|}-e^{-x})dx=2a+2(e-1)-(e-\frac1e)=2a+e-2+\frac1e$. Setting this equal to $\frac{e^2+8e+1}{e}=e+8+\frac1e$ gives $2a-2=8$, so $a=5$. Trap: $\int_{-1}^1 e^{|x|}dx=2(e-1)$, not $e-\frac1e$.",
 stem=J('Jan #245')['stem'].replace(r'\frac{\pi^2 + 8e + 1}{e}',r'\frac{e^2 + 8e + 1}{e}'))
fix('Apr #2',r"Differentiate: $10f=5f+5xf'-5x^4\Rightarrow xf'-f=x^4\Rightarrow (f/x)'=x^2$, so $f/x=\frac{x^3}{3}+C$. At $x=1$: $0=5f(1)-10$, so $f(1)=2$, $C=\frac53$. Thus $f(3)=3(9+\frac53)=32$. Trap: use the given relation at $x=1$ to fix the constant.",
 stem=J('Apr #2')['stem'].replace(r'If $\int_1^x f(t)\,dt',r'If $10\int_1^x f(t)\,dt'))
ok('Apr #3',r"With $2n$ terms, (even-term sum) $-$ (odd-term sum) $=nd=6$ and $(2n-1)d=\frac{21}{2}$, so $d=\frac32$, $n=4$. Odd-term sum: $4a_1+18=24$, so $a_1=\frac32$. Terms $\frac32,3,\frac92,\dots,12$: the integers are $3,6,9,12$, i.e. 4 terms.")
fix('Apr #4',r"Each step goes from $b$ to $a=2b+1$, so going backwards along the chain: $1\to3\to7\to15\to31\to63$ (next, 127, exceeds 100). The chain $(63,31),(31,15),(15,7),(7,3),(3,1)$ has 5 pairs, so $k=5$. Starting from any other number gives a shorter chain.",
 stem=J('Apr #4')['stem'].replace(r'\{1, 2, 3, \ldots, 10\}',r'\{1, 2, 3, \ldots, 100\}'))
ok('Apr #5',r"$2b=\frac14(2ae)\Rightarrow b=\frac{ae}{4}$. Then $a^2(1-e^2)=\frac{a^2e^2}{16}$ gives $17e^2=16$, so $e=\frac{4}{\sqrt{17}}$. Trap: the distance between the foci is $2ae$, not $ae$.")
ok('Apr #6',r"$\vec a\times\vec b=(2,17,-7)$ with magnitude $\sqrt{342}=3\sqrt{38}$. With $\vec{PQ}=(2,3,-2)$, $|\vec{PQ}\cdot(\vec a\times\vec b)|=|4+51+14|=69$. So the distance is $\frac{69}{3\sqrt{38}}=\frac{23}{\sqrt{38}}$.")
ok('Apr #7',r"$x^2=2(2x+6)\Rightarrow x=-2$ or $6$, and the second-quadrant point is $(-2,2)$. Using $\int_{-c}^{c}\frac{g(x)}{1+5^x}dx=\int_0^c g(x)dx$ for even $g$: $I=\int_0^2 9x^2dx=24$. Trap: the limits are $a=-2$, $b=2$, the coordinates of the point.")
ok('Apr #8',r"For infinitely many solutions, $\Delta=0$ and $\Delta_x=\Delta_y=\Delta_z=0$. Solving gives $\lambda=-1$, $\mu=-5$, so $\lambda^2+\mu^2=26$.")
ok('Apr #9',r"Factor as a quadratic in $\csc\theta$: $\csc\theta=2$ or $-\frac{2}{\sqrt3}$, i.e. $\sin\theta=\frac12$ or $-\frac{\sqrt3}{2}$. On $[-\frac{7\pi}{6},\frac{4\pi}{3}]$: $\sin\theta=\frac12$ at $-\frac{7\pi}{6},\frac{\pi}{6},\frac{5\pi}{6}$, and $\sin\theta=-\frac{\sqrt3}{2}$ at $-\frac{2\pi}{3},-\frac{\pi}{3},\frac{4\pi}{3}$. Total 6. Trap: both endpoints are solutions.")
ok('Apr #10',r"Bags are equally likely and each has 10 balls, so $p=\frac{3}{3+4+5}=\frac14$ and $q=\frac{4}{5+3+4}=\frac13$. Hence $\frac1p+\frac1q=7$.")
ok('Apr #11',r"Sum $=72\Rightarrow a+b=19$. $\sum x^2=8(9.25+81)=722\Rightarrow a^2+b^2=193$, so $ab=\frac{361-193}{2}=84$. Thus $a+b+ab=103$.")
ok('Apr #12',r"$10+3x-x^2>0\Rightarrow -2<x<5$, and $x+|x|>0\Rightarrow x>0$. So the domain is $(0,5)$: $(1+0)^2+5^2=26$.")
ok('Apr #13',r"Rationalise: the integrand equals $\frac{\sqrt{3+x^2}-\sqrt{1+x^2}}{2}$. Using $\int_0^1\sqrt{x^2+k}\,dx=\frac{\sqrt{1+k}}{2}+\frac k2\ln\frac{1+\sqrt{1+k}}{\sqrt k}$: $\int_0^1\sqrt{3+x^2}=1+\frac32\ln\sqrt3$ and $\int_0^1\sqrt{1+x^2}=\frac{\sqrt2}{2}+\frac12\ln(1+\sqrt2)$. So $4\cdot\frac12(\dots)=2+3\ln\sqrt3-\sqrt2-\ln(1+\sqrt2)$. Subtracting $3\ln\sqrt3$ gives $2-\sqrt2-\ln(1+\sqrt2)$.")
ok('Apr #14',r"Expand: the constant term $1+a-b$ and the $x^2$ term $-2-8a$ must both vanish. So $a=-\frac14$, $b=\frac34$ and $a+b=\frac12$.")
ok('Apr #15',r"Write the sum as $\sum(10-10^{-r})\binom{11}{r+1}=10(2^{11}-1)-10\sum_{j=1}^{11}\binom{11}{j}10^{-j}=10\cdot2^{11}-10(1.1)^{11}$. This equals $\frac{20^{11}-11^{11}}{10^{10}}$, so $\alpha=20$.")
ok('Apr #17',r"Focus $S(4,0)$. $P(1,-4)$ has parameter $t=-\frac12$, so $Q$ has $t=2$, i.e. $Q(16,16)$. $SP=1+4=5$ and $SQ=16+4=20$, so $m:n=1:4$ and $m^2+n^2=17$.")
ok('Apr #18',r"Solving $(\vec a-\vec c)\times\vec b=(-18,-3,12)$ with $\vec a\cdot\vec c=3$ gives $\vec c=(2,1,2)$. Then $\vec a\cdot\vec d=[\vec a\ \vec b\ \vec c]=-15$, so $|\vec a\cdot\vec d|=15$.")
ok('Apr #19',r"The normal makes $45^\circ$ with the x-axis, so $L$ is $x+y+c=0$, i.e. $b=1$. The intercepts both have length $|c|$, so $\frac{c^2}{2}=48$ and $c^2=96$. Hence $b^2+c^2=97$.")
ok('Apr #20',r"$A^3=2A^2+4A-4I$. Then $A^4=2A^3+4A^2-4A=8A^2+4A-8I$ and $A^5=8A^3+4A^2-8A=20A^2+24A-32I$. So $\alpha+\beta+\gamma=12$.")
ok('Apr #26',r"By Legendre's formula, $\lfloor50/3\rfloor+\lfloor50/9\rfloor+\lfloor50/27\rfloor=16+5+1=22$.")
ok('Apr #27',r"Arrange five 1's, three 2's and two 0's: $\frac{10!}{5!\,3!\,2!}=2520$. Trap: the remaining two terms must be 0's, so they are identical, not distinct.")
ok('Apr #28',r"$ae=\sqrt{10}$ and $\frac ae=\frac{9}{\sqrt{10}}$, so $a^2=9$, $e^2=\frac{10}{9}$ and $b^2=a^2(e^2-1)=1$. Then $l=\frac{2b^2}{a}=\frac23$ and $9(e^2+l)=10+6=16$.")
ok('Apr #29',r"Rearranging gives $f(2x+2y)\sin(x-y)=f(2x-2y)\sin(x+y)$, i.e. $\frac{f(u)}{\sin(u/2)}$ is constant. So $f(x)=k\sin\frac x2$, and $f'(0)=\frac k2=\frac12$ gives $k=1$. Then $f''(x)=-\frac14\sin\frac x2$, $f''(\frac{5\pi}{3})=-\frac18$, and $24f''=-3$.")
fix('Apr #30',r"$\det A=\alpha\beta+6=0$ with $\alpha+\beta=1$ gives $\alpha=3$, $\beta=-2$. Here $\operatorname{tr}A=1$ and $\det A=0$, so $A^2=A$. Hence $(I+A)^8=I+(2^8-1)A=I+255A=\begin{pmatrix}766&-255\\1530&-509\end{pmatrix}$.",
 stem=J('Apr #30')['stem'].replace(r'\begin{pmatrix}\alpha-1 & -1',r'\begin{pmatrix}\alpha & -1'))
fix('Apr #31',r"$\frac{x+1}{x^{2/3}-x^{1/3}+1}=x^{1/3}+1$ and $\frac{x-1}{x-\sqrt x}=\frac{\sqrt x+1}{\sqrt x}=1+x^{-1/2}$. So the base is $x^{1/3}-x^{-1/2}$. In the general term $\binom{10}{r}x^{(10-r)/3}(-1)^r x^{-r/2}$, the exponent is 0 when $r=4$, giving $\binom{10}{4}=210$.",
 stem=J('Apr #31')['stem'].replace(r'- \tfrac{x+1}{x-x^{1/2}}',r'- \tfrac{x-1}{x-x^{1/2}}'))
ok('Apr #32',r"Factor: $(2\cos\theta-\sqrt3)(\sqrt2\cos\theta+1)=0$, so $\cos\theta=\frac{\sqrt3}{2}$ or $-\frac{1}{\sqrt2}$. Each value has 4 solutions in $[-2\pi,2\pi]$, giving 8 in total.")
ok('Apr #33',r"$\sum_{k=1}^{12}a_{2k-1}=12a_1+132d=-\frac{72}{5}a_1$, so $d=-\frac{a_1}{5}$. $S_n=\frac n2(2a_1+(n-1)d)=0$ gives $2=\frac{n-1}{5}$, so $n=11$.")
ok('Apr #34',r"$f'(x)=6(x-a)(x-2a)$. With $a>0$, the maximum is at $p=a$ and the minimum at $q=2a$. $a^2=2a$ gives $a=2$, so $f(x)=2x^3-18x^2+48x+1$ and $f(3)=37$.")
ok('Apr #35',r"Cross-multiplying: $2+k^2z=k^2z+kz\bar z=k^2z+k$, so $k=2$ and the point is $2+4i$. Its distance from the centre $1+2i$ is $\sqrt5$, so the maximum distance from the circle is $\sqrt5+1$.")
ok('Apr #36',r"The magnitudes are $3,3,1$, so we need $\frac{2a_1-a_2+2a_3}{3}=\frac{a_1+2a_2-2a_3}{3}=a_3$. $(7,9,5)$ satisfies this: $\frac{15}{3}=\frac{15}{3}=5$, and $|(7,9,5)|=\sqrt{155}$. The other sign patterns fail.")
fix('Apr #37',r"Symmetric: if $f(0)=g(1)$ and $f(1)=g(0)$, then $g(0)=f(1)$ and $g(1)=f(0)$. Not reflexive: that needs $f(0)=f(1)$ for every $f$. Not transitive: $(f,g),(g,h)\in R$ give $f(0)=h(0)$, not $f(0)=h(1)$. So $R$ is symmetric only.",
 options={'A':'Symmetric and transitive but not reflexive','B':'Symmetric but neither reflexive nor transitive','C':'Reflexive but neither symmetric nor transitive','D':'Transitive but neither reflexive nor symmetric'})
ok('Apr #38',r"For a finite limit, $\gamma=1$, which leaves numerator $\sim\alpha x^3$. The denominator $\sin2x-\beta x\sim(2-\beta)x-\frac43x^3$ needs $\beta=2$. Then $\frac{\alpha}{-4/3}=3$ gives $\alpha=-4$, and $\beta+\gamma-\alpha=7$.")
ok('Apr #39',r"$P_{10}=(\alpha+\beta)P_9-\alpha\beta P_8$ with $\alpha+\beta=P_1=1$: $123=76-47\alpha\beta$, so $\alpha\beta=-1$. The roots $\frac1\alpha,\frac1\beta$ have sum $\frac{1}{-1}=-1$ and product $-1$: $x^2+x-1=0$.")
ok('Apr #40',r"Setting $\Delta=\Delta_x=\Delta_y=\Delta_z=0$ gives $\alpha=-\frac{19}{9}$, $\beta=\frac{6}{11}$. So $22\beta-9\alpha=12+19=31$.")
ok('Apr #41',r"$a^2=18$, $e^2=\frac12$. $SP\cdot S'P=(a+ex)(a-ex)=18-\frac{x^2}{2}$ with $x^2\in[0,18]$. The maximum is 18 and the minimum is 9, so the sum is 27.")
ok('Apr #42',r"Distance from $P$ to the line: $\frac{|\vec{AP}\times\vec d|}{|\vec d|}$ with $A(-3,1,-4)$, $\vec d=(5,2,3)$, which gives $h=\sqrt{\frac{21}{2}}$. Area $=\frac12\cdot5\cdot h=\frac{5\sqrt{21}}{2}$, so $\frac mn=\frac{5\sqrt{21}}{2}$, i.e. $2m-5\sqrt{21}\,n=0$.")
fix('Apr #43',r"For a tetrahedron with mutually perpendicular edges at $A$, De Gua's theorem gives $[BCD]^2=[ABC]^2+[ACD]^2+[ADB]^2=25+36+49=110$. So $[BCD]=\sqrt{110}$.",
 stem=J('Apr #43')['stem'].replace('the area (in square units) of ABCD','the area (in square units) of the triangle BCD'))
ok('Apr #44',r"$A=\begin{pmatrix}0&a&1\\2&0&0\\a&1&1\end{pmatrix}$, so $\det A=-2(a-1)=-4$ and $a=3$. Then $\det(4\,\mathrm{adj}(2A))=4^3\det(2A)^2=64\cdot(8\cdot(-4))^2=2^6\cdot2^{10}=2^{16}$. So $m=16$, $n=0$ and $m+n=16$.")
ok('Apr #45',r"$SP$ has slope $\sqrt3$: for $P(t^2,2t)$, $\frac{2t}{t^2-1}=\sqrt3$ gives $t=\sqrt3$, so $P(3,2\sqrt3)$. The circle on $PS$ as diameter has centre $(2,\sqrt3)$ and radius $\frac{SP}{2}=2$, so it touches the y-axis at $(0,\sqrt3)$. Hence $5\alpha^2=15$.")
fix('Apr #51',r"Let $g(x)=|x+2|-2|x|$; then $g(-2)=-4$, $g(0)=2$, and $g=0$ at $x=-\frac23$ and $x=2$. For $f=|g|$: local minima at $x=-\frac23$ and $x=2$ (zeros), and a local maximum at $x=0$. At $x=-2$, $f$ is strictly monotone, so there is no extremum. So $m+n=3$.",
 stem=r"Let $f: \mathbb{R}\to\mathbb{R}$ be a function defined by $$f(x)=\bigl|\,\lvert x+2\rvert - 2\lvert x\rvert\,\bigr|.$$ If $m$ is the number of points of local minima and $n$ is the number of points of local maxima of $f$, then $m+n$ is:")
ok('Apr #52',r"$\alpha=2\beta$, $\gamma=\beta$: $\cos^22\beta+2\cos^2\beta=1$. With $c=\cos^2\beta$: $4c^2-2c=0$, so $c=0$ or $\frac12$. This gives $\beta=\frac\pi2$ ($\alpha=\pi$) or $\beta=\frac\pi4$ ($\alpha=\frac\pi2$); $\beta=\frac{3\pi}{4}$ would need $\alpha>\pi$. So the sum is $\frac{3\pi}{4}$.")
ok('Apr #53',r"The circle through $(0,0),(4,6),(-1,5)$ is $x^2+y^2-4x-6y=0$, with $r^2=13$. Substituting $(k,3k)$: $10k^2-22k=0$, so $k=\frac{11}{5}$. Then $10k+r^2=22+13=35$.")
ok('Apr #54',r"$a+b=14$ and $a^2+b^2=5(10+25)-59=116$, so $ab=40$, giving $a=10$, $b=4$. The new data $2,5,13,11,9$ has mean 8, and its variance is $\frac{36+9+25+9+1}{5}=16$.")
ok('Apr #55',r"$R=\{(-2,1),(-1,1),(0,1),(1,1),(2,2),(3,3)\}$, so $l=6$. Reflexive needs $(-2,-2),(-1,-1),(0,0)$, so $m=3$. Symmetric needs $(1,-2),(1,-1),(1,0)$, so $n=3$. Total 12.")
ok('Apr #56',r"The family is $(x+2y-5)+\lambda(3x+7y-17)=0$, which passes through $P(1,2)$. The line farthest from $O$ is perpendicular to $OP$: $x+2y=5$. Distance from $(3,6)$: $\frac{10}{\sqrt5}$, so $d^2=20$.")
ok('Apr #57',r"$(12-k)x^2+2(12-k)x-2=0$ has equal roots when $4(12-k)^2+8(12-k)=0$, i.e. $k=14$ ($k\ne12$). The distance of $(14,7)$ from the line is $\frac{42+28+5}{5}=15$.")
ok('Apr #58',r"$\binom{22}{3}-\binom{13}{3}-\binom{10}{3}=1540-286-120=1134$. Remove collinear triples on $L_1$ ($O$ plus 12 points) and on $L_2$ ($O$ plus 9 points). Trap: $O$ lies on both lines.")
ok('Apr #59',r"Put $x=3$: $f(3)+3f(8)=12$. Put $x=8$: $f(8)+3f(3)=32$. Adding: $4(f(3)+f(8))=44$, so the answer is 11.")
ok('Apr #60',r"Using $x\to\pi-x$: $I=4\pi\int_0^\pi\frac{dx}{4\cos^2x+\sin^2x}=8\pi\int_0^{\pi/2}\frac{\sec^2x}{4+\tan^2x}dx=8\pi\cdot\frac12\cdot\frac\pi2=2\pi^2$.")
ok('Apr #61',r"$|x-y|\le y$ means $y\ge\frac x2$ (with $x\ge0$). The curves $y=\frac x2$ and $y=4\sqrt x$ meet at $x=64$. Area $=\int_0^{64}(4\sqrt x-\frac x2)dx=\frac{4096}{3}-1024=\frac{1024}{3}$.")
ok('Apr #62',r"$\sum_{x\ge0}(x+1)3^{-x}=\frac{1}{(1-1/3)^2}=\frac94$, so $k=\frac49$. $P(X\le2)=\frac49(1+\frac23+\frac13)=\frac89$, so $P(X\ge3)=\frac19$.")
ok('Apr #63',r"$3\tan^2x+3=3\sec^2x$, so the equation is $y'+3\sec^2x\,y=\sec^2x$ with integrating factor $e^{3\tan x}$. This gives $y=\frac13+Ce^{-3\tan x}$, and $y(0)$ gives $C=e^3$. Then $y(\frac\pi4)=\frac13+e^3e^{-3}=\frac43$.")
ok('Apr #64',r"$z_k-z_0=r e^{i\theta}\omega^{k}$, where $\omega$ is a cube root of unity. The sum of squares is $r^2e^{2i\theta}(\omega^2+\omega^4+\omega^6)=r^2e^{2i\theta}(1+\omega+\omega^2)=0$.")
ok('Apr #65',r"With $s=\sin x$: $2\sqrt3s^2+(4-\sqrt3)s-2\sqrt3+2(\sqrt3-1)=0$, which gives $s=\frac12$ or $s=-\frac{2}{\sqrt3}$ (rejected). $\sin x=\frac12$ on $[-2\pi,\frac{5\pi}{2}]$: $x=-\frac{11\pi}{6},-\frac{7\pi}{6},\frac\pi6,\frac{5\pi}{6},\frac{13\pi}{6}$, i.e. 5 solutions.")
ok('Apr #66',r"The circle has centre $(0,-6)$ and radius 1. The normal to $y^2=8x$ at $(2t^2,4t)$ passes through $(0,-6)$ when $t=-1$, giving the point $(2,-4)$ at distance $\sqrt{4+4}=2\sqrt2$. So the shortest distance is $2\sqrt2-1$.")
fix('Apr #67',r"$ae=2$ and $e=\frac12$ give $a=4$, $b^2=12$. The minimum enclosing circle is $x^2+y^2=16$. $QR$ lies on $y=-2\sqrt3$, and the farthest point of $C$ from it is $(0,4)$, at height $4+2\sqrt3$. Maximum area $=\frac12\cdot8\cdot(4+2\sqrt3)=8(2+\sqrt3)$.",
 stem=J('Apr #67')['stem'].replace('length $29$','length $8$').replace('y�axis','y-axis'))
ok('Apr #68',r"Parametrise the second line from $(7,10,11)$ as $(7+2\lambda,10-3\lambda,11+6\lambda)$. It meets the first line when $y=4$ and $\frac{x-4}{1}=\frac{z-2}{3}$, giving $\lambda=2$. So the distance is $2\cdot|(2,-3,6)|=2\cdot7=14$.")
ok('Apr #69',r"The $n$-th term is $\frac{n^2}{n!}=\frac{n}{(n-1)!}$, and $\sum_{n\ge1}\frac{n}{(n-1)!}=\sum_{m\ge0}\frac{m+1}{m!}=e+e=2e$.")
assert set(R)==set(d), set(d)^set(R)
for k,v in R.items():
    if v['verdict']=='fix' and 'stem' in v:
        assert v['stem']!=d[k]['stem'],k
        assert '�' not in v['stem'],k
json.dump(R,open('pw_batch4.result.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
r=json.load(open('pw_batch4.result.json',encoding='utf-8'))
from collections import Counter;print(Counter(v['verdict'] for v in r.values()))
for k in ['JEE Main 2025 Apr #67','JEE Main 2025 Apr #30','JEE Main 2025 Apr #31']: print(r[k]['stem'])
