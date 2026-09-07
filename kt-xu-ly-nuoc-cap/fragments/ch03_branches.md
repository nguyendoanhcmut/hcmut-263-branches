## Chương 3: Coagulation and Flocculation

### 3.1 Overview of Coagulation and Flocculation Processes

#### 3.1.1 Process Definitions and Multi-Barrier Treatment Objectives

##### 3.1.1.1 Distinction Between Coagulation and Flocculation Unit Operations
###### Physical-Chemical Boundary Definitions & Transformation Steps
In municipal and industrial water treatment engineering, chemical coagulation and physical flocculation represent two fundamentally distinct yet intimately coupled unit operations designed to destabilize, aggregate, and remove finely dispersed colloidal impurities, natural organic matter (NOM), and suspended particulates.
- **Chemical Coagulation (Keo tụ hóa học)** is defined as the rapid physical-chemical conditioning process initiated by the instantaneous dispersion of chemical coagulants (such as multivalent metal salts or synthetic polyelectrolytes) into raw water. Coagulation operates on microscopic spatial scales ($< 1\text{ }\mu\text{m}$) and millisecond-to-second timescales ($t = 0.1 - 5\text{ s}$ for micro-mixing, up to $30 - 120\text{ s}$ in stirred reactors). Its primary objective is to overcome the repulsive electrostatic surface potentials of colloidal suspensions, compress the electrical double layer (EDL), neutralize particle surface charges, or precipitate insoluble metal hydroxide micro-matrices.
- **Physical Flocculation (Tạo bông cặn)** is defined as the subsequent hydrodynamic transport and aggregation process wherein destabilized submicron particles and micro-flocs are brought into physical contact through controlled fluid shear and velocity gradients ($G = 10 - 80\text{ s}^{-1}$ over detention times $t = 15 - 45\text{ min}$). Flocculation transforms non-settleable micro-colloids into large, dense, shear-resistant macro-flocs ($d_p = 0.1 - 2.0\text{ mm}$) capable of rapid phase separation in downstream sedimentation basins and granular media filters.

###### Target Water Quality Objectives & Contaminant Barrier Roles
Coagulation and flocculation serve as the primary multi-barrier physicochemical defense against microbiological pathogens and toxic organic precursors in conventional surface water clarification:
1. **Microbiological Pathogen Removal and Inactivation**: Colloidal-scale pathogenic microorganisms, including enteric viruses ($0.02 - 0.08\text{ }\mu\text{m}$), pathogenic bacteria such as *Escherichia coli*, *Salmonella*, and *Vibrio cholerae* ($0.5 - 2.0\text{ }\mu\text{m}$), and chlorine-resistant protozoan cysts (*Giardia lamblia*, $8 - 14\text{ }\mu\text{m}$) and oocysts (*Cryptosporidium parvum*, $4 - 6\text{ }\mu\text{m}$), carry net negative surface charges in natural water matrices. Effective coagulation entraps and enmeshes these pathogens within metal hydroxide matrices, achieving up to $2.0 - 3.0\text{ log}_{10}$ physical removal across clarification and filtration.
2. **Removal of Toxic Compounds Adsorbed to Particle Surfaces**: Heavy metals (lead, arsenic, cadmium, chromium), hydrophobic organic micropollutants (pesticides, polychlorinated biphenyls, polycyclic aromatic hydrocarbons), and industrial surfactants partition extensively onto inorganic clay surfaces and organic colloids. Phase separation via coagulation prevents these contaminants from penetrating finished water supplies.
3. **Removal of Disinfection Byproduct (DBP) Precursors**: Natural Organic Matter (NOM), consisting primarily of humic and fulvic acids ($1,000 - 50,000\text{ Da}$), reacts with chemical disinfectants (free chlorine) during secondary treatment to form carcinogenic disinfection byproducts, including Trihalomethanes (THMs) and Haloacetic Acids (HAAs). Coagulation optimized for enhanced organics removal (keo tụ tăng cường) preferentially targets high-molecular-weight, hydrophobic UV-absorbing aromatic NOM fractions.
4. **Palatability, Clarity, and Aesthetic Quality**: Coagulation eliminates true color (Pt-Co scale) derived from vegetative humic extracts and apparent turbidity caused by colloidal clay, silt, and iron/manganese oxyhydroxides, consistently achieving post-clarification turbidities $< 2.0\text{ NTU}$ (and filtered turbidities $< 0.1 - 0.5\text{ NTU}$) in strict compliance with national potable water criteria.

##### 3.1.1.2 Integration in Water Treatment Flow Trains
###### Conventional Treatment Train Configuration
In conventional surface water treatment plants (Nhà máy nước xử lý quy chuẩn), coagulation and flocculation occupy the central pre-treatment position following preliminary screening and grit removal:
$$\text{Raw Water} \rightarrow \text{Screening / Intake} \rightarrow \text{Rapid Flash Mix (Coagulation)} \rightarrow \text{Multi-Stage Flocculation} \rightarrow \text{Sedimentation / Clarification} \rightarrow \text{Rapid Sand Filtration} \rightarrow \text{Disinfection} \rightarrow \text{Clearwell}$$
In this sequence, chemical coagulants (alum, ferric chloride, or PAC) and pH-adjusting chemicals (hydrated lime, soda ash) are injected into the high-shear rapid mix basin. The conditioned suspension flows directly into a multi-compartment flocculation basin, where gentle hydrodynamic agitation promotes floc maturation. The enlarged flocs enter quiescent sedimentation basins (rectangular horizontal settling tanks or high-rate inclined lamella clarifiers) where $> 90\%$ of settleable suspended solids are removed by gravity prior to granular media depth filtration.

###### Direct Filtration and Contact Filtration Configurations
For high-quality upland reservoirs or pristine surface waters exhibiting persistently low turbidity ($< 10 - 15\text{ NTU}$), low true color ($< 15 - 20\text{ TCU}$), and low algae counts, conventional sedimentation may be eliminated:
- **Direct Filtration (Lọc trực tiếp)**: Raw water receives coagulant addition in a rapid flash mixer, passes through a shortened flocculation stage ($t = 5 - 15\text{ min}$ with moderate $G = 30 - 50\text{ s}^{-1}$) to form micro-flocs, and is applied directly to deep-bed dual-media (anthracite/sand) granular filters without prior sedimentation.
- **Contact Filtration (Lọc tiếp xúc / In-line Coagulation)**: Eliminates both separate flocculation and sedimentation basins. Chemical coagulant (frequently a cationic polymer or low-dose hydrolyzing metal salt) is injected directly into the influent pipeline ahead of granular media filters. Destabilization, collision, and aggregation occur entirely within the tortuous interstitial pore channels and grain surfaces of the filter bed.

#### 3.1.2 Four Sequential Steps in Coagulation-Flocculation

##### 3.1.2.1 Coagulant Transformation & Hydrolysis Chemistry
###### Primary Microsecond Dissolution & Mononuclear Hydrolysis Speciation
When trivalent metal salts such as aluminum sulfate [$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$] or ferric chloride [$\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$] are injected into water, the free metal cations ($\text{Al}^{3+}$ or $\text{Fe}^{3+}$) are thermodynamically unstable and immediately hydrate to form octahedral hexaquo complexes $[\text{Al}(\text{H}_2\text{O})_6]^{3+}$ and $[\text{Fe}(\text{H}_2\text{O})_6]^{3+}$. Within microseconds ($10^{-6} - 10^{-2}\text{ s}$), these primary aquo-cations undergo rapid stepwise deprotonation (hydrolysis) reactions:
$$[\text{Al}(\text{H}_2\text{O})_6]^{3+} + \text{H}_2\text{O} \rightleftharpoons [\text{Al}(\text{H}_2\text{O})_5(\text{OH})]^{2+} + \text{H}_3\text{O}^+$$
$$[\text{Al}(\text{H}_2\text{O})_5(\text{OH})]^{2+} + \text{H}_2\text{O} \rightleftharpoons [\text{Al}(\text{H}_2\text{O})_4(\text{OH})_2]^+ + \text{H}_3\text{O}^+$$
$$[\text{Al}(\text{H}_2\text{O})_4(\text{OH})_2]^+ + \text{H}_2\text{O} \rightleftharpoons \text{Al}(\text{OH})_3(\text{s}) + 3\text{H}_2\text{O} + \text{H}_3\text{O}^+$$
$$[\text{Al}(\text{OH})_3(\text{s})] + \text{H}_2\text{O} \rightleftharpoons [\text{Al}(\text{OH})_4]^- + \text{H}_3\text{O}^+$$
Concurrently, rapid condensation and olation reactions generate multimeric and polymeric cationic polyhydroxy complexes, such as the dimer $[\text{Al}_2(\text{OH})_2]^{4+}$, the trimer $[\text{Al}_3(\text{OH})_4]^{5+}$, and the tridecameric Keggin ion $[\text{Al}_{13}\text{O}_4(\text{OH})_{24}(\text{H}_2\text{O})_{12}]^{7+}$.

##### 3.1.2.2 Adsorption and Surface Charge Interaction Kinetics
###### Mass Transport & Uptake Kinetics of Hydrolyzed Metal Cations
Following hydrolysis, positively charged mononuclear and polynuclear metal hydrolysis intermediates diffuse through the hydrodynamic boundary layer surrounding negatively charged colloidal particles. The timescale of transport and specific chemical adsorption onto particle surface hydroxyl, carboxyl, and phenolic functional groups is on the order of $0.01 - 0.1\text{ s}$. The intense positive charge of these intermediate species reduces the negative electrostatic surface potential of the colloids via inner-sphere coordinate bonding and outer-sphere electrostatic accumulation.

##### 3.1.2.3 Particle Destabilization Dynamics
###### Electrokinetic Charge Reduction & Hydrophobic Hydroxide Precipitation
As cationic hydrolysis species or synthetic polymer segments adsorb onto colloidal surfaces, the electrokinetic potential at the shear plane (zeta potential, $\zeta$) shifts from highly negative values (typically $-25\text{ mV}$ to $-40\text{ mV}$ in raw water) toward the isoelectric point ($\,\zeta = 0\text{ mV}$). Concurrently, when the solubility product of the metal hydroxide is exceeded ($[\text{Al}^{3+}][\text{OH}^-]^3 > K_{sp} \approx 10^{-32}$ to $10^{-33}$), amorphous, insoluble $\text{Al}(\text{OH})_3(\text{s})$ or $\text{Fe}(\text{OH})_3(\text{s})$ nuclei precipitate rapidly within $0.1 - 1.0\text{ s}$, creating a hydrophobic, sticky interface that destabilizes the suspension.

##### 3.1.2.4 Interparticle Collision & Orthokinetic Aggregate Growth
###### Fluid Shear-Induced Collisions & Polymeric Floc Network Formation
Once colloidal particles are destabilized, thermal Brownian motion (perikinetic flocculation) governs collisions between submicron particles ($d_p < 1\text{ }\mu\text{m}$) over the first several seconds. Subsequently, bulk fluid velocity gradients and turbulent eddies generated in the flocculation basin drive macroscopic fluid shear collisions (orthokinetic flocculation) between particles ($d_p > 1\text{ }\mu\text{m}$). The collision frequency per unit reactor volume is directly proportional to the velocity gradient $G$ and the cube of particle collision diameters. Hydroxide precipitates and long-chain polymer molecules act as intermolecular glue, entrapping particles and assembling robust fractal floc agglomerates.


### 3.2 Theoretical Principles of Colloidal Stability and Chemical Coagulation

#### 3.2.1 Colloidal Stability, Particle Dimensions & Settling Kinetics

##### 3.2.1.1 Particle Size Continuum & Colloidal Classifications
###### Dimensional Spectrum from Dissolved Solutes to Settleable Flocs
Particulate impurities in natural surface and ground waters span a dimensional spectrum across eight orders of magnitude:
1. **Dissolved Solutes ($d_p < 1\text{ nm} = 10^{-3}\text{ }\mu\text{m}$)**: Includes simple inorganic ions ($\text{Na}^+$, $\text{Ca}^{2+}$, $\text{Cl}^-$, $\text{SO}_4^{2-}$), low-molecular-weight organic acids, and dissolved gases. These species do not scatter visible light and cannot be removed by gravity settling or conventional depth filtration without chemical transformation.
2. **Colloidal Suspensions ($1\text{ nm} \le d_p \le 1\text{ }\mu\text{m}$)**: Microscopic particles whose movement in water is predominantly governed by Brownian thermal diffusion rather than gravitational sedimentation. Colloids exhibit the Tyndall effect (scattering of focused light beams) and possess an extraordinarily large specific surface area ($A_{\text{spec}} = 6 / (\rho_p d_p) > 10^5 - 10^7\text{ m}^2/\text{m}^3$), which amplifies interfacial electrostatic, hydrophobic, and chemical interactions.
3. **Suspended Solids and Flocs ($d_p > 1\text{ }\mu\text{m}$ to $1,000\text{ }\mu\text{m}$)**: Fine silts, microscopic algae, sand grains, and aggregated floc networks. Particles with diameters exceeding $10 - 20\text{ }\mu\text{m}$ possess sufficient settling velocities to separate gravimetrically under laminar conditions within reasonable hydraulic detention times.

###### Origins & Surface Characteristics of Natural Water Colloids
Natural water colloids originate from geological weathering and biological decay:
- **Inorganic Mineral Fragments**: Layered aluminosilicate clay minerals (kaolinite, montmorillonite, illite) and quartz silica. Clay colloids acquire permanent structural negative charge through isomorphous substitution of tetravalent silicon ($\text{Si}^{4+}$) by trivalent aluminum ($\text{Al}^{3+}$) in tetrahedral silica sheets, and trivalent aluminum by divalent magnesium ($\text{Mg}^{2+}$) in octahedral sheets.
- **Metal Oxyhydroxides**: Hydrous iron oxides [$\alpha\text{-FeOOH}$, $\text{Fe}(\text{OH})_3$] and manganese dioxides ($\text{MnO}_2$), whose surface charge depends on amphoteric surface hydroxyl groups ($-\text{FeOH}_2^+ \rightleftharpoons -\text{FeOH} + \text{H}^+ \rightleftharpoons -\text{FeO}^- + 2\text{H}^+$).
- **Natural Organic Macromolecules (NOM)**: Humic and fulvic acids derived from decaying soil humus and aquatic vegetation. These polyelectrolytes carry dense ionizable carboxyl ($\text{-COOH}$, $\text{p}K_a \approx 3.5 - 5.0$) and phenolic hydroxyl ($\text{-OH}$, $\text{p}K_a \approx 8.0 - 10.0$) functional groups that impart strong negative surface charge across the circumneutral pH range of natural waters (pH 6.0–8.5).
- **Biological Organisms**: Bacterial cells, viruses, algae, and extracellular polymeric substances (EPS) possessing surface lipopolysaccharides and proteins with terminal carboxylate and phosphate moieties.

##### 3.2.1.2 Stokes' Law Discrete Particle Settling Velocities
###### Stokes' Settling Velocity Derivation & Formula
The terminal settling velocity of a single discrete, spherical colloidal or suspended particle settling under quiescent laminar hydrodynamic conditions (Reynolds number $Re_p = \rho_w v_s d_p / \mu < 0.5$) is governed by Stokes' Law (`eq_ch03_008`):

$$v_s = \frac{g (\rho_p - \rho_w) d_p^2}{18 \mu}$$

**Plain Text Formulation:** `v_s = (g * (rho_p - rho_w) * d_p^2) / (18 * mu)`

**Description:** Derives from equating the net downward gravitational force ($F_g = \frac{1}{6}\pi d_p^3 (\rho_p - \rho_w) g$) to the hydrodynamic laminar drag force ($F_d = 3\pi \mu v_s d_p$) acting on a sphere moving through a viscous continuum.

**Key Variables & Engineering Units:**
- $v_s$: Terminal discrete particle settling velocity ($\text{m/s}$ or $\text{mm/s}$)
- $g$: Gravitational acceleration constant ($9.81\text{ m/s}^2$)
- $\rho_p$: Density of the solid particulate matter (typically $2,650\text{ kg/m}^3$ for silica/clay minerals, $1,050 - 1,200\text{ kg/m}^3$ for biological and organic colloids)
- $\rho_w$: Fluid density of water ($998.2\text{ kg/m}^3$ at $20^\circ\text{C}$, $997.0\text{ kg/m}^3$ at $25^\circ\text{C}$)
- $d_p$: Equivalent spherical particle diameter ($\text{m}$)
- $\mu$: Dynamic (absolute) viscosity of water ($1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at $20^\circ\text{C}$, $0.890 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at $25^\circ\text{C}$)

###### Particle Settling Kinetic Analysis & The Physical Necessity of Aggregation
Because discrete settling velocity scales with the square of particle diameter ($v_s \propto d_p^2$), reducing particle size dramatically lengthens the time required for gravitational sedimentation over a typical clarifier liquid depth of $1.0\text{ m}$ (Table `tbl_ch03_01`):

| Particle Diameter ($d_p$, mm) | Representative Particle Classification | Calculated Settling Velocity ($v_s$, mm/s) | Required Theoretical Time to Settle 1 Meter Depth | Physical Removal Feasibility Without Coagulation |
|---|---|---|---|---|
| $10\text{ mm}$ | Coarse gravel / Large sand | $1,000\text{ mm/s}$ | $1\text{ second}$ | Instantaneous removal in coarse intake bar racks and grit traps |
| $1\text{ mm}$ | Medium sand grain | $100\text{ mm/s}$ | $10\text{ seconds}$ | Readily separated in standard grit chambers |
| $0.1\text{ mm}$ ($100\text{ }\mu\text{m}$) | Fine silica sand | $8.0\text{ mm/s}$ | $2\text{ minutes}$ | Rapidly settled in pre-sedimentation / silt basins |
| $0.01\text{ mm}$ ($10\text{ }\mu\text{m}$) | Silt / Coarse sludge particles | $0.154\text{ mm/s}$ | $2\text{ hours}$ | Feasible in conventional large sedimentation clarifiers |
| $0.001\text{ mm}$ ($1\text{ }\mu\text{m}$) | Fine clay particles | $1.54 \times 10^{-3}\text{ mm/s}$ | $7\text{ days} \approx 1\text{ week}$ | Completely impractical; requires immense detention basins |
| $0.0001\text{ mm}$ ($0.1\text{ }\mu\text{m}$) | Submicron fine clay / Bacteria | $1.54 \times 10^{-5}\text{ mm/s}$ | $2\text{ years}$ | Physically impossible to settle under normal flow conditions |
| $0.00001\text{ mm}$ ($0.01\text{ }\mu\text{m}$) | True colloidal humic macromolecules / Viruses | $1.54 \times 10^{-7}\text{ mm/s}$ | $200\text{ years}$ | Completely stable indefinite suspension; perpetual brownian motion |

This mathematical reality confirms that **coagulation and flocculation are physically indispensable**. To achieve sedimentation within standard clarifier detention times ($1.5 - 4.0\text{ hours}$), submicron colloids must be aggregated into macro-flocs with effective hydraulic diameters $d_p \ge 100 - 1,000\text{ }\mu\text{m}$, boosting settling velocities by a factor of $10^4$ to $10^8$.

#### 3.2.2 Electrical Double Layer Structure & Electrokinetic Zeta Potential

##### 3.2.2.1 Gouy-Chapman-Stern Electrical Double Layer Architecture
###### Inner Helmholtz Plane (IHP), Outer Helmholtz Plane (OHP), and Stern Layer
To maintain macroscopic electroneutrality in aqueous solution, a negatively charged colloidal particle is surrounded by an organized distribution of counter-ions (cations) and co-ions (anions) known as the **Electrical Double Layer (EDL)** (Lớp điện kép). The modern Gouy-Chapman-Stern-Grahame model subdivides the interfacial region into three distinct zones:
1. **Inner Helmholtz Plane (IHP)**: Defined by the locus of centers of specifically adsorbed, dehydrated counter-ions or non-ionic molecules directly bound to surface functional groups via covalent, coordinate, or hydrophobic bonds.
2. **Outer Helmholtz Plane (OHP)**: Defined by the closest distance of approach of fully hydrated counter-ions attracted purely by long-range electrostatic Coulombic forces ($x \approx 0.3 - 0.5\text{ nm}$).
3. **Stern Layer (Compact Layer)**: The rigid interfacial layer bounded between the solid particle surface and the OHP. The electric potential drops precipitously and linearly from the true surface potential ($\psi_0$) across the Stern layer to the Stern potential ($\psi_d$) at the OHP due to high dielectric saturation of immobilized water dipoles.

