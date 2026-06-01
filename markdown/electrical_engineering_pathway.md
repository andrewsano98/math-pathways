<!--
title: "Math in Electrical Engineering"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/electrical_engineering_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Electrical Engineering
    </h1>
  </div>

</div>

<br>

### What will I be doing?
- Designing and analyzing electrical circuits, systems, and components such as resistors, capacitors, and transistors  
- Building and testing electronic systems using simulation software and physical prototyping tools  
- Developing embedded systems and hardware control logic for devices and machinery  
- Using MATLAB, SPICE, or similar tools to simulate circuit behavior and signal responses  
- Working with power systems to generate, transmit, and distribute electrical energy efficiently  
- Designing communication systems that transmit signals through wired or wireless channels  
- Testing and troubleshooting electrical systems to ensure safety, efficiency, and reliability  


### What are the most common jobs?
- Electrical Engineer  
- Electronics Engineer  
- Power Systems Engineer  
- Control Systems Engineer  
- Telecommunications Engineer  
- Circuit Design Engineer  
- Embedded Systems Engineer  
- Signal Processing Engineer  

### What math concepts do I need to know?
- Calculus  
- Differential Equations  
- Linear Algebra  
- Complex Numbers  
- Algebra  
- Statistics  
- Fourier Analysis  
- Graphing and Functions  
- Systems of Equations  

--- PAGE ---

## Circuit Analysis

Circuit analysis is the study of how electrical quantities such as current, voltage, and charge evolve within electrical networks. Because many circuits operate under time-varying conditions, particularly in alternating current (AC) systems, calculus becomes a fundamental tool for describing and predicting circuit behavior.

<br>

### Time-Varying Current and Voltage

In dynamic circuits, current and voltage are not constant but change continuously with time. These changes are naturally described using derivatives, which capture rates of change.

Current is defined as the rate of flow of electric charge:

$$
I(t) = \frac{dQ}{dt}
$$

Where:
- $I(t)$ = current at time $t$  
- $Q(t)$ = electric charge  

This relationship shows that current is fundamentally a dynamic quantity derived from how charge accumulates or moves through a system.

For inductive elements, voltage is related to the rate of change of current:

$$
V(t) = L\frac{dI}{dt}
$$

Where:
- $V(t)$ = voltage across an inductor  
- $L$ = inductance  
- $\frac{dI}{dt}$ = rate of change of current  

This equation reflects the fact that inductors resist changes in current, producing voltage in response to dynamic variation.

<br>

### Total Charge and Integral Relationships

While derivatives describe instantaneous change, integrals describe accumulation over time. In circuit systems, charge can be recovered from current by integrating over a time interval:

$$
Q(t) = \int I(t)\,dt
$$

Where:
- $Q(t)$ = total accumulated charge  
- $I(t)$ = current function over time  

This relationship is essential for understanding how charge builds up in capacitors and how energy is stored in electrical fields.

Integration provides a complementary perspective to differentiation, linking instantaneous behavior to long-term system accumulation.

<br>

### Physical Interpretation of Dynamic Circuits

Together, these relationships describe the fundamental time-dependent structure of electrical circuits:

- Current represents the *flow* of charge  
- Voltage represents *energy potential differences*  
- Inductors respond to changes in current  
- Capacitors store charge over time  

These interactions create systems that evolve dynamically rather than remaining static.

<br>

### Applications in Electrical Systems

Calculus-based circuit analysis is essential in a wide range of engineering applications:

- **Capacitor and inductor behavior** — modeling energy storage and release  
- **Time-dependent circuit response** — analyzing transient behavior in switching systems  
- **Signal variation in power systems** — understanding fluctuations in AC transmission  

In practical engineering, these tools allow designers to predict how circuits respond not only in steady-state conditions, but also during transitions, disturbances, and oscillatory behavior.

Circuit analysis therefore forms the foundational mathematical language for all dynamic electrical systems.


--- PAGE ---

## Linear Algebra in Circuit Networks

Modern electrical circuits often consist of large, interconnected networks containing many nodes and loops. As circuits scale in complexity, solving them manually becomes impractical. Linear algebra provides a structured framework for representing and solving these systems efficiently using matrices and vectors.

Instead of analyzing individual components in isolation, circuit behavior is expressed as a system of simultaneous equations.

<br>

### Node Voltage Analysis (Kirchhoff’s Current Law Formulation)

Node voltage analysis is based on Kirchhoff’s Current Law (KCL), which states that the sum of currents entering a node must equal the sum of currents leaving it.

For a network of nodes, this system can be written in matrix form:

