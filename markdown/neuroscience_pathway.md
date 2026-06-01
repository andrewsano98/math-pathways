<!--
title: "Math in Neuroscience"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/neuroscience_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Neuroscience
    </h1>
  </div>

</div>

<br>

###  What will I be doing? 
- Collecting neural data using EEG, fMRI, PET scans, and electrophysiology recording systems  
- Processing and analyzing brain data using Python, MATLAB, and neuroscience-specific toolboxes  
- Running statistical and computational models to study neural activity, cognition, and behavior  
- Applying signal processing techniques to clean and interpret neural signals  
- Using machine learning methods to classify brain states or decode neural patterns  
- Designing and running controlled experiments to test hypotheses about brain function  
- Interpreting neuroimaging and behavioral data to study neurological disorders and cognition  


<br>

###  What are the most common jobs?
- Neuroscientist  
- Neurologist  
- Cognitive Scientist  
- Neuropsychologist  
- Biomedical Researcher  
- Clinical Neuroscientist  
- Neuroimaging Analyst  
- Computational Neuroscientist  


<br>

###  What math concepts do I need to know?
- Statistics  
- Probability  
- Calculus  
- Linear Algebra  
- Differential Equations  
- Data Analysis  
- Signal Processing  
- Graph Theory  
- Machine Learning Basics  

--- PAGE ---

## Neurons and Electrical Signaling

Neurons are specialized biological cells designed to transmit information through a combination of electrical impulses and chemical signaling. At the core of this system is the **action potential**, a rapid, temporary change in voltage across the neuron's membrane that propagates along the axon.

This process can be interpreted as a biological signal transmission system governed by electrochemical gradients, where ion movement creates controlled changes in membrane potential.


<br>

###  Membrane Potential and Electrical State

At rest, a neuron maintains a voltage difference across its membrane known as the **resting membrane potential**. This arises from uneven distributions of ions such as sodium (Na⁺), potassium (K⁺), and chloride (Cl⁻).

- The inside of the neuron is typically more negative than the outside
- This difference is maintained by ion pumps and selective membrane permeability

The membrane potential can be thought of as a stored electrical state, similar to a charged capacitor in a circuit.


<br>

###  Action Potentials as Signal Pulses

An action potential is a rapid sequence of voltage changes that travels along the axon. It follows a threshold-based process:

1. A stimulus causes depolarization
2. If a threshold is reached, voltage-gated channels open
3. Sodium ions rush in, rapidly increasing voltage
4. Potassium ions exit, restoring the negative state
5. The neuron resets during a refractory period

This creates a binary-like signal:
- Below threshold - no signal
- Above threshold - full signal spike

This all-or-nothing behavior makes neural signaling robust against noise.


<br>

###  Signal Propagation Along the Axon

Once initiated, the action potential propagates along the axon without losing strength. This occurs through a chain reaction of depolarization between adjacent membrane segments.

Two key mechanisms improve transmission speed:
- **Myelination**: insulating layers that prevent ion leakage
- **Nodes of Ranvier**: gaps where the signal is actively regenerated

This allows signals to effectively "jump" along the axon, increasing transmission efficiency.


<br>

###  Mathematical Interpretation of Signal Flow

Neural signaling can be modeled using electrical circuit analogies:

- Membrane behaves like a capacitor
- Ion channels behave like variable resistors
- Ion gradients behave like voltage sources

A simplified representation of membrane dynamics is:

$$ C \frac{dV}{dt} = I_{\text{ion}} $$

Where:
- $C$ is membrane capacitance  
- $V$ is membrane potential  
- $I_{\text{ion}}$ is ionic current  

This expresses how changes in voltage depend on ion flow over time.


<br>

###  Information Encoding in Neurons

Neurons do not encode information by signal strength, but by **frequency and timing**:

- Stronger stimuli - higher firing rate
- Different patterns - different information signals
- Temporal coordination - network-level computation

This converts biological activity into a structured information system.


<br>

###  Network Behavior and Emergent Computation

A single neuron is simple, but networks of neurons produce complex behavior:

