<!--
title: "Math in Music"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

<img
src="markdown/pathway_images/music_photo_1.jpeg"
alt="Placeholder Text"
class="pathway-image"
/>

<div class="pathway-title-overlay">
<h1 class="pathway-title">
Music
</h1>
</div>

</div>

<br>
<br>

### What can I do?
- Producing and editing audio using digital audio workstations (DAWs) such as Ableton Live, Logic Pro, or Pro Tools  
- Applying digital signal processing techniques for mixing, mastering, and sound design  
- Using MIDI programming and virtual instruments to compose and arrange music  
- Analyzing audio waveforms, frequency spectra, and harmonics using audio analysis tools  
- Recording and processing live instruments and vocals in studio environments  
- Using sampling, synthesis, and effects processing to create sound textures  
- Collaborating with engineers and producers to refine audio quality and production output  

garage band and cakewalk should be included

<br>
<br>

### What math concepts do I need to know?
- Fractions and Ratios
- Rhythm and Time Signatures
- Patterns and Sequences
- Wave Functions
- Frequency and Pitch Relationships
- Algebra
- Graphing and Functions
- Fourier Concepts
- Probability


--- PAGE ---

## Sound Waves & Acoustics

Sound is a mechanical wave produced by vibrating objects and transmitted through a medium such as air, water, or solid materials. In music, sound waves form the physical basis of pitch, loudness, timbre, harmony, and resonance. Acoustics is the scientific study of sound behavior, including how sound waves are generated, transmitted, reflected, and perceived. Musical acoustics combines physics, mathematics, engineering, and auditory perception to explain how musical sounds are created and experienced. Understanding sound wave behavior is essential for instrument design, recording technology, architectural acoustics, and music theory.


<br>

### Frequency

Frequency describes the number of wave cycles that occur per second and is measured in hertz (Hz). Frequency determines the perceived pitch of a sound. Higher frequencies produce higher pitches, while lower frequencies produce lower pitches. The relationship between frequency and wave period is:

$$
f = \frac{1}{T}
$$

Where:
- $f$ = frequency
- $T$ = wave period

<br>

The speed of a wave is related to frequency and wavelength by:

$$
v = f\lambda
$$

Where:
- $v$ = wave velocity
- $f$ = frequency
- $\lambda$ = wavelength

In music:
- A4 is commonly tuned to 440 Hz
- Doubling frequency raises pitch by one octave
- Halving frequency lowers pitch by one octave

Frequency relationships form the mathematical foundation of musical tuning systems and harmonic intervals.


<br>

### Amplitude

Amplitude describes the maximum displacement of a sound wave from its equilibrium position. In acoustics, amplitude is closely related to perceived loudness.

Greater amplitude corresponds to:
- Increased sound intensity
- Greater energy transfer
- Louder perceived sound

A simple sinusoidal sound wave may be written as:

$$
y(t) = A\sin(2\pi ft)
$$

Where:
- $A$ = amplitude
- $f$ = frequency
- $t$ = time

Although loudness perception is influenced by human hearing sensitivity and frequency, amplitude remains one of the primary physical determinants of sound intensity.


<br>

### Harmonics

Most musical sounds are not composed of a single pure frequency. Instead, they contain multiple frequencies called harmonics or overtones. The lowest frequency is called the **fundamental frequency**, while higher integer multiples are called harmonics. The harmonic series is:

$$
f_n = nf_1
$$

Where:
- $f_n$ = $n$-th harmonic frequency
- $f_1$ = fundamental frequency
- $n$ = harmonic number

For example, if the fundamental frequency is 100 Hz:
- 2nd harmonic = 200 Hz
- 3rd harmonic = 300 Hz
- 4th harmonic = 400 Hz

Harmonics strongly influence timbre, allowing listeners to distinguish different instruments even when they play the same pitch. String instruments, brass instruments, woodwinds, and vocal systems each produce characteristic harmonic structures.


<br>

### Resonance

Resonance occurs when a system vibrates most efficiently at specific natural frequencies. When an external vibration matches one of these frequencies, oscillation amplitude increases dramatically.

Resonance is fundamental in:
- Instrument amplification
- Vocal acoustics
- Architectural acoustics
- String vibration
- Air column resonance

The resonant frequency of a stretched string is approximated by:

$$
f = \frac{1}{2L}\sqrt{\frac{T}{\mu}}
$$

