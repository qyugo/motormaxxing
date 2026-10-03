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
    <figcaption>1. Analytical Motor Model & UI.</figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/bda9567a-19c8-4262-996d-6315954c4c0d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>Fig. 2: BLDC Motor Builds.</figcaption>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/21d9bb4c-289d-42fb-8375-9db78879503d" autoplay loop muted playsinline style="width: 100%;"></video>
    <figcaption>Fig. 3: Dynamometer Build & test.</figcaption>
  </figure>
</div>

## 1. Analytical Motor Model + Python Calculator
An interactive Python tool and UI built using PyQt5 for hand-winding stators and adjusting variables to see its effect on performance.

| Inputs         | Outputs       | Features                 |
|----------------|--------------|-----------------------|
| - Stator/rotor/slot/airgap/magnet geometry <br> - Winding configurations, input current <br> - Material characteristics, operating temperature   | - Graphical outputs: Estimated KV per turn count, current density vs. strands per coil <br> Peak torque, motor constants <br> - Strand length needed per coil <br> - Phase resistance     |   - Empirical or analytical correction factors <br> - Live adjustments of results    |

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="75%"> 


## 2. Brushless DC Motor Builds

An application of the winding and construction calculators for a real prototype build.

Current builds are for a 8110 stator and FDM printed stator, wired for 36N42P in star configuration for a high-torque robotic actuator.

<img src="https://github.com/user-attachments/assets/a01c3e12-953a-452b-a3e7-c14a6115308f" width = "80%"/>


## 3. Motor Testing Hardware

Building a dynamometer to test characteristics of motors.

<img src="https://github.com/user-attachments/assets/8a747d03-b4ab-476c-b65f-c94a0c34b9dc" width = "80%"/>

