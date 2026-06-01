<!-- 
title: "Math in Archaeology"
output: html_document
bibliography: rmarkdown.bib
 -->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/archaeology_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Archaeology
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Scanning landscapes and excavation sites using LiDAR (an active remote sensing technology that uses pulsed laser light to measure precise 3D distances to objects and surfaces) to detect hidden structures and terrain features  
- Mapping excavation areas and spatial relationships using GIS software  
- Reconstructing artifacts and ancient environments using photogrammetry and 3D modeling tools  
- Dating materials and analyzing composition using laboratory instruments such as radiocarbon dating and spectroscopy tools  
- Recording, cataloging, and organizing artifacts and excavation data in structured databases  
- Analyzing artifact distributions and cultural patterns using statistical software  
- Reconstructing historical landscapes and settlement patterns using digital mapping tools and spatial analysis  

<br>

###  What are the most common jobs?
**Technicians** are the most common jobs available for an archaeologist. It is possible to be a field technician, where you would perform work at an archaeological site or a lab technician such as those that perform radiocarbon dating for determining the age of artificacts. Many jobs involve a mixture of both.

<br>

###  What math concepts do I need to know?
- Geographic Information Systems (GIS) 
- Radiocarbon Dating   
- Calculus
- Topology
- Geometry
- Statistics
- Trigonometry  
- Data Analysis  


--- PAGE ---

## Radiocarbon Dating

Radiocarbon dating measures the decay of carbon-14 in organic materials to estimate age. Because carbon-14 decays at a known rate, the remaining amount in a sample can be used to calculate how long it has been since the organism died. This method is widely used for dating materials up to tens of thousands of years old. It is a direct application of exponential decay in real-world analysis.

<br>

###  Carbon Isotopes and the Baseline Assumption

Living organisms continuously exchange carbon with the environment, maintaining an approximately constant ratio of carbon-14 to carbon-12 while alive. When the organism dies, this exchange stops.

At that point:
- Carbon-14 begins to decay
- Carbon-12 remains stable

This creates a measurable imbalance that evolves over time.

<br>

###  Exponential Decay

The decay of carbon-14 follows an exponential function:

$$
N(t) = N_0 e^{-\lambda t}
$$

Where:
- $N(t)$ = amount of carbon-14 remaining at time $t$
- $N_0$ = initial amount of carbon-14 at time of death
- $\lambda$ = decay constant
- $t$ = time elapsed since death

This equation shows that decay is proportional to the current amount present, meaning the process slows down over time in absolute terms but remains constant in relative terms.

<br>

###  Solving for Age

To determine the age of a sample, the equation is rearranged:

- Start from the measured ratio $\frac{N(t)}{N_0}$
- Solve for $t$ using logarithms:

$$
t = \frac{1}{\lambda} \ln\left(\frac{N_0}{N(t)}\right)
$$

This converts a physical measurement into a time estimate.

<br>

###  Half-Life Interpretation

Carbon-14 has a half-life of approximately 5,730 years. This means:

- After 5,730 years, half of the original carbon-14 remains
- After 11,460 years, one quarter remains
- After each additional half-life, the quantity halves again

Mathematically, this follows:

- $N(t) = N_0 \left(\frac{1}{2}\right)^{t / T_{1/2}}$

Where $T_{1/2}$ is the half-life.

<br>

### Calibration and Error Margins

Absolute dating is not exact and always includes some level of uncertainty. One major challenge in Carbon-14 dating is accurately determining how much C14 remains in a sample while also accounting for environmental factors such as atmospheric variation, contamination, and long-term climate effects. Carbon-14 concentration is commonly measured using **Mass Spectrometry**, which can detect extremely small isotope concentrations. However, measurements can still be affected by factors such as sample contamination, equipment calibration issues, uneven sample composition, and human or procedural error during testing.

Because of these uncertainties, estimated ages are typically represented using a confidence interval:

$$CI_{95\%}(t) = [\hat{t} - \Delta t,\ \hat{t} + \Delta t]$$

Where:

- $CI_{95\%}(t)$ = 95% confidence interval for the true age
- $\hat{t}$ = estimated age from measurement
- $\Delta t$ = measurement uncertainty (combined statistical + systematic error)

<br>

### Carbon and Isotope Analysis

Beyond radiocarbon dating, archaeologists use isotope analysis to study diet, migration, and environmental conditions. Different isotopic ratios in bones and materials can reveal information about ancient lifestyles. These methods rely on chemical and mathematical interpretation of measurable data. They extend archaeology into the realm of geochemistry.

<br>

###  Isotopes as Quantitative Signatures

Isotopes are variants of the same element with different neutron counts. In archaeological analysis, the key idea is not their identity but their **ratios**.

A sample may contain isotopes such as:
- Carbon-12 ($^{12}C$)
- Carbon-13 ($^{13}C$)
- Carbon-14 ($^{14}C$)

Instead of absolute counts, scientists analyze ratios like $\frac{^{13}C}{^{12}C}$ or $\frac{^{15}N}{^{14}N}$.

These ratios act like chemical fingerprints of biological and environmental processes.

<br>

###  Ratio Comparison as a Normalization Process

Because raw isotope amounts vary widely, data is standardized:

- Measured ratio vs. standard reference ratio

A common form is the delta notation:

$$
\delta = \frac{R_{\text{sample}} - R_{\text{standard}}}{R_{\text{standard}}}
$$

Where:
- $R_{\text{sample}}$ = isotope ratio in specimen
- $R_{\text{standard}}$ = reference baseline

This transforms raw measurements into comparable values across time and location.

<br>

###  Diet Reconstruction Through Isotope Signatures

Different food sources produce distinct isotope patterns:

- C3 plants (wheat, rice) - lower $^{13}C$ ratios
- C4 plants (maize, sugarcane) - higher $^{13}C$ ratios
- Marine food sources - distinct nitrogen and carbon signatures

Thus, an organism's isotope ratio becomes a weighted mixture:

$$
R_{\text{bone}} \approx w_1 R_{\text{plants}} + w_2 R_{\text{meat}} + w_3 R_{\text{marine}}
$$


--- PAGE ---

## Remote Sensing and Geophysical Methods

Modern archaeology uses remote sensing techniques such as satellite imaging, ground-penetrating radar, and LiDAR to detect buried structures. These tools allow researchers to “see” beneath the surface without excavation. Data is processed computationally to reveal hidden patterns. This introduces physics, signal processing, and spatial modeling into archaeology.

<br>

### Ground-Penetrating Radar and Wave Reflection

Ground-penetrating radar (GPR) is a geophysical imaging technique used to investigate subsurface structures without excavation. It works by transmitting high-frequency electromagnetic pulses into the ground and analyzing the reflected signals that return from boundaries where material properties change.

These reflections occur because different subsurface materials (soil, rock, water, voids, and archaeological features) have different electromagnetic permittivity and conductivity. When a wave encounters such a boundary, part of its energy is reflected back while the remainder continues propagating deeper.

<br>

### Wave propagation in subsurface media

The velocity of electromagnetic waves in a material depends on the material’s dielectric properties:

$$
v = \frac{c}{\sqrt{\epsilon_r}}
$$

Where:

- $v$ = wave velocity in the medium
- $c$ = speed of light in vacuum
- $ϵ_{r}$ = relative permittivity

This relationship is essential for converting radar signal timing into spatial depth estimates.

<br>

### Two-way travel time and depth estimation

GPR measures the time required for a wave to travel to a subsurface boundary and return to the receiver. Depth is computed using:

$$
d = \frac{v t}{2}
$$

Where:

- $d$ = depth
- $v$ = wave velocity
- $t$ = two-way travel time

The division by 2 accounts for the down-and-return propagation path.

<br>

### Reflection coefficient