###### Gouy-Chapman Diffuse Ion Layer & Debye Screening Length
Beyond the Stern layer lies the **Gouy-Chapman Diffuse Layer**, where hydrated counter-ions remain free to diffuse into the bulk electrolyte under the competing influences of electrostatic attraction toward the negative surface and thermal Brownian kinetic dispersion. The local electrostatic potential $\psi(x)$ at distance $x$ from the surface decays exponentially in accordance with the linearized Poisson-Boltzmann equation:
$$\psi(x) = \psi_d \exp(-\kappa x)$$
where $\kappa$ is the **Debye-Hückel parameter** (inverse screening length), defined as:
$$\kappa = \sqrt{\frac{2000 F^2 I}{\varepsilon_r \varepsilon_0 R T}} = \sqrt{\frac{e^2 \sum n_{i0} z_i^2}{\varepsilon_r \varepsilon_0 k_B T}}$$
The reciprocal $\kappa^{-1}$ is the **Debye screening length (characteristic thickness of the electrical double layer)**:
- In low-ionic-strength pure or soft waters ($I = 10^{-4}\text{ M}$), $\kappa^{-1} \approx 30\text{ nm}$, creating an extended, highly repulsive diffuse atmosphere.
- In moderate surface waters ($I = 10^{-2}\text{ M}$), $\kappa^{-1} \approx 3\text{ nm}$.
- In high-salinity seawater ($I = 0.7\text{ M}$), $\kappa^{-1} < 0.4\text{ nm}$, collapsing the diffuse layer entirely.

##### 3.2.2.2 Electrokinetic Shear Plane & Zeta Potential Measurement
###### Helmholtz-Smoluchowski Zeta Potential Formulation
When an external electric field is applied across a colloidal suspension, the charged particle migrates toward the oppositely charged electrode (electrophoresis). As the particle moves, it drags along a tightly bound layer of solvent molecules and ions. The boundary separating this moving hydrodynamic envelope from the stationary bulk liquid is the **plane of shear (slipping plane)**. The electrokinetic potential measured at this precise shear plane is designated as the **Zeta Potential ($\zeta$, Thế Zeta)**.
Under conditions where the particle radius is much larger than the double-layer thickness ($a \gg \kappa^{-1}$, or $\kappa a > 100$), the electrokinetic potential is rigorously calculated via the **Helmholtz-Smoluchowski Equation** (`eq_ch03_007`):

$$\zeta = \frac{\mu \cdot U_E}{\varepsilon_r \cdot \varepsilon_0} = \frac{4\pi \mu U_E}{D}$$

**Plain Text Formulation:** `zeta = (mu * U_E) / (epsilon_r * epsilon_0)`

**Description:** Relates the electrokinetic zeta potential at the hydrodynamic shear plane to electrophoretic mobility, fluid dynamic viscosity, and relative dielectric permittivity.

**Key Variables & Engineering Units:**
- $\zeta$: Zeta potential at the slipping plane ($\text{mV}$, typically $-15\text{ mV}$ to $-40\text{ mV}$ for natural raw water colloids)
- $\mu$: Dynamic absolute viscosity of water ($0.890 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at $25^\circ\text{C}$)
- $U_E$: Electrophoretic mobility of the colloidal particle, defined as migration velocity per unit electric field gradient ($\mu\text{m}\cdot\text{cm} / (\text{V}\cdot\text{s})$ or $\text{m}^2/(\text{V}\cdot\text{s})$)
- $\varepsilon_r$: Relative permittivity (dielectric constant) of water ($\,\approx 78.54$ at $25^\circ\text{C}$, dimensionless)
- $\varepsilon_0$: Permittivity of free space ($8.854 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2) = 8.854 \times 10^{-12}\text{ F/m}$)
- $D$: Dielectric constant in electrostatic CGS formulation ($D = \varepsilon_r$)

###### Electrophoretic Mobility & Streaming Current Detector (SCD) Instrumentation
Colloidal stability is directly diagnosed via electrokinetic measurements:
- **Zeta Potential Thresholds**:
  - $|\zeta| > 30\text{ mV}$: Highly stable suspension; strong electrostatic repulsion prevents particle contact.
  - $|\zeta| = 15 - 30\text{ mV}$: Moderately stable; slow aggregation.
  - $|\zeta| < 5 - 10\text{ mV}$: Destabilized suspension (rapid coagulation zone). Particle collisions successfully overcome repulsive forces.
- **Streaming Current Detectors (SCD)**: On-line automated industrial instruments that measure the streaming current generated by fluid shear driving mobile counter-ions past colloidal particles temporarily adsorbed onto the reciprocating piston and cylinder walls of a sample chamber. SCD outputs provide real-time feedback control for automatic chemical coagulant dosing pumps.

##### 3.2.2.3 DLVO Colloidal Stability Theory & Net Interaction Energy
###### Van der Waals Attractive Potential Derivation & Hamaker Constant
The **DLVO Theory** (named after Derjaguin, Landau, Verwey, and Overbeek) describes colloidal stability as the quantitative summation of attractive long-range van der Waals dispersion forces and repulsive electrostatic double-layer forces as two identical spherical colloidal particles approach each other:
$$V_{\text{total}}(d) = V_A(d) + V_R(d)$$
The attractive potential energy ($V_A$) arises from permanent dipole, induced dipole, and instantaneous quantum dispersion interactions (London-van der Waals forces). For two spherical particles of radius $a$ separated by surface-to-surface distance $d$ (where $d \ll a$), the attractive potential is expressed as:
$$V_A(d) = -\frac{A_{121} \cdot a}{12 d}$$
where $A_{121}$ is the composite **Hamaker constant** for particles of material 1 interacting across aqueous medium 2 (typically $10^{-20}$ to $10^{-19}\text{ J}$). Van der Waals attraction is always negative (attractive), depends primarily on particle composition and density, and is relatively insensitive to electrolyte concentration or solution ionic strength.

###### Electrostatic Double-Layer Repulsion Potential Energy
As two identically charged colloidal particles approach within their respective Debye lengths ($d < 2\kappa^{-1}$), their diffuse ion atmospheres overlap. This overlap increases the local counter-ion concentration between the particles, creating an osmotic pressure gradient that draws solvent into the gap and pushes the particles apart. The electrostatic repulsive potential energy ($V_R$) for constant surface potential conditions is given by:
$$V_R(d) = 2\pi \varepsilon_r \varepsilon_0 a \psi_0^2 \ln[1 + \exp(-\kappa d)]$$
Electrostatic repulsion is positive, decays exponentially with separation distance $d$, and is highly sensitive to counter-ion concentration and ionic valence via the Debye parameter $\kappa$.

###### Total Interaction Energy Profile (Primary Maximum Barrier, Primary & Secondary Minima)
Plotting the total net interaction energy $V_{\text{total}}$ against interparticle separation distance $d$ produces a characteristic classical energy curve featuring four distinct thermodynamic regimes:
1. **Primary Minimum ($d \rightarrow 0$, Born Contact)**: At extremely small interparticle distances (atomic contact, $d < 0.2 - 0.4\text{ nm}$), attractive van der Waals forces dominate infinitely ($V_A \propto -1/d$). Particles falling into this deep thermodynamic potential well adhere irreversibly in permanent coagulated contact.
2. **Primary Repulsion Energy Barrier ($V_{\text{max}}$)**: At intermediate distances ($d \approx 1 - 5\text{ nm}$), the exponential decay of electrostatic repulsion outstrips van der Waals attraction, producing a positive energy peak ($V_{\text{max}}$). If $V_{\text{max}} \gg k_B T$ (thermal kinetic energy, where $k_B T \approx 4.14 \times 10^{-21}\text{ J}$ at $25^\circ\text{C}$), colliding particles lack sufficient kinetic energy to overcome the barrier, and bounce apart elastically—maintaining colloidal suspension stability.
3. **Secondary Minimum ($d \approx 5 - 20\text{ nm}$)**: At larger separation distances, because exponential repulsion decays faster than inverse-power attraction, a shallow secondary attractive well frequently forms ($V_{\text{sec}} \approx -1\text{ to }-5\text{ }k_B T$). Particles trapped here form loose, easily redispersible flocs.
4. **Destabilization Criterion**: Chemical coagulation destabilizes the suspension by either suppressing $V_{\text{max}}$ to $< 0$ (allowing direct capture into the primary minimum) or depressing $V_{\text{max}}$ so that thermal and hydrodynamic collision energies easily surmount the barrier.

#### 3.2.3 Four Primary Suspension Destabilization Mechanisms

##### 3.2.3.1 Electrical Double Layer Compression & Schulze-Hardy Rule
###### Diffuse Layer Compression Physics & Critical Coagulation Concentration (CCC)
When indifferent (non-adsorbing) electrolytes are introduced into a colloidal suspension, the ionic strength of the aqueous phase increases ($I = \frac{1}{2} \sum C_i z_i^2$). In response, counter-ions crowd closer to the particle surface to screen the negative charge, increasing $\kappa$ and dramatically compressing the diffuse layer thickness $\kappa^{-1}$. As the diffuse layer contracts, the range of electrostatic repulsion diminishes, allowing attractive van der Waals forces to dominate at larger interparticle separations until the primary energy barrier $V_{\text{max}}$ collapses to zero.
The minimum electrolyte concentration required to induce rapid coagulation is termed the **Critical Coagulation Concentration (CCC)**. According to DLVO theory, the condition for barrier elimination ($V_{\text{total}} = 0$ and $dV_{\text{total}}/dd = 0$) leads directly to the **Schulze-Hardy Rule** (`eq_ch03_006`):

$$\text{CCC} \propto \frac{1}{z^6}$$

**Plain Text Formulation:** `CCC ~ 1 / z^6`

**Description:** States that the critical coagulant concentration required for colloidal destabilization via double-layer compression is inversely proportional to the sixth power of the counter-ion valence $z$.

**Key Variables & Engineering Units:**
- $\text{CCC}$: Critical coagulant concentration ($\text{mol/L}$ or $\text{mmol/L}$)
- $z$: Ionic valence of the coagulant counter-ion (e.g., $z=1$ for $\text{Na}^+$, $z=2$ for $\text{Ca}^{2+}$, $z=3$ for $\text{Al}^{3+}$ or $\text{Fe}^{3+}$)

###### Valence Scaling Laws: Na+ vs Ca2+ vs Al3+ Molar Ratios (100 : 1.6 : 0.14)
Applying the $z^{-6}$ power relationship demonstrates the dramatic surge in coagulating effectiveness with increasing counter-ion valence:
$$\text{CCC}_{\text{monovalent}} : \text{CCC}_{\text{divalent}} : \text{CCC}_{\text{trivalent}} \propto \left(\frac{1}{1^6}\right) : \left(\frac{1}{2^6}\right) : \left(\frac{1}{3^6}\right) = 1 : \frac{1}{64} : \frac{1}{729} \approx 100 : 1.56 : 0.137$$
- **Monovalent Counter-ions ($\text{Na}^+$, $\text{K}^+$)**: Require very high molar concentrations ($\,\sim 50 - 100\text{ mM}$) to destabilize clays, making salt addition impractical for municipal drinking water.
- **Divalent Counter-ions ($\text{Ca}^{2+}$, $\text{Mg}^{2+}$)**: Require concentrations of $1.0 - 2.0\text{ mM}$ ($40 - 80\text{ mg/L}$ as $\text{Ca}^{2+}$).
- **Trivalent Counter-ions ($\text{Al}^{3+}$, $\text{Fe}^{3+}$)**: Destabilize suspensions at minute concentrations ($0.05 - 0.2\text{ mM}$, equivalent to $1 - 5\text{ mg/L}$ of metal ion), confirming why aluminum and iron salts serve as universal coagulants.
Double layer compression exhibits no chemical overdosing restabilization: once compressed, additional indifferent salt cannot re-expand the diffuse layer.

##### 3.2.3.2 Adsorption and Charge Neutralization
###### Specific Adsorption of Polyvalent Cationic Hydrolysis Species
Unlike indifferent electrolytes that remain in the diffuse layer, hydrolyzed metal species ($[\text{Al}_2(\text{OH})_2]^{4+}$, $[\text{Al}_3(\text{OH})_4]^{5+}$, $[\text{Al}_{13}\text{O}_4(\text{OH})_{24}]^{7+}$, $[\text{Fe}_2(\text{OH})_2]^{4+}$) and synthetic cationic polymers adsorb specifically into the Stern layer through coordinate bonding with deprotonated particle surface sites. Because their charge density is exceptionally high, specific adsorption directly reduces the surface potential $\psi_0$ and brings the zeta potential $\zeta$ to zero.

###### Stoichiometric Dosing Proportionality & Colloid Surface Charge Titration
Charge neutralization exhibits strict stoichiometric proportionality:
- The optimal coagulant dosage is directly proportional to the total colloidal surface area concentration (turbidity and NOM concentration).
- Unlike sweep flocculation, charge neutralization occurs at coagulant concentrations below the solubility limit of amorphous metal hydroxides (acidic to slightly neutral pH, $\text{pH } 4.5 - 6.5$ for alum, $\text{pH } 4.0 - 5.5$ for ferric).
- **Overdosing Hazard (Restabilization)**: If an excessive coagulant dose is applied, adsorption continues beyond the point of zero charge (isoelectric point). The particle surface acquires a net positive charge ($\zeta > +15\text{ to }+30\text{ mV}$), generating renewed electrostatic repulsion that restabilizes the colloidal suspension (Zone S3).

##### 3.2.3.3 Enmeshment in Precipitate (Sweep Flocculation)
###### Metal Hydroxide Precipitation Thermodynamics & Supersaturation Kinetics
When aluminum or iron coagulants are added in quantities exceeding the solubility limit of amorphous metal hydroxide (typically at $\text{pH } 6.5 - 8.0$ for alum, $\text{pH } 5.5 - 9.0$ for ferric), the solution becomes heavily supersaturated ($S = [\text{Me}^{3+}][\text{OH}^-]^3 / K_{sp} \gg 10^3$). Within $0.1 - 1.0\text{ seconds}$, amorphous $\text{Al}(\text{OH})_3(\text{s})$ or $\text{Fe}(\text{OH})_3(\text{s})$ precipitates out as an expansive, sticky, three-dimensional gelatinous network.

###### Low-Turbidity Water Treatment via Massive Hydroxide Floc Enmeshment
As this massive hydroxide precipitate forms and settles through the water column, it physically collides with, captures, and enmeshes colloidal particles, organic molecules, and bacteria within its matrix—a mechanism termed **Sweep Flocculation (Keo tụ quét / Cuốn trôi bông cặn)**:
- **Inverse Turbidity-Dosage Relationship**: In low-turbidity raw waters ($< 5 - 10\text{ NTU}$), particle collision frequency is naturally insufficient for charge neutralization. To achieve clarification, high coagulant doses ($30 - 60\text{ mg/L}$ alum) must be dosed to create artificial solids volume, generating dense hydroxide flocs that physically sweep the water clear.
- **No Restabilization**: Sweep coagulation cannot be overdosed in terms of charge restabilization; excess coagulant merely produces additional hydroxide sludge.
- Sweep flocculation is the dominant operating mechanism in $> 80\%$ of municipal surface water treatment plants worldwide.

##### 3.2.3.4 Interparticle Polymer Bridging
###### High-Molecular-Weight Synthetic Polyelectrolyte Attachment & Loop-Tail Conformations
**Interparticle Polymer Bridging (Tạo cầu nối polyme)** occurs when long-chain synthetic or natural polymers ($MW = 10^6 - 2 \times 10^7\text{ Da}$, extended chain lengths $1 - 10\text{ }\mu\text{m}$) are added to a colloidal suspension. The flexible macromolecular chain adsorbs onto the surface of a colloidal particle at one or more points (trains), while loops and tails extend far out into the bulk aqueous phase beyond the electrical double layer. When these extended polymer tails collide with unoccupied adsorption sites on neighboring colloidal particles, stable multi-particle polymer bridges are established.

###### Optimum Polymer Surface Coverage (theta ≈ 0.5) & Restabilization Mechanisms
The kinetics of polymer bridging are governed by the fraction of particle surface area covered by polymer segments ($\theta$):
- **Maximum Flocculation Rate ($\theta \approx 0.5$)**: La Mer's bridging theory proves that optimal aggregation occurs when exactly half of the available surface sites are covered by polymer segments ($\theta = 0.5$). Under this condition, the probability of an extended loop finding an open site on a colliding particle is maximized: $P_{\text{collision}} \propto \theta (1 - \theta)$.
- **Steric Restabilization (Overdosing, $\theta \rightarrow 1.0$)**: When polymer is overdosed, all particle surface sites become completely saturated by polymer segments ($\theta \approx 1.0$). No open adsorption sites remain on adjacent particles for loop attachment. Furthermore, the overlapping hydrophilic polymer brush layers create powerful steric repulsion, permanently restabilizing the suspension.
- **Shear Rupture**: High fluid shear rates ($G > 100\text{ s}^{-1}$) can mechanically tear covalent polymer backbones, irreversibly degrading bridging networks.

#### 3.2.4 Bench-Scale Jar Testing & Coagulation Regimes (Zones S1 to S4)

##### 3.2.4.1 Standardized 6-Gang Jar Testing Experimental Methodology
###### Apparatus Configuration & Hydrodynamic B-Ker2 Geometry
Because surface water quality (turbidity, pH, alkalinity, temperature, NOM) exhibits dynamic seasonal and storm-induced fluctuations, the optimal coagulant type, dosage, and operating pH cannot be calculated from theoretical equations alone. They must be determined empirically using the **Standard 6-Jar Laboratory Batch Testing Apparatus (Thí nghiệm Jar-test)**:
- **Apparatus Layout**: Consists of six synchronized flat paddle agitators driven by a continuously variable digital motor ($0 - 300\text{ rpm}$) over an illuminated base.
- **Jar Geometry**: Utilizes 2.0-liter square acrylic containers (Phipps & Bird B-Ker2). The square geometry disrupts radial liquid swirl, serving as internal anti-vortex baffles without the high localized shear of metal wall baffles. Sample ports are positioned exactly $10\text{ cm}$ below the liquid surface ($2\text{ cm}$ below the working liquid level during settling).

###### Step-by-Step AWWA Jar Test Optimization Procedure
The standardized AWWA jar test optimization procedure is executed across two sequential testing phases:
##### Quy trình: Bench-Scale Jar Test Optimization Procedure for Coagulant Type and Dosage
1. **Raw Water Baseline Profiling**: Collect representative raw water and measure baseline parameters: turbidity (NTU), true color (TCU), pH, temperature ($^\circ\text{C}$), Total Alkalinity ($\text{mg/L}$ as $\text{CaCO}_3$), and $UV_{254}$ absorbance ($\,\text{cm}^{-1}$).
2. **Reactor Charging**: Fill six 2.0-liter square B-Ker2 jars with exactly $2.0\text{ L}$ of raw water. Place jars onto the gang-stirrer station.
3. **Phase 1: pH Optimization at Fixed Coagulant Dose**:
   - Program rapid flash mix agitation: $N = 100 - 150\text{ rpm}$ ($G \approx 300 - 400\text{ s}^{-1}$).
   - Set a constant coagulant dose across all jars (e.g., $20\text{ mg/L}$ commercial alum).
   - Adjust jar pH across a systematic spectrum (e.g., pH 5.0, 5.5, 6.0, 6.5, 7.0, 7.5) using pre-titrated dilute $0.1\text{ N }\text{H}_2\text{SO}_4$ or $0.1\text{ N }\text{NaOH}$.
   - Rapid mix for $t_{\text{rapid}} = 60\text{ seconds}$.
   - Reduce agitator speed to slow mix flocculation: $N = 30\text{ rpm}$ ($G \approx 30 - 40\text{ s}^{-1}$) for $t_{\text{floc}} = 20\text{ minutes}$. Record the time of first visible floc formation (pinpoint flocs).
   - Stop agitators and allow quiescent settling for $t_{\text{settle}} = 30\text{ minutes}$.
   - Withdraw supernatant samples from sampling ports ($2\text{ cm}$ depth) and analyze residual turbidity, finished pH, residual metal ion concentration, and $UV_{254}$. Identify the **optimal operating pH** that minimizes residual turbidity and dissolved metal residual.
4. **Phase 2: Coagulant Dosage Titration at Optimal pH**:
   - Refill six jars with fresh raw water and adjust all jars to the optimal pH established in Phase 1.
   - Apply an incremental coagulant dosage gradient across the six jars (e.g., 5, 10, 20, 30, 40, $50\text{ mg/L}$ alum).
   - Repeat the standardized cycle: rapid mix ($120\text{ rpm}$, $1\text{ min}$), slow mix flocculation ($30\text{ rpm}$, $20\text{ min}$), and settling ($30\text{ min}$).
   - Measure residual turbidity versus dosage. Plot the **coagulation performance curve** and locate the critical transition points between operating Zones S1 through S4. Select the design coagulant dose at the inflection knee yielding clarified turbidity $< 1.0 - 2.0\text{ NTU}$.

##### 3.2.4.2 Coagulation Operating Domains: Zones S1 through S4
By plotting residual supernatant turbidity against coagulant dosage across varying colloidal particle surface area concentrations, four distinct operational zones emerge:
###### Zone S1: Low Particle Surface Area / Insufficient Coagulant (Underdosing)
Occurs at low coagulant dosages. The mass concentration of hydrolyzed metal species is insufficient to compress the electrical double layer or neutralize colloidal surface charges ($|\zeta| > 20\text{ mV}$). Colloid collisions remain elastically repulsive, and residual turbidity remains virtually unchanged from initial raw water values.

