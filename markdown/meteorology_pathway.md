<!--
title: "Math in Meteorology"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/meteorology_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Meterology
    </h1>
  </div>

</div>

<br>

It is common to think of meteorologists as weather forecasters on the news, but these are far from the only ones. There are meteorologists that work for air travel and shipping companies, for instance. Sometimes, they can also be useful in specific emergency cases; they were instrumental in the rescue of the Tham Luang cave rescue in 2018 to coordinate search and rescue efforts. Similar cases can be said regarding operations that would take several days to accomplish, such as combatting wildfires.

<br>

###  What will I be doing?
- Collecting atmospheric data using satellites, radar systems, weather stations, and radiosonde instruments  
- Processing and analyzing large-scale weather datasets using scientific computing and data analysis tools  
- Running numerical weather prediction models on high-performance computing systems to simulate atmospheric behavior and forecast conditions  
- Using Python, Fortran, and related scientific programming tools to analyze data and automate forecasting workflows  
- Applying GIS software to visualize and analyze spatial weather and climate patterns  
- Using data assimilation systems to integrate real-time observations with model outputs  
- Interpreting satellite imagery and model outputs to track storms, hurricanes, and severe weather systems  
- Evaluating and calibrating predictive models based on observed atmospheric data and historical records   

<br>

###  What are the most common jobs?
- Meteorologist  
- Weather Forecaster  
- Climate Scientist  
- Atmospheric Researcher  
- Broadcast Meteorologist  
- Air Quality Specialist  
- Hydrometeorologist  
- Data Scientist (Climate/Weather)  


<br>

###  What math concepts do I need to know?
- Differential Equations  
- Statistics  
- Probability  
- Calculus  
- Linear Algebra  
- Fluid Dynamics  
- Data Analysis  
- Numerical Methods  
- Graphing and Functions  

--- PAGE ---

## Atmospheric Structure and Layers

The Earth's atmosphere is a layered fluid system governed by gravity, thermodynamics, and radiative energy transfer. While we divide it into discrete layers for convenience, the atmosphere is mathematically continuous, with properties like pressure, density, and temperature changing smoothly with altitude.

The major atmospheric layers are:

- Troposphere (surface to ~8–15 km): weather, convection, and most atmospheric mass
- Stratosphere (~15–50 km): stable layer containing the ozone layer
- Mesosphere (~50–85 km): temperature decreases with altitude again
- Thermosphere (~85–600 km): high-energy solar radiation dominates behavior
- Exosphere (~600 km+): outermost region transitioning into space

Each layer is defined primarily by how temperature changes with altitude, not by a physical boundary.

<br>


###  The Ideal Gas Law

The most important unifying relationship is the ideal gas law, which connects all major state variables:


$$
PV = nRT
$$

Where:
- $P$ is pressure
- $V$ is volume
- $n$ is the number of moles of gas
- $R$ is the ideal gas constant
- $T$ is temperature in Kelvin

This equation shows that pressure and volume are directly tied to temperature and particle quantity.

<br>


###  Boyle's Law

When temperature is held constant, pressure and volume are inversely related:

$$
P_1V_1 = P_2V_2
$$

This means:
- Decreasing volume increases pressure
- Increasing volume decreases pressure

This occurs because particles have less space to move, increasing collision frequency with container walls.

<br>

###  Charles's Law

When pressure is constant, volume is directly proportional to temperature:

$$
\frac{V_1}{T_1} = \frac{V_2}{T_2}
$$

As temperature increases:
- Particle motion increases
- Gas expands to maintain pressure balance

This explains why gases expand when heated.


<br>

###  Gay-Lussac's Law

When volume is constant, pressure is directly proportional to temperature:

$$
\frac{P_1}{T_1} = \frac{P_2}{T_2}
$$

This occurs because faster-moving particles collide more forcefully with container walls.

<br>

###  Atmospheric Pressure