Where:
- $L$ = string length
- $T$ = tension
- $\mu$ = linear mass density

Instrument bodies act as resonators that amplify and shape sound through selective reinforcement of frequencies.

Examples include:
- Guitar soundboards
- Violin bodies
- Piano soundboards
- Brass air columns

Resonance also explains phenomena such as sympathetic vibration, where nearby objects vibrate in response to matching frequencies.


<br>

### Wave interference

When multiple sound waves overlap, they combine through interference. **Constructive interference** occurs when waves reinforce one another, increasing amplitude. **Destructive interference** occurs when waves partially or completely cancel each other. Interference patterns are determined by phase relationships between waves. The superposition principle states:

$$
y_{total} = y_1 + y_2
$$

Interference produces many important acoustic phenomena including:
- Beats
- Standing waves
- Room acoustics
- Noise cancellation
- Phase effects in recording

Beat frequency is given by:

$$
f_{beat} = |f_1 - f_2|
$$

Where:
- $f_1$ and $f_2$ are nearby frequencies

Musicians often use beats to tune instruments by minimizing interference fluctuations.


<br>

### Fourier analysis

Fourier analysis is a mathematical method used to decompose complex waveforms into combinations of sinusoidal components. According to Fourier theory, any periodic sound can be represented as a sum of sine and cosine waves. The Fourier series is:

$$
f(t) =
a_0 +
\sum_{n=1}^{\infty}
\left(
a_n \cos(n\omega t)
+
b_n \sin(n\omega t)
\right)
$$

Where:
- $a_n$ and $b_n$ are Fourier coefficients
- $\omega$ = angular frequency
- $n$ = harmonic index

Fourier analysis is essential in:
- Audio engineering
- Signal processing
- Music synthesis
- Spectral analysis
- Digital recording

Spectrograms generated through Fourier transforms allow visualization of frequency content over time. Modern music technology heavily depends on Fourier-based signal analysis.


<br>

### Chladni figures

Chladni figures are geometric vibration patterns formed when a surface vibrates at specific resonant frequencies. When fine particles such as sand are placed on a vibrating metal plate, the vibrations cause the particles to move away from regions with strong motion and settle along regions with little or no motion. These stationary regions are called *nodal lines*, and the resulting arrangements form intricate standing wave patterns across the surface.

These patterns provide a visual demonstration of resonance, standing waves, symmetry, and vibrational modes in physical systems. Different frequencies produce different geometric arrangements, revealing how the shape of the surface and the frequency of vibration influence wave behavior. Chladni figures were among the earliest experimental demonstrations of wave mechanics and remain important in the study of acoustics, resonance, and elasticity theory. The mathematical behavior of vibrating plates is described using partial differential equations that model wave propagation and mechanical deformation.

Chladni figures remain important in:
- Instrument design
- Acoustical engineering
- Material science
- Physics education
- Modal analysis

They also illustrate the deep relationship between mathematics, geometry, sound, and visual pattern formation.


--- PAGE ---

## Digital Audio Production

Digital audio production is the process of recording, editing, arranging, manipulating, and mixing sound using computer-based technology. Modern music production relies heavily on software environments known as Digital Audio Workstations (DAWs), which integrate recording tools, virtual instruments, signal processing, sequencing systems, and mixing capabilities into a unified platform. Digital production has transformed music creation by allowing composers, producers, and engineers to manipulate sound with extraordinary precision and flexibility. Contemporary production environments support:

- Multi-track recording
- Virtual synthesis
- MIDI sequencing
- Audio editing
- Sampling
- Real-time effects processing
- Automation systems

Digital audio production is now central to nearly every modern genre of music, film scoring, broadcasting, game audio, and multimedia design.


<br>

### Ableton Live

Ableton Live is a Digital Audio Workstation designed for both studio production and live performance. It is particularly well known for its flexible workflow, real-time looping capabilities, and performance-oriented interface.

Ableton Live is divided into two primary workspaces:

<br>

1. **Session View** allows non-linear arrangement through clip launching and loop triggering. This environment is especially useful for:
> - Live electronic performance
> - Improvisation
> - Loop-based composition
> - Experimental arrangement
2. **Arrangement View** provides a traditional timeline-based editing environment used for:
> - Song structuring
> - Automation
> - Linear composition
> - Detailed mixing

<br>

