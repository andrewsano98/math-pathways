<!-- 
title: "Math in Biotechnology"
output: html_document
bibliography: rmarkdown.bib
 -->


<div class="pathway-card">

<img
src="markdown/pathway_images/biotechnology_photo_1.jpeg"
alt="Placeholder Text"
class="pathway-image"
/>

<div class="pathway-title-overlay">
<h1 class="pathway-title">
Biotechnology
</h1>
</div>

</div>

<br>

### What will I be doing?
- Designing and running biological experiments in laboratories to test cells, proteins, or genetic material
- Analyzing DNA, RNA, and protein data using sequencing and bioinformatics tools
- Modeling biological systems and population behaviors using computational biology software
- Running statistical analysis on experimental results to determine significance and reliability
- Culturing and modifying microorganisms or cell lines for research or industrial applications
- Using laboratory instrumentation (PCR machines, centrifuges, spectrometers) to process biological samples
- Interpreting experimental data to develop medical, agricultural, or industrial biotechnologies

<br>

### What are the most common jobs?
- Biotechnologist
- Biomedical Scientist
- Genetic Engineer
- Clinical Research Scientist
- Pharmaceutical Researcher
- Laboratory Technician
- Bioinformatics Analyst
- Quality Control Specialist

<br>

### What math concepts do I need to know?
- Statistics
- Probability
- Algebra
- Calculus
- Data Analysis
- Differential Equations
- Linear Algebra
- Growth Models
- Experimental Design

--- PAGE ---

## Basics of Biology

The most important basic biological concepts to learn in preparation for biological research or the biotech industry can be summed up as the following:

1. The Central Dogma of Biology
2. Enzyme Kinetics
3. Protein Folding & Structure

<br>

Modern biology also relies heavily on statistics, experimental design, thermodynamics, reaction kinetics, and computational modeling.

### Central Dogma

The central dogma of molecular biology describes how hereditary information in  through biological systems:

$$
\text{DNA} \rightarrow \text{RNA} \rightarrow \text{Protein}
$$

This pathway is oversimplified and in practice there are many steps in transcription and translation. There are many forms of DNA, RNA and proteins that make the pathway several steps longer. However, this is a general rule.

<br>

### Enzymes as Biological Catalysts

Enzymes are proteins that accelerate biochemical reactions without being consumed. In biotechnology, they are treated as programmable reaction tools.

Their activity is often modeled using the Michaelis-Menten equation:

$$
v = \frac{V_{max}[S]}{K_m + [S]}
$$

Where:
- $ v $ = reaction rate
- $ [S] $ = substrate concentration
- $ V_{max} $ = maximum rate
- $ K_m $ = substrate affinity constant

This describes how efficiently enzymes convert substrates into products.

### Protein Folding and Structural Prediction

Protein folding is the process by which a linear chain of amino acids (a polypeptide) transforms into a functional three-dimensional structure. This structure determines what the protein does inside a cell—whether it acts as an enzyme, structural component, signaling molecule, or transport agent.

<br>

### Forces Driving Folding

Protein structure is determined by multiple interacting forces:

- Hydrogen bonding
- Hydrophobic interactions
- Electrostatic attraction and repulsion
- Van der Waals forces
- Steric (spatial) constraints

These forces collectively define a high-dimensional energy surface.

<br>

### Structural Levels of Organization

Protein structure is organized hierarchically:

- **Primary structure**: amino acid sequence
- **Secondary structure**: alpha helices, beta sheets
- **Tertiary structure**: full 3D folding
- **Quaternary structure**: multi-protein complexes

Each level emerges from interactions at the previous level.


--- PAGE ---

## Biological Assays & Testing

In the biotech pipeline, a variety of different tests need to be performed, typically to check for the presence and concentration of contaminants that can negatively impact the efficacy of medicine that patients rely on.

There are six primary reasons for testing, but most assays rely on the following equation:

$$
C_{1}V_{1} = C_{2}V_{2}
$$

This is because samples need to be diluted at different concentrations for different tests, and because samples are typically most stable when preserved at a higher concentration.

It is also common to see the following two formulas as a means to assess the quality of the test:

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
$$

Where:
- $SS_{res}$ = residual sum of squares (unexplained variation/error)
- $SS_{tot}$ = total sum of squares (total variation in the data)

