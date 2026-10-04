import json
src=json.load(open('../eq_batch3.json',encoding='utf-8'))
R={}
def ok(ref,e): R[ref]={"verdict":"ok","explanation":e}
def fix(ref,stem,opts,e): R[ref]={"verdict":"fix","stem":stem,"options":opts,"explanation":e}
def drop(ref,r): R[ref]={"verdict":"drop","reason":r}
S={x['ref']:x for x in src}
def O(ref): return dict(S[ref]['options'])

fix("M-24-Q13", r"Angles A, B and C of a triangle ABC are in A.P. With the usual notations, if $\frac{b}{c} = \frac{\sqrt{3}}{\sqrt{2}}$ and $\angle C = \frac{\pi}{4}$, then angle A is equal to", O("M-24-Q13"),
 r"Since $A, B, C$ are in A.P., $B = \frac{\pi}{3}$. Check with the sine rule: $\frac{b}{c} = \frac{\sin B}{\sin C} = \frac{\sqrt{3}/2}{1/\sqrt{2}} = \frac{\sqrt{3}}{\sqrt{2}}$, consistent. Hence $A = \pi - \frac{\pi}{3} - \frac{\pi}{4} = \frac{5\pi}{12}$.")
fix("M-28-Q17", r"The equation of the line passing through $(-4, 3, 1)$, parallel to the plane $x + 2y - z - 5 = 0$ and intersecting the line $\frac{x + 1}{-3} = \frac{y - 3}{2} = \frac{z - 2}{-1}$ is", O("M-28-Q17"),
 r"A general point of the given line is $(-3\lambda - 1, 2\lambda + 3, 2 - \lambda)$, so the direction from $(-4,3,1)$ is $(3 - 3\lambda, 2\lambda, 1 - \lambda)$. Parallel to the plane: $(3 - 3\lambda) + 4\lambda - (1 - \lambda) = 0 \Rightarrow \lambda = -1$, giving direction $(6, -2, 2) \propto (3, -1, 1)$. Hence $\frac{x + 4}{3} = \frac{y - 3}{-1} = \frac{z - 1}{1}$. Options A and C are also parallel to the plane but do not meet the given line.")
fix("M-11-Q16", r"If $f(x) = \begin{cases} 3x - 1, & x \geq 1 \\ 2x + 3, & x < 1 \end{cases}$ and $g(x) = \begin{cases} 3 - x, & x < 2 \\ 2x - 3, & x \geq 2 \end{cases}$, then $\lim_{x \to 2} f(g(x)) =$", O("M-11-Q16"),
 r"As $x \to 2^-$, $g(x) = 3 - x \to 1^+$; as $x \to 2^+$, $g(x) = 2x - 3 \to 1^+$. So $g(x) \to 1^+$ from both sides and $\lim f(g(x)) = \lim_{u \to 1^+} (3u - 1) = 2$. Using $f(1^-) = 5$ would be wrong since $g$ approaches 1 from above.")
drop("M-22-Q9","Region A is missing from the stem (set definition lost); question cannot be solved as written.")
ok("M-28-Q5", r"Without restriction: $\binom{7}{3}\binom{5}{2} = 35 \times 10 = 350$ teams. Teams containing both A and B: choose 1 more boy from 5 and 2 girls: $\binom{5}{1}\binom{5}{2} = 50$. Required number $= 350 - 50 = 300$.")
fix("M-17-Q14", r"Let $f(x) = a^x$ $(a > 0)$ be written as $f(x) = g(x) + h(x)$, where $g(x)$ is an even function and $h(x)$ is an odd function. Then the value of $g(x + y) + g(x - y)$ is", O("M-17-Q14"),
 r"The even part is $g(x) = \frac{a^x + a^{-x}}{2}$. Then $g(x+y) + g(x-y) = \frac{1}{2}\left(a^{x+y} + a^{-x-y} + a^{x-y} + a^{y-x}\right) = \frac{1}{2}(a^x + a^{-x})(a^y + a^{-y}) = 2g(x)g(y)$.")
o=O("M-20-Q16"); o["D"]=r"Both $\frac{\pi}{6}$ and $\frac{5\pi}{6}$"
fix("M-20-Q16", S["M-20-Q16"]["stem"], o,
 r"The principal value branch of $\sin^{-1}$ is $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$. The only angle there with $\sin\theta = \frac{1}{2}$ is $\theta = \frac{\pi}{6}$. Although $\sin\frac{5\pi}{6} = \frac{1}{2}$, $\frac{5\pi}{6}$ lies outside the principal range.")
