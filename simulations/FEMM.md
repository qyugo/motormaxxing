---
title: V3 FEA Simulation (Metal)
parent: FEMM Simulations
nav_order: 1
---

# Finite Element Method Magnetics (FEMM) Simulation for N42, 0.75mm airgap (V3) Motor


In conjunction with my analytical model, I wanted to have a numerical model as well. David Meeker's FEMM program allows for a 2D simulation for calculating airgap flux density, torque (and cogging torque by a spinning Lua script), flux linkage, and back-EMF. 

Both analytical model (my Python UI), the FEMM simulation, and experimental characterization using my dynos will support the creation of these motors, and be improved periodically.

Limitations of the FEMM model:

There will inevitably be some error from FEMM since it is in 2D, so end effects and axial leakage, so errors will be more apparent for shorter stack lengths (thinner motors).

## 1. Static Mesh and Analysis of 2D Cross Section

OnShape Model:

<img src="https://github.com/user-attachments/assets/dfdcbe1a-02fb-480e-bec1-cce122ddb903" width="45%"/>
<img src="https://github.com/user-attachments/assets/ca3f652f-e714-4417-97ea-39f4640afe6d" width="45%"/>

Material: M19 Stator Laminations, Steel 1018 (hot rolled), 26AWG Copper, N42 Magnets

I generated the rest of the rotor and magnets using Python, so further adjustments to magnet strength and dimensions, airgap, and rotor back-iron thickness can be quickly tested, while the stator remains the same.

Correct winding directions of A,B, and C phases wound using AabBCcaABbcC [etc...] are programmed into the python script and "wrapped" around each stator tooth. A divider was placed in the midline of each slot to divide teeth windings.

Meshing for magnetic analysis:

<img src="https://github.com/user-attachments/assets/60acae5b-52ca-4bb1-98ee-51593dd89af5" width="45%"/>
<img src="https://github.com/user-attachments/assets/681892f5-b385-435b-b1f5-0a3d65c07777" width="45%"/>


Results of static analysis from mesh. To confirm that the permanent magnets were placed correctly in an alternating N-S fashion, I plotted airgap flux density B, verifying 42 sign changes for 42 poles.

<img src="https://github.com/user-attachments/assets/57a2e2cc-226f-4504-80ad-a9e601125107" width="34%"/>
<img src="https://github.com/user-attachments/assets/7799095b-1bbd-4ca5-b73a-16fccf7ad9b8" width="58%"/>


## 2. Dynamic Analysis (Sweep)

Next, a dynamic analysis across a full sweep of the rotor was performed using Python. For this run, I set the continuous and peak current to 5A/10A, for cogging torque, unloaded flux linkage, and loaded torque.

Initially, I was getting very small flux values, and realized I had the problem depth set to 1mm. With a 10mm stack length, I increased the depth as such, and values made much more sense.

Cogging Torque:

<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/ae49832b-148d-402b-b4ba-f715aa975d75" />

Flux Linkage (No load):

<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/da0ce83c-ec4a-44c9-8777-5dcf4b63f782" />

Loaded Torque:

<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/7023efde-69bd-43d8-870e-7015a2c8d530" />

## 3. Results and Comparison with Analytical Model

With these results, I inputted the same parameters into my Python calculator and obtained the error in results between the numerical FEMM and my analytical UI.

<img width="671" height="242" alt="Screenshot 2026-10-16 at 5 04 50 PM" src="https://github.com/user-attachments/assets/7faf0c1f-d677-4b49-ba42-f0d04702fc74" />

Using the same airgap, back-iron thickness, motor configurations (36N42P, star, stator diameter and stack length, etc):

| Quantity | Analytical | FEMM | Accuracy (FEMM vs Analytical) |
|---|---|---|---|
| KV (rpm/V) | 78.2 | 81.6 | +4.3% |
| Kt (N·m/A) | 0.1057 | 0.1012 | −4.3% |
| Peak torque @ 8 A (N·m) | 0.8456 | 0.808 (interpolated) | −4.4% |
| Turns for 100 KV | 6.3 | 6.5 | +3.2% |
| Bg (T) | 0.613 | 0.712 | +16% |
| $\alpha_i$ | 0.762 | 0.722 | −5% |
| Current density @ 8 A (A/mm²) | 15.53 | 15.5 | -0.193% |
| Flux linkage $\lambda$, peak (mWb) | 3.355 | 3.218 | −4.1% |

Overall, the analytical model, with corrections to slot leakage applied, was quite close to the numerical model.
