<!--
title: "Math in Medicine"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/medicine_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Medicine
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Collecting and analyzing clinical data from medical imaging, lab tests, and patient records  
- Using statistical software and programming tools (e.g., R, Python) for medical data analysis  
- Interpreting diagnostic imaging such as MRI, CT scans, and X-rays using specialized systems  
- Applying biostatistics and epidemiological models to study disease patterns and treatment outcomes  
- Using electronic health record (EHR) systems to track patient history and outcomes  
- Running clinical trials and analyzing experimental treatment effectiveness  
- Supporting diagnostic and treatment decisions through evidence-based data interpretation  


<br>

###  What are the most common jobs?
- Physician  
- Surgeon  
- Nurse Practitioner  
- Registered Nurse  
- Medical Researcher  
- Pharmacist  
- Radiologist  
- Medical Technician  


<br>

###  What math concepts do I need to know?
- Statistics  
- Probability  
- Algebra  
- Calculus  
- Data Analysis  
- Ratios and Proportions  
- Dosage Calculations  
- Graphing and Trends  
- Epidemiology Models  

--- PAGE ---

## Human Anatomy & Physiology

Human anatomy and physiology form the foundational biological framework for all medical science. Anatomy describes the structural organization of the human body, while physiology explains how these structures function and interact dynamically over time. Together, they provide a systems-level understanding of health and disease by linking form to function across multiple scales of biological organization.

Modern approaches to physiology increasingly emphasize quantitative modeling, where biological systems are treated not only as descriptive entities but as dynamic systems governed by physical, chemical, and mathematical principles.

<br>

### Organ Systems and Physiological Regulation

The human body is organized into interdependent organ systems, each responsible for specific physiological functions while simultaneously contributing to overall systemic stability. These include the cardiovascular, respiratory, nervous, endocrine, musculoskeletal, and digestive systems.

Although each system has distinct roles, none operates in isolation. Instead, physiological regulation emerges from continuous interaction between systems, coordinated through chemical signaling, neural control, and mechanical feedback. This interdependence allows the body to maintain internal stability despite external environmental changes.

<br>

### Cardiovascular, Respiratory, and Neural Dynamics

Three of the most mathematically and physically relevant systems in physiology are the cardiovascular, respiratory, and nervous systems.

The cardiovascular system governs transport of oxygen, nutrients, hormones, and waste products through a closed circulatory network. Blood flow dynamics can be understood using principles of fluid mechanics and pressure gradients.

The respiratory system regulates gas exchange through diffusion across alveolar membranes, coupling external atmospheric conditions with internal metabolic demands.

The nervous system coordinates rapid signaling using electrochemical impulses. These signals propagate through networks of neurons that can be modeled using dynamical systems and network theory.

Together, these systems form a tightly coupled regulatory network that maintains physiological coherence across time.

<br>

### Homeostasis and Feedback Control Systems

A central principle of physiology is homeostasis, the maintenance of stable internal conditions within narrow physiological ranges. This stability is not static but dynamically maintained through feedback mechanisms.

Homeostatic regulation typically follows a structured feedback loop:

$$\text{Change} \rightarrow \text{Detection} \rightarrow \text{Response} \rightarrow \text{Stabilization}$$

In this framework:
- **Change** represents a deviation from a physiological set point
- **Detection** occurs through sensory receptors or monitoring systems
- **Response** is executed by effector organs or signaling pathways
- **Stabilization** restores equilibrium or reduces deviation

Negative feedback systems dominate physiological regulation, ensuring that deviations are corrected rather than amplified. This structure is analogous to control systems in engineering, where stability and responsiveness must be balanced.

<br>

### Biological Transport and Diffusion Processes

Transport processes are fundamental to physiological function, enabling the movement of molecules, ions, and energy across biological compartments. These processes include diffusion, osmosis, and active transport.

Diffusion, in particular, is driven by concentration gradients and can be described mathematically as:

$$\text{Flux} \propto \nabla C$$

where the flux of a substance is proportional to the spatial gradient of its concentration.

This principle explains a wide range of physiological phenomena, including:
- Oxygen diffusion from alveoli into blood
- Nutrient exchange across capillary walls
- Waste removal from tissues
- Cellular signaling molecule distribution

Transport systems often combine passive diffusion with active mechanisms that require energy input, allowing organisms to maintain concentration gradients essential for life.

<br>

### Systems-Level Physiological Modeling

At the highest level of organization, physiology is best understood as a systems-level phenomenon in which multiple organ systems interact dynamically. These interactions can be modeled using mathematical frameworks such as differential equations, network models, and feedback control systems.

Systems-level modeling allows researchers to predict how changes in one subsystem affect overall physiological behavior. For example, alterations in cardiac output influence oxygen delivery, which in turn affects cellular metabolism and neural activity.

This approach shifts physiology from a purely descriptive science to a predictive and computational discipline. By integrating structural anatomy with dynamic modeling, systems physiology provides a unified framework for understanding both normal function and pathological disruption.

<br>

### Cardiovascular, Respiratory, and Physiological Modeling

Human anatomy and physiology is fundamentally a quantitative discipline in which biological function is described through measurable variables such as pressure, flow, concentration gradients, and electrical potential. Many core physiological processes can be represented using mathematical relationships that connect structure to function, particularly in the cardiovascular, respiratory, and nervous systems.

<br>

### Cardiac Output Equation

Cardiac output is the volume of blood pumped by the heart per unit time and is a central measure of cardiovascular performance.

$$
CO = HR \times SV
$$

where:
- $CO$ is cardiac output
- $HR$ is heart rate
- $SV$ is stroke volume

Cardiac output determines systemic perfusion and oxygen delivery to tissues. It increases during exercise and decreases in conditions such as heart failure or hypovolemia. This relationship highlights how cardiac performance depends on both rate and volume components.

<br>

### Mean Arterial Pressure Equation

Mean arterial pressure (MAP) represents the average arterial pressure throughout one cardiac cycle and is a key determinant of organ perfusion.

$$
MAP=\frac{SBP+2(DBP)}{3}
$$

where:
- $SBP$ is systolic blood pressure
- $DBP$ is diastolic blood pressure

Because the heart spends more time in diastole than systole, diastolic pressure is weighted more heavily. MAP is clinically important for assessing tissue perfusion, particularly in critical care settings.

<br>

### Poiseuille’s Law

Poiseuille’s law describes laminar flow of fluid through a cylindrical vessel and is fundamental to understanding blood flow in arteries and airways.

$$
Q=\frac{\pi r^4\Delta P}{8\eta L}
$$

