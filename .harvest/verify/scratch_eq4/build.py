import json
src = json.load(open('D:/PersonalProjects/Revanth/bitsat-mock/.harvest/verify/eq_batch4.json', encoding='utf-8'))
by = {x['ref']: x for x in src}
R = {}

def ok(ref, e):
    R[ref] = {"verdict": "ok", "explanation": e}

def fix(ref, e, stem=None, options=None):
    s = stem if stem is not None else by[ref]['stem']
    o = dict(by[ref]['options'])
    if options:
        o.update(options)
    R[ref] = {"verdict": "fix", "explanation": e, "stem": s, "options": o}

def drop(ref, r):
    R[ref] = {"verdict": "drop", "reason": r}

ok("M-23-Q19", r"Since $x^2-3x+4>0$ for all real $x$, the inequality becomes $x^2-mx-2>-(x^2-3x+4)$, i.e. $2x^2-(m+3)x+2>0$ for all $x$. This needs discriminant $(m+3)^2-16<0$, i.e. $-7<m<1$. The integers $-6,-5,\dots,0$ give 7 values.")

ok("M-28-Q9", r"With vertex $A(1,2)$, the other vertices are reflections of $A$ through the midpoints: $B=2(-1,1)-(1,2)=(-3,0)$ and $C=2(2,3)-(1,2)=(3,4)$. Centroid $=\left(\frac{1-3+3}{3},\frac{2+0+4}{3}\right)=\left(\frac13,2\right)$.")

fix("M-13-Q2", r"By Leibniz rule, $\frac{dy}{dx}=2x\cos^{-1}(x^4)-\cos^{-1}(x^2)$. At $x=2^{-1/4}$: $x^4=\frac12$, $x^2=\frac1{\sqrt2}$, so slope $=2\cdot2^{-1/4}\cdot\frac{\pi}{3}-\frac{\pi}{4}=\left(\frac{\sqrt[4]{8}}{3}-\frac14\right)\pi$, since $2\cdot 2^{-1/4}=2^{3/4}=\sqrt[4]{8}$.",
    stem=r"The slope of the tangent to the curve $y=\int_{x}^{x^{2}}\cos^{-1}(t^{2})\,dt$ at $x=\frac{1}{\sqrt[4]{2}}$ is")

fix("M-17-Q20", r"Write $x=[x]+\{x\}$: $\{x\}+2[x]+2\{x\}=[x]\Rightarrow 3\{x\}=-[x]$. Since $0\le\{x\}<1$, $[x]\in\{0,-1,-2\}$, giving $\{x\}=0,\frac13,\frac23$ and $x=0,-\frac23,-\frac43$. Sum $=-2$.",
    stem=r"The sum of all real solutions of the equation $\{x\}+2x=[x]$ (where $\{\cdot\}$ and $[\cdot]$ denote the fractional part function and the greatest integer function respectively) is equal to")

fix("M-17-Q6", r"$OA=OA$, so $R$ is reflexive; $OA=OB\Rightarrow OB=OA$, so symmetric; $OA=OB$ and $OB=OC\Rightarrow OA=OC$, so transitive. Hence $R$ is an equivalence relation (points are related iff they lie on the same circle centred at $O$).",
    stem=r"A relation $R$ on the set of points of a given plane is defined by $(A,B)\in R$ if $OA=OB$, where $O$ is a fixed point in the same plane. Then the relation $R$ is")

ok("M-19-Q5", r"Numerator: $\sqrt{x^2+1}-\sqrt[3]{x^3+1}\approx\left(x+\frac{1}{2x}\right)-\left(x+\frac{1}{3x^2}\right)\to0$. Denominator: $\sqrt[4]{x^4+1}-\sqrt[5]{x^4+1}\approx x-x^{4/5}\to\infty$. Hence the limit is $0$.")

fix("M-09-Q1", r"We need $6-[x^2-2]>0$, i.e. $[x^2-2]\le5$, i.e. $x^2-2<6\Rightarrow x^2<8$. The positive integers satisfying this are $x=1,2$, so there are 2 values.",
    stem=r"Let $f(x)=\frac{1}{\sqrt{6-[x^{2}-2]}}$, where $[\cdot]$ is the greatest integer function. Then the number of positive integral values in the domain of $f(x)$ is")