Atmospheric pressure decreases with altitude because there is less air above to exert weight. This leads to an exponential relationship derived from hydrostatic equilibrium.


$$
P(h) = P_0 e^{-h/H}
$$

Where:
- $P$ is pressure at height $h$
- $P_0$ is sea-level pressure
- $h$ is altitude
- $H$ is the scale height
- $e$ is Euler's number

This shows that pressure does not decrease linearly. Instead, it drops rapidly near the surface and more slowly at higher altitudes.


<br>

###  Hydrostatic Equilibrium and Vertical Balance

The exponential structure of the atmosphere comes from hydrostatic equilibrium, where the downward force of gravity is balanced by the upward pressure gradient force.

This creates a continuous balance:

- Gravity pulls atmospheric mass downward
- Pressure decreases upward to counterbalance weight
- Density decreases with both pressure and altitude

This is why the atmosphere naturally forms a smooth gradient rather than sharp divisions.

<br>

###  Temperature-Based Layering

Atmospheric layers are primarily defined by temperature trends:

- Troposphere: temperature decreases with altitude due to adiabatic cooling
- Stratosphere: temperature increases due to ozone absorption of ultraviolet radiation
- Mesosphere: temperature decreases again due to reduced absorption
- Thermosphere: temperature increases due to high-energy solar radiation absorption

These gradients control stability and vertical motion. For example, the stratosphere resists convection because warmer air lies above cooler air.

<br>

###  Density and Atmospheric Compression

Air density also decreases exponentially with altitude, closely tied to pressure through the ideal gas relationship.

Key consequences:

- Most atmospheric mass is concentrated near Earth's surface
- Small altitude changes significantly affect aircraft performance
- Weather systems are confined to lower altitudes where density and moisture are higher

<br>

### Temperature & Molecular Motion

Temperature is directly proportional to the average kinetic energy of gas particles:

$$
T \propto \langle KE \rangle
$$

As temperature increases:
- Particle velocity increases  
- Collision frequency increases  
- Collision force increases  

At constant volume, this leads to increased pressure:

$$
P \propto T \quad (\text{at constant } V, n)
$$

<br>

### Pressure & Molecular Motion

Pressure is proportional to both particle density and average kinetic energy:

$$
P \propto \frac{N}{V} \cdot \langle KE \rangle
$$

Where:
- $\frac{N}{V}$ = particle density  

From this relationship:
- Increasing particle number increases pressure  
- Decreasing volume increases pressure  
- Increasing temperature increases pressure  

<br>

### Pressure & Volume

Volume is inversely related to pressure when temperature is constant:

$$
P \propto \frac{1}{V} \quad (\text{at constant } T, n)
$$

This explains compression and expansion behavior in sealed systems such as pistons and gas chambers.

<br>

### Continuity Equation

Atmospheric flow approximately conserves mass.

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
$$

Where:
- $\rho$ = density  
- $\mathbf{v}$ = velocity field  

Applications:
- Fluid flow modeling
- Numerical weather simulations
- Atmospheric circulation analysis


--- PAGE ---

## Temperature, Humidity, and Atmospheric State

Meteorologists do not simply measure current atmospheric conditions; they use physical laws, observational data, and numerical models to predict how those conditions will evolve over time. Forecasting temperature, humidity, and pressure involves tracking how air masses move, exchange energy, and interact with radiation, moisture, and terrain.

Modern forecasts combine:
- Surface weather stations
- Weather balloons (radiosondes)
- Satellites
- Radar systems
- Numerical weather prediction (NWP) models

These data sources are continuously assimilated into computational models that solve atmospheric equations forward through time.

<br>

### Temperature Forecasting

Future air temperature is predicted by modeling:
- Solar heating
- Infrared cooling
- Advection of warm or cold air masses
- Cloud cover effects
- Surface heat exchange

One important mechanism is **advection**, where moving air transports heat horizontally:

$$
\frac{\partial T}{\partial t}
=
-\vec{v}\cdot\nabla T
$$