fix("M-11-Q13", r"An urn contains 5 red and 2 green balls. One ball is drawn from the urn; if it is red, a green ball is put into the urn, and if it is green, a red ball is put into the urn (the drawn ball is not returned). A second ball is then drawn. The probability that it is red is", O("M-11-Q13"),
 r"If the first ball is red (prob. $\frac{5}{7}$), the urn becomes 4 red, 3 green, so $P(R_2) = \frac{4}{7}$. If the first is green (prob. $\frac{2}{7}$), it becomes 6 red, 1 green, so $P(R_2) = \frac{6}{7}$. Total: $\frac{5}{7}\cdot\frac{4}{7} + \frac{2}{7}\cdot\frac{6}{7} = \frac{20 + 12}{49} = \frac{32}{49}$.")
fix("M-17-Q5", r"If $f(x) = \frac{x - 1}{x + 1}$, then $f(f(ax))$ is equal to", O("M-17-Q5"),
 r"$f(f(u)) = \frac{\frac{u-1}{u+1} - 1}{\frac{u-1}{u+1} + 1} = \frac{-2}{2u} = -\frac{1}{u}$, so $f(f(ax)) = -\frac{1}{ax}$. Also $\frac{f(x) - 1}{f(x) + 1} = \frac{-2/(x+1)}{2x/(x+1)} = -\frac{1}{x}$, so option C equals $-\frac{1}{ax}$. Option A has the wrong sign.")
fix("M-07-Q20", r"In an equilateral triangle ABC, $r$, $R$, $r_1$ form (where the symbols have their usual meanings)", {"A":"an A.P.","B":"an H.P.","C":"a G.P.","D":"an A.G.P."},
 r"For side $a$: $\Delta = \frac{\sqrt{3}}{4}a^2$, $s = \frac{3a}{2}$. Then $r = \frac{\Delta}{s} = \frac{a}{2\sqrt{3}}$, $R = \frac{a}{\sqrt{3}} = \frac{2a}{2\sqrt{3}}$, $r_1 = \frac{\Delta}{s - a} = \frac{3a}{2\sqrt{3}}$. These are in the ratio $1 : 2 : 3$, so they form an A.P. (not a G.P., since $2^2 \neq 1 \cdot 3$).")
fix("M-24-Q10", r"In a triangle ABC, if the area $\Delta = a^2 - (b - c)^2$, then $\tan A$ is", O("M-24-Q10"),
 r"$a^2 - (b-c)^2 = (a - b + c)(a + b - c) = 4(s-b)(s-c)$. Since $\tan\frac{A}{2} = \frac{(s-b)(s-c)}{\Delta}$, we get $\tan\frac{A}{2} = \frac{1}{4}$. Then $\tan A = \frac{2 \cdot \frac{1}{4}}{1 - \frac{1}{16}} = \frac{8}{15}$.")
fix("M-18-Q20", r"If the numerically greatest term in the expansion of $(1 - x)^{21}$ $(x > 0)$ has the numerically greatest coefficient, then the complete set of values of $x$ is", O("M-18-Q20"),
 r"The greatest coefficients are $\binom{21}{10} = \binom{21}{11}$, so the unique greatest term must be $T_{11}$ or $T_{12}$. $|T_{11}| > |T_{10}|$ requires $\frac{12}{10}x > 1$, i.e. $x > \frac{5}{6}$; $|T_{12}| > |T_{13}|$ requires $\frac{10}{12}x < 1$, i.e. $x < \frac{6}{5}$. Hence $x \in \left(\frac{5}{6}, \frac{6}{5}\right)$. At the endpoints a term with a smaller coefficient ties for greatest, so the closed interval is excluded.")
drop("M-26-Q25","Stem is garbled (Hindi mojibake) and mismatched: asks for gradient of a common tangent while options/solution concern a parabola's directrix.")
fix("M-07-Q14", r"Let the area of $\Delta ABC$ be 8 square units. Then the value of the expression $E = b^2\sin 2C + c^2\sin 2B$ is equal to", O("M-07-Q14"),
 r"Using $\sin C = \frac{2\Delta}{ab}$ and $\sin B = \frac{2\Delta}{ac}$: $E = 2b^2\sin C\cos C + 2c^2\sin B\cos B = \frac{4\Delta}{a}(b\cos C + c\cos B)$. By the projection formula $b\cos C + c\cos B = a$, so $E = 4\Delta = 32$.")
fix("M-16-Q7", r"If $\log_{0.3}(x - 1) < \log_{0.09}(x - 1)$, then $x$ lies in the interval", O("M-16-Q7"),
 r"Let $L = \log_{0.3}(x-1)$; since $0.09 = 0.3^2$, the right side is $\frac{L}{2}$. So $L < \frac{L}{2} \Rightarrow L < 0 \Rightarrow x - 1 > 1$ (base $< 1$). Thus $x \in (2, \infty)$. For $x \in (1,2)$, $L > 0$ and the inequality fails.")
