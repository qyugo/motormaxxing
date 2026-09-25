# Motormaxxing
Attempt at full-stack upskilling for brushless motors. To be updated periodically.

Self-learning and practice while reading _Brushless PM Motor Design_ by Duane Hanselman (1994).

This repository contains the following sub-projects:

## 1. Python Winding Calculator
An interactive Python tool and UI built using PyQt5 for hand-winding your stators and adjusting variables to see its effect on performance.
Inputs: 
- Stator/rotor/magnet geometry
- Winding characteristics
- Material characteristics, operating temperature
  
Outputs:
- Graphical: Estimated KV per turn count, current density vs. strands per coil
- Peak torque
- Strand length needed per coil
- Phase resistance

<img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="75%"> 


## 2. Example Crafting of 36N42P BLDC Outrunner Motor

An application of the winding and construction calculators for a hand-wound 8110 stator and FDM printed stator, wired for 36N42P in star configuration for a high-torque robotic actuator.

<img src="https://github.com/user-attachments/assets/a7ce6ace-9ecd-4dec-a5ff-cda109243b8c" width="36%"> 

<img src="https://github.com/user-attachments/assets/723905bd-2630-4893-95b4-50d02e611639" width="26%"> 

<img src="https://github.com/user-attachments/assets/f86a411e-1f80-47ba-9de4-a4d2a9937460" width="29%"> 

<img src="https://github.com/user-attachments/assets/e3f66143-3f8e-49ec-9755-bfc6c50cd72c" width="52%"> 

<img src="https://github.com/user-attachments/assets/575e070e-9562-4655-95c3-17ae9103bcbb" width="43%"> 



## 3. Motor Characterization (In Progress)

For testing and validating motor characteristics.

Dynamometer setup, measuring KV, finding the empirical K and Ke/Kt constants and comparing with the analytical tool.