where:
- $Q$ is flow rate
- $r$ is vessel radius
- $\Delta P$ is pressure difference
- $\eta$ is viscosity
- $L$ is vessel length

A key implication is that flow is extremely sensitive to radius changes, as it is proportional to the fourth power of radius. Small changes in vessel diameter can therefore produce large changes in blood flow.

<br>

### Fick Principle

The Fick principle relates oxygen consumption to cardiac output and arteriovenous oxygen difference.

$$
CO=\frac{VO_2}{C_{aO_2}-C_{vO_2}}
$$

where:
- $VO_2$ is oxygen consumption
- $C_{aO_2}$ is arterial oxygen content
- $C_{vO_2}$ is venous oxygen content

This relationship allows indirect estimation of cardiac output based on oxygen utilization, linking respiratory physiology with cardiovascular performance.

<br>

### Oxygen Content Equation

Arterial oxygen content reflects the total amount of oxygen carried in blood, including both hemoglobin-bound and dissolved oxygen.

$$
C_{aO_2}=(1.34\times Hb\times S_{aO_2})+(0.003\times P_{aO_2})
$$

where:
- $Hb$ is hemoglobin concentration
- $S_{aO_2}$ is oxygen saturation
- $P_{aO_2}$ is partial pressure of oxygen

Most oxygen is transported bound to hemoglobin, while a small fraction is dissolved in plasma. This equation explains why anemia can significantly reduce oxygen delivery even when oxygen saturation appears normal.

<br>

### A–a Gradient

The alveolar–arterial (A–a) gradient measures the difference between oxygen concentration in the alveoli and arterial blood.

$$
A-a\ Gradient=P_{AO_2}-P_{aO_2}
$$

An increased gradient indicates impaired oxygen transfer from lungs to blood, which may occur in conditions such as ventilation–perfusion mismatch, diffusion impairment, or shunting. It is a key diagnostic tool in respiratory physiology.

<br>

### Henderson–Hasselbalch Equation

The Henderson–Hasselbalch equation describes the relationship between blood pH, bicarbonate concentration, and carbon dioxide levels.

$$
pH=6.1+\log\frac{[HCO_3^-]}{0.03P_{CO_2}}
$$

This equation reflects the bicarbonate buffering system, which is the primary regulator of acid–base balance in human physiology. It illustrates how respiratory and renal systems jointly regulate blood pH.

<br>

### Alveolar Gas Equation

The alveolar gas equation estimates the partial pressure of oxygen in the alveoli.

$$
P_{AO_2}=F_{IO_2}(P_{atm}-P_{H_2O})-\frac{P_{aCO_2}}{R}
$$

where:
- $F_{IO_2}$ is inspired oxygen fraction
- $P_{atm}$ is atmospheric pressure
- $P_{H_2O}$ is water vapor pressure
- $R$ is respiratory exchange ratio

This equation is essential for understanding oxygen availability in the lungs and is widely used in assessing hypoxemia and ventilatory function.

<br>

### Bernoulli Equation

The simplified Bernoulli equation estimates pressure differences in cardiovascular flow using velocity measurements.

$$
\Delta P=4v^2
$$

where:
- $v$ is blood flow velocity

This relationship is widely used in echocardiography to estimate pressure gradients across heart valves, particularly in valvular stenosis. It connects fluid dynamics with clinical cardiac imaging.

<br>

### Nernst Equation

The Nernst equation describes the electrical potential across a membrane due to ion concentration differences.

$$
E=\frac{RT}{zF}\ln\frac{[ion]_{out}}{[ion]_{in}}
$$

where:
- $R$ is the gas constant
- $T$ is temperature
- $z$ is ionic charge
- $F$ is Faraday’s constant

This equation is fundamental to understanding membrane potentials in excitable cells, including neurons and muscle cells. It explains how ion gradients generate electrical signaling in physiology.

<br>

### Hodgkin–Huxley Membrane Equation

The Hodgkin–Huxley model describes the electrical behavior of excitable cell membranes.

$$
C_m\frac{dV}{dt}=I_{ext}-I_{ion}
$$

where:
- $C_m$ is membrane capacitance
- $V$ is membrane potential
- $I_{ext}$ is external current
- $I_{ion}$ is ionic current

This equation models how action potentials are generated and propagated in neurons. It represents a foundational framework in neurophysiology, linking ion channel dynamics to electrical activity in biological membranes.


--- PAGE ---

## Nursing & Triage

**Nursing and triage** involve the continuous assessment, prioritization, and monitoring of patients in order to identify physiological instability and guide clinical intervention. In many healthcare settings, nurses serve as the primary interface between patients and the broader medical system, collecting real-time clinical measurements that inform diagnosis, treatment decisions, and emergency escalation.

Triage involves quickly assessing a patient's physiological condition when time is limited and information may be incomplete. Measurements obtained at the bedside are used to estimate patient stability, detect deterioration, and prioritize allocation of medical resources.

<br>

### Vital Signs Assessment

The foundation of nursing assessment is the measurement of core physiological variables, commonly referred to as **vital signs**. These include:

- Heart rate (HR)
- Blood pressure (BP)
- Respiratory rate (RR)
- Body temperature
- Oxygen saturation (SpO₂)

Together, these variables provide a high-level summary of cardiovascular, respiratory, metabolic, and neurological function.

Blood pressure measurements are often further analyzed using **Mean Arterial Pressure (MAP)**, which estimates average arterial perfusion pressure throughout the cardiac cycle:

$$
MAP \approx \frac{2(DBP)+SBP}{3}
$$

where:
- $SBP$ = systolic blood pressure
- $DBP$ = diastolic blood pressure

MAP is clinically important because tissue perfusion depends more strongly on average arterial pressure than on systolic pressure alone.

Low MAP values may indicate:
- Shock
- Blood loss
- Sepsis
- Cardiovascular instability

Persistent abnormalities in vital signs often represent early indicators of physiological deterioration before severe symptoms become clinically obvious.

<br>

### Pulse Oximetry and Oxygen Saturation

Pulse oximetry is a noninvasive method used to estimate the percentage of hemoglobin molecules carrying oxygen in arterial blood.

A simplified representation is:

$$
SpO_2 \approx
\frac{\text{oxygenated hemoglobin}}
{\text{total hemoglobin}}
\times 100\%
$$

Pulse oximeters function by measuring differential absorption of red and infrared light through tissue. Because oxygenated and deoxygenated hemoglobin absorb light differently, oxygen saturation can be estimated continuously in real time.

Clinically, oxygen saturation provides insight into:
- Pulmonary gas exchange
- Respiratory efficiency
- Circulatory adequacy
- Risk of hypoxia