$$
\mathbf{G}\mathbf{V} = \mathbf{I}
$$

Where:
- $\mathbf{G}$ = conductance matrix (circuit connectivity and element values)  
- $\mathbf{V}$ = vector of node voltages  
- $\mathbf{I}$ = vector of injected currents  

This formulation transforms a complex circuit into a solvable linear system.

Key characteristics:
- Each equation represents conservation of current at a node  
- Unknowns are node voltages relative to a reference point  
- System size scales with number of nodes  

Node analysis is especially powerful for large electrical networks and computer-aided circuit design.

<br>

### Mesh Current Analysis (Loop Equation Formulation)

Mesh current analysis focuses on closed loops within a circuit and applies Kirchhoff’s Voltage Law (KVL), which states that the sum of voltage drops around any closed loop is zero.

This system is expressed in matrix form as:

$$
\mathbf{Z}\mathbf{I} = \mathbf{V}
$$

Where:
- $\mathbf{Z}$ = impedance matrix (resistance, inductance, capacitance effects)  
- $\mathbf{I}$ = vector of mesh currents  
- $\mathbf{V}$ = vector of voltage sources  

This representation converts loop-based constraints into a solvable linear algebra problem.

Key characteristics:
- Each equation corresponds to a closed loop in the circuit  
- Unknowns are loop (mesh) currents  
- Useful for planar circuit structures  

Mesh analysis is particularly effective in circuits with fewer loops than nodes.

<br>

### Matrix Interpretation of Circuit Behavior

Both node and mesh methods share a common structure:

- Electrical networks become linear systems  
- Physical laws become algebraic constraints  
- Unknown electrical quantities become vectors  
- Component relationships become matrices  

This abstraction allows engineers to apply computational methods rather than manual calculation.

<br>

### Applications in Engineering Systems

Linear algebra in circuit networks is fundamental to many areas of electrical engineering:

- **Power grid modeling** — analyzing large-scale transmission systems  
- **Integrated circuit design** — solving complex transistor-level networks  
- **Electrical network simulation** — enabling computer-aided design (CAD) tools  

As circuit complexity increases, matrix-based methods become not just useful, but essential for practical analysis and design.


--- PAGE ---

## AC Circuits, Phasors, and Complex Numbers

Alternating current (AC) circuits involve voltages and currents that vary sinusoidally over time. Unlike direct current systems, where values remain constant, AC systems require a mathematical framework capable of capturing oscillation, phase shifts, and frequency-dependent behavior. Complex numbers and phasors provide this framework by transforming time-dependent differential equations into simpler algebraic forms.

<br>

### Phasor Representation of Sinusoidal Signals

A sinusoidal signal can be expressed compactly using complex exponentials. This representation, known as a **phasor**, encodes both magnitude and phase information.

$$
V(t) = V_0 e^{j\omega t}
$$

Where:
- $V_0$ = amplitude of the signal  
- $\omega$ = angular frequency  
- $j$ = imaginary unit ($j^2 = -1$)  

This formulation is powerful because it converts oscillatory behavior into exponential form, enabling easier mathematical manipulation.

Key idea:
- Time-domain oscillations become rotations in the complex plane  

<br>

### Impedance in RLC Circuits

In AC analysis, resistance alone is not sufficient to describe circuit behavior. Instead, each component contributes a frequency-dependent quantity called **impedance**, which generalizes resistance to complex-valued systems.

$$
Z_R = R,\quad Z_L = j\omega L,\quad Z_C = \frac{1}{j\omega C}
$$

Where:
- $Z_R$ = resistance (real-valued impedance)  
- $Z_L$ = inductive reactance (frequency-dependent)  
- $Z_C$ = capacitive reactance (inverse frequency dependence)  

These expressions show that:
- Inductors resist changes in current more strongly at high frequencies  
- Capacitors oppose low-frequency signals more strongly  
- Resistors remain constant across all frequencies  

Together, these elements define the frequency response of an AC circuit.

<br>

### Ohm’s Law in Complex Form

Using phasors and impedance, Ohm’s law extends naturally into the complex domain:

$$
V = IZ
$$

Where:
- $V$ = complex voltage phasor  
- $I$ = complex current phasor  
- $Z$ = impedance  

This formulation transforms differential equations into simple algebraic equations, significantly simplifying circuit analysis in the frequency domain.

<br>

### Physical Interpretation of Phasors

Phasor analysis provides a geometric interpretation of AC systems:

- Magnitude corresponds to signal strength  
- Phase corresponds to timing shift  
- Complex multiplication represents rotation and scaling  