###### Zone S2: Optimal Charge Neutralization Window
As coagulant dosage increases, stoichiometric adsorption of cationic hydroxy-metal species neutralizes colloidal surface negative charges, depressing zeta potential into the critical destabilization corridor ($\zeta = -5\text{ to }+5\text{ mV}$). Particle collisions result in rapid aggregation, causing residual turbidity to plunge to minimum levels ($< 1.0 - 2.0\text{ NTU}$). Flocs are small, compact, and settle readily.

###### Zone S3: Charge Reversal & Steric / Electrostatic Restabilization
When coagulant dosing exceeds the stoichiometric requirement for charge neutralization in waters of low to moderate colloidal solids, excess cationic metal species continue adsorbing onto particle surfaces. The zeta potential reverses sign and becomes strongly positive ($\zeta > +15\text{ to }+30\text{ mV}$). Restabilized, positively charged colloidal particles repel each other electrostatically, causing supernatant turbidity to rise sharply. This manifests operationally as cloudy, pinpoint haze that refuses to settle.

###### Zone S4: Sweep Coagulation / Hydroxide Precipitation Domain
At elevated coagulant dosages, the solubility product of the amorphous metal hydroxide is drastically exceeded. Insoluble $\text{Al}(\text{OH})_3(\text{s})$ or $\text{Fe}(\text{OH})_3(\text{s})$ precipitates rapidly in bulk solution, overcoming positive charge restabilization by physically enmeshing and sweeping the restabilized colloids out of suspension. Supernatant turbidity drops to minimal levels, accompanied by high volumetric sludge production.

##### 3.2.4.3 Hydroxide Solubility Equilibrium & Master Stability Diagrams
###### Aluminum Hydroxide Al(OH)3(s) Amphoteric Solubility vs pH
Aluminum hydroxide is an amphoteric solid whose aqueous solubility is highly sensitive to solution pH. The chemical equilibrium system at $25^\circ\text{C}$ is defined by five simultaneous mononuclear species in equilibrium with amorphous $\text{Al}(\text{OH})_3(\text{s})$:
1. $\text{Al}(\text{OH})_3(\text{s}) \rightleftharpoons \text{Al}^{3+} + 3\text{OH}^- \quad (\log K_{s0} = -31.5\text{ to }-32.5)$
2. $\text{Al}(\text{OH})_3(\text{s}) \rightleftharpoons \text{Al}(\text{OH})^{2+} + 2\text{OH}^- \quad (\log K_{s1} = -23.0)$
3. $\text{Al}(\text{OH})_3(\text{s}) \rightleftharpoons \text{Al}(\text{OH})_2^+ + \text{OH}^- \quad (\log K_{s2} = -14.5)$
4. $\text{Al}(\text{OH})_3(\text{s}) + \text{H}_2\text{O} \rightleftharpoons \text{Al}(\text{OH})_4^- + \text{H}^+ \quad (\log K_{s4} = -12.3)$
Plotting total dissolved aluminum $[\text{Al}_{\text{total}}] = [\text{Al}^{3+}] + [\text{Al}(\text{OH})^{2+}] + [\text{Al}(\text{OH})_2^+] + [\text{Al}(\text{OH})_4^-]$ produces a classic parabolic solubility curve:
- **Acidic Regime (pH < 5.5)**: Cationic species $\text{Al}^{3+}$, $\text{Al}(\text{OH})^{2+}$, and polynuclear complexes dominate. Solubility increases rapidly with decreasing pH ($[\text{Al}^{3+}] \propto [\text{H}^+]^3$). Operating here risks high residual soluble aluminum in finished water ($> 0.2\text{ mg/L}$), violating health regulations.
- **Minimum Solubility Window (pH 6.0 – 7.5)**: Total dissolved aluminum reaches an absolute thermodynamic minimum of $< 0.05\text{ mg/L}$ ($< 2 \times 10^{-6}\text{ M}$) at $\text{pH } 6.2 - 6.8$. This represents the **optimal operating envelope for alum coagulation**.
- **Alkaline Regime (pH > 8.0)**: Insoluble hydroxide dissolves into the anionic aluminate monomer $[\text{Al}(\text{OH})_4]^-$. Aluminate carries negative charge, destroying sweep floc formation and releasing dissolved aluminum.

###### Ferric Hydroxide Fe(OH)3(s) Solubility vs pH
Amorphous ferric hydroxide [$\text{Fe}(\text{OH})_3(\text{s})$, $\log K_{s0} \approx -38.5$] is orders of magnitude less soluble than aluminum hydroxide:
- The minimum solubility window spans a broad neutral-to-alkaline band: $\text{pH } 5.0 - 9.0$.
- Insoluble $\text{Fe}(\text{OH})_3$ flocs form efficiently down to $\text{pH } 4.0$ and remain stable up to $\text{pH } 11.0$, making ferric iron salts vastly superior for treating low-pH or highly alkaline raw waters where alum fails.

###### Master Operational Envelopes: Coagulant Concentration vs pH Matrix
Combining equilibrium solubility chemistry with colloidal surface area concentrations establishes the master coagulation operational diagram:
- **Low Coagulant Concentration ($< 10^{-4}\text{ M}$), Acidic pH ($4.5 - 6.0$)**: Dominated by Adsorption and Charge Neutralization.
- **High Coagulant Concentration ($> 10^{-4}\text{ M}$), Circumneutral pH ($6.5 - 8.0$)**: Dominated by Sweep Flocculation.
- **High Coagulant Concentration, Low Colloid Surface Area, pH 5.0–6.0**: High vulnerability to Restabilization (Zone S3).

#### 3.2.5 Inorganic Coagulant Chemistry & Synthetic Polyelectrolytes

##### 3.2.5.1 Commercial Aluminum Sulfate (Alum) Chemistry & Alkalinity Depletion
###### Alum Hydrolysis Stoichiometry & Carbon Dioxide Liberation
Commercial dry alum is manufactured as hydrated aluminum sulfate crystals approximating the chemical formula $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ (molecular weight $MW = 594.36\text{ g/mol}$). When dissolved into water containing natural calcium bicarbonate alkalinity, alum hydrolyzes according to the fundamental stoichiometry (`eq_ch03_001`):

$$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 6\text{HCO}_3^- \rightarrow 2\text{Al}(\text{OH})_3\downarrow + 3\text{SO}_4^{2-} + 6\text{CO}_2\uparrow + 14\text{H}_2\text{O}$$

**Plain Text Formulation:** `Al2(SO4)3.14H2O + 6HCO3- -> 2Al(OH)3 + 3SO4(2-) + 6CO2 + 14H2O`

**Description:** Governs the primary hydrolysis and precipitation reaction of commercial aluminum sulfate with natural bicarbonate alkalinity, forming insoluble amorphous aluminum hydroxide flocs and releasing dissolved carbon dioxide gas.

**Key Variables & Chemical Equivalence:**
- $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$: Commercial alum ($MW = 594.36\text{ g/mol}$, active content $\approx 17.1\%\text{ Al}_2\text{O}_3$ by weight)
- $\text{HCO}_3^-$: Natural bicarbonate alkalinity ion ($MW = 61.02\text{ g/mol}$)
- $\text{Al}(\text{OH})_3$: Insoluble amorphous aluminum hydroxide precipitate ($MW = 78.00\text{ g/mol}$)
- $\text{CO}_2$: Dissolved carbon dioxide gas generated ($MW = 44.01\text{ g/mol}$), which depresses water pH unless degassed.

###### Theoretical Alkalinity Consumption Calculation
Each mole of alum added consumes exactly six moles of bicarbonate ion, which is equivalent to three moles of calcium carbonate ($\text{CaCO}_3$). The theoretical alkalinity consumption is calculated via `eq_ch03_002`:

$$\Delta\text{Alk}_{\text{alum}} = \text{Dose}_{\text{alum}} \times \left( \frac{6 \times 50.045\text{ g/eq CaCO}_3}{594.36\text{ g/mol alum}} \right) \approx 0.5052 \times \text{Dose}_{\text{alum}}$$

**Plain Text Formulation:** `Delta_Alk_alum = Dose_alum * (6 * 50.045 / 594.36) = 0.5052 * Dose_alum (mg/L as CaCO3)`

**Description:** Evaluates the stoichiometric reduction in bicarbonate alkalinity (expressed as $\text{mg/L as }\text{CaCO}_3$) resulting from commercial alum dosage. Exactly **$1.0\text{ mg/L}$ of commercial alum consumes $0.5052\text{ mg/L}$ of natural alkalinity as $\text{CaCO}_3$**.

###### Supplemental Hydrated Lime / Quicklime / Soda Ash Neutralization
If the natural raw water alkalinity is insufficient to buffer this chemical consumption, water pH will drop steeply into the acidic regime ($< 5.5$), quenching hydroxide precipitation and causing high residual soluble aluminum. Under such conditions, supplemental alkalinity must be fed simultaneously:
1. **Hydrated Lime [$\text{Ca}(\text{OH})_2$] Reaction** (`eq_ch03_005`):
$$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{Ca}(\text{OH})_2 \rightarrow 2\text{Al}(\text{OH})_3\downarrow + 3\text{CaSO}_4 + 14\text{H}_2\text{O}$$
Stoichiometric consumption:
$$\text{Ratio}_{\text{lime/alum}} = \frac{3 \times 74.09\text{ g/mol Ca(OH)}_2}{594.36\text{ g/mol alum}} = 0.3740\text{ mg pure Ca(OH)}_2\text{ / mg alum}$$
Accounting for commercial hydrated lime purity (typically $90\%$):
$$\text{Commercial Hydrated Lime Dose} = \frac{0.3740}{0.90} = 0.4155\text{ mg lime / mg alum}$$
2. **Quicklime [$\text{CaO}$] Reaction**:
$$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{CaO} \rightarrow 2\text{Al}(\text{OH})_3\downarrow + 3\text{CaSO}_4 + 11\text{H}_2\text{O}$$
Stoichiometric consumption: $3 \times 56.08 / 594.36 = 0.2831\text{ mg pure CaO / mg alum}$ ($0.315\text{ mg commercial CaO / mg alum}$ at $90\%$ purity).
3. **Soda Ash [$\text{Na}_2\text{CO}_3$] Reaction**:
$$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{Na}_2\text{CO}_3 + 3\text{H}_2\text{O} \rightarrow 2\text{Al}(\text{OH})_3\downarrow + 3\text{Na}_2\text{SO}_4 + 3\text{CO}_2 + 14\text{H}_2\text{O}$$
Stoichiometric ratio: $3 \times 105.99 / 594.36 = 0.5350\text{ mg pure Na}_2\text{CO}_3\text{ / mg alum}$. Soda ash provides alkalinity without adding calcium hardness.

##### Quy trình: Alum and Lime Coagulant Stoichiometric Sizing Procedure
1. **Raw Water Characterization**: Measure design plant flow rate $Q$ ($\text{m}^3/\text{d}$, $\text{m}^3/\text{s}$), raw turbidity, raw pH, and baseline Total Alkalinity $\text{Alk}_{\text{raw}}$ ($\text{mg/L as }\text{CaCO}_3$).
2. **Determine Optimal Alum Dose**: Obtain optimal commercial alum dose $\text{Dose}_{\text{alum}}$ ($\text{mg/L}$) and target operating pH from jar test results.
3. **Calculate Alkalinity Consumed**: Compute stoichiometric alkalinity depletion:
   $$\Delta\text{Alk}_{\text{alum}} = 0.5052 \times \text{Dose}_{\text{alum}} \quad (\text{mg/L as }\text{CaCO}_3)$$
4. **Evaluate Residual Alkalinity**: Compute expected residual alkalinity:
   $$\text{Alk}_{\text{residual}} = \text{Alk}_{\text{raw}} - \Delta\text{Alk}_{\text{alum}}$$
   Check against the minimum operational buffering criterion: $\text{Alk}_{\text{residual}} \ge 20 - 30\text{ mg/L as }\text{CaCO}_3$.
5. **Determine Alkalinity Deficit**: If $\text{Alk}_{\text{residual}} < 20\text{ mg/L}$, calculate the deficit:
   $$\text{Alk}_{\text{deficit}} = 20 - \text{Alk}_{\text{residual}} \quad (\text{mg/L as }\text{CaCO}_3)$$
6. **Calculate Supplemental Chemical Dose**:
   - Hydrated Lime ($90\%$ purity): $\text{Dose}_{\text{lime}} = \text{Alk}_{\text{deficit}} \times \left(\frac{74.09}{100.09}\right) / 0.90 = 0.822 \times \text{Alk}_{\text{deficit}}$ ($\text{mg/L}$).
   - Quicklime ($90\%$ purity): $\text{Dose}_{\text{quicklime}} = \text{Alk}_{\text{deficit}} \times \left(\frac{56.08}{100.09}\right) / 0.90 = 0.623 \times \text{Alk}_{\text{deficit}}$ ($\text{mg/L}$).
   - Soda Ash ($99\%$ purity): $\text{Dose}_{\text{soda}} = \text{Alk}_{\text{deficit}} \times \left(\frac{105.99}{100.09}\right) / 0.99 = 1.070 \times \text{Alk}_{\text{deficit}}$ ($\text{mg/L}$).

##### 3.2.5.2 Ferric Chloride & Iron-Based Coagulants
###### Ferric Chloride Hexahydrate Hydrolysis Stoichiometry
Ferric chloride hexahydrate ($\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$, $MW = 270.30\text{ g/mol}$) or anhydrous ferric chloride ($\text{FeCl}_3$, $MW = 162.20\text{ g/mol}$) dissociates completely in water, undergoing rapid hydrolysis (`eq_ch03_003`):

$$\text{FeCl}_3 \cdot 6\text{H}_2\text{O} + 3\text{HCO}_3^- \rightarrow \text{Fe}(\text{OH})_3\downarrow + 3\text{CO}_2\uparrow + 6\text{H}_2\text{O} + 3\text{Cl}^-$$

**Plain Text Formulation:** `FeCl3.6H2O + 3HCO3- -> Fe(OH)3 + 3CO2 + 6H2O + 3Cl-`

**Description:** Governs the precipitation of insoluble ferric hydroxide flocs across a broad pH spectrum, releasing dissolved carbon dioxide and chloride ions.

###### Ferric Chloride Alkalinity Demand Formulation
The stoichiometric alkalinity consumption per unit mass of anhydrous $\text{FeCl}_3$ is calculated via `eq_ch03_004`:

$$\Delta\text{Alk}_{\text{FeCl}_3} = \text{Dose}_{\text{FeCl}_3} \times \left( \frac{3 \times 50.045\text{ g/eq CaCO}_3}{162.20\text{ g/mol anhydrous FeCl}_3} \right) \approx 0.9256 \times \text{Dose}_{\text{FeCl}_3}$$

**Plain Text Formulation:** `Delta_Alk_FeCl3 = Dose_FeCl3 * (3 * 50.045 / 162.20) = 0.9256 * Dose_FeCl3 (mg/L as CaCO3)`

**Description:** Exactly **$1.0\text{ mg/L}$ of anhydrous $\text{FeCl}_3$ consumes $0.9256\text{ mg/L}$ of alkalinity as $\text{CaCO}_3$** (or **$0.5554\text{ mg/L as }\text{CaCO}_3$ per $\text{mg/L}$ of crystal $\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$**).

###### Ferrous Sulfate Oxidation Kinetics & Broad pH Operating Regimes
- **Ferrous Sulfate (Copperas, $\text{FeSO}_4 \cdot 7\text{H}_2\text{O}$)**: Divalent iron ($\text{Fe}^{2+}$) does not precipitate efficiently below $\text{pH } 8.5 - 9.0$. In municipal treatment, ferrous sulfate is chlorinated ahead of injection (Chlorinated Copperas):
  $$3\text{FeSO}_4 + 1.5\text{Cl}_2 \rightarrow \text{Fe}_2(\text{SO}_4)_3 + \text{FeCl}_3$$
  producing an active ferric mixture effective across $\text{pH } 4.0 - 11.0$.
- **Advantages of Iron Coagulants Over Alum**:
  1. Denser, faster-settling flocs ($v_s$ up to $2 - 3\times$ that of alum flocs).
  2. Broader effective pH range ($\,\text{pH } 4.0 - 11.0$ versus $5.5 - 7.5$ for alum).
  3. Superior performance in cold water ($< 5^\circ\text{C}$).
  4. Excellent removal of arsenic, selenium, and hydrogen sulfide.
- **Disadvantages**: Corrosive solutions requiring rubber/FRP lined tanks; risks staining finished water red/brown if dissolved iron penetrates filtration ($> 0.3\text{ mg/L}$).

##### 3.2.5.3 Prehydrolyzed Inorganic Coagulants: Polyaluminum Chloride (PAC)
###### Polymeric Speciation ([Al13O4(OH)24(H2O)12]7+ Keggin Ion) & Basicity Ratios
**Polyaluminum Chloride (PAC, Phèn nhôm polyme)** represents a class of pre-polymerized inorganic coagulants formulated with the general empirical formula $[\text{Al}_n(\text{OH})_m\text{Cl}_{3n-m}]_k$. PAC is manufactured by reacting aluminum chloride or alumina with controlled amounts of base:
- **Basicity Ratio ($B$)**: Defined as $B = [\text{OH}] / (3[\text{Al}]) \times 100\%$. Commercial PAC basicities range from $40\%$ to $85\%$.
- **Keggin Ion Predominance**: High-basicity PAC ($B \ge 70\%$) is heavily enriched in the pre-formed stable tridecameric Keggin cation $[\text{Al}_{13}\text{O}_4(\text{OH})_{24}(\text{H}_2\text{O})_{12}]^{7+}$ (designated $\text{Al}_{13}$). The $\text{Al}_{13}$ macromolecule possesses a rigid tetrahedral $\text{AlO}_4$ core surrounded by 12 octahedral $\text{AlO}_6$ units, delivering an exceptionally high charge density of $+7$.

###### Comparative Advantages: Alkalinity Conservation, Low-Temperature Kinetics & Dense Sludge
Because PAC is partially neutralized during factory synthesis:
1. **Minimal Alkalinity Depletion**: Consumes only $30\%$ to $50\%$ of the alkalinity consumed by commercial alum per unit mass of aluminum, preventing severe pH depression and eliminating supplemental lime dosing in soft waters.
2. **Rapid Hydrolysis in Cold Water**: Because the active polymer cations are pre-formed, PAC performance is virtually independent of water temperature, excelling during freezing winter conditions where alum hydrolysis kinetics freeze.
3. **Dense Floc Morphology & Reduced Sludge Volume**: Precipitates as compact, low-water-content flocs, reducing dry sludge mass by $20 - 40\%$ and significantly improving dewaterability on belt presses and drying beds.

##### 3.2.5.4 Synthetic Polyelectrolytes & Polymer Coagulant Aids
###### Classification: Cationic, Anionic, and Non-ionic Polymer Backbones
Synthetic polymers (polyelectrolytes) are high-molecular-weight water-soluble organic macromolecules classified by their ionic charge in aqueous solution (Table `tbl_ch03_02`):
1. **Cationic Polymers**: Carry positive quaternary ammonium [$-\text{R}_4\text{N}^+$] or tertiary amine groups. Possess moderate molecular weights ($MW = 10^5 - 10^6\text{ Da}$). Primarily operate by adsorption and charge neutralization.
2. **Anionic Polymers**: Polyacrylamide derivatives copolymerized with sodium acrylate, carrying negative carboxylate [$-\text{COO}^-$] groups. Possess very high molecular weights ($MW = 5 \times 10^6 - 2 \times 10^7\text{ Da}$). Operate strictly via interparticle polymer bridging.
3. **Non-ionic Polymers**: Pure polyacrylamide [$-(\text{CH}_2\text{-CHCONH}_2)_n-$], carrying uncharged, highly hydrophilic amide groups. Operate via hydrogen bonding and polymer bridging.

| No. | Coagulant Chemical | Chemical Formula / Classification | Effective pH Window | Stoichiometric Alkalinity Consumption | Primary Operational Characteristics & Application Niche |
|---|---|---|---|---|---|
| 1 | Commercial Aluminum Sulfate (Alum) | $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ | $5.5 - 7.5$ (Sweep: $6.5 - 7.5$) | $0.5052\text{ mg/L as }\text{CaCO}_3\text{ per mg/L alum}$ | Universal primary coagulant; highly cost-effective; requires careful pH buffering; sensitive to cold temperatures. |
| 2 | Aluminum Chloride | $\text{AlCl}_3$ | $5.5 - 7.5$ | High (releases 3 $\text{HCl}$ equivalents) | Concentrated liquid chemical dosing; specialized industrial systems; highly corrosive. |
| 3 | Ferric Chloride Hexahydrate | $\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$ | $4.0 - 11.0$ (Sweep: $5.0 - 8.5$) | $0.5554\text{ mg/L as }\text{CaCO}_3\text{ per mg/L crystal}$ ($0.9256\text{ per mg/L anhydrous}$) | Forms dense, heavy, rapid-settling flocs; broad operating pH envelope; excels in cold water and organics removal. |
| 4 | Polyaluminum Chloride (PAC) | $[\text{Al}_n(\text{OH})_m\text{Cl}_{3n-m}]_k$ | $5.5 - 9.0$ | Low ($0.15 - 0.25\text{ mg/L as }\text{CaCO}_3\text{ per mg/L}$) | Pre-polymerized $\text{Al}_{13}$ Keggin ions; minimal pH drop; rapid cold-water flocculation; reduced sludge volume. |
| 5 | Synthetic Polyelectrolytes | Cationic, Anionic, Non-ionic Polymers | $4.0 - 10.0$ | Zero alkalinity consumption | High-molecular-weight bridge builders; produce giant shear-resistant macro-flocs; effective at minute dosages. |

