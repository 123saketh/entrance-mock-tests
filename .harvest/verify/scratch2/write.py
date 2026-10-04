import json
src=json.load(open('../pw_batch2.json',encoding='utf-8'))
S={x['ref']:x for x in src}
R={}
def ok(n,e): R[f"JEE Main 2025 Jan #{n}"]={"verdict":"ok","explanation":e}
def drop(n,r): R[f"JEE Main 2025 Jan #{n}"]={"verdict":"drop","reason":r}
def fix(n,e,stem=None,options=None):
    d={"verdict":"fix","explanation":e}
    if stem: d["stem"]=stem
    if options: d["options"]=options
    R[f"JEE Main 2025 Jan #{n}"]=d
def st(n): return S[f"JEE Main 2025 Jan #{n}"]["stem"]

fix(78,r"$|\vec{OA}|=|\vec{OB}|=2$ and the two vectors are symmetric about $y=x$, so the bisector is $y=x$. Distance of $C(a,1-a)$ from it is $\frac{|2a-1|}{\sqrt2}=\frac{9}{\sqrt2}$, so $2a-1=\pm9$, giving $a=5$ or $a=-4$. Sum $=1$. Trap: forgetting the negative case of the modulus.",
    stem=st(78).replace(r"\frac{\theta}{\sqrt{2}}",r"\frac{9}{\sqrt{2}}"))
fix(79,r"For ${}^{12}C_{r-1},{}^{12}C_r,{}^{12}C_{r+1}$ in G.P. we would need $\frac{13-r}{r}=\frac{12-r}{r+1}$, i.e. $13=0$, impossible, so $p=0$. In $(3^{1/4}+4^{1/3})^{12}$, $T_{k+1}={}^{12}C_k\,3^{(12-k)/4}4^{k/3}$ is rational iff $4\mid(12-k)$ and $3\mid k$, i.e. $k=0,12$: $q=27+256=283$. Hence $p+q=283$.",
    stem=st(79).replace(r"\sqrt[4]{4}",r"\sqrt[3]{4}"))
ok(80,r"$\sec^{-1}t$ needs $|t|\ge1$. Since $[x]$ is an integer, $2[x]+1$ is an odd integer, so $|2[x]+1|\ge1$ always. Hence the domain is $(-\infty,\infty)$. Trap: treating $2[x]+1$ like $2x+1$ and excluding $(-1,0)$.")
ok(81,r"GARDEN has 6 distinct letters with vowels A and E. By symmetry, A comes before E in exactly half of the $6!$ arrangements. So the probability that the vowels are NOT in alphabetical order is $\frac12$.")
fix(82,r"Each term equals $\frac{1}{\sin(\pi/6)}\left[\cot\left(\frac{\pi}{4}+\frac{(r-1)\pi}{6}\right)-\cot\left(\frac{\pi}{4}+\frac{r\pi}{6}\right)\right]$, so the sum telescopes to $2\left[\cot\frac{\pi}{4}-\cot\left(\frac{\pi}{4}+\frac{13\pi}{6}\right)\right]=2[1-\cot 75^\circ]=2[1-(2-\sqrt3)]=2\sqrt3-2$. So $a=2,b=-2$ and $a^2+b^2=8$.",
    stem=r"If $\sum_{r=1}^{13} \left\{\frac{1}{\sin \left(\frac{\pi}{4}+(r-1) \frac{\pi}{6}\right) \sin \left(\frac{\pi}{4}+\frac{r\pi}{6}\right)}\right\}=a \sqrt{3}+b$, $a, b \in \mathbb{Z}$, then $a^2+b^2$ is equal to:")