This allows engineers to analyze synchronization, resonance, and interference effects in a unified mathematical framework.

<br>

### Applications in Electrical Engineering

Complex number and phasor analysis are essential in many domains of electrical engineering:

- **Power systems analysis** — understanding voltage and current distribution in AC grids  
- **Filter design** — shaping frequency response in analog and digital systems  
- **Signal phase and frequency analysis** — studying oscillations in communication and control systems  

Phasor methods remain one of the most important tools for simplifying and understanding AC circuit behavior in both theoretical and applied engineering contexts.


--- PAGE ---

## Signal Processing and Fourier Analysis

Signal processing is the study of how information-bearing signals such as sound, images, and communication waveforms can be analyzed, transformed, and reconstructed. A central idea in this field is that complex signals in the time domain can be decomposed into simpler sinusoidal components in the frequency domain. Fourier analysis provides the mathematical framework for this decomposition.

<br>

### Fourier Transform

The Fourier transform converts a time-domain signal into its frequency-domain representation. This allows engineers to analyze which frequencies are present in a signal and how much each contributes.

$$
X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t}dt
$$

Where:
- $x(t)$ = time-domain signal  
- $X(\omega)$ = frequency-domain representation  
- $\omega$ = angular frequency  
- $j$ = imaginary unit  

Key interpretation:
- Time signals are expressed as a sum of continuous frequency components  
- Each frequency component carries amplitude and phase information  

This transformation is fundamental for analyzing oscillatory and wave-based systems.

<br>

### Inverse Fourier Transform

The inverse Fourier transform reconstructs the original time-domain signal from its frequency components:

$$
x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(\omega)e^{j\omega t}d\omega
$$

Where:
- $X(\omega)$ = frequency representation  
- $x(t)$ = reconstructed time signal  

This relationship ensures that no information is lost between domains, making Fourier analysis a complete and reversible representation of signals.

<br>

### Frequency-Domain Interpretation

Fourier analysis provides a dual perspective on signals:

- Time domain: describes how a signal changes over time  
- Frequency domain: describes what frequencies compose the signal  

This duality is essential for understanding:
- Oscillations  
- Wave interference  
- Signal filtering  
- System response  

Many engineering problems become simpler when viewed in the frequency domain rather than the time domain.

<br>

### Applications in Engineering Systems

Fourier analysis is widely used across electrical and computational engineering:

- **Audio processing** — equalization, compression, and sound synthesis  
- **Image compression** — frequency-based encoding and reduction of redundancy  
- **Wireless communication** — modulation and bandwidth analysis  
- **Noise filtering and signal reconstruction** — removing unwanted frequency components  

These applications rely on separating meaningful information from noise or redundancy in the frequency spectrum.

<br>

### Statistical and Information-Theoretic Concepts

Real-world signals are often corrupted by noise, requiring statistical modeling techniques.

Key concepts include:
- **Noise modeling** — representing random fluctuations in signals  
- **Error probability** — likelihood of incorrect signal interpretation  
- **Signal-to-noise ratio (SNR)** — measure of signal strength relative to background noise  

SNR is commonly expressed as:

$$
\text{SNR} = \frac{P_{\text{signal}}}{P_{\text{noise}}}
$$

Higher SNR values indicate clearer and more reliable signal transmission.


--- PAGE ---

## Vector Calculus and Electromagnetics

Electromagnetics describes how electric and magnetic fields interact, propagate, and evolve in space and time. Unlike circuit theory, which focuses on lumped components, electromagnetic theory treats electrical phenomena as continuous fields distributed across space. Vector calculus provides the mathematical language necessary to describe these spatially varying quantities.

<br>

### Electric Field Divergence and Gauss’s Law

Electric fields originate from electric charges and spread through space. The relationship between charge density and electric field behavior is described by Gauss’s law in differential form:

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$

Where:
- $\nabla \cdot \mathbf{E}$ = divergence of the electric field  
- $\mathbf{E}$ = electric field vector  
- $\rho$ = charge density  
- $\epsilon_0$ = permittivity of free space  

Key interpretation:
- Positive charge acts as a source of electric field lines  
- Negative charge acts as a sink  
- Divergence measures how strongly field lines originate or terminate at a point  

This equation forms the foundation of electrostatics and field-based circuit interpretation.

<br>

### Magnetic Field Curl and Ampère–Maxwell Law

Magnetic fields are generated by electric currents and changing electric fields. This relationship is captured by the Ampère–Maxwell law:

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