$$
CV = \frac{\sigma}{\mu} \times 100\%
$$

Where:
- $CV$ = coefficient of variation
- $\sigma$ = standard deviation
- $\mu$ = mean

Typically, regulation standards expect that the $R^{2}$ value will be greater than $0.98$ and that each $CV$ will be less than some value between $0.10$ or $0.30$, though this can vary depending on the test, company standards, and federal regulations.

Tests generally can be categorized based on six different goals:

1. Presence
2. Quantification
3. Location
4. Interaction
5. Function
6. System-wide State


--- PAGE ---

## Presence

In biotechnology, some biological molecules must be confirmed as absent from a sample, even in trace amounts. This is especially important in quality control of biologically engineered products, where residual DNA, RNA, or host-cell proteins may indicate contamination.

These assays are designed to detect whether a target molecule is present at all, rather than how much is present.

- Detect DNA, RNA, proteins, or other biomolecules  
- Used as a binary validation step in quality control  
- Common in biomanufacturing and purification pipelines  

### DNA Amplification Assays (PCR-based)

DNA and RNA detection often relies on amplification techniques such as:

- PCR (Polymerase Chain Reaction)  
- qPCR (Quantitative PCR)  
- RT-PCR (Reverse Transcription PCR)  

These methods amplify genetic material exponentially:

$$
N(t)=N_0 \cdot 2^t
$$

Where:
- $N_0$ = initial amount of DNA  
- $t$ = number of amplification cycles  

<br>

Gene expression changes in qPCR are commonly calculated using the ΔΔCt method:

$$
\text{Fold Change} = 2^{-\Delta\Delta C_t}
$$

Where:
- $\Delta\Delta C_t$ = difference in threshold cycles between experimental and control conditions  


<br>

### Western Blot

Western blotting detects specific proteins by separating them by size using gel electrophoresis and then identifying them with antibodies.

A key measurement is the migration ratio:

$$
R_f = \frac{\text{Distance traveled by protein}}{\text{Distance traveled by dye front}}
$$

- Larger proteins migrate more slowly  
- Smaller proteins migrate farther  
- Band position identifies protein size  

<br>

### ELISA (Enzyme-Linked Immunosorbent Assay)

ELISA detects soluble proteins or antibodies using enzyme-linked signal amplification. Concentration is determined by comparing signal intensity to a standard curve.

The calibration curve is typically linearized as:

$$
y = mx + b
$$

Where:
- $m = \frac{n\sum xy - (\sum x)(\sum y)}{n\sum x^2 - (\sum x)^2}$
- $b = \frac{\sum y - m\sum x}{n}$

- Signal intensity corresponds to concentration  
- Standards are used for calibration  
- Output is quantified using spectrophotometry  


--- PAGE ---

## Quantity & Concentration

Once the presence of a molecule has been confirmed, the next step is often to determine how much of it is present in a sample. This is essential for comparing experimental conditions, assessing biological activity, and ensuring consistency across batches or treatments.

These assays are designed to measure abundance or concentration in a quantitative way, often translating experimental signals such as absorbance, intensity, or peak area into meaningful numerical values.

- Quantify DNA, RNA, proteins, metabolites, or small molecules  
- Convert experimental signals into concentration estimates  
- Common in drug development, diagnostics, and biochemical analysis

<br>

### Mass Spectrometry

Mass spectrometry identifies molecules by ionizing them and separating them based on mass-to-charge ratio $\frac{m}{z}$.

- Molecules are converted into charged ions  
- Ions are accelerated through electromagnetic fields  
- A detector measures intensity at each m/z value  

Each peak corresponds to a molecular species, and peak height reflects abundance.

<br>

### Cell Viability Assays (MTT/XTT)

The MTT assay measures metabolic activity as a proxy for viable cell number.

$$
A \propto N_{\text{viable}}
$$

- Living cells convert MTT into colored formazan  
- Absorbance increases with viable cell count  
- Used in toxicity and drug screening studies  

Cell survival in viability assays is commonly expressed relative to a control:

$$
\text{Viability} =
\frac{A_{\text{sample}}}{A_{\text{control}}}
\times 100\%
$$

Where:
- $A_{\text{sample}}$ = absorbance of treated sample  
- $A_{\text{control}}$ = absorbance of control (untreated cells) 

<br>

### Spectrophotometry

