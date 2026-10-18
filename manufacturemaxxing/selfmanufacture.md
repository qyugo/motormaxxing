---
title: Low-Cost Self-Manufacture for V3
parent: 2. Motor Builds
nav_order: 4
has_children: true
---

# Manufacturing Plan for V3 Motor
10/18/2026

This outlines a potential plan for self-manufacturing some motors out of metal at a fraction cost of getting it machined in full, but with many extra steps from me. I figured this would be a great learning opportunity regardless, and it would allow me to make multiple iterations and make adjustments without relying on an external shop in the meantime.

I may still get the motor machined or at least some quotes, but after running DFM analysis the cost seemed too great for one piece. I want to be able to create many of these.

V3 Rotor Housing 3D Model and Drawing/Tolerances (as of 10/18/26):

<img src="https://github.com/user-attachments/assets/86c84d82-8e12-489f-bcc5-1d07f3cae146" width = "33%" />

<img src="https://github.com/user-attachments/assets/a89edce6-e723-45f8-9f1b-4bcc0dd74425" width = "60%"/>

## Aluminum Shell (deprecated, initial research)

Aluminum 6061 extrusions were considered for the cheapest possible build, as aluminum is the most common extrusion material, and also soft enough to be turned on a small lathe if need be. V3 motor may be updated periodically to decrease complexity/costs for manufacturing.

Rather than fully CNC machining the machine, the rotor can be split into multiple segments, such as the backiron for the magnets and the rotor hub.


A final BOM will be created for this manufacturing method.

4.0in OD / 102mm OD x 98mm ID aluminum (1 ft/30cm)

<img src="https://github.com/user-attachments/assets/799b4883-57af-4511-a9c9-2436c4549c78" width = "22%"/>

<img width="468" height="177" alt="Screenshot 2026-10-18 at 12 46 21 PM" src="https://github.com/user-attachments/assets/b6d6a283-9f34-4971-9a86-13e6844bca29" />