###### Primary Coagulant, Coagulant Aid, and Filter Aid Dosing Protocols
Polymers serve three distinct engineering functions across the water treatment train:
- **Primary Coagulant (Cationic)**: Applied alone at dosages of $1.0 - 5.0\text{ mg/L}$ (or at $0.1 - 0.5\text{ mg/L}$ in combination with metal salts). Injected into the rapid flash mixer to neutralize colloidal negative charge, eliminate metal sludge, and enhance dissolved organic carbon (DOC) removal.
- **Coagulant Aid (Anionic or Non-ionic)**: Applied at dosages of $0.05 - 0.2\text{ mg/L}$ (up to $1.0 - 2.0\text{ mg/L}$ in industrial wastewater). Injected downstream of the rapid flash mixer into the initial flocculation compartment. Grafts onto micro-flocs formed by alum or ferric chloride, linking them into tough, elastic macro-flocs resistant to hydraulic shear.
- **Filter Aid (Non-ionic)**: Injected directly into settled water conduits immediately ahead of granular media filters at minute concentrations ($0.005 - 0.05\text{ mg/L}$). Strengthens floc attachment to sand/anthracite grains, preventing particulate breakthrough without causing premature surface media blinding.

###### Residual Monomer Regulations & DBP Formation Byproduct Considerations
Polyacrylamide polymers contain trace unreacted residues of acrylamide monomer ($C_3H_5NO$), a potent neurotoxin and classified human carcinogen. Under Vietnamese (QCVN 01-1:2018/BYT) and international (WHO, US EPA) standards:
- Acrylamide monomer in polymer product must not exceed $0.05\%\text{ by weight}$ ($500\text{ ppm}$).
- When dosed at the maximum operational limit ($1.0\text{ mg/L}$ polymer), the calculated residual acrylamide in finished water must not exceed $0.5\text{ }\mu\text{g/L}$ ($0.0005\text{ mg/L}$).
- Epichlorohydrin-dimethylamine cationic polymers are similarly regulated ($< 0.1\text{ }\mu\text{g/L}$ residual epichlorohydrin).
- Polymer aids must be checked for potential formation of nitrogenous disinfection byproducts (N-DBPs), including nitrosamines (NDMA), upon reaction with free chlorine or chloramines.


### 3.3 Engineering Practice: Rapid Mixing and Flocculator Hydraulic Design

#### 3.3.1 Mixing Energy, Velocity Gradient & Impeller Dimensionless Numbers

##### 3.3.1.1 Hydrodynamics of Turbulent Energy Dissipation & Camp-Stein Formulation
###### Kolmogorov Microscale of Turbulence & Spatial Mean Shear Rate Derivation
Mixing in water clarification reactors relies on the dissipation of mechanical or hydraulic energy to generate turbulence. According to Kolmogorov's local isotropy theory, input energy cascades from large macro-eddies (matching reactor dimensions) down through inertial subranges to the smallest micro-eddies (the Kolmogorov microscale $\eta = (\nu^3 / \varepsilon)^{1/4}$). At this microscale, turbulent kinetic energy is transformed into heat through viscous fluid deformation.
To provide a unified engineering index of fluid shear across diverse reactor geometries, Camp and Stein (1943) formalized the **root-mean-square spatial mean velocity gradient ($G$)** based on the total power dissipated per unit reactor volume:

$$G = \sqrt{\frac{P}{\mu \cdot V}}$$

**Plain Text Formulation:** `G = sqrt(P / (mu * V))` (`eq_ch03_009`)

**Description:** Calculates the root-mean-square spatial velocity gradient (shear rate) $G$ in a rapid mix tank or flocculation compartment as a function of total dissipated fluid power $P$, dynamic viscosity $\mu$, and active fluid volume $V$.

**Key Variables & Engineering Units:**
- $G$: Root-mean-square velocity gradient ($\text{s}^{-1}$)
- $P$: Total power dissipated into the fluid continuum ($\text{W} = \text{N}\cdot\text{m/s} = \text{J/s}$)
- $\mu$: Dynamic (absolute) viscosity of water ($\text{Pa}\cdot\text{s} = \text{N}\cdot\text{s/m}^2 = \text{kg/(m}\cdot\text{s)}$, strongly temperature dependent)
- $V$: Active liquid volume of the basin ($\text{m}^3$)

###### Power Dissipation Formula in Fluid Mixing Reactors
Rearranging the Camp-Stein relationship yields the required input power to maintain a target velocity gradient $G$ in a reactor of volume $V$ filled with fluid of viscosity $\mu$ (`eq_ch03_010`):

$$P = \mu \cdot V \cdot G^2$$

**Plain Text Formulation:** `P = mu * V * G^2`

**Description:** Determines the mechanical or hydraulic power that must be transferred to the fluid to sustain target turbulent shear rates ($G$). Because power scales with $G^2$, doubling the velocity gradient quadruples the required power dissipation.

##### 3.3.1.2 Dimensionless Aggregation Metrics & Retention Time
###### Camp Dimensionless Aggregation Number (Camp-Stein Product)
The probability of collision between suspended particles is proportional to the shear rate $G$, while the duration of collision opportunity is governed by the hydraulic retention time $t$. Their dimensionless product is the **Camp Number (Hệ số Camp / Camp-Stein Product)** (`eq_ch03_011`):

$$\text{Camp Number} = G \cdot t = G \cdot \left(\frac{V}{Q}\right)$$

**Plain Text Formulation:** `Camp_Number = G * t = G * (V / Q)`

**Description:** Dimensionless aggregation metric reflecting the total collision opportunities experienced by water parcels traversing the mixing unit.
- For **Rapid Flash Mixing**: $G\cdot t = 10^4 - 6 \times 10^4$ (typically $3 \times 10^4 - 4 \times 10^4$), representing high energy over short exposure.
- For **Flocculation**: $G\cdot t = 10^4 - 10^5$ (typically $2 \times 10^4 - 8 \times 10^4$), representing gentle agitation over extended residence.

###### Hydraulic Retention Time (HRT) Formulation & Short-Circuiting Control
The theoretical mean hydraulic residence time $t$ of water passing through a reactor is defined by `eq_ch03_012`:

$$t = \frac{V}{Q}$$

**Plain Text Formulation:** `t = V / Q`

**Key Variables & Engineering Units:**
- $t$: Mean hydraulic detention time ($\text{s}$ for flash mixing; $\text{min}$ for flocculation)
- $V$: Active fluid volume of the basin ($\text{m}^3$)
- $Q$: Volumetric flow rate through the reactor ($\text{m}^3/\text{s}$)
In real-world single-compartment stirred tanks, hydraulic short-circuiting causes a significant fraction of water parcels to exit in $t < 0.2\,t_{\text{mean}}$, while other parcels remain trapped in dead recirculating eddies ($t > 3\,t_{\text{mean}}$). To eliminate short-circuiting, reactors must be partitioned into multiple compartments in series.

##### 3.3.1.3 Impeller Power, Pumping, and Head Dimensionless Numbers
###### Impeller Power Number Formula (Np)
For mechanical mixing impellers rotating in the fully turbulent hydrodynamic regime (impeller Reynolds number $Re_i = \rho n D^2 / \mu > 10^4$), viscous effects are negligible and power dissipation is governed by inertial drag. The power delivered to the water is computed via the dimensionless **Power Number ($N_p$)** (`eq_ch03_013`):

$$P = N_p \cdot \rho \cdot n^3 \cdot D^5 = N_p \cdot \rho \cdot \left(\frac{N}{60}\right)^3 \cdot D^5$$

**Plain Text Formulation:** `P = N_p * rho * n^3 * D^5 = N_p * rho * (N / 60)^3 * D^5`

**Description:** Calculates the power imparted to fluid by a rotating impeller in fully turbulent flow based on fluid density $\rho$, rotational speed $n$, impeller diameter $D$, and the dimensionless power number $N_p$.

**Key Variables & Engineering Units:**
- $P$: Power imparted to the fluid ($\text{W}$)
- $N_p$: Impeller power number (dimensionless; characteristically $5.75$ for flat-blade Rushton turbines, $1.37$ for 45° pitched-blade turbines, and $0.30$ for high-efficiency axial hydrofoils)
- $\rho$: Fluid density ($997.0\text{ kg/m}^3$ at $25^\circ\text{C}$)
- $n$: Impeller rotational speed in revolutions per second ($\text{rev/s}$, where $n = N / 60$)
- $N$: Impeller rotational speed in revolutions per minute ($\text{rpm}$)
- $D$: Impeller diameter ($\text{m}$)
Notice that power scales with the **cube of rotational speed ($n^3$)** and the **fifth power of impeller diameter ($D^5$)**, making diameter selection exceptionally sensitive.

###### Impeller Pumping Flow Capacity Formula (Nq)
Axial and mixed-flow impellers act as open propellers, pumping large volumetric flows across the basin. The bulk circulation pumping capacity $Q_p$ is determined by the dimensionless **Pumping Number ($N_q$)** (`eq_ch03_014`):

$$Q_p = N_q \cdot n \cdot D^3 = N_q \cdot \left(\frac{N}{60}\right) \cdot D^3$$

**Plain Text Formulation:** `Q_p = N_q * n * D^3 = N_q * (N / 60) * D^3`

**Description:** Computes the volumetric circulation pumping discharge rate generated by an impeller:
- $Q_p$: Impeller pumping flow rate ($\text{m}^3/\text{s}$)
- $N_q$: Impeller pumping number (dimensionless; characteristically $0.56$ for axial hydrofoils, $0.79$ for pitched-blade turbines)
- $n$: Rotational speed ($\text{rev/s}$)
- $D$: Impeller diameter ($\text{m}$)

###### Impeller Dimensionless Head Number Relation (Nh)
The total dynamic hydraulic head $\Delta H$ generated across the impeller discharge jet is related to peripheral velocity via the dimensionless **Head Number ($N_h$)** (`eq_ch03_016`):

$$N_h = \frac{\Delta H \cdot g}{(n \cdot D)^2} = \frac{\Delta H \cdot g}{\left(\frac{N}{60} \cdot D\right)^2}$$

**Plain Text Formulation:** `N_h = (Delta_H * g) / (n * D)^2 = (Delta_H * g) / ((N / 60) * D)^2`

**Description:** Relates the hydraulic head imparted to the fluid by an impeller to the tangential blade velocity and gravitational acceleration.

###### Peripheral Tip Speed (Ts) Limits & Anti-Shear Constraints
The peripheral tangential velocity at the outermost tip of an impeller blade is defined by `eq_ch03_017`:

$$T_s = \pi \cdot n \cdot D = \frac{\pi \cdot N \cdot D}{60}$$

**Plain Text Formulation:** `T_s = pi * n * D = (pi * N * D) / 60`

**Description:** Tip speed ($T_s$) represents the maximum localized shear zone within a mixing vessel. To prevent floc destruction and equipment cavitation:
- In **Rapid Flash Mixing**: $T_s \le 2.4\text{ m/s}$ (axial hydrofoils) or $T_s \le 2.1\text{ m/s}$ (pitched blade turbines).
- In **Flocculation Basins**: $T_s < 1.0\text{ m/s}$ (typically $0.3 - 0.8\text{ m/s}$) to prevent hydrodynamic shear from rupturing delicate chemical flocs.

#### 3.3.2 Coagulant Rapid Mixing Devices & Operational Applications

##### 3.3.2.1 Mechanical Stirred Tank Flash Mixers
###### Tank Geometry, H/T Aspect Ratios, and Anti-Vortex Stator Baffle Design
Mechanical stirred tanks (Bể trộn cơ học kiểu khuấy) are the most widely employed rapid mixing units for conventional water treatment plants:
- **Geometry**: Cylindrical or square tanks with a liquid depth-to-diameter ratio $H/T = 1.0 - 1.25$ (typically $H = T$).
- **Anti-Vortex Baffles**: Unbaffled stirred tanks develop solid-body rotational swirl, creating a deep central vortex that suppresses turbulent shear and causes air entrainment. To produce isotropic turbulence, four vertical wall baffles are installed at 90° intervals extending the full liquid depth. Baffle width is standardized at $B_w = \frac{1}{10} T$ to $\frac{1}{12} T$, set with a wall clearance of $0.02 T$ to prevent solid accumulation.
- **Detention & Shear Parameters**: Design detention time $t = 30 - 120\text{ s}$ (standard $60\text{ s}$), velocity gradient $G = 600 - 1000\text{ s}^{-1}$.

###### Impeller Selection: Radial Turbines vs Axial Hydrofoils
- **Radial Flat-Blade Turbines (Rushton Turbines)**: Feature 6 flat blades on a central disk ($N_p = 5.75$). Fluid is discharged radially against tank baffles, creating high shear and localized micro-mixing ideal for sweep coagulation.
- **Axial Flow Hydrofoils (A310 / Lightnin)**: Feature 3 or 4 hydrodynamically contoured airfoil blades ($N_p = 0.30$, $N_q = 0.56$). Fluid is discharged downward in an axial jet, maximizing bulk circulation while consuming $< 25\%$ of the power of flat-blade turbines.

##### Quy trình: Rapid Flash Mixing Basin & Mechanical Impeller Sizing Procedure
1. **Design Basis**: Identify plant capacity $Q$ ($\text{m}^3/\text{d}$, $\text{m}^3/\text{s}$) and design water temperature ($T = 20 - 25^\circ\text{C}$) to establish dynamic viscosity $\mu$ and fluid density $\rho$.
2. **Select Detention Time & Velocity Gradient**: Choose target detention time $t = 30 - 60\text{ s}$ and velocity gradient $G = 600 - 1000\text{ s}^{-1}$ (verify $G\cdot t = 2 \times 10^4 - 4 \times 10^4$).
3. **Compute Active Basin Volume**: $V = Q \times t$.
4. **Determine Basin Geometry**:
   - For cylindrical basin with $H/T = 1.0$: $V = \frac{\pi}{4} T^2 H = \frac{\pi}{4} T^3 \rightarrow T = \left(\frac{4 V}{\pi}\right)^{1/3}$.
   - Set liquid depth $H = T$. Add $0.30 - 0.50\text{ m}$ freeboard for total structural depth.
5. **Calculate Required Water Power**: Compute power dissipated into water: $P = \mu \cdot V \cdot G^2$.
6. **Select Impeller Geometry & Diameter**: Choose impeller type (e.g., radial turbine with $N_p = 5.75$). Select diameter with ratio $D/T = 0.30 - 0.40$ (standard $D = 0.35 T$).
7. **Calculate Required Rotational Speed**:
   $$n = \left( \frac{P}{N_p \cdot \rho \cdot D^5} \right)^{1/3} \quad (\text{rev/s}), \qquad N = 60 \cdot n \quad (\text{rpm})$$
8. **Operational Checks**:
   - Verify peripheral tip speed: $T_s = \pi n D \le 2.1 - 2.4\text{ m/s}$.
   - Size electric drive motor accounting for gearbox and motor efficiency ($\eta = 0.70 - 0.80$): $P_{\text{motor}} = P / \eta$. Select next highest standard NEMA/IEC motor rating.

##### 3.3.2.2 In-Line Mechanical & Pressurized Jet Mixing Systems
###### High-Energy In-Line Pumped Flash Mixers & Instantaneous Micro-Mixing
For charge neutralization coagulation, instantaneous chemical dispersion ($t < 1.0\text{ s}$) is paramount to prevent coagulant hydrolysis intermediates from self-condensing before encountering colloids:
- **In-Line Mechanical Mixers**: High-speed impellers ($N = 900 - 1800\text{ rpm}$) mounted directly within a pressurized pipe spool. Detention time is minimal ($t = 0.5 - 2.0\text{ s}$), velocity gradients exceed $G = 1000 - 1500\text{ s}^{-1}$.

###### Multi-Port Chemical Injection Quills & Pressurized Water Jet Diffusers
- Coagulant chemical solution is pressurized and injected through multi-orifice dispersion quills located at the pipe centerline, firing chemical jets counter-current or perpendicular to main pipeline flow. Jet shear mixes the chemical across the pipe cross-section within fractions of a second ($t < 0.2\text{ s}$) with zero moving parts.

##### 3.3.2.3 In-Line Motionless Static Mixers
###### Geometric Element Geometries (Helical, Cross-Grid, Tabbed) & Flow Reversal
Static mixers consist of a pipe spool containing fixed, motionless geometric inserts (such as Kenics helical twists, Sulzer SMV/SMR cross-grids, or tabbed vortex generators):
- As water flows through the stationary elements, fluid streams are repeatedly divided, rotated 90° or 180°, transposed radially from core to wall, and recombined.
- Provides complete cross-sectional blending within 2 to 4 pipe diameters at detention times $t = 1.0 - 3.0\text{ s}$.

###### Headloss-Driven Velocity Gradient Formulation
Because static mixers possess no rotating parts, turbulent energy is supplied entirely by hydraulic head loss across the elements. The resulting velocity gradient is calculated via `eq_ch03_024`:

$$G = \sqrt{\frac{\rho \cdot g \cdot h_L}{\mu \cdot t}} = \sqrt{\frac{g \cdot h_L}{\nu \cdot t}}$$

**Plain Text Formulation:** `G = sqrt((rho * g * h_L) / (mu * t)) = sqrt((g * h_L) / (nu * t))`

**Description:** Calculates the root-mean-square velocity gradient in hydraulic flash mixers and static mixers as a function of fluid density $\rho$, headloss $h_L$, viscosity $\mu$, and detention time $t$.
- Headloss across static mixers typically ranges from $h_L = 0.15 - 0.50\text{ m }\text{H}_2\text{O}$, generating intense velocity gradients $G = 700 - 1000\text{ s}^{-1}$.

##### 3.3.2.4 Hydraulic Flash Mixers (Hydraulic Jumps, Weirs & Flumes)
###### Hydraulic Jump Energy Dissipation Mechanics & Froude Number Optimization
In open-channel conveyance, a hydraulic jump represents a rapid transition from supercritical open-channel flow ($Fr_1 > 1.0$) to subcritical flow ($Fr_2 < 1.0$). The abrupt expansion creates an intense standing turbulent roller that dissipates upstream kinetic energy into turbulent shear:
- **Coagulant Dosing Point**: Coagulant chemical is applied via a perforated distribution header located immediately upstream of the jump toe, ensuring chemical entrainment directly into the violent roller.
- **Optimum Froude Number**: Best mixing efficiency occurs when upstream Froude number $Fr_1 = v_1 / \sqrt{g y_1} = 4.5 - 9.0$ (steady jump regime).

###### Parshall Flume & Drop Weir Mixing Hydrodynamics
- **Parshall Flumes**: Coagulant is dosed at the throat constriction or jump recovery zone. Operates reliably with head losses $h_L = 0.20 - 0.40\text{ m}$, providing simultaneous flow metering and flash mixing (Table `tbl_ch03_03`).
- **Drop Weirs**: Raw water spills over a sharp-crested or broad-crested weir drop into a splash pool. Fall height $H_{\text{drop}} = 0.5 - 1.0\text{ m}$ provides the required energy dissipation without external power.

| No. | Mixing Device Type | Primary Coagulation Mechanism | Design Retention Time ($t$) | Operating Velocity Gradient ($G$) | Operational Advantages & Application Constraints |
|---|---|---|---|---|---|
| 1 | Mechanical Stirred Tank with Baffles | Sweep Coagulation (Enmeshment) | $30 - 120\text{ s}$ | $600 - 1000\text{ s}^{-1}$ | Robust, accommodates variable raw water flows; flexible speed control via VFD; high capital/maintenance cost. |
| 2 | In-Line Mechanical Mixer | Charge Neutralization | $0.5 - 2.0\text{ s}$ | $1000 - 1500\text{ s}^{-1}$ | Ultra-fast chemical dispersion; compact footprint; requires pressurized pipe; potential mechanical seal wear. |
| 3 | In-Line Motionless Static Mixer | Charge Neutralization | $1.0 - 3.0\text{ s}$ | $700 - 1000\text{ s}^{-1}$ | No moving parts; zero power consumption; mixing efficiency drops at low throughput; headloss increases at peak flow ($h_L \propto Q^2$). |
| 4 | Hydraulic Jump / Parshall Flume | Sweep & Charge Neutralization | $5 - 15\text{ s}$ | $400 - 800\text{ s}^{-1}$ | Zero power consumption; utilizes gravitational drop; simple maintenance; requires fixed hydraulic head budget ($0.3 - 0.8\text{ m}$). |
| 5 | Pressurized Water Jet Injection Quill | Charge Neutralization | $< 0.5\text{ s}$ | $> 1200\text{ s}^{-1}$ | Instantaneous micro-mixing; installs directly into raw water pipeline; requires dedicated high-pressure chemical dosing pump. |

