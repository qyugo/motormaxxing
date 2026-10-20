---
title: CNC DFM Analysis for V3
parent: 2. Motor Builds
nav_order: 3
has_children: true
---

# DFM for a Metal Motor (In progress)

Clearly, a metal motor is significantly advantageous to a plastic one, for flux return as well as mechanical stability and heatsinking.

Further, it is evident that the current rotors up to V2 are not very CNC-able.


In this section, the working V2 design is modified to optimize for a metal model, via lathe + CNC milling, for cost and manufacturability.

First, I used DFM studio to obtain a rating and estimated domestic cost using the current V2.

<img width="1400" height="631" alt="Screenshot 2026-10-12 at 12 55 34 PM" src="https://github.com/user-attachments/assets/9f06c5d3-e10e-4587-a02e-c9f0a1fb6cc4" />

<img width="384" height="439" alt="Screenshot 2026-10-14 at 3 58 35 PM" src="https://github.com/user-attachments/assets/3c2f7a49-0cf1-404c-a55f-5b59a112b1d3" />




Evidently, there are issues with this model made for FDM printing that a CNC machine would either be unable to do, or be significantly more expensive.

As CNC machines are unable to make sharp corners, filleting and dogbones are placed to make the part manufacturable.

This is designed with a 1/8" (3.175mm) cutter in mind, as most small-end shops would contain it, allowing for a cheaper build.

<img width="453" height="329" alt="Screenshot 2026-10-12 at 1 09 37 PM" src="https://github.com/user-attachments/assets/81d99d80-9008-4ea7-900a-586cd9a3b65c" />

Iteration 2: Cost estimate: 

<img width="1914" height="956" alt="Screenshot 2026-10-14 at 1 18 45 PM" src="https://github.com/user-attachments/assets/e180111b-41b4-4221-96c0-f5a460ba2932" />

Iteration 3
<img width="594" height="482" alt="Screenshot 2026-10-14 at 4 18 14 PM" src="https://github.com/user-attachments/assets/079cda4c-3f08-4170-a873-d41d3aff8ddb" />
<img width="588" height="463" alt="Screenshot 2026-10-14 at 4 18 49 PM" src="https://github.com/user-attachments/assets/17ec491d-0085-49ae-8c3e-e3aba630537a" />

Iteration 4: $1113
<img width="1432" height="605" alt="Screenshot 2026-10-15 at 12 43 38 PM" src="https://github.com/user-attachments/assets/9ecff2c6-34f7-4ceb-8053-d2a9f8ba6a7e" />

At this point, I figured CNC milling this thing may be not the most economical, but perhaps scalable through automation if I wanted to make a bunch, with a simpler design.

I decided to explore the possibility of self-manufacture, with just a lathe and some aluminum and steel 1018 extrusions in the [next section](../manufacturemaxxing/selfmanufacture.md).

Iteration 5: $223 domestic, ~73.62 international

<img width="1350" height="872" alt="Screenshot 2026-10-20 at 4 28 57 PM" src="https://github.com/user-attachments/assets/18ea4a03-b0bd-4921-84e4-456ffe806399" />