fix("M-11-Q20", r"The lines meet at $\left(\frac65,\frac65\right)$. Let $A=(a,0)$, $B=(0,b)$; $P$ divides $AB$ with $AP:PB=1:3$, so $P=(h,k)=\left(\frac{3a}{4},\frac{b}{4}\right)$, i.e. $a=\frac{4h}{3}$, $b=4k$. Since $\frac{x}{a}+\frac{y}{b}=1$ passes through $\left(\frac65,\frac65\right)$: $\frac65\left(\frac{3}{4h}+\frac{1}{4k}\right)=1\Rightarrow 6(3k+h)=20hk$, i.e. $3x+9y-10xy=0$.",
    stem=r"A variable line, drawn through the point of intersection of the straight lines $3x+2y-6=0$ and $2x+3y-6=0$, meets the x-axis and y-axis at $A$ and $B$ respectively. The locus of the point $P$ on $AB$ such that $PB:PA=3:1$ is",
    options={"A": r"$3x+9y+10xy=0$", "B": r"$3x+9y-10xy=0$", "C": r"$3x-9y-10xy=0$", "D": r"$9x-9y-10xy=0$"})

ok("M-28-Q15", r"With $r^2+h^2=9$, $V=\frac13\pi h(9-h^2)$. $\frac{dV}{dh}=\frac13\pi(9-3h^2)=0\Rightarrow h=\sqrt3$, $r^2=6$. $V_{\max}=\frac13\pi\cdot6\cdot\sqrt3=2\sqrt3\pi$.")

ok("M-01-Q3", r"For $p\to q$ with $p$: triangles are equiangular, $q$: triangles are similar, the contrapositive is $\sim q\to\sim p$: if two triangles are not similar then they are not equiangular. Option D is the inverse, not the contrapositive.")

fix("M-27-Q20", r"$3a+4b+c=0$ means every such line passes through the fixed point $(3,4)$. The distance from $(1,-2)$ is maximum when the line is perpendicular to the segment joining $(3,4)$ and $(1,-2)$, whose slope is $3$. So the slope is $-\frac13$: $y-4=-\frac13(x-3)\Rightarrow x+3y-15=0$.",
    stem=r"The equation of the straight line $ax+by+c=0$, where $3a+4b+c=0$, which is at maximum distance from $(1,-2)$, is")

ok("M-25-Q7", r"Take a point $(h,3-h)$ on $x+y=3$. Its chord of contact is $hx+(3-h)y=9$, i.e. $h(x-y)+3(y-3)=0$. This passes through the intersection of $x=y$ and $y=3$, i.e. $(3,3)$, for every $h$.")

fix("M-23-Q18", r"A point $P$ lies on some circle of radius 3 whose centre is on $x^2+y^2=25$ (distance 5 from $O$). So the distance $OP$ ranges from $5-3=2$ to $5+3=8$. Hence $4\le x^2+y^2\le64$.",
    stem=r"The centres of a set of circles, each of radius 3, lie on the circle $x^2+y^2=25$. The locus of any point on these circles is",
    options={"A": r"$3\le x^2+y^2\le9$", "B": r"$x^2+y^2\ge25$", "C": r"$x^2+y^2\le25$", "D": r"$4\le x^2+y^2\le64$"})

fix("M-19-Q13", r"The product of $n$ G.M.'s inserted between $a$ and $b$ is $(ab)^{n/2}$. So $(2\times162)^{n/2}=324^{n/2}=18^n=5832=18^3$, giving $n=3$.",
    stem=r"$n$ G.M.'s are inserted between the two numbers 2 and 162. If the product of the $n$ G.M.'s is 5832, then $n$ is")

ok("M-20-Q4", r"Since $\alpha,\beta$ satisfy $t^2=6t+2$, we get $\alpha^{n}=6\alpha^{n-1}+2\alpha^{n-2}$ and similarly for $\beta$. Subtracting, $a_n=6a_{n-1}+2a_{n-2}$. With $n=10$: $a_{10}-2a_8=6a_9$, so $\frac{a_{10}-2a_8}{2a_9}=3$.")

fix("M-26-Q19", r"Perpendicular tangents meet on the director circle of $\frac{x^2}{5}+\frac{y^2}{4}=1$, i.e. $x^2+y^2=9$. Put $m=3\cos\theta$, $n=3\sin\theta$: $E=12\cos\theta+9\sin\theta$, which ranges over $[-\sqrt{144+81},\sqrt{144+81}]=[-15,15]$.",
    stem=r"Let $(m,n)$ be a point from which two perpendicular tangents can be drawn to the ellipse $4x^2+5y^2=20$. If $E=4m+3n$, then")

