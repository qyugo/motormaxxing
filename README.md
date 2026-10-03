---
title: Overview
nav_order: 1
permalink: /
---


# Motormaxxing
Attempt at full-stack upskilling for brushless motors. To be updated periodically.

<video src="https://github.com/user-attachments/assets/fb8ee87a-f4b3-4df1-b4ab-6bcff8b6aa19" autoplay loop muted playsinline style="width: 30%;"></video>

<video src="https://github.com/user-attachments/assets/bda9567a-19c8-4262-996d-6315954c4c0d" autoplay loop muted playsinline style="width: 35%;"></video>

<video src="https://github.com/user-attachments/assets/21d9bb4c-289d-42fb-8375-9db78879503d" autoplay loop muted playsinline style="width: 35%;"></video>

This repository contains the following sub-projects:

## 1. Python Winding Calculator
An interactive Python tool and UI built using PyQt5 for hand-winding stators and adjusting variables to see its effect on performance.

| Inputs         | Outputs       | Features                 |
|----------------|--------------|-----------------------|
| Stator/rotor/slot/airgap/magnet geometry    | Graphical: Estimated KV per turn count, current density vs. strands per coil        |   Empirical or analytical correction factors    |
| Winding configurations, input current  | Peak torque, motor constants  | Live adjustment of results     |
| Material characteristics, operating temperature            | Strand length needed per coil, slot fill    | |
|             | Phase resistance   | |



Inputs: 
- Stator/rotor/slot/airgap/magnet geometry
- Winding configurations, input current
- Material characteristics, operating temperature
  
Outputs:
- Graphical: Estimated KV per turn count, current density vs. strands per coil
- Peak torque, motor constants
- Strand length needed per coil
- Phase resistance

Features:
- Empirical or analytical correction factors
- Live adjustment of results

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="75%"> 


## 2. Example Crafting of 36N42P BLDC Outrunner Motor

An application of the winding and construction calculators for a hand-wound 8110 stator and FDM printed stator, wired for 36N42P in star configuration for a high-torque robotic actuator.


<img width="1280" height="720" alt="IMG_3859 Large" src="https://github.com/user-attachments/assets/a01c3e12-953a-452b-a3e7-c14a6115308f" />

<div style="display: flex; gap: 1rem;">
  <img src="https://github.com/user-attachments/assets/a7ce6ace-9ecd-4dec-a5ff-cda109243b8c" style="width: 30%;">
  <img src="https://github.com/user-attachments/assets/723905bd-2630-4893-95b4-50d02e611639" style="width: 20%;">
  <img src="https://github.com/user-attachments/assets/f86a411e-1f80-47ba-9de4-a4d2a9937460" style="width: 25%;">
</div>

<img src="https://github.com/user-attachments/assets/e3f66143-3f8e-49ec-9755-bfc6c50cd72c" width="52%"> 




## 3. Motor Characterization (In Progress)

For testing and validating motor characteristics.

Dynamometer build, measuring KV, finding the empirical K and Ke/Kt constants and comparing with the analytical tool.

<img width="1280" height="960" alt="dyno361kb" src="https://github.com/user-attachments/assets/8a747d03-b4ab-476c-b65f-c94a0c34b9dc" />

