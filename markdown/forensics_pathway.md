<!--
title: "Math in Forensics"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

<img
src="markdown/pathway_images/forensics_photo_1.jpeg"
alt="Placeholder Text"
class="pathway-image"
/>

<div class="pathway-title-overlay">
<h1 class="pathway-title">
Forensics
</h1>
</div>

</div>

<br>

### What will I be doing?

- Collecting and preserving biological, chemical, digital, and physical evidence using standardized forensic procedures
- Processing DNA samples using PCR amplification, electrophoresis, and forensic DNA analysis systems
- Analyzing fingerprints, ballistic evidence, toxicology reports, and trace materials using comparison microscopes, spectrometers, and specialized forensic lab equipment
- Using forensic imaging and 3D reconstruction software such as FARO Zone and Autodesk tools to document and analyze crime scenes
- Applying digital forensics tools such as EnCase, FTK (Forensic Toolkit), Autopsy, and Wireshark to recover and analyze electronic evidence, metadata, and network activity
- Using databases such as AFIS and CODIS to identify fingerprint and DNA matches
- Interpreting laboratory and investigative findings to support criminal investigations and legal proceedings


<br>

### What are the most common jobs?

- Forensic Scientist
- Crime Scene Investigator (CSI)
- Forensic Analyst
- Digital Forensics Specialist
- Forensic Toxicologist
- Forensic Pathologist
- Forensic Biologist
- Forensic Laboratory Technician


<br>

### What math concepts do I need to know?

- Statistics
- Probability
- Data Analysis
- Algebra
- Geometry
- Measurement and Scaling
- Pattern Recognition
- Error Analysis
- Graphing and Trends


--- PAGE ---

## Crime Scene Investigation & Reconstruction

Crime scene investigation forms the foundational stage of forensic analysis, focusing on the systematic collection, preservation, and spatial interpretation of physical evidence. The goal is to reconstruct the sequence of events that occurred at a scene while maintaining the integrity and admissibility of all collected data.

<br>

### Evidence Documentation and Preservation

Accurate documentation ensures that physical reality is preserved in a reproducible form for later analysis.

- Crime scene photography from multiple perspectives
- Sketching and digital scene mapping
- Evidence labeling and cataloging
- Chain of custody tracking to maintain legal integrity
- Contamination prevention through controlled access protocols

Key principle:
- Every item of evidence must be traceable from discovery to courtroom presentation

<br>

### Spatial Mapping and Reconstruction

Crime scene reconstruction relies heavily on spatial relationships between objects, people, and physical traces.

Techniques include:
- Measurement-based scene diagrams
- 3D scanning and reconstruction models
- Geometric triangulation of evidence positions

A fundamental tool is distance calculation between points in a coordinate system:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

Where:
- $d$ = distance between two evidence points
- $(x_1, y_1), (x_2, y_2)$ = spatial coordinates

This allows investigators to reconstruct relative positioning and movement patterns within a scene.

<br>

### Event Sequencing and Temporal Reconstruction

Once spatial structure is established, investigators infer the order and timing of events.

A basic relationship between distance, time, and velocity is given by:

$$
t = \frac{d}{v}
$$

Where:
- $t$ = estimated time interval
- $d$ = distance traveled between evidence points
- $v$ = estimated velocity of movement

This relationship is used in:
- Movement reconstruction
- Trajectory estimation
- Determining plausible sequences of actions

<br>

### Key Principles of Reconstruction

Crime scene reconstruction integrates physical, spatial, and temporal information into a coherent model of events.

- **Spatial relationships** determine where events occurred
- **Temporal ordering** determines when events occurred
- **Physical constraints** determine how events could have occurred

Together, these constraints form a bounded reconstruction space in which only physically and geometrically consistent explanations are considered valid.


--- PAGE ---

## Time of Death Estimation

Time of death estimation—also referred to as postmortem interval (PMI) estimation—combines physiological, chemical, and environmental indicators to approximate the time elapsed since death. Because decomposition is influenced by multiple interacting variables (temperature, humidity, body composition, and environment), PMI is typically expressed as a range rather than a precise value.