Spectrophotometry measures light absorption to estimate molecular concentration.

- DNA/RNA quantification  
- Protein concentration measurement  
- Enzyme activity tracking  

A foundational relationship in spectrophotometric analysis is the Beer-Lambert Law, which links light absorbance to concentration:

$$
A = \varepsilon lc
$$

Where:
- $A$ = absorbance  
- $\varepsilon$ = molar absorptivity  
- $l$ = path length  
- $c$ = concentration

<br>

### HPLC (High-Performance Liquid Chromatography)

HPLC separates chemical mixtures into individual components using liquid-phase chromatography.

- Components are separated based on chemical interactions with the column  
- Output is a chromatogram with distinct peaks  
- Each peak corresponds to a molecular species  

In chromatography, the **retention factor** describes how long a compound is retained in the column relative to an unretained species:

$$
k' = \frac{t_R - t_0}{t_0}
$$

Where:
- $t_R$ = retention time of the analyte  
- $t_0$ = dead time (time for unretained species) 


--- PAGE ---

## Location & Spatial Structure

Cellular function is not determined solely by which molecules are present, but also by where those molecules are located within the cell. Eukaryotic cells are highly compartmentalized, and this spatial organization plays a critical role in regulating biochemical activity. The study of this spatial organization is referred to as subcellular localization.

At a physical level, spatial patterns within cells can often be described using concentration fields that vary over space and time. For example, diffusion processes help determine how molecules spread within intracellular environments:

$$
C(x,t) = \frac{1}{\sqrt{4\pi Dt}} e^{-\frac{x^2}{4Dt}}
$$

Where:
- $C(x,t)$ represents concentration at position $x$ and time $t$
- $D$ is the diffusion coefficient

This type of relationship helps explain why molecular signals form gradients rather than remaining uniformly distributed.

Common intracellular locations include key functional regions of the cell, each associated with distinct biological roles:

- Nucleus  
- Mitochondria  
- Cell membrane  
- Endoplasmic reticulum  
- Lysosomes and vesicles  
- Cytoskeleton and cytosol  

<br>

### Fluorescence In Situ Hybridization (FISH)

Fluorescence In Situ Hybridization (FISH) is a molecular technique used to detect and localize specific DNA or RNA sequences within fixed cells. It relies on fluorescent probes that bind to complementary genetic sequences, allowing researchers to visualize spatial patterns of gene presence.

The observed fluorescence signal can be modeled as a function of local target concentration:

$$
I(x,y) = \alpha C(x,y) + \beta
$$

Where:
- $I(x,y)$ is the measured fluorescence intensity
- $C(x,y)$ is the local concentration of the target sequence
- $\alpha$ represents signal scaling
- $\beta$ represents background fluorescence

- Probes bind complementary nucleic acid sequences  
- Fluorescent signals indicate the physical location of target genes  
- Commonly used to map chromosomal regions and detect genetic abnormalities  

<br>

### Immunofluorescence (IF)

Immunofluorescence (IF) is a technique used to detect and localize specific proteins within cells using antibodies tagged with fluorescent markers. It allows both spatial and quantitative analysis of protein distribution.

Fluorescence intensity in these systems often follows a saturation relationship with respect to antigen concentration:

$$
S = \frac{S_{\max}[A]}{K_d + [A]}
$$

Where:
- $S$ is measured signal intensity
- $[A]$ is antigen concentration
- $K_d$ is the dissociation constant

- Antibodies bind specifically to target proteins  
- Fluorescence indicates protein localization and relative abundance  
- Enables visualization of protein distribution within cellular compartments  

<br>

### Microscopy

Microscopy encompasses a range of imaging techniques used to observe cellular and subcellular structures that are not visible to the naked eye. Most imaging methods produce two-dimensional projections of inherently three-dimensional biological structures.

A simplified representation of this projection process is:

$$
\text{Image}(x,y) = \int \rho(x,y,z)\,dz
$$

Where:
- $\rho(x,y,z)$ represents the 3D density of the sample
- The integral represents projection along the optical axis

Different microscopy methods provide different levels of resolution and contrast depending on the biological question being studied.

- Brightfield microscopy: used for general visualization of cell morphology  
- Fluorescence microscopy: visualizes labeled molecules and cellular components  
- Electron microscopy: provides high-resolution images of ultrastructural detail  

