---
title: V2 (Working Plastic Build)
parent: 2. Motor Builds
nav_order: 1
has_children: true
---

# Motor V2

A few updates were implemented after the failure of the V1 motor.

<video src="https://github.com/user-attachments/assets/bda9567a-19c8-4262-996d-6315954c4c0d" autoplay loop muted playsinline style="width: 100%;"></video>

A slightly larger, 1.25mm airgap was used to account for human errors from JB weld application/buildup in constructing the rotor magnets.

<img src="https://github.com/user-attachments/assets/2e06e949-349e-40ab-b591-0b09ca89582d" width="23%"/>
<img src="https://github.com/user-attachments/assets/43d81169-eee6-47cd-9220-714c41d551f6" width="35%"/>
<img src="https://github.com/user-attachments/assets/322183f8-5c8e-4ba0-8d10-9c04eb0e5ead" width="35%"/>



Additionally, with more stator core winding techniques developed since the first one, I was able to fit a fourth internal parallel strand per bundle, bringing the theoretical current density from 7.7 $A/mm^2$ down to 5.82 $A/mm^2$ at a 3A phase current.

<video src="https://github.com/user-attachments/assets/fcafa64b-c9ab-4098-a93f-8e37dfa5ae22" autoplay loop muted playsinline style="width: 100%;"></video>

More care was taken in welding the magnets to prevent magnet rub, and an updated bearing design resulted in a free-spinning rotor with felt cogging behavior, much like the COTS motors I own.

This was quite satisfying to put together, and I now bring the motor (unpowered) with me wherever I go to use as a fidget spinner.



<video src="https://github.com/user-attachments/assets/4998a40d-5d8d-4aae-9f4f-dfe09829d258" autoplay loop muted playsinline style="width: 100%;"></video>

# Documentation for V2 First Spin (BG431B Open Loop)

After soldering the enameled copper wire (took longer than I imagined) into their respective 4-strand phases (three phases) and the ends in star configuration, it was time to see if it could spin without exploding.

I decided to try an open loop test using the STM32 B-G431B-ESC1 using ST Motor Control Workbench and STMCubeIDE to go for a simple open loop velocity ramp with very conservative power.

With 96 turns per phase (8 per tooth), the measured phase resistance was 0.5 $\Omega$.

Knowing 21 pole pairs, 10.5 Vrms/kRPM, and setting 8V/3A limits:

<video src="https://github.com/user-attachments/assets/d951ecac-e92d-4f63-b2b6-3e24d5d7f2f4" controls playsinline style="width: 100%;"></video>

This technically reports a KV of 125, which is probably incorrect, since there's no voltage sensing on the board. More robust test methods are described in my documentation for my YVDyno-8308 trials, found [here](../testing-and-validation/SimpleMotorTester.md).

<img src="https://github.com/user-attachments/assets/8dedf724-d455-4db7-add5-2534e80eece0" width="80%"/>

<img src="https://github.com/user-attachments/assets/4cd3105b-9475-471f-9d24-ed8a72d43fef" width="80%"/>

