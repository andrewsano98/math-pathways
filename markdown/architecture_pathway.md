<!-- 
title: "Math in Architecture"
output: html_document
bibliography: rmarkdown.bib
 -->


<div class="pathway-card">

<img
src="markdown/pathway_images/architecture_photo_1.jpeg"
alt="Placeholder Text"
class="pathway-image"
/>

<div class="pathway-title-overlay">
<h1 class="pathway-title">
Architecture
</h1>
</div>

</div>

<br>

### What will I be doing?
- Designing building layouts, floor plans, and structural concepts using CAD software
- Developing integrated building models that coordinate structural, mechanical, and electrical systems using BIM tools
- Creating 3D visualizations and renderings to communicate design ideas to clients and teams
- Testing structural integrity and load behavior using engineering analysis software
- Selecting appropriate construction materials based on physical properties, cost, and performance requirements
- Coordinating project timelines, teams, and construction phases using project management tools
- Revising and refining designs based on client feedback, regulations, and engineering constraints


<br>

### What are the most common jobs?
- Architect
- Residential Architect
- Commercial Architect
- Landscape Architect
- Urban Planner
- Interior Designer
- Architectural Designer
- Building Information Modeling Specialist


<br>

### What math concepts do I need to know?
- Geometry
- Trigonometry
- Algebra
- Measurement and Scaling
- Spatial Reasoning
- Structural Analysis
- Calculus
- Proportions and Ratios
- Physics of Forces


--- PAGE ---

### Structural Systems

Modern structures can be understood as interconnected geometric networks. Columns act as vertical vectors, beams act as horizontal constraints, and joints define transformation points between forces.

A simplified structural force model can be visualized using vector decomposition:

$ \vec{F} = \vec{F_x} + \vec{F_y} $

This decomposition helps engineers understand how loads transfer through different parts of a building.


--- PAGE ---

### Categories of Smart Materials

Smart materials are typically classified based on the type of stimulus they respond to:

1. **Thermo-responsive materials**
 These materials change properties based on temperature. For example, they may expand, contract, or alter stiffness.

 A simplified thermal expansion model is:

 $ \Delta L = \alpha L_0 \Delta T $

 where:
 - $\Delta L$ is change in length
 - $\alpha$ is the thermal expansion coefficient
 - $L_0$ is original length
 - $\Delta T$ is temperature change

 This relationship is critical in designing structures that must tolerate thermal variation without failure.

2. **Photo-responsive materials**
 These materials react to light intensity or wavelength. They may change opacity, color, or conductivity depending on solar exposure.

 Light intensity distribution across a surface can be modeled using inverse-square relationships:

 $ I = \frac{P}{4\pi r^2} $

 where $I$ is intensity and $r$ is distance from the light source.

3. **Hydro-responsive materials**
 These materials respond to moisture levels, expanding or contracting based on humidity. This is useful in passive ventilation systems.

 Humidity-driven deformation can be treated as a proportional response:

 $ S = kH $

 where $S$ is structural change and $H$ is humidity level.

4. **Stress-responsive materials (piezoelectric systems)**
 These materials generate electrical signals when mechanically stressed, or deform when electrically stimulated.

 A simplified relationship is:

 $ V \propto F $

 where voltage output is proportional to applied force.

<br>

### Load Redistribution and Structural Efficiency

Adaptive structures improve efficiency by redistributing loads in real time. Instead of resisting force through static reinforcement, the system adjusts its form to minimize stress concentration.

Stress distribution can be conceptually modeled as:

$ \sigma = \frac{F}{A} $

where reducing stress involves either decreasing force concentration or increasing effective area dynamically.

In adaptive systems:
- Structural members may thicken under load
- Load paths may shift toward stronger regions
- Redundant elements may disengage to reduce weight


<br>

### Energy Efficiency and Environmental Interaction

Smart materials contribute to sustainability by reducing energy consumption through passive adaptation.

Examples include:
- Facades that open or close based on sunlight intensity
- Materials that change reflectivity to regulate heat absorption
- Ventilation systems that respond to temperature gradients

Heat transfer optimization often aims to control:

$ Q = mc\Delta T $

by dynamically adjusting exposure, insulation, or airflow.


<br>

### Control Theory in Architecture

Adaptive structures borrow heavily from control theory, where systems are regulated using sensors and feedback loops.

A basic control model is:

$ u(t) = K(e(t)) $

where:
- $u(t)$ is the system response
- $e(t)$ is the error between desired and actual state
- $K$ is a control function

This ensures that structures maintain stability while adapting to changing conditions.

<br>

### Structural Intelligence and Computation

Smart architectural systems are often described as having “structural intelligence,” meaning they can compute responses to external stimuli.

This involves:
- Real-time data processing
- Predictive modeling of environmental changes
- Algorithmic adjustment of physical form

In this sense, architecture becomes a physical computation system embedded in material form.


--- PAGE ---

### Social Spacing and Crowd Behavior

Human spatial behavior includes implicit geometric boundaries known as personal space zones. These can be modeled as concentric regions around an individual:

- Intimate zone
- Personal zone
- Social zone
- Public zone

Each zone can be approximated as a radius:

$ A = \pi r^2 $

where $r$ varies depending on cultural and contextual factors.

When density forces overlap of these zones, discomfort or behavioral adjustment occurs, influencing movement and positioning.

<br>

### Spatial Optimization in Design

Architects use behavioral data to optimize layouts for efficiency and comfort. This often involves minimizing travel time while maximizing usability:

$ \min \sum d_i $

subject to:
- accessibility constraints
- safety regulations
- visibility requirements

This creates a multi-variable system where human behavior becomes part of the design equation.

<br>

### Feedback Between People and Space

Human-centered spatial behavior is not one-directional. People shape space through use, and space shapes behavior through design.

This feedback loop can be modeled as:

$ S_{t+1} = f(S_t, H_t) $

where:
- $S_t$ is spatial configuration
- $H_t$ is human behavior at time $t$

Over time, this leads to emergent patterns such as worn pathways, informal shortcuts, or social gathering zones.


--- PAGE ---

### Heat Transfer and Thermal Behavior

One of the most important aspects of environmental physics is heat transfer. Buildings constantly gain and lose heat through conduction, convection, and radiation.

A fundamental relationship governing heat energy is:

$ Q = mc\Delta T $

where:
- $Q$ is heat energy transferred
- $m$ is mass
- $c$ is specific heat capacity
- $\Delta T$ is temperature change

Heat flow through a material is also governed by conduction:

$ Q = \frac{kA\Delta T}{d} $

where:
- $k$ is thermal conductivity
- $A$ is surface area
- $d$ is thickness

These relationships guide decisions about insulation, wall composition, and material selection.

<br>

### Solar Radiation and Energy Input

Buildings absorb energy from sunlight, which can be modeled using intensity relationships:

$ I = \frac{P}{4\pi r^2} $

where $I$ is radiation intensity and $r$ is distance from the source.

The angle of incidence also affects energy absorption. When sunlight strikes a surface, effective energy is proportional to:

$ E \propto \cos(\theta) $

where $\theta$ is the angle between sunlight direction and surface normal.

This explains why architects orient buildings and design shading devices to control solar gain throughout the day and seasons.

<br>

### Airflow and Fluid Dynamics

Air movement around and within buildings follows principles of fluid dynamics. Wind pressure and ventilation can be approximated using velocity and density relationships.

A simplified airflow model is:

$ Q = A v $

where:
- $Q$ is volumetric flow rate
- $A$ is opening area
- $v$ is air velocity

Pressure differences drive airflow:

$ \Delta P = \frac{1}{2} \rho v^2 $

where:
- $\rho$ is air density
- $v$ is wind speed

Architects use these principles to design natural ventilation systems, reduce cooling loads, and improve indoor air quality.

<br>

### Moisture Transport and Humidity

Water vapor movement affects both comfort and structural integrity. Moisture diffusion can be modeled as a gradient-driven process:

$ J \propto -\nabla H $

where:
- $J$ is moisture flux
- $H$ is humidity concentration

If poorly controlled, moisture can lead to condensation, mold growth, or material degradation. Vapor barriers and breathable materials are designed based on these principles.