Ableton Live is widely used in:
- Electronic music production
- Live DJ performance
- Experimental sound design
- Film scoring
- Hybrid performance systems

Its integrated workflow encourages rapid iteration and real-time creative experimentation.

<br>

### FL Studio

FL Studio is a Digital Audio Workstation known for its pattern-based sequencing workflow and accessibility for electronic music production.

Originally focused on loop sequencing, FL Studio has evolved into a comprehensive production environment supporting audio recording, MIDI composition, automation, mixing, plugin hosting, and sound synthesis. A central feature of FL Studio is the **step sequencer**, which allows rhythmic and melodic patterns to be programmed efficiently.

FL Studio is especially popular in areas such as:
- Hip-hop production  
- EDM  
- Trap music  
- Beat making  
- Experimental electronic composition  

Its workflow emphasizes rapid pattern creation and intuitive arrangement building.


<br>

### Logic Pro

Logic Pro is Apple’s professional Digital Audio Workstation designed for advanced music production, recording, composition, and mixing.

Logic Pro integrates multi-track recording, MIDI sequencing, virtual instruments, spatial audio tools, advanced automation systems, and large integrated sound libraries into a single production environment.

The software is widely used in:
- Professional studio production  
- Film and television scoring  
- Orchestral mockups  
- Songwriting  
- Post-production  

Logic Pro also includes advanced production features such as Flex Time, pitch correction, smart tempo analysis, surround sound mixing, and integrated notation editing. Its ecosystem is strongly optimized for macOS-based production environments.


<br>

### Digital Audio Workstations (DAWs)

A Digital Audio Workstation (DAW) is a software platform used for producing and editing digital audio.

Core DAW functions include recording, sequencing, editing, mixing, mastering, plugin processing, and automation. Most DAWs operate using a multi-track timeline in which audio and MIDI information are organized into independent channels.

Typical DAW components include:
- Mixer consoles  
- Piano roll editors  
- Audio waveform editors  
- Plugin chains  
- Routing systems  
- Transport controls  

DAWs support both destructive and non-destructive editing workflows, allowing producers to manipulate sound while preserving original recordings. Modern DAWs form the technological foundation of nearly all contemporary music production environments.


<br>

### MIDI Systems

MIDI (Musical Instrument Digital Interface) is a digital communication protocol that allows electronic musical devices and software systems to exchange performance information.

Unlike audio signals, MIDI does not transmit sound directly. Instead, it transmits performance data such as note pitch, velocity, timing, modulation, sustain control, and instrument selection. A MIDI note message typically includes a note number, velocity value, start time, and duration.

Because MIDI stores symbolic performance data rather than recorded sound, it allows for:
- Flexible editing  
- Instrument replacement  
- Quantization  
- Real-time orchestration  
- Efficient file storage  

MIDI systems are essential in areas such as virtual instrument control, electronic composition, film scoring, game audio, and live performance automation. The MIDI standard remains one of the most influential technologies in modern music production.


<br>

### Audio Layering

Audio layering is the process of combining multiple sounds to create richer, fuller, or more complex sonic textures.

Layering may involve stacking instruments, combining synthesizers, reinforcing drum sounds, blending vocal harmonies, or merging acoustic and electronic elements. Effective layering allows producers to shape timbre, stereo width, frequency balance, dynamic intensity, and emotional character within a mix.

For example:
- A snare drum may contain multiple layered samples  
- Vocal stacks may create harmonic density  
- Synth layers may combine warm and bright tonal characteristics  

Successful layering requires careful attention to phase relationships, frequency masking, dynamic balance, and spatial placement. Poorly managed layering can produce muddiness or destructive interference, while well-balanced layering creates depth and clarity.


<br>

### Sampling

Sampling is the process of recording, extracting, or reusing segments of existing audio for creative manipulation and recomposition.

Samples may include instrument recordings, drum hits, vocal phrases, environmental sounds, field recordings, or historical recordings. Once imported into a production environment, samples can be looped, time-stretched, pitch-shifted, chopped, filtered, or rearranged into entirely new musical structures.

Sampling forms the basis of many modern genres including:
- Hip-hop  
- EDM  
- House music  
- Experimental music  
- Lo-fi production  

Digital samplers allow producers to map audio recordings across MIDI keyboards and manipulate them as playable instruments. Modern sampling systems often include granular synthesis, spectral manipulation, real-time slicing, and AI-assisted audio processing.