Core methods include:
- Algor mortis (body cooling)
- Rigor mortis (muscle stiffening and relaxation)
- Livor mortis (blood settling)
- Biochemical and entomological indicators (later-stage decomposition)

<br>

### Body Cooling

After death, the body gradually equilibrates with ambient temperature. This cooling process is often approximated using Newton’s Law of Cooling:

$$
T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}
$$

Where:
- $T(t)$ = body temperature at time $t$
- $T_{\text{env}}$ = ambient temperature
- $T_0$ = initial body temperature (≈ 37°C)
- $k$ = cooling constant (environment-dependent)
- $t$ = time since death

A simplified forensic approximation sometimes used in early estimation is:

$$
\Delta T \approx 1.5^\circ \text{C per hour (initial phase)}
$$

Used in the following cases:
- When the body is discovered within the first ~24 hours after death
- When ambient temperature conditions are known or can be estimated
- When no advanced decomposition indicators are yet present
- When a rapid preliminary PMI estimate is required at the scene

<br>

### Rigor Mortis

Rigor mortis describes the biochemical stiffening of muscles due to ATP depletion. It follows a predictable but environment-sensitive timeline:

A simplified stage model:

$$
R(t) =
\begin{cases}
0 & t < 2 \text{ hours (onset phase)} \\
1 & 2 \leq t \leq 12 \text{ hours (peak rigidity)} \\
0 & t > 24 \text{ hours (resolution phase)}
\end{cases}
$$

Where:
- $R(t)$ = qualitative rigor state

Used in the following cases:
- When estimating PMI within ~2–36 hours after death
- When the body shows measurable muscle stiffness or relaxation
- When combined with algor mortis for cross-validation
- When environmental temperature has not severely disrupted decomposition timing

<br>

### Livor Mortis

Livor mortis refers to gravitational pooling of blood after circulation ceases. Its development provides timing constraints based on fixation and color changes.

A simplified interpretive relationship:

$$
L(t) \propto \text{degree of fixation over time}
$$

Where livor progresses from:
- Unfixed (movable under pressure)
- Partially fixed
- Fully fixed (non-blanching)

Used in the following cases:
- When determining whether body position has been altered postmortem
- When estimating PMI within the first 6–12 hours
- When assessing consistency between body position and livor distribution
- When corroborating rigor and temperature-based estimates

<br>

### Integrated Postmortem Interval Estimation

In practice, PMI is estimated by combining multiple independent indicators into a constrained range:

$$
PMI \approx f(T_{\text{body}}, R(t), L(t), E, H)
$$

Where:
- $T_{\text{body}}$ = measured body temperature
- $R(t)$ = rigor mortis stage
- $L(t)$ = livor mortis stage
- $E$ = environmental conditions
- $H$ = humidity and exposure factors

Used in the following cases:
- When multiple physiological indicators are available simultaneously
- When a defensible court-admissible time range is required
- When environmental conditions significantly affect single-method estimates
- When reconstructing event timelines in forensic investigations

<br>

### Forensic Entomology

In addition to temperature- and physiology-based methods, insect activity provides a highly reliable biological clock in medium to late postmortem intervals. Forensic entomology is based on the predictable colonization of a body by insects, particularly flies and beetles, whose life cycles progress at known temperature-dependent rates.

The first organisms to arrive are typically **blowflies (Calliphoridae)**, which can detect and colonize a body within minutes to hours after death. They lay eggs in natural openings or wounds, which hatch into larvae (maggots). These larvae progress through distinct developmental stages:

- **Egg stage**: deposited shortly after death under favorable conditions
- **Larval stages (instars)**: multiple feeding stages where maggots consume tissue
- **Pupal stage**: transformation phase, often in soil or nearby sheltered areas
- **Adult emergence**: flies leave the body environment

Other commonly observed groups include:
- **Flesh flies (Sarcophagidae)**: often deposit live larvae rather than eggs
- **Beetles (Dermestidae, Histeridae)**: arrive later in decomposition and feed on dried tissues
- **Mites and parasitoid wasps**: appear in later stages and can indicate extended postmortem intervals