- Sensory processing (vision, hearing, touch)
- Motor control (movement coordination)
- Memory formation (synaptic strengthening)
- Decision-making (distributed computation)

Synapses adjust their strength over time, allowing learning through structural change.


<br>

###  Neural Signaling as a Physical System

Although biological in origin, neurons obey strict physical laws:

- Electrochemical gradients drive ion flow
- Voltage changes follow differential dynamics
- Signal propagation depends on conductivity and resistance
- Network behavior emerges from coupled nonlinear systems

This makes neural systems a direct example of biology implementing physical signal theory through electrochemical constraints and threshold-based dynamics.

--- PAGE ---

## Synapses and Chemical Communication

Synapses are specialized junctions where neurons communicate with each other using chemical signals known as neurotransmitters. Unlike the electrical signaling that travels along an axon, synaptic transmission involves a conversion from electrical energy into chemical signaling and then back into electrical activity in the receiving neuron.

This makes synapses a key interface between two different modes of information transfer: electrical and chemical.


<br>

###  The Synaptic Transmission Process

When an action potential reaches the end of a neuron (the presynaptic terminal), it triggers a sequence of events:

1. Voltage-gated calcium channels open
2. Calcium ions (Ca²⁺) enter the presynaptic terminal
3. Synaptic vesicles fuse with the membrane
4. Neurotransmitters are released into the synaptic cleft
5. Neurotransmitters bind to receptors on the postsynaptic neuron

This process converts an electrical signal into a chemical signal across a tiny gap.


<br>

###  Excitatory and Inhibitory Effects

Neurotransmitters do not all produce the same effect. They influence whether the next neuron is more or less likely to fire:

- **Excitatory synapses** increase the probability of an action potential
- **Inhibitory synapses** decrease the probability of an action potential

This is determined by how neurotransmitter binding changes ion flow in the postsynaptic membrane.


<br>

###  Synaptic Potentials and Threshold Dynamics

Instead of immediate full action potentials, synapses produce graded changes in membrane voltage called synaptic potentials:

- Excitatory postsynaptic potentials (EPSPs)
- Inhibitory postsynaptic potentials (IPSPs)

These signals combine through a process called **summation**:

- Temporal summation: repeated signals over time
- Spatial summation: multiple synapses contributing simultaneously

If the combined input crosses a threshold, the neuron fires an action potential.

<br>

###  Mathematical View of Synaptic Integration

Synaptic input can be modeled as a weighted accumulation of signals:

$$ V(t) = \sum w_i s_i(t) $$

Where:
- $V(t)$ is the membrane potential at time $t$
- $w_i$ represents synaptic strength (weight)
- $s_i(t)$ represents incoming synaptic signals

A neuron therefore combines many incoming signals into a single electrical state that evolves over time.


<br>

###  Synaptic Strength and Plasticity

Synapses are not fixed; their strength changes over time through a process called **synaptic plasticity**.

Key mechanisms include:
- Long-term potentiation (LTP): strengthening of synaptic connections
- Long-term depression (LTD): weakening of synaptic connections

These changes depend on activity patterns and timing between neurons.

<br>

### Neurotransmitters

Neurons communicate using chemical messengers called **neurotransmitters**, each of which affects neural activity in different ways. Some neurotransmitters increase the likelihood that a neuron will fire, while others suppress activity or alter how signals are processed throughout the network. For example, glutamate is typically associated with excitatory signaling, while GABA is commonly associated with inhibitory signaling. Dopamine plays an important role in reward and motivation systems, serotonin is involved in mood and regulation, and acetylcholine contributes to attention and muscle activation. These chemicals interact with specialized receptor systems, allowing neural communication to become highly selective and functionally specialized.

<br>

### Signal Conversion as an Information System

Synaptic communication can be understood as a multi-stage information processing system in which electrical and chemical signals are continuously converted into one another. When an electrical impulse reaches the end of a neuron, neurotransmitters are released into the synapse and bind to receptors on the next neuron, producing a new electrical response. This process can be summarized conceptually as:

