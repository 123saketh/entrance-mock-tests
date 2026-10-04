import json
R={}
def ok(ref,e): R[ref]={"verdict":"ok","explanation":e}
def fix(ref,e,stem=None,options=None):
    d={"verdict":"fix","explanation":e}
    if stem: d["stem"]=stem
    if options: d["options"]=options
    R[ref]=d
def drop(ref,r): R[ref]={"verdict":"drop","reason":r}
P="JEE Main 2025 Apr #"
ok(P+"70",r"Need $x^2-9x+18>0$ and $1-\log_4(x^2-9x+18)>0$, i.e. $x^2-9x+18<4\Rightarrow x^2-9x+14<0\Rightarrow 2<x<7$. With $x<3$ or $x>6$, the domain is $(2,3)\cup(6,7)$, so the sum is $2+3+6+7=18$. Trap: forgetting the inner positivity condition.")
ok(P+"76",r"$\mathrm{adj}(2A)=4\,\mathrm{adj}A$, so $3A\,\mathrm{adj}(2A)=12A\,\mathrm{adj}A=12|A|I=60I$. Then $\mathrm{adj}(60I)=60^2I$ and $|2\cdot60^2I|=2^3\cdot60^6=2^{15}3^6 5^6$. Hence $\alpha+\beta+\gamma=15+6+6=27$. Trap: $\mathrm{adj}(kA)=k^{n-1}\mathrm{adj}A$, not $k\,\mathrm{adj}A$.")
fix(P+"77",r"Take $A=(1+2t,2+3t,3+4t)$ on $L_1$ and $B=(6+s,s,4-s)$ on $L_2$; collinearity with $(4,1,0)$ gives $t=-1$, $s=3$. So $A=(-1,-1,-1)$, $B=(9,3,1)$. The determinant is $1(-1+3)-0+1(-3+9)=2+6=8$.",
    stem=r"Let a line passing through the point $(4,1,0)$ intersect the line $L_1:\;\frac{x-1}{2}=\frac{y-2}{3}=\frac{z-3}{4}$ at the point $A(\alpha,\beta,\gamma)$ and the line $L_2:\;x-6 = y = -z + 4$ at the point $B(a,b,c)$. Then $\det\begin{pmatrix}1 & 0 & 1 \ \alpha & \beta & \gamma \ a & b & c\end{pmatrix}$ is equal to:")
ok(P+"78",r"Since $\alpha^2=-\sqrt3\alpha+16$, $P_{25}+\sqrt3P_{24}=16P_{23}$, so the first fraction is $8$. Since $\gamma^2=-3\gamma+1$, $Q_{25}=-3Q_{24}+Q_{23}$, so the second fraction is $-3$. Total $8-3=5$.")
ok(P+"79",r"Rational terms (even powers of $\sqrt3$) sum to $\frac{(2+\sqrt3)^8+(2-\sqrt3)^8}{2}$. Now $(2+\sqrt3)^2=7+4\sqrt3$, $(2+\sqrt3)^4=97+56\sqrt3$, $(2+\sqrt3)^8=18817+10864\sqrt3$. So the sum is $18817$.")
ok(P+"80",r"For each $x$, list $y$ with $-x^2\le 2y\le 4-x^2$: $x=0$: $y=0,1,2$; $x=\pm1$: $y=0,1$; $x=\pm2$: $y=-2,-1,0$; $x=\pm3$: $y=-3$. So $\ell=3+4+6+2=15$. Pairs $(x,x)$ present: $(0,0),(1,1),(-2,-2),(-3,-3)$, so $m=7-4=3$. $\ell+m=18$.")
ok(P+"81",r"$P$ is inside. For a chord through $P$ at angle $\theta$, $PA\cdot PB=\frac{|S_P|}{\cos^2\theta/36+\sin^2\theta/25}$, maximal when $\theta=0$ (horizontal). On $y=\sqrt5$: $x=\pm\frac{12}{\sqrt5}$, so $PA=\frac{7}{\sqrt5}$, $PB=\frac{17}{\sqrt5}$. Then $5(PA^2+PB^2)=49+289=338$.")
ok(P+"82",r"Differences $2,8,14,20,\dots$ form an A.P. with difference $6$, so $T_n=3n^2-7n+5$. Then $S_{20}=3\cdot2870-7\cdot210+5\cdot20=8610-1470+100=7240$.")
ok(P+"83",r"Log needs $\frac{2x-3}{5+4x}>0$: $x<-\frac54$ or $x>\frac32$. $\sin^{-1}$ needs $(4+3x)^2\le(2-x)^2\Rightarrow 2x^2+7x+3\le0\Rightarrow -3\le x\le-\frac12$. Intersection gives $\alpha=-3$, $\beta=-\frac54$, so $\alpha^2+4\beta=9-5=4$.")
fix(P+"84",r"$\sum_{r=0}^{9}\frac{r+3}{2^r}\binom9r=3\left(\tfrac32\right)^9+\tfrac92\left(\tfrac32\right)^8=6\left(\tfrac32\right)^9$. Removing the $r=0$ term ($=3$): sum $=6\left(\tfrac32\right)^9-3$, so $\alpha=6,\beta=3$ and $(\alpha+\beta)^2=81$.",
    stem=r"If $\displaystyle\sum_{r=1}^{9}\left(\frac{r+3}{2^r}\right)\binom{9}{r} = \alpha\left(\tfrac{3}{2}\right)^9 - \beta$, where $\alpha,\beta\in\mathbb{N}$, then $(\alpha+\beta)^2$ is equal to:")
