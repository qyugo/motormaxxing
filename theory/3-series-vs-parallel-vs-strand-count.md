# Series vs. Parallel Winding
In this section, a clarification of **series vs. parallel coil winding** will be discussed and how it differs from **strand count**. There are some sources online that I have come across that are unclear or incorrect about the distinctions of motor winding configurations.

## Confusion 1: Strand Count

Strand count would be the _number of parallel wire strands in each conductor_. This will be used later on to effectively make the wire of each phase (thicker) with more wires running the same A path, B path, etc. This is done to make the current-carrying capacity of each phase larger by increasing the effective cross-sectional copper area of each phase.

More strands in a "bundle" would not affect the effective _turn count_ **(T)**; for example, in the following partial construction of an 8110 36N42P motor of just the A phase, I did 8 turns per tooth, and used a strand count of 3. Basically, three strands are following the wiring config of A, but the effective turn count (T) is still 8, not 24.

<img src="https://github.com/user-attachments/assets/f7e021ef-c715-4308-97bc-716d9e6ddc0c" width="50%"> 

Summary: The term "Strand Count" does not affect the attributes of the circuit, but rather it's current-carrying capacity.

## Series vs. Parallel Winding

This is NOT the same as how many parallel strands constitute a phase. Parallel paths would be the splitting of one phase into separate parallel circuits. This can be done to adjust both the voltage and current characteristics of the motor.

<img src="https://github.com/user-attachments/assets/ae6e0465-ce9a-4499-a251-750ee65f6614" width="70%"> 

Diagram Source (with self labels): https://www.emetor.com/glossary/number-of-parallel-paths/

The top image in the figure above shows a series winding. In a series winding, there is technically "1 parallel path." This is the configuration used for the example used in this repository for a simple BLDC construction.

The middle image in the figure shows an example of a parallel path, specifically "2 parallel paths" in this case.

The bottom image shows one series path, effectively functioning the same as the top image, but is composed of two strands, which functions as a "thicker" single wire. Sometimes, this also can be characterized as "internally split up into two parallel paths," which may raise some confusion.

## Performance Characteristics
In series windings, the back-EMF of each coil adds to the next, so the total would be the sum of the BEMF of all coils. More coils in series would usually constitute a lower KV, higher torque per amp, and requiring _higher voltage_ for operation and _less current_ draw.

For parallel windings, the back-EMFs are kept low, resulting in a higher KV, lower voltage requirement and more current draw.

Much of the voltage difference is due to the coil resistance attributes:

For a **parallel winding**, the phase resistance _R_phase_ = R_coil / N_teeth_per_phase.
For a **series winding**, _R_phase_ = R_coil * N_teeth_per_phase.

And finally, more strands per bundle will decrease the phase resistance via a separate mechanism, by making the effective strand "fatter."

## Next Up
Additionally, voltage and current characteristics can be modified by terminating the windings in either **Delta** or **Star** (also known as Wye or Y-configuration. This will be discussed in the next module.