drop("M-12-Q8","Stem truncated ('the value of f' - argument missing) and option A is junk ('be').")
drop("M-11-Q14","Own solution gives third side through (35/2, -10) with slope +13/61, i.e. option C; key B has slope -13/61. Key appears wrong.")
fix("M-09-Q17", r"The mean of 200 observations is 48 and their standard deviation is 3. Then the sum of the squares of all the observations is", O("M-09-Q17"),
 r"$\sigma^2 = \frac{\sum x^2}{n} - \bar{x}^2 \Rightarrow 9 = \frac{\sum x^2}{200} - 48^2$. So $\sum x^2 = 200(9 + 2304) = 200 \times 2313 = 462600$.")
fix("M-06-Q6", r"If $f(x) = x^2 + 2bx + 2c^2$ and $g(x) = -x^2 - 2cx + b^2$ are such that $\min f(x) > \max g(x)$, then the relation between $b$ and $c$ is", {"A":"No relation","B":r"$0 < c < \frac{b}{2}$","C":r"$c^2 < 2b$","D":r"$c^2 > 2b^2$"},
 r"$f(x) = (x + b)^2 + 2c^2 - b^2$, so $\min f = 2c^2 - b^2$. $g(x) = -(x + c)^2 + b^2 + c^2$, so $\max g = b^2 + c^2$. Then $2c^2 - b^2 > b^2 + c^2 \Rightarrow c^2 > 2b^2$.")
fix("M-24-Q12", r"In a $\Delta ABC$, if $\frac{s - a}{11} = \frac{s - b}{12} = \frac{s - c}{13}$, then $\tan^2\frac{A}{2}$ is equal to", O("M-24-Q12"),
 r"Each ratio equals $\frac{3s - (a+b+c)}{36} = \frac{s}{36}$, so $s - a = 11k$, $s - b = 12k$, $s - c = 13k$, $s = 36k$. Then $\tan^2\frac{A}{2} = \frac{(s-b)(s-c)}{s(s-a)} = \frac{12 \cdot 13}{36 \cdot 11} = \frac{13}{33}$.")
fix("M-17-Q19", r"If the trivial solution is the only solution of the system of equations $x - ky + z = 0$, $kx + 3y - kz = 0$, $3x + y - z = 0$, then the set of all values of $k$ is", {"A":r"$\mathbb{R} - \{2\}$","B":r"$\mathbb{R} - \{-3\}$","C":r"$\mathbb{R} - \{2, -3\}$","D":r"$\{-2, -3\}$"},
 r"For only the trivial solution, the coefficient determinant must be non-zero: $\begin{vmatrix} 1 & -k & 1 \\ k & 3 & -k \\ 3 & 1 & -1 \end{vmatrix} = (k - 3) + 2k^2 + (k - 9) = 2(k + 3)(k - 2)$. So $k \neq 2, -3$, i.e. $k \in \mathbb{R} - \{2, -3\}$.")
fix("M-11-Q3", r"If $\lim_{n \to \infty} \frac{\left(\sum_{r=1}^{2n}\sqrt{r}\right)\left(\sum_{r=1}^{2n}\frac{1}{\sqrt{r}}\right)}{4\sum_{r=1}^{n} r} = \frac{\lambda}{3}$, then $\lambda =$", O("M-11-Q3"),
 r"The denominator is $2n(n+1)$. Writing as Riemann sums, $\frac{1}{n}\sum_{r=1}^{2n}\sqrt{\frac{r}{n}} \to \int_0^2\sqrt{x}\,dx = \frac{4\sqrt{2}}{3}$ and $\frac{1}{n}\sum_{r=1}^{2n}\frac{1}{\sqrt{r/n}} \to \int_0^2\frac{dx}{\sqrt{x}} = 2\sqrt{2}$. The limit is $\frac{1}{2}\cdot\frac{4\sqrt{2}}{3}\cdot 2\sqrt{2} = \frac{8}{3}$, so $\lambda = 8$.")
fix("M-20-Q13", r"If $y = \sin^{-1}(3x - 4x^3)$, then the number of points in $(-1, 1)$ where $y$ is not differentiable is", O("M-20-Q13"),
 r"$y' = \frac{3(1 - 4x^2)}{\sqrt{1 - (3x - 4x^3)^2}} = \frac{3(1 - 4x^2)}{|1 - 4x^2|\sqrt{1 - x^2}}$. This equals $\frac{3}{\sqrt{1-x^2}}$ for $|x| < \frac{1}{2}$ and $-\frac{3}{\sqrt{1-x^2}}$ for $\frac{1}{2} < |x| < 1$, so the derivative jumps at $x = \pm\frac{1}{2}$. Hence there are 2 such points in $(-1, 1)$.")