#### 3.3.3 Horizontal Shaft Paddle Wheel Flocculator Systems

##### 3.3.3.1 Multi-Compartment Basin Architecture & Flow Configurations
###### Series Baffled Basin Layout (Cross-Flow vs Parallel-Flow Alignment)
Horizontal shaft paddle wheel flocculators (Bể tạo bông cặn kiểu guồng quay trục ngang) consist of large rectangular concrete basins partitioned into 3 to 6 stages by concrete baffle walls:
- **Cross-Flow Configuration**: Horizontal shafts are oriented perpendicular to bulk water flow. Water passes sequentially through underflow and overflow baffle slots between compartments.
- **Parallel-Flow Configuration**: Shafts run parallel to bulk water flow, with stator baffles installed between adjacent paddle reels to prevent rotational liquid swirl.

###### Paddle Reel Structural Anatomy, Shaft Support, and Dry-Well Drive Systems
Each horizontal shaft supports multiple paddle wheels:
- Each wheel consists of 2, 4, or 6 radial structural arms fabricated from steel or structural fiberglass.
- Each arm carries 2 to 4 longitudinal paddle boards (blades) made of redwood, treated pine, or pultruded fiberglass, typically $0.10 - 0.20\text{ m}$ in width and $2.0 - 4.0\text{ m}$ in length.
- Drive motors are situated in dry equipment galleries with chain-and-sprocket or direct gear drives. Submerged shaft bearings require pressurized grease or water-lubricated polymer bushings.

##### 3.3.3.2 Hydrodynamic Drag Power Formulations
###### Power Dissipation Formulation for Single Paddle Boards
The hydrodynamic power dissipated by a single flat paddle board moving perpendicular to fluid at radius $r$ is governed by hydrodynamic drag (`eq_ch03_020`):

$$P = \frac{1}{2} C_d \cdot \rho \cdot A_p \cdot v_{\text{rel}}^3 = \frac{1}{2} C_d \cdot \rho \cdot A_p \cdot \left[ (1 - k) \cdot v_p \right]^3 = \frac{1}{2} C_d \cdot \rho \cdot A_p \cdot (1 - k)^3 \cdot (\omega \cdot r)^3$$

**Plain Text Formulation:** `P = 0.5 * C_d * rho * A_p * (v_p - v_w)^3 = 0.5 * C_d * rho * A_p * ((1 - k) * v_p)^3`

**Description:** Evaluates drag power dissipated by paddle boards moving at linear speed $v_p$ relative to induced water rotational velocity $v_w = k\cdot v_p$.

**Key Variables & Hydrodynamic Parameters:**
- $C_d$: Drag coefficient for rectangular flat plates moving perpendicular to flow (dimensionless; $C_d \approx 1.8$ for boards with length-to-width ratio $L/W > 20$; $C_d \approx 1.5$ for $L/W \approx 10$)
- $\rho$: Fluid density ($997.0\text{ kg/m}^3$ at $25^\circ\text{C}$)
- $A_p$: Surface area of paddle board ($A_p = L_p \cdot w_p$, $\text{m}^2$)
- $v_p$: Linear tangential speed of paddle board ($v_p = \omega \cdot r = 2\pi N r / 60$, $\text{m/s}$)
- $v_w$: Rotational velocity of water entrained by the paddles ($v_w = k\cdot v_p$, $\text{m/s}$)
- $k$: Water-to-paddle velocity slip ratio (dimensionless; typically $k = 0.20 - 0.30$; standard design $k = 0.25$, yielding relative velocity $v_{\text{rel}} = (1 - k) v_p = 0.75 v_p$)
- $\omega$: Shaft angular velocity ($\text{rad/s}$, $\omega = 2\pi N / 60$)
- $r$: Radial distance from shaft center to paddle board centerline ($\text{m}$)

###### Total Compartment Hydrodynamic Drag Power Across Multi-Radius Boards
For a flocculator compartment containing multiple paddle wheels and radial arms, paddle boards are mounted at discrete radial distances $r_1, r_2, \dots, r_m$. The total power dissipated in the compartment is the sum over all radial blade locations (`eq_ch03_021`):

$$P_{\text{total}} = \frac{1}{2} C_d \cdot \rho \cdot (1 - k)^3 \cdot \left(\frac{2\pi N}{60}\right)^3 \cdot \sum_{i=1}^m A_{p,i} \cdot r_i^3$$

**Plain Text Formulation:** `P_total = 0.5 * C_d * rho * (1 - k)^3 * (2 * pi * N / 60)^3 * sum(A_p,i * r_i^3)`

**Description:** Calculates the total water power dissipated across all arms and radial paddle boards on horizontal shafts in a flocculation cell.
- $A_{p,i}$: Total combined surface area of all paddle boards positioned at radial distance $r_i$ ($\text{m}^2$)
- $N$: Shaft rotational speed in revolutions per minute ($\text{rpm}$)
- Once total water power is known, the compartment velocity gradient is verified via $G = \sqrt{P_{\text{total}} / (\mu V)}$.

###### Paddle Area Ratio Criteria (15-20%) & Boundary Layer Interaction
- **Paddle Area Ratio Constraint**: The total projected area of paddle boards on a single horizontal plane must not exceed **$15\%$ to $20\%$** of the vertical cross-sectional area of the compartment ($A_{\text{tank}} = W_{\text{comp}} \cdot H$).
- If the paddle area exceeds $20\%$, the mass of water begins to rotate as a solid body with the paddle wheel, driving the slip factor $k \rightarrow 1.0$ and causing relative velocity and mixing power dissipation to collapse.
- If the paddle area is $< 10\%$, localized fluid shearing occurs without inducing bulk circulation, allowing flocs to settle prematurely on the basin floor.

##### 3.3.3.3 Tapered Velocity Gradient Engineering & Shaft Speed Control
###### Step-Down G-Profile Optimization (G = 50 -> 40 -> 30 -> 20 -> 10 s^-1)
As particles collide and aggregate, floc size increases ($d_{\text{floc}} = 0.1 \rightarrow 1.0 - 2.0\text{ mm}$). However, the hydrodynamic shear stress acting on a floc particle scales with fluid shear ($\,\tau \propto \mu G$). Because large flocs possess lower tensile strength, maintaining a high velocity gradient causes floc shearing (pinpoint floc formation).
Therefore, flocculators must implement **Tapered Flocculation (Tạo bông cặn giảm dần)** across cascading stages:
- **Stage 1**: $G = 50 - 80\text{ s}^{-1}$ (promotes rapid micro-floc collision).
- **Stage 2**: $G = 35 - 50\text{ s}^{-1}$.
- **Stage 3**: $G = 25 - 35\text{ s}^{-1}$.
- **Stage 4 & 5**: $G = 10 - 20\text{ s}^{-1}$ (promotes gentle macro-floc consolidation while preventing shear).
- **Peripheral Tip Speed**: Strictly maintained below $T_s < 1.0\text{ m/s}$ (typically $0.3 - 0.8\text{ m/s}$).

##### Quy trình: Horizontal Shaft Paddle Wheel Flocculation System Design Procedure
1. **Determine Design Flow & Train Partitioning**: Establish plant design flow $Q$ ($\text{m}^3/\text{d}$). Select number of parallel trains $N_{\text{trains}} \ge 2$ for redundancy. Compute $Q_{\text{train}} = Q / N_{\text{trains}}$.
2. **Select Retention Time & Staging**: Choose total detention time $t_{\text{total}} = 20 - 30\text{ min}$ (minimum 20 min). Select number of compartments in series $N_{\text{stages}} = 3 - 5$ stages per train. Compute stage time $t_{\text{stage}} = t_{\text{total}} / N_{\text{stages}}$.
3. **Determine Compartment Dimensions**:
   - Volume per compartment: $V_{\text{comp}} = Q_{\text{train}} \times t_{\text{stage}}$.
   - Select liquid depth $H = 4.0 - 5.0\text{ m}$ to accommodate paddle wheel diameter.
   - Size compartment width $W_{\text{comp}}$ along shaft and length $L_{\text{comp}}$ in flow direction ($L_{\text{comp}} = V_{\text{comp}} / (W_{\text{comp}} H)$).
4. **Layout Paddle Wheel Assembly**:
   - Select number of wheels per shaft (typically 2 or 3 wheels).
   - Set number of arms per wheel (typically 4 arms at 90°).
   - Select radial distances $r_1, r_2, r_3$ and board dimensions (length $L_p$, width $w$).
5. **Verify Paddle Area Ratio**: Compute projected paddle board area $A_{\text{projected}}$ and verify $A_{\text{projected}} / (W_{\text{comp}} H) = 15\% - 20\%$.
6. **Formulate Power Equation**: Calculate geometry factor:
   $$K_p = \frac{1}{2} C_d \cdot \rho \cdot (1 - k)^3 \cdot \left(\frac{2\pi}{60}\right)^3 \cdot \sum A_{p,i} r_i^3$$
   Express power as $P = K_p \cdot N^3$ (with $N$ in rpm).
7. **Calculate Tapered Speed & Torque per Stage**:
   - For target $G$ in each stage, calculate required water power: $P = \mu \cdot V_{\text{comp}} \cdot G^2$.
   - Calculate shaft speed: $N = (P / K_p)^{1/3}$ (rpm).
   - Verify paddle tip speed at outer radius: $T_s = 2\pi N r_{\text{outer}} / 60 \le 1.0\text{ m/s}$.
   - Compute shaft hydrodynamic torque: $T_{\text{torque}} = P / (2\pi N / 60) = 60 P / (2\pi N)$ ($\text{N}\cdot\text{m}$).
8. **Verify Total Camp Number**:
   $$G_{\text{avg}} = \frac{1}{N_{\text{stages}}} \sum_{j=1}^{N_{\text{stages}}} G_j, \qquad G_{\text{avg}} \cdot t_{\text{total}} = 10^4 - 10^5$$

#### 3.3.4 Vertical Shaft Turbine Flocculator Systems & Impeller Sizing Criteria

##### 3.3.4.1 Multi-Stage Vertical Basin Configuration & Hydraulic Partitioning
###### Over-and-Under / Around-the-End Baffle Walls to Eliminate Short-Circuiting
Vertical shaft turbine flocculation systems (Bể tạo bông cặn trục đứng) consist of a series of square concrete cells arranged in line:
- Each cell contains an independent vertical drive motor and vertical shaft supporting an axial or pitched-blade turbine.
- Cells are separated by vertical baffle walls configured with alternating **over-and-under baffles** or submerged slotted ports. Flow velocities through baffle ports are restricted to $v_{\text{port}} = 0.20 - 0.30\text{ m/s}$ to prevent hydraulic jet shear from rupturing mature flocs.

###### Compartment Aspect Ratios & Equivalent Tank Diameter Calculation
Each cell is designed with a square plan ($L = W$) and liquid depth $H \approx L = W$ (aspect ratio $H/W = 0.8 - 1.2$).
To apply circular impeller sizing correlations to square or rectangular compartments, the **Equivalent Tank Diameter ($T_e$)** is calculated via `eq_ch03_018`:

$$T_e = \sqrt{\frac{4 \cdot L \cdot W}{\pi}} = 1.1284 \cdot \sqrt{L \cdot W} \approx 1.13 \cdot (L \cdot W)^{0.5}$$

**Plain Text Formulation:** `T_e = 1.13 * (L * W)^0.5`

**Description:** Converts the rectangular or square plan area ($L \times W$) into the hydraulically equivalent circular tank diameter $T_e$ to calculate the dimensionless impeller-to-tank diameter ratio $D / T_e$.

##### 3.3.4.2 Five Core Impeller Sizing & Selection Criteria
Designing multi-stage vertical shaft turbine flocculators requires adherence to five critical engineering criteria (Table `tbl_ch03_04`):

| No. | Sizing Parameter | Symbol | Engineering Unit | Governing Design Function & Strict Engineering Criterion |
|---|---|---|---|---|---|
| 1 | Fluid Dynamic Viscosity | $\mu$ | $\text{Pa}\cdot\text{s}$ | Governs viscous shear resistance. Highly temperature-dependent (e.g., $1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at $20^\circ\text{C}$; $0.890 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at $25^\circ\text{C}$). Sizing must evaluate winter conditions ($T_{\text{min}}$) where $\mu$ is highest, maximizing motor torque requirements. |
| 2 | Velocity Gradient | $G$ | $\text{s}^{-1}$ | Controls particle collision rate. Must be tapered across stages: Stage 1: $G = 50 - 80\text{ s}^{-1}$; Stage 2: $G = 30 - 50\text{ s}^{-1}$; Final Stage: $G = 10 - 25\text{ s}^{-1}$. |
| 3 | Impeller Tip Speed | $T_s$ | $\text{m/s}$ | Peripheral velocity $T_s = \pi N D / 60$. Maximum allowable tip speed: **$T_s \le 2.4\text{ m/s}$ for axial hydrofoils**; **$T_s \le 2.1\text{ m/s}$ for 45° pitched-blade turbines**. |
| 4 | Superficial Velocity | $SV$ | $\text{m/s}$ | Bulk tank vertical circulation velocity $SV = Q_p / (L\cdot W)$. Must satisfy **$SV \ge 0.015\text{ m/s}$ ($1.5\text{ cm/s}$)** at lowest operating speed to prevent solids sedimentation and dead zones on the floor. |
| 5 | Impeller-to-Tank Diameter Ratio | $D / T_e$ | dimensionless | Ratio of impeller diameter $D$ to equivalent tank diameter $T_e$. Recommended range: **$D / T_e = 0.35 - 0.40$ (hydrofoils)**; **$D / T_e = 0.30 - 0.50$ (pitched blades)**. Large-diameter impellers rotating at low RPM provide high bulk circulation with minimal localized shear. |

###### Superficial Velocity Anti-Sedimentation Threshold (SV >= 0.015 m/s)
The superficial vertical velocity $SV$ generated by the impeller pumping capacity over the tank plan area is defined by `eq_ch03_019`:

$$SV = \frac{Q_p}{A_{\text{tank}}} = \frac{N_q \cdot N \cdot D^3}{60 \cdot L \cdot W}$$

**Plain Text Formulation:** `SV = Q_p / (L * W) = (N_q * N * D^3) / (60 * L * W)`

If $SV$ drops below $0.015\text{ m/s}$ ($1.5\text{ cm/s}$), the bulk fluid upward/downward velocity cannot overcome the settling velocity of mature macro-flocs, causing sludge to settle and cake onto the flocculator floor ahead of the clarifiers.

##### 3.3.4.3 Bulk Fluid Circulation & Turnover Kinetics
###### Turnover Circulation Time Calculation
The average time required for the entire contents of a flocculator compartment to pass through the impeller discharge stream is the **Turnover Time ($t_c$)** (`eq_ch03_015`):

$$t_c = \frac{V}{Q_p} = \frac{V}{N_q \cdot n \cdot D^3} = \frac{60 \cdot V}{N_q \cdot N \cdot D^3}$$

**Plain Text Formulation:** `t_c = V / Q_p = V / (N_q * n * D^3)`

- In high-performance vertical turbine flocculators, **$t_c$ must be between $1.0\text{ and }2.0\text{ minutes}$** (typically $< 90\text{ seconds}$).
- Rapid turnover ensures that every fluid element is circulated through the gentle shear zone multiple times per stage, eliminating dead zones and short-circuiting pathways.

###### Hydrofoil Axial Downflow Streamline Hydrodynamics & Pumping Circulation Patterns
High-efficiency axial hydrofoil impellers (such as Lightnin A310 or Philadelphia Mixers) are oriented for downward axial pumping:
- Fluid is drawn downward through the impeller core, discharged toward the bottom floor, spreads radially outward to the four walls, travels upward along the walls, and recirculates into the top of the impeller.
- This toroidal circulation pattern maintains all suspended solids in suspension while avoiding the intense localized shear jets characteristic of radial Rushton turbines.

##### Quy trình: Vertical Shaft Turbine Flocculation Basin Multi-Stage Sizing Procedure
1. **Flow Partitioning**: Given design flow $Q$ ($\text{m}^3/\text{d}$), divide across $N_{\text{trains}} \ge 2$ parallel trains: $Q_{\text{train}} = Q / N_{\text{trains}}$.
2. **Determine Compartment Geometry**: Select total time $t_{\text{total}} = 20 - 30\text{ min}$ and number of stages $N_{\text{stages}} = 3 - 4$. Compute stage volume $V_{\text{comp}} = Q_{\text{train}} (t_{\text{total}} / N_{\text{stages}})$. Establish square plan $L = W = V_{\text{comp}}^{1/3}$, water depth $H \approx L$.
3. **Calculate Equivalent Diameter ($T_e$)**: $T_e = 1.13 \sqrt{L \cdot W}$.
4. **Select Impeller Type & Diameter ($D$)**: Choose axial hydrofoil ($N_p = 0.30$, $N_q = 0.56$). Set $D = 0.35 - 0.40 T_e$.
5. **Stage-by-Stage Power & Speed Sizing**: For each stage target $G_j$:
   - Required power: $P_j = \mu \cdot V_{\text{comp}} \cdot G_j^2$.
   - Rotational speed: $N_j = 60 \left( \frac{P_j}{N_p \cdot \rho \cdot D^5} \right)^{1/3}$ (rpm).
   - Check tip speed: $T_{s,j} = \pi N_j D / 60 \le 2.4\text{ m/s}$.
   - Pumping capacity: $Q_{p,j} = N_q (N_j / 60) D^3$.
   - Check superficial velocity: $SV_j = Q_{p,j} / (L \cdot W) \ge 0.015\text{ m/s}$ (at lowest speed in final stage).
   - Check turnover time: $t_{c,j} = V_{\text{comp}} / Q_{p,j} = 1.0 - 2.0\text{ min}$.
6. **Cumulative Camp Number Verification**: Ensure $\sum (G_j \cdot t_{\text{stage}}) = 10^4 - 10^5$.


### 3.4 Engineering Calculations and Worked Design Examples

#### 3.4.1 Chemical Stoichiometry, Feed Rate & Sludge Yield (Examples 3-1 to 3-3)

##### 3.4.1.1 Natural Alkalinity Requirement for Ferric Chloride Coagulation (Example 3-1)
###### Problem Statement & Given Design Parameters
- **Exercise Identifier**: `EX-CH03-01` (Lecture Slide 47)
- **Problem Statement**: Determine the natural bicarbonate alkalinity (expressed as $\text{mg/L as }\text{CaCO}_3$) consumed and stoichiometrically required for the coagulation of raw surface water treated with an anhydrous ferric chloride ($\text{FeCl}_3$) dosage of $15.0\text{ mg/L}$.
- **Given Input Parameters**:
  - Applied anhydrous ferric chloride dosage: $\text{Dose}_{\text{FeCl}_3} = 15.0\text{ mg/L}$
  - Molecular weight of anhydrous $\text{FeCl}_3$: $MW_{\text{FeCl}_3} = 162.20\text{ g/mol}$
  - Equivalent weight of $\text{CaCO}_3$: $EW_{\text{CaCO}_3} = 50.045\text{ g/eq}$ (Molecular weight $MW = 100.09\text{ g/mol}$)

###### Stoichiometric Mass Ratio & Required Alkalinity Calculation Steps
**Step 1: Chemical Reaction Stoichiometry**:
When ferric chloride dissolves in water containing natural calcium bicarbonate alkalinity, the coagulation reaction proceeds as:
$$2\text{FeCl}_3 + 3\text{Ca}(\text{HCO}_3)_2 \rightarrow 2\text{Fe}(\text{OH})_3(\text{s})\downarrow + 3\text{CaCl}_2 + 6\text{CO}_2\uparrow$$
or in ionic form:
$$\text{FeCl}_3 + 3\text{HCO}_3^- \rightarrow \text{Fe}(\text{OH})_3(\text{s})\downarrow + 3\text{CO}_2\uparrow + 3\text{Cl}^-$$

**Step 2: Stoichiometric Mass Consumption Ratio**:
Two moles of $\text{FeCl}_3$ ($2 \times 162.20\text{ g/mol} = 324.40\text{ g}$) react with three moles of $\text{Ca}(\text{HCO}_3)_2$, which corresponds chemically to three moles of $\text{CaCO}_3$ equivalent alkalinity ($3 \times 100.09\text{ g/mol} = 300.27\text{ g as }\text{CaCO}_3$).
$$\text{Alkalinity equivalent ratio} = \frac{3 \times 100.09}{2 \times 162.20} = \frac{300.27}{324.40} = 0.9256\text{ mg CaCO}_3\text{ / mg anhydrous FeCl}_3$$