Declining SpO₂ values may signal:
- Respiratory failure
- Airway obstruction
- Pneumonia
- Pulmonary embolism
- Cardiac compromise

Pulse oximetry is therefore central to emergency medicine, perioperative monitoring, and critical care.

<br>

### Glasgow Coma Scale (GCS)

Neurological status is frequently evaluated using the **Glasgow Coma Scale (GCS)**, a structured scoring system designed to quantify level of consciousness.

The total score is calculated as:

$$
GCS = E + V + M
$$

where:
- $E$ = eye response score
- $V$ = verbal response score
- $M$ = motor response score

The scale ranges from:
- 3 (deep unconsciousness)
- to 15 (fully alert)

GCS scoring is widely used in:
- Trauma assessment
- Stroke evaluation
- Intensive care monitoring
- Emergency triage

A decreasing GCS may indicate:
- Brain injury
- Hypoxia
- Metabolic disturbance
- Neurological deterioration

Because neurological decline can occur rapidly, repeated GCS assessment is often more important than a single isolated score.

<br>

### Early Warning Scores and Deterioration Detection

Hospitals commonly use aggregate scoring systems such as:
- NEWS (National Early Warning Score)
- MEWS (Modified Early Warning Score)

These systems combine multiple physiological measurements into a unified deterioration score.

Conceptually:

$$
\text{Total Score} =
\sum (\text{physiological risk points})
$$

Variables commonly included are:
- Heart rate
- Blood pressure
- Respiratory rate
- Temperature
- Oxygen saturation
- Mental status

Higher scores correspond to increased probability of clinical deterioration and trigger escalation protocols such as:
- Physician notification
- Rapid response activation
- ICU evaluation

These scoring systems transform bedside measurements into structured probabilistic risk assessment tools.

<br>

### Capillary Refill and Peripheral Perfusion

Peripheral circulation is commonly evaluated using **capillary refill time**, which estimates adequacy of blood flow to peripheral tissues.

Perfusion can be conceptualized as:

$$
\text{Perfusion} \propto
\frac{\text{Blood Flow}}
{\text{Vascular Resistance}}
$$

Capillary refill is assessed by briefly compressing tissue—typically a fingernail bed—and measuring the time required for normal coloration to return.

Delayed refill may indicate:
- Shock
- Dehydration
- Hypothermia
- Poor cardiac output
- Peripheral vasoconstriction

Although simple, perfusion assessment provides rapid insight into circulatory status during emergency evaluation.

<br>

### Fluid Balance Monitoring

Accurate monitoring of fluid intake and output is essential in many hospitalized patients.

Net fluid balance is essentially:

$$
\text{Net Fluid Balance} =
\text{Intake} - \text{Output}
$$

Intake includes:
- Oral fluids
- Intravenous fluids
- Enteral feeding

Output includes:
- Urine
- Drainage
- Vomiting
- Blood loss

Fluid balance monitoring is particularly important in:
- Heart failure
- Kidney disease
- Critical care
- Postoperative management

Even relatively small imbalances can significantly alter:
- Blood pressure
- Electrolyte concentration
- Tissue perfusion
- Organ function

<br>

### Weight-Based Dosing and Fluid Status

Body weight is frequently used to guide medication dosing and fluid administration.

A generalized dosing relationship is:

$$
\text{Dose} =
\text{mg/kg} \times \text{Body Weight}
$$

Weight-based calculations are especially important in:
- Pediatrics
- Critical care
- Chemotherapy
- Anesthesia

Bedside weight measurements also provide indirect information about:
- Fluid retention
- Nutritional status
- Edema formation
- Response to therapy

Rapid weight changes over short periods often reflect fluid shifts rather than changes in body tissue mass.

<br>

### Pain Assessment and Subjective Measurement

Pain is commonly quantified using standardized scoring systems such as:
- Numeric Rating Scale (0–10)
- Wong-Baker Faces Scale

A simplified representation is:

$$
\text{Pain Score} \in [0,10]
$$

Although pain is subjective, structured scoring allows:
- Trend monitoring
- Communication between providers
- Evaluation of treatment effectiveness
- Standardization in clinical documentation

Pain assessment plays an important role in:
- Emergency triage
- Postoperative recovery
- Chronic disease management
- Palliative care

Because subjective symptoms cannot be measured directly through laboratory instrumentation, structured scales serve as proxies for internal patient experience.

<br>

### Corrected Calcium Equation

The corrected calcium equation adjusts measured serum calcium based on albumin concentration.

$$
\text{Corrected Ca} = \text{Measured Ca} +0.8(4-\text{Albumin})
$$

This correction accounts for the fact that a significant portion of circulating calcium is protein-bound, primarily to albumin. In conditions of hypoalbuminemia, total calcium may appear low even when physiologically active ionized calcium is normal. This adjustment improves clinical interpretation of calcium status in hospitalized patients.


--- PAGE ---

## Epidemiology & Public Health

Epidemiology and public health study how disease, injury, and health-related conditions are distributed across populations. Unlike individual clinical medicine, which focuses on diagnosing and treating single patients, epidemiology analyzes large-scale trends, risk factors, and transmission dynamics in order to understand and improve population health.

Modern public health relies heavily on mathematics, probability, statistics, and computational modeling to measure disease burden, evaluate interventions, and forecast future outcomes. These tools allow researchers and policymakers to move from isolated observations toward systematic population-level decision-making.

<br>

### Incidence and Prevalence Modeling

Two of the most fundamental epidemiological measurements are **incidence** and **prevalence**.

Incidence measures the rate of new disease occurrence within a population over a specified time interval:

$$
\text{Incidence} =
\frac{\text{New Cases}}
{\text{Population At Risk}}
$$

Prevalence measures the proportion of individuals currently affected by a condition:

$$
\text{Prevalence} =
\frac{\text{Existing Cases}}
{\text{Population}}
$$

Although related, these quantities describe different aspects of disease burden:
- Incidence reflects disease emergence
- Prevalence reflects total population impact

For example:
- A rapidly spreading infection may have high incidence
- A chronic disease may have high prevalence even with low incidence

These measures are foundational in:
- Disease surveillance
- Healthcare planning
- Resource allocation
- Public health policy

<br>

### Relative Risk and Odds Ratios

Epidemiology frequently compares disease probability between groups exposed and unexposed to potential risk factors.

A common measure is **relative risk (RR)**:

$$
RR =
\frac{P(A|B)}
{P(A|\neg B)}
$$

where:
- $P(A|B)$ = probability of outcome $A$ given exposure $B$
- $P(A|\neg B)$ = probability of outcome without exposure