<br>

### Cryo-EM and X-ray Crystallography

Cryo-electron microscopy (cryo-EM) and X-ray crystallography are high-resolution structural biology techniques used to determine the three-dimensional arrangement of biomolecules at near-atomic resolution. These methods reconstruct molecular structure from measured physical signals.

In diffraction-based methods such as X-ray crystallography, the measured intensity is related to the Fourier transform of the electron density:

$$
I(\mathbf{q}) \propto |\mathcal{F}[\rho(\mathbf{r})]|^2
$$

Where:
- $\rho(\mathbf{r})$ is the electron density of the molecule
- $\mathcal{F}$ denotes the Fourier transform
- $I(\mathbf{q})$ is the measured diffraction intensity

- Cryo-EM: images rapidly frozen samples using electron beams to reconstruct 3D structures  
- X-ray crystallography: analyzes diffraction patterns from crystallized molecules to infer atomic structure  
- Both methods enable detailed reconstruction of protein and macromolecular structures


--- PAGE ---

## Interaction

Interaction assays investigate how biological molecules physically or functionally influence one another within a system. These interactions form the basis of signaling pathways, immune recognition, and drug binding, and they are essential for understanding how biological processes are coordinated at the molecular level. In experimental biology, interaction studies are primarily concerned with identifying whether binding occurs, how strongly it occurs, and how dynamic that binding is over time.

- Detect protein–protein, protein–DNA, or protein–ligand interactions  
- Quantify binding strength, affinity, and kinetic behavior  
- Applied in drug discovery, signaling analysis, and structural biology  

<br>

### Co-Immunoprecipitation (Co-IP)

Co-immunoprecipitation is an experimental technique used to identify protein–protein interactions by using antibodies to isolate a target protein along with any proteins bound to it. The presence of co-precipitated proteins provides evidence of a physical interaction within a cellular environment.

- Identifies protein complexes in biological samples  
- Uses antibody-based precipitation of target proteins  
- Commonly applied in pathway and network analysis  

<br>

### Surface Plasmon Resonance (SPR)

Surface plasmon resonance is a real-time, label-free method for measuring molecular binding interactions. It models interactions as a reversible chemical equilibrium:

$$
A + B \rightleftharpoons AB
$$

SPR allows direct observation of association and dissociation processes, enabling the extraction of kinetic parameters such as binding rates and equilibrium behavior.

Binding strength is commonly summarized using the dissociation constant:

$$
K_D = \frac{[A][B]}{[AB]}
$$

Where:
- $K_D$ represents the equilibrium dissociation constant  
- $[A]$ and $[B]$ are the concentrations of unbound binding partners  
- $[AB]$ is the concentration of the bound complex  

Lower values of $K_D$ correspond to stronger molecular binding.

<br>

### Yeast Two-Hybrid Assay

The yeast two-hybrid system detects protein–protein interactions in vivo by linking binding events to the activation of a reporter gene. When two proteins interact, they bring together transcriptional components that trigger measurable gene expression.

- Detects interactions within living cells  
- Uses reporter gene activation as a readout  
- Useful for mapping interaction networks  

<br>

### Binding Affinity Assays

Binding affinity assays quantify the strength of interaction between molecular partners. These methods are widely used in pharmacology and receptor biology to evaluate how tightly a drug or ligand binds to its target.

- Measure equilibrium binding strength  
- Used to compare candidate drug molecules  
- Inform dose and efficacy relationships  


--- PAGE ---

## Function

Functional assays are used to evaluate how biological systems respond to specific perturbations such as drugs, genetic modifications, or environmental changes. Unlike structural or compositional assays, which describe what is present in a system, functional assays focus on what the system does under controlled conditions. These measurements are essential for linking molecular interventions to physiological or cellular outcomes.

- Quantify changes in biological activity following experimental manipulation  
- Assess gene function, drug efficacy, and cellular response dynamics  
- Widely used in pharmacology, genetics, and systems biology  

<br>

### CRISPR Gene Editing

CRISPR-Cas systems enable precise, targeted modification of genetic material, allowing researchers to directly investigate the functional role of specific genes. By comparing edited and unedited systems, the resulting change in phenotype or activity can be quantified.

A common way to express the functional effect of editing is:

$$
\Delta P = P_{\text{edited}} - P_{\text{control}}
$$