[HPS Performance Products](https://hpsperformanceproducts.com/products/hps-straight-6061-aluminum-tubing-tube-pipe-piping-seamless?variant=40434209095870)

Cost: $50.38

For a 21.5mm thick rotor, and an 8.5mm stator (stator will be discussed later), this money can theoretically contribute to 10.15 motors, accounting for losses perhaps 9 or 10.

For reference, this is how the ring would sit on the current motor:

<img width="570" height="484" alt="Screenshot 2026-10-18 at 1 39 36 PM" src="https://github.com/user-attachments/assets/4b845984-126e-4675-b39c-865fc5a06aca" />

This idea is currently on hold, as it may be better to design 

## Steel Backiron

Evidently, I had planned at this point for a smaller 1040/1018 steel sleeve (about 10mm height) to sit inside this aluminum ring to serve as a proper backiron for the NdFeB magnets, as aluminum is insufficient in its magnetic properties to provide flux return.

However, I thought I could scrap this idea and the aluminum tube altogether by redesigning around a pre-made steel backiron, since 1018/1020 steel would be harder to machine myself on a small lathe. Aluminum 6061, on the other hand, can be easily carved out to fit any tolerances and advanced geometry, and doesn't require the same ferromagnetic properties as the steel backiron.

The choices were mainly between 1018 and 1040 steel, which are similar in price but slightly different in mechanical and magnetic properties, with 1040 being slightly stronger in stiffness/tensile strength. Since my outrunners are not going to run at too crazy of RPMs, I felt this was a negligible issue.

Further, I had already run some FEMM simulations for 1018.

Next was needing a 4.65mm thick steel backiron to fit within the aluminum tube while providing the proper 0.75mm airgap from my simulation.

The inner diameter would be more important, with 88.7mm providing a 0.75mm airgap between the magnets and the stator. An ideal outer diameter would be the inner diameter of the aluminum outer shell, but this would heavily depend on errors from the aluminum fab, in which a small lathe could make any adjustments.

With some proper turning clean-up, concentricity can be achieved with some small errors.

* Source 1: WRONG DIAMETER - DEPRECATED*

<img src="https://github.com/user-attachments/assets/ff04ac89-ee32-4318-98e4-b8fad2731485" />

[Mcmaster 1018 Steel](https://www.mcmaster.com/products/grade-1018-steel/shape~round-tube/?s=grade-1018-steel)
For 1ft, $17.85, not including shipping & tax

<img src="https://github.com/user-attachments/assets/550214ea-2af6-4341-b2f0-e5ac8fa5d64d" />

* END *

Source 2:

A 3.75" by 3.5" ID steel tube was almost identical to the backiron I had designed, perhaps by coincidence. The best option I could find was by Speedy Metals, who as far as I can see, only provide C1020 materials for their steel tubing, with a perfect size available.

Since 1020 steel is almost identical to the 1018 run on the simulations, I decided to purchase some and rerun the simulations, although I would expect not too big of a difference.

https://www.speedymetals.com/ShoppingCart.aspx?add=true&ReturnUrl=https%3a%2f%2fwww.speedymetals.com%2fpc-3551-8242-3-34-od-x-125-wall-dom-steel-tube.aspx
For 1ft, this was funny:
<img width="1370" height="449" alt="Screenshot 2026-10-18 at 2 37 38 PM" src="https://github.com/user-attachments/assets/652ba0ba-0771-4bc2-9eba-a0274c52e42e" />

However, testing out their by-the-inch, which has a cutting tolerance of up to 1/8 in, seeing if I can go for 1/2 inch blocks:

<img width="513" height="72" alt="Screenshot 2026-10-18 at 2 45 23 PM" src="https://github.com/user-attachments/assets/55210fea-24e6-47e2-b97d-6e5455cfa87e" />

If I were to cut them myself, I would save approximately $1 per piece (if using the 12in $63.33 option), and $1.83 per piece if their identical 12in by-the-inch option really costs 42.22.

I decided to go for a set of 6 pieces cut by them, for prototyping. Since my magnets are all slightly under 12mm, some additional spacing for joining the ring to the rest of the aluminum housing would be helpful.
It is also worth noting that their cuts are listed as having a tolerance of -0, and +1/8". Therefore, I placed out a few steps of 1/8" to visualize my decision.

Length Decision table:

| Length Option (in) | mm conversion | Cost per ($) |
| --- | --- | --- |
| 7/16" | 11.1125 | 3.52 |
| 1/2" | 12.7mm | 3.52 |
| 9/16" | 14.2875 | 3.52 |
| 5/8" | 15.875 | 3.52 |

I decided to go for the 1/2" + 1/8in tolerance. Below are some views, where the silver ring is the expected 1020 steel part, with red being the possible 1/8" added tolerance, overlayed and compared to the existing rotor cap and magnets in Onshape.

<img width="730" height="263" alt="Screenshot 2026-10-18 at 3 19 35 PM" src="https://github.com/user-attachments/assets/4996d710-cab0-401a-9e6f-55fab2a193b5" />

<img width="654" height="205" alt="Screenshot 2026-10-18 at 3 20 36 PM" src="https://github.com/user-attachments/assets/d0256fa2-c88b-4568-a59c-a4ceaefa84fe" />

For 6 pieces, this is 21.11. Shipping was 23.64.

<img width="1416" height="235" alt="Screenshot 2026-10-18 at 3 28 48 PM" src="https://github.com/user-attachments/assets/a0ac3dd1-71fb-4ed0-83f9-df6b2b1cdf12" />

A jig is used for the attaching of magnets to the backiron, and no slot dividers like the PETG design will be used.

## Aluminum Cylinder + Lathe Analysis

With this, aluminum cylinders were considered for the stator and rotors, which can be lathed. Since some boring is needed for the bearing housing, and a good tolerance fit, I decided to change the idea to machining a solid cylinder of aluminum to build around the steel backirons I ordered.

Depending on the errors on the steel backiron, the aluminum can be adjusted with a small lathe, as it is a much softer metal.

Buying a full cylinder would definitely be more expensive than a tube extrusion, but I decided to explore the cost analysis regardless.