ok("P-22-Q13", r"$a=F/m=4t$, so $v=2t^2$ (starting from rest). At $t=2$ s, $v=8$ m/s. By the work-energy theorem $W=\frac12(1)(8)^2=32$ J $=8n$, so $n=4$.")

fix("P-19-Q5", r"Limit of resolution $\theta=1.22\frac{\lambda}{D}$. Minimum separation on the moon $=d\theta=\frac{1.22\times5893\times10^{-10}\times4\times10^{8}}{5}\approx57.5$ m $\approx58$ m.",
    stem=r"The aperture diameter of a telescope is 5 m. The separation between the moon and the earth is $4\times10^{5}$ km. With light of wavelength 5893 Å, the minimum separation between objects on the surface of the moon, so that they are just resolved, is close to")

fix("P-12-Q15", r"At null point the cell's emf (no current drawn, so internal resistance is irrelevant) balances 1000 cm: potential gradient $=\frac{5}{1000}$ V/cm. Potential across the whole 1200 cm wire $=6$ V, so $R=\frac{6}{60\times10^{-3}}=100\,\Omega$.",
    stem=r"The length of a potentiometer wire is 1200 cm and it carries a current of 60 mA. For a cell of emf 5 V and internal resistance of $20\,\Omega$, the null point on it is found to be at 1000 cm. The resistance of the whole wire is")

fix("P-22-Q16", r"The train is a semicircular arc of radius $R$; its centre of mass is at $\frac{2R}{\pi}$ from the centre and moves with angular speed $\omega=\frac{V}{R}$. So $v_{cm}=\frac{2R}{\pi}\cdot\frac{V}{R}=\frac{2V}{\pi}$ and momentum $=Mv_{cm}=\frac{2MV}{\pi}$. It is not $MV$ because the velocities of different parts point in different directions.",
    stem=r"A train of mass $M$ is moving on a circular track of radius $R$ with constant speed $V$. The length of the train is half of the perimeter of the track. The linear momentum of the train will be")

ok("P-08-Q18", r"First law: $\Delta Q=\Delta U+W\Rightarrow110=40+W\Rightarrow W=70$ J.")

fix("P-13-Q11", r"$\frac{B^2}{2\mu_0}$ is the magnetic energy density, i.e. energy per unit volume: $\frac{ML^2T^{-2}}{L^3}=ML^{-1}T^{-2}$.",
    options={"A": r"$MLT^{-2}$", "B": r"$ML^{-1}T^{-2}$", "C": r"$ML^{2}T^{-1}$", "D": r"$ML^{2}T^{-2}$"})

fix("P-19-Q9", r"For a sphere, $E=\frac{kQ}{R^2}$ and $V=\frac{kQ}{R}=ER$. So $\frac{V_1}{V_2}=\frac{E_1R_1}{E_2R_2}=\frac{R_1}{R_2}\cdot\frac{R_1}{R_2}=\left(\frac{R_1}{R_2}\right)^2$.",
    stem=r"Consider two charged metallic spheres $S_1$ and $S_2$ of radii $R_1$ and $R_2$, respectively. The electric fields $E_1$ (on $S_1$) and $E_2$ (on $S_2$) on their surfaces are such that $E_1/E_2=R_1/R_2$. Then the ratio $V_1(\text{on }S_1)/V_2(\text{on }S_2)$ of the electrostatic potentials on each sphere is",
    options={"A": r"$\left(\frac{R_1}{R_2}\right)^3$", "B": r"$\frac{R_1}{R_2}$", "C": r"$\frac{R_2}{R_1}$", "D": r"$\left(\frac{R_1}{R_2}\right)^2$"})

fix("P-19-Q12", r"Inside, $B=\frac{\mu_0Ir}{2\pi a^2}$, so at $r=\frac a3$: $B_1=\frac{\mu_0I}{6\pi a}$. Outside, $B=\frac{\mu_0I}{2\pi r}$, so at $2a$: $B_2=\frac{\mu_0I}{4\pi a}$. Ratio $\frac{B_1}{B_2}=\frac46=\frac23$.",
    stem=r"A long, straight wire of radius $a$ carries a current distributed uniformly over its cross-section. The ratio of the magnetic fields due to the wire at distances $\frac{a}{3}$ and $2a$, respectively, from the axis of the wire is")