Interpretation:
- $RR = 1$ → no association
- $RR > 1$ → increased risk
- $RR < 1$ → protective effect

Another important comparison metric is the **odds ratio (OR)**:

$$
OR = \frac{ad}{bc}
$$

Odds ratios are widely used in:
- Case-control studies
- Logistic regression
- Statistical inference
- Clinical research

Because many epidemiological studies cannot directly measure absolute probabilities, odds-based methods are often mathematically more practical.

<br>

### Compartmental Epidemic Models

Population disease spread is commonly modeled using **compartmental systems**, where individuals transition between epidemiological states.

The classic **SIR model** divides populations into:
- Susceptible ($S$)
- Infectious ($I$)
- Recovered ($R$)

Transmission dynamics are modeled using coupled differential equations such as:

$$
\frac{dS}{dt} = -\beta SI
$$

$$
\frac{dI}{dt} =
\beta SI - \gamma I
$$

where:
- $\beta$ = transmission rate
- $\gamma$ = recovery rate

These equations describe how:
- susceptible populations decline through exposure
- infectious populations increase through transmission
- recovery reduces active infection levels

More advanced systems such as SEIR models add additional compartments including:
- Exposed
- Hospitalized
- Vaccinated
- Deceased

Compartmental models are central to:
- Pandemic forecasting
- Vaccination strategy analysis
- Healthcare planning
- Transmission modeling

<br>

### Reproduction Number and Outbreak Forecasting

One of the most important epidemiological parameters is the **basic reproduction number**, denoted $R_0$.

A simplified representation is:

$$
R_0 =
\frac{\beta}{\gamma}
$$

Conceptually, $R_0$ represents the average number of secondary infections generated by one infected individual in a fully susceptible population.

Threshold behavior emerges naturally:
- $R_0 > 1$ → outbreak growth
- $R_0 < 1$ → outbreak decline

Because transmission is nonlinear, relatively small changes in:
- contact rate
- immunity
- intervention policy
- vaccination coverage

can dramatically alter outbreak trajectories.

Forecasting models therefore play a major role in public health decision-making during epidemics and pandemics.

<br>

### Survival Analysis and Time-to-Event Modeling

Many public health problems involve analyzing the probability that an event has not yet occurred after a given time.

This is described using a **survival function**:

$$
S(t)=P(T>t)
$$

where:
- $T$ represents time until an event
- $S(t)$ gives the probability of surviving beyond time $t$

Survival analysis is widely used in:
- Cancer prognosis
- Clinical trials
- Mortality analysis
- Reliability modeling
- Treatment effectiveness studies

A key challenge in survival analysis is handling **censored data**, where patient outcomes may be incomplete or ongoing at the time of analysis.

<br>

### Screening Accuracy and Diagnostic Evaluation

Public health screening programs rely heavily on statistical evaluation of diagnostic performance.

Two critical measures are **sensitivity** and **specificity**.

Sensitivity measures the probability that a test correctly identifies disease:

$$
\text{Sensitivity} =
\frac{TP}{TP+FN}
$$

Specificity measures the probability that a test correctly identifies absence of disease:

$$
\text{Specificity} =
\frac{TN}{TN+FP}
$$

where:
- $TP$ = true positives
- $FN$ = false negatives
- $TN$ = true negatives
- $FP$ = false positives

These measures are essential because screening tests must balance:
- missed disease
- false alarms
- cost
- population impact

Importantly, the usefulness of a screening test also depends strongly on disease prevalence within the target population.

<br>

### Logistic Regression and Population Risk Modeling

Many epidemiological systems attempt to estimate the probability of disease or adverse outcomes based on multiple variables simultaneously.

A common model is **logistic regression**:

$$
P(Y=1)=
\frac{1}
{1+e^{-(\beta_0+\beta X)}}
$$

where:
- $X$ represents predictor variables
- $\beta$ values represent weighted contributions

Logistic regression is widely used because:
- probabilities remain bounded between 0 and 1
- multiple risk factors can be integrated simultaneously
- nonlinear probability behavior can be modeled

Applications include:
- disease prediction
- mortality risk estimation
- hospital readmission forecasting
- population risk stratification

These models form part of the mathematical foundation underlying modern evidence-based medicine.

<br>

### Public Health Intervention and Resource Optimization

Public health systems must allocate limited resources efficiently across large populations.

Examples include:
- vaccine distribution
- ICU capacity planning
- staffing allocation
- outbreak response coordination
- screening program deployment

These problems are fundamentally optimization problems involving:
- limited budgets
- uncertain outcomes
- competing priorities
- ethical constraints

Interventions are evaluated not only by effectiveness, but also by:
- scalability
- cost efficiency
- accessibility
- population impact

<br>

### Logistic Growth Equation

The logistic growth equation models population growth with a limiting carrying capacity.

$$
P(t)=\frac{K}{1+Ae^{-rt}}
$$

where:
- $P(t)$ is population at time $t$
- $K$ is carrying capacity
- $r$ is growth rate
- $A$ is a constant determined by initial conditions

This model is widely used in epidemiology, tumor growth modeling, and biological population dynamics. It captures the transition from exponential growth to saturation as resources become limited.


--- PAGE ---

## Medical Imaging

**Medical imaging** is the study of how internal anatomical and physiological structures can be visualized using physical signals, computational reconstruction, and mathematical modeling. Modern imaging systems transform indirect measurements into interpretable visual representations of the human body, allowing clinicians to diagnose disease, guide interventions, and monitor physiological processes without direct surgical access.

Different imaging modalities rely on different physical principles, but all share a common framework:
1. A signal interacts with tissue
2. Tissue alters the signal
3. Sensors measure the modified signal
4. Reconstruction algorithms generate interpretable images

Because of this, medical imaging sits at the intersection of medicine, physics, engineering, computer science, and applied mathematics.

<br>

### X-Ray Radiography

X-ray radiography is one of the oldest and most widely used imaging techniques. X-rays pass through the body and are attenuated differently depending on tissue density and composition.

A simplified attenuation model is:

$$
I = I_0 e^{-\mu x}
$$

where:
- $I_0$ = initial X-ray intensity
- $I$ = transmitted intensity
- $\mu$ = attenuation coefficient
- $x$ = tissue thickness

Dense structures such as bone absorb more radiation and therefore appear brighter on radiographic images.

X-ray imaging is commonly used for:
- fracture detection
- chest imaging
- dental imaging
- skeletal evaluation

Because attenuation depends on tissue composition, radiography provides indirect information about internal structure through differential absorption patterns.