Where:
- $\nabla \times \mathbf{B}$ = curl of the magnetic field  
- $\mathbf{B}$ = magnetic field vector  
- $\mathbf{J}$ = current density  
- $\mu_0$ = permeability of free space  
- $\frac{\partial \mathbf{E}}{\partial t}$ = time-varying electric field  

Key interpretation:
- Electric currents produce circulating magnetic fields  
- Changing electric fields also generate magnetic fields  
- Curl measures rotational structure in a vector field  

This law is central to understanding dynamic electromagnetic systems.

<br>

### Physical Meaning of Field Operations

Vector calculus operations provide intuitive physical interpretations:

- **Divergence** → measures sources and sinks of fields  
- **Curl** → measures rotation or circulation of fields  
- **Gradient** → measures spatial rate of change  

Together, these operations describe how fields behave locally and globally in space.

<br>

### Electromagnetic Wave Propagation

Maxwell’s equations collectively imply the existence of electromagnetic waves, where electric and magnetic fields propagate through space as coupled oscillations.

These waves:
- Travel at the speed of light in vacuum  
- Carry energy and momentum  
- Exhibit both electric and magnetic components perpendicular to each other  

This theoretical result underlies all modern wireless communication systems.

<br>

### Applications in Electrical Engineering

Vector calculus and electromagnetics are essential in the design and analysis of many real-world systems:

- **Antenna design** — shaping radiation patterns and signal directionality  
- **Transmission lines** — modeling signal propagation along conductors  
- **Electromagnetic wave propagation** — analyzing radio, microwave, and optical signals  
- **Wireless communication systems** — enabling long-distance information transfer  

These principles form the physical foundation of modern communication and electromagnetic engineering.

--- PAGE ---

## Laplace Transforms and Control Systems

Many electrical and mechanical systems are dynamic in nature, meaning their behavior evolves over time in response to inputs, disturbances, and feedback. Control systems aim to regulate this behavior, ensuring stability, accuracy, and desired performance. The Laplace transform provides a powerful mathematical tool for analyzing such systems by converting time-domain differential equations into algebraic equations in the complex frequency domain.

<br>

### Laplace Transform Definition

The Laplace transform maps a time-domain function into a complex frequency-domain representation:

$$
F(s) = \int_0^\infty f(t)e^{-st}dt
$$

Where:
- $f(t)$ = time-domain signal or system response  
- $F(s)$ = transformed function in the complex frequency domain  
- $s$ = complex variable ($s = \sigma + j\omega$)  

Key interpretation:
- Time-dependent behavior is encoded into algebraic form  
- Exponential decay and oscillation are captured simultaneously  
- System dynamics become easier to analyze and manipulate  

<br>

### Transforming Differential Equations

One of the most important advantages of the Laplace transform is its ability to convert differential equations into algebraic equations.

In the time domain, systems are often described by differential equations. After transformation, derivatives become polynomial terms in $s$, allowing for simpler solution methods.

Key benefit:
- Differential operators → algebraic expressions in $s$  
- Complex dynamic systems become solvable using linear algebra techniques  

This transformation is central to modern control theory.

<br>

### System Interpretation in the Frequency Domain

In the Laplace domain:
- Poles represent system stability characteristics  
- Zeros represent response behavior and system attenuation  
- Transfer functions describe input-output relationships  

A general system is often expressed as:

$$
G(s) = \frac{Y(s)}{X(s)}
$$

Where:
- $G(s)$ = transfer function  
- $Y(s)$ = output response  
- $X(s)$ = input signal  

This representation allows engineers to analyze system behavior without directly solving time-dependent equations.

<br>

### Stability and Dynamic Response

Control systems are evaluated based on their stability and response characteristics:

- Stable systems return to equilibrium after disturbances  
- Unstable systems grow without bound over time  
- Critically stable systems oscillate at the boundary of stability  

The location of poles in the complex plane determines system stability.

Key idea:
- Left-half plane poles → stable systems  
- Right-half plane poles → unstable systems  

<br>

### Applications in Engineering Systems

Laplace transform methods are widely used in engineering applications involving dynamic feedback and control:

- **Motor control systems** — regulating speed and torque in electric motors  
- **Robotics and automation** — controlling motion and mechanical response  
- **Voltage regulation systems** — maintaining stable electrical output in power systems  
- **Stability analysis of feedback systems** — ensuring reliable system behavior under feedback loops  

These applications rely on the ability to predict system behavior before physical implementation.


--- PAGE ---

## Probability, Statistics, and Communication Systems

