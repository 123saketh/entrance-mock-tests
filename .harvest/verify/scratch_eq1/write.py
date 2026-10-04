import json
R={}
def ok(ref,e): R[ref]={"verdict":"ok","explanation":e}
def fix(ref,s,o,e): R[ref]={"verdict":"fix","stem":s,"options":dict(zip("ABCD",o)),"explanation":e}
def drop(ref,r): R[ref]={"verdict":"drop","reason":r}

fix("CH-20-Q11",r"Identify the product D in the following reaction sequence: $\mathrm{CH_3COOH}\xrightarrow{\mathrm{LiAlH_4}}A\xrightarrow{\mathrm{H^+},\ 443\,K}B\xrightarrow{\mathrm{Br_2}}C\xrightarrow{\text{alc. KOH}}D$",
 ["Methane","Alcohol","Acetylene","Benzaldehyde"],
 r"$\mathrm{LiAlH_4}$ reduces acetic acid to ethanol (A). Acid dehydration at 443 K gives ethene (B), which adds $\mathrm{Br_2}$ to give 1,2-dibromoethane (C). Double dehydrohalogenation with alcoholic KOH gives ethyne, $\mathrm{HC\equiv CH}$ (acetylene). 'Alcohol' is only the first intermediate A.")
ok("CH-28-Q6",r"ZnO dissolves in acids ($\mathrm{ZnO + H_2SO_4 \rightarrow ZnSO_4 + H_2O}$) and in alkalis ($\mathrm{ZnO + 2NaOH \rightarrow Na_2ZnO_2 + H_2O}$), so it is amphoteric. $\mathrm{Na_2O}$ is basic, while $\mathrm{SO_2}$ and $\mathrm{B_2O_3}$ are acidic.")
fix("CH-11-Q5",r"The oxidation number of S in $\mathrm{H_2S_2O_8}$ is",["+2","+4","+6","+7"],
 r"$\mathrm{H_2S_2O_8}$ (peroxodisulphuric acid) has one peroxide link $\mathrm{-O-O-}$ (O at $-1$) and six O atoms at $-2$. So $2(+1)+2x+6(-2)+2(-1)=0$, which gives $x=+6$. Taking every O as $-2$ gives the wrong value $+7$.")
ok("CH-12-Q17",r"Chlorobenzene condenses with chloral ($\mathrm{CCl_3CHO}$) in the presence of conc. $\mathrm{H_2SO_4}$: two chlorobenzene rings attach to the aldehyde carbon, giving p,p'-dichlorodiphenyltrichloroethane (DDT). Gammexene is benzene hexachloride, made by chlorinating benzene.")
fix("CH-15-Q16",r"For the coagulation of 200 mL of $\mathrm{As_2S_3}$ sol, 10 mL of 1 M NaCl is required. What is the coagulating value of NaCl (millimoles of electrolyte needed to coagulate 1 L of sol)?",
 ["200","100","50","25"],
 r"10 mL of 1 M NaCl contains 10 mmol NaCl, and this coagulates 200 mL of sol. For 1000 mL the requirement is $10\times\frac{1000}{200}=50$ mmol, so the coagulating value is 50.")
ok("CH-08-Q10",r"The enzyme diastase (amylase) hydrolyses starch to maltose. Maltase then converts maltose to glucose, invertase hydrolyses sucrose, and zymase ferments glucose to ethanol.")
fix("CH-27-Q7",r"The reaction $\mathrm{3ClO^-(aq) \rightarrow ClO_3^-(aq) + 2Cl^-(aq)}$ is an example of",
 ["Oxidation reaction","Reduction reaction","Disproportionation reaction","Decomposition reaction"],
 r"Cl is $+1$ in $\mathrm{ClO^-}$. It goes up to $+5$ in $\mathrm{ClO_3^-}$ and down to $-1$ in $\mathrm{Cl^-}$. Because the same species is both oxidised and reduced, this is a disproportionation reaction.")
fix("CH-24-Q16",r"The pH of a solution obtained by mixing equal volumes of 0.1 M triethylamine ($K_b = 6.4\times10^{-5}$) and $\frac{4}{45}$ M $\mathrm{NH_4OH}$ ($K_b = 1.8\times10^{-5}$) will be",
 ["11.3","10.3","12.3","11.45"],
 r"Mixing equal volumes halves each concentration, to 0.05 M and $\frac{2}{45}$ M. For two weak bases, $[\mathrm{OH^-}]=\sqrt{0.05(6.4\times10^{-5})+\frac{2}{45}(1.8\times10^{-5})}=\sqrt{4\times10^{-6}}=2\times10^{-3}$ M. So pOH = 2.7 and pH = 11.3. Ignoring the dilution gives the trap value 11.45.")
