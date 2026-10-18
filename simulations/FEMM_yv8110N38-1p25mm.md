---
title: V2 FEA Simulation
parent: FEMM Simulations
nav_order: 2
---

# FEMM for V2 PETG Motor

Version: YV8110 V2, N38 NdFeB magnets, 1.25mm airgap, PETG backiron. 

First, the rotor was redrawn in FEMM to change the backiron material to air (as the magnetic permeability for PETG is essentially the same).

The magnets are also slightly smaller, with a 2.5mm thickness compared to the N42 magnets, and a narrower width of 4.5mm. The new rotor with alternating N38 magnets was drawn using Python around the stator, which remains the same.

<img width="942" height="579" alt="Screenshot 2026-10-17 at 2 34 54 PM" src="https://github.com/user-attachments/assets/b91afcdf-33ba-4bf5-af5d-0f82fbdec149" />

Visible in the FEMM solver that the lack of a back-iron causes the motor flux to go outwards. 

<img width="710" height="629" alt="Screenshot 2026-10-17 at 3 00 19 PM" src="https://github.com/user-attachments/assets/cfb3d404-6426-4691-baf3-8e36a5af003c" />
<img width="808" height="766" alt="Screenshot 2026-10-17 at 2 59 52 PM" src="https://github.com/user-attachments/assets/02f0a659-d694-46c0-8d86-55c29f5ad8ad" />

<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/d0a7d827-e10e-453b-9b0c-767182afaad2" />
<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/910e127c-c99f-424f-86c5-b861717f151c" />
<img width="1500" height="690" alt="image" src="https://github.com/user-attachments/assets/07556617-c174-4cc9-9ca9-e824f00f1a25" />


| Quantity | FEMM, N38 / PETG / 1.25 mm gap |
|---|---|
| KV, star (rpm/V) | 151.1 |
| Kt (N·m/A, peak) | 0.0547 |
| Peak torque @ 8 A (N·m) | 0.438 |
| Torque @ 5 A / 10 A (N·m) | 0.274 / 0.547 |
| Turns for 100 KV | 12.1 |
| Flux linkage λ, phase peak (mWb) | 1.738 |
| Back-EMF constant, phase (V·s/rad) | 0.0365 |
| Back-EMF at 1000 rpm, phase peak (V) | 3.82 |
| Current density @ 8 A, 4×26 AWG (A/mm²) | 15.5 |
| Cogging, peak-to-peak (mN·m) | 1.2 ) |
| Torque ripple, peak-to-peak | 0.8% at 5 A, 0.3% at 10 A |
| 10 A / 5 A torque ratio | 1.999 |