fix("P-14-Q15", r"By Malus's law, $\cos^2\theta=0.1\Rightarrow\cos\theta\approx0.316\Rightarrow\theta\approx71.6^\circ$ between polarizer and analyzer axes. Zero intensity requires $\theta=90^\circ$, so the analyzer must be rotated further by $90^\circ-71.6^\circ=18.4^\circ$. Option C (71.6°) is the current angle, not the extra rotation.",
    stem=r"A polarizer-analyzer set is adjusted such that the intensity of light coming out of the analyzer is just 10% of the intensity of light incident on it from the polarizer. Assuming that the polarizer-analyzer set does not absorb any light, the angle by which the analyzer needs to be rotated further to reduce the output intensity to zero is",
    options={"A": r"$45^\circ$", "B": r"$90^\circ$", "C": r"$71.6^\circ$", "D": r"$18.4^\circ$"})

fix("P-20-Q10", r"Lens maker's formula with $R_1=\infty$, $R_2=-30$ cm (the focal length does not depend on which face faces the object): $\frac1f=(1.5-1)\left(0+\frac1{30}\right)=\frac{1}{60}$, so $f=60$ cm.",
    stem=r"A point object in air is in front of the curved surface of a plano-convex lens. The radius of curvature of the curved surface is 30 cm and the refractive index of the lens material is 1.5. The focal length of the lens (in cm) is")

fix("P-08-Q15", r"Water vs sand: $100\times1\times10=100\times s_s\times20\Rightarrow s_s=0.5$ cal g$^{-1}$°C$^{-1}$. Liquid vs sand: $100\times s_l\times20=100\times0.5\times10\Rightarrow s_l=0.25$ cal g$^{-1}$°C$^{-1}$ $=0.25\times4.2=1.05$ kJ kg$^{-1}$K$^{-1}$.",
    stem=r"The temperature of 100 g of water in a thermoflask remains fixed for a pretty long time at 50°C. An equal mass of sand at 20°C is poured into the flask and shaken for some time so that the temperature of the mixture is 40°C. Now the experiment is repeated with 100 g of a liquid at 50°C and an equal amount of sand at 20°C, when the temperature of the mixture is found to be 30°C. The specific heat of the liquid (in $\mathrm{kJ\,kg^{-1}\,K^{-1}}$) is")

fix("P-08-Q8", r"Isothermal bulk modulus $B=-V\left(\frac{dP}{dV}\right)_T=P$. With $n=1$ mol ($32$ g of $\mathrm{O_2}$), $T=400$ K, $V=1\,\mathrm{m^3}$: $P=\frac{nRT}{V}=400R$.",
    stem=r"32 g of $\mathrm{O_2}$ is contained in a cubical container of side 1 m and maintained at a temperature of 127°C. The isothermal bulk modulus of elasticity of the gas in terms of the universal gas constant $R$ is")

ok("P-06-Q15", r"Work required $W(d)=-\int_0^d kx(x-\lambda)\,dx=k\left(\frac{\lambda d^2}{2}-\frac{d^3}{3}\right)$. $\frac{dW}{dd}=kd(\lambda-d)\ge0$ for $0\le d\le\lambda$, so $W$ increases throughout and is maximum at $d=\lambda$. Note $d=\lambda/2$ is where the force magnitude peaks, not the work.")

fix("P-17-Q12", r"Restoring torque $\tau=-(I\pi a^2)B\theta$; moment of inertia about a diameter $=\frac{ma^2}{2}$. So $\omega^2=\frac{2\pi a^2IB}{ma^2}=\frac{2\pi IB}{m}$ and $T=\frac{2\pi}{\omega}=2\pi\sqrt{\frac{m}{2\pi IB}}=\sqrt{\frac{2\pi m}{IB}}$.",
    stem=r"A small circular loop of conducting wire has radius $a$ and carries current $I$. It is placed in a uniform magnetic field $B$ perpendicular to its plane such that when rotated slightly about its diameter and released, it starts performing simple harmonic motion of time period $T$. If the mass of the loop is $m$, then")

fix("P-18-Q20", r"$I_z=\frac12MR^2$. About a diameter $I=\frac14MR^2$; the line $y=x+c$ is parallel to a diameter at distance $\frac{|c|}{\sqrt2}$. Parallel axes: $\frac14MR^2+M\frac{c^2}{2}=\frac12MR^2\Rightarrow c^2=\frac{R^2}{2}\Rightarrow c=\pm\frac{R}{\sqrt2}$.",
    stem=r"A uniform disc of radius $R$ lies in the x-y plane, with its centre at the origin. Its moment of inertia about the z-axis is equal to its moment of inertia about the line $y=x+c$. The value of $c$ will be")