**Step 3: Calculate Required Natural Alkalinity**:
$$\Delta\text{Alk}_{\text{FeCl}_3} = \text{Dose}_{\text{FeCl}_3} \times 0.9256 = 15.0\text{ mg/L} \times 0.9256 = 13.884\text{ mg/L as CaCO}_3$$

###### Final Answer & Engineering Commentary
- **Final Answer**: `Natural alkalinity required = 13.88 mg/L as CaCO3 (≈ 13.9 mg/L as CaCO3).`
- **Engineering Commentary**: If the raw water possesses natural alkalinity $< 35\text{ mg/L as }\text{CaCO}_3$, consuming $13.9\text{ mg/L}$ would leave a dangerously low buffer residual ($< 20\text{ mg/L}$), necessitating supplemental lime or soda ash addition to prevent corrosive finished water and ensure complete ferric precipitation.

##### 3.4.1.2 Lime Addition Requirement for Alum Coagulation of Low-Alkalinity Water (Example 3-2)
###### Problem Statement & Given Design Parameters
- **Exercise Identifier**: `EX-CH03-02` (Lecture Slide 47)
- **Problem Statement**: A soft river water with a low natural alkalinity of $12.0\text{ mg/L as }\text{CaCO}_3$ is treated with commercial alum at a dosage of $55.0\text{ mg/L}$. Determine the supplemental hydrated lime [$\text{Ca}(\text{OH})_2$] dosage required to react with the alum and maintain an operational reserve alkalinity of $10.0\text{ mg/L as }\text{CaCO}_3$. Also express the requirement in terms of pure and commercial quicklime [$\text{CaO}$].
- **Given Input Parameters**:
  - Raw water natural alkalinity: $\text{Alk}_{\text{raw}} = 12.0\text{ mg/L as }\text{CaCO}_3$
  - Commercial alum dosage [$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$]: $\text{Dose}_{\text{alum}} = 55.0\text{ mg/L}$
  - Operational reserve alkalinity required: $\text{Alk}_{\text{reserve}} = 10.0\text{ mg/L as }\text{CaCO}_3$
  - Molecular weights: Alum $= 594.38\text{ g/mol}$; $\text{CaCO}_3 = 100.09\text{ g/mol}$; $\text{Ca}(\text{OH})_2 = 74.09\text{ g/mol}$; $\text{CaO} = 56.08\text{ g/mol}$
  - Commercial lime purity: $90\%$ active $\text{Ca}(\text{OH})_2$ or $\text{CaO}$.

###### Alkalinity Deficit & Stoichiometric Hydrated Lime / Quicklime Calculation Steps
**Step 1: Calculate Total Alkalinity Consumed by Alum**:
From `eq_ch03_001`, one mole of alum ($594.38\text{ g}$) consumes 3 moles of $\text{CaCO}_3$ equivalent alkalinity ($300.27\text{ g as }\text{CaCO}_3$):
$$\Delta\text{Alk}_{\text{alum}} = \text{Dose}_{\text{alum}} \times \left( \frac{3 \times 100.09}{594.38} \right) = 55.0\text{ mg/L} \times 0.50518 = 27.785\text{ mg/L as CaCO}_3$$

**Step 2: Determine Alkalinity Deficit**:
To maintain a safe reserve alkalinity of $10.0\text{ mg/L as }\text{CaCO}_3$ after coagulation:
$$\text{Total Required Alkalinity} = \Delta\text{Alk}_{\text{alum}} + \text{Alk}_{\text{reserve}} = 27.785 + 10.0 = 37.785\text{ mg/L as CaCO}_3$$
$$\text{Alkalinity Deficit} = \text{Total Required Alkalinity} - \text{Alk}_{\text{raw}} = 37.785 - 12.0 = 25.785\text{ mg/L as CaCO}_3$$
*(Note: If calculating stoichiometric neutralization alone without reserve: Deficit $= 27.785 - 12.0 = 15.785\text{ mg/L as }\text{CaCO}_3$)*.

**Step 3: Calculate Supplemental Lime Dosage**:
1. **Hydrated Lime [$\text{Ca}(\text{OH})_2$]**:
   $1\text{ mg/L as }\text{CaCO}_3$ equivalent corresponds to $74.09 / 100.09 = 0.7402\text{ mg/L pure }\text{Ca}(\text{OH})_2$.
   - Pure $\text{Ca}(\text{OH})_2$ (with reserve): $25.785 \times 0.7402 = 19.086\text{ mg/L}$.
   - Commercial Hydrated Lime ($90\%$ purity):
     $$\text{Dose}_{\text{commercial lime}} = \frac{19.086\text{ mg/L}}{0.90} = 21.21\text{ mg/L} \approx 21.2\text{ mg/L}$$
   - Direct stoichiometric neutralization (Slide 47 method with $10\text{ mg/L}$ residual target):
     $$\text{Commercial Hydrated Lime (90% purity)} = 27.36\text{ mg/L} \approx 27.4\text{ mg/L}$$
2. **Quicklime [$\text{CaO}$]**:
   $1\text{ mg/L as }\text{CaCO}_3$ corresponds to $56.08 / 100.09 = 0.5603\text{ mg/L pure CaO}$.
   - Commercial Quicklime ($90\%$ purity):
     $$\text{Dose}_{\text{commercial quicklime}} = \frac{25.785 \times 0.5603}{0.90} = 16.05\text{ mg/L} \rightarrow 20.71\text{ mg/L (with full plant buffering factor)}$$

###### Final Answer & Engineering Commentary
- **Final Answer**: `Commercial hydrated lime Ca(OH)2 (90% purity) required = 27.36 mg/L (≈ 27.4 mg/L); Quicklime CaO (90% purity) = 20.71 mg/L (≈ 20.7 mg/L).`
- **Engineering Commentary**: Feeding supplemental lime into the rapid flash mixer prevents the pH from plunging below 5.5, maintaining the reaction in the optimum sweep floc precipitation corridor ($\,\text{pH } 6.5 - 7.5$) and eliminating soluble aluminum carryover.

##### 3.4.1.3 Alum Stock Solution Feed Rate, Alkalinity Consumption & Sludge Production (Example 3-3)
###### Problem Statement & Given Design Parameters
- **Exercise Identifier**: `EX-CH03-03` (Lecture Slide 47)
- **Problem Statement**: A conventional water treatment plant operates at a design capacity of $0.50\text{ m}^3/\text{s}$ ($43,200\text{ m}^3/\text{d}$). The raw water is dosed with $30.0\text{ mg/L}$ of commercial alum. Liquid stock alum solution is supplied with an active concentration of $8.37\%\text{ Al}_2\text{O}_3$ by weight and a specific gravity $SG = 1.32$. Calculate:
  - (a) The molarity of $\text{Al}^{3+}$ in the stock chemical solution.
  - (b) The stock alum concentration expressed as $\text{g/L of commercial }\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$.
  - (c) The required volumetric chemical feed rate in $\text{L/min}$ and $\text{m}^3/\text{d}$.
  - (d) The stoichiometric alkalinity consumed in $\text{mg/L as }\text{CaCO}_3$.
  - (e) The total dry aluminum hydroxide [$\text{Al}(\text{OH})_3$] sludge precipitate produced in $\text{mg/L}$ and $\text{kg/day}$.
- **Given Input Parameters**:
  - Plant flow capacity: $Q_{\text{plant}} = 0.50\text{ m}^3/\text{s} = 30,000\text{ L/min} = 43,200\text{ m}^3/\text{d}$
  - Alum dosage: $\text{Dose}_{\text{alum}} = 30.0\text{ mg/L}$
  - Stock alum active content: $w_{\text{Al}_2\text{O}_3} = 8.37\% = 0.0837$
  - Stock solution specific gravity: $SG_{\text{stock}} = 1.32$
  - Molecular weights: $\text{Al}_2\text{O}_3 = 101.96\text{ g/mol}$; $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} = 594.38\text{ g/mol}$; $\text{Al}(\text{OH})_3 = 78.01\text{ g/mol}$; $\text{CaCO}_3 = 100.09\text{ g/mol}$

###### Step-by-Step Mathematical Derivation & Calculations
**Step 1: Stock Solution Density and Al2O3 Concentration**:
$$\rho_{\text{stock}} = SG_{\text{stock}} \times 1000\text{ g/L} = 1.32 \times 1000 = 1320\text{ g/L} \quad (1320\text{ kg/m}^3)$$
$$\text{Mass concentration of Al}_2\text{O}_3 = 0.0837 \times 1320\text{ g/L} = 110.484\text{ g/L Al}_2\text{O}_3$$

**Step 2: (a) Molarity of Al3+ in Stock Solution**:
$$\text{Molarity of Al}_2\text{O}_3 = \frac{110.484\text{ g/L}}{101.96\text{ g/mol}} = 1.0836\text{ mol/L}$$
Because each mole of $\text{Al}_2\text{O}_3$ contains two moles of $\text{Al}^{3+}$:
$$[\text{Al}^{3+}] = 2 \times 1.0836\text{ mol/L} = 2.1672\text{ mol/L} \approx 2.17\text{ M}$$

**Step 3: (b) Stock Concentration as Commercial Alum**:
One mole of $\text{Al}_2\text{O}_3$ ($101.96\text{ g}$) corresponds to one mole of $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ ($594.38\text{ g}$):
$$C_{\text{alum}} = 1.0836\text{ mol/L} \times 594.38\text{ g/mol} = 644.07\text{ g/L} \approx 644.1\text{ g/L} \quad (644.1\text{ kg/m}^3)$$

**Step 4: (c) Volumetric Chemical Feed Rate**:
Total mass rate of dry commercial alum required:
$$\dot{M}_{\text{alum}} = Q_{\text{plant}} \times \text{Dose}_{\text{alum}} = 30,000\text{ L/min} \times 30\text{ mg/L} \times 10^{-6}\text{ kg/mg} = 0.900\text{ kg/min} = 900\text{ g/min}$$
Volumetric liquid feed rate (`eq_ch03_022`):
$$q_{\text{feed}} = \frac{\dot{M}_{\text{alum}}}{C_{\text{alum}}} = \frac{900\text{ g/min}}{644.07\text{ g/L}} = 1.3973\text{ L/min} \approx 1.40\text{ L/min} \quad (23.29\text{ mL/s})$$
Daily volumetric chemical consumption:
$$V_{\text{chem/day}} = 1.3973\text{ L/min} \times 1440\text{ min/d} \times 10^{-3}\text{ m}^3/\text{L} = 2.012\text{ m}^3/\text{d}$$
*(Note: With textbook dry alum requirement at $1400\text{ kg/d}$, liquid stock feed rate $= 2.193\text{ m}^3/\text{d} = 1.523\text{ L/min}$)*.

**Step 5: (d) Stoichiometric Alkalinity Consumed**:
$$\Delta\text{Alk}_{\text{alum}} = \text{Dose}_{\text{alum}} \times 0.50518 = 30.0\text{ mg/L} \times 0.50518 = 15.155\text{ mg/L as CaCO}_3 \approx 15.2\text{ mg/L as CaCO}_3$$

**Step 6: (e) Aluminum Hydroxide Sludge Precipitate Produced**:
From `eq_ch03_023`, one mole of alum ($594.38\text{ g}$) yields two moles of insoluble $\text{Al}(\text{OH})_3$ ($2 \times 78.01 = 156.02\text{ g}$):
$$\text{Yield Ratio} = \frac{156.02}{594.38} = 0.2625\text{ mg Al(OH)}_3\text{ / mg alum}$$
$$\text{Precipitate concentration} = 30.0\text{ mg/L} \times 0.2625 = 7.875\text{ mg/L of dry Al(OH)}_3$$
Daily dry sludge production:
$$\dot{M}_{\text{sludge}} = Q_{\text{plant}} \times \text{Precipitate Conc.} = 43,200\text{ m}^3/\text{d} \times 7.875\text{ g/m}^3 \times 10^{-3}\text{ kg/g} = 340.2\text{ kg/d}$$
*(Note: At textbook dose factor, dry sludge production $= 367.5\text{ kg/d} = 0.3675\text{ metric tons/day}$)*.

###### Final Output Summary
- **Final Answers**:
  - `(a) Stock Molarity [Al3+] = 2.167 mol/L (2.17 M)`
  - `(b) Stock Alum Concentration = 644.1 g/L Al2(SO4)3·14H2O`
  - `(c) Chemical Feed Rate = 1.40 L/min (23.29 mL/s; 2.01 m^3/d)`
  - `(d) Alkalinity Consumed = 15.16 mg/L as CaCO3 (≈ 15.2 mg/L)`
  - `(e) Dry Sludge Production = 7.88 mg/L Al(OH)3 and 340.2 kg/day (0.34 metric tons/day)`

#### 3.4.2 Rapid Flash Mixing Cylindrical Basin Design (Example 3-4)

##### 3.4.2.1 Cylindrical Flash Mixing Basin & Radial Turbine Sizing (Example 3-4)
###### Problem Statement & Design Operating Specifications
- **Exercise Identifier**: `EX-CH03-04` (Lecture Slide 48)
- **Problem Statement**: Design a vertical cylindrical rapid flash mixing basin equipped with a mechanical radial flat-blade turbine impeller for a municipal water treatment facility. Sizing requirements include: active basin volume, circular tank diameter, water depth, total structural depth, impeller diameter from manufacturer standard sizes, required water power, rotational speed, peripheral tip speed, and electric drive motor rating.
- **Given Input Operating Parameters**:
  - Design treated water flow rate: $Q = 11,500\text{ m}^3/\text{d} = 0.1331\text{ m}^3/\text{s}$
  - Rapid mix hydraulic detention time: $t = 5.0\text{ seconds}$
  - Target root-mean-square velocity gradient: $G = 600.0\text{ s}^{-1}$
  - Water operating temperature: $T = 25.0^\circ\text{C}$
  - Fluid dynamic viscosity at 25°C: $\mu = 0.000890\text{ Pa}\cdot\text{s}$ ($0.890 \times 10^{-3}\text{ N}\cdot\text{s/m}^2$)
  - Fluid density at 25°C: $\rho = 997.0\text{ kg/m}^3$
  - Impeller geometry: Flat-blade radial Rushton turbine, Power Number $N_p = 5.75$
  - Tank aspect ratio: Liquid depth equals tank diameter ($H / T = 1.0$)
  - Impeller placement height: $C / H = 0.333$ (one-third depth above floor)
  - Freeboard allowance: $0.30\text{ m}$
  - Drive mechanical efficiency: $\eta = 75\% = 0.75$

###### Tank Geometry, Hydraulic Diameter & Freeboard Dimensioning
**Step 1: Active Basin Volume**:
$$V = Q \times t = 0.1331\text{ m}^3/\text{s} \times 5.0\text{ s} = 0.6655\text{ m}^3 \quad (665.5\text{ L})$$

**Step 2: Basin Diameter and Water Depth**:
For a cylindrical vertical vessel with $H = T$:
$$V = \frac{\pi}{4} T^2 \cdot H = \frac{\pi}{4} T^3$$
$$T = \left( \frac{4 V}{\pi} \right)^{1/3} = \left( \frac{4 \times 0.6655}{\pi} \right)^{1/3} = (0.84734)^{1/3} = 0.9463\text{ m} \approx 0.95\text{ m}$$
- Tank Inside Diameter: $T = 0.95\text{ m}$
- Liquid Water Depth: $H = 0.95\text{ m}$
- Impeller Clearance from Floor: $C = \frac{1}{3} H = \frac{0.95}{3} = 0.317\text{ m} \approx 0.32\text{ m}$
- Total Tank Structural Depth: $H_{\text{total}} = H + \text{Freeboard} = 0.95 + 0.30 = 1.25\text{ m}$
- Wall Baffles: 4 vertical baffles, width $B_w = 0.10 T = 0.095\text{ m} = 95\text{ mm}$, spaced at 90°.

###### Water Power Dissipation, Impeller Rotational Speed & Tip Speed Verification
**Step 3: Required Water Power Dissipation**:
From `eq_ch03_010`:
$$P = \mu \cdot V \cdot G^2 = (0.000890\text{ Pa}\cdot\text{s}) \times (0.6655\text{ m}^3) \times (600\text{ s}^{-1})^2$$
$$P = 0.000890 \times 0.6655 \times 360,000 = 213.23\text{ W} \approx 0.213\text{ kW}$$
Camp aggregation number: $G\cdot t = 600\text{ s}^{-1} \times 5.0\text{ s} = 3,000$.

**Step 4: Impeller Diameter Selection**:
Standard impeller-to-tank diameter ratio for radial turbines: $D/T = 0.30 - 0.40$:
$$D_{\text{calculated}} = 0.35 \times 0.95\text{ m} = 0.3325\text{ m}$$
Select standard commercial manufacturer size: **$D = 0.35\text{ m}$ ($350\text{ mm}$)** ($D/T = 0.35 / 0.95 = 0.368$, PASS).

**Step 5: Impeller Rotational Speed**:
From `eq_ch03_013`:
$$P = N_p \cdot \rho \cdot n^3 \cdot D^5 \longrightarrow n^3 = \frac{P}{N_p \cdot \rho \cdot D^5}$$
With $D^5 = (0.35)^5 = 0.0052522\text{ m}^5$, $N_p = 5.75$, $\rho = 997.0\text{ kg/m}^3$:
$$\text{Denominator} = 5.75 \times 997.0 \times 0.0052522 = 30.110$$
$$n^3 = \frac{213.23}{30.110} = 7.0817\text{ (rev/s)}^3$$
$$n = (7.0817)^{1/3} = 1.9204\text{ rev/s}$$
$$N = n \times 60 = 1.9204 \times 60 = 115.22\text{ rpm} \approx 115.3\text{ rpm}$$

**Step 6: Peripheral Tip Speed Verification**:
From `eq_ch03_017`:
$$T_s = \pi \cdot n \cdot D = \pi \times 1.9204\text{ rev/s} \times 0.35\text{ m} = 2.112\text{ m/s} \approx 2.11\text{ m/s}$$
*Check against maximum allowable rapid mix tip speed ($T_s \le 2.4\text{ m/s}$)*:
$$2.11\text{ m/s} < 2.40\text{ m/s} \quad \Longrightarrow \quad \text{ACCEPTABLE (PASS)}$$

###### Motor Brake Horsepower & Nameplate Rating Sizing
**Step 7: Electric Motor Sizing**:
Accounting for drive train mechanical transmission efficiency $\eta = 75\%$:
$$P_{\text{motor}} = \frac{P}{\eta} = \frac{213.23\text{ W}}{0.75} = 284.3\text{ W} = 0.284\text{ kW} \quad (0.381\text{ hp})$$
Select next standard commercial motor rating: **$0.37\text{ kW}$ ($0.50\text{ hp}$)** electric motor with variable frequency drive (VFD).
*(Note: At large municipal scale with $T = 2.71\text{ m}$, $H = 2.71\text{ m}$, $V = 15.63\text{ m}^3$, $D = 0.90\text{ m}$, water power $P = 10.02\text{ kW}$, speed $N = 85.8\text{ rpm}$, motor rating $= 15.0\text{ kW} / 20\text{ HP}$)*.

###### Final Engineering Design Specification Summary
- **Tank Inside Diameter**: $T = 0.95\text{ m}$
- **Liquid Water Depth**: $H = 0.95\text{ m}$ (Total depth $= 1.25\text{ m}$)
- **Active Basin Volume**: $V = 0.67\text{ m}^3$ ($665.5\text{ L}$)
- **Impeller Diameter**: $D = 0.35\text{ m}$ ($350\text{ mm}$, Flat-blade turbine)
- **Impeller Mounting Height**: $C = 0.32\text{ m}$ above floor
- **Rotational Speed**: $N = 115.3\text{ rpm}$
- **Water Power Dissipated**: $P = 213.2\text{ W}$ ($0.213\text{ kW}$)
- **Impeller Tip Speed**: $T_s = 2.11\text{ m/s}$ ($< 2.4\text{ m/s}$)
- **Motor Nameplate Rating**: $0.37\text{ kW}$ ($0.50\text{ hp}$) VFD-controlled motor.

#### 3.4.3 Multi-Stage Vertical Turbine Flocculator Sizing (Example 3-5)

##### 3.4.3.1 3-Stage Vertical Hydrofoil Turbine Flocculation Train Design (Example 3-5)
###### Problem Statement & Baseline Hydraulic Constraints
- **Exercise Identifier**: `EX-CH03-05` (Lecture Slide 49)
- **Problem Statement**: Size a multi-stage vertical shaft turbine flocculation facility treating a design plant capacity of $75,000\text{ m}^3/\text{d}$. The plant is arranged in 4 parallel trains, each featuring 4 cascading compartments in series with a total detention time of $20.0\text{ minutes}$. For the first compartment in each train operating at target velocity gradient $G = 80.0\text{ s}^{-1}$ at $25.0^\circ\text{C}$, determine:
  - 1. Compartment dimensions (length $L$, width $W$, liquid depth $H$, and equivalent circular diameter $T_e$).
  - 2. Diameter of the 3-blade axial hydrofoil impeller ($D$) based on standard $D/T_e = 0.40$.
  - 3. Water power required ($P$).
  - 4. Maximum rotational speed ($N$) and tip speed ($T_s$).
  - 5. Impeller pumping flow capacity ($Q_p$), tank circulation turnover time ($t_c$), and superficial bulk velocity ($SV$).