Sampling has become both a technical process and an artistic practice that reshapes existing sounds into entirely new musical contexts.


--- PAGE ---

## Music Theory & Pattern Systems

Music theory is the study of how musical sounds are organized into structured systems of pitch, rhythm, and harmony. Although music is often perceived as expressive or emotional, its underlying structure is highly mathematical, relying on ratios, patterns, symmetry, and hierarchical organization. Music theory and pattern systems describe how musical elements combine to produce coherence over time, allowing listeners to recognize melody, harmony, and rhythm as structured forms rather than random sound.


<br>

### Scales

A musical scale is an ordered sequence of pitches arranged by frequency. Scales provide the foundational framework for melody and harmony in Western and non-Western music systems.

In Western music, the most common scale is the major scale, defined by a specific pattern of whole and half steps:

$$
W - W - H - W - W - W - H
$$

Where:
- W = whole step
- H = half step

Scales define the tonal space within which musical ideas are constructed. Different cultures use different tuning systems, including:
- Diatonic scales
- Pentatonic scales
- Chromatic scales
- Microtonal scales

Each scale establishes a unique set of tonal relationships that influence melodic behavior.


<br>

### Chords

A chord is a collection of three or more pitches sounded simultaneously. Chords form the harmonic foundation of most musical systems.

The simplest chord structure is the triad, built from stacked intervals:

$$
\text{Root + Third + Fifth}
$$

Chords are classified based on interval structure:
- Major chords (bright, stable)
- Minor chords (dark, emotional)
- Diminished chords (tense, unstable)
- Augmented chords (suspended, ambiguous)

Chord relationships create harmonic progressions that define musical movement and emotional direction. Harmony emerges from frequency relationships and interference patterns between simultaneous tones.


<br>

### Rhythm

Rhythm refers to the organization of sound and silence over time. It is the temporal structure that gives music motion and structure. Rhythm is based on:
- Repetition
- Timing intervals
- Accents
- Grouping patterns

At its simplest level, rhythm can be understood as time intervals between events:

$$
\Delta t = t_{n+1} - t_n
$$

Rhythmic organization creates patterns that the human brain perceives as structured time, allowing for coordination, dance, and synchronization.


<br>

### Time signatures

Time signatures describe how beats are grouped within a measure of music. They define the metric structure of rhythm.

A time signature is written as:

$$
\frac{\text{beats per measure}}{\text{note value per beat}}
$$

Common examples include:
- 4/4 (common time)
- 3/4 (waltz time)
- 6/8 (compound meter)
- 7/8 (irregular meter)

Time signatures determine how rhythm is subdivided and organized, influencing the perceived flow and emphasis of musical phrases.


<br>

### Interval relationships

An interval is the distance between two pitches, measured in frequency ratio or semitones. In frequency terms, intervals follow exponential relationships:

$$
f_2 = f_1 \cdot r
$$

Where:
- $f_1$, $f_2$ = frequencies
- $r$ = interval ratio

Common simple ratios include:
- Octave: 2:1
- Perfect fifth: 3:2
- Perfect fourth: 4:3

Intervals are the building blocks of melody and harmony, defining how pitches relate to one another.


<br>

### Mathematical ratios in music

Music is fundamentally structured around numerical relationships between frequencies. Many harmonic systems are based on simple integer ratios, which are perceived as consonant by the human ear. The harmonic series is defined as:

$$
f_n = n f_1
$$

Where:
- $f_n$ = harmonic frequency
- $f_1$ = fundamental frequency

These ratios explain why certain combinations of notes sound stable or pleasing. Consonance arises from low-complexity frequency relationships, while dissonance arises from more complex ratios. Tuning systems such as just intonation and equal temperament are different ways of approximating these mathematical relationships.

<br>

### Polyrhythms

A polyrhythm occurs when two or more independent rhythmic patterns are played simultaneously, often with different time subdivisions. A common example is a 3:2 polyrhythm, where one rhythm divides time into three equal parts while another divides it into two. This can be expressed as a fraction such as $\frac{3}{2}$. Polyrhythms create complex temporal textures by layering competing periodic structures.

They are widely used in:
- African drumming traditions
- Contemporary classical music
- Jazz improvisation
- Progressive and experimental music