ok(P+"85",r"Using $C_3\to C_3-C_1$: expanding gives $y=\sin x\cdot(28-27)-\cos x\cdot(27-27)+(\cos x+1)(27-28)=\sin x-\cos x-1$, wait simplify fully: $y=\sin x-\cos x-1$ up to the $\sin x,\cos x$ terms which satisfy $y''+y=0$. Hence $y''+y$ equals the constant term $-1$.")
ok(P+"86",r"Rewrite as $\tan x=\frac{\pi-2x}{3}$ and intersect graphs. The line meets each branch of $\tan x$ in $[-2\pi,2\pi]$ once except where it leaves the window: counting branch by branch gives $5$ intersection points. Trap: miscounting the partial branches at the ends of the interval.")
fix(P+"87",r"Differentiating $\int_0^x g=x-\int_0^x tg(t)\,dt$ gives $g=1-xg$, so $g(x)=\frac1{1+x}$. The DE becomes $y'-y\tan x=2\sec x$; with integrating factor $\cos x$, $(y\cos x)'=2$, so $y\cos x=2x$. Hence $y(\pi/3)=\frac{2\pi/3}{1/2}=\frac{4\pi}{3}$.",
    stem=r"Let $g$ be a differentiable function such that $\displaystyle\int_0^x g(t)\,dt = x - \int_0^x t\,g(t)\,dt$, $x\ge0$, and let $y=y(x)$ satisfy the differential equation $\frac{dy}{dx} - y\tan x = 2(x+1)\sec x\,g(x)$ for $x\in[0,\tfrac{\pi}{2})$. If $y(0)=0$, then $y\bigl(\tfrac{\pi}{3}\bigr)$ is equal to:")
ok(P+"88",r"The line is $y=x$: $A=(-2,-2)$, $B=(\frac p6,\frac p6)$, and $AB=\sqrt2\left|\frac p6+2\right|=\frac9{\sqrt2}$ gives $p=15$. $AM=\frac{|-8-4-15|}{\sqrt{20}}=\frac{27}{\sqrt{20}}$, $BM=\sqrt{AB^2-AM^2}=\frac9{\sqrt{20}}$. Ratio $=3$.")
ok(P+"89",r"Clearing denominators: $z^2+3i=(2+3i)(z-2+i)$, i.e. $z^2-(2+3i)z+(7+7i)=0$. Then $z_1+z_2=2+3i$, $z_1z_2=7+7i$, and $z_1^2+z_2^2=(2+3i)^2-2(7+7i)=-5+12i-14-14i=-19-2i$.")
fix(P+"90",r"Put $u=3-x^2$: $\int x^3\sqrt{3-x^2}\,dx=-\frac12\int(3-u)\sqrt u\,du=-u^{3/2}+\frac{u^{5/2}}5+C$. At $x=\sqrt2$ ($u=1$): $-\frac45+C=-\frac45$, so $C=0$. At $x=1$ ($u=2$): $f(1)=-2\sqrt2+\frac{4\sqrt2}5=-\frac{6\sqrt2}5$.",
    stem=r"Let $f(x)=\int x^3\sqrt{3 - x^2}\,dx$. If $5f(\sqrt{2}) = -4$, then $f(1)$ is equal to:")
ok(P+"91",r"$a_3a_5=a_4^2=729\Rightarrow a_4=27$, so $a_2=\frac{111}4-27=\frac34$ and $r^2=36$, $r=6$. Then $a_1=\frac18$, $a_2=\frac34$, $a_3=\frac92$; sum $=\frac{43}8$, and $24\cdot\frac{43}8=129$.")
fix(P+"92",r"Need $\log_6(3+4x-x^2)>1\Rightarrow x^2-4x+3<0$, so $(a,b)=(1,3)$ and $b-a=2$. $\int_0^2\lfloor x^2\rfloor dx=(\sqrt2-1)+2(\sqrt3-\sqrt2)+3(2-\sqrt3)=5-\sqrt2-\sqrt3$. So $p+q+r=5+2+3=10$.",
    stem=r"Let the domain of the function $f(x)=\log_2\bigl(\log_4\bigl(\log_6(3+4x-x^2)\bigr)\bigr)$ be $(a,b)$. If $\displaystyle\int_0^{b-a} \lfloor x^2\rfloor\,dx = p - \sqrt{q} - \sqrt{r}$, with $p,q,r\in\mathbb{N}$ and $\gcd(p,q,r)=1$, where $\lfloor\cdot\rfloor$ is the greatest integer function, then $p+q+r$ is equal to:")
ok(P+"93",r"The parabolas are mirror images in $y=x$. Distance from $(t,t^2+2)$ to $y=x$ is $\frac{t^2-t+2}{\sqrt2}$, minimised at $t=\frac12$: $\frac{7}{4\sqrt2}$. The gap between the curves is twice this, $\frac{7\sqrt2}4$, so the smallest circle has radius $\frac{7\sqrt2}8$.")
ok(P+"94",r"Left limit: $e^a$. Right side is $0/0$ only if $c=8$; then the limit is $\frac{1/4}{1/12}=3$. Continuity: $e^a=1+b=3$, so $b=2$. Thus $e^abc=3\cdot2\cdot8=48$.")
ok(P+"95",r"$L_1$: $(1,2,t)$, $L_2$: $(\lambda,s,6)$. The common perpendicular is along the $x$-axis, so the shortest distance is $|\lambda-1|=3$, giving $\lambda_1=4$, $\lambda_2=-2$. Distance$^2$ of $(4,-2,7)$ from $L_1$ ($x=1,y=2$) is $3^2+4^2=25$.")
json.dump(R,open('r1.json','w'),ensure_ascii=False,indent=1)