<br>

### Light Behavior and Daylighting

Light in buildings follows geometric and wave-based principles. Reflection, refraction, and absorption determine how light enters and moves through space.

Illuminance decreases with distance according to:

$ E = \frac{I}{r^2} $

where:
- $E$ is illuminance
- $I$ is luminous intensity
- $r$ is distance

Architects use these relationships to optimize window placement, skylights, and reflective surfaces to maximize natural lighting while minimizing glare.

<br>

### Acoustic Behavior in Space

Sound is another physical wave that interacts with building geometry. Acoustic performance depends on reflection, absorption, and diffusion.

Sound intensity decreases with distance:

$ I \propto \frac{1}{r^2} $

Reverberation time, a key measure of acoustic quality, can be approximated by:

$ T = \frac{0.161 V}{A} $

where:
- $T$ is reverberation time
- $V$ is room volume
- $A$ is total absorption area

These principles guide the design of concert halls, classrooms, and open-plan spaces.

<br>

### Energy Balance in Buildings

A building can be modeled as an energy system with inputs and outputs:

- Inputs: solar radiation, internal heat sources, external temperature
- Outputs: heat loss through walls, ventilation, radiation

A simplified energy balance equation is:

$ \text{Energy In} = \text{Energy Out} + \Delta \text{Stored Energy} $

When balanced, indoor temperature remains stable; when imbalanced, heating or cooling is required.

<br>

### Thermal Comfort and Human Interaction

Environmental physics directly affects human comfort. Thermal comfort depends on temperature, humidity, airflow, and radiation.

A simplified comfort deviation model is:

$ C = |T - T_{opt}| $

where:
- $C$ is discomfort
- $T$ is actual temperature
- $T_{opt}$ is optimal comfort temperature

Lower values indicate better comfort conditions.

<br>

### Building Envelope as a Physical System

The building envelope (walls, roof, windows) acts as a mediator between inside and outside environments. It controls:

- Heat flow
- Air exchange
- Light transmission
- Moisture movement

Each layer of the envelope contributes to overall system behavior, effectively functioning as a multi-variable filter for environmental forces.

<br>

### Feedback Between Environment and Design

Environmental physics introduces feedback loops where design decisions influence physical behavior, which in turn informs further design adjustments.

This can be modeled as:

$ x_{n+1} = f(x_n, E_n) $

where:
- $x_n$ is building state
- $E_n$ is environmental input

This iterative relationship is central to performance-based architecture.


--- PAGE ---

### Density and Usage Intensity

Different programmatic spaces have different occupancy patterns. This affects required area and spatial design.

Density is defined as:

$ \rho = \frac{N}{A} $

where:
- $N$ is number of users
- $A$ is area of space

High-density spaces (auditoriums, transit hubs) require:
- larger circulation capacity
- stronger structural design
- efficient entry/exit distribution

Low-density spaces (offices, storage) allow more flexibility in layout.

<br>

### Temporal Programmatic Behavior

Programmatic design is not only spatial but also temporal. Spaces may change function over time.

This introduces a time-dependent function:

$ P(t) $

where programmatic use varies by time of day, season, or schedule.

Examples:
- Schools: classrooms used at peak daytime hours
- Offices: peak occupancy during work hours
- Event spaces: intermittent high-density use

This leads to multi-function spatial design, where one area serves multiple roles depending on time.

<br>

### Flexibility and Modular Systems

To accommodate changing programmatic needs, architects often use modular grids.

A modular system can be defined as:

$ A = n \cdot s^2 $

where:
- $s$ is module size
- $n$ is number of modules

This allows spaces to be reconfigured without breaking structural logic.

Flexibility reduces long-term inefficiency by allowing adaptation to new requirements.

<br>

### Optimization of Programmatic Efficiency

Programmatic design often seeks to optimize multiple competing objectives:

- Minimize circulation distance
- Maximize usable area
- Reduce wasted space
- Improve adjacency efficiency

A simplified objective function might be:

$ \text{Efficiency} = \frac{\text{Functional Output}}{\text{Spatial Input}} $