<br>

### Computed Tomography (CT)

Computed Tomography (CT) extends X-ray imaging into cross-sectional and three-dimensional reconstruction. Instead of collecting a single projection image, CT systems gather many projections from multiple rotational angles around the patient. Computational algorithms then reconstruct internal anatomy. A simplified tomographic reconstruction expression is:

$$
f(x,y)=
\int_{\theta=0}^{\pi}
P_\theta(s)\,d\theta
$$

where:
- $P_\theta(s)$ represents projection data acquired at angle $\theta$
- $f(x,y)$ represents the reconstructed structure

CT scanning is widely used for:
- trauma assessment
- intracranial hemorrhage detection
- vascular imaging
- cancer staging
- surgical planning

Modern CT systems can rapidly generate high-resolution volumetric reconstructions of anatomical structures.

<br>

### Magnetic Resonance Imaging (MRI)

Magnetic Resonance Imaging (MRI) uses magnetic fields and radiofrequency signals to generate detailed images of soft tissue.

MRI signal behavior is often modeled as:

$$
S(t)=
S_0 e^{-t/T_2}\cos(\omega t)
$$

where:
- $S_0$ = initial signal amplitude
- $T_2$ = transverse relaxation constant
- $\omega$ = angular frequency

MRI exploits the magnetic behavior of hydrogen nuclei within tissue. After excitation by radiofrequency pulses, nuclei emit measurable signals while relaxing back toward equilibrium. Different tissues exhibit different relaxation properties, allowing MRI to produce strong soft-tissue contrast.

MRI is especially useful for:
- brain imaging
- spinal imaging
- musculoskeletal evaluation
- tumor detection
- cardiovascular imaging

Because MRI does not use ionizing radiation, it is particularly valuable for repeated imaging and high-detail soft tissue analysis.

<br>

### Ultrasound Imaging

Ultrasound systems generate images using reflected high-frequency sound waves. Distance estimation is based on signal travel time:

$$
d=\frac{vt}{2}
$$

where:
- $d$ = distance to reflecting structure
- $v$ = sound velocity in tissue
- $t$ = round-trip travel time

The factor of $\frac{1}{2}$ accounts for the signal traveling to the structure and back.

It is commonly used in:
- obstetrics
- cardiac imaging
- abdominal imaging
- vascular assessment
- emergency medicine

Ultrasound systems continuously reconstruct anatomical structure from returning acoustic echoes.

<br>

### Positron Emission Tomography (PET)

Positron Emission Tomography (PET) is a functional imaging technique that visualizes metabolic activity rather than anatomical structure alone.

Radioactive tracers injected into the body undergo exponential decay:

$$
A(t)=A_0 e^{-\lambda t}
$$

where:
- $A_0$ = initial radioactive activity
- $\lambda$ = decay constant
- $A(t)$ = activity at time $t$

PET systems detect emitted photons resulting from positron annihilation events and reconstruct tracer distribution throughout the body.

PET imaging is especially useful for:
- cancer metabolism imaging
- neurological studies
- cardiac perfusion analysis
- functional tissue assessment

Because metabolic abnormalities often appear before structural changes, PET can detect disease processes at very early stages.

<br>

### Doppler Ultrasound

Doppler ultrasound measures blood flow velocity by analyzing frequency shifts in reflected ultrasound waves.

The Doppler relationship is:

$$
\Delta f =
\frac{2vf_0\cos\theta}{c}
$$

where:
- $\Delta f$ = frequency shift
- $v$ = blood flow velocity
- $f_0$ = transmitted frequency
- $\theta$ = angle relative to flow direction
- $c$ = sound velocity in tissue

Moving blood cells alter reflected sound frequency through the Doppler effect.

Doppler systems are widely used to evaluate:
- arterial blood flow
- venous obstruction
- cardiac valve function
- vascular stenosis
- fetal circulation

Because blood flow dynamics are essential to cardiovascular physiology, Doppler ultrasound provides important hemodynamic information.

<br>

### Fluoroscopy

Fluoroscopy provides continuous real-time X-ray imaging during movement and procedural intervention.

Unlike static radiographs, fluoroscopic systems generate dynamic image sequences that allow clinicians to visualize:
- joint movement
- swallowing mechanics
- catheter placement
- vascular procedures
- orthopedic alignment

Fluoroscopy is heavily used during:
- cardiac catheterization
- gastrointestinal studies
- orthopedic surgery
- interventional radiology

<br>

### Functional MRI (fMRI)

Functional MRI (fMRI) measures neural activity indirectly through blood oxygenation changes.

A simplified relationship is:

$$
\Delta S \propto
\Delta(\text{blood oxygenation})
$$

Active brain regions consume oxygen differently, altering local magnetic properties and producing measurable signal changes known as the **BOLD response** (Blood Oxygen Level Dependent signal).

fMRI is widely used in:
- cognitive neuroscience
- language mapping
- surgical planning
- behavioral research
- brain network analysis

Rather than imaging structure alone, fMRI attempts to estimate functional activity and connectivity across neural systems.

<br>

### Image Quality, Noise, and Reconstruction Challenges

All imaging systems operate under physical and computational limitations involving:
- signal noise
- spatial resolution
- motion artifacts
- sampling constraints
- reconstruction error

Improving image quality often requires balancing:
- acquisition speed
- computational cost
- radiation exposure
- signal strength

Modern imaging systems therefore rely heavily on:
- Fourier analysis
- filtering methods
- statistical estimation
- machine learning
- numerical optimization

<br>

### Beer–Lambert Law

The Beer–Lambert law describes the attenuation of light or radiation as it passes through a medium.

$$
I=I_0e^{-\mu x}
$$

where:
- $I$ is transmitted intensity
- $I_0$ is initial intensity
- $\mu$ is the attenuation coefficient
- $x$ is path length through the medium

This relationship is fundamental in medical imaging and spectroscopy. It explains how tissues absorb or scatter radiation and is used in technologies such as CT imaging and optical diagnostic systems.

<br>

### Cockcroft–Gault Equation

The Cockcroft–Gault equation estimates creatinine clearance, which is a proxy for renal filtration function.

$$
CrCl=\frac{(140- \text{age})\times \text{weight}}{72\times S_{Cr}}
$$

where:
- $CrCl$ is creatinine clearance
- $S_{Cr}$ is serum creatinine

This equation is widely used in clinical pharmacology to adjust drug dosing in patients with impaired renal function. It provides an estimate of kidney filtration capacity based on measurable physiological variables.


--- PAGE ---

## Pharmacology & Therapeutics