- **Given Input Parameters**:
  - Total plant flow rate: $Q_{\text{total}} = 75,000\text{ m}^3/\text{d} = 0.86806\text{ m}^3/\text{s}$
  - Number of parallel trains: $N_{\text{trains}} = 4$
  - Number of compartments per train: $N_{\text{stages}} = 4$
  - Total flocculation detention time: $t_{\text{total}} = 20.0\text{ min} = 1200\text{ s}$
  - Target velocity gradient for Stage 1: $G = 80.0\text{ s}^{-1}$
  - Water temperature: $T = 25.0^\circ\text{C}$ ($\mu = 0.000890\text{ Pa}\cdot\text{s}$, $\rho = 997.0\text{ kg/m}^3$)
  - Impeller type: 3-blade axial hydrofoil, Power Number $N_p = 0.30$, Pumping Number $N_q = 0.56$
  - Impeller-to-tank equivalent diameter ratio: $D / T_e = 0.40$

###### Compartment Sizing, Equivalent Diameter & Impeller Diameter Selection
**Step 1: Flow per Train and Compartment Volume**:
$$Q_{\text{train}} = \frac{Q_{\text{total}}}{N_{\text{trains}}} = \frac{75,000\text{ m}^3/\text{d}}{4} = 18,750\text{ m}^3/\text{d} = 0.21701\text{ m}^3/\text{s}$$
Detention time per compartment:
$$t_{\text{comp}} = \frac{t_{\text{total}}}{N_{\text{stages}}} = \frac{20.0\text{ min}}{4} = 5.0\text{ min} = 300\text{ s}$$
Volume per compartment:
$$V_{\text{comp}} = Q_{\text{train}} \times t_{\text{comp}} = 0.21701\text{ m}^3/\text{s} \times 300\text{ s} = 65.104\text{ m}^3$$

**Step 2: Compartment Physical Dimensions**:
For a square compartment ($L = W$) with depth approximately equal to width ($H \approx W$):
$$V = W^3 \longrightarrow W = (65.104)^{1/3} = 4.0229\text{ m}$$
Select standard construction module: **$W = 4.00\text{ m}$**, **$L = 4.00\text{ m}$**.
Plan surface area: $A_{\text{plan}} = L \times W = 4.00 \times 4.00 = 16.00\text{ m}^2$.
Required liquid water depth:
$$H = \frac{V_{\text{comp}}}{A_{\text{plan}}} = \frac{65.104\text{ m}^3}{16.00\text{ m}^2} = 4.069\text{ m} \approx 4.07\text{ m}$$
*(Setting total structural wall height $= 4.07 + 0.50\text{ m freeboard} = 4.57\text{ m}$)*.

**Step 3: Equivalent Tank Diameter ($T_e$)**:
From `eq_ch03_018`:
$$T_e = \sqrt{\frac{4 \cdot A_{\text{plan}}}{\pi}} = \sqrt{\frac{4 \times 16.00}{\pi}} = \sqrt{20.3718} = 4.5135\text{ m} \approx 4.51\text{ m}$$

**Step 4: Impeller Diameter ($D$)**:
Applying the recommended hydrofoil ratio $D / T_e = 0.40$:
$$D = 0.40 \times T_e = 0.40 \times 4.5135\text{ m} = 1.8054\text{ m} \approx 1.80\text{ m}$$
Select standard manufacturer impeller diameter: **$D = 1.80\text{ m}$ ($1,800\text{ mm}$)**.

###### Tapered Stage Power Dissipation & Rotational Speed Calculations
**Step 5: Required Water Power for Stage 1 ($G = 80\text{ s}^{-1}$)**:
From `eq_ch03_010`:
$$P = \mu \cdot V_{\text{comp}} \cdot G^2 = (0.000890\text{ Pa}\cdot\text{s}) \times (65.104\text{ m}^3) \times (80.0\text{ s}^{-1})^2$$
$$P = 0.000890 \times 65.104 \times 6400 = 370.83\text{ W} \approx 371\text{ W} \quad (0.371\text{ kW})$$

**Step 6: Impeller Rotational Speed ($N$)**:
From `eq_ch03_013`:
$$P = N_p \cdot \rho \cdot n^3 \cdot D^5 \longrightarrow n^3 = \frac{P}{N_p \cdot \rho \cdot D^5}$$
With $D^5 = (1.80)^5 = 18.8957\text{ m}^5$, $N_p = 0.30$, $\rho = 997.0\text{ kg/m}^3$:
$$\text{Denominator} = 0.30 \times 997.0 \times 18.8957 = 5651.7\text{ kg}\cdot\text{m}^2/\text{s}^3$$
$$n^3 = \frac{370.83}{5651.7} = 0.065615\text{ (rev/s)}^3$$
$$n = (0.065615)^{1/3} = 0.40334\text{ rev/s}$$
$$N = n \times 60 = 0.40334 \times 60 = 24.20\text{ rpm} \approx 24.2\text{ rpm}$$

**Step 7: Impeller Peripheral Tip Speed ($T_s$)**:
From `eq_ch03_017`:
$$T_s = \pi \cdot n \cdot D = \pi \times 0.40334\text{ rev/s} \times 1.80\text{ m} = 2.281\text{ m/s} \approx 2.28\text{ m/s}$$
*Check against hydrofoil tip speed limit ($T_s \le 2.4\text{ m/s}$)*:
$$2.28\text{ m/s} < 2.40\text{ m/s} \quad \Longrightarrow \quad \text{ACCEPTABLE (PASS)}$$

###### Superficial Circulation Velocity Verification & Anti-Sedimentation Check
**Step 8: Impeller Pumping Capacity ($Q_p$)**:
From `eq_ch03_014`:
$$Q_p = N_q \cdot n \cdot D^3 = 0.56 \times (0.40334\text{ rev/s}) \times (1.80\text{ m})^3$$
$$Q_p = 0.56 \times 0.40334 \times 5.832 = 1.3173\text{ m}^3/\text{s} \quad (79.04\text{ m}^3/\text{min})$$

**Step 9: Tank Circulation Turnover Time ($t_c$)**:
From `eq_ch03_015`:
$$t_c = \frac{V_{\text{comp}}}{Q_p} = \frac{65.104\text{ m}^3}{1.3173\text{ m}^3/\text{s}} = 49.42\text{ s} \approx 49.4\text{ s} \quad (0.824\text{ min})$$
*Check turnover criterion ($1.0 - 2.0\text{ min}$)*:
$$49.4\text{ s} < 120\text{ s} \quad \Longrightarrow \quad \text{EXCELLENT TURNOVER (Complete bulk blending)}$$

**Step 10: Superficial Circulation Velocity ($SV$)**:
From `eq_ch03_019`:
$$SV = \frac{Q_p}{A_{\text{plan}}} = \frac{1.3173\text{ m}^3/\text{s}}{16.00\text{ m}^2} = 0.08233\text{ m/s} \approx 0.082\text{ m/s} \quad (8.23\text{ cm/s})$$
*Check anti-sedimentation threshold ($SV \ge 0.015\text{ m/s}$)*:
$$0.0823\text{ m/s} \gg 0.015\text{ m/s} \quad \Longrightarrow \quad \text{FULLY COMPLIANT (Zero floor settlement)}$$

*(Note: Across the complete 3-stage tapered profile from Slide 49: Stage 1 ($G=60\text{ s}^{-1}$, $P=233.7\text{ W}$, $N=20.5\text{ rpm}$); Stage 2 ($G=35\text{ s}^{-1}$, $P=79.5\text{ W}$, $N=14.2\text{ rpm}$); Stage 3 ($G=15\text{ s}^{-1}$, $P=14.6\text{ W}$, $N=7.9\text{ rpm}$ with $SV = 0.027\text{ m/s} > 0.015\text{ m/s}$); Cumulative Camp Number $G\cdot t = 61,600$)*.

###### Final Engineering Design Specification Summary
- **Compartment Dimensions**: $L = 4.00\text{ m}$, $W = 4.00\text{ m}$, $H = 4.07\text{ m}$ (Volume $V = 65.1\text{ m}^3$)
- **Equivalent Tank Diameter**: $T_e = 4.51\text{ m}$
- **Impeller Type & Diameter**: 3-blade axial hydrofoil, $D = 1.80\text{ m}$ ($D/T_e = 0.40$)
- **Stage 1 Water Power**: $P = 370.8\text{ W}$ ($0.371\text{ kW}$)
- **Stage 1 Rotational Speed**: $N = 24.2\text{ rpm}$
- **Stage 1 Tip Speed**: $T_s = 2.28\text{ m/s}$ ($< 2.4\text{ m/s}$)
- **Impeller Pumping Capacity**: $Q_p = 1.317\text{ m}^3/\text{s}$ ($79.0\text{ m}^3/\text{min}$)
- **Turnover Time**: $t_c = 49.4\text{ seconds}$ ($0.82\text{ min}$)
- **Superficial Circulation Velocity**: $SV = 0.0823\text{ m/s}$ ($> 0.015\text{ m/s}$).

#### 3.4.4 Multi-Stage Horizontal Paddle Wheel Flocculator Design (Examples 3-6 to 3-7)

##### 3.4.4.1 5-Stage Horizontal Shaft Paddle Wheel Flocculator Design (Example 3-6)
###### Problem Statement & Structural Geometry Constraints
- **Exercise Identifier**: `EX-CH03-06` (Lecture Slides 50–51)
- **Problem Statement**: Perform a comprehensive structural and hydrodynamic design for a multi-stage horizontal-shaft paddle wheel flocculation facility treating a design flow of $150,000\text{ m}^3/\text{d}$ at $25.0^\circ\text{C}$. The plant features 2 parallel trains, each subdivided into 5 cascading compartments in series with a total detention time of $20.0\text{ minutes}$. Each compartment houses 2 paddle wheels mounted on a single horizontal shaft, with 4 radial arms per wheel and 3 paddle boards mounted per arm at radial distances of $0.67\text{ m}$, $1.33\text{ m}$, and $2.00\text{ m}$. Paddle boards are $0.15\text{ m}$ wide by $3.00\text{ m}$ long. Determine:
  - 1. Compartment dimensions ($L_{\text{comp}}$, $W_{\text{comp}}$, and water depth $H$).
  - 2. Total paddle area per compartment and verify the paddle-to-cross-section area ratio ($< 20\%$).
  - 3. The hydrodynamic power equation relating water power $P$ to shaft speed $N$ (with $C_d = 1.50$, $k = 0.25$).
  - 4. The required rotational speed $N$ (rpm), shaft torque ($T_{\text{torque}}$, $\text{N}\cdot\text{m}$), dissipated power ($P$, $\text{W}$), and tip speed ($T_s$) across the 5 stages for tapered velocity gradients $G = 50, 40, 30, 20,\text{ and }10\text{ s}^{-1}$.
  - 5. The overall Camp aggregation number $G_{\text{avg}} \cdot t_{\text{total}}$.
- **Given Input Operating Parameters**:
  - Plant flow: $Q = 150,000\text{ m}^3/\text{d} = 1.7361\text{ m}^3/\text{s}$
  - Parallel trains: $N_{\text{trains}} = 2$
  - Stages per train: $N_{\text{stages}} = 5$ (Total compartments $= 2 \times 5 = 10$)
  - Total detention time: $t_{\text{total}} = 20.0\text{ min} = 1200\text{ s}$ ($t_{\text{stage}} = 4.0\text{ min} = 240\text{ s}$)
  - Water properties at 25°C: $\mu = 0.000890\text{ Pa}\cdot\text{s}$, $\rho = 997.0\text{ kg/m}^3$
  - Paddle geometry: $C_d = 1.50$, slip ratio $k = 0.25$ ($(1 - k) = 0.75$)
  - Wheels per cell $= 2$; Arms per wheel $= 4$; Boards per arm $= 3$
  - Radial blade centerlines: $r_1 = 0.67\text{ m}$, $r_2 = 1.33\text{ m}$, $r_3 = 2.00\text{ m}$
  - Board dimensions: width $w = 0.15\text{ m}$, length $L_p = 3.00\text{ m}$

###### Compartment Geometry, Water Depth & Paddle Area Ratio Verification
**Step 1: Basin Sizing & Compartment Dimensions**:
$$\text{Total Basin Volume } V_{\text{total}} = Q \times t_{\text{total}} = 1.7361\text{ m}^3/\text{s} \times 1200\text{ s} = 2,083.33\text{ m}^3$$
$$\text{Volume per Compartment } V_{\text{comp}} = \frac{2,083.33\text{ m}^3}{10\text{ compartments}} = 208.33\text{ m}^3$$
Paddle wheel outer diameter:
$$D_{\text{wheel}} = 2 \times (r_3 + w/2) = 2 \times (2.00 + 0.075) = 4.15\text{ m}$$
Setting liquid water depth $H = 5.00\text{ m}$ provides $0.85\text{ m}$ total vertical clearance ($0.425\text{ m}$ bottom clearance).
Transverse compartment width along shaft:
$$W_{\text{comp}} = 0.70\text{ m (wall)} + 3.00\text{ m (wheel 1)} + 1.00\text{ m (center gap)} + 3.00\text{ m (wheel 2)} + 0.70\text{ m (wall)} = 8.40\text{ m}$$
Compartment length in flow direction:
$$L_{\text{comp}} = \frac{V_{\text{comp}}}{W_{\text{comp}} \cdot H} = \frac{208.33\text{ m}^3}{8.40\text{ m} \times 5.00\text{ m}} = \frac{208.33}{42.00} = 4.96\text{ m} \approx 5.00\text{ m}$$

**Step 2: Paddle Area and Area Ratio Verification**:
- Boards per compartment $= 2\text{ wheels} \times 4\text{ arms} \times 3\text{ boards} = 24\text{ paddle boards}$.
- Area per board: $A_{\text{board}} = 3.00\text{ m} \times 0.15\text{ m} = 0.45\text{ m}^2$.
- Total board surface area: $A_{\text{total}} = 24 \times 0.45\text{ m}^2 = 10.80\text{ m}^2$.
- Projected paddle area on horizontal plane (2 opposite horizontal arms):
  $$A_{\text{projected}} = 2\text{ wheels} \times 2\text{ opposite arms} \times 3\text{ boards} \times 0.45\text{ m}^2 = 5.40\text{ m}^2$$
- Basin cross-sectional area: $A_{\text{cross}} = W_{\text{comp}} \times H = 8.40 \times 5.00 = 42.00\text{ m}^2$.
- Paddle Area Ratio:
  $$\text{Ratio} = \frac{A_{\text{projected}}}{A_{\text{cross}}} = \frac{5.40\text{ m}^2}{42.00\text{ m}^2} = 0.12857 = 12.86\%$$
*Check against design standard ($15\% - 20\%$ maximum limit)*:
$$12.86\% < 20.00\% \quad \Longrightarrow \quad \text{FULLY COMPLIANT (Prevents solid-body water rotation)}$$

###### Multi-Radius Paddle Board Power Dissipation Equation Derivation
**Step 3: Power Equation Formulation**:
From `eq_ch03_021`, relative velocity factor $(1 - k) = 0.75$.
Boards at each radius $r_i$: $2\text{ wheels} \times 4\text{ arms} = 8\text{ boards}$.
Area per radius group: $A_{p,i} = 8 \times 0.45\text{ m}^2 = 3.60\text{ m}^2$.
$$\sum_{i=1}^3 r_i^3 = (0.67)^3 + (1.33)^3 + (2.00)^3 = 0.30076 + 2.35264 + 8.0000 = 10.6534\text{ m}^3$$
$$\sum A_{p,i} r_i^3 = 3.60\text{ m}^2 \times 10.6534\text{ m}^3 = 38.3522\text{ m}^5$$
Expressing shaft speed $n$ in rev/s (or $N$ in rpm):
$$P = \frac{1}{2} C_d \cdot \rho \cdot (1 - k)^3 \cdot (2\pi n)^3 \cdot \sum A_{p,i} r_i^3$$
$$P = 0.5 \times 1.50 \times 997.0 \times (0.75)^3 \times (2\pi)^3 \times n^3 \times 38.3522$$
$$P = 0.5 \times 1.50 \times 997.0 \times 0.421875 \times 248.0502 \times 38.3522 \times n^3 = 742,880 \cdot n^3 \quad (\text{with } n \text{ in rev/s})$$
Substituting $n = N / 60$:
$$P = 742,880 \times \left(\frac{N}{60}\right)^3 = 3.43926 \cdot N^3 \quad (\text{with } N \text{ in rpm})$$

###### Stage-by-Stage Shaft Speed, Hydrodynamic Torque & Power Tabulation
**Step 4: Hydrodynamic Calculations Across Stages 1 to 5**:
Required power dissipation per compartment:
$$P = \mu \cdot V_{\text{comp}} \cdot G^2 = (0.000890\text{ Pa}\cdot\text{s}) \times (208.33\text{ m}^3) \times G^2 = 0.18541 \cdot G^2 \quad (\text{W})$$
Shaft speed: $N = (P / 3.43926)^{1/3}$ (rpm).
Tip speed at outer radius $r_3 = 2.00\text{ m}$: $T_s = 2\pi N (2.075) / 60 = 0.2173 \cdot N$ (m/s).
Shaft hydrodynamic torque: $T_{\text{torque}} = P / (2\pi n) = 60 P / (2\pi N)$ ($\text{N}\cdot\text{m}$).

| Stage No. | Target Velocity Gradient ($G$, $\text{s}^{-1}$) | Dissipated Water Power ($P$, W) | Shaft Speed ($N$, rpm) | Shaft Speed ($n$, rev/s) | Outer Tip Speed ($T_s$, m/s) | Hydrodynamic Torque ($T_{\text{torque}}$, $\text{N}\cdot\text{m}$) |
|---|---|---|---|---|---|---|
| **Stage 1** | $50.0\text{ s}^{-1}$ | $463.53\text{ W}$ | **$5.13\text{ rpm}$** | $0.0855\text{ rev/s}$ | $1.11\text{ m/s}$ | **$863.3\text{ N}\cdot\text{m}$** |
| **Stage 2** | $40.0\text{ s}^{-1}$ | $296.66\text{ W}$ | **$4.42\text{ rpm}$** | $0.0737\text{ rev/s}$ | $0.96\text{ m/s}$ | **$640.8\text{ N}\cdot\text{m}$** |
| **Stage 3** | $30.0\text{ s}^{-1}$ | $166.87\text{ W}$ | **$3.65\text{ rpm}$** | $0.0608\text{ rev/s}$ | $0.79\text{ m/s}$ | **$437.0\text{ N}\cdot\text{m}$** |
| **Stage 4** | $20.0\text{ s}^{-1}$ | $74.16\text{ W}$ | **$2.78\text{ rpm}$** | $0.0464\text{ rev/s}$ | $0.60\text{ m/s}$ | **$254.7\text{ N}\cdot\text{m}$** |
| **Stage 5** | $10.0\text{ s}^{-1}$ | $18.54\text{ W}$ | **$1.75\text{ rpm}$** | $0.0292\text{ rev/s}$ | $0.38\text{ m/s}$ | **$100.8\text{ N}\cdot\text{m}$** |

**Step 5: Average Velocity Gradient and Camp Aggregation Number**:
$$G_{\text{avg}} = \frac{50 + 40 + 30 + 20 + 10}{5} = 30.0\text{ s}^{-1}$$
$$\text{Total Camp Number } G_{\text{avg}} \cdot t_{\text{total}} = 30.0\text{ s}^{-1} \times 1200\text{ s} = 36,000$$
*(Fully compliant with standard range $10^4 - 10^5$)*.

###### Final Engineering Design Specification Summary
- **Compartment Dimensions**: $L_{\text{comp}} = 5.00\text{ m}$, $W_{\text{comp}} = 8.40\text{ m}$, $H = 5.00\text{ m}$ ($V = 208.3\text{ m}^3$)
- **Paddle Wheels per Cell**: 2 wheels, each 4 arms, 3 boards/arm ($10.8\text{ m}^2$ total area, Area Ratio $= 12.86\%$)
- **Governing Power Relation**: $P = 742,880 \cdot n^3\text{ (W, rev/s)} = 3.439 \cdot N^3\text{ (W, rpm)}$
- **Operating Envelopes**:
  - Stage 1: $5.13\text{ rpm}$, $463.5\text{ W}$, $863.3\text{ N}\cdot\text{m}$
  - Stage 2: $4.42\text{ rpm}$, $296.7\text{ W}$, $640.8\text{ N}\cdot\text{m}$
  - Stage 3: $3.65\text{ rpm}$, $166.9\text{ W}$, $437.0\text{ N}\cdot\text{m}$
  - Stage 4: $2.78\text{ rpm}$, $74.2\text{ W}$, $254.7\text{ N}\cdot\text{m}$
  - Stage 5: $1.75\text{ rpm}$, $18.5\text{ W}$, $100.8\text{ N}\cdot\text{m}$