Where:
- $P_{\text{edited}}$ represents the measured outcome after genetic modification  
- $P_{\text{control}}$ represents the baseline (unmodified) system  

- Enables gene knockout and knock-in experiments  
- Used to determine gene function and regulatory roles  
- Central tool in synthetic and molecular biology  

<br>

### Drug Response Assays

Drug response assays characterize how biological systems react to varying concentrations of a compound. These responses are typically modeled using dose–response relationships, which capture both potency and maximal effect:

$$
E(d)=\frac{E_{\max}d^n}{EC_{50}^n+d^n}
$$

Where:
- $E(d)$ = observed effect at dose $d$  
- $E_{\max}$ = maximum achievable effect  
- $EC_{50}$ = dose producing half-maximal response  
- $n$ = Hill coefficient (response steepness)  

- Used to quantify drug potency and efficacy  
- Produces sigmoidal dose–response curves  
- Fundamental in pharmacology and toxicology  

<br>

### Electrophysiology

Electrophysiology measures electrical activity in biological systems by recording voltage changes over time. These measurements are used to study how cells such as neurons and cardiomyocytes communicate and respond to stimuli.

Electrical behavior in simple biological systems can be described using Ohm’s Law:

$$
I = \frac{V}{R}
$$

Where:
- $I$ = current  
- $V$ = voltage  
- $R$ = resistance  

- Records membrane potentials and signaling activity  
- Central to neuroscience and cardiac physiology  
- Used to study excitability and signal transmission  

<br>

### Enzyme Activity Assays

Enzyme activity assays measure the rate at which enzymes catalyze biochemical reactions. Reaction velocity depends on enzyme concentration, substrate availability, and reaction conditions.

A simplified rate relationship is given by:

$$
v = k[E][S]
$$

Where:
- $v$ = reaction velocity  
- $E$ = enzyme concentration  
- $S$ = substrate concentration  
- $k$ = rate constant  

- Quantifies catalytic efficiency  
- Tracks substrate conversion over time  
- Used in metabolism and biochemical pathway analysis  

<br>

### Toxicology Testing

Toxicology testing evaluates the harmful effects of chemical compounds on biological systems. These assays are used to determine both the presence and severity of toxic responses across different dose levels.

Drug safety is commonly summarized using the therapeutic index:

$$
TI = \frac{TD_{50}}{ED_{50}}
$$

Where:
- $TD_{50}$ = dose causing toxicity in 50% of a population  
- $ED_{50}$ = dose producing a therapeutic effect in 50% of a population  

- Measures dose-dependent toxicity and safety margins  
- Used in regulatory science and drug development  
- Essential for assessing risk–benefit profiles of pharmaceuticals


--- PAGE ---

## System-Wide State

System-wide assays are used to characterize the overall state of a biological system by measuring large-scale patterns across genes, proteins, or metabolites. Rather than focusing on individual molecules, these approaches aim to capture coordinated behavior across entire biological networks.

These assays are designed to describe global biological activity and system-level changes across conditions, often revealing patterns that are not visible at the level of single-molecule analysis.

- Measure genome-wide, proteome-wide, or metabolome-wide activity  
- Compare global biological states across conditions, tissues, or disease states  
- Common in systems biology, precision medicine, and large-scale biological data analysis  

<br>

### RNA-seq / scRNA-seq

RNA sequencing measures gene expression by quantifying RNA abundance across thousands of genes simultaneously. Single-cell RNA-seq extends this resolution to individual cells, revealing heterogeneity within tissues.

- Captures gene expression profiles at system scale  
- Enables comparison between conditions, tissues, or cell types  
- Used in disease classification and systems-level biology  

A standard way to quantify changes in expression is log-transformed fold change:

$$
\log_2(\text{Fold Change}) =
\log_2\left(\frac{\text{Treatment}}{\text{Control}}\right)
$$

<br>

### Proteomics

Proteomics analyzes the full set of proteins expressed in a biological system.

- Measures global protein abundance and variation  
- Identifies biomarkers associated with disease states  
- Maps functional pathways and protein networks  

<br>

### Metabolomics

Metabolomics measures small-molecule metabolites that reflect the biochemical activity of a system.

- Captures real-time metabolic state of cells or organisms  
- Sensitive to environmental and physiological changes  
- Used in nutrition science, disease diagnosis, and metabolic research  