fix("M-18-Q8", r"If $g(x) = \sin^2 x + \sin^2\left(\frac{\pi}{3} + x\right) + \cos x\cos\left(x + \frac{\pi}{3}\right)$ and $f\left(\frac{5}{4}\right) = 2$, then $f(g(5))$ is equal to", O("M-18-Q8"),
 r"Simplifying, $g(x) = 1 - \cos\left(2x + \frac{\pi}{3}\right)\cos\frac{\pi}{3} + \frac{1}{2}\left[\cos\left(2x + \frac{\pi}{3}\right) + \cos\frac{\pi}{3}\right] = 1 + \frac{1}{4} = \frac{5}{4}$ for all $x$. So $g(5) = \frac{5}{4}$ and $f(g(5)) = f\left(\frac{5}{4}\right) = 2$.")
ok("M-20-Q8", r"For $y = \frac{c^3}{x^2}$, $y' = -\frac{2c^3}{x^3}$. The tangent at $(x_1, y_1)$ has $x$-intercept $a = x_1 + \frac{x_1}{2} = \frac{3x_1}{2}$ and $y$-intercept $b = y_1 + \frac{2c^3}{x_1^2} = \frac{3c^3}{x_1^2}$. Hence $a^2 b = \frac{9x_1^2}{4}\cdot\frac{3c^3}{x_1^2} = \frac{27}{4}c^3$.")
ok("M-24-Q8", r"Since $R = \frac{abc}{4\Delta}$, $2R\Delta = \frac{abc}{2} = \frac{2 \times 9}{2} = 9$.")
fix("M-07-Q13", r"In a triangle ABC, the equations of the medians AD and BE are $2x + 3y = 6$ and $3x - 2y = 10$ respectively. If $AD = 6$ and $BE = 11$, then the area of $\Delta ABC$ is equal to", O("M-07-Q13"),
 r"The slopes $-\frac{2}{3}$ and $\frac{3}{2}$ show $AD \perp BE$. With centroid $G$, $AG = \frac{2}{3}AD = 4$ and $AG \perp BE$, so $\text{Area}(\Delta ABE) = \frac{1}{2} \cdot BE \cdot AG = \frac{1}{2}\cdot 11 \cdot 4 = 22$. Since median $BE$ halves the triangle, $\text{Area}(\Delta ABC) = 2 \times 22 = 44$.")
fix("M-06-Q11", r"If $a, b, p, q$ are non-zero real numbers, then the two equations $2a^2x^2 - 2abx + b^2 = 0$ and $p^2x^2 + 2pqx + q^2 = 0$ have", {"A":"No common root","B":r"One common root if $2a^2 + b^2 = p^2 + q^2$","C":r"Two common roots if $3pq = 2ab$","D":r"Two common roots if $3qb = 2ap$"},
 r"For the first equation, $D = 4a^2b^2 - 8a^2b^2 = -4a^2b^2 < 0$, so its roots are non-real. The second is $(px + q)^2 = 0$, with the real root $x = -\frac{q}{p}$. A real root cannot equal a non-real root, so there is no common root.")
ok("M-16-Q10", r"Let $f(x) = x^2 + ax - 4$. Since $f(0) = -4 < 0$, the roots lie on opposite sides of 0, so the smaller root is negative. It lies in $(-1, 2)$ iff it lies in $(-1, 0)$, i.e. $f(-1) > 0$: $1 - a - 4 > 0 \Rightarrow a < -3$. Hence $a \in (-\infty, -3)$.")
fix("M-06-Q13", r"The first term of an A.P. of consecutive integers is $p^2 + 1$. The sum of $(2p + 1)$ terms of this series can be expressed as", {"A":r"$(p + 1)^2$","B":r"$(2p + 1)(p + 1)^2$","C":r"$(p + 1)^3$","D":r"$p^3 + (p + 1)^3$"},
 r"With $a = p^2 + 1$, $d = 1$, $n = 2p + 1$: $S = \frac{2p + 1}{2}\left[2(p^2 + 1) + 2p\right] = (2p + 1)(p^2 + p + 1) = 2p^3 + 3p^2 + 3p + 1 = p^3 + (p + 1)^3$.")
ok("M-05-Q12", r"$\frac{1}{\log_{\sqrt{bc}}(abc)} = \log_{abc}\sqrt{bc}$, etc. The sum is $\frac{1}{2}\log_{abc}(bc \cdot ca \cdot ab) = \frac{1}{2}\log_{abc}(abc)^2 = 1$.")
fix("M-22-Q19", r"Let $I = \int_a^b \left(x^4 - 2x^2\right)dx$. If $I$ is minimum, then the ordered pair $(a, b)$ is", O("M-22-Q19"),
 r"$I$ is smallest when we integrate exactly over the region where the integrand is negative, with $a < b$. $x^4 - 2x^2 = x^2(x^2 - 2) < 0$ for $-\sqrt{2} < x < \sqrt{2}$, so $(a, b) = (-\sqrt{2}, \sqrt{2})$. Option B reverses the limits, which makes $I$ positive.")