ok("CH-07-Q13",r"Chemotherapy uses chemicals (drugs) to destroy cancer cells or stop them from multiplying, which arrests further growth of the tumour. Physiotherapy, electrotherapy and psychotherapy do not act on cancerous cells.")
fix("CH-06-Q1",r"A particle X moving with a certain velocity has a de Broglie wavelength of 1 Å. If particle Y has a mass 25% that of X and a velocity 75% that of X, the de Broglie wavelength of Y will be",
 ["0.19 Å","5.33 Å","6.88 Å","4.8 Å"],
 r"Since $\lambda = \frac{h}{mv}$, $\frac{\lambda_X}{\lambda_Y}=\frac{m_Y v_Y}{m_X v_X}=0.25\times0.75=\frac{3}{16}$. So $\lambda_Y=\frac{16}{3}\lambda_X=5.33$ Å.")
fix("CH-12-Q11",r"The final step in the extraction of copper from copper pyrites in the Bessemer converter involves the reaction",
 [r"$\mathrm{4Cu_2O + FeS \rightarrow 8Cu + FeSO_4}$",r"$\mathrm{Cu_2S + 2Cu_2O \rightarrow 6Cu + SO_2}$",r"$\mathrm{2Cu_2O + FeS \rightarrow 4Cu + Fe + SO_2}$",r"$\mathrm{Cu_2S + 2FeO \rightarrow 2Cu + 2Fe + SO_2}$"],
 r"In the Bessemer converter, part of the $\mathrm{Cu_2S}$ is oxidised to $\mathrm{Cu_2O}$. This oxide then reacts with the remaining $\mathrm{Cu_2S}$ (self-reduction): $\mathrm{Cu_2S + 2Cu_2O \rightarrow 6Cu + SO_2}$, which gives blister copper. Iron is removed earlier as $\mathrm{FeSiO_3}$ slag, so it plays no part in this step.")
fix("CH-22-Q10",r"Which one of the following substances, used in dry cleaning, is a better strategy to control environmental pollution?",
 ["Tetrachloroethylene","Carbon dioxide","Sulphur dioxide","Nitrogen dioxide"],
 r"Liquefied $\mathrm{CO_2}$ (with a suitable detergent) is the green-chemistry replacement for chlorinated solvents in dry cleaning. Tetrachloroethylene ($\mathrm{Cl_2C=CCl_2}$) is a suspected carcinogen that contaminates groundwater, while $\mathrm{SO_2}$ and $\mathrm{NO_2}$ are air pollutants.")
drop("CH-09-Q14","Bromine compounds such as CH2Br2 and halons also deplete ozone, so 'all are correct' is arguably right; 'CBrCs' is unclear.")
fix("CH-12-Q12",r"Heating a mixture of $\mathrm{Cu_2O}$ and $\mathrm{Cu_2S}$ will give",
 [r"$\mathrm{Cu + SO_2}$",r"$\mathrm{Cu + SO_3}$",r"$\mathrm{CuO + CuS}$",r"$\mathrm{Cu_2SO_3}$"],
 r"Self-reduction (auto-reduction) takes place: $\mathrm{Cu_2S + 2Cu_2O \rightarrow 6Cu + SO_2}$. Sulphide ion is the reducing agent and is oxidised to $\mathrm{SO_2}$, not $\mathrm{SO_3}$.")
drop("CH-07-Q14","Ampicillin is also generally classed as a broad-spectrum antibiotic, so more than one option can be argued.")
fix("CH-16-Q16",r"How many millilitres of 0.1 N $\mathrm{H_2SO_4}$ solution will be required for complete reaction with a solution containing 0.125 g of pure $\mathrm{Na_2CO_3}$?",
 ["23.6 mL","25.6 mL","26.3 mL","32.6 mL"],
 r"The equivalent weight of $\mathrm{Na_2CO_3}$ is $106/2=53$, so it supplies $\frac{0.125}{53}=2.36\times10^{-3}$ eq. Equating equivalents, $0.1\times\frac{V}{1000}=2.36\times10^{-3}$, which gives $V\approx23.6$ mL.")