Where:
- $T$ = temperature
- $\vec{v}$ = wind velocity vector
- $\nabla T$ = spatial temperature gradient

This relationship shows that wind moving across temperature gradients changes local temperature over time.

Forecast models also account for:
- Day/night radiation cycles
- Ocean influence
- Elevation effects
- Urban heat island effects
- Seasonal solar angle variation

<br>

### Humidity and Dew Point Prediction

Humidity forecasts depend on predicting:
- Moisture transport
- Evaporation
- Condensation
- Cloud formation
- Precipitation processes

Meteorologists often track **specific humidity** or **mixing ratio**, which measures water vapor content in air.

Relative humidity depends strongly on temperature because warmer air can hold more moisture. Even if water vapor remains constant, cooling air increases relative humidity.

A common forecasting relationship is:

$$
RH = \frac{e}{e_s(T)} \times 100
$$

Where:
- $RH$ = relative humidity
- $e$ = actual vapor pressure
- $e_s(T)$ = saturation vapor pressure at temperature $T$

Forecasting humidity therefore requires simultaneous prediction of both:
- Atmospheric moisture content
- Future temperature

Dew point forecasting is especially important because it helps predict:
- Fog formation
- Cloud development
- Thunderstorm potential
- Human comfort levels

<br>

### Atmospheric Pressure Prediction

Pressure forecasts are produced by modeling the movement and interaction of large-scale air masses.

Pressure changes occur when:
- Air converges or diverges
- Air columns warm or cool
- Storm systems intensify or weaken

A key forecasting principle is the pressure-gradient relationship:

$$
\vec{F}_p = -\frac{1}{\rho}\nabla P
$$

Where:
- $\vec{F}_p$ = pressure-gradient force
- $\rho$ = air density
- $\nabla P$ = pressure gradient

Pressure gradients drive wind, which then redistributes heat and moisture throughout the atmosphere.

Meteorologists monitor:
- High-pressure ridges
- Low-pressure cyclones
- Frontal boundaries
- Jet stream structure

to predict future atmospheric evolution.

<br>

### Wind Chill and Heat Index Forecasting

Forecasts of apparent temperature combine meteorological predictions with empirical human-response models.

Wind chill forecasts use predicted:
- Air temperature
- Wind speed

because stronger winds increase heat loss from exposed skin.

Heat index forecasts combine:
- Temperature
- Relative humidity

since high humidity reduces evaporative cooling from perspiration.

These quantities are forecast indirectly by first predicting the underlying atmospheric variables through numerical weather models.

<br>

### Adiabatic Cooling and Expansion

As air rises, pressure decreases and the air expands, causing cooling without heat exchange.

Dry adiabatic lapse rate:

$$
\Gamma_d = -\frac{dT}{dz} \approx 9.8^\circ \text{C/km}
$$

Where:
- $\Gamma_d$ = dry adiabatic lapse rate  
- $\frac{dT}{dz}$ = rate of temperature change with altitude  

Applications:
- Cloud formation
- Atmospheric stability
- Thunderstorm development


--- PAGE ---

## Wind and Atmospheric Motion

Wind represents the movement of air caused primarily by differences in atmospheric pressure. Predicting atmospheric motion is one of the central goals of meteorology because wind transports heat, moisture, pollutants, and storm systems across the planet. Modern forecasting combines observational data with fluid dynamics models that simulate the atmosphere as a moving fluid system.

Meteorologists predict:
- Wind speed and direction
- Wind gust intensity
- Jet stream behavior
- Frontal movement
- Convective and storm-related motion

These forecasts rely heavily on numerical weather prediction (NWP), satellite observations, radar data, and upper-atmosphere measurements.

<br>

### Pressure Gradients and Wind Formation

Wind develops because air naturally accelerates from regions of higher pressure toward regions of lower pressure.

The pressure-gradient force is given by:

$$
\vec{F}_p = -\frac{1}{\rho}\nabla P
$$

Where:
- $\vec{F}_p$ = pressure-gradient force
- $\rho$ = air density
- $\nabla P$ = spatial pressure gradient

Stronger pressure gradients produce stronger winds. Closely packed isobars on weather maps therefore indicate regions of potentially high wind speed.

Forecast models track how pressure systems evolve over time in order to predict future wind patterns.

<br>

### Coriolis Effect and Wind Direction

Because Earth rotates, moving air is deflected by the Coriolis effect. This causes winds to curve rather than travel in straight lines.

The Coriolis acceleration is:

$$
\vec{a}_c = -2\vec{\Omega} \times \vec{v}
$$

Where:
- $\vec{a}_c$ = Coriolis acceleration
- $\vec{\Omega}$ = Earth's rotational vector
- $\vec{v}$ = velocity of the moving air parcel

This effect:
- Deflects winds to the right in the Northern Hemisphere
- Deflects winds to the left in the Southern Hemisphere
- Influences global circulation and storm rotation

Meteorologists must account for Coriolis effects when predicting:
- Cyclones and hurricanes
- Jet stream motion
- Large-scale wind circulation

<br>

### Doppler Shift and Wind Measurement

Doppler radar measures wind velocity by detecting frequency shifts in reflected signals.

$$
\Delta f = \frac{2v}{\lambda}
$$

Where:
- $\Delta f$ = frequency shift  
- $v$ = radial velocity of target  
- $\lambda$ = radar wavelength  

Applications:
- Storm rotation detection
- Wind field mapping
- Tornado identification

<br>

### Wind Speed and Gust Prediction

Forecasting wind speed involves predicting:
- Pressure gradients
- Atmospheric stability
- Surface friction
- Turbulence and vertical mixing

Wind gusts occur when turbulent air transfers faster-moving air from higher altitudes downward toward the surface.

Meteorologists analyze:
- Boundary layer instability
- Convective mixing
- Thunderstorm outflows
- Terrain effects

to estimate potential gust intensity.

Strong gust forecasting is especially important for:
- Aviation
- Marine forecasting
- Severe weather warnings
- Wildfire behavior prediction

<br>

### Jet Stream Prediction

Jet streams are narrow bands of extremely fast-moving air located in the upper atmosphere. They form primarily due to strong horizontal temperature gradients between air masses.

Forecasting jet stream position is critical because jet streams:
- Steer storm systems
- Influence temperature patterns
- Enhance severe weather development
- Affect aviation routes

Upper-atmosphere wind behavior is modeled using conservation of momentum and large-scale fluid dynamics equations.

Meteorologists track:
- Rossby wave patterns
- Polar jet displacement
- Subtropical jet interactions
- Upper-level troughs and ridges

to predict long-range atmospheric motion.

<br>

### Front Movement and Air Mass Interaction

Fronts form where contrasting air masses meet. Their movement determines many short-term weather changes.

Major front types include:
- Cold fronts
- Warm fronts
- Stationary fronts
- Occluded fronts

Fronts are predicted by tracking:
- Air mass velocity
- Temperature gradients
- Moisture transport
- Pressure evolution

Cold fronts often produce:
- Rapid temperature drops
- Strong winds
- Thunderstorms
- Convective instability

Warm fronts typically produce:
- Gradual warming
- Extended cloud cover
- Steady precipitation

Numerical models simulate how these boundaries evolve over time to forecast future weather conditions.

<br>

### Convective Activity and Vertical Motion

Convective activity occurs when warm, less dense air rises through cooler surrounding air. This process drives:
- Thunderstorms
- Heavy rainfall
- Turbulence
- Severe weather development

One important mechanism is buoyancy:

$$
F_b \propto (\rho_{\text{environment}} - \rho_{\text{parcel}})
$$