<br>

### High-Throughput Screening

High-throughput screening evaluates large libraries of compounds or conditions in parallel to identify biological activity.

- Enables rapid testing of thousands to millions of samples  
- Produces large-scale datasets for drug discovery  
- Used to identify candidate compounds or genetic targets  

Assay quality in screening experiments is evaluated using the Z'-factor:

$$
Z' = 1 - \frac{3(\sigma_p + \sigma_n)}{|\mu_p - \mu_n|}
$$

Where:
- $\mu_p$, $\mu_n$ = means of positive and negative controls  
- $\sigma_p$, $\sigma_n$ = standard deviations of positive and negative controls  


<br>

### Bioinformatics

Bioinformatics applies computational methods to analyze and interpret large biological datasets.

- Sequence alignment and genomic analysis tools  
- Statistical modeling of biological systems  
- Machine learning approaches for pattern discovery  
- Common tools include Python, R, and specialized bioinformatics software


--- PAGE ---

## Pharmacokinetics and Drug Modeling

Pharmacokinetics is the quantitative study of how drugs move through the body over time. It provides a mathematical description of the processes that determine drug concentration in biological systems, including absorption, distribution, metabolism, and excretion (ADME). These models are used to predict how drug levels change in the bloodstream and tissues, and they form the basis for determining safe and effective dosing regimens.

<br>

### ADME Framework

The ADME framework describes the four fundamental physiological processes that govern the fate of a drug after administration. Each component contributes to the overall concentration-time profile observed in the body.

- Absorption: entry of the drug into systemic circulation from the site of administration  
- Distribution: reversible movement of the drug between blood and tissues  
- Metabolism: biochemical transformation of the drug, primarily in the liver  
- Excretion: removal of the drug and its metabolites from the body, primarily via kidneys or bile  

<br>

### One-Compartment Model

The one-compartment model assumes that the drug distributes instantaneously and uniformly throughout the body, treating the system as a single homogeneous compartment. Drug elimination is modeled as a first-order decay process.

$$
C(t) = C_0 e^{-kt}
$$

Where:

- $C_0$ = initial drug concentration immediately after administration  
- $k$ = elimination rate constant governing the speed of decay  

This model is commonly used for drugs that distribute rapidly relative to their elimination time scale.

<br>

### Absorption Model

This model extends basic elimination dynamics by incorporating a separate absorption process, allowing for more realistic representation of orally or extravascularly administered drugs.

$$
\frac{dC}{dt} = k_aA - k_eC
$$

This equation captures the balance between drug entering the bloodstream through absorption and leaving the system through elimination.

Where:

- $k_aA$ = rate of drug absorption into systemic circulation  
- $k_eC$ = rate of drug elimination from the body  

<br>

### Half-Life

The half-life of a drug is defined as the time required for its concentration to decrease by 50% during elimination. It provides a practical measure of how long a drug remains active in the body.

$$
t_{1/2} = \frac{\ln 2}{k}
$$

- Determines the duration of pharmacological effect  
- Used to guide dosing intervals and accumulation risk  

<br>

### Multi-Compartment Systems

Multi-compartment models describe drug distribution across multiple physiological spaces, such as blood plasma, tissues, and organs. Each compartment is represented by its own time-dependent concentration.

$$
C_i = C_i(t)
$$

These models capture more complex pharmacokinetic behavior, particularly when drug distribution is not instantaneous or uniform.

- Represents drug movement between distinct tissue compartments  
- Modeled using systems of coupled differential equations  
- Used for drugs with slow or heterogeneous distribution  

<br>

### Distribution Factors

Drug distribution is influenced by physiological and physicochemical properties that determine how readily a drug moves between blood and tissues. These factors shape both the magnitude and duration of drug exposure in different compartments.

- Blood flow to tissues, which affects delivery rate  
- Tissue permeability, which governs movement across membranes  
- Protein binding, which limits the free (active) drug fraction  
- Lipid solubility, which influences membrane penetration and tissue accumulation  


--- PAGE ---

## Stability Studies

Stability studies in biotechnology and pharmaceuticals evaluate how a biological product or drug changes over time under different environmental conditions. The goal is to determine how long a product remains safe, effective, and chemically intact during storage and use.

<br>

