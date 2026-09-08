## Introduction
First, this document will describe the construction of three-phase motors. Two-phase or one-phase motors will not be addressed here, as they are far less common in BLDCs.

It is important to consider and understand the difference between different winding parameters, such as:

1. Distributed vs. concentrated windings,
2. Single and double-layer,
3. Series vs. parallel windings,
4. Star (Wye) vs. Delta termination,
5. Winding factor (kw),
6. PM rotor magnet construction (geometry, air gap, skewing)

# Distributed vs. Concentrated Windings and its Implications
Simply put, a concentrated winding is one where each coil wraps a single tooth, while a coil in a distributed winding can span multiple teeth.

Generally, concentrated windings are found in BLDC motors, while distributed windings constitute that of PMSM motors. In this section, a brief description and characterization of performance distinctions will be provided. The primary distinction being _back-EMF._

<img src="https://github.com/user-attachments/assets/05997369-10e8-4dc6-8b0e-69efdcf1bcb4" width="45%"> 
<img src="https://github.com/user-attachments/assets/e3f81259-892a-4888-b390-39a313f7fdd4" width="47%"> 

Sources:

GuangRi Winding https://grwinding.com/concentrated-winding-and-distributed-winding/

E.A. Lomonova, "In‐wheel PM motor: compromise between high power density and extended speed capability" (2011). https://www.researchgate.net/figure/Armature-winding-types-for-an-interior-rotor-machine-a-distributed-winding-b_fig2_228883617

## Concentrated Windings (BLDC)
Concentrated windings are only possible when the slots-per-pole-per-phase (denoted as _q_) works out to less than 1.

For example, for a 36-slot, 42-pole, 3-phase motor, _q =_ 36/42/3 = 0.286.

This repository assumes concentrated windings, since they're easier to wind by hand and manufacture, and are more commonly found in BLDC motors. 

A drawback to consider for concentrated windings is its trapezoidal back-EMF profile, which shows up as more cogging torque and torque ripple.

## Distributed Windings (PMSM)
Distributed coils are more commonly found in induction and EV traction motors, with _q > 1._

For the purpose of this repository, distributed windings are not addressed, as they are harder to manufacture. However, a characteristic of distributed windings are a smoother, sinusoidal back-EMF profile, compared to that of concentrated windings, due to a more uniform flux pattern caused by the overlapping of wires.

## Theoretical and Measured BEMF of Concentrated and Distributed Windings

<img src="https://github.com/user-attachments/assets/2ded2f9e-3ea3-4a65-8408-ef4674a16f10" width="45%"> 
<img src="https://github.com/user-attachments/assets/aa38fcfd-c62f-4335-bc3a-2bda1d1b3fba" width="47%"> 

Source: Jang Seok Myeong (2012) "Comparative Analysis on Magnetic Field and Inductances of Slotless Permanent Magnet Machine with Two Types of Winding based on Analytical Method." https://www.researchgate.net/figure/Color-online-Comparison-of-back-EMF-in-distributed-and-concentrated-types-of-winding_fig1_264032495

However, with careful construction of the stator and rotor magnets in a BLDC, a near-sine back-EMF profile can be achieved.