Pharmacology and therapeutics study how drugs interact with biological systems in order to produce therapeutic effects, prevent disease, and manage physiological dysfunction. Modern pharmacology relies heavily on mathematical modeling, quantitative analysis, and systems-level physiology in order to determine safe and effective treatment strategies.

Many pharmacologic processes can be described using principles from:
- Differential equations
- Exponential decay
- Probability theory
- Optimization
- Statistical modeling
- Dynamical systems

Because drug behavior changes over time and varies between individuals, quantitative reasoning plays a central role in clinical therapeutics.

<br>

### Therapeutic Drug Monitoring

Therapeutic drug monitoring measures drug concentration within the bloodstream in order to maintain effective treatment levels while minimizing toxicity.

Many drugs approximately follow exponential decay behavior:

$$
C(t)=C_0 e^{-kt}
$$

where:
- $C(t)$ is drug concentration at time $t$
- $C_0$ is initial concentration
- $k$ is the elimination constant

This relationship reflects how many drugs are removed proportionally to their current concentration.

Therapeutic monitoring is especially important for:
- Narrow therapeutic index medications
- Anticonvulsants
- Immunosuppressants
- Certain antibiotics
- Chemotherapy agents

Because drug levels vary over time, repeated measurement and trend interpretation are often necessary.

<br>

### Dose-Response Titration Testing

Dose-response relationships describe how physiological effect changes as drug concentration changes. Rather than increasing indefinitely, drug effects typically approach a maximum response as concentration rises.

A common pharmacodynamic model is:

$$
E=
\frac{E_{max}C}
{EC_{50}+C}
$$

Where:
- $E$ = drug effect
- $E_{max}$ = maximum achievable effect
- $C$ = drug concentration
- $EC_{50}$ = concentration producing half-maximal effect

This relationship demonstrates that increasing dosage does not always produce proportional increases in therapeutic effect. As drug concentration rises, additional increases often produce progressively smaller gains in effect.


<br>

### Pharmacokinetic Clearance Testing

Pharmacokinetics studies how the body absorbs, distributes, metabolizes, and eliminates medications. One of the most important measures in pharmacokinetics is clearance, which quantifies how efficiently a drug is removed from circulation.

Drug clearance is commonly represented as:

$$
Cl=
\frac{\text{Rate of Elimination}}
{\text{Plasma Concentration}}
$$

Where:
- $Cl$ = drug clearance
- Rate of Elimination = amount of drug removed per unit time
- Plasma Concentration = concentration of drug in the bloodstream

Because elimination rates vary substantially between patients, individualized pharmacokinetic assessment is often necessary. Clearance measurements help clinicians determine appropriate dosing schedules and reduce the risk of drug accumulation.


<br>

### Drug Interaction Screening Assays

Drug interaction testing evaluates how multiple medications influence one another's effects, metabolism, or toxicity. While some combinations enhance therapeutic outcomes, others can reduce effectiveness or create dangerous adverse effects.

Interactions are commonly classified into three categories:

- **Synergistic interactions**, where combined effects exceed the sum of individual effects
- **Additive interactions**, where combined effects are approximately equal to the sum of individual effects
- **Antagonistic interactions**, where one drug reduces the effect of another

Many interactions occur through mechanisms such as enzyme inhibition, receptor competition, altered protein binding, changes in metabolism, or interference within physiological pathways. Modern screening increasingly relies on computational modeling, database-driven analysis, statistical risk assessment, and machine learning systems to identify potentially hazardous medication combinations before severe adverse events occur.


<br>

### Renal Function Testing for Dose Adjustment

Many medications are eliminated through the kidneys, making renal function an important determinant of safe and effective dosing. Reduced kidney function can slow drug elimination, increasing the risk of toxicity.

Creatinine clearance is commonly estimated using relationships such as:

$$
CrCl \approx
\frac{(140-\text{age})\times \text{weight}}
{72 \times Cr}
$$

Where:
- $CrCl$ = creatinine clearance
- $Cr$ = serum creatinine concentration

Renal dose adjustments are particularly important for antibiotics, chemotherapy agents, cardiovascular medications, anticoagulants, and many critical care drugs. Assessing kidney function helps clinicians tailor treatment to the patient's ability to eliminate medications safely.


<br>

### Liver Function Testing for Metabolic Drug Processing

The liver is the primary site of metabolism for many medications. Because of this, liver function has a major impact on how drugs are processed, how long they remain active in the body, and how likely they are to cause adverse effects.

Liver function testing evaluates several aspects of hepatic health, including:

- Enzyme activity
- Bilirubin levels
- Protein synthesis
- Signs of hepatic injury
- Overall metabolic capacity

These measurements help determine whether medications can be metabolized normally or whether dosage adjustments may be necessary.

Liver function assessment is particularly important for drugs that have:

- Extensive hepatic metabolism
- Narrow therapeutic windows
- Active metabolites
- Significant toxicity potential

Because liver function varies substantially between individuals, it is a major source of patient-specific variability in pharmacologic treatment.


<br>

### Allergy and Hypersensitivity Testing

Hypersensitivity testing evaluates abnormal immune responses to medications and other biological substances. Reactions can range from mild discomfort to severe medical emergencies.

Examples include:

- Skin irritation and rashes
- Delayed inflammatory responses
- Drug eruptions
- Respiratory compromise
- Anaphylaxis

To assess these risks, clinicians may use skin testing, antibody detection, exposure monitoring, clinical observation, and other forms of immune response analysis.

Beyond its clinical importance, hypersensitivity testing demonstrates how therapeutic decision-making intersects with several broader fields, including:

- Immunology
- Probability
- Patient variability
- Risk assessment

Because severe allergic reactions can be unpredictable and potentially life-threatening, careful screening remains an important component of safe medical practice.


<br>

### Toxicology Screening

Toxicology testing detects drugs, metabolites, toxins, and other chemical exposures within biological samples. The goal is not only to determine whether a substance is present, but also to understand its concentration and potential physiological effects.

Common testing methods include:

- Blood analysis
- Urine screening
- Mass spectrometry
- Chromatography
- Immunoassays

These techniques can provide information about:

- Drug concentration
- Exposure timing
- Metabolic byproducts
- Elimination patterns
- Toxic thresholds

Toxicology plays an important role in many fields, including emergency medicine, poison control, forensic investigation, occupational exposure monitoring, and substance misuse assessment.

Because many toxic effects depend strongly on concentration, toxicology relies heavily on quantitative analysis and pharmacokinetic modeling.


<br>

### Mathematical Modeling in Pharmacology