### Concentration Decay Over Time

Many degradation processes can be approximated as a decrease in active compound concentration:


$$ C(t) = C_0 e^{-kt} $$

Where:
- $ C(t) $ = concentration at time $ t $
- $ C_0 $ = initial concentration
- $ k $ = degradation rate constant

This models first-order degradation, which is common in pharmaceuticals.

<br>

### Temperature Dependence and the Arrhenius Model

Chemical degradation rates increase with temperature. This relationship is often modeled using the Arrhenius equation:

$$ k = A e^{-\frac{E_a}{RT}} $$

Where:
- $ k $ = reaction rate constant
- $ A $ = frequency factor
- $ E_a $ = activation energy
- $ R $ = gas constant
- $ T $ = temperature (Kelvin)

This shows that small temperature changes can significantly affect stability.

<br>

### Environmental Factors in Stability

Stability is influenced by multiple external variables:

- Temperature
- Humidity
- Light exposure
- Oxygen availability
- pH conditions

Each factor modifies degradation rates, often in nonlinear ways.

<br>

### Reaction Kinetics in Degradation

Some degradation processes follow higher-order kinetics rather than simple exponential decay. For example:

$$ \frac{dC}{dt} = -kC^n $$

Where:
- $ n \neq 1 $ introduces nonlinear degradation behavior

This reflects more complex molecular interactions.

<br>

### Stability as a Predictive Model

Stability studies combine experimental data with mathematical modeling to predict:

- Expiration dates
- Storage requirements
- Packaging conditions
- Transport constraints

This makes stability analysis a predictive engineering discipline rather than just observational science.


--- PAGE ---

## Biostatistics and Experimental Design

Biostatistics and experimental design form the mathematical backbone of biotechnology research. They determine whether observed biological effects are real, reproducible, and meaningful—or whether they are simply the result of noise, bias, or random variation.

<br>

### Hypothesis Testing Framework

Most biostatistical inference begins with hypothesis testing:

- Null hypothesis: no effect exists
- Alternative hypothesis: a real effect exists

This is formalized as:

$$
H_0:\mu_T = \mu_C
$$

$$
H_1:\mu_T \ne \mu_C
$$

Where:
- $ \mu_T $ = mean outcome in treatment group
- $ \mu_C $ = mean outcome in control group

<br>

### Confidence Intervals and Estimation

Instead of single-point estimates, biostatistics uses intervals to represent uncertainty:

$$
CI_{95\%}(\theta) = [\hat{\theta}-\Delta,\ \hat{\theta}+\Delta]
$$

Where:
- $ \theta $ = estimated biological parameter (e.g., mean response, risk ratio)

This reflects the inherent uncertainty in sampling biological populations.

<br>

### Control Groups and Causal Inference

Control groups provide a baseline for comparison, allowing researchers to estimate causal effects by isolating the impact of the treatment.

Without controls, it becomes impossible to distinguish treatment effects from background variation.

<br>

### Sampling and Population Inference

Biostatistics often deals with inferring properties of a large population from a smaller sample:

$$
\hat{\mu} \approx \mu
$$

Where:
- $ \hat{\mu} $ = sample estimate
- $ \mu $ = true population parameter

Proper sampling design ensures representativeness.

<br>

### Statistical Power and Experiment Sensitivity

Statistical power measures the probability of detecting a real effect when it exists:

$$
Power = 1 - \beta
$$

Where:
- $ \beta $ = false negative rate

Higher power reduces the chance of missing meaningful biological effects.

<br>

### Experimental Design Structure

Good experimental design ensures that:

- Variables are controlled
- Confounders are minimized
- Measurements are consistent
- Results are reproducible

Common designs include:
- Randomized controlled trials
- Factorial experiments
- Dose-response studies
- Longitudinal studies

<br>

### Error Types in Biostatistics

Two main types of inference errors exist:

- Type I error (false positive): detecting an effect that is not real
- Type II error (false negative): failing to detect a real effect

Balancing these errors is a core design challenge.

<br>

### Regression and Modeling Relationships

Many biological relationships are modeled using regression techniques:

$$
Y = \beta_0 + \beta_1X + \epsilon
$$

Where:
- $ X $ = predictor variable
- $ Y $ = outcome variable
- $ \epsilon $ = residual error

This allows quantification of relationships between variables.