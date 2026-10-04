import json
R=json.load(open('r2.json',encoding='utf-8'))
def ok(ref,e): R[ref]={"verdict":"ok","explanation":e}
def fix(ref,e,stem=None,options=None):
    d={"verdict":"fix","explanation":e}
    if stem: d["stem"]=stem
    if options: d["options"]=options
    R[ref]=d
def drop(ref,r): R[ref]={"verdict":"drop","reason":r}
P="JEE Main 2025 Apr #"
ok(P+"105",r"Note $\omega_2=i\,\overline{\omega_1}$, so $\omega_1\omega_2=i|\omega_1|^2$: $\alpha=0$, $\beta=(8\sin\theta+7\cos\theta)^2+(\sin\theta+4\cos\theta)^2=65+60\sin2\theta$. Hence $p=125$, $q=5$, $p+q=130$.")
fix(P+"126",r"$g(x)=\frac{3x-2}{x-1}$ is decreasing, mapping $[2,4]$ onto $[\frac{10}3,4]$; $f'(x)=\frac{-11}{(5x+2)^2}<0$, so $f$ is decreasing. Range of $f\circ g$: $[f(4),f(\tfrac{10}3)]=[\tfrac12,\tfrac{29}{56}]$. Then $\beta-\alpha=\frac1{56}$, so the answer is $56$.",
    stem=r"Let $f, g: (1, \infty) \to \mathbb{R}$ be defined as $f(x) = \frac{2x+3}{5x+2}$ and $g(x) = \frac{2-3x}{1-x}$. If the range of the function $f\circ g: [2,4] \to \mathbb{R}$ is $[\alpha, \beta]$, then $\frac{1}{\beta - \alpha}$ is equal to:")
drop(P+"127",r"As transcribed $D=A\cap B$ is infinite; reading $A$ as $x^2+y^2=25$ gives $|D|=4$, $|C|=11$ and $7920$ one-one maps, not $17160$. Original sets uncertain.")
fix(P+"128",r"$A$: $5k-4$, $B$: $7k+2$. Common terms are $\equiv1\pmod5$ and $\equiv2\pmod7$: $16,51,86,\dots$ (step $35$) up to $\min(10121,14177)=10121$, giving $\lfloor\frac{10121-16}{35}\rfloor+1=289$ terms. $n(A\cup B)=2025+2025-289=3761$.",
    stem=r"Let $A = \{1, 6, 11, 16, \ldots\}$ and $B = \{9, 16, 23, 30, \ldots\}$ be the sets consisting of the first 2025 terms of two arithmetic progressions. Then $n(A \cup B)$ is:")
ok(P+"129",r"Total $\binom{16}{12}=1820$. Favourable (engineers, doctors, professors): $(3,1,8)$: $4\cdot2\cdot45=360$; $(3,2,7)$: $4\cdot1\cdot120=480$; $(4,1,7)$: $1\cdot2\cdot120=240$; $(4,2,6)$: $1\cdot1\cdot210=210$. Sum $1290$, probability $\frac{1290}{1820}=\frac{129}{182}$.")
fix(P+"130",r"$(x+y)^{2n-3}$ has $2n-2$ coefficients summing to $2^{2n-3}$, so $\frac{2^{2n-3}}{2n-2}=16$, giving $n=5$. Then $P=(9,5)$ and its distance from $x+y=8$ is $\frac{|9+5-8|}{\sqrt2}=3\sqrt2$.",
    stem=r"For an integer $n \ge 2$, if the arithmetic mean of all coefficients in the binomial expansion of $(x + y)^{2n-3}$ is $16$, then the distance of the point $P(2n-1, n^2-4n)$ from the line $x + y = 8$ is:")
fix(P+"131",r"$\vec b_1\times\vec b_2=(3,-1,1)\times(-3,2,4)=(-6,-15,3)$, magnitude $3\sqrt{30}$. With $\vec a_2-\vec a_1=(-6,-7-\alpha,\beta-3)$, the distance is $\frac{|15\alpha+3\beta+132|}{3\sqrt{30}}=3\sqrt{30}$, so $5\alpha+\beta+44=\pm90$. The positive value is $5\alpha+\beta=46$.",
    stem=r"Let the shortest distance between the lines $\frac{x-3}{3} = \frac{y-\alpha}{-1} = \frac{z-3}{1}$ and $\frac{x+3}{-3} = \frac{y+7}{2} = \frac{z-\beta}{4}$ be $3\sqrt{30}$. Then the positive value of $5\alpha + \beta$ is:")