<br>

$$
\text{Electrical signal} \rightarrow \text{chemical release} \rightarrow \text{receptor activation} \rightarrow \text{electrical response}
$$

<br>

Because multiple stages are involved, neural signaling is not purely mechanical or linear. Synapses can strengthen, weaken, filter, or modulate signals depending on receptor behavior, neurotransmitter concentration, and prior neural activity. As a result, information transmission in the brain depends on both electrical dynamics and chemical state.

<br>

### Synapses as Computational Units

From a computational perspective, synapses behave similarly to adjustable processing units within a large network. Each synapse influences how strongly one neuron affects another, effectively assigning different “weights” to incoming signals. Some signals may be amplified, while others are suppressed or ignored entirely depending on the state of the network.

Synapses also introduce threshold-like behavior, since neurons generally fire only when incoming activity exceeds certain activation levels. In addition, synaptic strength can change over time through learning and plasticity. These properties make neural systems comparable to weighted network structures in mathematics and computer science, where connections determine how information moves through the system.

<br>

### Encoding as Pattern Formation

When new information is encountered, sensory systems first convert external stimuli into neural activity patterns. This activity then spreads through interconnected neural networks, where synaptic connections may strengthen or weaken through processes associated with learning and plasticity. Over time, the resulting activity pattern becomes associated with the experience itself.

Rather than storing exact copies of events, the brain encodes information through relationships between neurons and the patterns of activity they produce together. Memory formation is therefore better understood as the creation and reinforcement of structured neural pathways rather than the storage of isolated data points.

<br>

### Distributed Representation

Memories and cognitive processes are distributed across many different regions of the brain rather than stored in a single location. Different components of an experience are processed by specialized neural systems. For example, visual information is strongly associated with visual cortex regions, emotional responses involve structures such as the amygdala, spatial context is linked to the hippocampus, and movement-related information involves motor systems.

As a result, a single memory is not stored in one neuron or one isolated area. Instead, memories emerge from coordinated activity across large interconnected networks. This creates a distributed storage architecture in which information is represented through patterns of connectivity and shared neural activation.

<br>

### Types of Memory Systems

Different forms of memory rely on partially distinct neural systems, each optimized for different durations, functions, and types of information processing.

1. **Short-Term Memory**

> - Temporary maintenance of information through active neural firing  
> - Sustained electrical activity across localized neural circuits  
> - Limited storage capacity and short duration (seconds to minutes without reinforcement)  
> - Easily disrupted by distraction or competing input  
> - Acts as a workspace for immediate reasoning, attention, and decision-making  
> - Often serves as a buffer before information is either discarded or encoded into long-term memory  

2. **Long-Term Memory**

> - Involves structural and functional changes at synapses (synaptic plasticity)  
> - Stabilized neural pathways formed through repeated activation  
> - Persistent connectivity patterns that encode stored information  
> - Can retain information over long periods ranging from days to decades  
> - Includes both explicit (conscious recall) and implicit (unconscious influence) forms  
> - Requires consolidation processes to become durable and resistant to decay  

3. **Procedural Memory**

> - Encodes learned skills, habits, and automated behaviors (e.g., walking, typing, playing an instrument)  
> - Relies heavily on motor systems and subcortical structures such as the basal ganglia and cerebellum  
> - Developed through repetition and practice rather than verbal instruction  
> - Operates largely without conscious awareness once fully learned  
> - Becomes more efficient over time as actions are optimized and refined  
> - Often remains intact even when other memory systems are impaired  

<br>

### Associative Networks

Memory systems are highly associative, meaning that concepts and experiences become linked when they occur together repeatedly. Over time, patterns of neural activity that are frequently activated together develop stronger connections. As a result, activating one idea can increase the likelihood of activating related ideas, memories, or emotions.

This creates an interconnected network structure in which information is organized through associations rather than isolated storage. From a computational perspective, memory can therefore be viewed as a large associative graph where neural pathways encode relationships between experiences.

<br>

### Retrieval