fix("M-16-Q11", r"The value of $b$ for which the equation $2\log_{1/25}(bx + 28) = -\log_5(12 - 4x - x^2)$ has coincident real roots is", O("M-16-Q11"),
 r"$2\log_{1/25}(bx + 28) = -\log_5(bx + 28)$, so $bx + 28 = 12 - 4x - x^2 > 0$, i.e. $x^2 + (b + 4)x + 16 = 0$. For equal roots, $(b + 4)^2 = 64 \Rightarrow b = 4$ or $-12$. For $b = 4$, $x = -4$ and $12 - 4x - x^2 = 12 > 0$, which is valid. For $b = -12$, $x = 4$ gives $12 - 16 - 16 < 0$, outside the domain. So $b = 4$ only, and option C is wrong.")
ok("M-13-Q18", r"In the region $y^2 = x$ requires $x \geq 0$, where $y = |x| = x$. The curves $y = \sqrt{x}$ and $y = x$ meet at $x = 0, 1$. Area $= \int_0^1(\sqrt{x} - x)\,dx = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}$.")
fix("M-08-Q6", r"The total number of ways in which 15 identical blankets can be distributed among 4 persons so that each of them gets at least two blankets is", O("M-08-Q6"),
 r"First give 2 blankets to each person, leaving 7. Distributing 7 identical blankets among 4 persons with no restriction gives $\binom{7 + 3}{3} = \binom{10}{3} = 120$ ways.")
ok("M-20-Q15", r"Put $\sqrt{x} = t$, so $\frac{dx}{2\sqrt{x}} = dt$. The integral becomes $2\int a^t\,dt = \frac{2a^t}{\ln a} + C = 2a^{\sqrt{x}}\log_a e + C$. Option A multiplies by $\log_e a$ instead of dividing.")
fix("M-01-Q1", r"Let $f(x) = \operatorname{sgn}(x^2 - 4|x| + k)$. If $f(x)$ is discontinuous at exactly four points, then the range of $k$ is", O("M-01-Q1"),
 r"$f$ is discontinuous where $x^2 - 4|x| + k$ changes sign, so we need 4 distinct real roots. That means $t^2 - 4t + k = 0$ (with $t = |x|$) must have two distinct positive roots: $16 - 4k > 0$ and $k > 0$. So $k \in (0, 4)$. At $k = 0$ the roots are only $0, \pm 4$.")
ok("M-23-Q8", r"Since both sets share the mean 5, the combined mean is also 5 and the combined variance is $\frac{n_1\sigma_1^2 + n_2\sigma_2^2}{n_1 + n_2} = \frac{10 \cdot 4 + 20 \cdot 9}{30} = \frac{22}{3}$. So $\sigma = \sqrt{\frac{22}{3}}$.")
fix("M-09-Q14", r"If $\lim_{x \to 1}\frac{1 - x + \ln x}{1 + \cos\pi x} = L$, then $|[17L]|$ equals (where $[\cdot]$ denotes the greatest integer function)", O("M-09-Q14"),
 r"Put $x = 1 + h$: the numerator is $-h + \ln(1 + h) \approx -\frac{h^2}{2}$ and the denominator is $1 - \cos\pi h \approx \frac{\pi^2h^2}{2}$. So $L = -\frac{1}{\pi^2}$ and $17L \approx -1.72$. Then $[17L] = -2$ and $|[17L]| = 2$. Taking $[1.72] = 1$ (ignoring the sign) would be the trap.")
fix("M-12-Q5", r"If the twice differentiable function $f(x)$ is the inverse of $g(x)$, then $f''(g(x))$ is equal to", O("M-12-Q5"),
 r"From $f(g(x)) = x$: $f'(g(x))\,g'(x) = 1 \Rightarrow f'(g(x)) = \frac{1}{g'(x)}$. Differentiating again: $f''(g(x))\,g'(x) = -\frac{g''(x)}{(g'(x))^2}$, so $f''(g(x)) = -\frac{g''(x)}{(g'(x))^3}$. Option B forgets the extra factor of $g'(x)$.")