Higher efficiency indicates better alignment between space and use.

<br>

### Behavioral Feedback in Programmatic Layout

Once a building is occupied, real human behavior often differs from the initial program. This creates feedback loops:

1. Initial program defines layout
2. Users interact with space
3. Usage patterns emerge
4. Design is adjusted or reinterpreted

This can be modeled as:

$ S_{t+1} = f(S_t, U_t) $

where:
- $S_t$ is spatial configuration
- $U_t$ is user behavior

Over time, spaces may evolve informally through usage patterns rather than formal redesign.


<br>

### Hierarchy and Spatial Priority

Not all programmatic spaces have equal importance. Hierarchical organization assigns priority levels:

- Primary spaces (high importance, main functions)
- Secondary spaces (support functions)
- Tertiary spaces (service, storage, circulation)

This hierarchy affects:
- placement within building
- size allocation
- accessibility routes

Mathematically, this can be represented as weighted importance:

$ W_i > W_j \Rightarrow A_i \geq A_j $

where $W_i$ is functional weight.


--- PAGE ---

### Key Components of Urban & Site Context

1. **Site Boundaries and Geometry**
 Every site has a defined shape—often irregular. Architects analyze perimeter length, area, and usable buildable zones.

 - Area of rectangular site: $A = lw$
 - Area of irregular site (approximation): decomposition into triangles or grids

 Understanding geometry helps determine how efficiently space can be used and how buildings can be oriented.

2. **Topography and Slope**
 Land is rarely flat. Elevation changes affect drainage, accessibility, and structural design.

 Slope between two points is given by:

 $ m = \frac{y_2 - y_1}{x_2 - x_1} $

 In site planning, slope influences:
 - Foundation design (stepped vs. flat foundations)
 - Water runoff direction
 - Road and ramp feasibility

 Steeper slopes often require retaining walls or terracing strategies.

3. **Orientation and Sun Path**
 The angle of sunlight changes throughout the day and year, affecting energy efficiency and comfort.

 Architects use angular reasoning to optimize:
 - Window placement
 - Natural lighting
 - Solar heat gain

 A simplified solar angle relationship can be modeled using periodic functions:

 $ y = A \sin(B(x - C)) + D $

 This helps approximate seasonal variation in sun height and daylight duration.

4. **Urban Grid and Connectivity**
 Cities often follow grid systems or radial layouts. These can be analyzed using:
 - Graph theory (nodes = intersections, edges = streets)
 - Network distance vs. Euclidean distance

 For example:
 - Euclidean distance: straight-line distance
 - Manhattan distance: $|x_1 - x_2| + |y_1 - y_2|$

 This distinction affects real-world travel time and accessibility.

5. **Zoning and Constraint Mapping**
 Zoning laws define what can be built where. These constraints act like boundary conditions in a mathematical system.

 Common zoning variables include:
 - Maximum height (H)
 - Floor-area ratio (FAR)
 - Setback distance (s)

 For example:
 $ \text{Buildable Area} = \text{Site Area} \times \text{FAR} $

 These constraints reduce design freedom but create predictable urban structure.

<br>

### Spatial Reasoning in Design

Urban context analysis is essentially **applied spatial reasoning**. Architects mentally transform maps, rotate forms, and simulate how people move through space. This involves:

- Translating 2D maps into 3D environments
- Estimating visual corridors and sightlines
- Predicting crowd flow using vector-like movement paths

A simple directional vector for movement might be expressed as:

$ \vec{v} = \langle x_2 - x_1,\; y_2 - y_1 \rangle $

This helps model pedestrian flow or circulation between spaces.


--- PAGE ---

### Beam Bending and Structural Stress

When a beam is loaded, internal stress develops based on bending moment and geometry.

$$
\sigma = \frac{My}{I}
$$

Where:
- $\sigma$ = bending stress
- $M$ = bending moment
- $y$ = distance from neutral axis
- $I$ = second moment of area

This relationship determines where materials fail first in a structure.

<br>

### Shear Force and Internal Loading

Structural members experience shear forces that vary along their length:

- Shear force: $V(x)$
- Moment: $M(x)$

