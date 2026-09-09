# Mechanical Construction of BLDC Motors
In this section, an introduction to BLDC motors in the concept of electric motors is discussed, as well as mechanical characteristics

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

## Permanent Magnet Rotor Structure and Air Gap (Rotormaxxing)
The structure of the PM rotor can influence motor characteristics such as torque output, flux linkage, and _cogging torque._

###Rotor Shell and Magnets
Generally, a circular array of rectangular neodymium-iron-boron (NdFeB) magnets are used in BLDC rotors. Neodymium magnets can possess a strength grade from N35 to N52. The magnet grade as well as its thickness can offer parameters for adjusting PM strength.

The material of the rotor shell to house the magnets is also considered. In general, the only 'useful' magnetic flux from the PMs is that directed inwards towards the stator, so generally a ferromagnetic material is selected to maximize efficiency and torque.

The following image is from a video by Aaed Musa on YouTube, comparing the magnetic fields of that of a 3D-printed rotor shell as well as a steel shell.

<img src="https://github.com/user-attachments/assets/708217f4-bc75-4223-af83-3f238113f0af" width="45%"> 

As observed, a steel shell is effective at directing the PM flux inwards. Many DC motors also implement a _flux ring_ for this exact purpose:

<img src="https://github.com/user-attachments/assets/5b4dc9a5-03d7-4704-b6b5-cb621d23c948" width="45%"> 


**Flux Linkage**: 
The concept of flux linkage is commonly used to describe the interactions of the generated magnetic fields through the inductor-like windings on each stator tooth.

According to Faraday's Law, any change in flux linkage over time generates a _back-EMF._