fix("CH-11-Q19",r"An engine operating between 150 °C and 25 °C takes 500 J of heat from the higher-temperature reservoir. If there are no frictional losses, the work done by the engine is",
 ["147.7 J","157.75 J","165.85 J","169.95 J"],
 r"With no losses the engine is reversible (Carnot). Here $T_1=423$ K and $T_2=298$ K. $W=Q\frac{T_1-T_2}{T_1}=500\times\frac{125}{423}\approx147.7$ J.")
drop("CH-28-Q21","Stem refers to an unstated reaction or figure (RCOZ substrate is not given).")
fix("CH-18-Q16",r"An electron with $n = 3$ has only one radial node. The orbital angular momentum of the electron will be",
 ["0",r"$\sqrt{6}\,\frac{h}{2\pi}$",r"$\sqrt{2}\,\frac{h}{2\pi}$",r"$3\left(\frac{h}{2\pi}\right)$"],
 r"Radial nodes $= n-l-1 = 1$ with $n=3$ gives $l=1$ (a 3p electron). Orbital angular momentum $=\sqrt{l(l+1)}\frac{h}{2\pi}=\sqrt{2}\frac{h}{2\pi}$. The value $\sqrt{6}\frac{h}{2\pi}$ would correspond to $l=2$.")
fix("CH-08-Q4",r"3.2 moles of hydrogen iodide were heated in a sealed bulb at 444 °C till equilibrium was reached. Its degree of dissociation at this temperature was found to be 22%. The number of moles of hydrogen iodide present at equilibrium is",
 ["2.496","1.87","2","4"],
 r"Moles of HI dissociated $=0.22\times3.2=0.704$. Moles of HI left at equilibrium $=3.2-0.704=2.496$.")
drop("CH-07-Q11","The key (Diazepam) is a tranquilizer, not a non-addictive analgesic. The correct choice would be N-acetyl-p-aminophenol (paracetamol), so the key disagrees with my solution.")
drop("CH-14-Q8","Stem is garbled ('maximum balanced oxide'), so the intended question (number of oxides vs amphoteric etc.) is unclear.")
fix("CH-21-Q20",r"An aqueous solution of a colourless metal sulphate M gives a white precipitate with $\mathrm{NH_4OH}$, which is soluble in excess $\mathrm{NH_4OH}$. On passing $\mathrm{H_2S}$ gas through this solution, a white precipitate is formed. The metal M in the salt is",
 ["Ca","Ba","Al","Zn"],
 r"$\mathrm{Zn^{2+}}$ gives white $\mathrm{Zn(OH)_2}$ with $\mathrm{NH_4OH}$, which dissolves in excess as $\mathrm{[Zn(NH_3)_4]^{2+}}$. $\mathrm{H_2S}$ then precipitates white ZnS. $\mathrm{Al(OH)_3}$ is not soluble in excess $\mathrm{NH_4OH}$, and Ca/Ba give no hydroxide precipitate with it.")
drop("CH-09-Q6","Na2O2 (peroxide O at -1) can also act as both oxidising and reducing agent, and SnCl2 arguably can too, so the answer is not unique.")
fix("CH-07-Q1",r"For a real (van der Waals) gas at the Boyle temperature and low pressure, the pressure may be ($V_m$ = molar volume)",
 [r"$abV_m$",r"$\frac{V_m}{ab}$",r"$\frac{a}{bV_m}$",r"$\frac{b}{aV_m}$"],
 r"At the Boyle temperature $T_B=\frac{a}{Rb}$, a gas behaves ideally at low pressure, so $Z=\frac{PV_m}{RT}=1$. Then $P=\frac{RT_B}{V_m}=\frac{R\cdot\frac{a}{Rb}}{V_m}=\frac{a}{bV_m}$.")
fix("CH-09-Q19",r"The disease that occurs due to eating fish with a high Hg content is",
 ["Minamata disease","Beri-beri","Kwashiorkor","Osteosclerosis"],
 r"Mercury in water is converted into highly toxic methylmercury, which builds up in fish. People who eat such fish develop Minamata disease, a neurological disorder first reported in Minamata, Japan. Beri-beri and kwashiorkor are nutritional deficiency diseases.")
fix("CH-28-Q24",r"The presence or absence of a hydroxy group on which carbon atom of the sugar differentiates RNA and DNA?",
 [r"$1^{\text{st}}$",r"$2^{\text{nd}}$",r"$3^{\text{rd}}$",r"$4^{\text{th}}$"],
 r"RNA contains ribose, which has an $-\mathrm{OH}$ at C-2'. DNA contains 2'-deoxyribose, which lacks the $-\mathrm{OH}$ at this carbon. Both sugars carry $-\mathrm{OH}$ at C-3', so it is the 2nd carbon that distinguishes them.")