ok(83,r"Differentiate $g(x^3)=x^6+x^7$: $g'(x^3)\cdot3x^2=6x^5+7x^6$, and $g'(u)=uf(u)$, so $3x^5f(x^3)=6x^5+7x^6$, giving $f(x^3)=2+\frac{7x}{3}$. Then $\sum_{r=1}^{15}f(r^3)=30+\frac73\cdot120=310$.")
ok(84,r"$f'(x)=6(x-2)(x-3)$; $f(0)=7$, $f(2)=35$, $f(3)=34$, so $A=[7,35]$ (29 integers). $g(0)=0$, $g\to0$ as $x\to\infty$ and its maximum is less than 1, so the only integer in $B$ is $0$. Hence $n(S)=29+1=30$. Trap: forgetting $0\in B$.")
ok(85,r"$P(W)=\frac13\left(\frac{6}{10}+\frac{4}{10}+\frac{5}{10}\right)=\frac12$. By Bayes, $P(B_2\mid W)=\frac{\frac13\cdot\frac{4}{10}}{\frac12}=\frac{4}{15}$.")
ok(87,r"$a_k=\frac{(k+2)(k+3)}{4}$, so $\frac1{a_k}=4\left(\frac1{k+2}-\frac1{k+3}\right)$ and $S_n=4\left(\frac13-\frac1{n+3}\right)$. Then $S_{2025}=4\cdot\frac{675}{2028}$ and $507S_{2025}=\frac{2700}{4}=675$.")
ok(88,r"The functional equation gives $f(x)=1\pm x^n$; degree 2 with range in $(-\infty,1)$ forces $f(x)=1-x^2$. Then $1-K^2=-2K\Rightarrow K^2-2K-1=0$, so $K=1\pm\sqrt2$. Sum of squares $=(K_1+K_2)^2-2K_1K_2=4+2=6$.")
ok(89,r"Substituting $y^2=8x-x^2$ into $4x^2-9y^2=36$ gives $13x^2-72x-36=0$, so $x=6$ (the root $-\frac{12}{13}$ gives $y^2<0$). So $A,B=(6,\pm2\sqrt3)$. With $P(h,k)$, the centroid is $X=\frac{h+12}{3},Y=\frac k3$; substituting $h=3X-12,k=3Y$ into $2h-3k+4=0$ gives $6x-9y=20$.")
ok(90,r"Put $x=t^4$: $\int\frac{4t^3}{t(1+t)}dt=4\int\left(t-1+\frac1{1+t}\right)dt=4\left(\frac{t^2}2-t+\ln(1+t)\right)+C$. $f(0)=-6$ gives $C=-6$. At $t=1$: $f(1)=4\left(-\frac12+\ln2\right)-6=4(\log_e2-2)$.")
ok(91,r"Curves $x=\frac1{1+y^2}$ and $x=\frac{y^2}2$ meet where $y^4+y^2-2=0$, i.e. $y=\pm1$. Area $=\int_{-1}^{1}\left(\frac1{1+y^2}-\frac{y^2}{2}\right)dy=\frac\pi2-\frac13$.")
fix(92,r"Line through $P\left(\frac{15}{7},\frac{32}{7},7\right)$ along $(1,4,7)$: $\left(\frac{15}{7}+t,\frac{32}{7}+4t,7+7t\right)$. Substituting into $\frac{x+1}{3}=\frac{y+3}{5}=\frac{z+5}{7}$ gives $t=-1$, i.e. the point $\left(\frac87,\frac47,0\right)$. Required square of distance $=t^2(1+16+49)=66$. Trap: computing the perpendicular distance instead of the distance along the given direction.",
    stem=st(92).replace(r"\left(\frac{10}{7}, \frac{22}{7}, 7\right)",r"\left(\frac{15}{7}, \frac{32}{7}, 7\right)"))
ok(94,r"Sum of roots $=3-2i$, product $=2-2i$. Testing $x=1$: $1-3+2i-2i+2=0$, so the roots are $1$ and $2-2i$. Thus $\alpha=1,\beta=0,\gamma=2,\delta=-2$ and $\alpha\gamma+\beta\delta=2$.")
ok(95,r"The equal sides have slopes $\frac12$ and $-1$; the third side makes equal angles with both: $\left|\frac{m-\frac12}{1+\frac m2}\right|=\left|\frac{m+1}{1-m}\right|$. Squaring and simplifying gives $(m^2+1)(m^2-6m-1)=0$, so the real values are $m=3\pm\sqrt{10}$, with sum $6$.")
ok(101,r"$\sum x_i=50$, mean $5$; variance $\frac45$ gives $\sum(x_i-5)^2=8$. Then $98=8+10(5-\beta)^2\Rightarrow\beta=8$ (as $\beta>2$). New data $2(x_i-1)+32$: $\mu=2\cdot4+32=40$, $\sigma^2=4\cdot\frac45=\frac{16}5$. So $\frac{\beta\mu}{\sigma^2}=\frac{320\cdot5}{16}=100$.")
ok(102,r"$3a+3d=54\Rightarrow a+d=18$. $S_{20}=10(2a+19d)=10(36+17d)\in(1600,1800)\Rightarrow 17d\in(124,144)$, so $d=8$, $a=10$. $T_{11}=a+10d=90$.")
ok(103,r"Let $t=\frac1{\sqrt x}>0$. First factor: $9t^2-9t+2=0\Rightarrow t=\frac13,\frac23$. Second: $2t^2-7t+3=0\Rightarrow t=3,\frac12$. All four values are positive and distinct, giving 4 values of $x$.")
fix(104,r"$\sec^2x-\tan^2y=1\iff\tan^2x=\tan^2y$. On $\left[0,\frac\pi2\right)$, $\tan$ is non-negative and injective, so this means $x=y$. Equality is reflexive, symmetric and transitive, so R is an equivalence relation.",
    stem=st(104).replace(r"\left[0, \frac{x}{y}\right)",r"\left[0, \frac{\pi}{2}\right)"))