Because insect development is strongly temperature-dependent, the species present and their developmental stage allow investigators to estimate how long colonization has been occurring. This is particularly useful when:
- Traditional physiological indicators (rigor, livor, temperature) are no longer reliable
- The body has been exposed long enough for active decomposition or skeletonization
- Environmental conditions have altered soft-tissue-based time estimates

In practice, forensic entomologists estimate the time since colonization by identifying:
- The **species present**
- The **developmental stage (egg, larva, pupa, adult)**
- The **ambient temperature history of the environment**

This produces a biologically grounded estimate of minimum postmortem interval, often expressed as the time since insect colonization, which typically follows but does not always equal the exact time of death.


--- PAGE ---

## Bloodstain Pattern Analysis & Forensic Physics

Bloodstain pattern analysis applies principles of fluid dynamics and classical mechanics to reconstruct events involving bloodshed. By analyzing the shape, distribution, and spatial arrangement of bloodstains, investigators can infer the direction, velocity, and nature of forces involved in an incident.

<br>

### Bloodstain Pattern Types

Different physical mechanisms produce distinct stain patterns:

- **Impact spatter**: Created when force is applied to a blood source (e.g., blunt force trauma)
- **Passive patterns**: Result from gravity-driven flow or dripping
- **Cast-off patterns**: Produced by blood flung from a moving object
- **Arterial patterns**: Caused by pressurized blood release from arteries

Each pattern encodes information about motion, force, and position at the time of the event.

<br>

### Directionality and Geometric Reconstruction

Bloodstains are often elliptical due to angular impact with a surface. The shape encodes the angle of impact:

$$
\theta = \sin^{-1}\left(\frac{w}{l}\right)
$$

Where:
- $w$ = width of the stain
- $l$ = length of the stain
- $\theta$ = angle of impact relative to the surface

This relationship allows investigators to reconstruct the direction of travel of blood droplets, forming the basis for convergence and origin mapping.

<br>

### Trajectory and Area of Origin

By combining multiple stains with known angles of impact, investigators can reconstruct the three-dimensional area of origin.

Key concept:
- Each stain defines a spatial vector in 3D space
- Intersection of vectors approximates the source location

This transforms flat pattern evidence into volumetric reconstruction.

<br>

### Velocity and Motion Estimation

Basic kinematic relationships are used to approximate motion characteristics of blood droplets and impacting objects.

Velocity estimation:

$$
v = \frac{d}{t}
$$

Where:
- $v$ = velocity
- $d$ = distance traveled
- $t$ = time of travel

This is often combined with trajectory modeling to estimate force magnitude and direction.

<br>

### Gravitational and Vertical Motion Effects

Blood droplets in flight are also influenced by gravity, particularly in passive or airborne patterns. Vertical motion can be approximated using:

$$
y = \frac{1}{2}gt^2
$$

Where:
- $y$ = vertical displacement
- $g$ = gravitational acceleration
- $t$ = time in motion

This relationship is used to refine height-of-origin estimates in reconstruction models.

<br>

### Physical Interpretation

Bloodstain pattern analysis bridges biology and physics by treating biological fluid behavior as a mechanical system governed by:

- Force application and transfer
- Projectile motion dynamics
- Gravitational acceleration
- Surface interaction geometry


--- PAGE ---

## Ballistics & Firearm Investigation

Study of firearms, projectiles, and impact behavior, using classical mechanics to reconstruct firing events and trajectories.

- Trajectory analysis
- Firearm identification
- Bullet striation comparison
- Gunshot residue (GSR) testing
- Internal, external, and terminal ballistics
- Ballistic comparison systems

<br>

### Linear Momentum

A projectile’s motion is governed by conservation of momentum, which links mass and velocity.

$$
p = mv
\quad,\quad
KE = \frac{1}{2}mv^2
$$

Where:
- $p$ = linear momentum
- $m$ = mass of projectile
- $v$ = velocity
- $KE$ = kinetic energy

<br>

### Projectile Motion Trajectory

This equation models the curved flight path of a projectile under gravity, assuming no air resistance.

$$
y = x\tan\theta - \frac{gx^2}{2v_0^2\cos^2\theta}
$$

Where:
- $x, y$ = spatial coordinates of projectile path
- $\theta$ = launch angle
- $v_0$ = initial velocity
- $g$ = gravitational acceleration

