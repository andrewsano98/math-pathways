<!-- 
title: "Math in Chemical Engineering"
output: html_document
bibliography: rmarkdown.bib
 -->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/chemical_engineering_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Chemical Engineering
    </h1>
  </div>

</div>

<br>

###  What will I be doing? 
- Designing and optimizing industrial chemical processes such as reactions, separations, and material production  
- Running simulations of chemical reactions and process flows using specialized engineering software  
- Calculating mass, energy, and momentum balances to design efficient production systems  
- Testing reaction behavior and material properties in laboratory and pilot-scale experiments  
- Monitoring and controlling industrial systems using sensors and automated control software  
- Analyzing chemical data to improve yield, efficiency, safety, and environmental impact  
- Scaling laboratory chemical processes into full industrial production systems  


<br>

###  What are the most common jobs?
- Chemical Engineer  
- Process Engineer  
- Plant Engineer  
- Research and Development Engineer  
- Materials Engineer  
- Environmental Engineer  
- Pharmaceutical Engineer  
- Production Engineer  


<br>

###  What math concepts do I need to know?
- Calculus  
- Differential Equations  
- Linear Algebra  
- Statistics  
- Algebra  
- Thermodynamics  
- Reaction Kinetics  
- Fluid Mechanics  
- Mass and Energy Balances  


--- PAGE ---

## Thermodynamics & Energy

Energy transition refers to the large-scale shift in how energy is produced, stored, and distributed, with the goal of reducing greenhouse gas emissions while maintaining reliability, affordability, and scalability. In chemical engineering, this concept sits at the intersection of thermodynamics, reaction engineering, electrochemistry, and process systems design.

This topic can be divided into three closely connected systems:

1. **Energy generation** - converting chemical, thermal, nuclear, solar, or mechanical energy into usable electrical or mechanical power.

2. **Energy storage and conversion** - storing energy in forms such as batteries, hydrogen, fuels, or thermal systems and converting it between different forms when needed.

3. **Energy transport** - distributing energy through industrial systems while minimizing losses, improving efficiency, and reducing environmental impact.

<br>

### First Law of Thermodynamics

The First Law of Thermodynamics describes the conservation of energy within physical systems. It forms the foundation for analyzing heat, work, and energy transfer in engineering processes.

$$
\Delta E = Q - W
$$

Where:
- $\Delta E$ = change in system energy  
- $Q$ = heat added to the system  
- $W$ = work done by the system  


<br>

### General Steady-State Energy Balance

Many industrial systems operate under steady-state conditions, where energy entering and leaving the system remains balanced over time. This framework is widely used in reactors, turbines, heat exchangers, and process engineering systems.

$$
\dot{Q} - \dot{W} + \sum \dot{m}_{in} h_{in} = \sum \dot{m}_{out} h_{out}
$$

Where:
- $\dot{Q}$ = heat transfer rate into the system  
- $\dot{W}$ = work rate done by the system  
- $\dot{m}$ = mass flow rate  
- $h$ = specific enthalpy  

<br>

### Gibbs Free Energy

Gibbs free energy determines whether chemical and electrochemical processes occur spontaneously under constant temperature and pressure conditions. It is especially important in fuel cells, batteries, electrochemistry, and hydrogen systems.

$$
\Delta G = \Delta H - T\Delta S \quad \text{given} \quad \Delta G < 0
$$

Where:
- $\Delta G$ = Gibbs free energy change  
- $\Delta H$ = enthalpy change  
- $T$ = temperature  
- $\Delta S$ = entropy change  

<br>

### Heat Transfer in Energy Systems

Thermal energy moves through systems by conduction, convection, and radiation. Understanding these mechanisms is essential for thermal management, reactor design, insulation, and power generation systems.

| Formula | Equation |
|---|---|
| *Fourier's Law* | $q = -k \frac{dT}{dx}$ |
| *Convective Heat Transfer* | $q = hA(T_s - T_\infty)$ |
| *Radiative Heat Transfer* | $q = \epsilon \sigma A (T^4 - T_{sur}^4)$ |

Where:
- $q$ = heat transfer rate  
- $k$ = thermal conductivity  
- $h$ = convective heat transfer coefficient  
- $A$ = surface area  
- $T_s$ = surface temperature  
- $T_\infty$ = ambient fluid temperature  
- $\epsilon$ = emissivity  
- $\sigma$ = Stefan–Boltzmann constant  
- $T_{sur}$ = surrounding temperature  

<br>

### Fluid Flow and Mass Transport

Fluid mechanics governs how liquids and gases move through pipes, reactors, turbines, and transport systems. These principles are critical for controlling pressure, velocity, and mass transport in engineering applications.