The amplitude of reflected signals depends on impedance contrast between materials:

$$
R = \frac{Z_2 - Z_1}{Z_2 + Z_1}
$$

Where:

- $R$ = reflection coefficient
- $Z_{1}, Z_{2}$= electromagnetic impedance of the two media

Large contrasts produce strong reflections, often indicating buried walls, voids, or structural changes.

<br>

### Signal attenuation

As electromagnetic waves travel through the ground, their amplitude decreases due to absorption and scattering. This attenuation is commonly modeled exponentially:

$$
A(x) = A_0 e^{-\alpha x}
$$

Where:

- $A(x)$ = amplitude at depth x
- $A_{0}$ = initial amplitude
- $α$ = attenuation coefficient

Attenuation limits penetration depth and affects resolution in GPR surveys.

<br>

### LiDAR and Surface Reconstruction

LiDAR (Light Detection and Ranging) is a remote sensing technology that measures distance by emitting laser pulses and recording their return time after reflection from surfaces. It is widely used in archaeology for high-resolution topographic mapping and three-dimensional reconstruction.

LiDAR produces dense point clouds that represent surface geometry with high spatial accuracy, often capable of penetrating vegetation to reveal hidden terrain features.

<br>

### Time-of-flight distance measurement

LiDAR calculates distance using the time-of-flight principle:

$$
d = \frac{c t}{2}
$$

Where:

- $d$ = distance to target surface
- $c$ = speed of light
- $t$ = round-trip travel time

This provides precise spatial measurements for each laser pulse return.

<br>

### Point cloud generation

Each LiDAR return generates a 3D coordinate:

$$
(x, y, z)
$$

By aggregating millions of returns, LiDAR constructs dense point clouds representing terrain and structures. Spatial relationships within these datasets are analyzed using Euclidean geometry:

$$
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}
$$

These point clouds form the raw input for surface reconstruction and digital terrain modeling.

<br>

### Surface reconstruction from LiDAR data

Point clouds are converted into continuous surfaces using interpolation and triangulation methods.

A common representation of terrain is:

$$
z = f(x, y)
$$

This defines elevation as a continuous function over a spatial domain.

Surface reconstruction algorithms infer geometry from discrete samples, producing meshes suitable for visualization and analysis.

<br>

### Digital terrain models

LiDAR data is used to generate Digital Terrain Models (DTMs), which represent bare-earth surfaces after filtering vegetation and built structures.

DTMs are essential for:

- Detecting subtle archaeological features
- Mapping ancient landscapes
- Hydrological modeling
- Visibility and line-of-sight analysis

These models allow researchers to reconstruct terrain that is no longer visible at ground level.

<br>

### Archaeological applications of LiDAR

In archaeology, LiDAR is particularly powerful because it can reveal hidden structures beneath forest canopy and vegetation.

Applications include:

- Mapping ancient settlements
- Detecting buried architectural remains
- Reconstructing landscape modification
- Analyzing large-scale spatial patterns

By combining high-resolution spatial data with computational reconstruction methods, LiDAR provides one of the most effective tools for modern digital archaeology.


--- PAGE ---

## Other Techniques in Archaeological Dating

There are three remining common techniques used in archaeological dating:

1. Dendrochronology
2. Thermoluminescence (TL)
3. Optically Stimulated Luminescence (OSL)

<br>

### Dendrochronology

Dendrochronology is the scientific method of dating based on the analysis of patterns of tree-ring growth. Because trees typically produce one growth ring per year, their internal structure preserves a chronological record of environmental conditions such as temperature, precipitation, and soil moisture. This makes dendrochronology one of the most precise absolute dating methods in archaeology, often achieving annual resolution.

1. **Tree-Ring Growth Analysis**  
    Annual ring widths vary according to environmental conditions such as temperature, rainfall, and drought. Wider rings generally indicate favorable growth conditions, while narrower rings indicate environmental stress. Ring measurements are often standardized into growth indices:

$$
I_t = \frac{R_t}{\overline{R_t}}
$$

> Where:
> - $I_t$ = standardized growth index at time $t$
> - $R_t$ = measured ring width at time $t$
> - $\overline{R_t}$ = average ring width over the reference period

> This normalization reduces long-term biological growth trends and helps isolate environmental signals preserved within the tree-ring record.

<br>

2. **Cross-Dating and Sequence Matching**  
    Ring-width patterns from different trees are aligned to establish accurate chronological sequences. Trees within the same region often display similar growth responses to environmental variation, allowing their growth patterns to be compared statistically. Similarity between sequences is commonly measured using correlation:

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sigma_x \sigma_y}
$$

> Where:
> - $r$ = correlation coefficient
> - $x_i$ = value from the first tree-ring sequence
> - $y_i$ = value from the second tree-ring sequence
> - $\bar{x}$ = mean of the first sequence
> - $\bar{y}$ = mean of the second sequence
> - $\sigma_x$ = standard deviation of the first sequence
> - $\sigma_y$ = standard deviation of the second sequence

> Strong correlations indicate successful alignment and allow tree-ring sequences to be matched with annual precision.

<br>

3. **Master Chronology Construction**  
    Long-term reference chronologies are created by overlapping many individual tree-ring sequences. Each newly aligned sample extends the continuous timeline further into the past. These master chronologies serve as foundational reference systems for archaeological dating, paleoclimate reconstruction, and calibration of other chronological methods.

<br>

4. **Climatic Signal Extraction**  
    Tree rings preserve environmental and climatic information that can be analyzed to reconstruct past conditions. Statistical and signal-processing methods are used to separate climatic variation from long-term biological growth effects. These reconstructions provide insight into historical drought cycles, temperature variability, and broader long-term climate trends.

<br>

### Thermoluminescence

Thermoluminescence (TL) dating is a method used to determine the last time a mineral sample was heated to a high temperature. It is commonly applied to ceramics, burned stone, and heated sediments. The method is based on the accumulation of trapped electrons in crystal lattice defects caused by natural background radiation.

<br>

1. **Radiation Dose Accumulation**
   Environmental radiation gradually deposits energy into mineral crystals over time. The total accumulated radiation dose increases with elapsed time since the last heating event.

2. **Electron Trapping in Crystal Lattices**
   Imperfections within mineral crystal structures act as electron traps. These trapped electrons remain stable until sufficient thermal energy releases them.

3. **Heat-Induced Signal Reset**
   Heating the material releases trapped electrons, producing visible luminescence. This process effectively resets the thermoluminescence signal to zero. The most recent heating event becomes the starting point for age accumulation.

4. **Luminescence Signal Measurement**
   Reheating in the laboratory releases stored electrons as light. The measured light intensity is proportional to the total accumulated radiation dose. This signal is used to estimate the elapsed time since the last thermal reset.

5. **Age Estimation from Radiation Dose Rates**  
    The age of a sample is determined by comparing the total stored radiation dose with the rate at which radiation accumulates within the surrounding environment. This relationship is expressed as:

$$
t = \frac{D_e}{D_r}
$$

> Where:
> - $t$ = age of the sample  
> - $D_e$ = equivalent dose  
> - $D_r$ = annual dose rate  

> By dividing the total accumulated dose by the environmental dose rate, researchers can estimate the elapsed time since the material was last heated.

<br>

### Optically Stimulated Luminescence (OSL)

Optically Stimulated Luminescence (OSL) is a dating method used to determine the last time mineral grains, typically quartz or feldspar, were exposed to sunlight. It is especially useful for dating buried sediments in archaeological and geological contexts. The following techniques are methods used for OSL dating:

1. **Light-Sensitive Electron Trapping**
   Environmental radiation causes electrons to become trapped within mineral crystal defects. Unlike thermoluminescence, OSL signals are reset primarily through light exposure rather than heat.