Relationship:

$$
\frac{dM}{dx} = V(x)
$$

This allows engineers to map how loads transfer through beams, columns, and slabs.

<br>

### Beam Deflection and Elastic Behavior

Structural deformation is governed by elasticity:

$$
EI \frac{d^2y}{dx^2} = M(x)
$$

Where:
- $E$ = Young’s modulus
- $I$ = moment of inertia
- $y(x)$ = deflection curve

This determines how much a structure bends under load.

<br>

### Stress–Strain Relationship

$$
\sigma = E\epsilon
$$

Where:
- $\sigma$ = stress
- $E$ = Young’s modulus
- $\epsilon$ = strain

This defines elasticity and stiffness of materials.

<br>

### Plastic vs Elastic Deformation

- **Elastic region:** material returns to original shape
- **Plastic region:** permanent deformation occurs

This boundary defines structural safety limits.

<br>

### Fatigue and Long-Term Failure

Repeated loading causes gradual failure even below breaking stress:

- Cyclic stress → microfractures
- Accumulation → structural failure over time

This introduces time-dependent degradation into design.

<br>

## Optimization and Computational Design

Architecture often involves optimizing performance under constraints.

<br>

### General Optimization Framework

$$
\min f(x)
\quad \text{subject to} \quad g_i(x) \le 0
$$

Where:
- $f(x)$ = objective function (cost, energy, material use)
- $g_i(x)$ = constraints (structure, zoning, safety)

<br>

### Multi-Objective Optimization

Architectural design often balances competing goals:

- Minimize material usage
- Maximize structural strength
- Minimize energy consumption
- Maximize spatial efficiency

This becomes:

$$
\min (f_1(x), f_2(x), ..., f_n(x))
$$

leading to a **Pareto frontier of design solutions**.

## Form-Finding and Structural Geometry (Advanced Missing Layer)

Some architectural forms are not designed directly—they are solved as physical or mathematical equilibrium states.

<br>

### Minimal Surface Principle

Structures like membranes and shells minimize surface energy:

$$
\min A = \int \sqrt{1 + f_x^2 + f_y^2}\,dxdy
$$

This produces:
- tensile roofs
- soap-film-like geometries
- efficient spanning structures

<br>

### Tension vs Compression Systems

- **Compression systems:** stone, arches, columns
- **Tension systems:** cables, membranes, tensile grids

Equilibrium condition:

$$
\sum F = 0
$$

## Construction Sequencing and Project Modeling (Missing Temporal Layer)

Architecture also depends on time-dependent planning.

<br>

### Dependency Graph of Construction Tasks

- Nodes = construction tasks
- Edges = dependencies

This forms a directed acyclic graph (DAG).

<br>

### Critical Path Method (CPM)

Project duration is determined by the longest dependent chain:

$$
T_{project} = \max(\sum t_i)
$$

Where $t_i$ are task durations along a path.

This identifies:
- bottlenecks
- scheduling risks
- optimal sequencing

## Integrated Structural Optimization Systems

Modern architecture combines all missing components into a unified model:

- Geometry → defines form
- Physics → governs behavior
- Materials → define response
- Optimization → selects best configuration
- Time → governs construction and evolution

This creates a system:

$$
\text{Design} = f(\text{geometry}, \text{forces}, \text{materials}, \text{constraints}, t)
$$

Where architecture becomes a **solved system rather than a drawn object**.

# Architecture Pathway

## Core Philosophy

Architecture is not primarily about solving long equations by hand. Instead, architects use mathematical thinking through:

- geometry
- proportion
- scale
- spatial reasoning
- topology
- coordinate systems
- parametric relationships

Math in architecture is often abstract and visual rather than calculation-heavy. Architects constantly apply mathematical principles when designing structures, organizing space, producing technical drawings, and communicating dimensions for construction.

# Page 1 — Core Design & Drafting Software

## AutoCAD
Industry-standard 2D drafting software used throughout much of the world.

### Common Uses
- floor plans
- construction drawings
- dimensions and annotations
- technical documentation

### Mathematical Concepts
- coordinate systems
- geometry
- scale
- measurement
- transformations