ok(105,r"Parabolas: $(x-4)^2+(y-3)^2=y^2$ and $(x-4)^2+(y-3)^2=x^2$. Subtracting gives $x^2=y^2$; the real intersections have $x=y$, so $y^2-14y+25=0$ and $y=7\pm2\sqrt6$. Then $AB^2=2(4\sqrt6)^2=192$.")
ok(106,r"Let the counts of 1s, 2s and 3s be $a,b,c$ with $a+b+c=7$ and $a+2b+3c=11$, so $b+2c=4$: $(a,b,c)=(3,4,0),(4,2,1),(5,0,2)$. Count $=\frac{7!}{3!4!}+\frac{7!}{4!2!1!}+\frac{7!}{5!2!}=35+105+21=161$.")
ok(107,r"Equate $L_1$ and $L_2$: $-1+\lambda=2\mu$ and $2+2\lambda=1+7\mu$ give $\lambda=3,\mu=1$, so they meet at $(2,8,4)$. $\vec a+\vec b=(3,9,4)$, so $L_3$ is $(2+3s,8+9s,4+4s)$. With $s=2$ this gives $(8,26,12)$.")
ok(108,r"$\vec a\times\vec c=\vec c\times\vec b\Rightarrow(\vec a+\vec b)\times\vec c=\vec0$, so $\vec c=\lambda(5,-6,4)$ with $|\vec a+\vec b|^2=77$. Then $\vec a\cdot\vec b+\vec c\cdot(\vec a+\vec b)+|\vec c|^2=14+77\lambda+77\lambda^2=168\Rightarrow\lambda^2+\lambda-2=0$, so $\lambda=1,-2$. Max $|\vec c|^2=77\cdot4=308$.")
drop(109,r"Computed value: with $u=\sin\theta-\cos\theta$ the integral is $80\int_{-1}^1\frac{du}{25-16u^2}=8\log_e3$, which disagrees with the keyed $4\log_e3$ (no option matches).")
ok(110,r"$E_1$: $2ae=4,e=\frac1{\sqrt3}\Rightarrow a^2=12,b^2=8$, latus rectum $\frac{8}{\sqrt3}$. So $E_2$ has latus rectum $4=\frac{2A^2}{B}$ with $A^2=\frac23B^2$, giving $B^2=9,A^2=6$. Solving $\frac{x^2}{12}+\frac{y^2}8=1$ and $\frac{x^2}6+\frac{y^2}9=1$ gives $x^2=\frac65,y^2=\frac{36}5$. Area of the rectangle $=4|xy|=\frac{24\sqrt6}{5}$.")
ok(111,r"$C_{ij}=\sum_k a_{ik}A_{jk}$ equals $|A|\delta_{ij}$, so $C=|A|I$ and $|C|=|A|^2$. $|A|=\log_5128\cdot\log_425-\log_45\cdot\log_58=7-\frac32=\frac{11}2$. So $8|C|=8\cdot\frac{121}4=242$.")
ok(112,r"$z_1$ lies in the disc with centre $(8,2)$, radius 1; $z_2$ in the disc with centre $(2,-6)$, radius 2. The distance between the centres is $\sqrt{36+64}=10$, so the minimum $|z_1-z_2|=10-1-2=7$.")
drop(113,r"As transcribed, $(\alpha,\beta,\gamma)$ can be any point on any line perpendicular to both that meets $L_1$, so $5\alpha-11\beta-8\gamma$ is not determined. A condition (likely about $L_2$) is missing, and the original wording can't be recovered with confidence.")
fix(114,r"With rows $(1+\sin^2x,\cos^2x,4\sin4x),(\sin^2x,1+\cos^2x,4\sin4x),(\sin^2x,\cos^2x,1+4\sin4x)$: do $C_1\to C_1+C_2$, then subtract $R_1$ from $R_2$ and $R_3$. The determinant becomes $2+4\sin4x$. So $M=6$, $m=-2$, and $M^4-m^4=1296-16=1280$.",
    stem=st(114).replace(r"\\ 1 + \sin^2 x & \cos^2 x & 4 \sin 4x \\ \sin^2 x",r"\\ \sin^2 x & 1 + \cos^2 x & 4 \sin 4x \\ \sin^2 x"))