ok("CH-14-Q4",r"Mass of oxygen combined $=5-4=1$ g. Equivalent weight $=\frac{\text{mass of Cu}}{\text{mass of O}}\times8=\frac{4}{1}\times8=32$.")
ok("CH-28-Q17",r"The concentration halves (0.8 to 0.4 M) in 15 min, so $t_{1/2}=15$ min, which is independent of concentration for first order. Going from 0.1 M to 0.025 M is a fall to one quarter, i.e. two half-lives, so $2\times15=30$ min.")
fix("CH-23-Q22",r"Excess silver nitrate is added to a water sample to determine the amount of chloride ion present. 1.4 g of silver chloride is precipitated. The mass of chloride ion present in the sample is (molar masses in g mol$^{-1}$: $\mathrm{AgNO_3}$ = 169.91, AgCl = 143.25)",
 ["0.25 g","0.35 g","0.50 g","0.75 g"],
 r"$\mathrm{Ag^+ + Cl^- \rightarrow AgCl\downarrow}$, so moles of $\mathrm{Cl^-}$ = moles of AgCl $=\frac{1.4}{143.25}$. Mass of $\mathrm{Cl^-}=\frac{1.4}{143.25}\times35.5\approx0.35$ g. The molar mass of $\mathrm{AgNO_3}$ is not needed because it is in excess.")
fix("CH-24-Q18",r"The pH of a solution obtained by mixing 100 mL of 0.2 M $\mathrm{CH_3COOH}$ with 100 mL of 0.2 M NaOH would be ($\mathrm{p}K_a$ of $\mathrm{CH_3COOH}$ = 4.74)",
 ["4.74","8.87","9.10","8.57"],
 r"20 mmol acid reacts completely with 20 mmol NaOH, giving 20 mmol $\mathrm{CH_3COO^-}$ in 200 mL, i.e. 0.1 M. For this salt hydrolysis, $\mathrm{pH}=7+\frac{1}{2}\mathrm{p}K_a+\frac{1}{2}\log C=7+2.37-0.5=8.87$. The value 4.74 would apply to a half-neutralised buffer.")
ok("CH-09-Q17",r"Excess fluoride (above about 2 ppm) in drinking water during tooth formation causes dental fluorosis, i.e. brown mottling of the teeth. Small amounts (about 1 ppm) actually protect enamel by forming fluorapatite.")
fix("CH-13-Q8",r"Mark the oxide which is amphoteric in character.",[r"$\mathrm{CO_2}$",r"$\mathrm{SiO_2}$",r"$\mathrm{SnO_2}$","CaO"],
 r"$\mathrm{SnO_2}$ reacts with both bases ($\mathrm{SnO_2 + 2NaOH \rightarrow Na_2SnO_3 + H_2O}$) and acids ($\mathrm{SnO_2 + 4HCl \rightarrow SnCl_4 + 2H_2O}$), so it is amphoteric. $\mathrm{CO_2}$ and $\mathrm{SiO_2}$ are acidic, and CaO is basic.")
fix("CH-13-Q1",r"Calculate the lowering of vapour pressure caused by adding 100 g of sucrose (molecular mass = 342) to 1000 g of water, if the vapour pressure of pure water at 25 °C is 23.8 mm Hg.",
 ["1.25 mm Hg","0.125 mm Hg","1.15 mm Hg","0.0125 mm Hg"],
 r"$n_{\text{sucrose}}=\frac{100}{342}=0.292$ and $n_{\text{water}}=\frac{1000}{18}=55.5$. By Raoult's law, $\Delta P=P^0\frac{n}{n+N}=23.8\times\frac{0.292}{55.8}\approx0.125$ mm Hg.")
