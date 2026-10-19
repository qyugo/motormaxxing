---
title: 2. Motor Builds
nav_order: 3
has_children: true
---
``` motormaxxing 2/3 ```

## Subproject 2: Building a Working Motor from Scratch

Currently, a few variants of the 8110 motor have been built. 

## V2 (Working PETG Motor)

This version utilizes NdFeB N38 magnets with 1.25mm airgap, with 8 turns per tooth, and 4 internal parallel strands.

<img width="1280" height="720" alt="IMG_3859 Large" src="https://github.com/user-attachments/assets/bb89b1c4-0304-4586-934c-db11f2844be5" />

This one managed to spin with both the BG431B-ESC1 as well as the ODrive S1, as well as my custom YVGESC driver.

## V3 (in progress metal motor)

The initial plan after the working V2 model is to build a new CNC-machined rotor, and slightly thicker, N42 magnets, with the same 8 turn/tooth winding pattern, and four internal parallel strands.

Currently, it is not within my budget to get a fully CNCed rotor, but ran some DFM analyses and tolerance drawings nonetheless.

<img width="880" height="437" alt="Screenshot 2026-10-18 at 1 15 08 PM" src="https://github.com/user-attachments/assets/0018a61c-7726-4b83-8070-0a66d86dec8f" />

However, in progress is a cost-optimized manufacturing process that allows me to (hopefully) create many metal motors without sending a CNC milling quote. I figured with some creative design to account for the rotor/stator hubs and the back-iron for the magnets, I could create a metal motor using just a lathe, that is both multimaterial and a fraction of machining cost.


## Deprecated Models

V1: PETG, NdFeB N38 steel-epoxy-welded, Bad bearings, caused wobble/rotor would stick to one side of the stator core. 3 internal parallel strands, as it was my first winding, and couldn't fit a fourth, unlike when I wound V2.

<img src="https://github.com/user-attachments/assets/8988e030-856d-4172-ab51-8e681b8d0e78" width="60%" />

V1.1: Bearing problem fixed (no more wobble), however magnet rub present due to too small an airgap and epoxy buildup unaccounted for.

<img src="https://github.com/user-attachments/assets/1e8f9740-5094-4c2b-b727-03c0f476d5c7" width="40%"/>
<img src="https://github.com/user-attachments/assets/97e3cc04-dbf8-4c27-990b-7c5d1d6d70c1" width="40%"/>

V1.2: Since the rotor was welded, I took this opportunity to print a 8010 PETG stator core, for a horrible, fully 3D printed motor (minus bearings and windings). This was not tested, but it was fun to have around as a paperweight.

<img src="https://github.com/user-attachments/assets/bec1bfd9-c72b-4ee8-a91b-b48d25301081" width="60%"/>

V2.1: Prototype with slightly adjusted rotor depth so I can fasten adapters/couplings/gears while saving space.

<img width="1280" height="1073" alt="IMG_4590 Large 2" src="https://github.com/user-attachments/assets/15bcb1bf-0727-4e41-95e3-a15b0a47ca72" />