fix("P-05-Q14", r"Let $L=c^ag^bp^x$: $[L]=[LT^{-1}]^a[LT^{-2}]^b[ML^{-1}T^{-2}]^x$. Mass: $x=0$; length: $a+b=1$; time: $-a-2b=0$. So $a=2$, $b=-1$, and $[L]=c^2/g$.",
    stem=r"If the velocity of light $c$, the acceleration due to gravity $g$ and the atmospheric pressure $p$ are taken as the fundamental quantities, then the dimensions of length will be")

fix("P-05-Q5", r"Along the incline, flight time $T=\frac{2u\sin(\alpha-\beta)}{g\cos\beta}$. Striking at right angles means the velocity component along the incline is zero then: $u\cos(\alpha-\beta)=g\sin\beta\,T$. Combining: $2\tan(\alpha-\beta)=\cot\beta$. Then $\tan\alpha=\frac{\frac12\cot\beta+\tan\beta}{1-\frac12}=\cot\beta+2\tan\beta$.",
    options={"A": r"$\cot\beta-2\tan\beta$", "B": r"$\tan\beta+2\cot\beta$", "C": r"$\cot\beta+2\tan\beta$", "D": r"$\tan\beta-2\cot\beta$"})

ok("P-06-Q17", r"$\frac{dU}{dx}=2x-4=0$ at $x=2$, so the force is zero there. $\frac{d^2U}{dx^2}=2>0$, so $U$ is a minimum and $x=2$ is a point of stable equilibrium.")

ok("P-19-Q16", r"Total resistance needed $=\frac{V}{I_g}=\frac{10}{10^{-3}}=10\,\mathrm{k\Omega}$. Series resistance $=10000-100=9900\,\Omega=9.9\,\mathrm{k\Omega}$. Option B ignores the coil resistance.")

fix("P-05-Q8", r"To reach the exactly opposite point, the swimmer's component along the flow must cancel the current. Heading at $60^\circ$ to the perpendicular (upstream), this component is $2\sin60^\circ=\sqrt3$ km/h, so the current speed is $\sqrt3$ km/h.",
    stem=r"A man who can swim at the rate of $2$ km/h (in still water) crosses a river to a point exactly opposite on the other bank by swimming at an angle of 60° to the direction perpendicular to the river flow. The velocity of the water current in km/h is")

ok("P-17-Q10", r"Light escapes only within the critical cone: $\sin C=\frac34$, $\cos C=\frac{\sqrt7}{4}$. Fraction $=\frac{2\pi r^2(1-\cos C)}{4\pi r^2}=\frac{1-\cos C}{2}=\frac{4-\sqrt7}{8}\approx0.17$, i.e. about 17%.")

ok("P-05-Q1", r"$v=3t^2-12t+3$, $a=6t-12=0\Rightarrow t=2$ s. Then $v=12-24+3=-9$ m/s.")

fix("P-16-Q9", r"$v=\frac{dx}{dt}=\frac{t}{2}$, so $v=0$ at $t=0$ and $v=1$ m/s at $t=2$ s. Work done $=\Delta K=\frac12\times6\times1^2=3$ J.",
    stem=r"A body of mass 6 kg is acted upon by a force which causes a displacement in it given by $x=\frac{t^{2}}{4}$ metre, where $t$ is the time in seconds. The work done by the force in 2 seconds is")

fix("P-12-Q12", r"$C_1+C_2=10\,\mu F$ and, at the same voltage, $U\propto C$, so $C_2=4C_1$. Thus $C_1=2\,\mu F$, $C_2=8\,\mu F$. In series: $C=\frac{2\times8}{10}=1.6\,\mu F$.",
    stem=r"The effective capacitance of a parallel combination of two capacitors $C_1$ and $C_2$ is $10\,\mu F$. When these capacitors are individually connected to a voltage source of 1 V, the energy stored in the capacitor $C_2$ is 4 times that of $C_1$. If these capacitors are connected in series, their effective capacitance will be")