Memory retrieval is not a perfect replay of stored information. Instead, the brain reconstructs a memory by reactivating portions of the original neural activity pattern associated with the experience. In many cases, only part of the original information is needed to trigger a larger reconstruction process. For example, a particular smell may trigger a childhood memory, a familiar sound may reactivate emotional associations, or an image may bring back contextual details connected to a past event. This phenomenon is known as **pattern completion**, where partial neural input leads to the reconstruction of a larger memory network.

Because memories are reconstructed rather than replayed exactly, recall is not always perfectly accurate. During retrieval, details may be altered, omitted, or influenced by related associations and later experiences. Emotional state, suggestion, and repeated reinterpretation can also modify how a memory is reconstructed over time.

As a result, memory retrieval is considered an active generative process rather than a precise recording system. The brain prioritizes reconstruction of meaningful patterns and relationships, even if some details become distorted in the process.

<br>

### Memory Consolidation

New memories are often initially fragile and unstable. Through a process known as **memory consolidation**, repeated neural activity gradually strengthens the connections associated with an experience. Repetition, rehearsal, and sleep all contribute to reinforcing these neural pathways over time.

As consolidation progresses, temporary patterns of activity become more stable and durable long-term representations. This process allows information to transition from short-term encoding into more persistent memory structures that can later be reconstructed and retrieved.


--- PAGE ---

## Neural Oscillations and Brain Waves

Brain activity is not completely random or continuous. Large populations of neurons often synchronize their electrical activity, producing rhythmic patterns known as **neural oscillations** or **brain waves**. These oscillations occur at different frequencies and are associated with different cognitive and physiological states such as attention, relaxation, sleep, memory processing, and alertness. From a mathematical perspective, brain waves introduce concepts from periodic functions, signal processing, frequency analysis, and wave behavior into neuroscience.

<br>

### What Neural Oscillations Are

Neural oscillations are rhythmic patterns of electrical activity produced by groups of neurons firing in coordinated ways. Rather than operating independently, large networks of neurons often synchronize their activity, creating repeating wave-like signals that can be measured throughout the brain. These oscillations vary in both frequency and amplitude and are typically classified into different categories such as delta, theta, alpha, beta, and gamma waves.

Different oscillation frequencies are associated with different brain states and cognitive functions. For example, slower oscillations are commonly linked to deep sleep and recovery processes, while faster oscillations are associated with attention, sensory processing, and active thinking. Because these signals behave as repeating waveforms over time, neural oscillations are frequently studied using mathematical tools from trigonometry, signal processing, Fourier analysis, and differential equations.

Neural oscillations are commonly measured using technologies such as electroencephalography (EEG), which records voltage fluctuations produced by neural activity. By analyzing the frequency structure of these signals, researchers can study patterns related to sleep, learning, memory, neurological disorders, and overall brain function.

<br>

###  Frequency and Brain States

Different oscillation frequencies are associated with different functional states.

Common frequency bands include:

- Delta waves - deep sleep
- Theta waves - memory and drowsiness
- Alpha waves - relaxed wakefulness
- Beta waves - active thinking and focus
- Gamma waves - high-level processing and integration

Frequency is measured in hertz (Hz), meaning cycles per second.

<br>

###  Oscillations as Periodic Functions

Neural oscillations can be modeled mathematically as periodic signals:

$$
V(t) = A \sin(2\pi f t + \phi)
$$

Where:
- $V(t)$ is signal voltage over time
- $A$ is amplitude
- $f$ is frequency
- $\phi$ is phase shift

This resembles wave equations used throughout physics and signal analysis.

<br>

### Amplitude, Frequency, and Phase

Brain wave analysis focuses on several key signal properties:

1. **Frequency** - How rapidly the oscillation repeats
2. **Amplitude** - The strength or magnitude of the signal
3. **Phase** - The relative timing alignment between oscillations

Interactions between these properties influence neural coordination and information flow.

<br>

### Synchronization and Coordination

Neural synchronization occurs when groups of neurons begin firing in coordinated rhythmic patterns. Rather than acting as isolated units, different regions of the brain often synchronize their oscillatory activity to exchange information more efficiently. This coordination allows large neural networks to integrate sensory input, process information, and produce organized behavioral responses.