ok("M-24-Q16", r"$a^2 = b^2 + c^2 - 2bc\cos A = 4 + 3 - 2\cdot 2\sqrt{3}\cdot\frac{\sqrt{3}}{2} = 1$, so $a = 1$. Then $R = \frac{a}{2\sin A} = \frac{1}{2 \cdot \frac{1}{2}} = 1$.")
fix("M-16-Q1", r"Let $(x_0, y_0)$ be the solution of the equations $(2x)^{\ln 2} = (3y)^{\ln 3}$ and $3^{\ln x} = 2^{\ln y}$. Then $x_0$ is", O("M-16-Q1"),
 r"Let $X = \ln x$, $Y = \ln y$. Taking logs: $\ln 2(\ln 2 + X) = \ln 3(\ln 3 + Y)$ and $X\ln 3 = Y\ln 2$, so $Y = \frac{X\ln 3}{\ln 2}$. Substituting gives $X\cdot\frac{(\ln 2)^2 - (\ln 3)^2}{\ln 2} = (\ln 3)^2 - (\ln 2)^2$, so $X = -\ln 2$ and $x_0 = \frac{1}{2}$.")
fix("M-13-Q17", r"The value of $\int_0^{2\pi} x\sin^6 x\cos^4 x\,dx$ is equal to", O("M-13-Q17"),
 r"Using $x \to 2\pi - x$: $2I = 2\pi\int_0^{2\pi}\sin^6 x\cos^4 x\,dx = 8\pi\int_0^{\pi/2}\sin^6 x\cos^4 x\,dx$. By the Wallis formula, $\int_0^{\pi/2}\sin^6 x\cos^4 x\,dx = \frac{5\cdot3\cdot1\cdot3\cdot1}{10\cdot8\cdot6\cdot4\cdot2}\cdot\frac{\pi}{2} = \frac{3\pi}{512}$. So $I = 4\pi\cdot\frac{3\pi}{512} = \frac{3\pi^2}{128}$.")
ok("M-16-Q9", r"$2x^2 + 3x + 4 = 0$ has discriminant $9 - 32 < 0$, so its roots are a non-real conjugate pair. A real-coefficient quadratic sharing one of them shares both, so $\frac{a}{2} = \frac{b}{3} = \frac{c}{4} = k$. Then $a + b + c = 9k$, and the least value in $\mathbb{N}$ is 9 (at $k = 1$).")
ok("M-24-Q19", r"$r_1, r_2, r_3$ in H.P. means $\frac{1}{r_1} = \frac{s-a}{\Delta}$, $\frac{s-b}{\Delta}$, $\frac{s-c}{\Delta}$ are in A.P. So $s - a, s - b, s - c$ are in A.P., hence $a, b, c$ are in A.P. Then $2b = a + c$ and $\frac{a + c}{b} = 2$.")
fix("M-09-Q15", r"The least positive integral value of $b$ for which the function $f(x) = 2bx - 3\sin x + c$ is monotonically increasing for all $x \in \mathbb{R}$ is", O("M-09-Q15"),
 r"We need $f'(x) = 2b - 3\cos x \geq 0$ for all $x$, i.e. $2b \geq 3$, so $b \geq \frac{3}{2}$. The least positive integer is $b = 2$; $b = 1$ fails because $2 - 3\cos x < 0$ near $x = 0$.")
ok("M-17-Q16", r"Since $M^2 = M$, $M^k = M$ for all $k \geq 1$. Then $(I + M)^3 = I + 3M + 3M^2 + M^3 = I + 7M$, so $(I + M)^3 - 7M = I$.")
ok("M-22-Q12", r"Take $C = (t^2, 2t)$ with $-2 < t < 3$ (arc through O). Area $= \frac{1}{2}\left|\begin{vmatrix} 4 & -4 & 1 \\ 9 & 6 & 1 \\ t^2 & 2t & 1 \end{vmatrix}\right| = 30 + 5t - 5t^2$. This is maximised at $t = \frac{1}{2}$, giving $30 + \frac{5}{2} - \frac{5}{4} = 31\frac{1}{4}$.")
ok("M-12-Q11", r"Integrating by parts, $\int f g''\,dx = f g' - \int f' g'\,dx$ and $\int f'' g\,dx = f' g - \int f' g'\,dx$. Subtracting cancels the $\int f'g'$ terms: $\int(fg'' - f''g)\,dx = f(x)g'(x) - f'(x)g(x) + C$. Option B has the opposite sign.")
drop("M-07-Q7","Key is wrong: for p=F, r=F the statement is (T) -> (T -> F) = F, so it is not a tautology (nor a contradiction); correct answer would be D, not A.")
ok("M-22-Q1", r"$\sum_{i=1}^5 x_i = 750$ and $\sum x_i^2 = 5(150^2 + 18) = 112590$. With the new student, $\sum x = 906$ (mean 151) and $\sum x^2 = 112590 + 156^2 = 136926$. The variance is $\frac{136926}{6} - 151^2 = 22821 - 22801 = 20$.")
ok("M-12-Q17", r"$y' = 20x(3x^4 - 6x^3 + 3x^2 - 4)$. Let $g(x) = 3x^4 - 6x^3 + 3x^2 - 4 = 3x^2(x - 1)^2 - 4$. Then $g(0) = -4 < 0$ and $g \to \infty$ at both ends, so $g$ has exactly one negative root $\alpha$ and one root $\beta > 1$. The sign of $y'$ goes $-, +, -, +$ across $\alpha, 0, \beta$, so the minima are at $\alpha$ and $\beta$ and the maximum is at 0: 2 points of minima.")
fix("M-19-Q4", r"$\lim_{x \to 0}\frac{\ln\left(\tan\left(\frac{\pi}{4} + ax\right)\right)}{\sin bx}$, $b \neq 0$, is equal to", O("M-19-Q4"),
 r"$\tan\left(\frac{\pi}{4} + ax\right) = \frac{1 + \tan ax}{1 - \tan ax} = 1 + \frac{2\tan ax}{1 - \tan ax}$. So the numerator is $\approx \frac{2\tan ax}{1 - \tan ax} \approx 2ax$ and the denominator is $\approx bx$. The limit is $\frac{2a}{b}$.")
