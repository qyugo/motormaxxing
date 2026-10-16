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
    <figcaption>Analytical Motor Model & UI, within 5% accuracy to FEMM simulations.</figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/bda9567a-19c8-4262-996d-6315954c4c0d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>BLDC Motor Builds (hand wound/FDM prototypes) + Metal DFM analysis </figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/21d9bb4c-289d-42fb-8375-9db78879503d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>Testing Rigs/Dynamometer Builds + Motor Characterization results.</figcaption>
  </figure>
</div>

## 1. Analytical Motor Model + Python Calculator

An interactive Python tool and UI built using PyQt5 for hand-winding stators and adjusting variables to see its effect on performance, with correction factors applied to account for slot leakage/flux loss. Full derivations, code, and process available.

Additionally, I ran an FEA simulation using FEMM by David Meeker to obtain an error between a numerical software and my analytical model. The results were quite close, with KV, Kt, peak torque, and flux linkage being **accurate to within 5%.**

| Inputs         | Outputs       | Features                 |
|----------------|--------------|-----------------------|
| - Stator/rotor/slot/airgap/magnet geometry <br> - Winding configurations, input current <br> - Material characteristics, operating temperature   | - Graphical outputs: Estimated KV per turn count, current density vs. strands per coil <br> Peak torque, motor constants <br> - Strand length needed per coil <br> - Phase resistance     |   - Empirical or analytical correction factors <br> - Live adjustments of results    |

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="75%"> 

Click [here](analytical-calculator/README.md) for subproject documentation.

## 2. Brushless DC Motor Builds

An application of the winding and construction calculators for a real prototype build.

A few variants around a 81mm diameter, 10mm stack length silicon steel laminated stator core are built. It features a currently FDM printed rotor and housing, wired for 36N42P in star configuration for a high-torque robotic actuator.

<img width="5712" height="4284" alt="IMG_3794" src="https://github.com/user-attachments/assets/427e2a84-3f20-4565-b44d-6088a82d4945" />


Click [here](V2-Build/README.md) for subproject documentation.

## 3. Motor Testing Hardware

Building two dynamometers to test characteristics of motors. One variant involves an old Delco CS-144 alternator being repurposed to a passive absorption dynamometer, and the other is a BLDC-BLDC coupling.

<img src="https://github.com/user-attachments/assets/8a747d03-b4ab-476c-b65f-c94a0c34b9dc" width = "80%"/>

<img width="1119" height="724" alt="photo_2026-10-13 20 41 12" src="https://github.com/user-attachments/assets/ce6d4c23-6e41-4a6d-b688-b08809804f53" />


Click [here](testing-and-validation/dynosetup.md) for subproject documentation.

