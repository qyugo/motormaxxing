---
title: BLDC Coupling Rig
parent: 3. Testing Hardware
nav_order: 1
---

# Simple Motor Tester

A simple rig was constructed to measure the motors I've crafted in this repo. A further installment of a dynamometer was created using a car alternator.

Since I had two BLDC motors (Eaglepower LA8308) with spec sheets, I would drive one motor coupled to another motor which generates an output voltage through three phases.

Then, a simple load resistor was placed on the phase outputs to measure power.

There are some drawbacks to a 3D printed setup, such as the warping of the rig itself. However, I designed a housing case with some long screws to allow the coupled motors to act somewhat independently from the surface  they're on, with a supporting bracket that can rest on a tabletop and be clampable.

Regardless, any small amount of misalignment, which is inevitable when humans are involved, may cause damage to the motors or the shafts. Thus, I built a few sets of jaw couplings out of PETG with 3D-printed TPU spider inserts to allow for some flexibility while maintaining solid force transmission (and without backlash).

3D Printed coupling with TPU spider
<img width="838" height="591" alt="image" src="https://github.com/user-attachments/assets/48c2a41c-f05c-48eb-ab0b-eecd31b74835" />

<img width="802" height="459" alt="image" src="https://github.com/user-attachments/assets/4f614efc-b791-4096-aa8f-b247c576eb3d" />

KV Test of Known Motor: LA8308

This motor is listed to have 90KV. First, voltage of phases A and B were measured at speeds of 1, 2, 3, 5, 7, and 10 rev/s without any load. Additionally, Iq of the powered motor was measured through the driver for input current.

Oscilloscope:

<img src="https://github.com/user-attachments/assets/58d940f7-f3fd-441b-9a1b-c46b9b69018a" width="15%" />
<img src="https://github.com/user-attachments/assets/07b6a532-125c-4a19-8499-8d244c17aba8" width="15%"/>
<img src="https://github.com/user-attachments/assets/53734451-1da8-4d9b-89c3-fe7ed7f69cca" width="15%"/>
<img src="https://github.com/user-attachments/assets/3cab0c88-84d7-42e5-84de-e6befbf8be6c" width="15%"/>
<img src="https://github.com/user-attachments/assets/04a8503e-1a79-4cc1-a525-4e6b24a21dc0" width="15%"/>
<img src="https://github.com/user-attachments/assets/eeb00423-70a7-481f-9e9a-ad2c4d6b59aa" width="15%"/>

Iq:

<img width="772" height="421" alt="image" src="https://github.com/user-attachments/assets/918a1037-c419-4c82-b5d6-1b7fef7c4c32" />


| rev/s | Vpp A-C (V) | Vpp B-C (V) | avg Vpp (V) | Iq mean (A) |
|---|---|---|---|---|
| 1 | 1.30 | 1.47 | 1.39 | -0.334 |
| 2 | 2.52 | 2.39 | 2.46 | -0.330 |
| 3 | 3.68 | 3.58 | 3.63 | -0.342 |
| 5 | 6.13 | 6.17 | 6.15 | -0.336 |
| 7 | 8.43 | 8.28 | 8.36 | -0.352 |
| 10 | 11.93 | 13.16 | 12.55 | -0.336 |