| Formula | Equation |
|---|---|
| *Bernoulli's Equation* | $P + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}$ |
| *Hagen–Poiseuille Equation* | $Q = \frac{\pi r^4 \Delta P}{8 \mu L}$ |

Where:
- $P$ = pressure  
- $\rho$ = fluid density  
- $v$ = flow velocity  
- $g$ = gravitational acceleration  
- $h$ = height  
- $Q$ = volumetric flow rate  
- $r$ = pipe radius  
- $\Delta P$ = pressure difference  
- $\mu$ = dynamic viscosity  
- $L$ = pipe length  

<br>

### Continuity Equation

The continuity equation expresses conservation of mass within flowing systems. It is fundamental in pipeline analysis, fluid transport, and process engineering.

$$
\dot{m}_{in} = \dot{m}_{out} \quad \text{or} \quad \rho A V = \text{constant}
$$

Where:
- $\dot{m}$ = mass flow rate  
- $\rho$ = density  
- $A$ = cross-sectional area  
- $V$ = flow velocity  

<br>

### Ideal Gas Law

The ideal gas law relates pressure, volume, temperature, and amount of gas within a system. It is widely used in chemical processing, storage systems, combustion analysis, and thermodynamic modeling.

$$
PV = nRT
$$

Where:
- $P$ = pressure  
- $V$ = volume  
- $n$ = amount of substance (moles)  
- $R$ = gas constant  
- $T$ = temperature  

<br>

### Arrhenius Equation

Chemical reaction rates depend strongly on temperature. The Arrhenius equation models this relationship and is widely used in catalysis, combustion, fuel reforming, and electrochemical systems.

$$
k = A e^{-E_a / RT}
$$

Where:
- $k$ = rate constant  
- $A$ = pre-exponential factor  
- $E_a$ = activation energy  
- $R$ = gas constant  
- $T$ = temperature  

<br>

### Efficiency in Thermodynamic Cycles

Thermodynamic efficiency measures how effectively a system converts heat into useful work. These relationships are central to engines, turbines, refrigeration systems, and power generation technologies.

$$
\eta = \frac{W_{out}}{Q_{in}} \quad \text{or} \quad \eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h} \quad \text{for ideal heat engines}
$$

Where:
- $\eta$ = efficiency  
- $W_{out}$ = work output  
- $Q_{in}$ = heat input  
- $T_c$ = cold reservoir temperature  
- $T_h$ = hot reservoir temperature  

<br>

### Energy Production

Energy production concerns the conversion of raw energy resources into usable electrical or chemical energy. Classical systems are dominated by combustion-based processes, where chemical energy stored in fuels is released through oxidation reactions.

**Fossil fuel-based energy sources:**
- Coal — high energy density, high emissions  
- Natural gas — lower emissions than coal, widely used for electricity generation  
- Oil — primarily used in transportation fuels  

A generalized combustion reaction can be expressed as:

$$
\text{C}_x\text{H}_y + O_2 \rightarrow CO_2 + H_2O + \text{energy}
$$

In contrast, modern low-carbon systems aim to reduce or eliminate direct carbon emissions. These include:

- Renewable energy systems (solar, wind, hydro)
- Nuclear fission-based energy production
- Hydrogen-based energy cycles, including electrolysis:

$$
2H_2O \rightarrow 2H_2 + O_2
$$

<br>

### Energy Storage

Energy storage is essential for managing the mismatch between energy supply and demand, particularly in systems reliant on intermittent sources such as wind and solar.

Storage technologies can be broadly grouped into:

- Electrochemical systems (lithium-ion, sodium-ion batteries)
- Chemical storage (hydrogen, synthetic fuels)
- Mechanical storage (pumped hydro, compressed air systems)

For electrochemical systems, a key design metric is energy density:

$$
\text{Energy Density} = \frac{\text{Energy stored}}{\text{mass or volume}}
$$

Where:
- Energy stored = usable energy contained in the system  
- mass or volume = system mass or volume basis  

Engineers optimize these systems by improving electrode kinetics, enhancing electrolyte stability, and minimizing long-term degradation.

Hydrogen systems store energy chemically and release it through fuel cells:

$$
2H_2 + O_2 \rightarrow 2H_2O + \text{energy}
$$

The central engineering challenge is achieving a balance between efficiency, cost, scalability, and operational safety.

<br>

### Energy Distribution

Energy distribution focuses on transporting energy from production sites to end users through interconnected infrastructure systems such as electrical grids, pipelines, and fuel transport networks.

A key limitation in electrical transmission is resistive power loss:

$$
P_{loss} = I^2R
$$

