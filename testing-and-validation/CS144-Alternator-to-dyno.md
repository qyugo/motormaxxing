## Old Car Alternator to Passive Dynamometer

I had an old Delco CS-144 alternator laying around from my old car in high school, and have been meaning to use it for a project.
Previously, the rectifier was broken, but it has since been deconstructed, hollowed out, and the three stator phases and two field wires routed out.

Unlike a BLDC motor, both the rotor and the stator are composed of windings, with the outer stator windings containing three phases, and an inrunner wound-rotor containing a single field coil, powered by two brushes via slip rings. Surrounding the rotor coil are claw poles, which act as flux concentrators to become alternating N-S magnets when powered, in a 6-pair, 12-pole configuration.

This alternator is essentially a wound-rotor synchronous motor (WRSM). However, it can function somewhat as a brushless motor (with brushes) if a constant voltage is applied to the "field" as the rotor spins, essentially having the stator function as a permanent magnet.

However, its normal alternator-type configuration (generating electrical power from movement) will be utilized, functioning as a passive absorption dynamometer.

## 1. Deconstruction

The most difficult part of this process was detaching the pulley. However, I managed to get it off using a breaker bar, while a strap wrench and a sketchy vise clamping kept the pulley in place, along with some anger.

<img src="https://github.com/user-attachments/assets/aee1bce7-cac8-4dbf-990c-6aff853fce55" width="25%"/>
<img src="https://github.com/user-attachments/assets/8f58d0e5-cf3a-4ea5-9d38-d343e3536099" width="65%"/>

I replaced the brushes and verified that the rotor windings were still functional, with a phase resistance of about 0.1-0.2 ohms. The field excitation also retained function, as a magnetic field is generated when a small DC voltage was applied to the slip rings.

<img src="https://github.com/user-attachments/assets/f09570b9-1251-4aec-bb40-40373392eef5" width="45%"/>
<img src="https://github.com/user-attachments/assets/fc8589e2-2d56-4183-bb1c-c3cb05c26b80" width="45%"/>

## 2. Mechanical Setup

In images, the white wires are the three stator phase windings, and the red and black wires are the two terminals for powering the rotor.

<img src="https://github.com/user-attachments/assets/26ad4054-d508-46ba-932f-1046d2abe941" width="80%"/>

As a passive/absorption dynamometer, the test motor will spin the shaft of the CS-144 alternator via a 1:1 coupling, which produces a voltage/current through the three output stator phase windings, provided the field current (rotor) is separately powered.

The three phase wires will then be routed to a three-phase rectifier, which will convert the three wires to a standard DC output (+/-).

A power resistor is then places across the DC output of the rectifier, sized as follows.

### Power Resistor
The power resistor value and rating will be derived from the maximum voltage ceiling of the dynamometer and intended maximum current for the test.

The maximum voltage ceiling $V_{max}$ depends on the range of field excitation and the maximum intended RPM for the test motor.

Voltage ceiling will be the RMS voltage measured across two of the three phase wires @ maximum field excitation and maximum RPM.

Then, using an intended continuous current $I_{motor}$ for testing operations, a resistance value can be sized:

$$
R = \frac{V}{I}
$$

The power rating for the resistor is sized 3x the maximum power situation:

$$
P = V * I
$$

Voltage and DC current is then measured across the rectifier output/resistor, coupled with speed data measured using either a tachometer or the test motor's encoder.

V + I + RPM will be logged at different points to characterize the motor.

Unlike other dynamometers (i.e. Prony brake) that can directly measure torque, this setup can use the standard $T = \frac{V * I}{\omega}$ equation.

A set of two INA226 current sense monitors and an Arduino Nano will be used to measure the current via voltage across its shunt resistor. This will be placed to measure both the field circuit (field winding) and the load circuit (power resistor, diode output).

<img src="https://github.com/user-attachments/assets/4902706c-1f4a-40de-9310-2b2022cf7778" width = "50%"/>


## Relevant Readings

## A. Torque vs. RPM

## B. Generated Voltage vs. RPM

KV Characterization

## C. Motor Phase Current vs. Resistive Load Current

Checking for losses, plotting drive-side current with the dynamometer's output DC current. If there is a large disparity, losses or error may be apparent.

## D. Output Power vs. RPM

## E. Efficiency/Loss vs. RPM

The efficiency $\eta$ can be calculated by the power output from the resistor/rectifier side $P_{OUT}$ and the power in from the driver side, $P_{IN}$.

$$
\eta = \frac{P_{OUT}}{P_{IN}}
$$

Plotting this vs. RPM can give efficiency characteristics across different speeds.

## F. Generated Torque/Voltage Across Field Current Sweep (Fixed RPM)