2. **Signal Reset During Sediment Transport**
   Sunlight exposure during erosion, transport, and deposition releases trapped electrons. Burial marks the beginning of age accumulation once light exposure is removed.

3. **Burial Age Accumulation**
   After burial, trapped electrons gradually accumulate again due to surrounding radiation. The total stored luminescence signal reflects the time elapsed since burial.

4. **Quartz and Feldspar Behavior**
   Quartz is commonly preferred because of its relatively stable luminescence properties. Feldspar can also be used but may exhibit more complex signal fading and decay behavior.

5. **Environmental Dose Rate Modeling**
   Accurate age estimation requires calculating the radiation dose absorbed over time. Major radiation sources include cosmic radiation, radioactive decay in surrounding sediments, water content and sediment composition.

6. **OSL Age Determination**  
    The burial age of sediments is determined by comparing the total accumulated radiation dose with the environmental dose rate using the relationship:

$$
t = \frac{D_e}{D_r}
$$

> Where:
> - $t$ = burial age  
> - $D_e$ = equivalent dose  
> - $D_r$ = dose rate  

> This equation forms the foundation of OSL dating by estimating the time elapsed since sediments were last exposed to sunlight prior to burial.


--- PAGE ---

## Digital Archaeology and Reconstruction

Digital archaeology uses computational tools to reconstruct, analyze, and visualize ancient artifacts, structures, and environments in three dimensions. These methods combine geometry, computer vision, spatial analysis, and historical interpretation to recover information from archaeological remains and transform raw observational data into interactive digital models. Modern reconstruction systems rely heavily on photogrammetry, computer graphics, optimization algorithms, and spatial modeling to study sites that may be damaged, incomplete, or inaccessible.

<br>

### 3D Reconstruction and Modeling

3D reconstruction and modeling recover geometric structure, spatial relationships, and surface detail from visual or sensor-based data. Archaeologists use these methods to digitally reconstruct artifacts, buildings, excavation sites, and historical landscapes with high spatial accuracy. Most reconstruction pipelines convert raw image or sensor measurements into structured 3D representations such as point clouds, polygon meshes, and textured surfaces. The mathematical foundation of these systems is based on **projective geometry**, **linear algebra**, **optimization**, and **computational geometry**.

<br>

### Photogrammetry

Photogrammetry reconstructs 3D structure from overlapping 2D images by using multiple viewpoints to infer spatial depth through geometric intersection. A core mathematical relationship is the **perspective projection equation**, which maps 3D world coordinates into 2D image coordinates:

$$
x = f\frac{X}{Z}, \quad y = f\frac{Y}{Z}
$$

Where:
- $X, Y, Z$ are 3D world coordinates
- $x, y$ are image plane coordinates
- $f$ is focal length

Reconstruction accuracy is evaluated using **reprojection error minimization**, which measures the difference between observed and predicted image points:

$$
E = \sum_i \|x_i - \hat{x}_i\|^2
$$

Minimizing this error is central to estimating camera parameters and optimizing 3D structure reconstruction.

<br>

### Structure from Motion (SfM)

Structure from Motion (SfM) reconstructs both 3D structure and camera motion simultaneously from image sequences. These systems rely on **epipolar geometry**, which describes geometric relationships between multiple image views. A central constraint is the **essential matrix equation**:

$$
x'^T E x = 0
$$

Where:
- $E$ is the essential matrix
- $x, x'$ are corresponding image points

Camera orientation is represented using **rotation matrices**, which satisfy the orthogonality condition:

$$
R^T R = I
$$

SfM also uses **homogeneous coordinate transformations** to combine translation and rotation into a single matrix operation:

$$
X' = T X
$$

These transformations form the mathematical basis of multi-view reconstruction pipelines used in archaeological site modeling.

<br>

### Mesh Generation and Surface Reconstruction