fix(116,r"$k^3+6k^2+11k+5=(k+1)(k+2)(k+3)-1$, so the term is $\frac1{k!}-\frac1{(k+3)!}$. The sum tends to $(e-1)-\left(e-1-1-\frac12-\frac16\right)=\frac53$. Trap: with constant $6$ the sum would be $e-1$.",
    stem=st(116).replace("11k + 6","11k + 5"))
fix(117,r"$T_{r+1}={}^nC_r\,7^{(n-r)/3}11^{r/12}$ is an integer iff $12\mid r$ and $3\mid(n-r)$, so $3\mid n$. The number of such $r$ is $\lfloor n/12\rfloor+1=183$, so $n\ge12\cdot182=2184$, and $2184$ is divisible by 3. The least $n$ is $2184$.",
    stem=st(117).replace(r"\sqrt[3]{11}",r"\sqrt[12]{11}"))
ok(118,r"Let $u=\ln\cos x$, so $du=-\tan x\,dx$. The equation becomes $\frac{dy}{du}+\frac{3y}{u}=\frac1{u^2}$; with integrating factor $u^3$, $yu^3=\frac{u^2}2+C$. At $x=\frac\pi4$, $u=-\frac{\ln2}2$ and $y=-\frac1{\ln2}$ give $C=0$, so $y=\frac1{2\ln\cos x}$. At $\frac\pi6$: $y=\frac1{\ln\frac34}=\frac1{\log_e3-\log_e4}$.")
ok(119,r"The centre's distance from $x+y=1$ is $\frac1{\sqrt2}$, so $AB=2\sqrt{4-\frac12}=\sqrt{14}$. The perpendicular bisector of chord $AB$ passes through the centre, so $CD$ is a diameter of length 4 and is perpendicular to $AB$. Area $=\frac12\cdot\sqrt{14}\cdot4=2\sqrt{14}$.")
ok(120,r"The region lies above $y=|x-1|$, below $y=\frac{x^2+3}{2}$ on $[-1,1]$ and below $y=3-|x|$ on $[1,2]$. $A=\int_{-1}^{1}\left(\frac{x^2+3}{2}-|x-1|\right)dx+\int_1^2\left((3-x)-(x-1)\right)dx=\frac43+1=\frac73$. So $6A=14$.")
ok(126,r"$f'(x)=x(x-4)(x-5)$: $f$ increases on $[1,4]$ and decreases on $[4,5]$. With $f(x)=\frac{x^4}4-3x^3+10x^2$: $f(1)=\frac{29}4$, $f(4)=32$, $f(5)=\frac{125}4$. Range $=\left[\frac{29}4,32\right]$, so $4(\alpha+\beta)=29+128=157$.")
ok(127,r"$\vec b\times\vec c=(-7,7,7)$, so $\hat a=\pm\frac{(1,-1,-1)}{\sqrt3}$. The angle condition with $(1,1,1)$ (dot $=-\frac13$) picks $\hat a=\frac{(1,-1,-1)}{\sqrt3}$. Then $\frac{-\alpha}{\sqrt3\sqrt{2+\alpha^2}}=\frac12$ needs $\alpha<0$ and $4\alpha^2=6+3\alpha^2$, so $\alpha=-\sqrt6$.")
ok(128,r"Integrating factor $\sec x$: $(y\sec x)'=\frac{1+2\cos x}{(2+\cos x)^2}=\frac{d}{dx}\frac{\sin x}{2+\cos x}$. So $y\sec x=\frac{\sin x}{2+\cos x}+C$; $f(\pi/3)=\frac{\sqrt3}{10}$ gives $C=0$. Then $f(\pi/4)=\frac{1/2}{2+1/\sqrt2}=\frac1{4+\sqrt2}=\frac{4-\sqrt2}{14}$.")
ok(129,r"A general point of $L$ is $(1+t,-1-t,2+2t)$. Perpendicularity from $(1,2,2)$: $t+(3+t)+4t=0\Rightarrow t=-\frac12$, so $P=\left(\frac12,-\frac12,1\right)$. Intersecting with the second line gives $t=-2$, $Q=(-1,1,-2)$. $PQ^2=\frac94+\frac94+9=\frac{27}2$, so $2PQ^2=27$.")
ok(130,r"$A=vv^T$ with $v=(\sqrt2,2,2\sqrt2)$, so $A^2=(v\cdot v)vv^T=14\,vv^T$. Third-row sum $=14\cdot2\sqrt2\cdot(3\sqrt2+2)=168+56\sqrt2$. So $\alpha+\beta=224$.")
fix(131,r"$A=(1,0)$, $B=(0,1)$. With $N=(1-s,s)$ ($s=\frac{\lambda}{1+\lambda}$) and $MN\perp AB$, $M=(0,2s-1)$, which needs $s\ge\frac12$. Then $AN=s\sqrt2$ and $MN=\sqrt2(1-s)$, so area $=s(1-s)=\frac49\cdot\frac12$, giving $s=\frac13$ or $\frac23$; only $s=\frac23$ is valid. So $\lambda=2$, and the sum is 2.",
    stem=st(131).replace("A right-angled triangle $AMN$","A triangle $AMN$, right-angled at $N$,"))