<br>

### Impulse–Momentum Relationship

Impulse describes how a force applied over time changes an object’s momentum.

$$
F\Delta t = \Delta p
$$

Where:
- $F$ = applied force
- $\Delta t$ = time interval of force application
- $\Delta p$ = change in momentum

<br>

### Kinematic Deceleration

This relation estimates acceleration during penetration or stopping over a known distance.

$$
a = \frac{v^2 - v_0^2}{2d}
$$

Where:
- $a$ = constant acceleration (or deceleration)
- $v_0$ = initial velocity
- $v$ = final velocity
- $d$ = stopping distance
- Energy–work relationship in ballistic impact

<br>

### Work–Energy Relationship

This connects force and displacement to the change in kinetic energy during impact.

$$
W = Fd = \Delta KE
$$

Where:
- $W$ = work done during impact
- $F$ = average impact force
- $d$ = penetration or stopping distance
- $\Delta KE$ = change in kinetic energy

<br>

### Applications in Forensic Ballistics

These models support reconstruction and identification tasks in forensic analysis.

- Shooter position estimation
- Weapon matching and caliber estimation
- Impact reconstruction and penetration analysis


--- PAGE ---

## DNA Analysis

DNA analysis in forensic science is best understood as a pipeline of specialized laboratory techniques, each contributing a different layer of mathematical interpretation. Rather than a single statistical model, DNA evidence is built from measurement, amplification, pattern matching, and probabilistic comparison.

<br>

### Polymerase Chain Reaction (PCR)

PCR (Polymerase Chain Reaction) is used to amplify small amounts of DNA into measurable quantities.

Mathematically, PCR is modeled as exponential growth:

$$
N = N_0 (1 + E)^n
$$

Where:
- $N_0$ = initial DNA quantity
- $E$ = amplification efficiency
- $n$ = number of cycles
- $N$ = final DNA quantity

Used when:
- DNA quantity is too low for direct analysis
- Samples are degraded or fragmented
- Trace biological material must be amplified before profiling
- Preparing samples for STR or sequencing workflows

<br>

### Short Tandem Repeat (STR) Analysis

STR analysis is the primary method of forensic DNA profiling and focuses on highly variable repeating regions of DNA. It is used when sufficient, relatively intact biological material is available for comparison against known individuals or databases.

Used when:
- A standard biological sample is available with sufficient DNA quality
- Blood, saliva, semen, or fresh tissue is recovered at a scene
- Investigators expect relatively intact nuclear DNA
- Generating routine forensic DNA profiles for identification
- Comparing evidence samples against known suspects or DNA databases (e.g., CODIS-style systems)

<br>

### Touch DNA

Touch DNA refers to trace genetic material left behind through contact, often consisting of very small and degraded amounts of DNA. It is commonly encountered when no visible biological fluids are present and is highly sensitive to contamination and interpretation uncertainty.

Used when:
- Only trace contact material is present
- No visible biological fluid can be recovered
- objects are believed to have been handled by a suspect (e.g., weapons, tools, clothing)
- Investigators are testing indirect transfer of biological material
- Reconstructing contact-based interactions at a scene

<br>

### Genetic Sequencing

Genetic sequencing determines the exact order of nucleotides in a DNA sample and is used when standard STR analysis is insufficient. It is especially valuable for highly degraded samples or complex mixtures requiring higher resolution.

Used in the following cases:
- STR analysis is inconclusive or yields partial profiles
- DNA is highly degraded (e.g., fire exposure, decomposition, environmental damage)
- complex mixtures cannot be separated using standard STR methods
- Unidentified remains require maximum genetic resolution
- High-resolution identification is required beyond standard forensic profiling

<br>

### Population Frequency Estimation

Population frequency estimation determines how common a DNA profile is within a relevant population group. It is used to translate a DNA match into a measurable weight of evidence rather than a simple match/non-match conclusion.

Used in the following cases:
- After a DNA profile has been successfully generated and verified
- Reporting DNA results in legal or courtroom contexts
- Quantifying the strength or rarity of a genetic match
- Comparing evidence profiles against population databases
- Translating a genetic match into probabilistic evidentiary weight rather than a binary conclusion