o=O("M-13-Q1"); o["C"]=r"$2\pi$"
fix("M-13-Q1", r"The value of $I = \int_{-1}^{1}\left(\cos^{-1}x + \frac{x^7 - 3x^5 + 7x^3 - x}{\cos^2 x}\right)dx$ is", o,
 r"The second term is an odd function, so its integral over $[-1, 1]$ is 0. For the first, $\cos^{-1}x + \cos^{-1}(-x) = \pi$, so $2\int_{-1}^1\cos^{-1}x\,dx = \int_{-1}^1 \pi\,dx = 2\pi$, giving $\int_{-1}^1\cos^{-1}x\,dx = \pi$. Hence $I = \pi$.")
ok("M-20-Q17", r"Since $\sin^{-1}u + \cos^{-1}u = \frac{\pi}{2}$, we get $\sin^{-1}\frac{4}{x} = \cos^{-1}\frac{3}{x}$. This requires $\frac{3}{x} \geq 0$ and $\frac{4}{x} = \sqrt{1 - \frac{9}{x^2}}$, so $x^2 = 25$ with $x > 0$, i.e. $x = 5$. For $x = -5$ the left side equals $-\frac{\pi}{2}$.")
ok("M-09-Q16", r"Sorted: 34, 38, 42, 44, 46, 48, 54, 55, 63, 70; median $= \frac{46 + 48}{2} = 47$. The absolute deviations are 13, 9, 5, 3, 1, 1, 7, 8, 16, 23, with sum 86. Mean deviation $= \frac{86}{10} = 8.6$.")
fix("M-19-Q16", r"If $H_1, H_2, H_3, \ldots, H_{2n+1}$ are in H.P., then $\sum_{i=1}^{2n}(-1)^i\left(\frac{H_i + H_{i+1}}{H_i - H_{i+1}}\right)$ is equal to", O("M-19-Q16"),
 r"Let $\frac{1}{H_i} = A + (i-1)k$. Dividing by $H_iH_{i+1}$: $\frac{H_i + H_{i+1}}{H_i - H_{i+1}} = \frac{\frac{1}{H_{i+1}} + \frac{1}{H_i}}{k} = \frac{2A + (2i - 1)k}{k}$. Over $i = 1, \ldots, 2n$, $\sum(-1)^i\frac{2A}{k} = 0$, and $\sum(-1)^i(2i - 1)$ consists of $n$ pairs each equal to 2. The sum is $2n$.")
ok("M-16-Q19", r"Let $T_m = AR^{m-1}$. Then $AR^{2p-1} = q^2$ and $AR^{2q-1} = p^2$. Multiplying: $(AR^{p+q-1})^2 = p^2q^2$, so $T_{p+q} = pq$ (taking the positive value; $-pq$ is not among the options).")
o={"A":r"$\log_{10}\pi$","B":r"$\sqrt{\log_{10}\pi^2}$","C":r"$\left(\frac{1}{\log_{10}\pi}\right)^3$","D":r"$\frac{1}{\log_{10}\sqrt{\pi}}$"}
fix("M-05-Q15", S["M-05-Q15"]["stem"], o,
 r"Let $t = \log_{10}\pi \approx 0.497$. Then option B $= \sqrt{2t} \approx 0.997$, option C $= t^{-3} \approx 8.1$, and option D $= \frac{2}{t} \approx 4.0$. So $\log_{10}\pi$ is the smallest.")