Synchronization is especially important in processes involving attention, movement, perception, and memory formation. For example, when performing a complex task, multiple brain regions may temporarily synchronize their activity to coordinate communication and share information rapidly. Mathematically, synchronization introduces concepts related to coupled oscillators, phase relationships, and dynamical systems, where interacting systems gradually align their behavior over time.

Disruptions in neural synchronization have been associated with neurological and psychiatric disorders such as epilepsy, Parkinson’s disease, and schizophrenia, making synchronization an important topic in both neuroscience research and clinical medicine.

<br>

###  EEG and Signal Measurement

Brain waves can be measured using **electroencephalography (EEG)**, which detects voltage fluctuations at the scalp.

EEG records:
- Aggregate neural activity
- Rhythmic voltage changes over time
- Frequency distributions across brain states

Because EEG measures collective activity, it captures large-scale network synchronization rather than individual neurons.

<br>

###  Frequency Analysis and Fourier Methods

Complex brain signals contain many overlapping frequencies simultaneously. To analyze these signals, neuroscientists use frequency decomposition techniques such as Fourier analysis. A continuous signal can be represented using the Fourier transform:

$$
F(\omega)=\int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt
$$

Where:
- $f(t)$ is the original time-domain signal
- $F(\omega)$ is the frequency-domain representation
- $\omega$ is angular frequency
- $e^{-i\omega t}$ represents oscillatory basis functions

This allows neural activity to be separated into its underlying frequency components.

Fourier-based methods are widely used in:
- EEG analysis
- Brain-computer interfaces
- Signal filtering
- Neural oscillation research
- Frequency band isolation

<br>

###  Oscillations and Information Processing

Neural oscillations play an important role in how the brain processes, organizes, and transmits information. Different oscillation frequencies are associated with different types of cognitive activity, allowing the brain to regulate communication across neural networks on multiple timescales.

One important idea is that oscillations help control the timing of neural firing. Because neurons are more likely to activate during certain phases of an oscillatory cycle, rhythmic activity can influence when information is transmitted or suppressed. This creates structured timing patterns that improve coordination between different brain regions.

Researchers believe oscillations contribute to:
- Attention and focus  
- Memory encoding and retrieval  
- Sensory perception  
- Motor coordination  
- Sleep and consciousness  

From a mathematical perspective, these processes involve concepts from wave behavior, signal timing, frequency analysis, and information theory. Oscillatory activity can therefore be studied as both a biological and computational system.

<br>

###  Resonance and Dynamic Stability

Resonance occurs when a system responds strongly to inputs that match its natural frequency of oscillation. In neuroscience, resonance helps explain why certain neural circuits respond more efficiently to signals occurring at particular frequencies. Because neurons and neural networks possess intrinsic electrical properties, some patterns of stimulation can amplify oscillatory activity while others may be suppressed.

Dynamic stability refers to the ability of neural systems to maintain organized activity while continuously adapting to changing inputs. The brain must remain flexible enough to process new information while also preventing unstable or chaotic activity from spreading uncontrollably.

These ideas are closely related to concepts from differential equations, feedback systems, and dynamical systems theory. Small changes in oscillatory behavior can sometimes produce large changes in neural activity, making stability and resonance central topics in the mathematical study of brain function. Researchers use these principles to better understand processes such as attention regulation, sensory processing, seizure activity, and neural network behavior.


--- PAGE ---

## Common Computational Tools

Computational neuroscience uses computer-based models to understand how neural systems function. Instead of only observing brain activity, researchers build simulations that reproduce simplified versions of neurons and neural networks.

These tools help explain:
- How single neurons process signals  
- How networks of neurons produce activity patterns  
- How brain-wide behavior emerges from local interactions  

<br>

### NEURON Simulation Tools

NEURON is used to simulate biologically detailed neurons.

It is commonly used for:
- Modeling electrical activity in neurons  
- Simulating synaptic communication  
- Studying how signals travel through dendrites  