Polyrhythms demonstrate that rhythm can be understood as interacting periodic systems, where multiple time cycles coexist within a single musical framework.


--- PAGE ---

## Audio Engineering & Signal Processing

Audio engineering and signal processing involve the manipulation of sound signals to improve, alter, or creatively shape their sonic characteristics. This field combines physics, mathematics, and digital computation to control how audio behaves in both time and frequency domains. Modern audio engineering is fundamental to music production, broadcasting, film sound design, and digital communication systems. It relies on understanding how sound waves can be represented, transformed, and reconstructed using mathematical operations.

<br>

### Waveforms

A waveform represents how a sound signal varies over time. It is typically visualized as amplitude versus time and serves as the most basic representation of audio.

Common waveform types include:
- Sine waves (pure tone)
- Square waves (rich in harmonics)
- Sawtooth waves (bright, full-spectrum sound)
- Triangle waves (smooth harmonic structure)

A simple sinusoidal waveform is described by:

$$
y(t) = A\sin(2\pi ft + \phi)
$$

Where:
- $A$ = amplitude
- $f$ = frequency
- $t$ = time
- $\phi$ = phase

Waveforms form the foundation for synthesis, analysis, and digital representation of sound.


<br>

### Compression

Audio compression reduces the dynamic range of a signal, making quiet sounds louder and loud sounds quieter. This creates a more balanced and controlled overall sound. A basic conceptual model of compression is:

$$
y =
\begin{cases}
x & x \leq T \\
T + \frac{x - T}{R} & x > T
\end{cases}
$$

Where:
- $x$ = input signal level
- $y$ = output signal level
- $T$ = threshold
- $R$ = compression ratio

Compression is widely used in:
- Music mixing
- Broadcasting
- Podcast production
- Mastering

It helps maintain consistent loudness and prevents signal distortion.


<br>

### Equalization

Equalization (EQ) is the process of adjusting the balance between frequency components in an audio signal. Audio signals can be decomposed into frequency bands, and EQ allows selective boosting or attenuation of these bands. A conceptual EQ operation can be expressed as:

$$
Y(f) = H(f)\cdot X(f)
$$

Where:
- $X(f)$ = input signal in frequency domain
- $H(f)$ = filter response
- $Y(f)$ = output signal

EQ is used to:
- Remove unwanted frequencies
- Enhance clarity
- Shape tonal character
- Prevent masking between instruments

Different EQ types include:
- Parametric EQ
- Graphic EQ
- Shelving filters
- High-pass and low-pass filters


<br>

### Reverb

Reverb (reverberation) is the persistence of sound after it is produced, caused by reflections from surfaces in an environment. It can be modeled as the accumulation of delayed and attenuated copies of a signal:

$$
y(t) = x(t) + \sum_{n=1}^{\infty} a_n x(t - \tau_n)
$$

Where:
- $x(t)$ = original signal
- $a_n$ = attenuation factor
- $\tau_n$ = delay time

Reverb is essential for:
- Creating spatial depth
- Simulating acoustic environments
- Enhancing musical realism

Types of reverb include:
- Room reverb
- Hall reverb
- Plate reverb
- Spring reverb

<br>

### Filters

Filters selectively modify frequency content within an audio signal.

Common filter types include:
- Low-pass filters (remove high frequencies)
- High-pass filters (remove low frequencies)
- Band-pass filters (allow a range of frequencies)
- Notch filters (remove narrow frequency bands)

<br>

### Signal chains

A signal chain is the ordered sequence of audio processing steps applied to a sound. A typical signal chain may include:

1. Gain adjustment
2. Equalization
3. Compression
4. Filtering
5. Reverb or delay
6. Limiting

Each processing stage modifies the signal before passing it to the next stage. Signal chain design is crucial for achieving clarity, balance, and creative sound shaping.


<br>

### Noise reduction

Noise reduction removes unwanted background signals from an audio recording. A basic model separates signal and noise:

$$
x(t) = s(t) + n(t)
$$

Where:
- $x(t)$ = observed signal
- $s(t)$ = desired signal
- $n(t)$ = noise

Noise reduction techniques include:
- Spectral subtraction
- Adaptive filtering
- Gate-based suppression
- Machine learning-based separation

Effective noise reduction improves clarity without significantly distorting the original signal, making it essential in professional audio production.


--- PAGE ---

## Visualization & Experimental Music