fix(P+"132",r"Put $h=x-1$: numerator $=h(6+\lambda\cos h)-\mu\sin h=(6+\lambda-\mu)h+\left(\frac\mu6-\frac\lambda2\right)h^3+\dots$. So $6+\lambda-\mu=0$ and $\frac\mu6-\frac\lambda2=-1$, giving $\lambda=6$, $\mu=12$, $\lambda+\mu=18$.",
    stem=r"If $\displaystyle\lim_{x\to1} \frac{(x-1)\bigl(6 + \lambda \cos(x-1)\bigr) + \mu \sin(1-x)}{(x-1)^3} = -1$, where $\lambda, \mu \in \mathbb{R}$, then $\lambda + \mu$ is equal to:")
fix(P+"133",r"Write $e^{-x}f(x)=e^{-x}(1-2x)+\int_0^xe^{-t}f(t)\,dt$ and differentiate: $e^{-x}(f'-f)=e^{-x}(2x-3)+e^{-x}f$, so $f'=2f+2x-3$ with $f(0)=1$. Trying $f=Ax+B$ gives $f(x)=1-x$ (the $Ce^{2x}$ part vanishes). The region is a triangle with vertices $(0,0),(1,0),(0,1)$: area $\frac12$.",
    stem=r"Let $f: [0, \infty) \to \mathbb{R}$ be a differentiable function such that $f(x) = 1 - 2x + \int_0^x e^{x-t} f(t) \, dt$ for all $x \in [0, \infty)$. Then the area of the region bounded by $y = f(x)$ and the coordinate axes is:")
fix(P+"134",r"Foot: $(6+3t,7+2t,7-2t)$ with $(5+3t,5+2t,4-2t)\cdot(3,2,-2)=0\Rightarrow t=-1$, foot $F=(3,5,9)$. Since $|\vec d|=\sqrt{17}$, $A,B=F\pm2\vec d=(9,9,5)$ and $(-3,1,13)$. $\vec{OA}\cdot\vec{OB}=-27+9+65=47$.",
    stem=r"Let $A$ and $B$ be two distinct points on the line $L: \frac{x-6}{3} = \frac{y-7}{2} = \frac{z-7}{-2}$. Both $A$ and $B$ are at a distance $2\sqrt{17}$ from the foot of the perpendicular drawn from the point $(1, 2, 3)$ to the line $L$. If $O$ is the origin, then $\overrightarrow{OA} \cdot \overrightarrow{OB}$ is equal to:")
fix(P+"135",r"Telescoping $f(x)-f(\tfrac x2)=\tfrac x2$, $f(\tfrac x2)-f(\tfrac x4)=\tfrac x4,\dots$: $f(x)-f(\tfrac x{2^n})=x(1-2^{-n})\to x$. So $G(x)=x$ and $\sum_{r=1}^{10}G(r^2)=\sum r^2=385$.",
    stem=r"Let $f: \mathbb{R} \to \mathbb{R}$ be a continuous function satisfying $f(0) = 1$ and $f(2x) - f(x) = x$ for all $x \in \mathbb{R}$. If $\displaystyle\lim_{n\to\infty} \left[f(x) - f\left(\tfrac{x}{2^n}\right)\right] = G(x)$, then $\sum_{r=1}^{10} G(r^2)$ is equal to:")
fix(P+"136",r"Odd-position terms are $(4k-3)^2$ and even-position terms are $4k-1$, $k=1,\dots,20$. $\sum(4k-3)^2=16\cdot2870-24\cdot210+9\cdot20=41060$ and $\sum(4k-1)=840-20=820$. Total $41880$.",
    stem=r"$1 + 3 + 5^2 + 7 + 9^2 + \dots$ up to 40 terms is equal to:")
fix(P+"137",r"$\frac{T_{15}\text{ (start)}}{T_{15}\text{ (end)}}=\left(\frac{2^{1/3}}{3^{-1/3}}\right)^{n-28}=6^{(n-28)/3}=\frac16$, so $n-28=-3$, $n=25$. Then $\binom{25}3=2300$.",
    stem=r"In the expansion of $\left(\sqrt[3]{2} + \frac{1}{\sqrt[3]{3}}\right)^n$, $n \in \mathbb{N}$, if the ratio of the 15th term from the beginning to the 15th term from the end is $\tfrac{1}{6}$, then the value of $\binom{n}{3}$ is:")