--- PAGE ---

## Toxicology & Laboratory Analytical Science

Toxicology applies chemical measurement and analytical instrumentation to identify, quantify, and interpret substances relevant to forensic investigations. It combines principles of chemistry, biology, and statistical interpretation to determine exposure, impairment, or cause of death.

- Toxicology screening
- Drug and alcohol testing
- Chromatography techniques
- Spectroscopy methods
- Microscopy analysis
- Chemical residue detection
- Laboratory information systems (LIMS)

Key concepts:
- Concentration measurement
- Substance identification
- Dose-response relationships
- Signal interpretation in chemical analysis
- Detection limits and measurement uncertainty

<br>

### Beer–Lambert Law

This relationship allows unknown concentrations to be determined from measured light absorption in spectroscopic analysis.

$$
A = \epsilon c l
$$

Where:
- $A$ = absorbance
- $\epsilon$ = molar absorptivity
- $c$ = concentration
- $l$ = optical path length

Absorbance increases linearly with both concentration and path length under ideal conditions. This linearity is what makes spectrophotometry useful in forensic toxicology, because it allows unknown substance concentrations (such as drugs, poisons, or alcohol metabolites) to be inferred from measured light attenuation. In practice, deviations from linearity may occur at high concentrations due to chemical interactions or instrumental limitations.

<br>

### Absorbance

Absorbance expresses light attenuation on a logarithmic scale, making it especially useful for detecting small changes in low-concentration forensic samples.

$$
A = -\log_{10}(T)
$$

Where:
- $A$ = absorbance
- $T$ = transmittance

Absorbance is a logarithmic measure of how much light is absorbed by a sample. This means that equal increases in absorbance correspond to exponential decreases in transmitted light, which makes the scale particularly sensitive for detecting low concentrations of forensic substances.

<br>

### Transmittance Definition

This connects raw instrument readings (light intensity measurements) to absorbance values used in toxicological quantification.

$$
T = \frac{I}{I_0}
$$

Where:
- $I$ = transmitted light intensity
- $I_0$ = incident light intensity

These relationships are fundamental in spectroscopic toxicology because they allow chemical concentration to be inferred indirectly from how substances interact with light, particularly in drug screening, blood alcohol analysis, and trace compound identification.

<br>

### Concentration from Calibration Curves

In practical forensic laboratory settings, unknown concentrations are often determined using calibration data:

$$
c = \frac{A - b}{m}
$$

Where:
- $A$ = measured absorbance (or instrument signal)
- $m$ = slope of calibration curve
- $b$ = intercept (baseline offset)

<br>

### Signal-to-Noise Ratio

Analytical reliability depends on distinguishing true signal from background noise:

$$
SNR = \frac{\mu_{\text{signal}}}{\sigma_{\text{noise}}}
$$

Where:
- $\mu_{\text{signal}}$ = mean measured signal
- $\sigma_{\text{noise}}$ = standard deviation of noise

Higher SNR values correspond to more reliable detection and identification.

<br>

### Toxicology

Toxicology applies chemical measurement and analytical reasoning to determine the presence, concentration, and physiological impact of substances in biological systems. In forensic contexts, it is used to assess impairment, poisoning, overdose, or drug involvement in cause of death. Unlike simple detection methods, toxicology requires interpretation of how substances behave in the body over time, including metabolism, distribution, and postmortem changes that may alter measured concentrations.

Used when:
- Drugs, alcohol, or poisons are suspected in death or impairment cases
- Multiple substances or interactions (e.g., polydrug exposure) are involved
- Cause of death may involve toxicological factors
- Interpreting postmortem chemical changes (e.g., redistribution)

<br>

### Chromatography

Chromatography is a separation technique used to isolate and identify components in complex chemical mixtures. In forensic science, it is primarily used to detect drugs, toxins, and trace chemical residues in biological and physical evidence.

A key measurable parameter in chromatography is the retention factor:

$$
R_f = \frac{\text{distance traveled by substance}}{\text{distance traveled by solvent front}}
$$

This value helps identify substances by comparing their movement through a medium relative to known standards. Chromatography is especially important because most forensic samples are mixtures rather than pure substances, requiring separation before accurate identification or quantification.