ok(132,r"Letters in order: A,K,N,P,R,U. Words starting A, K, N: $3\cdot120=360$. Then P with A, K, N second: $3\cdot24=72$, total 432. PR then A second: 6 more, total 438. Next comes PRK: PRKANU is 439th and PRKAUN is 440th.")
ok(133,r"No real roots: $(a-5)^2-8(15-3a)<0\Rightarrow a^2+14a-95<0\Rightarrow a\in(-19,5)$. Integers are $-18,\dots,4$. $\sum x^2=\sum_{1}^{18}k^2+\sum_1^4k^2=2109+30=2139$.")
ok(135,r"$\cos|x|=\cos x$ is smooth, so non-differentiability comes only from simple roots of $x^2-ax+2$. Since $x=2$ is a root, $a=3$, and the roots are $1,2$, so $\beta=1$. Distance of $(2,1)$ from $12x+5y+10=0$ is $\frac{24+5+10}{13}=3$.")
ok(136,r"The curve $|y|=1-x^2$ lies inside the unit circle and encloses area $2\int_{-1}^1(1-x^2)dx=\frac83$. So $\alpha=\pi-\frac83$ and $9\alpha=9\pi-24$, giving $\beta=9,\gamma=-24$ and $|\beta-\gamma|=33$.")
ok(137,r"By Fermat, $7^{22}\equiv1\pmod{23}$, so $7^{103}=7^{88}\cdot7^{15}\equiv7^{15}$. $7^2\equiv3$, so $7^{14}\equiv3^7=2187\equiv2$ and $7^{15}\equiv14$. Remainder $14$.")
ok(138,r"Chord with given midpoint: $T=S_1$: $\frac{5x}{18}+\frac{y}{8}=\frac{25}{36}+\frac1{16}=\frac{109}{144}$. Multiplying by 144: $40x+18y=109$, so $\alpha+\beta=58$.")
drop(139,r"As transcribed, the second domain is $(-\infty,-2)\cup(-1,\frac12)\cup(4,\infty)$, not a single interval $(\gamma,\delta)$. The keyed 186 needs $\gamma^2=16$, which doesn't follow from the stem.")
ok(140,r"The centre is on the perpendicular bisector $x=2$ of the two points and on $3x+2y+2=0$, so it is $(2,-4)$ with $r^2=40$. Distance$^2$ from the centre to $(1,2)$ is $37$, so the half-chord is $\sqrt3$ and the chord length is $2\sqrt3$.")
fix(141,r"Direction of $L$: $(2,1,-2)\times(1,3,4)=(10,-10,5)\parallel(2,-2,1)$. $L$: $(2+2t,-1-2t,3+t)$ meets $x=0$ at $t=-1$, so $Q=(0,1,2)$. $PQ=|t|\cdot\sqrt{4+4+1}=3$.",
    stem=st(141).replace(r"\frac{x-1}{4}=\frac{y+1}{4}=\frac{z-3}{2}",r"\frac{x-1}{2}=\frac{y+1}{1}=\frac{z-3}{-2}").replace(r"\frac{x-3}{4}=\frac{y-2}{3}",r"\frac{x-3}{1}=\frac{y-2}{3}"))