ok("P-16-Q13", r"Initial COM height $=\frac{2\times30+4\times0}{6}=10$ m; initial COM velocity $=\frac{2\times0+4\times15}{6}=10$ m/s upward; COM acceleration $=g$ downward. Extra rise $=\frac{10^2}{2\times10}=5$ m (reached at $t=1$ s, before either body hits the ground or collides), so maximum height $=15$ m.")

fix("P-19-Q18", r"Phase difference $\Delta\phi=\frac{2\pi}{\lambda}\cdot\frac{\lambda}{8}=\frac{\pi}{4}$. $\frac{I}{I_0}=\cos^2\frac{\Delta\phi}{2}=\cos^2\frac{\pi}{8}\approx0.853$.",
    stem=r"In a double-slit experiment, at a certain point on the screen the path difference between the two interfering waves is $\frac{1}{8}$th of a wavelength. The ratio of the intensity of light at that point to that at the centre of a bright fringe is")

fix("P-13-Q15", r"Demagnetization requires $H=nI$ equal to the coercivity, with $n=\frac{100}{0.1}=1000$ turns/m. So $I=\frac{3\times10^3}{1000}=3$ A.",
    stem=r"The coercivity of a small magnet where the ferromagnet gets demagnetized is $3\times10^{3}\ \mathrm{A\,m^{-1}}$. The current required to be passed in a solenoid of length 10 cm and number of turns 100, so that the magnet gets demagnetized when inside the solenoid, is")

fix("P-01-Q14", r"$L=I\omega=\frac25MR^2\omega$ with $M=6\times10^{24}$ kg, $R=6.4\times10^6$ m, $\omega=\frac{2\pi}{86400}\approx7.3\times10^{-5}$ rad/s. $L\approx0.4\times6\times10^{24}\times4.1\times10^{13}\times7.3\times10^{-5}\approx7\times10^{33}$, of the order of $10^{34}$ kg m$^2$s$^{-1}$.",
    options={"A": r"$10^{38}$", "B": r"$10^{34}$", "C": r"$10^{30}$", "D": r"$10^{22}$"})

fix("P-23-Q3", r"Energy conservation: $\frac12v^2-\frac{GM}{R}=\frac12u^2-\frac{GM}{10R}\Rightarrow v^2=u^2+\frac{9}{10}\cdot\frac{2GM}{R}=u^2+0.9v_e^2$. So $v^2=144+0.9\times(11.2)^2\approx256.9$, giving $v\approx16$ km/s.",
    stem=r"An asteroid is moving directly towards the centre of the earth. When at a distance of $10R$ ($R$ is the radius of the earth) from the earth's centre, it has a speed of 12 km/s. Neglecting the effect of the earth's atmosphere, what will be the speed of the asteroid (in km/s) when it hits the surface of the earth? (Escape velocity from the earth is 11.2 km/s.)")

fix("P-08-Q10", r"For an ideal gas $U\propto T$ (since $U=0$ at $T=0$). In a reversible adiabatic process $TV^{\gamma-1}=$ constant, so $UV^{\gamma-1}=$ constant. Raising to the power $\frac{1}{\gamma-1}$: $VU^{\frac{1}{\gamma-1}}=$ constant.",
    stem=r"An ideal gas, whose internal energy $U$ is zero at absolute zero temperature, undergoes a reversible adiabatic compression. If $U$, $P$, $V$, $T$ represent the internal energy, pressure, volume and absolute temperature of the gas respectively, and $\gamma=\frac{C_P}{C_V}$, then",
    options={"A": r"$UV^{\gamma}=$ constant", "B": r"$UP^{\gamma}=$ constant", "C": r"$TU^{\gamma-1}=$ constant", "D": r"$VU^{\frac{1}{\gamma-1}}=$ constant"})

ok("P-01-Q12", r"Case 1: $\vec F=q\vec v\times\vec B$ with $\vec v$ north and $\vec F$ up requires $\vec B$ pointing west above the wire, so the current flows south. Case 2: east of a southward current, $\vec B$ points vertically up. With $\vec v$ westward (towards the wire), $\vec F=q(-\hat i)\times\hat k=q\hat j$, i.e. north.")

ok("P-05-Q11", r"Displacement $=\int_0^2(4t-3t^2)\,dt=[2t^2-t^3]_0^2=8-8=0$. Average velocity $=\frac{0}{2}=0$. (Average speed would be nonzero since the particle reverses at $t=\frac43$ s.)")

