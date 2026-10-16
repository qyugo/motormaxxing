---
title: FEMM Simulations
nav_order: 6
has_children: true
---

# Finite Element Method Magnetics (FEMM) 2D Simulation for N42, 0.75mm airgap (V3) Motor

<img src="https://github.com/user-attachments/assets/693b72cf-29ac-40c4-859d-2ada0fe9b138" width="50%"/>


In conjunction with my analytical model, I wanted to have a numerical model as well. David Meeker's FEMM allows for a 2D simulation for calculating airgap flux density, torque (and cogging torque by a spinning Lua script), flux linkage, and back-EMF. 

Both analytical model (my Python UI), the FEMM simulation, and experimental characterization using my dynos will support the creation of these motors, and be improved periodically.

Limitations of the FEMM model:

There will inevitably be some error from FEMM since it is in 2D, so end effects and axial leakage, so errors will be more apparent for shorter stack lengths (thinner motors).

OnShape Model:

<img src="https://github.com/user-attachments/assets/dfdcbe1a-02fb-480e-bec1-cce122ddb903" width="45%"/>
<img src="https://github.com/user-attachments/assets/ca3f652f-e714-4417-97ea-39f4640afe6d" width="45%"/>

Material: M19 Stator Laminations, Steel 1018 (hot rolled), 26AWG Copper, N42 Magnets

I generated the rest of the rotor and magnets using Python, so further adjustments to magnet strength and dimensions, airgap, and rotor back-iron thickness can be quickly tested, while the stator remains the same.

Correct winding directions of A,B, and C phases wound using AabBCcaABbcC [etc...] are programmed into the python script.

Magnetic Meshing

<img src="https://github.com/user-attachments/assets/60acae5b-52ca-4bb1-98ee-51593dd89af5" width="45%"/>
<img src="https://github.com/user-attachments/assets/681892f5-b385-435b-b1f5-0a3d65c07777" width="45%"/>


Static analysis and airgap flux density B (42 sign changes):

<img src="https://github.com/user-attachments/assets/57a2e2cc-226f-4504-80ad-a9e601125107" width="36%"/>

<img src="https://github.com/user-attachments/assets/7799095b-1bbd-4ca5-b73a-16fccf7ad9b8" width="60%"/>