Where:
- $P_{loss}$ = power lost as heat  
- $I$ = electric current  
- $R$ = resistance  

This relationship explains why high-voltage transmission is preferred: increasing voltage reduces current, which in turn reduces energy losses.

In chemical and process engineering systems, distribution challenges also include material compatibility and network optimization. Key contributions include:

- Designing hydrogen-resistant pipeline materials
- Integrating carbon capture into industrial process networks
- Optimizing large-scale energy flow systems to minimize losses

<br>

### Carbon Emissions and System Efficiency

A central metric in evaluating energy systems is carbon intensity, defined as:

$$
\text{Carbon Intensity} = \frac{\text{CO}_2 \text{ emissions}}{\text{energy produced}}
$$

Where:
- CO₂ emissions = total carbon dioxide released  
- energy produced = useful energy output  

Reducing carbon intensity requires coordinated improvements across multiple dimensions of the system:

- Transitioning to low-carbon or zero-carbon energy sources  
- Increasing thermodynamic and process efficiency  
- Improving integration between production, storage, and distribution systems  

It is also important to consider lifecycle emissions, since even renewable systems carry embedded carbon costs associated with manufacturing, transportation, and maintenance.


--- PAGE ---

## Petrochemicals & Fuels

Petrochemicals and fuels form one of the most foundational sectors in chemical engineering, focusing on converting crude oil and natural gas into usable energy carriers and chemical feedstocks. These materials underpin transportation, plastics, pharmaceuticals, fertilizers, and countless industrial products.

<br>

### Crude Oil as a Feedstock

Crude oil is not a single substance but a mixture of hydrocarbons ranging from light gases to heavy asphalt-like compounds. These can include:

- Alkanes (saturated hydrocarbons)
- Cycloalkanes
- Aromatic hydrocarbons
- Trace sulfur, nitrogen, and metal compounds

Because crude oil is chemically diverse, it must be separated and processed before use.


<br>

### Fractional Distillation

The first major step in refining is separating crude oil by boiling point using a distillation column. Components vaporize at different temperatures and condense at different heights.

Typical fractions include:

- Refinery gases (LPG)
- Gasoline (naphtha range)
- Kerosene (jet fuel)
- Diesel
- Heavy fuel oils
- Residuals (bitumen/asphalt)

This process relies on volatility differences rather than chemical change. A key concept is phase equilibrium, often represented through vapor-liquid balance relationships:

$$
y_i P = x_i P_i^{sat}
$$

Where:
- $x_i$ = liquid phase mole fraction  
- $y_i$ = vapor phase mole fraction  
- $P_i^{sat}$ = saturation pressure  

<br>

### Cracking
Heavy hydrocarbons are broken into lighter, more useful molecules:

$$
C_{16}H_{34} \rightarrow C_8H_{18} + C_8H_{16}
$$

Types include:
- Thermal cracking (high heat)
- Catalytic cracking (zeolites, lower temperature, higher selectivity)

Cracking increases gasoline and olefin production (important for plastics).


<br>

### Reforming
Low-octane hydrocarbons are rearranged into higher-octane compounds, often producing hydrogen as a byproduct.

This improves fuel quality for engines by increasing octane rating (resistance to knocking).


<br>

### Petrochemicals

Beyond fuels, petroleum is a critical source of chemical building blocks:

- Ethylene (C₂H₄)
- Propylene (C₃H₆)
- Benzene (C₆H₆)

These are used to produce:

- Plastics (polyethylene, polypropylene)
- Synthetic fibers (polyester, nylon)
- Solvents and detergents

Polymerization example:

$$
nC_2H_4 \rightarrow (C_2H_4)_n
$$

Chemical engineers design reactors that control chain length, branching, and material properties.


<br>

### Combustion and Fuel Efficiency

Fuels ultimately release energy through combustion:

$$
C_xH_y + O_2 \rightarrow CO_2 + H_2O + \text{energy}
$$

A key performance metric is the heating value:

- Higher Heating Value (HHV)
- Lower Heating Value (LHV)

Efficiency is often limited by thermodynamic constraints and incomplete combustion.

Engine performance also depends on stoichiometric balance:

$$
C_xH_y + \left(x + \frac{y}{4}\right)O_2 \rightarrow xCO_2 + \frac{y}{2}H_2O
$$

Too much or too little oxygen reduces efficiency and increases pollutants.


<br>

### Environmental Constraints and Modern Shifts

Petrochemical systems are under increasing pressure due to:

- CO₂ emissions from combustion
- NOₓ and SOₓ pollutants
- Plastic waste accumulation

Chemical engineers address this through:

- Carbon capture systems integrated into refineries
- Cleaner catalytic processes
- Bio-based feedstock alternatives
- Hydrogen blending in fuels