drop("CH-13-Q9","Disputed chemistry: Al is passivated or reacts sluggishly, and Mg gives H2 with very dilute HNO3, so more than one option can be argued.")
ok("CH-20-Q4",r"100 g of water is $\frac{100}{18}=5.56$ mol. $\Delta T=\frac{q}{nC_p}=\frac{1000}{5.56\times75}=2.4$ K.")
fix("CH-07-Q15",r"Asthma patients use a mixture of ______ for respiration.",
 [r"$\mathrm{O_2}$ and $\mathrm{N_2O}$",r"$\mathrm{O_2}$ and He",r"$\mathrm{O_2}$ and $\mathrm{NH_3}$",r"$\mathrm{O_2}$ and CO"],
 r"Helium is inert and very light, so a He–$\mathrm{O_2}$ mixture (heliox) has low density and diffuses easily through narrowed airways, which reduces breathing effort. $\mathrm{N_2O}$ is an anaesthetic, and $\mathrm{NH_3}$ and CO are toxic.")
ok("CH-13-Q5",r"In osmosis, solvent flows through a semipermeable membrane from the less concentrated (dilute) solution to the more concentrated one. Since liquid flows from A to B, A is less concentrated than B.")
fix("CH-07-Q16",r"Electrolysis of fused sodium hydride liberates hydrogen at the",["Anode","Cathode","Cathode and anode both","None of these"],
 r"Fused NaH is ionic: $\mathrm{Na^+H^-}$. Hydride ions move to the anode and are oxidised: $\mathrm{2H^- \rightarrow H_2 + 2e^-}$. Sodium is deposited at the cathode, so $\mathrm{H_2}$ appears at the anode, unlike in the electrolysis of water.")
fix("CH-20-Q1",r"For a first-order reaction $\mathrm{X(g) \rightarrow Y(g) + Z(g)}$, the half-life period is 10 min. In what period of time would the concentration of X be reduced to 10% of its original concentration?",
 ["20 min","33 min","15 min","25 min"],
 r"$k=\frac{0.693}{10}\ \mathrm{min^{-1}}$. For a fall to 10%, $t=\frac{2.303}{k}\log\frac{[X]_0}{0.1[X]_0}=\frac{2.303\times10}{0.693}\approx33$ min. Note that 20 min (two half-lives) only takes the concentration to 25%.")
fix("CH-16-Q13",r"Among the following species, which has the weakest carbon–oxygen bond?",
 [r"$\mathrm{CO_2}$",r"$\mathrm{CH_3COO^-}$","CO",r"$\mathrm{CO_3^{2-}}$"],
 r"C–O bond orders are: CO = 3, $\mathrm{CO_2}$ = 2, $\mathrm{CH_3COO^-}$ = 1.5 (resonance over 2 O), and $\mathrm{CO_3^{2-}}$ = $\frac{4}{3}\approx1.33$ (resonance over 3 O). The lowest bond order means the weakest bond, so the answer is $\mathrm{CO_3^{2-}}$.")
fix("CH-13-Q11",r"Which of the following is in the increasing order of ionic character?",
 [r"$\mathrm{PbCl_4 < PbCl_2 < CaCl_2 < NaCl}$",r"$\mathrm{PbCl_2 < PbCl_4 < CaCl_2 < NaCl}$",r"$\mathrm{PbCl_2 < PbCl_4 < NaCl < CaCl_2}$",r"$\mathrm{PbCl_4 < PbCl_2 < NaCl < CaCl_2}$"],
 r"By Fajans' rules, the small, highly charged $\mathrm{Pb^{4+}}$ polarises $\mathrm{Cl^-}$ the most, so $\mathrm{PbCl_4}$ is the most covalent, followed by $\mathrm{PbCl_2}$. $\mathrm{Ca^{2+}}$ polarises more than $\mathrm{Na^+}$ (higher charge), so NaCl is the most ionic: $\mathrm{PbCl_4 < PbCl_2 < CaCl_2 < NaCl}$.")
fix("CH-20-Q7",r"Choose the chain-terminating step: (a) $\mathrm{H_2 \rightarrow H^\bullet + H^\bullet}$ (b) $\mathrm{Br_2 \rightarrow Br^\bullet + Br^\bullet}$ (c) $\mathrm{Br^\bullet + HBr \rightarrow H^\bullet + Br_2}$ (d) $\mathrm{H^\bullet + Br_2 \rightarrow HBr + Br^\bullet}$ (e) $\mathrm{Br^\bullet + Br^\bullet \rightarrow Br_2}$",
 ["a","c","d","e"],
 r"A termination step uses up free radicals without making new ones. In (e) two $\mathrm{Br^\bullet}$ radicals combine to form $\mathrm{Br_2}$. Steps (c) and (d) consume one radical and produce another (propagation), and (a) and (b) generate radicals (initiation).")
