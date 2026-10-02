---
title: First Spin
parent: V2 (Current Build)
grand_parent: Hardware
nav_order: 1
---

# Documentation for First Spin

After soldering the enameled copper wire (took longer than I imagined) into their respective 4-strand phases (three phases) and the ends in star configuration, it was time to see if it could spin without exploding.

I decided to try an open loop test using the STM32 B-G431B-ESC1 using ST Motor Control Workbench and STMCubeIDE to go for a simple open loop velocity ramp with very conservative power.

With 96 turns per phase (8 per tooth), the measured phase resistance was 0.5 $\ohm$.

Knowing 21 pole pairs, 10.5 Vrms/kRPM

8V-3A

<img src="https://github.com/user-attachments/assets/8dedf724-d455-4db7-add5-2534e80eece0" width="80%"/>

<img src="https://github.com/user-attachments/assets/4cd3105b-9475-471f-9d24-ed8a72d43fef" width="80%"/>