Where:
- $F_b$ = buoyant force
- $\rho_{\text{parcel}}$ = density of rising air
- $\rho_{\text{environment}}$ = surrounding air density

If rising air remains warmer and less dense than its surroundings, convection intensifies.

Convective prediction is essential for forecasting:
- Severe thunderstorms
- Tornado environments
- Lightning activity
- Flash flooding

<br>

### Geostrophic Wind

At large scales and away from surface friction, winds often approach geostrophic balance, where the pressure-gradient force and Coriolis force balance each other.

The geostrophic wind speed is approximated by:

$$
V_g = \frac{1}{f\rho}\frac{\partial P}{\partial n}
$$

Where:
- $V_g$ = geostrophic wind speed
- $f$ = Coriolis parameter
- $\rho$ = air density
- $\frac{\partial P}{\partial n}$ = pressure gradient perpendicular to flow

Geostrophic flow is especially important in:
- Jet stream dynamics
- Midlatitude weather systems
- Large-scale atmospheric circulation

<br>

### Atmospheric Advection

Wind transports atmospheric properties such as temperature and moisture through advection.

A simplified advection relationship is:

$$
\frac{\partial T}{\partial t} = -\vec{v} \cdot \nabla T
$$

Where:
- $T$ = temperature
- $\vec{v}$ = wind velocity vector
- $\nabla T$ = temperature gradient

Strong temperature advection often signals:
- Frontal movement
- Storm development
- Rapid temperature changes

<br>

### Wind Shear

Wind shear describes how wind speed or direction changes with height.

$$
\text{Shear} = \frac{\Delta v}{\Delta z}
$$

Where:
- $\Delta v$ = change in wind velocity
- $\Delta z$ = change in altitude

Strong wind shear is associated with:
- Severe thunderstorms
- Tornado formation
- Turbulence
- Hurricane organization

<br>

### Vorticity

Vorticity measures local atmospheric rotation.

$$
\boldsymbol{\omega} = \nabla \times \mathbf{v}
$$

Where:
- $\boldsymbol{\omega}$ = vorticity  
- $\mathbf{v}$ = velocity field  

Applications:
- Cyclone formation
- Tornado dynamics
- Large-scale atmospheric circulation


--- PAGE ---

## Precipitation

Hydrometeorology focuses on forecasting the movement, phase, accumulation, and cycling of water throughout the atmosphere and surface environment. Meteorologists predict precipitation by combining atmospheric thermodynamics, cloud microphysics, fluid dynamics, radar observations, satellite data, and numerical weather prediction models.

Forecasting hydrological conditions involves predicting:
- When precipitation will occur
- How much precipitation will accumulate
- Whether it will fall as rain, snow, sleet, or freezing rain
- How water interacts with soil, rivers, vegetation, and reservoirs

<br>

### Rainfall Accumulation Forecasting

Rainfall accumulation depends on:
- Moisture content
- Storm duration
- Atmospheric lift strength
- Storm movement speed

One important atmospheric quantity is precipitable water (PW), which estimates the total water vapor available in a vertical atmospheric column.

Precipitable water is commonly modeled as:

$$
PW = \frac{1}{\rho_w g}\int_{p_t}^{p_s} q \, dp
$$

Where:
- $PW$ = precipitable water  
- $\rho_w$ = density of liquid water  
- $g$ = gravitational acceleration  
- $q$ = specific humidity  
- $p_s$ = surface pressure  
- $p_t$ = pressure at the top of the atmospheric column  

Higher precipitable water values indicate greater atmospheric moisture availability and an increased potential for heavy rainfall. Slow-moving or training thunderstorms can produce extreme rainfall accumulation and flash flooding.

Meteorologists use:
- Radar-derived rainfall estimates
- Numerical precipitation models
- River basin hydrology models
- Soil saturation data

to estimate flood potential.

<br>

### Flood Risk Prediction

Flood forecasting combines meteorology with hydrology to predict how precipitation will move through rivers, streams, and drainage systems.

