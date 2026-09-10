# Mechanical Construction of BLDC Motors
In this section, an introduction to BLDC motors in the concept of electric motors is discussed, as well as mechanical characteristics and its effect on variables.

Taken from the background section of my own BLDC motor driver documentation.

## 1. Brushed vs Brushless DC Motors

DC motors are typically composed of two concentric magnetic-field generating components: a circular array of permanent magnets for a fixed magnetic field, and a circular series of wound copper coils, which can act as variable magnets depending on the electrical current passed through them.

Brushless motors are distinct from brushed DC motors in their commutation method, or how current is switched in the copper motor windings to generate a moving magnetic field against the permanent magnets. 

In brushed motors, the wound coils are typically found in the rotor (the rotating component), where a direct-contact brush armature supplies a switching current to induce rotation against a permanent magnet stator, which remains stationary. In brushless motors, the wound coils are the unmoving stator, which requires an external circuit board to induce a spinning magnetic field, which generates resultant movement in the permanent-magnet rotor.

Brushed motors tend to experience higher noise and wear due to the direct contact of the brush armature against the spinning rotor, though it remains relatively low cost and un-complex in its hardware requirements. However, brushless motors thus experience longer lifespans and efficiencies, and lower noise from lack of direct-contact parts, but requires a more complex control scheme for the wound-coil stator from an electronic speed controller (ESC).

<img src="https://github.com/user-attachments/assets/edcf24f6-8f8a-4621-afab-b9fdcc575ab1" width="45%"> 

<hr width="30%">
<small>Image Source: https://www.dc-pump.com/brushed-vs-brushless-dc-pump-differences/</small>

## 2. Inrunner vs Outrunner Motors
The stator and rotor refer to concentric structures in a motor, with the former being stationary, and the latter being the spinning portion. In all BLDC motors, the rotor is composed of permanent magnets, while the stator is commonly constructed out of silicon steel laminations, with "teeth" for copper coils to be wound across. Winding copper coils essentially creates an inductor, that generates a magnetic field when an electrical current passes through it.

This is the basis of how BLDC motors generate movement - the PM rotor (with a fixed magnetic attribute, being permanent magnets) can spin against a stator composed of windings that can be controlled to have a changing magnetic field.

The orientation of the stator and rotor in relation to one another can impact the performance of a BLDC motor. As the permanent magnets always act as the spinning rotor in a BLDC, it can exhibit higher torques when set as the outer shell of the motor (outrunner motor), and higher speed when it is set as the inner component.

<img src="https://github.com/user-attachments/assets/b9857ae5-e30f-4db3-bcd4-7a00cdb9fccb" width="45%"> 

For the purposes of this repository, an outrunner BLDC motor is assumed and constructed in the example. Much of the calculations remain the same when it comes to the coiling section. However, the torque characteristics are the main differences, as well as the use of the air gap variable.

<hr width="30%">
Source: https://ican-motor.com/bldc-motor-specifications-about-motor-selection/

## 3. Statormaxxing

The stator is the stationary element in a motor. In all BLDCs, the stator houses copper coils that function as variable inductors to generate a moving magnetic field. Windings will be discussed in the next module, but this section will talk about the bare-bones construction of the stator _core_.

Stators can either be the outer component (inrunner BLDC), or the inner component (outrunner), and are comprised of several "teeth" (where copper is wound across) and equivalent "slots" (the space between each teeth). In three-phase motors, the number of teeth and slots are always a multiple of 3.

<img src="https://github.com/user-attachments/assets/45c5c600-b48c-4a15-9497-49da97b87930" width="45%"> 
<img src="https://github.com/user-attachments/assets/299bd69b-f38a-42b5-8c1b-0221c37277d2" width="41%"> 



Eddy current is a current loop that occurs within a piece of conductive material as a moving magnetic field, such as that of a spinning motor, is introduced in its vicinity. 

However, with any current loop, there can be a resistance dependent on the length of the loop, which inevitably can cause power loss according to the relation $I^2R$. 

Therefore, the stator of a BLDC is commonly constructed from a stacked lamination of silicon steel sheets. This stack is effective at breaking up eddy currents into several smaller current "loops," thereby reducing eddy current loss. 