fix("CH-06-Q17",r"The energy required to melt 1 g of ice is 33 J. The number of quanta of radiation of frequency $4.67\times10^{13}\ \mathrm{s^{-1}}$ that must be absorbed to melt 10 g of ice is",
 [r"$1.065\times10^{22}$",r"$3.205\times10^{23}$",r"$9.076\times10^{20}$","None of these"],
 r"Energy needed $=33\times10=330$ J, and each quantum carries $h\nu=6.626\times10^{-34}\times4.67\times10^{13}=3.09\times10^{-20}$ J. So $n=\frac{330}{3.09\times10^{-20}}\approx1.07\times10^{22}$.")
ok("CH-19-Q6",r"Azides (e.g. $\mathrm{Pb(N_3)_2}$, $\mathrm{AgN_3}$, $\mathrm{Ba(N_3)_2}$) decompose rapidly and exothermically on heating to release $\mathrm{N_2}$ gas, and many of them explode; lead azide is used as a detonator. Sulphates, chlorides and phosphides do not explode on heating.")
ok("CH-22-Q4",r"CaO is called quick lime. Slaked lime is $\mathrm{Ca(OH)_2}$, milk of lime is a suspension of $\mathrm{Ca(OH)_2}$ in water, and limestone is $\mathrm{CaCO_3}$.")
fix("CH-11-Q1",r"The conversion of $\mathrm{PbO_2}$ to $\mathrm{Pb(NO_3)_2}$ is",
 ["Oxidation","Reduction","Neither oxidation nor reduction","Both oxidation and reduction"],
 r"Pb is $+4$ in $\mathrm{PbO_2}$ and $+2$ in $\mathrm{Pb(NO_3)_2}$. The decrease in oxidation number means Pb is reduced.")
fix("CH-05-Q19",r"Aspirin has the formula $\mathrm{C_9H_8O_4}$. How many atoms of oxygen are there in a tablet weighing 360 mg?",
 [r"$1.204\times10^{23}$",r"$1.08\times10^{22}$",r"$1.204\times10^{24}$",r"$4.81\times10^{21}$"],
 r"Molar mass $=180$ g/mol, so moles of aspirin $=\frac{0.360}{180}=2\times10^{-3}$. O atoms $=2\times10^{-3}\times4\times6.022\times10^{23}\approx4.81\times10^{21}$.")
fix("CH-16-Q19",r"What will be the concentration of $\mathrm{Ca^{2+}}$ ions in a 1 litre sample of hard water if, after treatment with washing soda, 10 g of insoluble $\mathrm{CaCO_3}$ is precipitated?",
 ["0.2 M","0.1 M","0.3 M","0.4 M"],
 r"$\mathrm{Ca^{2+} + Na_2CO_3 \rightarrow CaCO_3\downarrow + 2Na^+}$, so moles of $\mathrm{Ca^{2+}}$ = moles of $\mathrm{CaCO_3}=\frac{10}{100}=0.1$. In 1 L this is 0.1 M.")
fix("CH-18-Q17",r"At 273 K and 9 atm pressure, the compressibility factor of a gas is 0.9. The volume of 1 millimole of the gas at this temperature and pressure is",
 ["2.24 litre","0.020 mL","2.24 mL","22.4 mL"],
 r"$V=\frac{ZnRT}{P}=\frac{0.9\times10^{-3}\times0.0821\times273}{9}=2.24\times10^{-3}$ L $=2.24$ mL.")
fix("CH-07-Q6",r"The compressibility factor of a gas is 0.9 at 273 K and 9 atm. Find the volume of $10^{-3}$ mol of the gas at this T and P ($R = 0.0821$ atm L mol$^{-1}$ K$^{-1}$).",
 ["2.24 L","22.4 L","2.24 mL","22.4 mL"],
 r"$Z=\frac{PV}{nRT}$ gives $V=\frac{0.9\times10^{-3}\times0.0821\times273}{9}=2.24\times10^{-3}$ L $=2.24$ mL.")
drop("CH-10-Q16","Option D is truncated (the energy value is missing), so the question is incomplete.")
fix("CH-11-Q7",r"When $\mathrm{SO_2}$ is passed through an acidic solution of potassium dichromate, chromium sulphate is formed. The change in oxidation state of chromium is",
 ["+4 to +2","+5 to +3","+6 to +3","+7 to +2"],
 r"$\mathrm{Cr_2O_7^{2-} + 3SO_2 + 2H^+ \rightarrow 2Cr^{3+} + 3SO_4^{2-} + H_2O}$. Cr goes from $+6$ in dichromate to $+3$ in $\mathrm{Cr_2(SO_4)_3}$, and $\mathrm{SO_2}$ is oxidised to sulphate.")