Visualization and experimental music explore the relationship between sound, mathematics, and visual patterns. In these systems, sound is not only an auditory phenomenon but also a structured physical and computational process that can produce observable geometric, spectral, and algorithmic patterns. This field bridges acoustics, physics, computer science, and artistic practice, allowing sound to be studied and created through both visual and mathematical representations. Experimental music further expands traditional composition by incorporating randomness, algorithms, and non-traditional sound structures.

<br>

### Cymatics

Cymatics is the study of visible sound vibration patterns produced on physical surfaces. When sound waves interact with materials such as sand, water, or powder, they generate structured geometric patterns corresponding to the frequency and amplitude of the vibration. Different frequencies produce distinct spatial arrangements:
- Low frequencies produce large, simple structures
- High frequencies produce complex, intricate patterns

Cymatic systems demonstrate that sound is not purely abstract but has tangible physical manifestations in matter. These patterns are governed by wave interference and resonance phenomena, linking acoustics directly to spatial geometry.


<br>

### Chladni plates

Chladni plates are thin metal surfaces that visualize vibrational modes when driven at specific frequencies. When a plate vibrates, regions of maximum displacement cause particles (such as sand) to move away, while nodal lines remain stable and accumulate material. The resulting patterns represent standing wave structures. Chladni plate behavior is governed by solutions to the wave equation in two-dimensional systems:

$$
\nabla^2 u + k^2 u = 0
$$

Where:
- $u$ = displacement field
- $k$ = wave number

Chladni figures demonstrate how physical systems naturally organize into mathematically constrained patterns.


<br>

### Spectrograms

A spectrogram is a visual representation of sound showing how frequency content changes over time. It maps three dimensions:
- Time (horizontal axis)
- Frequency (vertical axis)
- Amplitude (color intensity)

Spectrograms are generated using Fourier analysis, which decomposes a signal into its frequency components. Mathematically, this is based on the Fourier transform:

$$
X(f,t) = \int_{-\infty}^{\infty} x(\tau)\, e^{-2\pi i f \tau} d\tau
$$

Spectrograms are widely used in:
- Music analysis
- Speech recognition
- Bioacoustics
- Sound design
- Audio forensics

They allow complex sounds to be studied as evolving frequency structures.


<br>

### Audio visualization

Audio visualization refers to the real-time or post-processed graphical representation of sound signals. Unlike spectrograms, audio visualization may include abstract or artistic interpretations of sound data.

Common visualization methods include:
- Waveform displays
- Frequency bars
- Oscilloscopes
- Particle-based systems
- Reactive geometric shapes

Audio visualization often maps sound properties such as:
- Amplitude → brightness or size
- Frequency → spatial position or color
- Rhythm → motion or repetition

These systems are widely used in:
- Music software interfaces
- Live performance visuals
- Interactive installations
- Digital art

Audio visualization makes sound perceptually accessible through visual encoding of acoustic information.


<br>

### Generative music

Generative music is music created using systems that produce sound through algorithmic processes rather than direct human composition. These systems may incorporate randomness, rules, or evolving structures.

Generative systems can be:
- Deterministic (rule-based)
- Stochastic (randomized)
- Hybrid (rule + randomness)

A simple generative model can be expressed as:

$$
x_{n+1} = f(x_n)
$$

Where:
- $x_n$ = musical state at step $n$
- $f$ = transformation function

Generative music systems are used in:
- Ambient music composition
- Video game soundtracks
- Procedural audio environments
- Interactive installations

These systems emphasize emergence, where complex musical structures arise from simple rules.


<br>

### Algorithmic composition

Algorithmic composition refers to the use of formal procedures, mathematical rules, or computational systems to generate musical material. Unlike generative music, which may emphasize evolving systems, algorithmic composition often focuses on structured processes for creating musical form.

Techniques include:
- Markov chains
- Cellular automata
- Fractal algorithms
- Set theory-based composition
- Probabilistic models

A Markov-based musical transition system can be described as:

$$
P(s_{n+1} \mid s_n)
$$

Where:
- $s_n$ = current musical state
- $P$ = transition probability

Algorithmic composition allows composers to:
- Explore large compositional spaces
- Generate non-repetitive structures
- Model musical complexity mathematically
- Create systems that evolve beyond human intuition

This approach highlights the deep connection between music, mathematics, and computation, where composition becomes the design of systems rather than individual notes.