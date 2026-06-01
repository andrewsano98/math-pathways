<!-- 
title: "Math in Art"
output: html_document
bibliography: rmarkdown.bib
 -->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/animation_photo_1.gif"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Animation
    </h1>
  </div>

</div>


<br>

### What can I do?
- Creating digital illustrations, animations, and visual designs using software such as Photoshop, Blender, and Procreate  
- Applying color theory, composition, perspective, and lighting techniques in visual design workflows  
- Using 2D and 3D modeling tools to develop environments, characters, and visual assets  
- Editing and refining artwork using digital rendering, photo manipulation, and visual effects tools  
- Working with graphic tablets, rendering engines, and asset pipelines for digital production  
- Collaborating with designers, animators, and creative teams to produce visual media and interactive content  
- Iterating visual concepts based on aesthetic goals, audience feedback, and production requirements  


<br>

### What math concepts do I need to know?
- Geometry  
- Proportions and Ratios  
- Symmetry  
- Transformations  
- Spatial Reasoning  
- Perspective  
- Measurement and Scaling  
- Patterns and Sequences  
- Trigonometry
- Physics


--- PAGE ---

## Elements & Principles of Design

The elements and principles of design form the visual foundation of animation, illustration, film, and digital media. The **elements of design** are the basic visual components used to construct an image, while the **principles of design** describe how those components are arranged to create structure, clarity, and visual impact.

Together, these concepts guide:
- Composition and staging
- Character and environment design
- Visual storytelling
- Motion and scene readability
- Emotional tone and audience attention

<br>

### Design Elements

The elements of design are the fundamental visual components used to build artwork and animation.

| Element | Description | Common Uses in Animation |
|---|---|---|
| **Line** | Defines edges, direction, and motion | Gesture drawing, motion trails, outlines |
| **Shape** | Two-dimensional enclosed areas | Character silhouettes, symbols, graphic design |
| **Form** | Three-dimensional structure and volume | Character modeling, perspective drawing |
| **Space** | Distance and relationship between objects | Depth, staging, camera composition |
| **Color** | Hue, saturation, and brightness relationships | Mood, lighting, emotional tone |
| **Value** | Lightness and darkness of surfaces | Shading, contrast, readability |
| **Texture** | Surface appearance or visual detail | Materials, realism, stylization |

<br>

### Design Principles

The principles of design describe how visual elements are organized into effective compositions. Different educational systems define slightly different sets of principles, but most overlap substantially.

| Principle | Description | Common Uses in Animation |
|---|---|---|
| **Balance** | Distribution of visual weight | Stable compositions, scene framing |
| **Unity** | Sense of visual cohesion | Consistent artistic style |
| **Variety** | Introduction of visual differences | Preventing visual monotony |
| **Emphasis** | Directing viewer attention | Focal points, important actions |
| **Movement** | Guiding the eye through an image | Action scenes, camera flow |
| **Pattern** | Repeated visual structures | Clothing, backgrounds, decorative motifs |
| **Proportion** | Relative size relationships | Character scaling, perspective |
| **Contrast** | Strong visual differences | Lighting, color separation, readability |
| **Repetition** | Reuse of visual elements | Rhythm, consistency, animation cycles |
| **White Space** | Intentional empty areas | Clarity, focus, composition control |
| **Rhythm** | Visual pacing and repetition | Motion timing, scene flow |
| **Hierarchy** | Ordering of visual importance | UI design, staging, focal structure |
| **Harmony** | Overall visual compatibility | Color palettes, unified compositions |

<br>

### Application in Animation and Visual Media

In animation, these concepts are not isolated artistic ideas but practical tools used continuously throughout production.

Applications include:
- Character silhouette readability
- Environment composition
- Camera staging
- Lighting and color scripting
- Motion clarity
- Visual pacing
- Interface and graphic design
- Scene organization and storytelling

Strong control of design elements and principles improves both the aesthetic quality and communicative clarity of animated work.


--- PAGE ---

## 3D Modeling and Rendering

3D modeling extends traditional drawing into a fully three-dimensional digital space. Instead of working on a flat surface, artists construct objects using virtual coordinates, building forms that exist in a simulated environment with height, width, and depth. This shift transforms drawing from a purely visual act into a spatial construction process grounded in geometry.

At its core, 3D art is built on mathematical representations of space, where every object is defined by points in a coordinate system and manipulated through geometric operations.


<br>

### Coordinate Systems and Spatial Representation

3D space is typically described using a Cartesian coordinate system with three axes:

- **X-axis**: left to right  
- **Y-axis**: up and down  
- **Z-axis**: forward and backward (depth)

Every point in a 3D scene can be defined as:

$$
P = (x, y, z)
$$

Objects are constructed by connecting these points into structures such as edges, faces, and volumes. This allows artists to build complex models from simple geometric components.


<br>

### Geometry: The Building Blocks of 3D Models