drop("CH-11-Q2","Stem is factually wrong: H2O2 oxidises (not reduces) K4[Fe(CN)6] in acidic solution, and it reduces K3[Fe(CN)6] in alkaline solution. As written, the keyed answer is wrong.")
fix("CH-20-Q9",r"A solution of urea (mol. wt. 60) contains 8.6 g per litre. It is isotonic with a 5% (w/v) solution of a non-volatile solute. The molecular weight of the solute will be",
 ["348.9","34.89","3489","861.2"],
 r"Isotonic non-electrolyte solutions have equal molar concentrations. Urea: $\frac{8.6}{60}=0.1433$ mol/L. A 5% solute contains 50 g/L, so $\frac{50}{M}=0.1433$, which gives $M\approx348.9$.")
fix("CH-23-Q1",r"0.22 g of a monohydric alcohol (A) liberates 56 mL of $\mathrm{CH_4}$ at STP on reaction with $\mathrm{CH_3MgBr}$. The molecular weight of the alcohol is",
 ["88 g","55 g","66 g","80 g"],
 r"$\mathrm{ROH + CH_3MgBr \rightarrow CH_4 + ROMgBr}$, so 1 mol of alcohol gives 1 mol of $\mathrm{CH_4}$. Moles of $\mathrm{CH_4}=\frac{56}{22400}=\frac{1}{400}$. Hence $M=0.22\times400=88$ g/mol (for example $\mathrm{C_5H_{11}OH}$).")
fix("CH-19-Q20",r"Which of the following oxides is amphoteric in nature?",
 [r"$\mathrm{N_2O_3}$",r"$\mathrm{P_4O_6}$",r"$\mathrm{Sb_4O_6}$",r"$\mathrm{Bi_2O_3}$"],
 r"Acidic character decreases down group 15. $\mathrm{N_2O_3}$ and $\mathrm{P_4O_6}$ are acidic, $\mathrm{Sb_4O_6}$ is amphoteric (it dissolves in both NaOH and HCl), and $\mathrm{Bi_2O_3}$ is basic.")
fix("CH-08-Q16",r"Colour is imparted to glass by mixing",["Synthetic dyes","Metal oxides","Oxides of non-metals","Coloured salts"],
 r"Glass is coloured by fusing small amounts of transition-metal oxides into the melt. For example, CoO gives blue, $\mathrm{Cr_2O_3}$ gives green and $\mathrm{Cu_2O}$ gives red. Organic dyes would decompose at glass-melting temperatures.")
fix("CH-16-Q18",r"What can be the maximum percentage of available chlorine in a bleaching powder sample? (Take the formula of bleaching powder as $\mathrm{CaOCl_2}$.)",
 ["52.9","55.9","58","60"],
 r"Available chlorine is the $\mathrm{Cl_2}$ released by the action of dilute acid: $\mathrm{CaOCl_2 + H_2SO_4 \rightarrow CaSO_4 + H_2O + Cl_2}$. Since 127 g of $\mathrm{CaOCl_2}$ gives 71 g of $\mathrm{Cl_2}$, the maximum is $\frac{71}{127}\times100=55.9\%$.")
ok("CH-08-Q12",r"Glucose (an aldose) reduces Fehling's solution: $\mathrm{Cu^{2+}}$ is reduced to $\mathrm{Cu_2O}$, which comes down as a red (brick-red) precipitate, while glucose is oxidised to gluconic acid.")
fix("CH-22-Q16",r"Which of the following polymers is synthesised using a free-radical polymerisation technique?",
 ["Teflon","Terylene","Melamine polymer","Nylon 6,6"],
 r"Teflon is made by free-radical addition polymerisation of tetrafluoroethylene ($\mathrm{CF_2=CF_2}$), using a peroxide or persulphate initiator. Terylene, melamine–formaldehyde resin and nylon 6,6 are all condensation polymers.")
fix("CH-09-Q4",r"Which of the following is not a reducing agent?",[r"$\mathrm{NaNO_2}$",r"$\mathrm{NaNO_3}$","HI",r"$\mathrm{SnCl_2}$"],
 r"In $\mathrm{NaNO_3}$, N is already in its highest oxidation state ($+5$), so it cannot be oxidised and can act only as an oxidising agent. $\mathrm{NaNO_2}$ (N $+3$), HI ($\mathrm{I^-}$) and $\mathrm{SnCl_2}$ ($\mathrm{Sn^{2+}}$) can all be oxidised, so they are reducing agents.")