Modern pharmacology increasingly relies on mathematical and computational models to predict drug behavior, optimize dosing strategies, and improve patient outcomes. These tools allow researchers and clinicians to analyze biological systems that would otherwise be too complex to study directly.

Common quantitative approaches include:

- Exponential decay models
- Differential equations
- Statistical inference
- Optimization methods
- Population pharmacokinetics
- Machine learning systems

These methods support a wide range of applications, including:

- Drug development
- Precision medicine
- Personalized dosing
- Clinical decision support
- Therapeutic safety analysis

As medicine becomes increasingly data-driven, quantitative pharmacology continues to play a growing role in healthcare by transforming large amounts of biological and clinical data into actionable medical decisions.

<br>

### Zero-Order Drug Elimination

Zero-order elimination occurs when a constant *amount* of drug is removed per unit time, independent of concentration.

$$
\frac{dC}{dt} = -k
$$

This typically happens when metabolic pathways become saturated.

Key features:
- Constant elimination rate
- Non-proportional to concentration
- Risk of toxicity at high doses

Examples:
- Ethanol (at moderate/high levels)
- Phenytoin (at high concentrations)
- Aspirin (toxicity range)

<br>

### First-Order Drug Elimination

First-order elimination occurs when a constant *fraction* of drug is removed per unit time.

$$
\frac{dC}{dt} = -kC
$$

This is the most common pharmacokinetic model in clinical medicine.

Key features:
- Exponential decay behavior
- Constant half-life
- Proportional to concentration

Most drugs follow this pattern at therapeutic doses.

<br>

### Drug Half-Life Equation

The half-life is the time required for drug concentration to reduce by 50%.

$$
t_{1/2}=\frac{\ln 2}{k}
$$

Key implications:
- Determines dosing intervals
- Predicts accumulation in steady state
- Central to pharmacokinetic planning

<br>

### Infusion Rate Equation

The infusion rate describes how quickly a medication is delivered over time.

$$
\text{Infusion Rate}=\frac{\text{Dose}}{\text{Time}}
$$

Key applications:
- IV medication administration
- Critical care dosing
- Anesthesia management
- Continuous drug delivery systems

<br>

### Standard Uptake Value (SUV) in PET Imaging

The standardized uptake value (SUV) quantifies radiotracer uptake in positron emission tomography (PET) imaging.

$$
SUV=\frac{\text{Tissue Activity}}{\frac{\text{Injected Dose}}{\text{Body Weight}}}
$$

SUV provides a normalized measure of metabolic activity within tissues, allowing comparison across patients and imaging conditions. It is particularly important in oncology for assessing tumor metabolism and treatment response.


--- PAGE ---

## Laboratory Diagnostics

Laboratory diagnostics is the branch of medicine concerned with analyzing biological samples to evaluate physiological function, detect disease, monitor treatment response, and guide clinical decision-making. Modern laboratory medicine combines chemistry, biology, immunology, molecular genetics, and statistical analysis to transform measurable biological data into clinically meaningful information.

Laboratory testing is fundamentally quantitative. Measurements must be accurate, reproducible, and interpretable within physiological and pathological contexts. Many diagnostic systems therefore rely heavily on mathematical modeling, calibration theory, probability, and statistical inference.

<br>

### Complete Blood Count (CBC)

A Complete Blood Count (CBC) evaluates the cellular composition of blood and is one of the most commonly ordered laboratory tests in medicine.

Key components include:
- Red blood cell (RBC) count
- White blood cell (WBC) count
- Hemoglobin concentration
- Hematocrit
- Platelet count

One important relationship is hematocrit, which measures the proportion of blood volume occupied by red blood cells:

$$
\text{Hematocrit} =
\frac{\text{RBC Volume}}
{\text{Total Blood Volume}}
\times 100\%
$$

CBC analysis is used to evaluate:
- Anemia
- Infection
- Inflammation
- Bone marrow disorders
- Blood loss
- Hematologic malignancies

Because blood composition changes dynamically with physiology and disease, CBC interpretation often requires trend analysis over time rather than isolated measurements.

<br>

### Basic Metabolic Panel (BMP) and Comprehensive Metabolic Panel (CMP)

Metabolic panels evaluate electrolyte balance, kidney function, glucose regulation, and acid-base physiology.

Common analytes include:
- Sodium ($Na^+$)
- Potassium ($K^+$)
- Chloride ($Cl^-$)
- Bicarbonate ($HCO_3^-$)
- Glucose
- Creatinine
- Blood urea nitrogen (BUN)

A commonly derived clinical value is the anion gap:

$$
\text{Anion Gap} =
Na^+-(Cl^-+HCO_3^-)
$$

The anion gap helps clinicians identify metabolic acidosis and infer the presence of unmeasured acids within the bloodstream. Metabolic panels illustrate how laboratory medicine frequently relies on derived variables rather than direct measurements alone.

<br>

### Blood Gas Analysis

Arterial blood gas (ABG) testing evaluates respiratory function, oxygenation, and acid-base balance.

Major variables include:
- pH
- Partial pressure of oxygen ($PaO_2$)
- Partial pressure of carbon dioxide ($PaCO_2$)
- Bicarbonate concentration

Acidity is quantified logarithmically through the pH relationship:

$$
pH = -\log[H^+]
$$

Because pH is logarithmic, even small numerical changes can represent large physiological shifts in hydrogen ion concentration.

Blood gas analysis is essential in:
- Respiratory failure
- Shock states
- Critical care medicine
- Mechanical ventilation management
- Metabolic disorders

Interpretation often requires integrating multiple interacting variables simultaneously.

<br>

### Enzyme-Linked Immunosorbent Assay (ELISA)

ELISA is an immunological testing method used to detect specific proteins, antibodies, hormones, or infectious agents.

The test relies on:
- Antigen-antibody binding
- Enzyme-linked signal amplification
- Optical signal measurement

Measured signal intensity is generally proportional to biomarker concentration:

$$
\text{Signal Intensity}
\propto
\text{Biomarker Concentration}
$$

ELISA systems are widely used in:
- Infectious disease testing
- Hormone analysis
- Autoimmune disease evaluation
- Cancer biomarker detection

Because the method amplifies biological signals, calibration and statistical threshold selection are essential for accurate interpretation.

<br>

### Polymerase Chain Reaction (PCR)

Polymerase Chain Reaction (PCR) is a molecular amplification technique used to detect extremely small amounts of genetic material.

PCR repeatedly doubles target DNA sequences through thermal cycling:

$$
N = N_0 2^n
$$

where:
- $N_0$ is the initial quantity of DNA
- $n$ is the number of amplification cycles