ok("M-28-Q18", r"The bisector planes are $\frac{2x - y + 2z - 4}{3} = \pm\frac{x + 2y + 2z - 2}{3}$, i.e. $x - 3y = 2$ or $3x + y + 4z = 6$. The point $(2, -4, 1)$ satisfies $6 - 4 + 4 = 6$, so it lies on the second bisector. None of the other points satisfies either equation.")
fix("M-11-Q9", r"There are 5 girls and 7 boys. A team of 3 boys and 2 girls is to be formed such that two specific boys are not in the same team. The number of ways to do so is", O("M-11-Q9"),
 r"Total teams without restriction: $\binom{7}{3}\binom{5}{2} = 350$. Teams containing both specific boys: $\binom{5}{1}\binom{5}{2} = 50$. Required $= 350 - 50 = 300$.")
ok("M-19-Q6", r"Rotating the axes about the origin does not change the perpendicular distance from the origin to $L$. So $\frac{1}{\sqrt{a^{-2} + b^{-2}}} = \frac{1}{\sqrt{p^{-2} + q^{-2}}}$, i.e. $\frac{1}{a^2} + \frac{1}{b^2} = \frac{1}{p^2} + \frac{1}{q^2}$. Hence the expression is 0.")
ok("M-23-Q22", r"$\frac{2}{x} = \frac{1}{8} + \frac{1}{y} \Rightarrow x = \frac{16y}{y + 8} = 16 - \frac{128}{y + 8}$. For positive integers $x, y$, $y + 8$ must be a divisor of 128 greater than 8: 16, 32, 64, 128. These give $(x, y) = (8, 8), (12, 24), (14, 56), (15, 120)$, so there are 4 pairs.")
ok("M-28-Q22", r"$3(1 - \sin 2\theta)^2 + 6(1 + \sin 2\theta) = 9 + 3\sin^2 2\theta = 9 + 12\sin^2\theta\cos^2\theta$. Also $4\sin^6\theta = 4(1 - \cos^2\theta)^3 = 4 - 12\cos^2\theta + 12\cos^4\theta - 4\cos^6\theta = 4 - 12\sin^2\theta\cos^2\theta - 4\cos^6\theta$. Adding gives $13 - 4\cos^6\theta$.")
ok("M-06-Q17", r"Since $b = \frac{2ac}{a + c}$: $b + a = \frac{a(a + 3c)}{a + c}$ and $b - a = \frac{a(c - a)}{a + c}$, so $\frac{b + a}{b - a} = \frac{a + 3c}{c - a}$. Similarly $\frac{b + c}{b - c} = \frac{3a + c}{a - c}$. The sum is $\frac{(a + 3c) - (3a + c)}{c - a} = 2$.")
fix("M-09-Q9", r"The function $f(x) = (x + 2)^{1/3}$ at $x = -2$", O("M-09-Q9"),
 r"$f'(x) = \frac{1}{3}(x + 2)^{-2/3} > 0$ for $x \neq -2$, so $f$ is increasing; $f'$ is infinite at $-2$, so $f$ is not differentiable there, though a vertical tangent exists. $f''(x) = -\frac{2}{9}(x + 2)^{-5/3}$ is positive for $x < -2$ and negative for $x > -2$, so the concavity changes at $x = -2$.")
ok("M-18-Q11", r"$|z - a^2| + |z - 2a| = 3$ is an ellipse when the distance between the foci is less than 3: $|a^2 - 2a| < 3 \Rightarrow -3 < a^2 - 2a < 3$. The left inequality always holds, and the right gives $-1 < a < 3$. With $a > 0$, $a \in (0, 3)$.")
fix("M-23-Q9", r"The greatest term in the expansion of $(1 + t)^{2n}$ has the greatest coefficient if and only if $t \in \left(\frac{9}{10}, \frac{10}{9}\right)$. The coefficient of $x^5$ in the expansion of $(1 + x - 2x^2)^n$ is", O("M-23-Q9"),
 r"In $(1 + t)^{2n}$ the middle term $T_{n+1}$ is greatest iff $t \in \left(\frac{n}{n+1}, \frac{n+1}{n}\right)$, so $n = 9$. In $(1 + x - 2x^2)^9$, the $x^5$ terms come from $(x\text{-count}, x^2\text{-count}) = (5, 0), (3, 1), (1, 2)$. That gives $\binom{9}{5} + \frac{9!}{5!\,3!\,1!}(-2) + \frac{9!}{6!\,1!\,2!}(4) = 126 - 1008 + 1008 = 126$.")

refs=[x['ref'] for x in src]
missing=[r for r in refs if r not in R]; extra=[r for r in R if r not in refs]
print('missing',missing,'extra',extra)
json.dump(R,open('../eq_batch3.result.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
d=json.load(open('../eq_batch3.result.json',encoding='utf-8'))
from collections import Counter;print(len(d),Counter(v['verdict'] for v in d.values()))