### Faraday's Law of Electrolysis

Critical for water electrolysis scaling:

$$
m = \frac{ItM}{nF}
$$

Where:
- $m$ = mass of substance produced  
- $I$ = electric current  
- $t$ = time  
- $M$ = molar mass of substance  
- $n$ = number of electrons transferred per ion  
- $F$ = Faraday constant  

<br>

### Nernst Equation

Used for batteries and fuel cells:

$$
E = E^\circ - \frac{RT}{nF} \ln Q
$$

Where:
- $E$ = cell potential under non-standard conditions  
- $E^\circ$ = standard cell potential  
- $R$ = universal gas constant  
- $T$ = temperature (Kelvin)  
- $n$ = number of electrons transferred  
- $F$ = Faraday constant  
- $Q$ = reaction quotient  


### Power in Energy Systems

Often used alongside efficiency metrics:

$$
P = VI \quad \text{and} \quad P = V I \cos(\phi) \quad \text{for AC systems}
$$

Where:
- $P$ = power
- $I$ = current
- $V$ = voltage
- $\phi$ = phase angle (power factor)



--- PAGE ---

## Plastics, Polymers & Advanced Materials

Plastics, polymers, and advanced materials focus on the design, synthesis, processing, and performance of large molecular structures that define modern materials science and chemical engineering. These materials determine everything from packaging and textiles to aerospace components and biomedical devices.

<br>

### What is a Polymer?

A polymer is a large molecule made of repeating structural units called monomers. These monomers are chemically bonded into long chains, sometimes with branching or cross-linking.

A general polymerization reaction can be written as:

$$
nM \rightarrow (M)_n
$$

For example, ethylene polymerizes into polyethylene:

$$
nC_2H_4 \rightarrow (C_2H_4)_n
$$

Chemical engineers control:
- Chain length (molecular weight)
- Branching structure
- Degree of cross-linking

These factors strongly influence material properties.


<br>

### Types of Polymerization


<br>

#### Addition Polymerization
Monomers add together without losing atoms. Common for vinyl-based plastics.

Example:
$$
nCH_2=CH_2 \rightarrow -(CH_2-CH_2)_n-
$$

Used in:
- Polyethylene (bags, bottles)
- Polypropylene (containers, textiles)


<br>

#### Condensation Polymerization
Monomers join and release small molecules like water.

Example (simplified):

$$
\text{diacid} + \text{diol} \rightarrow \text{polyester} + H_2O
$$

Used in:
- Nylon
- Polyester (PET)


<br>

### Structure–Property Relationships

One of the most important ideas in polymer engineering is that microscopic structure determines macroscopic behavior.

Key relationships include:

- Longer polymer chains generally increase strength, but they also make the material more difficult to process and shape.
- Greater branching tends to reduce density, often resulting in more flexible materials.
- Increased cross-linking makes a material more rigid, allowing polymers to transition from rubber-like behavior to hard plastics.

A simplified elasticity relationship for polymers can be expressed conceptually through stress-strain behavior:

$$
\sigma = E \epsilon
$$

Where:
- $ \sigma $ = stress  
- $ E $ = modulus of elasticity  
- $ \epsilon $ = strain  

Polymers can behave as:
- Elastic solids
- Viscous fluids
- Viscoelastic materials (both)

<br>

### Thermoplastics vs Thermosets

Polymers are classified based on how they respond to heat:

<br>

#### Thermoplastics
- Soften when heated, harden when cooled
- Reversible process
- Can be remolded

Examples:
- Polyethylene
- Polystyrene

<br>

#### Thermosets
- Form permanent cross-linked networks
- Do not melt upon reheating
- Structurally rigid

Examples:
- Epoxy resins
- Bakelite

<br>

### Advanced Materials

Beyond traditional plastics, chemical engineers design materials with specialized functions.

<br>

#### Composites
Materials made from two or more components:

- Fiber-reinforced polymers (carbon fiber, fiberglass)
- High strength-to-weight ratio

<br>

#### Conductive Polymers
Polymers engineered to conduct electricity by introducing conjugated bonding systems.

Used in:
- Flexible electronics
- Sensors
- Solar cells

<br>

#### Biomaterials
Engineered materials compatible with biological systems:

- Hydrogels
- Biodegradable polymers (PLA, PGA)

<br>

### Processing and Manufacturing

Material properties depend not only on chemistry but also on processing conditions:

- Temperature control during extrusion or molding
- Cooling rate (affects crystallinity)
- Pressure and shear forces in shaping processes

Crystallinity affects density and strength:

$$
\text{Crystallinity} \uparrow \Rightarrow \text{Strength} \uparrow, \text{Transparency} \downarrow
$$

<br>

### Environmental Considerations

A major challenge in polymer engineering is sustainability:

- Plastic waste accumulation
- Microplastic formation
- Difficulty in recycling mixed polymers

Solutions include:
- Biodegradable polymers
- Chemical recycling (breaking polymers back into monomers)
- Closed-loop manufacturing systems

<br>

### Diffusion and Mass Transfer

#### Fick's First Law:
$$
J = -D \frac{dC}{dx}
$$

Used in:
- gas separation
- membrane systems
- catalyst diffusion layers


--- PAGE ---

## Food & Consumer Products

Food and consumer products engineering focuses on transforming raw biological and chemical materials into safe, stable, nutritious, and desirable products at industrial scale. This area of chemical engineering blends thermodynamics, mass transfer, reaction engineering, and microbiology with sensory science and human behavior.

<br>

### From Raw Materials to Processed Products

Most food and consumer goods begin as complex natural systems:

- Agricultural crops (grains, fruits, oils)
- Animal products (milk, meat, eggs)
- Natural extracts (sugars, starches, proteins)

Chemical engineers design processes that transform these into stable products through:

- Separation
- Heat treatment
- Chemical modification
- Formulation

A key idea is mass balance:

$$
\text{Input} = \text{Output} + \text{Accumulation}
$$

This ensures efficiency, consistency, and minimal waste in production systems.

<br>

### Food Processing and Preservation

Food is biologically active and naturally degrades over time due to microbes, enzymes, and oxidation. Chemical engineering extends shelf life through controlled processing. Lower temperatures slow chemical and biological reactions, reducing spoilage rates.

Reaction rate dependence on temperature follows:

$$
k = A e^{-E_a / RT}
$$

Where:
- $E_a$ = activation energy  
- $R$ = gas constant  
- $T$ = temperature  

<br>

### Food Structure and Texture Engineering

Food is not just chemistry—it is structure. Texture depends on molecular arrangement and phase behavior.

Examples:
- Bread: gas bubbles trapped in gluten network
- Ice cream: controlled crystallization of ice and fat
- Chocolate: polymorphic crystal structures of cocoa butter

Phase transitions are critical:

$$
\text{Solid} \leftrightarrow \text{Liquid} \leftrightarrow \text{Gas}
$$

Chemical engineers control:
- Crystallization rate
- Emulsion stability
- Gel formation

<br>

### Emulsions
Mixtures of oil and water stabilized by emulsifiers.

Examples:
- Mayonnaise
- Milk
- Salad dressings

Droplet stability depends on surface tension and surfactants.

<br>

### Colloids
Fine dispersions of particles in a medium.

Examples:
- Yogurt (protein network in liquid)
- Foam (whipped cream)

One significant engineering challenge is to prevent phase separation over time.

<br>

### Consumer Product Formulation

Beyond food, chemical engineering also designs everyday consumer goods:

- Detergents and soaps
- Cosmetics and skincare products
- Pharmaceuticals (non-biological formulation)
- Cleaning agents

These systems require careful balancing of:

- Surfactants (reduce surface tension)
- Solvents (dissolve active ingredients)
- Stabilizers (prevent separation)
- Preservatives (inhibit microbial growth)

For example, surface tension reduction can be conceptualized as:

$$
\gamma = \gamma_0 - \Delta \gamma_{\text{surfactant}}
$$

Where surfactants lower interfacial energy to improve cleaning or mixing performance.

<br>

### Safety, Quality Control, and Regulation

Food and consumer product engineering is highly regulated because it directly affects human health.

Key concerns include:

- Contamination (biological, chemical, physical)
- Dosage control (active ingredients)
- Shelf-life stability
- Batch-to-batch consistency

Statistical quality control is widely used:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

Monitoring variance ensures consistent product quality.

<br>

### Sustainability in Food and Consumer Systems

Modern challenges include:

- Food waste reduction
- Energy-efficient processing
- Sustainable packaging
- Alternative protein sources

Chemical engineers are developing:
- Plant-based and lab-grown proteins
- Biodegradable packaging materials
- Low-energy processing techniques
- Closed-loop production systems


--- PAGE ---

## Water Treatment & Environmental Systems

Water treatment and environmental systems focus on designing processes that ensure clean water, safe wastewater disposal, and reduced environmental impact from industrial and municipal activity. In chemical engineering, this field combines fluid mechanics, separation processes, reaction engineering, and microbiology to protect both human health and ecosystems.

Water is a universal solvent, meaning it easily carries dissolved chemicals, microorganisms, and particulates. Without treatment, water sources can contain:

- Pathogens (bacteria, viruses, protozoa)
- Organic pollutants (oils, pesticides, pharmaceuticals)
- Inorganic ions (heavy metals like lead, mercury)
- Suspended solids (sediment, microplastics)

Chemical engineers design systems that reduce contaminant concentration to safe levels defined by environmental standards.

<br>

### Coagulation and Flocculation
Fine particles are destabilized and aggregated into larger clusters (flocs) using chemical additives.

- Coagulants neutralize particle charges
- Flocculation gently mixes to form larger aggregates

This process increases particle size, making separation easier.

<br>

### Sedimentation
Gravity is used to remove heavier flocs:

$$
v = \frac{2 r^2 (\rho_p - \rho_f) g}{9 \mu}
$$

Where:
- $v$ = settling velocity  
- $r$ = particle radius  
- $\rho_p$ = particle density  
- $\rho_f$ = fluid density  
- $\mu$ = viscosity  

Larger particles settle faster, improving separation efficiency.

<br>

### Filtration
Water passes through porous media (sand, activated carbon, membranes) to remove remaining solids and dissolved contaminants.

<br>

### Primary Wastewater Treatment

Physical removal of solids through screening and sedimentation.

<br>

### Secondary Wastewater Treatment

Biological processes break down organic matter using microorganisms.

A key reaction is aerobic decomposition:

$$
\text{Organic matter} + O_2 \rightarrow CO_2 + H_2O + \text{biomass}
$$

Activated sludge systems are commonly used, where microbial communities digest pollutants.

<br>

### Tertiary Wastewater Treatment
Advanced purification steps, including:

- Nutrient removal (nitrogen, phosphorus)
- Advanced filtration
- Chemical polishing

<br>

### Air Pollution Control
- Scrubbers remove SO₂ and particulate matter
- Catalytic converters reduce NOₓ emissions

Example reaction in catalytic converters:

$$
2CO + O_2 \rightarrow 2CO_2
$$

<br>

### Industrial Waste Treatment
Industries must treat chemical effluents before discharge:

- Neutralization of acids/bases
- Heavy metal precipitation
- Solvent recovery systems

<br>

### Desalination (Reverse Osmosis)
Uses pressure to overcome osmotic pressure:

$$
\pi = iMRT
$$

Where:
- $\pi$ = osmotic pressure  
- $M$ = molar concentration  
- $R$ = gas constant  
- $T$ = temperature  

High pressure forces water through membranes, leaving salts behind.

<br>

### Water Recycling
Treated wastewater is reused for:

- Agriculture
- Industrial cooling
- Groundwater recharge

<br>

### Sustainability and Environmental Impact

Environmental systems engineering aims to reduce:

- Chemical discharge into ecosystems
- Energy consumption in treatment processes
- Sludge and solid waste generation

Key strategies include:
- Energy-efficient aeration systems
- Membrane optimization
- Resource recovery (e.g., phosphorus from wastewater)
- Circular water systems (closed-loop reuse)


--- PAGE ---

## Industrial Chemicals

Industrial chemicals refer to the large-scale production of basic chemical substances that serve as building blocks for nearly all modern industries, including plastics, pharmaceuticals, agriculture, textiles, and energy systems. Chemical engineering in this area focuses on designing efficient, safe, and scalable processes that convert raw materials into high-purity chemical products.

<br>

### What Counts as an Industrial Chemical?

Industrial chemicals are typically high-volume, low-cost substances rather than specialized end products. They are often classified as:

- **Bulk chemicals** (produced in millions of tons annually)
- **Intermediate chemicals** (used to synthesize other products)
- **Specialty chemicals** (lower volume, higher value, more tailored applications)

Examples include:
- Ammonia (fertilizers)
- Sulfuric acid (industrial processing)
- Ethylene and propylene (plastics production)
- Chlorine (disinfection and chemical synthesis)

<br>

### The Importance of Scale

Industrial chemistry is defined by scale. Small efficiency improvements can have enormous economic and environmental impact.

A key concept is production rate:

$$
r = \frac{\text{amount produced}}{\text{time}}
$$

Even a small increase in yield or catalyst efficiency can translate into millions of dollars saved annually.

Chemical engineers design processes that maximize:
- Yield (product formation)
- Selectivity (desired product vs byproducts)
- Throughput (production per unit time)

<br>

### Ammonia Synthesis (Haber-Bosch Process)

One of the most important industrial reactions:

$$
N_2 + 3H_2 \rightleftharpoons 2NH_3
$$

This reaction is:
- High-pressure (to favor product formation)
- High-temperature (to increase reaction rate)
- Catalyst-driven (typically iron-based catalysts)