PCR technology is foundational in:
- Infectious disease detection
- Genetic testing
- Oncology
- Forensic analysis
- Molecular biology research

Because amplification is exponential, PCR can detect very low concentrations of viral or genetic material with high sensitivity.

<br>

### Troponin Testing for Cardiac Injury

Troponin is a cardiac biomarker released into the bloodstream following injury to heart muscle cells.

Rather than relying on a single measurement, clinicians often evaluate serial changes over time:

$$
\Delta \text{Troponin}
=
\text{Serial Change Over Time}
$$

Dynamic change patterns are important because:
- Rising values may indicate acute myocardial injury
- Stable elevations may reflect chronic disease
- Falling values may indicate recovery or resolution

Troponin interpretation therefore depends heavily on temporal trend analysis combined with clinical context and electrocardiographic findings.

<br>

### Hemoglobin A1C and Long-Term Glucose Control

Hemoglobin A1C (HbA1C) estimates average blood glucose levels over approximately two to three months by measuring glucose attachment to hemoglobin molecules.

A commonly used approximation for estimated average glucose (eAG) is:

$$
eAG \approx
28.7(A1C)-46.7
$$

HbA1C testing is important in:
- Diabetes diagnosis
- Long-term glucose monitoring
- Treatment evaluation
- Risk prediction for diabetic complications

Unlike single glucose measurements, HbA1C reflects cumulative glycemic exposure over time.

<br>

### Urinalysis

Urinalysis evaluates the chemical and microscopic composition of urine to assess renal function, hydration status, infection, and metabolic abnormalities.

Common measurements include:
- Specific gravity
- Protein concentration
- Glucose
- Ketones
- Blood
- White blood cells
- Bacterial content

Specific gravity compares urine density to water:

$$
\text{Specific Gravity} =
\frac{\rho_{\text{urine}}}
{\rho_{\text{water}}}
$$

This measurement provides insight into:
- Kidney concentrating ability
- Hydration status
- Solute concentration
- Renal dysfunction

Urinalysis combines direct chemical measurement with microscopic pattern recognition, making it both quantitative and interpretive in nature.


--- PAGE ---

## Specialized & Technical Medicine

Specialized and technical medical fields integrate medicine with genetics, neuroscience, signal processing, statistics, physics, and computational modeling. These disciplines often rely heavily on quantitative analysis in order to measure complex biological behavior, detect hidden physiological patterns, and predict disease risk.

Modern technical medicine increasingly depends on large-scale datasets, probabilistic modeling, biomedical instrumentation, and computational interpretation systems. As a result, mathematics and computer science have become deeply integrated into advanced medical diagnostics and research.

<br>

### Genetic Sequencing and Genome-Wide Analysis

Genetic sequencing analyzes the nucleotide structure of DNA in order to identify genetic variation, inherited traits, and disease-associated mutations.

Genome-wide analysis examines:
- Single nucleotide polymorphisms (SNPs)
- Structural variants
- Gene expression patterns
- Mutation frequencies
- Population-level genetic variation

Modern sequencing systems generate extremely large biological datasets that require:
- Statistical inference
- Pattern recognition
- Computational alignment algorithms
- Probabilistic modeling
- Machine learning techniques

Genome analysis is central to:
- Precision medicine
- Cancer genomics
- Inherited disease detection
- Evolutionary biology
- Pharmacogenomics

Because genetic information is inherently high-dimensional, computational analysis has become essential for modern genomic medicine.

<br>

### Polygenic Risk Score Calculation

Many diseases are influenced by numerous genetic variants that each contribute a small amount to overall disease susceptibility. Polygenic risk scores (PRS) combine these weighted contributions into a single predictive estimate:

$$
PRS=
\sum (\beta_i x_i)
$$

where:
- $\beta_i$ represents the statistical effect size of a genetic variant
- $x_i$ represents the presence or magnitude of that variant

This structure closely resembles:
- Linear regression
- Weighted scoring systems
- Machine learning classifiers
- Neural network weighting models

Polygenic modeling is used in:
- Cardiovascular risk prediction
- Cancer susceptibility analysis
- Psychiatric genetics
- Population screening
- Predictive genomics

These systems illustrate how complex biological behavior can often be modeled through aggregation of many small probabilistic effects.

<br>

### Electroencephalography (EEG) Neural Activity Measurement

Electroencephalography (EEG) measures electrical activity generated by neuronal signaling within the brain.

Complex neural waveforms can be represented as combinations of oscillatory frequency components:

$$
EEG(t)=
\sum A_i\sin(\omega_i t)
$$

where:
- $A_i$ represents signal amplitude
- $\omega_i$ represents angular frequency

EEG signals are commonly analyzed using:
- Fourier transforms
- Spectral decomposition
- Signal filtering
- Frequency-domain analysis
- Time series methods

Different frequency bands are associated with distinct neurological states, including:
- Sleep
- Attention
- Seizure activity
- Cognitive processing
- Consciousness states

Because EEG signals are highly noisy and dynamic, computational signal processing plays a major role in interpretation.

<br>

### Electromyography (EMG) Muscle Electrical Activity Testing

Electromyography (EMG) measures electrical activity generated during muscle contraction.

A simplified relationship may be expressed as:

$$
EMG(t)\propto
\text{muscle activation}
$$

EMG analysis evaluates:
- Motor neuron activity
- Muscle recruitment
- Signal amplitude
- Timing relationships
- Neuromuscular coordination

Applications include:
- Neurological diagnosis
- Rehabilitation medicine
- Prosthetic control systems
- Sports medicine
- Biomechanics

Because muscle activation patterns vary over time, EMG systems rely heavily on:
- Signal processing
- Noise filtering
- Pattern recognition
- Temporal analysis

EMG therefore serves as an important example of biomedical signal analysis applied to human physiology.

<br>

### Functional Cardiac Stress Testing

Functional cardiac stress testing evaluates cardiovascular performance under increased physiological demand.

Cardiac output is commonly modeled as:

$$
CO = HR \times SV
$$

where:
- $CO$ is cardiac output
- $HR$ is heart rate
- $SV$ is stroke volume

Stress testing examines how the cardiovascular system responds to:
- Exercise
- Pharmacologic stimulation
- Increased metabolic demand
- Oxygen consumption requirements

These tests are used to evaluate:
- Coronary artery disease
- Cardiac ischemia
- Exercise tolerance
- Arrhythmias
- Functional cardiovascular capacity

Stress testing integrates multiple physiological systems simultaneously, including:
- Cardiac dynamics
- Respiratory function
- Blood pressure regulation
- Oxygen transport
- Metabolic demand