fix("P-08-Q1", r"With $T\propto PV$: $TV^{3/2}=$ const $\Rightarrow PV^{5/2}=$ const, a polytropic process with $x=\frac52$. $C=C_V+\frac{R}{1-x}=\frac32R-\frac23R=\frac{5R}{6}$.",
    stem=r"A monoatomic ideal gas follows the process $TV^{3/2}=$ constant. The molar specific heat for this process is ($R$ = gas constant)")

ok("P-02-Q42", r"Initially the second fork is $256\pm6$ Hz. Waxing lowers fork 1's frequency and the beats fall to 4, so fork 2 must be 250 Hz (not 262) and waxed fork 1 is 254 or 246 Hz. Removing some wax raises its frequency to give 0 beats, i.e. 250 Hz, which is possible only from 246 Hz (from 254 Hz it would move away from 250).")

ok("P-06-Q4", r"$d\vec s=4t\,dt\,\hat i$ (the $\hat j$ part is constant). $W=\int_0^2(3t)(4t)\,dt=\int_0^2 12t^2\,dt=4t^3\big|_0^2=32$ J.")

ok("P-06-Q19", r"The whole rope accelerates at $a=\frac{F}{m}$. The 4 m beyond the point (mass $\frac45m$) is pulled only by the tension: $T=\frac45m\cdot\frac{F}{m}=\frac45\times5=4$ N.")

ok("P-06-Q10", r"$s=\frac12at^2$, so with the same distance and twice the time, $a_{\text{friction}}=\frac{a_0}{4}$: $g(\sin\theta-\mu\cos\theta)=\frac{g\sin\theta}{4}\Rightarrow\mu=\frac34\tan\theta=0.75$ at $45^\circ$.")

fix("P-13-Q8", r"Magnetic field lines form closed loops (zero net flux through any closed surface). Every field line passing through the coil area returns through the rest of the infinite plane in the opposite direction, so $\phi_i=-\phi_0$.",
    stem=r"Consider a circular coil of wire carrying constant current $I$, forming a magnetic dipole. The magnetic flux through an infinite plane that contains the circular coil, excluding the circular coil area, is $\phi_i$. The magnetic flux through the area of the circular coil is $\phi_0$. Which of the following options is correct?",
    options={"A": r"$\phi_i>\phi_0$", "B": r"$\phi_i<\phi_0$", "C": r"$\phi_i=-\phi_0$", "D": r"$\phi_i=\phi_0$"})

fix("P-05-Q12", r"Relative position of B w.r.t. A: $(d-vt,\,-2vt)$, so $R^2=(d-vt)^2+4v^2t^2$. $\frac{d(R^2)}{dt}=-2v(d-vt)+8v^2t=0\Rightarrow T_0=\frac{d}{5v}$. Then $R_{\min}^2=\frac{16d^2}{25}+\frac{4d^2}{25}\Rightarrow R_{\min}=\frac{2d}{\sqrt5}$, so B is wrong; $R(t)$ is neither a line nor a circle.",
    stem=r"Initially two particles A and B are at $(0,0)$ and $(d,0)$ respectively. They start moving with velocities $\vec v_A=v\hat i+v\hat j$ and $\vec v_B=-v\hat j$. If $R$ is the separation between them and $T_0$ is the time when the separation between them is minimum, then")

drop("P-12-Q4", "Refers to a figure/circuit (switch S1, plates) not provided; stem incomplete.")

fix("P-05-Q16", r"$\frac{\Delta A}{A}=2\frac{\Delta a}{a}+3\frac{\Delta b}{b}+\frac{\Delta c}{c}+\frac12\frac{\Delta d}{d}=2(1)+3(3)+2+\frac12(2)=14\%$.",
    stem=r"A physical quantity $A$ is related to four observations $a$, $b$, $c$ and $d$ as follows: $A=\frac{a^{2}b^{3}}{c\sqrt{d}}$. The percentage errors of measurement in $a$, $b$, $c$ and $d$ are 1%, 3%, 2% and 2% respectively. What is the percentage error in the quantity $A$?",
    options={"A": "12%", "B": "7%", "C": "5%", "D": "14%"})

fix("P-05-Q10", r"$\frac{dv}{dt}=-av^2\Rightarrow\frac1v=\frac1u+at\Rightarrow v=\frac{u}{1+aut}$. Then $s=\int_0^t\frac{u\,dt}{1+aut}=\frac1a\ln(1+aut)$.",
    stem=r"A point moves in a straight line under the retardation $av^2$, where $a$ is a positive constant and $v$ is the speed. If the initial speed is $u$, the distance covered in $t$ seconds is",
    options={"A": r"$aut$", "B": r"$\frac{1}{a}\ln(aut)$", "C": r"$\frac{1}{a}\ln(1+aut)$", "D": r"$a\ln(aut)$"})