Ammonia is essential for fertilizers, directly linking industrial chemistry to global food production.

<br>

### Sulfuric Acid Production (Contact Process)

A major industrial acid used in batteries, fertilizers, and refining:

Key step:

$$
2SO_2 + O_2 \rightarrow 2SO_3
$$

Followed by hydration:

$$
SO_3 + H_2O \rightarrow H_2SO_4
$$

Sulfuric acid is often called the “backbone of industry” due to its wide usage.

<br>

### Chlor-Alkali Process

Used to produce chlorine and sodium hydroxide:

$$
2NaCl + 2H_2O \rightarrow Cl_2 + H_2 + 2NaOH
$$

Products are essential for:
- Water treatment (chlorine)
- Soap and paper manufacturing (NaOH)
- Hydrogen production (H₂)

<br>

### Catalysis and Reaction Engineering

Most industrial chemicals rely on catalysts to improve reaction efficiency.

A catalyst:
- Lowers activation energy
- Increases reaction rate
- Is not consumed in the reaction

Reaction rate conceptually follows:

$$
r = k C_A^n
$$

Where:
- $r$ = reaction rate  
- $k$ = rate constant  
- $C_A$ = reactant concentration  
- $n$ = reaction order  

Chemical engineers design reactors to optimize temperature, pressure, and mixing for maximum productivity.

<br>

### Separation and Purification

After reactions occur, products must be separated from byproducts and unreacted materials.

Common separation methods:
- Distillation (boiling point differences)
- Absorption (gas-liquid transfer)
- Extraction (solubility differences)
- Crystallization (solid formation)

Distillation is especially important:

$$
y_i P = x_i P_i^{sat}
$$

Efficient separation is often as important as the reaction itself, sometimes even more expensive than the reaction step.

<br>

### Process Integration and Optimization

Industrial chemical plants are not single reactions but integrated systems.

Chemical engineers focus on:
- Heat integration (reusing waste heat)
- Mass integration (recycling unreacted feedstocks)
- Energy optimization

A key goal is reducing energy intensity:

$$
\text{Energy Intensity} = \frac{\text{energy used}}{\text{product mass}}
$$

Lower energy intensity improves both cost and sustainability.

<br>

### Safety and Risk Management

Industrial chemical production involves hazardous substances, so safety is critical.

Risks include:
- Toxic chemical exposure
- High-pressure system failures
- Exothermic reaction runaway

Engineers use:
- Pressure relief systems
- Process control loops
- Hazard and operability studies (HAZOP)

Maintaining stable operation is as important as maximizing output.

<br>

### Environmental Considerations

Industrial chemistry has significant environmental impact, including:

- Greenhouse gas emissions
- Chemical waste streams
- Energy consumption

Modern approaches aim to:
- Replace fossil-based feedstocks with renewable ones
- Improve catalyst efficiency to reduce waste
- Implement carbon capture systems
- Shift toward circular chemical production systems


--- PAGE ---

## Nuclear Chemistry & Nuclear Energy

Nuclear chemistry and nuclear energy focus on the behavior of atomic nuclei and the enormous amounts of energy released through nuclear reactions. In chemical and nuclear engineering, this field combines thermodynamics, reaction kinetics, neutron transport, heat transfer, and reactor systems design to produce controlled energy at industrial scale.

Unlike conventional chemical reactions, which involve electron interactions between atoms, nuclear reactions alter the nucleus itself. Because nuclear binding energies are extremely large, even small amounts of mass can produce enormous energy output.

<br>

### Nuclear Binding Energy and Mass Defect

Atomic nuclei are held together by the strong nuclear force. The total mass of a nucleus is slightly less than the combined masses of its individual protons and neutrons.

This missing mass is called the **mass defect**, and it corresponds directly to nuclear binding energy.

<br>

### Mass–Energy Equivalence

The fundamental relationship between mass and energy is:

$$
E = mc^2
$$

Where:
- $E$ = energy  
- $m$ = mass defect  
- $c$ = speed of light  

This equation explains why nuclear reactions release vastly more energy than ordinary chemical reactions.

<br>

### Nuclear Reaction Energy

The energy released during a nuclear reaction is determined by the difference in mass between reactants and products:

$$
Q = (m_{reactants} - m_{products})c^2
$$

Positive $Q$ values indicate energy-releasing reactions.

This relationship governs:
- Nuclear fission
- Nuclear fusion
- Radioactive decay processes

<br>

### Radioactive Decay Law

The number of radioactive nuclei remaining after time $t$ is:

$$
N(t) = N_0 e^{-\lambda t}
$$