A simplified water balance relationship is:

$$
P = R + E + \Delta S
$$

Where:
- $P$ = precipitation
- $R$ = runoff
- $E$ = evaporation
- $\Delta S$ = change in stored water

Meteorologists and hydrologists use:
- River gauge data
- Watershed models
- Terrain elevation maps
- Land surface models

to predict river rise and flooding potential.

<br>

### Thunderstorm Probability

Thunderstorms develop when warm, moist air rises rapidly through an unstable atmosphere. Forecasting thunderstorm probability therefore requires predicting:
- Atmospheric instability
- Moisture availability
- Vertical lift
- Wind shear

One of the most important instability measures is Convective Available Potential Energy (CAPE):

$$
CAPE = \int g \left(\frac{T_p - T_e}{T_e}\right) dz
$$

Where:
- $g$ = gravitational acceleration
- $T_p$ = temperature of the rising air parcel
- $T_e$ = environmental temperature
- $dz$ = vertical height increment

Higher CAPE values indicate greater potential for strong upward motion and severe convection.

Meteorologists also monitor:
- Frontal boundaries
- Drylines
- Surface heating
- Upper-level disturbances

to determine where thunderstorms are most likely to form.

<br>

### Clausius–Clapeyron Relation

The Clausius–Clapeyron equation describes how saturation vapor pressure changes with temperature. Warmer air can sustain much higher amounts of water vapor before condensation occurs, making this relationship fundamental to cloud formation and precipitation forecasting.

$$
\ln\left(\frac{P_1}{P_2}\right)
=
\left(
-\frac{\Delta H_{\text{vap}}}{R}
\right)
\left(
\frac{1}{T_2} - \frac{1}{T_1}
\right)
+ C
$$

Where:
- $P_1, P_2$ = vapor pressures at temperatures $T_1$ and $T_2$  
- $\Delta H_{\text{vap}}$ = enthalpy of vaporization  
- $R$ = universal gas constant  
- $T_1, T_2$ = absolute temperatures  
- $C$ = integration constant  

This relationship is important for:
- Predicting cloud formation
- Modeling atmospheric humidity
- Estimating precipitation potential
- Understanding how warming climates influence extreme rainfall

<br>

### Radar Reflectivity and Rainfall Estimation

Weather radar estimates precipitation intensity using radar reflectivity.

A common empirical relationship is:

$$
Z = aR^b
$$

Where:
- $Z$ = radar reflectivity
- $R$ = rainfall rate
- $a,b$ = empirically determined constants

Higher reflectivity values generally indicate heavier precipitation.

<br>

### Moisture Transport

Atmospheric moisture transport is often modeled using moisture flux:

$$
\vec{F}_q = q\vec{v}
$$

Where:
- $\vec{F}_q$ = moisture flux
- $q$ = specific humidity
- $\vec{v}$ = wind velocity vector

Strong moisture flux can support:
- Heavy rainfall
- Atmospheric rivers
- Tropical cyclone intensification

<br>

### Vertical Atmospheric Motion

Rising air cools adiabatically, allowing condensation and precipitation development.

A simplified vertical motion relationship is:

$$
w = \frac{dz}{dt}
$$

Where:
- $w$ = vertical velocity
- $z$ = altitude
- $t$ = time

Strong upward vertical motion is associated with:
- Thunderstorm formation
- Heavy rainfall
- Frontal precipitation
- Orographic lifting


--- PAGE ---

## Oceanic and Climate Systems

Oceanic and climate systems describe large-scale interactions between the atmosphere, oceans, solar energy, and Earth’s rotation. Meteorologists and climate scientists predict these systems using satellite observations, ocean buoys, atmospheric circulation models, and long-term statistical analysis to understand how energy and moisture move throughout the planet.

<br>

### Ocean Surface Temperature Prediction