This tool is used when researchers want detailed, cell-level models of brain activity.

<br>

### NEST Network Simulation Tools

NEST is used to simulate large networks of simplified neurons.

It focuses on:
- Large-scale brain activity simulations  
- Interaction between many neurons  
- Emergent network behavior  

It is useful for studying how large groups of neurons produce coordinated activity.

<br>

### Nengo Functional Modeling Tools

Nengo is used to build simplified models of brain function.

It is commonly used for:
- Modeling memory and decision-making  
- Simulating how groups of neurons represent information  
- Building biologically inspired computational systems  

It focuses on how neural systems perform computation at a functional level.

<br>

### Brain Dynamics Simulation Tools

The Brain Dynamics Toolbox is used to simulate how neural systems change over time.

It is used for:
- Modeling brain rhythms and oscillations  
- Studying stability of neural activity  
- Exploring how neural systems evolve dynamically  

It helps researchers understand how brain activity changes over time.

<br>

### Neural Network Simulation Tools

Neural network tools model simplified learning systems inspired by the brain.

They are used for:
- Pattern recognition  
- Learning from data  
- Modeling decision-making systems  

These tools help connect neuroscience concepts with artificial intelligence systems.

<br>

### Dynamical Systems Tools

Dynamical systems tools model how neural activity changes over time based on simple rules.

They are used to study:
- Stable and unstable activity patterns  
- Oscillations and rhythmic behavior  
- How small changes affect system behavior  

They provide a basic framework for understanding complex brain dynamics.

<br>

### Large-Scale Brain Modeling Tools

Large-scale brain modeling tools simulate interactions between brain regions.

They are used for:
- Whole-brain activity simulation  
- Modeling connections between brain areas  
- Studying global brain organization  

These tools focus on how different brain regions work together as a system.

<br>

## Electrophysiology & Neural Signal Processing

Electrophysiology measures electrical activity from the brain directly. Unlike imaging methods, it records signals with very high timing precision. Signal processing tools are used to clean and analyze these recordings.

<br>

### EEG and MEG Analysis Tools

EEG and MEG are used to record brain activity in real time.

These tools are used for:
- Recording brain signals  
- Removing noise and artifacts  
- Detecting responses to stimuli  
- Identifying brain activity patterns  

They convert raw recordings into usable brain signals for analysis.

<br>

### Neural Signal Filtering Tools

Filtering tools clean neural recordings.

They are used to:
- Remove noise  
- Isolate meaningful brain signals  
- Improve signal clarity  

This step is essential before analyzing brain activity.

<br>

### Frequency Analysis Tools

Frequency tools analyze brain activity based on rhythms.

They are used to:
- Identify brainwave patterns  
- Measure signal strength in different frequency ranges  
- Study rhythmic brain activity  

They help describe brain activity in terms of repeating patterns.

<br>

### Quantitative EEG Tools

Quantitative EEG tools extract measurable features from brain signals.

They are used to:
- Convert EEG data into numerical features  
- Compare brain activity across individuals or groups  
- Support clinical and research analysis  

They turn raw brain signals into structured data.

<br>

### Neural Signal Software Toolkits

Specialized software packages are used to analyze EEG and MEG data.

Common functions include:
- Cleaning and filtering signals  
- Breaking signals into frequency components  
- Identifying brain activity patterns  
- Running basic statistical analysis  

These toolkits provide complete workflows from raw data to results.

<br>

## Programming, Statistics, & Data Science

Neuroscience relies on programming and statistics to analyze data and build models.

These tools help:
- Organize experimental data  
- Perform statistical analysis  
- Build predictive models  
- Visualize results  

<br>

### Python for Scientific Computing

Python is used for:
- Data analysis  
- Machine learning  
- Scientific computing workflows  
- Data visualization  

It is the main tool for combining different analysis steps into one workflow.

<br>

### MATLAB for Numerical Computing

MATLAB is used for:
- Mathematical modeling  
- Signal and image processing  
- Simulation of systems  

It is commonly used for numerical and engineering-based neuroscience work.