## SketchUp
Simple and intuitive 3D modeling software widely used in architecture.

### Common Uses
- conceptual design
- massing studies
- rapid prototyping
- presentation models

### Mathematical Concepts
- 3D geometry
- perspective
- transformations
- spatial visualization

## Photoshop
Image editing and presentation software.

### Common Uses
- architectural presentation boards
- rendering touch-ups
- texture editing
- visual communication

### Mathematical Concepts
- scaling
- image resolution
- coordinate-based editing
- color interpolation

# Page 2 — 3D Modeling & Visualization

## Rhinoceros (Rhino)
Advanced 3D modeling software with strong curved geometry support.

### Common Uses
- freeform architectural design
- curved structures
- computational design workflows

### Mathematical Concepts
- NURBS geometry
- parametric curves
- surfaces
- topology

## Grasshopper
Parametric design plugin for Rhino.

### Common Uses
- procedural modeling
- generative architecture
- optimization workflows

### Mathematical Concepts
- algorithms
- vectors
- graph logic
- parametric equations
- transformations

## Advanced Visualization Software

### Examples
- Blender
- Maya
- 3DS Max
- Cinema 4D
- ZBrush

### Common Uses
- architectural visualization
- animation
- photorealistic rendering
- VR/AR visualization

### Mathematical Concepts
- lighting models
- transformations
- perspective projection
- mesh construction

# Page 3 — BIM & Technical Documentation

## Building Information Modeling (BIM)

### Major Software
- Revit
- ArchiCAD
- VectorWorks

### Common Uses
- integrated building systems
- construction coordination
- structural planning
- collaborative workflows

### Mathematical Concepts
- parametric relationships
- constraints
- geometry
- topology
- coordinate mapping

## Construction Documentation

### Common Tasks
- dimensioning
- section drawings
- elevation drawings
- site layouts

### Mathematical Concepts
- geometric precision
- ratios
- scale conversions
- tolerances

# Page 4 — Rendering & Visualization

## Raytracing Renderers

### Examples
- Vray
- Corona
- Maxwell
- Cycles

### Common Uses
- photorealistic rendering
- lighting simulation
- material visualization

### Mathematical Concepts
- ray tracing
- vectors
- light transport
- reflections
- probability sampling

## Real-Time Renderers

### Examples
- Enscape
- Lumion
- Twinmotion
- Eevee

### Common Uses
- real-time walkthroughs
- rapid visualization
- VR/AR experiences

### Mathematical Concepts
- rasterization
- real-time lighting
- spatial rendering
- camera projection

# Page 5 — Mathematical Thinking in Architecture

## Geometry
Used in:
- floor plans
- structural layouts
- spatial organization
- curved forms

## Trigonometry
Used in:
- roof angles
- perspective construction
- surveying
- structural orientation

## Topology
Used in:
- spatial connectivity
- circulation design
- parametric modeling
- surface continuity

## Calculus & Optimization
Appears indirectly in:
- structural optimization
- environmental simulation
- parametric workflows
- computational design systems

## Important Insight

Architecture uses mathematics constantly, but usually through:
- spatial reasoning
- visual systems
- geometric relationships
- software-driven modeling

rather than through long manual calculations.


# Architecture Pathway Concepts

1. **Technical Drafting & Construction Drawings**
 - AutoCAD
 - Floor plans
 - Blueprint design
 - Dimensions and scaling
 - Orthographic projection
 - Precision geometry

2. **3D Modeling & Spatial Design**
 - SketchUp
 - Rhinoceros (Rhino)
 - Curved geometry
 - Spatial reasoning
 - Mesh construction
 - Parametric modeling with Grasshopper

3. **Building Information Modeling (BIM)**
 - Revit
 - ArchiCAD
 - Digital building systems
 - Structural coordination
 - Construction workflow integration
 - Data-driven architecture

4. **Architectural Visualization & Rendering**
 - Vray
 - Lumion
 - Twinmotion
 - Photorealistic rendering
 - Lighting and materials
 - Real-time visualization
 - AR/VR architectural environments

5. **Interior Design**