Modern communication systems operate in environments that are inherently uncertain. Signals transmitted through physical media such as air, fiber optics, or electrical cables are subject to noise, interference, and distortion. Probability and statistics provide the mathematical framework for modeling these uncertainties and designing systems that remain reliable under imperfect conditions.

<br>

### Random Noise Modeling

Noise refers to unwanted random variation that interferes with signal transmission and reception. In communication systems, noise is typically modeled as a stochastic process.

Common characteristics include:
- Random amplitude fluctuations  
- Frequency-dependent distortion  
- Additive or multiplicative effects on signals  

A common idealized model is additive noise:

$$
Y = X + N
$$

Where:
- $X$ = transmitted signal  
- $N$ = noise component  
- $Y$ = received signal  

This framework allows engineers to analyze how noise affects signal integrity and system performance.

<br>

### Error Detection and Correction Codes

Because noise can corrupt transmitted information, communication systems use encoding schemes to detect and correct errors.

Key ideas include:
- Redundant encoding of information  
- Detection of inconsistencies in received data  
- Correction of a limited number of errors without retransmission  

These methods rely heavily on probability theory to determine:
- Likelihood of error occurrence  
- Optimal redundancy levels  
- Trade-offs between efficiency and reliability  

Error-correcting codes are essential for reliable digital communication across noisy channels.

<br>

### Channel Capacity

Channel capacity defines the maximum rate at which information can be transmitted over a communication channel with arbitrarily low error probability.

A foundational result in information theory is Shannon’s capacity concept:

$$
C = B \log_2(1 + \text{SNR})
$$

Where:
- $C$ = channel capacity (bits per second)  
- $B$ = bandwidth  
- $\text{SNR}$ = signal-to-noise ratio  

Key interpretation:
- Higher bandwidth increases data throughput  
- Higher noise reduces reliable transmission rate  
- There exists a fundamental upper bound on communication efficiency  

<br>

### Bit Error Rate (BER)

The bit error rate measures the probability that a transmitted bit is incorrectly received.

$$
\text{BER} = \frac{\text{Number of erroneous bits}}{\text{Total number of transmitted bits}}
$$

Where:
- A lower BER indicates higher communication reliability  
- BER depends on modulation scheme, noise level, and coding strategy  

Engineers use BER as a primary metric for evaluating communication system performance.

<br>

### Wireless Communication Reliability

Wireless systems are particularly affected by:
- Signal attenuation  
- Multipath interference  
- Environmental noise  
- Mobility and changing transmission conditions  

Statistical modeling allows engineers to:
- Predict performance under varying conditions  
- Design robust modulation schemes  
- Optimize antenna and receiver design  

<br>

### Data Transmission Efficiency

Efficiency in communication systems is defined by the balance between:
- Data rate (throughput)  
- Reliability (error probability)  
- Bandwidth usage  

Improving one aspect often impacts the others, making system design a multi-variable optimization problem.


--- PAGE ---

## Integrated System Design Perspective

Modern electrical engineering is not organized around a single mathematical tool, but rather a synthesis of multiple mathematical frameworks applied simultaneously. Real-world systems—ranging from microprocessors to power grids and wireless communication networks—require engineers to combine algebraic, differential, probabilistic, and geometric methods into a unified design approach.

<br>

### Mathematical Roles in Electrical Systems

Each branch of mathematics contributes a distinct perspective on system behavior:

- **Linear algebra: circuit structure**  
  Electrical networks are represented as systems of equations, where voltages and currents are solved using matrices and vectors.

- **Calculus: dynamic behavior**  
  Time-dependent changes in current, voltage, and charge are described using derivatives and integrals.

- **Fourier analysis: signal decomposition**  
  Complex signals are broken into frequency components to enable filtering, compression, and spectral analysis.

- **Probability: noise and uncertainty**  
  Random fluctuations in signals and system behavior are modeled statistically to ensure robustness.

- **Vector calculus: field behavior**  
  Electromagnetic fields are described in continuous space using divergence, curl, and gradient operators.

- **Laplace transforms: system stability**  
  Dynamic systems are converted into the frequency domain to analyze stability, control response, and feedback behavior.

<br>

### Unified System Modeling

In practice, a single engineering system often requires multiple mathematical perspectives at once. For example:

- A communication system uses Fourier analysis for signal processing  
- It uses probability theory to model noise and errors  
- It uses linear algebra for coding and decoding algorithms  
- It uses calculus to model time-varying signals  
- It uses Laplace transforms for filter and control design  
- It uses vector calculus for antenna and wave propagation analysis  

This layered structure reflects the complexity of real-world systems, where no single mathematical framework is sufficient on its own.