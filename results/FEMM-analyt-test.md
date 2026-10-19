---
title: Results (Analytical vs. Numerical vs. Experimental)
nav_order: 7
has_children: true
---

# FEMM vs. Analytical vs. Experimental Results (V2 and V3)

In this section, a small summary regarding the results of comparing FEMM simulation, my analytical model, and actual experimental results using my custom simple dynamometer, to see how the results fare.

<div class="video-row">
  <figure>
    <img src="https://github.com/user-attachments/assets/140b6cac-92cd-4652-8e88-956db5992207" width="100%"> 
  </figure>
  <figure>
    <img src="https://github.com/user-attachments/assets/870c4d00-eefb-4721-9796-e27da1f11586" width="100%"/>
  </figure>
  <figure>
    <video src="https://github.com/user-attachments/assets/4f748ef8-2a20-4e77-80fb-5e194c695dd6" autoplay loop muted playsinline style="width: 100%;"></video>
  </figure>
</div>

## V3 (Metal, N42, 0.75mm Airgap)

### Analytical Results

<img width="671" height="242" alt="Screenshot 2026-10-16 at 5 04 50 PM" src="https://github.com/user-attachments/assets/7faf0c1f-d677-4b49-ba42-f0d04702fc74" />

### FEMM Results

<img src="https://github.com/user-attachments/assets/ae49832b-148d-402b-b4ba-f715aa975d75" width="30%" />
<img src="https://github.com/user-attachments/assets/da0ce83c-ec4a-44c9-8777-5dcf4b63f782" width="30%"/>
<img src="https://github.com/user-attachments/assets/7023efde-69bd-43d8-870e-7015a2c8d530" width="30%"/>

### Analytical vs. Numerical

Analytical and FEMM models were within +/- 5% accuracy for Kv, Kt, Ke, flux linkage, current density, and peak torque. However, Bg was the only one slightly off.

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

### Experimental

Not available yet, as I have yet to craft a metal motor (as of 10/18/26).

## V2 (PETG, N38, 1.25mm Airgap)

### Analytical Results:

<img width="674" height="243" alt="Screenshot 2026-10-18 at 12 05 53 AM" src="https://github.com/user-attachments/assets/72771f7f-b9b9-4a65-bdd2-d4320500d8b9" />


### FEMM Results:

<img src="https://github.com/user-attachments/assets/d0a7d827-e10e-453b-9b0c-767182afaad2" width="30%"/>
<img src="https://github.com/user-attachments/assets/910e127c-c99f-424f-86c5-b861717f151c" width="30%"/>
<img src="https://github.com/user-attachments/assets/07556617-c174-4cc9-9ca9-e824f00f1a25" width="30%"/>

### Analytical vs. Numerical

| Quantity | Analytical | FEMM | Accuracy (FEMM vs Analytical) |
|---|---|---|---|
| KV (rpm/V) | 150.5 | 151.1 | +0.4% |
| Kt (N·m/A) | 0.0550 | 0.0547 | −0.5% |
| Peak torque @ 8 A (N·m) | 0.4397 | 0.438 (interpolated) | −0.4% |
| Turns for 100 KV | 12.0 | 12.1 | +0.8% |
| Bg (T) | 0.317 | 0.339 | +6.9% |
| $\alpha_i$ | 0.720 | 0.641 | −11.0% |
| Current density @ 8 A (A/mm²) | 15.53 | 15.5 | −0.2% |
| Flux linkage $\lambda$, peak (mWb) | 1.746 | 1.738 | −0.5% |

Overall, the analytical and numerical model agree for the plastic model as well, and the error for Bg was not as apparent as it was for the metal model.

### Experimental:

After calibrating my dynamometer with two known motors, I spun my plastic motor with one test and got some very interesting values.

<img src="https://github.com/user-attachments/assets/fc727cfe-42b0-4685-a48a-393f91d2df39" width="15%" />
<img src="https://github.com/user-attachments/assets/ed354f6e-8052-4396-9ac5-ece1b1381b5d" width="15%"/>
<img src="https://github.com/user-attachments/assets/1a0cad23-32cd-4f43-9009-7f3e82ea98b2" width="15%"/>
<img src="https://github.com/user-attachments/assets/462c0ef4-2819-423f-b3fa-6790294d4735" width="15%"/>
<img src="https://github.com/user-attachments/assets/95a58547-6fed-41e1-9d8a-7d4fbd6f39b4" width="15%"/>
<img src="https://github.com/user-attachments/assets/aa29ee3c-8f49-4a31-877d-14946f19b42b" width="15%"/>

<img width="1870" height="1020" alt="image" src="https://github.com/user-attachments/assets/5e9c3d68-e05a-4475-a2d5-004c20a7f530" />

*Experimental Results (V2)*

| Parameter | Value |
|---|---|
| Ke (line-to-line peak) | 0.041 V·s/rad |
| KV | 232 rpm/V |
| Kt (8.27 / KV) | 0.036 N·m/A |
| Drive-side drag (Iq × 0.085 N·m/A) | 0.025 N·m |

### Analytical vs. Numerical vs. Experimental (V2 Plastic)

| Quantity | Analytical | FEMM | Measured (dyno) | Measured vs FEMM |
|---|---|---|---|---|
| KV (rpm/V) | 150.5 | 151.1 | 232 | +53.5% |
| Ke, line-to-line peak (V·s/rad) | 0.0634 | 0.0632 | 0.041 | −35% |
| Kt (N·m/A) | 0.0550 | 0.0547 | 0.036 | −34% |
| Torque @ 8 A (N·m) | 0.4397 | 0.438 | 0.288 | −34% |

## Results Discussion (V2)

Although it doesn't seem like a short since the three phases are still operating generally as expected on the oscilloscope, although the sine waves have very small offsets, possibly due to my winding 7 instead of 8 turns on a couple teeth, give or take. This was one of my first wound motors, and I may have lost count.

The resultant KV was massively over the estimates by the generally agreed upon analytical and numerical models. I will continue to run some tests using different motor phases or try rewinding a new motor to see if there are any big jumps or issues with this one.

A note: I had ran the motor as a demonstration a few days prior, but it emitted a concerning amount of heat, which didn't happen on the initial spins. It is possible I had set the residual pole pairs to 20 instead of 21 since I frequently switch out the 40P LA8308 motors with the driver. this may have caused the motor to partially melt.

Another cause for issue is that the magnets I purchased were cheap N38 ones from AliExpress, and the size of the magnets was quite off from their listing, so it may be possible that their rating was off as well.

Still, the gap is too huge for this value to exist, unless there are additional losses due to friction or flux leakage that I hadn't accounted for.

Further Tests: Different phases to see if the results change, retesting phase resistance.

*TODO*