fix(P+"138",r"Let $x=\sin\theta$, $\theta\in(-\frac\pi6,\frac\pi4)$. The argument is $\sin\theta\cos\frac\pi6+\cos\theta\sin\frac\pi6=\sin(\theta+\frac\pi6)$, and $\theta+\frac\pi6\in(0,\frac{5\pi}{12})\subset[-\frac\pi2,\frac\pi2]$. So the value is $\frac\pi6+\sin^{-1}x$.",
    stem=r"Considering the principal values of the inverse trigonometric functions, $\sin^{-1}\left(\tfrac{\sqrt{3}}{2}x + \tfrac{1}{2}\sqrt{1-x^2}\right)$, $-\tfrac{1}{2} < x < \tfrac{1}{\sqrt{2}}$, is equal to:")
fix(P+"139",r"$\cos\theta=\frac{5}{\sqrt{10}\sqrt{5+\lambda^2}}=\frac{\sqrt5}{2\sqrt7}\Rightarrow5+\lambda^2=14$, $\lambda=3$. Since $\vec v_1\perp\vec v_2$, $|\vec v_1|^2+|\vec v_2|^2=|\vec v|^2=14$. Trap: computing the projections separately is unnecessary.",
    stem=r"Consider two vectors $\vec{u}=3\hat{i}-\hat{j}$ and $\vec{v}=2\hat{i}+\hat{j}-\lambda\hat{k}$, $\lambda > 0$. The angle between them is given by $\cos^{-1}\left(\tfrac{\sqrt{5}}{2\sqrt{7}}\right)$. Let $\vec{v}=\vec{v}_1+\vec{v}_2$, where $\vec{v}_1$ is parallel to $\vec{u}$ and $\vec{v}_2$ is perpendicular to $\vec{u}$. Then the value of $|\vec{v}_1|^2 + |\vec{v}_2|^2$ is:")
fix(P+"140",r"$4x-7y+10=0$ and $7x+4y=15$ are perpendicular (slopes $\frac47,-\frac74$), so the triangle is right-angled at their intersection $(1,2)$, which is its orthocentre. The second triangle is right-angled at the origin, orthocentre $(0,0)$. Distance $=\sqrt5$.",
    stem=r"Let the three sides of a triangle be on the lines $4x - 7y + 10 = 0$, $x + y = 5$, and $7x + 4y = 15$. Then the distance of its orthocentre from the orthocentre of the triangle formed by the lines $x = 0$, $y = 0$, and $x + y = 1$ is:")
drop(P+"141",r"As transcribed the integral equals $1+\int_{-1}^1\sqrt{|x|}\,dx=\frac73$, matching no option (key $1+\frac{2\sqrt2}{3}$); stem likely garbled.")
fix(P+"142",r"Distance between foci $2c=8$, $c=4$; $e=\frac45\Rightarrow a=5$, $b^2=25-16=9$. Latus rectum $=\frac{2b^2}a=\frac{18}5$.",
    stem=r"The length of the latus-rectum of the ellipse whose foci are $(2,5)$ and $(2,-3)$ and eccentricity is $\tfrac{4}{5}$ is:")
fix(P+"143",r"Roots are integers iff $(x+2)^2=n+4$ has integer solutions, i.e. $n+4$ is a perfect square. For $n\in[20,100]$: $n+4\in\{25,36,49,64,81,100\}$, so $6$ values.",
    stem=r"Consider the equation $x^2 + 4x - n = 0$, where $n \in [20,100]$ is a natural number. Then the number of all distinct values of $n$, for which the given equation has integral roots, is equal to:")
ok(P+"144",r"$P(X=0)=\frac{21}{45}$, $P(X=1)=\frac{21}{45}$, $P(X=2)=\frac3{45}$. $E[X]=\frac{27}{45}=\frac35$, $E[X^2]=\frac{33}{45}=\frac{11}{15}$. $\mathrm{Var}=\frac{11}{15}-\frac9{25}=\frac{28}{75}$. Trap: answering $E[X^2]=\frac{11}{15}$.")

src=json.load(open('../pw_batch5.json',encoding='utf-8'))
refs=[x['ref'] for x in src]
missing=[r for r in refs if r not in R]; extra=[r for r in R if r not in refs]
print('missing',missing,'extra',extra)
out={r:R[r] for r in refs}
json.dump(out,open('../pw_batch5.result.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
chk=json.load(open('../pw_batch5.result.json',encoding='utf-8'))
from collections import Counter
print(len(chk),Counter(v['verdict'] for v in chk.values()))
