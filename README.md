---
title: Overview
nav_order: 1
permalink: /
---


# Motormaxxing
Attempt at full-stack upskilling for brushless motors. To be updated periodically.

This repository contains the following three sub-projects:

<div class="video-row">
  <figure>
    <video src="https://github.com/user-attachments/assets/fb8ee87a-f4b3-4df1-b4ab-6bcff8b6aa19" autoplay loop muted playsinline  style="width: 100%;"></video>
    <figcaption>Analytical Motor Model & UI in Python, checked against numerical FEMM simulations (<5% error on Kv, Kt, flux linkage, and peak torque for V1 and V2).</figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/bda9567a-19c8-4262-996d-6315954c4c0d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>BLDC Motor Builds (hand wound/FDM prototypes) + Metal DFM analysis + low-cost manufacturing plan </figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/21d9bb4c-289d-42fb-8375-9db78879503d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>Testing Rigs/Dynamometer Builds + Motor Characterization results and validation of analytical/numerical models.</figcaption>
  </figure>
</div>

## 1. Analytical Motor Model + Python Calculator (and FEMM sim)

An interactive Python tool and UI built using PyQt5 for hand-winding stators and adjusting variables to see its effect on performance, with correction factors applied to account for slot leakage/flux loss. Full derivations, code, and process available.

Additionally, I ran an FEA simulation using FEMM by David Meeker to obtain an error between a numerical software and my analytical model. The results were quite close, with KV, Kt, peak torque, and flux linkage being **accurate to within 5%** for the metal model.

| Inputs         | Outputs       | Features                 |
|----------------|--------------|-----------------------|
| - Stator/rotor/slot/airgap/magnet geometry <br> - Winding configurations, input current <br> - Material characteristics, operating temperature   | - Graphical outputs: Estimated KV per turn count, current density vs. strands per coil <br> Peak torque, motor constants <br> - Strand length needed per coil <br> - Phase resistance     |   - Empirical or analytical correction factors <br> - Live adjustments of results    |

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="50%"> 
<img src="https://github.com/user-attachments/assets/bd5209dd-4083-486c-b190-2b37665033e1" width = "45%"/>

Left: My Python calculator. Right: FEMM Simulation.


Click [here](analytical-calculator/README.md) for Analytical Calculator subproject documentation.

## 2. Brushless DC Motor Builds

An application of the winding and construction calculators for a real prototype build.

A few variants around a 81mm diameter, 10mm stack length silicon steel laminated stator core are built. It features a currently FDM printed rotor and housing, wired for 36N42P in star configuration for a high-torque robotic actuator.

<img src="https://github.com/user-attachments/assets/427e2a84-3f20-4565-b44d-6088a82d4945" width="87%"/>

Currently, a few plastic motors have been built and tested. I am working on a low-cost manufacturing protocol for some metal motors. Here are some adjusted designs suited for cheap machining out of aluminum and steel:

<img src="https://github.com/user-attachments/assets/39d741a6-8d30-40f8-89d6-67e81b22d2ef" width="45%" />
<img src="https://github.com/user-attachments/assets/d805ee43-378d-4688-92ee-d504cf9315d2" width="45%" />

Currently working on an Aluminum 6061 + 1020 Steel version for better testing and heat performance:

<video src="https://github.com/user-attachments/assets/67364a27-335a-46b9-86a4-3b94f681b875" autoplay loop muted playsinline style="width: 100%;"></video>

Click [here](V2-Build/README.md) for Motor Builds subproject documentation.

## 3. Motor Testing Hardware

Building two dynamometers to test characteristics of motors. One variant involves an old Delco CS-144 alternator being repurposed to a passive absorption dynamometer, and the other is a BLDC-BLDC coupling.

<img src="https://github.com/user-attachments/assets/8a747d03-b4ab-476c-b65f-c94a0c34b9dc" width = "40%"/>
<img src="https://github.com/user-attachments/assets/ce6d4c23-6e41-4a6d-b688-b08809804f53" width = "46%"/>

Left: YVDyno-CS144. Right: YVDyno-8308.

Click [here](testing-and-validation/dynosetup.md) for Testing Hardware subproject documentation.