<br>

### R for Statistical Analysis

R is used for:
- Statistical testing  
- Data analysis  
- Research reporting  

It is mainly focused on statistical reasoning and interpretation.

<br>

### NumPy for Numerical Computation

NumPy is used for fast numerical operations.

It supports:
- Arrays and matrices  
- Basic mathematical operations  
- Efficient data computation  

It is a foundation for most scientific Python tools.

<br>

### SciPy for Scientific Methods

SciPy extends numerical tools for scientific applications.

It is used for:
- Optimization  
- Signal processing  
- Mathematical modeling  

It supports more advanced scientific calculations.

<br>

### Scikit-learn for Machine Learning

Scikit-learn is used for basic machine learning.

It is used for:
- Classification  
- Prediction  
- Pattern recognition  
- Model evaluation  

It helps build simple predictive models from data.

<br>

### Core Data Analysis Concepts

Across all tools, common goals include:
- Finding patterns in data  
- Making predictions  
- Testing hypotheses  
- Quantifying uncertainty  

These ideas form the foundation of modern data-driven neuroscience.

<br>

## Computational Neuroscience & Simulation

Computational neuroscience uses simplified models to understand how neurons and brain systems behave.

These models help explain:
- How neurons process signals  
- How networks generate activity  
- How complex behavior emerges  

<br>

### NEURON Modeling Tools

NEURON simulates realistic neuron behavior.

It is used for:
- Electrical activity in neurons  
- Signal transmission  
- Synaptic communication  

It focuses on detailed biological modeling of single neurons.

<br>

### NEST Simulation Tools

NEST simulates large networks of neurons.

It is used for:
- Large-scale brain activity  
- Network interactions  
- Emergent neural behavior  

It focuses on systems with many interacting neurons.

<br>

### Nengo Modeling Tools

Nengo models brain function at a simplified level.

It is used for:
- Memory systems  
- Decision-making models  
- Information processing in neural populations  

It focuses on how neural systems represent and compute information.

<br>

### Brain Dynamics Tools

Brain dynamics tools model how brain activity changes over time.

They are used for:
- Brain rhythms  
- Stability of neural systems  
- Time-based activity patterns  

They help study how brain activity evolves.

<br>

### Neural Network Tools

Neural networks model learning and pattern recognition.

They are used for:
- Learning from data  
- Classification tasks  
- Pattern detection  

They connect neuroscience ideas with artificial intelligence.

<br>

### Dynamical Systems Tools

These tools model how systems change over time.

They are used for:
- Stability analysis  
- Oscillatory behavior  
- System evolution  

They show how simple rules can produce complex behavior.

<br>

### Large-Scale Brain Models

These models simulate interactions between brain regions.

They are used for:
- Whole-brain activity  
- Brain connectivity  
- Global neural dynamics  

They focus on how brain regions work together as a system.

<br>

## Electrophysiology & Neural Signal Processing (Core Models)

Electrophysiology measures electrical brain activity directly.

Signal processing tools help interpret this data.

<br>

### EEG and MEG Tools

These tools are used for:
- Recording brain activity  
- Cleaning noisy signals  
- Detecting brain responses  
- Identifying activity patterns  

They provide real-time brain signal measurements.

<br>

### Filtering Tools

Filtering tools are used to:
- Remove noise  
- Improve signal clarity  
- Isolate brain activity  

They are a required preprocessing step.

<br>

### Frequency Analysis Tools

These tools are used to:
- Identify brain rhythms  
- Analyze signal patterns  
- Study oscillatory activity  

They describe brain activity in terms of repeating cycles.

<br>

### Quantitative EEG Tools

These tools convert EEG signals into numerical data.

They are used for:
- Feature extraction  
- Clinical analysis  
- Brain state classification  

They turn raw signals into measurable variables.

<br>

### Software Toolkits

EEG/MEG toolkits are used for full analysis pipelines.

They support:
- Data cleaning  
- Signal decomposition  
- Basic statistical analysis  

They provide complete workflows for brain signal analysis.