Ocean surface temperature strongly influences atmospheric circulation, storm formation, precipitation patterns, and long-term climate behavior. Forecasting sea surface temperatures involves combining the following through:
- Solar heating
- Evaporation and cooling
- Ocean current transport
- Vertical mixing and upwelling

A simplified surface heat balance relationship is:

$$
\Delta Q = mc\Delta T
$$

Where:
- $\Delta Q$ = heat energy change  
- $m$ = mass of water  
- $c$ = specific heat capacity  
- $\Delta T$ = temperature change  

Because water has a very high heat capacity, oceans store and redistribute enormous amounts of thermal energy, making them a major driver of global climate patterns.

Ocean temperature prediction is critical for:
- Hurricane forecasting
- El Niño and La Niña prediction
- Fisheries and marine ecosystems
- Seasonal climate outlooks

<br>

### Wave Height and Ocean Condition Forecasting

Ocean wave forecasts are generated by modeling how wind transfers energy into the ocean surface. Wave energy increases as stronger winds act over larger areas for longer periods of time.

A simplified wave speed relationship in deep water is:

$$
v = \sqrt{\frac{g\lambda}{2\pi}}
$$

Where:
- $v$ = wave speed  
- $g$ = gravitational acceleration  
- $\lambda$ = wavelength  

Wave forecasting is important for:
- Marine transportation
- Coastal safety
- Hurricane impact prediction
- Offshore engineering
- Navigation systems

<br>

### Tide Prediction

Tides are periodic changes in sea level caused primarily by the gravitational interactions between Earth, the Moon, and the Sun. Tide forecasting combines:
- Orbital mechanics
- Coastal geometry
- Ocean basin resonance
- Rotational effects of Earth
The gravitational force relationship governing tidal effects is:

$$
F = G\frac{m_1 m_2}{r^2}
$$

Where:
- $F$ = gravitational force  
- $G$ = gravitational constant  
- $m_1, m_2$ = interacting masses  
- $r$ = distance between bodies  

Tidal prediction systems use harmonic analysis to model repeating tidal cycles produced by lunar and solar motion.

Meteorologists and oceanographers forecast:
- High and low tide timing
- Tidal range
- Coastal flooding risk
- Storm surge interaction with tides

<br>

### Wind Stress on Ocean Surface

Momentum transfer from wind to ocean surface is described by:

$$
\tau = \rho_{air} C_d U^2
$$

Where:
- $\tau$ = wind stress  
- $\rho_{air}$ = air density  
- $C_d$ = drag coefficient  
- $U$ = wind speed  

This is the primary driver of wave formation and surface currents.

<br>

### Heat Transport in the Ocean

Ocean temperature evolves through both transport and diffusion of heat:

$$
\frac{\partial T}{\partial t} + \vec{u} \cdot \nabla T = \kappa \nabla^2 T
$$

Where:
- $T$ = temperature  
- $\vec{u}$ = ocean current velocity  
- $\kappa$ = thermal diffusivity  

This equation captures how ocean currents redistribute heat globally.

<br>

### Conservation of Mass in Ocean Flow

Ocean circulation obeys continuity of incompressible flow:

$$
\nabla \cdot \vec{u} = 0
$$

Where:
- $\vec{u}$ = velocity field of ocean water  

This constraint governs all large-scale ocean current systems.

<br>

### Geostrophic Ocean Flow

Large-scale ocean currents are often governed by a balance between pressure gradients and Coriolis force:

$$
f \vec{v} = -\frac{1}{\rho} \nabla P
$$

Where:
- $f$ = Coriolis parameter  
- $\vec{v}$ = ocean velocity  
- $P$ = pressure  

This explains major currents such as:
- Gulf Stream
- Kuroshio Current
- Antarctic Circumpolar Current

<br>

### Thermal Expansion and Sea Level Rise

Ocean volume increases with temperature:

$$
\Delta V = \beta V_0 \Delta T
$$

Where:
- $\beta$ = thermal expansion coefficient  
- $V_0$ = initial volume  
- $\Delta T$ = temperature change  