<img src="https://github.com/user-attachments/assets/f587a38e-1ace-4b95-89a9-cefa195da36a" width="45%"> 

Source: https://www.allaboutcircuits.com/technical-articles/eddy-current-loss-what-it-is-and-how-to-reduce-it-with-laminated-cores/

The image on the left shows a changing flux B and its resultant eddy current formulation in a stator with laminations stacked _parallel_ to the current loops. The image on the right shows the example of laminate stacking _normal_ to the loops, which evidently does not change the size of the loops, and ineffective at reducing power dissipation.

<img src="https://github.com/user-attachments/assets/25b9917d-0150-4c00-af3e-b7a1df245a13" width="45%"> 

Source: Hendrik Vansompel (2012). "Evaluation of a Simple Lamination Stacking Method for the Teeth of an Axial Flux Permanent-Magnet Synchronous Machine With Concentrated Stator Windings." 

The mechanical construction of the stator core will affect the available space for copper to be wound for N turns, as well as the mean turn length of each coil. These dimensions are independent of KV, kt, and torque production.

<img src="https://github.com/user-attachments/assets/43ecae50-6b85-4873-b29a-7349ced2df8f" width="50%"> 
<img src="https://github.com/user-attachments/assets/574fdac0-b4ba-4c1e-9395-c9f14eb6a771" width="45%"> 

**Limitations in this Repo:**

In the calculator and derivations, the values for slot and tooth width/depth and stator stack lengths are inputted by the user. Approximate measurements are assumed, as the variables will only affect the "fill factor" - the feasibility of wiring N strands for N turns in a given stator, as well as the resistance and power dissipation chain. 

Furthermore, fillets on the stator core, winding imperfections, and buildup length can create small imperfections. Regardless, a tolerance variable is provided, and these estimations can be produced. Additionally, an estimation of copper length required for a single phase can be calculated.

## 4. Rotormaxxing

Characterization Note:
Motors can be characterized by size, and slot/pole configurations. For instance, a 36N42P motor with a 8110 stator core would have 36 teeth, 42 permanent magnet slots (always divisible by 2), with 21 pole pairs, a stator diameter of 81mm, and a stack length of 10mm.

### Permanent Magnet Rotor Structure
The structure of the PM rotor can influence motor characteristics such as torque output, flux linkage, and _cogging torque._ 

### Rotor Shell and Magnets
Generally, a circular array of rectangular neodymium-iron-boron (NdFeB) magnets are used in BLDC rotors. Neodymium magnets can possess a strength grade from N35 to N52. The magnet grade as well as its thickness can offer parameters for adjusting PM strength.

The material of the rotor shell to house the magnets is also considered. In general, the only 'useful' magnetic flux from the PMs is that directed inwards towards the stator, so generally a ferromagnetic material is selected to maximize efficiency and torque.

The following image (left) is from a video by Aaed Musa on YouTube, comparing the magnetic fields of that of a 3D-printed rotor shell as well as a steel shell.

<img src="https://github.com/user-attachments/assets/708217f4-bc75-4223-af83-3f238113f0af" width="45%"> 
<img src="https://github.com/user-attachments/assets/5b4dc9a5-03d7-4704-b6b5-cb621d23c948" width="25%"> 

As observed, a steel shell is effective at directing the PM flux inwards. Many DC motors also implement a _flux ring_ for this exact purpose (image on right).

### Air Gap Length vs. Air Gap Radius
Once again, confusion strikes with Google-based motor researching. This time is the distinction between two distinct terms: _air gap length_ and _air gap radius_. Occasionally these can be conflated.

The airgap is characterized by the empty space between the PM magnets and the stator teeth. Generally, a distance of 1mm or less is found here.

A smaller airgap is accompanied by a higher motor torque, as well as a higher cogging torque (a subtle step-like motion exhibited in concentrated winding-type motors, as the PMs rotate past its nearest coil).

The following figures provide a torque and cogging torque comparison for inrunner BLDC motors.

<img src="https://github.com/user-attachments/assets/fd9aeda9-7bcb-410e-a78e-02e0143d62d1" width="50%"> 
<img src="https://github.com/user-attachments/assets/227d6c13-86a0-4129-8e63-444387d25b50" width="48%"> 