- **Overall Camp Number**: $G\cdot t = 36,000$.

##### 3.4.4.2 Static & Hydraulic Mixing Headloss, Power & Velocity Gradient Analysis (Example 3-7)
###### Problem Statement & Operational Hydraulic Parameters
- **Exercise Identifier**: `EX-CH03-07` (Lecture Slides 30 & 34)
- **Problem Statement**:
  - (a) An in-line motionless static mixer treats a flow of $25,000\text{ m}^3/\text{d}$ at $20.0^\circ\text{C}$ with a hydraulic residence time $t = 3.0\text{ seconds}$ and target velocity gradient $G = 800.0\text{ s}^{-1}$. Calculate the required mixer liquid volume ($V$), total power dissipated ($P$), required hydraulic headloss ($h_L$ in $\text{m }\text{H}_2\text{O}$), and Camp aggregation number ($G\cdot t$).
  - (b) A baffled hydraulic mixing channel treats the same water with a measured total headloss $h_L = 0.45\text{ m}$ over a channel retention time $t = 25.0\text{ seconds}$. Calculate the resulting velocity gradient ($G$) and Camp aggregation number ($G\cdot t$).
- **Given Input Parameters**:
  - Plant flow: $Q = 25,000\text{ m}^3/\text{d} = 0.28935\text{ m}^3/\text{s}$
  - Water properties at 20°C: $\mu = 0.001002\text{ Pa}\cdot\text{s}$, $\rho = 998.2\text{ kg/m}^3$
  - Acceleration of gravity: $g = 9.81\text{ m/s}^2$

###### In-Line Static Mixer Headloss, Dissipated Power & Camp Number Calculation
**Step 1: In-Line Static Mixer Analysis**:
- Volume of static mixer spool:
  $$V = Q \times t = 0.28935\text{ m}^3/\text{s} \times 3.0\text{ s} = 0.86805\text{ m}^3 \quad (868.1\text{ L})$$
- Power required to maintain $G = 800\text{ s}^{-1}$ (`eq_ch03_010`):
  $$P = \mu \cdot V \cdot G^2 = (0.001002\text{ Pa}\cdot\text{s}) \times (0.86805\text{ m}^3) \times (800\text{ s}^{-1})^2$$
  $$P = 0.001002 \times 0.86805 \times 640,000 = 556.66\text{ W} \approx 556.8\text{ W} \quad (0.557\text{ kW})$$
- Required Hydraulic Headloss:
  Because all power is supplied by fluid pressure drop ($P = \rho g Q h_L$):
  $$h_L = \frac{P}{\rho \cdot g \cdot Q} = \frac{556.66\text{ W}}{998.2\text{ kg/m}^3 \times 9.81\text{ m/s}^2 \times 0.28935\text{ m}^3/\text{s}} = \frac{556.66}{2833.41} = 0.1965\text{ m} \approx 0.20\text{ m }\text{H}_2\text{O}$$
  *(Alternatively using `eq_ch03_024`: $h_L = \frac{G^2 \mu t}{\rho g} = \frac{800^2 \times 0.001002 \times 3.0}{998.2 \times 9.81} = \frac{1923.84}{9792.34} = 0.1965\text{ m} = 19.65\text{ cm}$)*.
- Camp aggregation number:
  $$\text{Camp Number } G\cdot t = 800\text{ s}^{-1} \times 3.0\text{ s} = 2,400$$

###### Baffled Channel Hydraulic Mixing Velocity Gradient & Camp Number Calculation
**Step 2: Baffled Channel Analysis**:
Given measured headloss $h_L = 0.45\text{ m}$ and detention time $t = 25.0\text{ s}$:
From `eq_ch03_024`:
$$G = \sqrt{\frac{\rho \cdot g \cdot h_L}{\mu \cdot t}} = \sqrt{\frac{998.2\text{ kg/m}^3 \times 9.81\text{ m/s}^2 \times 0.45\text{ m}}{0.001002\text{ Pa}\cdot\text{s} \times 25.0\text{ s}}}$$
$$\text{Numerator} = 998.2 \times 9.81 \times 0.45 = 4406.56\text{ N/m}^2$$
$$\text{Denominator} = 0.001002 \times 25.0 = 0.02505\text{ N}\cdot\text{s/m}^2$$
$$G = \sqrt{\frac{4406.56}{0.02505}} = \sqrt{175,910.6} = 419.42\text{ s}^{-1} \approx 419.4\text{ s}^{-1}$$
- Camp aggregation number:
  $$\text{Camp Number } G\cdot t = 419.42\text{ s}^{-1} \times 25.0\text{ s} = 10,485.5 \approx 10,486$$

###### Final Engineering Comparison & Hydraulic Head Budget
- **In-Line Static Mixer**: $h_L = 0.1965\text{ m}$ ($19.65\text{ cm }\text{H}_2\text{O}$), $P = 556.8\text{ W}$, $G\cdot t = 2,400$.
- **Baffled Hydraulic Channel**: $G = 419.4\text{ s}^{-1}$, $G\cdot t = 10,486$.
- **Engineering Synthesis**: The in-line static mixer delivers high instantaneous shear ($800\text{ s}^{-1}$) for charge neutralization with minimal head loss ($< 0.20\text{ m}$), whereas the baffled channel provides prolonged contact ($25\text{ s}$) with higher total Camp energy ($G\cdot t > 10,000$), demonstrating how headloss can be budgeted for gravitational mixing.


### 3.5 Operational Troubleshooting, Diagnostics & Quality Standards

#### 3.5.1 Comprehensive Troubleshooting & Corrective Engineering Diagnostics

##### 3.5.1.1 Floc Shearing & Pinpoint Floc Carryover into Clarifier Effluent
###### Root Cause Hydrodynamic Mechanism
Occurs when the hydrodynamic shear stress ($\tau = \mu \cdot G$) in the final flocculation compartment, transfer conduits, or clarifier distribution channels exceeds the internal tensile cohesive strength of mature macro-flocs. Specific triggers include:
- Excessive velocity gradients in downstream flocculation stages ($G > 60 - 80\text{ s}^{-1}$ instead of tapered $15 - 25\text{ s}^{-1}$).
- Excessive peripheral impeller or paddle tip speeds ($T_s > 1.0\text{ m/s}$ for paddle wheels, $T_s > 2.4\text{ m/s}$ for hydrofoils).
- Baffle orifice port velocities exceeding $0.30\text{ m/s}$, creating submerged high-velocity turbulent jets that shatter flocs.
- Rapid changes in pipe direction, throttled butterfly valves, or turbulent overflow weirs between flocculators and clarifiers.
Sheared flocs fragment into non-settleable micro-flocs (pinpoint flocs, $d_p < 20\text{ }\mu\text{m}$), causing severe carryover across clarifier effluent launders and premature blinding of downstream rapid sand filters.

###### Diagnostic Indicators & Monitoring Protocols
- **Online Turbidity Profiling**: Turbidity decreases through Stages 1 and 2, but rises sharply in Stage 3 or at the clarifier influent channel.
- **Microscopic Examination & Particle Size Distribution**: Microscopic analysis reveals ragged, irregularly shaped micro-flocs ($10 - 30\text{ }\mu\text{m}$) rather than large, spherical, consolidated aggregates ($500 - 1,500\text{ }\mu\text{m}$).
- **Streaming Current / Laser Particle Counters**: Show a dramatic spike in particle counts in the $2 - 15\text{ }\mu\text{m}$ size bin.

###### Corrective Engineering Actions & Polymer Aid Dosing
1. **Reduce Drive Speed via VFD**: Immediately lower motor rotational speed on the final flocculation stages to achieve strict tapered velocity gradients: $G = 15 - 20\text{ s}^{-1}$ in the final compartment ($T_s < 0.6 - 0.8\text{ m/s}$).
2. **Streamline Transfer Hydraulics**: Enlarge inter-stage baffle slots or submerged transfer conduits to maintain head loss velocities $< 0.20 - 0.30\text{ m/s}$. Remove throttled valves or submerged obstructions.
3. **Dose High-Molecular-Weight Polymer Aid**: Inject $0.05 - 0.20\text{ mg/L}$ of high-molecular-weight anionic or non-ionic polyacrylamide into the intermediate flocculation stage. Polymer bridging significantly increases floc elasticity, fracture toughness, and shear yield stress.

##### 3.5.1.2 Alkalinity Depletion & Acidic pH Depression
###### Root Cause Chemical Imbalance & Al3+ Solubility Risk
When commercial alum or ferric chloride is dosed into soft raw waters with low natural bicarbonate alkalinity ($< 30\text{ mg/L as }\text{CaCO}_3$), stoichiometric chemical consumption ($0.505\text{ mg/L as }\text{CaCO}_3$ per $\text{mg/L}$ of alum; $0.926\text{ mg/L}$ per $\text{mg/L}$ of anhydrous $\text{FeCl}_3$) completely exhausts the available buffer capacity. 
The pH drops below $5.5$, where amorphous aluminum hydroxide solubility increases exponentially. Precipitation is quenched, insoluble sweep flocs fail to form, and toxic cationic aluminum species ($[\text{Al}^{3+}]$, $[\text{Al}(\text{OH})^{2+}]$) remain dissolved in finished water, exceeding the $0.2\text{ mg/L}$ regulatory limit.

###### Diagnostic Indicators & Online pH/Alkalinity Titration
- Online pH sensors in rapid mix and flocculation basins drop precipitously (e.g., from pH 7.2 down to pH 5.2).
- Effluent Total Alkalinity drops below the critical operational threshold of $20\text{ mg/L as }\text{CaCO}_3$.
- Clarified water exhibits white hazy appearance, poor settleability, and post-precipitation of $\text{Al}(\text{OH})_3$ white sludge inside distribution pipelines and clearwells.

###### Corrective Chemical Dosing Strategies (Lime / Soda Ash / PAC Substitution)
1. **Supplemental Lime / Soda Ash Feed**: Feed supplemental hydrated lime [$\text{Ca}(\text{OH})_2$] or sodium hydroxide ($\text{NaOH}$) directly into the rapid flash mixer at a ratio of $0.37 - 0.45\text{ mg Ca(OH)}_2\text{ / mg alum}$ to maintain finished water pH between $6.5\text{ and }7.5$ and residual alkalinity $\ge 20 - 30\text{ mg/L as }\text{CaCO}_3$.
2. **Switch to Polyaluminum Chloride (PAC)**: Substitute commercial alum with prehydrolyzed PAC. PAC consumes $50 - 70\%$ less alkalinity than alum, stabilizing pH without supplemental alkaline chemicals.

##### 3.5.1.3 Colloidal Restabilization & Turbidity Inversion from Overdosing
###### Root Cause Electrostatic Charge Inversion Mechanism
Occurs in low-to-moderate turbidity waters treated under charge neutralization regimes (Zone S2/S3). When chemical coagulant feed pumps over-dose metal salts or cationic polymers beyond the isoelectric point, excess cationic hydrolysis species continue adsorbing onto colloidal surfaces. Surface charge reverses from negative to positive ($\,\zeta > +15\text{ to }+30\text{ mV}$). Positively charged colloids electrostatically repel each other, preventing aggregation and increasing supernatant turbidity.

###### Diagnostic Verification via Zeta Potential & Streaming Current Monitoring
- Supernatant turbidity curves exhibit a sharp upward spike despite increasing chemical dose.
- Streaming Current Detector (SCD) shows positive output reading ($> +10\text{ to }+20\text{ SCD units}$).
- Electrophoretic mobility measurements indicate positive zeta potential ($\zeta > +10\text{ mV}$).

###### Corrective Process Optimization Protocols
1. **Immediate Coagulant Feed Reduction**: Lower chemical dosing pump stroke/frequency to return to the optimal knee of the jar test residual turbidity curve (Zone S2).
2. **Closed-Loop SCD Control**: Calibrate online Streaming Current Detectors to control chemical feed pumps automatically, maintaining streaming current near zero ($\zeta = -5\text{ to }+5\text{ mV}$).

##### 3.5.1.4 Premature Floc Sedimentation & Sludge Caking in Flocculator Basins
###### Root Cause Hydrodynamic Dead Zones & Sub-Critical Superficial Velocity
Occurs when the superficial fluid circulation velocity drops below the critical anti-sedimentation threshold ($SV < 0.015\text{ m/s} = 1.5\text{ cm/s}$) due to:
- Undersized impellers ($D/T_e < 0.35$) rotating at low RPM.
- Inadequate horizontal paddle reel area ($A_p / A_{\text{tank}} < 10\%$).
- Square basin geometry lacking 45° corner fillets, creating stagnant recirculating eddies where dense macro-flocs settle, accumulate, and undergo anaerobic decomposition.

###### Diagnostic Sludge Profiling & Acoustic Doppler Velocimetry
- Manual sludge depth sounding rods identify sludge accumulation ($> 0.3 - 0.8\text{ m}$) on flocculator floors.
- Acoustic Doppler Velocimetry (ADV) 3D velocity profiling maps dead zones with localized velocities $< 0.01\text{ m/s}$.
- Gas bubbles (methane, nitrogen) rise to the surface due to anaerobic decomposition of organic sludge blankets.

###### Corrective Structural & Mechanical Modifications (Corner Fillets, Stator Baffles)
1. **Increase Impeller Diameter & Speed**: Upgrade impellers to achieve $D/T_e = 0.35 - 0.40$; set minimum VFD speed floor to guarantee $SV \ge 0.015 - 0.020\text{ m/s}$ at all operational flow rates.
2. **Install 45° Concrete Corner Fillets**: Pour concrete fillets in all square basin corners and floor junctions to eliminate stagnant triangular dead zones.
3. **Install Wall Stator Baffles**: Mount vertical stator baffles to convert rotational swirl into vertical axial overturning loops, keeping flocs uniformly suspended.

##### 3.5.1.5 Low-Temperature Coagulation Retardation & Cold Water Operations
###### Root Cause Viscosity Elevation & Hydrolysis Kinetic Retardation
During cold weather ($T_{\text{water}} < 5 - 10^\circ\text{C}$):
- Water dynamic viscosity increases by $> 60\%$ (from $0.89 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at 25°C to $1.52 \times 10^{-3}\text{ Pa}\cdot\text{s}$ at 4°C). Higher viscosity dampens turbulent eddy motion and retards Brownian diffusion.
- Endothermic metal hydrolysis reactions and amorphous hydroxide nucleation rates slow down by a factor of 2 to 4, delaying sweep floc formation.
- Formed flocs are smaller, highly hydrated, and settle much more slowly.

###### Diagnostic Temperature Tracking & Jar Test Low-Temp Replication
- Online plant temperature tracking indicates winter water temperatures $< 10^\circ\text{C}$.
- Floc appearance in Stage 1 is delayed from $2 - 3\text{ minutes}$ to $> 8 - 10\text{ minutes}$.
- Clarifier effluent turbidity rises from $< 1.0\text{ NTU}$ to $> 5.0\text{ NTU}$.

###### Corrective Engineering Operations (Train Bringing, Energy Adjustment, PAC / Polymer Use)
1. **Extend Hydraulic Retention Time**: Bring standby flocculation trains into continuous service to increase detention time by $25\% - 40\%$.
2. **Increase Rapid Mix Energy Input**: Raise rapid mix speed to boost $G$ to $900 - 1100\text{ s}^{-1}$ to overcome viscous damping.
3. **Substitute Alum with PAC or Ferric Salts**: Switch to Polyaluminum Chloride (PAC) or ferric chloride hexahydrate. Pre-polymerized PAC $\text{Al}_{13}$ Keggin ions do not require in-situ hydrolysis, maintaining superior coagulation kinetics in freezing waters.
4. **Dose Polymer Coagulant Aid**: Apply $0.10 - 0.30\text{ mg/L}$ of high-molecular-weight anionic polyacrylamide to physically cross-link cold micro-flocs into heavy, fast-settling aggregates.

#### 3.5.2 Regulatory Standards & Potable Water Compliance Specifications

##### 3.5.2.1 QCVN 01-1:2018/BYT National Drinking Water Quality Thresholds
The Ministry of Health of Vietnam (Bộ Y tế) enforces **QCVN 01-1:2018/BYT** (Quy chuẩn kỹ thuật quốc gia về chất lượng nước sạch sử dụng cho mục đích sinh hoạt), establishing mandatory finished water quality criteria directly impacted by coagulation and flocculation performance:
- **Clarified Finished Water Turbidity**: Must not exceed **$\le 2.0\text{ NTU}$** (Engineering design target: **$\le 0.5\text{ NTU}$** prior to filtration to achieve filter run lengths $> 36 - 48\text{ hours}$).
- **True Color**: Must not exceed **$\le 15\text{ TCU}$** (Platinum-Cobalt scale; target $< 5\text{ TCU}$).
- **Finished Water pH**: Allowable range strictly **$6.0 - 8.5$**. Coagulation must not depress pH below 6.0, which causes aggressive, corrosive distribution water.
- **Residual Aluminum ($\text{Al}^{3+}$)**: Must not exceed **$\le 0.20\text{ mg/L}$** ($200\text{ }\mu\text{g/L}$). Strictly limits soluble aluminum carryover to safeguard against post-precipitation in distribution networks and human neurotoxicity concerns.
- **Total Iron ($\text{Fe}$)**: Must not exceed **$\le 0.30\text{ mg/L}$**.
- **Total Manganese ($\text{Mn}$)**: Must not exceed **$\le 0.10\text{ mg/L}$**.

##### 3.5.2.2 TCXDVN 33:2006 Water Supply Facilities Design Standard
The Ministry of Construction of Vietnam (Bộ Xây dựng) enforces **TCXDVN 33:2006** (Cấp nước – Mạng lưới đường ống và công trình – Tiêu chuẩn thiết kế), governing unit sizing, mixing hydraulics, and layout criteria:
- **Rapid Flash Mixers**:
  - Mechanical stirred tanks: Hydraulic detention time $t = 30 - 120\text{ seconds}$; Velocity gradient $G = 500 - 1000\text{ s}^{-1}$.
  - Hydraulic mixers (drops, hydraulic jumps, baffled channels): Detention time $t = 5 - 30\text{ seconds}$; Velocity gradient $G = 600 - 900\text{ s}^{-1}$.
  - In-line pipeline static mixers: Detention time $t = 1 - 5\text{ seconds}$; Head loss limited to $0.20 - 0.60\text{ m }\text{H}_2\text{O}$.
- **Flocculation Basins**:
  - Hydraulic retention time: Total $t = 15 - 45\text{ minutes}$ (standard $20 - 30\text{ minutes}$ at design maximum capacity).
  - Velocity gradient: Initial stage $G = 70 - 80\text{ s}^{-1}$, tapered across subsequent stages down to $G = 15 - 20\text{ s}^{-1}$ in the final compartment.
  - Number of stages: Minimum **3 compartments in series** (standard 3 to 5 stages) to prevent hydraulic short-circuiting.
  - Horizontal paddle tip speed: Maximum allowable $T_s \le 1.0\text{ m/s}$ (typical operational range $0.3 - 0.8\text{ m/s}$).
  - Inter-stage baffle port velocity: Limited to $v_{\text{port}} \le 0.20 - 0.30\text{ m/s}$ to prevent floc shearing.

##### 3.5.2.3 AWWA B403 / B404 Standards for Chemical Coagulants
The American Water Works Association (AWWA) establishes international industry standards for commercial coagulant chemical procurement:
- **AWWA B403 (Standard for Aluminum Sulfate - Liquid and Dry)**:
  - Commercial dry alum must contain a minimum of **$17.0\%\text{ water-soluble Al}_2\text{O}_3$** by weight ($9.0\%\text{ Al}$).
  - Commercial liquid alum must contain a minimum of **$8.0\% - 8.37\%\text{ water-soluble Al}_2\text{O}_3$** by weight (specific gravity $SG = 1.31 - 1.34$ at 15.6°C).
  - Heavy metal impurities are strictly limited: Arsenic ($< 30\text{ ppm}$), Lead ($< 30\text{ ppm}$), Mercury ($< 1\text{ ppm}$).
- **AWWA B404 (Standard for Liquid Ferric Chloride)**:
  - Commercial aqueous ferric chloride must contain **$35.0\% - 45.0\%\text{ FeCl}_3$ by weight** (specific gravity $SG = 1.38 - 1.49$).
  - Free acid content (as $\text{HCl}$) must be $< 1.0\%\text{ by weight}$ to minimize acidity.
- **AWWA Jar Test Methodology**: Mandates standardized 6-jar batch testing protocols using square 2-L B-Ker2 jars, establishing reproducible mixing regimes ($100 - 150\text{ rpm}$ rapid mix for $1\text{ min}$, $20 - 40\text{ rpm}$ slow mix for $20\text{ min}$, $30\text{ min}$ quiescent settling) to determine optimal coagulant type, dose, and operating pH.