3D models are made from geometric elements called **primitives**, such as:

- Cubes
- Spheres
- Cylinders
- Planes
- Cones

These primitives are often modified and combined to create more complex forms. A common workflow involves starting with a basic shape and progressively refining it through subdivision, extrusion, and deformation.

The relationships between points, edges, and faces form what is called a **mesh**, which is the underlying structure of most 3D models.


<br>

### Transformations in 3D Space

To manipulate objects, artists use geometric transformations. These include:

- **Translation**: moving an object through space
- **Rotation**: spinning an object around an axis
- **Scaling**: resizing an object proportionally or non-uniformly

Mathematically, scaling in 3D can be expressed as:

$$
(x', y', z') = (kx, ky, kz)
$$

Where $ k $ is the scaling factor applied to each axis.

These transformations allow for precise control over object placement and orientation within a scene.


<br>

### Surfaces, Normals, and Form

Each face of a 3D model has a direction called a **normal vector**, which indicates which way the surface is facing. Normals are essential for determining how light interacts with a surface.

For a surface to be shaded correctly, the renderer calculates the angle between the light source and the surface normal. This determines how bright or dark the surface appears.


<br>

### Rendering: Turning Geometry into Images

Rendering is the process of converting 3D data into a 2D image. This involves simulating how light behaves in a virtual environment. The renderer calculates:

- Light sources and direction
- Material properties (reflectivity, roughness, transparency)
- Camera position and perspective
- Shadows and occlusion

The result is a final image that visually represents the 3D scene as if it were being viewed through a camera.


<br>

### Lighting and Material Simulation

Lighting in 3D graphics is based on physical and mathematical models. Common lighting components include:

- **Ambient light**: general base illumination
- **Diffuse lighting**: light scattered across rough surfaces
- **Specular highlights**: sharp reflections on shiny surfaces

Materials define how surfaces respond to light. For example:
- Metal reflects light sharply
- Plastic has softer highlights
- Matte surfaces scatter light evenly

These behaviors are controlled by mathematical shading models that approximate real-world physics.


<br>

### Perspective and Camera Systems

In 3D rendering, the camera determines how the scene is projected onto a 2D plane. This involves perspective projection, where objects farther from the camera appear smaller.

This relationship is governed by projection mathematics, where depth affects scale:

$$
\text{projected size} \propto \frac{1}{z}
$$

This is the same principle used in traditional perspective drawing, but implemented through computational geometry.


--- PAGE ---

## Mathematical Foundations for Balance

Mathematical Foundations for Balance examines the quantitative principles that govern visual stability, proportion, and spatial organization in two-dimensional composition. Rather than treating balance as a purely aesthetic judgment, this framework describes it as a structured outcome of geometric relationships, proportional systems, and spatial distribution. Across visual disciplines such as drawing, painting, photography, and digital design, balance emerges from consistent mathematical constraints that determine how elements occupy space and relate to one another. This section establishes the core mathematical tools used to analyze and construct visually coherent and stable compositions.

<br>

1. **Perspective Geometry**  
    Perspective is the mathematical projection of three-dimensional space onto a two-dimensional surface. It is based on vanishing points, horizon lines, and the convergence of parallel lines, which together create the illusion of depth and spatial consistency in visual composition.

<br>

2. **Anatomy and Proportional Systems**  
    Human and animal forms are structured using proportional ratios that define spatial relationships within the body. These include head-to-body ratios, limb-to-torso ratios, and principles of symmetry and bilateral structure, all of which provide consistency and realism in figurative representation.

<br>

3. **Rule of Thirds**  
    The Rule of Thirds divides the canvas into a 3 × 3 grid to guide compositional balance and focal placement. Key intersections of this grid are often used to position important visual elements, creating natural emphasis and visual harmony:

$$
\left(\frac{1}{3}, \frac{2}{3}\right)
$$

<br>

4. **Golden Ratio**  
    The Golden Ratio is a classical proportional system frequently used in composition and design to achieve aesthetically balanced layouts. It is defined as:

$$
\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618
$$

> It is also expressed through proportional relationships:

$$
\frac{a + b}{a} = \frac{a}{b} = \phi
$$

> This ratio is commonly applied in composition layout, framing, spacing between elements, and spiral-based visual structures.

<br>

5. **Color Gradients and Interpolation**  
    Color gradients are created through mathematical interpolation between color values, allowing smooth transitions across visual space. A common form is linear interpolation:

$$
C(t) = (1 - t)C_1 + tC_2
$$

> Where:
> - $C_1$ and $C_2$ are color values  
> - $t \in [0,1]$ represents interpolation position between the two colors  


--- PAGE ---

## Physics in Animation

Modern animation is deeply connected to physics and mathematics. Even highly stylized animation relies on physical intuition to create believable motion, spatial consistency, timing, and interaction between objects. Whether animating a bouncing ball, a moving camera, cloth simulation, or a fully rigged character, animation systems must continuously calculate how objects move and transform through space over time.

At its core, animation physics is the study of motion, force, space, and transformation inside a simulated environment.

<br>

### Motion

The kinematic formulas can be used to represent motion in animation. The following four formulas are used in kinematic physics to describe motion of an object:

$$
v = v_0 + at
$$

$$
x = x_0 + v_0t + \frac{1}{2}at^2
$$

$$
v^2 = v_0^2 + 2a(x - x_0)
$$

$$
x = x_0 + \frac{(v + v_0)}{2}t
$$

Where:
- $x$ = position
- $x_0$ = initial position
- $v$ = final velocity
- $v_0$ = initial velocity
- $a$ = acceleration
- $t$ = time

<br>

### Space

Transformations describe how objects change position, scale, and orientation within 2D or 3D space. Every animated object undergoes continuous transformations between frames.

Common transformations include:
- translation
- rotation
- scaling
- skewing

These operations are typically handled using vectors and matrices inside animation software and game engines.

Transformations are foundational in rigging, camera systems, object movement, 3D modeling and scene construction. One of the simplest ways to represent this is the linear transformation form of matrix multiplication:

$$
A\mathbf{x} = \mathbf{b}
$$

Where:
- $A$ = transformation matrix
- $\mathbf{x}$ = original vector or object coordinates
- $\mathbf{b}$ = transformed output vector

This formula is most commonly used to transform objects within 2D and 3D space, including operations such as rotation, scaling, translation, and camera movement. These calculations work in the backend in digital art programs such as Photoshop when adjusting the size, shape and orientation of an image.


--- PAGE ---

## Animation Software

Modern animation and digital art rely heavily on 3D modeling software to create characters, environments, props, visual effects, and cinematic scenes. These tools combine artistic design with geometry, physics, lighting systems, and motion simulation to construct virtual worlds.

Some of the most common industry tools include:

- **Blender** — open-source 3D modeling, animation, sculpting, rendering, and simulation software
- **ZBrush** — digital sculpting software used for highly detailed characters and organic models
- **Maya** — industry-standard software for animation, rigging, simulation, and film production

These programs are used throughout:
- animation
- motion graphics
- video games
- visual effects (VFX)
- architectural visualization
- film production
- character design
- environment creation

Core workflows in 3D production include sculpting, mesh design, character and environment modeling, UV mapping and texturing, rigging and skeletal systems, lighting, rendering and motion simulation

At its core, 3D art is the process of mathematically representing objects within simulated space and then animating how those objects move, deform, and interact over time.

<br>

### Frames and the Illusion of Motion

Animation works by exploiting a perceptual phenomenon called **persistence of vision**, where the human eye blends rapidly changing images into continuous movement. Each image shown is called a **frame**, and small differences between frames generate perceived motion.

Key concepts include:

- **Frame rate (FPS)** — number of frames displayed per second (commonly 24, 30, or 60 FPS)
- **Keyframes** — major poses or important motion states defined by the animator
- **In-betweens (Tweening)** — intermediate frames automatically or manually generated between keyframes

Higher frame rates and smoother transitions generally produce more fluid and realistic movement.

Animation systems must continuously calculate:
- position
- rotation
- scaling
- deformation
- velocity
- timing

between frames in order to maintain smooth motion.

<br>

### Curves and Interpolation

Smooth movement in animation is usually controlled using interpolation curves rather than straight linear motion. These curves mathematically determine how objects accelerate, decelerate, and transition between positions over time.

Two of the most common systems are:

- **Bezier Curves**
- **B-Splines**

Bezier curves are especially common in:
- motion paths
- vector graphics
- camera movement
- animation easing systems

A cubic Bezier curve can be represented as:

$$
B(t) = (1-t)^3P_0 + 3(1-t)^2tP_1 + 3(1-t)t^2P_2 + t^3P_3
$$

Where:
- $P_0, P_1, P_2, P_3$ = control points
- $t$ = interpolation parameter between $0$ and $1$

These curves allow animators to create:
- smooth arcs
- natural acceleration
- controlled motion paths
- organic movement transitions

B-Splines extend these ideas further by smoothly connecting multiple curve segments together, making them highly useful in:
- CAD systems
- 3D modeling
- surface generation
- industrial design
- animation rigs

<br>

### Layers of Motion

Complex animated scenes contain multiple overlapping motion systems operating simultaneously. Professional animation often separates motion into layers so that each system can be controlled independently.

Examples include:

- **Primary motion** — major body movement or object motion
- **Secondary motion** — hair, cloth, tails, accessories, muscles
- **Environmental motion** — wind, particles, debris, water, foliage
- **Camera motion** — movement of the viewer perspective itself

These layers interact physically and visually but do not move identically. Small timing differences between layers create realism and prevent motion from appearing rigid or artificial.

This layered approach is fundamental in:
- character animation
- CGI films
- game animation
- motion graphics
- visual effects pipelines