Once point clouds are generated, surface reconstruction methods convert discrete spatial points into continuous geometric surfaces. Surface orientation is commonly represented using **surface normals**, calculated from cross products of adjacent vectors:

$$
\mathbf{n} = (\mathbf{v}_2 - \mathbf{v}_1) \times (\mathbf{v}_3 - \mathbf{v}_1)
$$

Mesh refinement and smoothing frequently use **Laplacian smoothing**, which approximates local surface curvature:

$$
\Delta f = \nabla^2 f
$$

These methods reduce noise, improve geometric continuity, and produce visually coherent surfaces suitable for archaeological interpretation and visualization.

<br>

### Texture Mapping

Texture mapping applies 2D image information onto reconstructed 3D surfaces in order to preserve visual realism and material appearance. A central operation is the **affine transformation**, which maps points between coordinate systems:

$$
\mathbf{x}' = A\mathbf{x} + \mathbf{b}
$$

Textures are interpolated across surfaces using **barycentric coordinates**, which express points inside a triangle as weighted combinations of its vertices:

$$
P = \lambda_1 A + \lambda_2 B + \lambda_3 C
$$

These methods ensure smooth, geometrically consistent texture placement across reconstructed archaeological models.

<br>

### Point Clouds and Spatial Geometry

Point clouds are collections of sampled 3D points representing real-world surfaces and structures. They form the foundational geometric data used in most reconstruction systems. Spatial relationships within point clouds are analyzed using the **Euclidean distance formula**:

$$
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}
$$

The geometric center of a point set is described using the **centroid equation**:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

Planar surfaces within point clouds are commonly modeled using the **plane equation**:

$$
Ax + By + Cz + D = 0
$$

These mathematical tools are essential for spatial alignment, segmentation, classification, and structural interpretation of archaeological data.

<br>

### Virtual Reality Archaeology

Virtual reality (VR) archaeology reconstructs historical environments within immersive 3D digital spaces that users can explore interactively. These systems rely heavily on **3D transformation matrices**, which combine scaling, rotation, and translation into unified spatial transformations:

$$
X' = T R S X
$$

VR rendering also depends on **perspective projection**, which simulates human visual perception by projecting 3D environments onto 2D displays. Together, these transformations maintain spatial consistency between user movement and rendered archaeological environments.

<br>

### Augmented Reality Reconstruction

Augmented reality (AR) reconstruction overlays digital archaeological reconstructions onto physical environments in real time. A key mathematical tool in AR systems is the **homography matrix**, which maps planar relationships between image space and world space:

$$
x' = Hx
$$

AR systems also rely on **camera pose estimation**, which determines the position and orientation of the camera relative to the surrounding environment. These techniques allow reconstructed digital objects to align accurately with physical archaeological sites.

<br>

### Interactive Site Visualization

Interactive visualization systems allow users to explore reconstructed archaeological environments dynamically through real-time rendering systems. These platforms rely on **spatial coordinate transformations**, **lighting models**, and **rendering pipelines** to simulate realistic environments and user interaction. A central concept is the **rendering equation**, which describes how light propagates and interacts within a scene to generate visually realistic images.

<br>

### Historical Environment Simulation

Historical environment simulation models how landscapes and archaeological sites evolve over time under environmental and human influences. These systems often use **differential equations** to describe processes such as erosion, vegetation growth, and climate variation. Terrain structure is commonly represented using **height maps**, where elevation is modeled as a spatial function:

$$
z = f(x, y)
$$

These simulations allow archaeologists to reconstruct not only static sites, but also long-term environmental and structural development across historical periods.

<br>

### Digital Museum Environments

Digital museum environments present reconstructed artifacts and archaeological sites within interactive virtual exhibition spaces. These systems rely on **projection geometry** to display 3D objects on 2D screens while preserving spatial relationships and depth perception. They also use **spatial mapping transformations** to organize navigation and object placement within virtual exhibits. Together, these techniques allow archaeological reconstructions to be experienced in accessible, interactive, and educational digital environments.