<hr width="30%">
Source: https://www.emworks.com/en/blog/motor-design/effect-of-airgap-length-on-bldc-machine-performance

The same attributes can be seen in outrunner motors.

Gap Radius (or Air Gap Radius)
The length from the center of the motor to the midpoint of the airgap mentioned above (the space between the rotor and the stator), effectively operating as the **moment arm** for torque generation in equations. This is where we can see a distinction between inrunner and outrunner motors: as the PMs are farther from the center than inrunners, there is generally a much larger gap radius, consistent with its higher torque expectation.


### Flux Linkage
The concept of flux linkage is commonly used to describe the interactions of the generated magnetic fields through the inductor-like windings on each stator tooth. A smaller airgap radius will enhance the back-EMF.

According to Faraday's Law, any change in flux linkage over time generates a _back-EMF._

$$
E = -N \frac{d\phi}{dt}
$$

Where E is the induced back-EMF voltage (V), $\phi$ is the flux per coil (Wb, V*s or T*m^2).

$\therefore$  $N\phi = \lambda$ = total flux linkage for N coil turns. 

### Back-EMF, Ke and Kt
The term 'back-EMF' will be referenced multiple times throughout this repository. 

Back-EMF is an electromotive force that is generated as a motor spins, that opposes the direction of the input force.

It is also proportional to the motor's angular speed, and as such it can be measured during motor operation to indirectly measure the motor speed in **sensorless** motor control. 

This gives us another relationship:

$E = k_e * \omega$

Where E is the back-emf (V), $\omega$ is the angular speed in rad/s, and $k_e$ being the back-EMF constant, in V/rad/s, or sometimes V/kRPM.

Fun fact: Motor speed caps out when the input motor voltage equals the back-EMF.

Finally, we can establish a relation to the torque constant $K_t$:

$K_e = K_t$ 

*These numbers are actually the same when standardizing for units, what reference points are used for measurement (line-to-line or line-to-neutral for star configurations) and for an _ideal case_, meaning no mechanical drag or magnetic saturation. A more detailed derivation can be found in the Math folder in this repo.

$\tau = K_t * I$, where $\tau$ is the torque (N*m), and I is the current (A).

## 5. Winding Factor

Winding factor _Kw_ is dependent on three variables: 

$$
K_w = K_p * K_{skew} * K_d
$$

### i. Pitch factor 

The Pitch factor $K_p$ is always 1 in a concentrated winding (one coil per pole). In this calculator, distributed winding calculation is not included, although a more in-depth explanation of the difference can be found in the next module.

### ii. Magnet skew 

The skew constant $K_{skew}$ is an optional orientation parameter of the PM magnets on the rotor. This can be done to smooth out _cogging torque_. 

<img src="https://github.com/user-attachments/assets/471a7abe-e580-4280-836c-eaf094b9c34c" width="48%"> 

In electrical radians $\theta_{elec}$:

$$
K_{skew} = \frac{sin(\theta_{elec}/2)}{\theta_{elec}/2}
$$

$\theta_{elec}$ refer to the degree in the current phase cycle of the AC current. To convert this to mechanical radians, simply divide it by the number of **pole pairs,** which is the number of PM magnets / 2.

### iii. Distribution Factor

For a distributed winding (q>=1), The distribution factor $K_d$ is dependent on the electrical angle between two slots $\gamma$, slots per pole per phase $q$.

$$
q = \frac{N_{slots}}{3*N_{poles}}
$$

Since electrical angle tracks back-EMF waveform, which spans a full N-S cycle of PM poles, the number of pole pairs $N_{poles}/2$ is used for $\gamma$:

$$
\gamma = 2\pi * \frac{N_{poles}}{2*N_{slots}}
$$

$$
K_d = \frac{sin(\frac{\gamma * q}{2})}{\frac{\gamma*q}{2}}
$$

Thus, for a concentrated winding configuration with no skew, the winding factor $K_w$ is equal to the distribution factor $K_d$.

For a 36N42P example,

$$
K_w \approx 0.9549.
$$





