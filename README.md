# motormaxxing
References and Examples for Actuator Crafting. 
Self-learning and practice of applying the principles described in _Brushless PM Motor Design_ by Duane Hanselman (1994).
This repository contains the following sub-projects:

## 1. Python Winding Calculator
An interactive Python tool for hand-winding your stators and adjusting variables to see its effect on performance.
Inputs: 
- Stator/rotor/magnet geometry
- Winding characteristics
- Material characteristics, operating temperature
  
Outputs:
- Estimated KV and current density
- Peak torque
- Strand length needed per coil
- Phase resistance

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="75%"> 


**2. Example Crafting of 36N42P BLDC Outrunner Motor**

An application of the winding and construction calculators for a 8110 stator, wired for 36N42P in star configuration for a high-torque robotic actuator.

**3. Motor Characterization (In Progress)**

For testing and validating motor characteristics.

Dynamometer setup, measuring KV, finding the empirical K and Ke/Kt constants and comparing with the analytical tool.