fix("CH-06-Q13",r"The radial probability distribution curve of an orbital of H has 4 local maxima. If the orbital has 3 angular nodes, the orbital will be",
 ["7f","8f","7d","8d"],
 r"The number of maxima is radial nodes + 1, so radial nodes $= n-l-1 = 3$ and $n-l=4$. Angular nodes $= l = 3$ (an f orbital), so $n=7$, giving 7f.")
fix("CH-24-Q8",r"What is the minimum mass of $\mathrm{CaCO_3(s)}$ required to establish equilibrium in a 6.50 litre container for the reaction $\mathrm{CaCO_3(s) \rightleftharpoons CaO(s) + CO_2(g)}$, $K_c = 0.05$? (Below this mass, it decomposes completely.)",
 ["32.5 g","24.6 g","40.9 g","8.0 g"],
 r"$K_c=[\mathrm{CO_2}]=0.05$ mol/L, so moles of $\mathrm{CO_2}$ at equilibrium $=0.05\times6.50=0.325$. This needs 0.325 mol of $\mathrm{CaCO_3}$ to decompose, i.e. $0.325\times100=32.5$ g. With any less, all of it would decompose before equilibrium is reached.")
fix("CH-12-Q4",r"The intermetallic compound LiAg crystallises in a cubic lattice in which both lithium and silver have a coordination number of eight. The crystal class is",
 ["Simple cubic","Body-centred cubic","Face-centred cubic","None of these"],
 r"A coordination number of 8 corresponds to the body-centred (CsCl-type) arrangement. Each Li sits at the body centre of a cube of 8 Ag atoms, and vice versa. Simple cubic gives CN 6 and fcc gives CN 12.")
fix("CH-21-Q1",r"In which case is the formation of butanenitrile possible?",
 [r"$\mathrm{C_3H_7Br + KCN}$",r"$\mathrm{C_4H_9Br + KCN}$",r"$\mathrm{C_3H_7OH + KCN}$",r"$\mathrm{C_4H_9OH + KCN}$"],
 r"$\mathrm{C_3H_7Br + KCN \rightarrow C_3H_7CN + KBr}$. The $-\mathrm{CN}$ carbon is counted in IUPAC naming, so $\mathrm{CH_3CH_2CH_2CN}$ is butanenitrile. $\mathrm{C_4H_9Br}$ would give pentanenitrile, and alcohols do not undergo substitution with KCN because $\mathrm{OH^-}$ is a poor leaving group.")
ok("M-10-Q2",r"Over all 24 arrangements, each digit appears 6 times in each place, giving $6(0+2+3+5)(1111)=66660$. Subtract the arrangements with 0 in front: each of 2, 3, 5 appears twice in each of the last three places, giving $2(10)(111)=2220$. The required sum is $66660-2220=64440$.")
fix("M-18-Q2",r"If $|z_1| = 1$, $|z_2| = 2$, $|z_3| = 3$ and $|z_2z_3 + 4z_1z_3 + 9z_1z_2| = 12$, then the value of $|z_1 + z_2 + z_3|$ equals",
 ["2","3","5","13"],
 r"Since $z\bar z=|z|^2$, we have $\frac{1}{z_1}=\bar z_1$, $\frac{4}{z_2}=\bar z_2$ and $\frac{9}{z_3}=\bar z_3$. So $z_2z_3+4z_1z_3+9z_1z_2=z_1z_2z_3(\bar z_1+\bar z_2+\bar z_3)$. Taking moduli, $12=6|z_1+z_2+z_3|$, which gives $|z_1+z_2+z_3|=2$.")

src=json.load(open('D:/PersonalProjects/Revanth/bitsat-mock/.harvest/verify/eq_batch1.json',encoding='utf-8'))
refs=[x['ref'] for x in src]
assert set(refs)==set(R), (set(refs)-set(R), set(R)-set(refs))
out='D:/PersonalProjects/Revanth/bitsat-mock/.harvest/verify/eq_batch1.result.json'
with open(out,'w',encoding='utf-8') as f: json.dump(R,f,ensure_ascii=False,indent=1)
d=json.load(open(out,encoding='utf-8'))
from collections import Counter; print(len(d),Counter(v['verdict'] for v in d.values()))
