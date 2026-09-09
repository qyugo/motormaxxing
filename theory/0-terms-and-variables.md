# Introduction to BLDC Motors

Taken from the background section of my own BLDC motor driver documentation.

## 1. Brushed vs Brushless DC Motors

DC motors are typically composed of two concentric magnetic-field generating components: a circular array of permanent magnets for a fixed magnetic field, and a circular series of wound copper coils, which can act as variable magnets depending on the electrical current passed through them.

Brushless motors are distinct from brushed DC motors in their commutation method, or how current is switched in the copper motor windings to generate a moving magnetic field against the permanent magnets. 

In brushed motors, the wound coils are typically found in the rotor (the rotating component), where a direct-contact brush armature supplies a switching current to induce rotation against a permanent magnet stator, which remains stationary. In brushless motors, the wound coils are the unmoving stator, which requires an external circuit board to induce a spinning magnetic field, which generates resultant movement in the permanent-magnet rotor.

Brushed motors tend to experience higher noise and wear due to the direct contact of the brush armature against the spinning rotor, though it remains relatively low cost and uncomplex in its hardware requirements. However, brushless motors thus experience longer lifespans and efficiencies, and lower noise from lack of direct-contact parts, but requires a more complex control scheme for the wound-coil stator from an electronic speed controller (ESC).

<img width="900" height="400" alt="brushed-vs-bldc" src="https://github.com/user-attachments/assets/edcf24f6-8f8a-4621-afab-b9fdcc575ab1" />

<hr width="30%">
<small>Image Source: https://www.dc-pump.com/brushed-vs-brushless-dc-pump-differences/</small>

## 2. Inrunner vs Outrunner Motors
The characteristics of a BLDC motor can be adjusted according to its construction to support different applications of the motor. The orientation of the stator and rotor can impact the performance of a BLDC motor. As the permanent magnets always act as the spinning rotor in a BLDC, it can exhibit higher torques when set as the outer shell of the motor, and higher speed in inrunner motors.

<img width="500" height="356" alt="in-out-runner" src="https://github.com/user-attachments/assets/b9857ae5-e30f-4db3-bcd4-7a00cdb9fccb" />

<hr width="30%">
Source: https://ican-motor.com/bldc-motor-specifications-about-motor-selection/