fix("P-18-Q1", r"Dragging up the plane needs $F_1=W\sin\theta+\mu W\cos\theta$; lifting needs $W$. $F_1<W\Rightarrow\mu<\frac{1-\sin\theta}{\cos\theta}=\frac{\cos\frac\theta2-\sin\frac\theta2}{\cos\frac\theta2+\sin\frac\theta2}=\tan\left(\frac\pi4-\frac\theta2\right)$.",
    stem=r"A weight $W$ is to be moved from the bottom to the top of an inclined plane of inclination $\theta$ to the horizontal. If a smaller force is to be applied to drag it along the plane in comparison to lifting it vertically up, the coefficient of friction should be such that")

ok("P-18-Q2", r"Only the tangential force does work, so power $=\frac{dK}{dt}=6t$. At $t=1$ s, $P=6$ W. (Equivalently $v=\sqrt3t$, $a_t=\sqrt3$, $P=ma_tv=6$ W.)")

ok("P-06-Q16", r"$v=\frac{dx}{dt}=t^2$, so $v(0)=0$ and $v(2)=4$ m/s. By the work-energy theorem, $W=\frac12\times2\times4^2=16$ J.")

ok("P-08-Q2", r"$v_{rms}=\sqrt2\,v_s\Rightarrow\frac{3RT}{M}=2\frac{\gamma RT}{M}\Rightarrow\gamma_{mix}=\frac32$. $\gamma_{mix}=\frac{2\cdot\frac72R+n\cdot\frac52R}{2\cdot\frac52R+n\cdot\frac32R}=\frac{14+5n}{10+3n}=\frac32\Rightarrow28+10n=30+9n\Rightarrow n=2$.")

fix("P-17-Q7", r"The same screen width holds $15\beta_1=10\beta_2$ with $\beta\propto\lambda$: $15\times500=10\lambda\Rightarrow\lambda=750$ nm.",
    stem=r"In a Young's double slit experiment, 15 fringes are observed on a small portion of the screen when light of wavelength 500 nm is used. Ten fringes are observed on the same section of the screen when another light source of wavelength $\lambda$ is used. Then the value of $\lambda$ is")

fix("P-07-Q9", r"The stick rotates about the fixed bottom end. Energy: $mg\frac{l}{2}=\frac12\cdot\frac{ml^2}{3}\omega^2\Rightarrow\omega=\sqrt{\frac{3g}{l}}$. Speed of the top end $=\omega l=\sqrt{3gl}=\sqrt{3g}$ for $l=1$ m (SI units).",
    stem=r"A uniform metre stick is held vertically with one end on the floor and is allowed to fall. Assuming that the end on the floor does not slip, the speed of the other end when it hits the floor is (in SI units)")

ok("P-22-Q19", r"Velocity $v=7-2t$ becomes zero at $t=3.5$ s, so the particle turns back during the 4th second. From $t=3$ to $3.5$ s it moves $\frac12(2)(0.5)^2=0.25$ m, and from $3.5$ to $4$ s it returns $0.25$ m. Distance $=0.5$ m $=\frac{x}{10}$, so $x=5$. (The displacement in that second is zero.)")

ok("P-24-Q9", r"The weight is unchanged and the cylinder does not expand, so $\rho_0\cdot A\cdot80=\rho_4\cdot A\cdot79$ (submerged lengths in cm). $\frac{\rho_4}{\rho_0}=\frac{80}{79}\approx1.01$.")

ok("P-24-Q10", r"Continuity: $vA=$ constant, so $v\propto\frac1{d^2}$. Minimum velocity is at maximum diameter: $\frac{v_{\min}}{v_{\max}}=\left(\frac{4.8}{6.4}\right)^2=\left(\frac34\right)^2=\frac{9}{16}$.")

missing = [r for r in by if r not in R]
extra = [r for r in R if r not in by]
print('missing', missing, 'extra', extra)
out = 'D:/PersonalProjects/Revanth/bitsat-mock/.harvest/verify/eq_batch4.result.json'
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
d = json.load(open(out, encoding='utf-8'))
from collections import Counter
print(len(d), Counter(v['verdict'] for v in d.values()))