Used when:
- Screening biological samples for unknown or suspected substances
- Separating mixtures of drugs, metabolites, or chemical residues
- Preparing samples for confirmatory laboratory testing

<br>

### Spectroscopy

Spectroscopy is an analytical method used to identify substances based on how they interact with electromagnetic radiation. Different molecules absorb or emit light at specific wavelengths, producing a characteristic spectral signature. In forensic science, spectroscopy is widely used for both qualitative identification and quantitative measurement of substances such as drugs, toxins, and chemical residues.

It is often used as a confirmatory technique following separation methods like chromatography, ensuring that both the identity and concentration of a substance are reliably determined.

Used when:
- Confirming or quantifying drugs or poisons after initial screening
- Analyzing or comparing chemical residues and unknown substances
- Validating results from preliminary toxicology tests


--- PAGE ---

## Cross-Cutting Statistical & Computational Methods

These methods provide the quantitative foundation for evaluating forensic evidence across all domains. The focus is not only on probability manipulation, but on how probabilities are *constructed from observed data*, including laboratory performance, test validation, and empirical error measurement.

<br>

### Empirical Probability and Evidence Frequency

In forensic contexts, probabilities are typically derived from observed counts in datasets:

$$
P(E) = \frac{\text{number of occurrences of } E}{\text{total observations}}
$$

Where:
- $E$ = observed evidence event

This is the foundational step that connects raw forensic data to probabilistic reasoning.

<br>

### Sensitivity and Specificity

Forensic tests (DNA tests, toxicology screens, fingerprint systems) are evaluated using controlled validation data.

**Sensitivity (true positive rate):**

$$
\text{Sensitivity} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
$$

**Specificity (true negative rate):**

$$
\text{Specificity} = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Positives}}
$$

These quantities directly determine how often a forensic method will correctly identify or correctly reject a match.

<br>

### False Positive and False Negative Rates

Error rates are central in legal interpretation:

$$
\text{False Positive Rate} = \frac{\text{False Positives}}{\text{False Positives} + \text{True Negatives}}
$$

$$
\text{False Negative Rate} = \frac{\text{False Negatives}}{\text{False Negatives} + \text{True Positives}}
$$

These values are *empirically measured*, not assumed, and come from laboratory validation studies.

<br>

### Predictive Values

These are often more legally relevant than raw error rates.

**Positive Predictive Value (PPV):**

$$
PPV = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
$$

**Negative Predictive Value (NPV):**

$$
NPV = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Negatives}}
$$

These depend on both test performance *and base rates in the population*.

<br>

### Likelihood Ratios

Likelihood ratios quantify how much a piece of evidence shifts support between two competing hypotheses:

$$
LR = \frac{P(E|H_1)}{P(E|H_2)}
$$

Where:
- $H_1$ = prosecution hypothesis
- $H_2$ = defense hypothesis

Unlike Bayesian posterior probability, likelihood ratios focus on *evidence strength derived from measured frequencies*.

<br>

### Base Rate Incorporation

Many forensic misinterpretations occur when ignoring base rates:

$$
P(H|E) \propto P(E|H)\cdot P(H)
$$

Where:
- $P(H)$ = prior probability derived from population frequency or case context
- $P(E|H)$ = empirically measured likelihood from validation data

This explicitly separates:
- what is observed in controlled testing
- what is expected in the real population

<br>

### Uncertainty Quantification

Forensic measurements always include variability:

$$
\mu \pm \sigma
$$

Where:
- $\mu$ = estimated value (e.g., concentration, match score)
- $\sigma$ = measurement uncertainty

Confidence intervals:

$$
\hat{\theta} \pm z \cdot \frac{\sigma}{\sqrt{n}}
$$

These quantify how stable or repeatable an evidentiary measurement is.

<br>

### Decision Thresholds in Forensic Systems

Many forensic tools operate using thresholds rather than binary logic:

$$
\text{Decision} =
\begin{cases}
\text{Match} & S \geq T \\
\text{No Match} & S < T
\end{cases}
$$

Where:
- $S$ = similarity or likelihood score
- $T$ = decision threshold

Adjusting $T$ directly changes false positive and false negative rates.