ok(142,r"$P(W)=\frac49\cdot\frac{n+1}{n+4}+\frac59\cdot\frac{n}{n+4}=\frac{9n+4}{9(n+4)}=\frac{29}{45}$. So $45n+20=29n+116$, giving $n=6$.")
ok(143,r"$R_2-R_1=(0,1,3\mid m-1)$ and $R_3-R_1=(0,3,9\mid m^2-1)$. For infinitely many solutions we need $m^2-1=3(m-1)$, i.e. $m=1,2$. Then $\sum_{n=1}^{10}(n+n^2)=55+385=440$.")
fix(144,r"$\log_ey=x\log_e\frac25\Rightarrow y=\left(\frac25\right)^x$ for $x=0,1,2,\dots$. The range is $\{1,\frac25,\frac4{25},\dots\}$, with sum $\frac{1}{1-\frac25}=\frac53$. Trap: forgetting the $x=0$ term $y=1$.",
    stem=st(144).replace(r"x \log_e \left(\frac{x}{5}\right)",r"x \log_e \left(\frac{2}{5}\right)"))
ok(145,r"$\sin x=1-\sin^2x=\cos^2x$, so $\cos^2x=\sin x=s$ and $\tan^2x=\frac{\sin^2x}{\cos^2x}=s$. The expression is $2(s^6+3s^5+3s^4+s^3)=2\left(s(s+1)\right)^3=2(s^2+s)^3=2$, since $s^2+s=1$.")
fix(151,r"$|z_1|=\sqrt{11}$, $OB=\sqrt{\frac{11}3}$, and $\angle AOB=\frac\pi6$. $AB^2=11+\frac{11}3-2\cdot\frac{11}{\sqrt3}\cdot\frac{\sqrt3}2=\frac{11}3$, so $AB=OB$ (isosceles). Since $OA^2=11>OB^2+AB^2=\frac{22}3$, the angle at $B$ is obtuse. Area $=\frac{11}{4\sqrt3}$, so A and C are false.",
    stem=st(151).replace(r"\arg(z_1) + \frac{\pi}{2}",r"\arg(z_1) + \frac{\pi}{6}"))
ok(152,r"For $f=px^2+qx+b$: $f(x+y)-f(x)-f(y)=2pxy-b$. Matching gives $p=-\frac17$ and $b=-1$; then $2+3a=-\frac17$ gives $a=-\frac57$ and $q=\frac{a+2}{a-1}=-\frac34$. For $i\ge1$, $|f(i)|=\frac{i^2}7+\frac{3i}4+1$. $28\sum_{1}^{5}=28\left(\frac{55}7+\frac{45}4+5\right)=675$.")
drop(154,r"As transcribed, the local minima are $\frac73$ (at $x=0$) and $-\frac{11}{72}$ (at $x=\frac92$), summing to $\frac{157}{72}$. That matches no option and disagrees with the key.")
ok(155,r"$\frac{{}^nC_r}{{}^nC_{r-1}}=2$ and $\frac{{}^nC_{r+1}}{{}^nC_r}=\frac54$ give $n=8,r=3$, so $C=(1,0)$. Centroid: $3x-1=4\cos t+2\sin t$, $3y=4\sin t-2\cos t$. Squaring and adding: $(3x-1)^2+(3y)^2=16+4=20$.")
ok(156,r"The circle touches the x-axis at $(a,0)$ with centre $(a,-r)$: $x^2+y^2-2ax+2ry+a^2=0$, so $\alpha=2a$, $\beta=2r$, $\gamma=a^2$. The y-intercept is $2\sqrt{r^2-a^2}=b$, so $b^2=\beta^2-4\gamma$. Hence $(2a,b^2)=(\alpha,\beta^2-4\gamma)$.")
fix(157,r"For $f(x)=\frac{4^x}{4^x+2}$: $f(x)+f(1-x)=\frac{4^x}{4^x+2}+\frac{2}{2+4^x}=1$. Pairing $k$ with $82-k$ gives 40 pairs summing to 1, plus $f\left(\frac12\right)=\frac12$. Total $=\frac{81}2$.",
    stem=r"If $f(x) = \frac{4^x}{4^x + 2}$, $x \in \mathbb{R}$, then $\sum_{k=1}^{81} f\left(\frac{k}{82}\right)$ is equal to")
assert set(R)==set(S), set(S)-set(R)
for k,v in R.items():
    if v['verdict']=='fix' and 'stem' in v: assert v['stem']!=S[k]['stem'],k
json.dump(R,open('../pw_batch2.result.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
r=json.load(open('../pw_batch2.result.json',encoding='utf-8'))
from collections import Counter; print(len(r),Counter(v['verdict'] for v in r.values()))