This is a major contributor to long-term sea level rise.

<br>

### Planetary Energy Balance

Earth’s climate is governed by the balance between incoming and outgoing radiation:

$$
(1 - \alpha) S = \sigma T^4
$$

Where:
- $\alpha$ = albedo  
- $S$ = incoming solar radiation  
- $\sigma$ = Stefan–Boltzmann constant  
- $T$ = Earth temperature  

This relationship governs long-term climate stability.


--- PAGE ---

## Air Quality and Environmental Monitoring

Air quality and environmental monitoring focus on measuring and predicting the composition of the atmosphere, particularly the presence and movement of pollutants, aerosols, and particulate matter. These systems combine ground-based sensors, satellite observations, and atmospheric transport models to track how contaminants spread and evolve over time.

<br>

### Air Quality and Particulate Concentration

Air quality is determined by the concentration of harmful or trace particles suspended in the atmosphere, including PM2.5 and PM10 particulate matter. Forecasting these concentrations requires modeling both emission sources and atmospheric removal processes such as deposition and chemical breakdown.

Key factors influencing particulate concentration include:
- Industrial and vehicular emissions
- Wind-driven dispersion
- Atmospheric stability and inversion layers
- Chemical reactions in the atmosphere
- Wet and dry deposition processes

A simplified concentration evolution model is:

$$
\frac{dC}{dt} = E - D - A
$$

Where:
- $C$ = pollutant concentration  
- $E$ = emission rate  
- $D$ = deposition/removal rate  
- $A$ = atmospheric dispersion or dilution  

High pollution events often occur when emissions accumulate faster than atmospheric mixing can disperse them, especially under stagnant weather conditions.

<br>

### Aerosol Concentration and Atmospheric Effects

Aerosols are fine solid or liquid particles suspended in the atmosphere that influence both air quality and radiative balance. They include dust, soot, sea salt, and industrial pollutants.

Aerosol behavior is influenced by:
- Particle size distribution
- Humidity and condensation processes
- Wind transport and mixing
- Chemical transformation in the atmosphere

A key relationship used in atmospheric optics is:

$$
\tau = \int \alpha(z)\,dz
$$

Where:
- $\tau$ = optical depth  
- $\alpha(z)$ = extinction coefficient at altitude $z$  

Higher aerosol concentrations increase optical depth, reducing visibility and altering solar radiation reaching Earth’s surface.

Aerosols also contribute to:
- Cloud formation (acting as condensation nuclei)
- Radiative forcing (cooling or warming effects)
- Long-range transport of pollutants

<br>

### Pollution Transport and Atmospheric Dispersion

Pollution transport describes how contaminants move through the atmosphere under the influence of wind fields, turbulence, and large-scale circulation systems. Forecasting pollutant movement requires solving advection-diffusion processes.

A simplified transport model is:

$$
\frac{\partial C}{\partial t} + \mathbf{u} \cdot \nabla C = K \nabla^2 C
$$

Where:
- $C$ = pollutant concentration  
- $\mathbf{u}$ = wind velocity field  
- $K$ = diffusion coefficient  

This equation captures:
- Advection (transport by wind)
- Diffusion (spreading due to turbulence)
- Temporal concentration changes

Pollution transport models are used to predict:
- Urban smog formation
- Industrial emission spread
- Cross-border pollution movement
- Long-range atmospheric contamination

<br>

### Particle Settling Velocity

Larger particles fall out of the atmosphere due to gravity:

$$
v_s = \frac{2}{9} \frac{r^2 (\rho_p - \rho_a) g}{\mu}
$$

Where:
- $v_s$ = settling velocity  
- $r$ = particle radius  
- $\rho_p$ = particle density  
- $\rho_a$ = air density  
- $\mu$ = dynamic viscosity of air  

This explains why:
- PM10 settles faster than PM2.5
- Fine particles remain suspended longer and travel farther