Where:
- $N(t)$ = remaining nuclei at time $t$  
- $N_0$ = initial quantity  
- $\lambda$ = decay constant  

Radioactive decay follows exponential behavior, meaning decay rate is proportional to the number of unstable nuclei remaining.

<br>

### Half-Life Relationship

The half-life is the time required for half of the radioactive nuclei to decay:

$$
t_{1/2} = \frac{\ln 2}{\lambda}
$$

Half-life is critical in:
- Nuclear waste management
- Medical isotope applications
- Reactor fuel analysis
- Radiation safety calculations

<br>

### Nuclear Fission and Chain Reactions

Most modern nuclear power systems rely on nuclear fission, where heavy nuclei such as uranium-235 split into smaller nuclei after absorbing neutrons.

Fission releases:
- Large quantities of thermal energy
- Additional neutrons
- Gamma radiation

The emitted neutrons can trigger additional fission events, producing a self-sustaining chain reaction.

<br>

### Neutron-Induced Fission Chain Reaction

The behavior of a reactor is governed by the neutron multiplication factor:

$$
k = \frac{\text{neutrons in next generation}}{\text{neutrons in current generation}}
$$

System behavior:
- $k < 1$ → subcritical  
- $k = 1$ → critical (steady reactor)  
- $k > 1$ → supercritical  

Maintaining $k \approx 1$ is essential for stable reactor operation.

<br>

### Nuclear Power Output

Reactor power generation depends on neutron activity and fission rate:

$$
P = \phi \Sigma_f E_f
$$

Where:
- $P$ = reactor power output  
- $\phi$ = neutron flux  
- $\Sigma_f$ = macroscopic fission cross-section  
- $E_f$ = energy released per fission event  

Chemical and nuclear engineers carefully regulate neutron flux and heat removal to maintain safe reactor conditions.

<br>

### Reaction Engineering and Reactor Systems

Although nuclear reactions differ fundamentally from ordinary chemical reactions, many reactor engineering principles remain similar. Engineers still analyze reaction rates, flow behavior, heat transfer, and reactor design.

<br>

### Reaction Rate Laws

General reaction behavior is often modeled using rate expressions:

$$
r_A = k C_A^n
$$

Where:
- $r_A$ = reaction rate  
- $k$ = rate constant  
- $C_A$ = reactant concentration  
- $n$ = reaction order  

Reaction kinetics influence:
- Fuel processing
- Coolant chemistry
- Hydrogen production systems
- Nuclear fuel reprocessing

<br>

### Reactor Design Equations

Chemical engineers use reactor models to describe how reactions evolve over time and space within industrial systems.

<br>

### Batch Reactor

A closed reactor system where material is processed over time without continuous inflow or outflow:

$$
\frac{dN_A}{dt} = -r_A V
$$

Where:
- $N_A$ = amount of species $A$  
- $r_A$ = reaction rate  
- $V$ = reactor volume  

<br>

### Continuous Stirred Tank Reactor (CSTR)

A continuously fed and mixed reactor commonly used in industrial chemical systems:

$$
F_{A0} - F_A + r_A V = 0
$$

Where:
- $F_{A0}$ = inlet molar flow rate  
- $F_A$ = outlet molar flow rate  

<br>

### Plug Flow Reactor (PFR)

A reactor model where fluid moves continuously through the system with minimal back-mixing:

$$
\frac{dF_A}{dV} = r_A
$$

These reactor models govern:
- Hydrogen production systems
- Fuel synthesis
- Emissions reduction systems
- Industrial nuclear fuel processing operations

<br>

### Heat Transfer and Reactor Safety

Nuclear reactors generate extremely high thermal power densities, making heat removal one of the most important engineering challenges.

Reactor systems require:
- Coolant circulation
- Heat exchangers
- Emergency shutdown systems
- Containment structures

Poor heat management can lead to:
- Fuel damage
- Pressure buildup
- Core meltdown scenarios

Because of this, reactor safety engineering is inseparable from thermodynamics and transport phenomena.

<br>

### Nuclear Energy and the Energy Transition

Nuclear energy is considered a low-carbon energy source because electricity generation does not directly emit carbon dioxide during operation.

Potential advantages include:
- Extremely high energy density
- Stable baseload power generation
- Low operational greenhouse gas emissions

Major challenges include:
- Radioactive waste storage
- High infrastructure costs
- Reactor safety concerns
- Nuclear proliferation risks

Modern reactor research includes:
- Small modular reactors (SMRs)
- Molten salt reactors
- Fusion energy systems
- Advanced passive safety designs

Chemical engineers contribute through:
- Fuel cycle optimization
- Coolant chemistry
- Corrosion prevention
- Reactor materials engineering
- Waste processing and containment