## Testing and Validation Hardware

In order to characterize the empirical K-values and determine how far off the analytical model was, a testing and validation setup is described in this section.

## Dynamometer

<img src="https://github.com/user-attachments/assets/0580764b-e500-4fc8-bfe4-44512cdba4ec" width="45%"> 

Pictured: _Power Test Dynamometer._

When driven, a BLDC motor produces a three-phase AC voltage output. This voltage and resultant motor speed depends on the KV rating motor, which can be extracted when both are measured.

$$
KV = RPM/V
$$

Additionally, current is generated as a function of voltage generated and total impedance Z:

$$
I = V/Z
$$

Where Z is the sum of the motor internal phase resistance $R_{phase}$, external load resistance $R_{load}$, and inductive reactance (AC opposition) $X_L$:

$$
Z = R_{phase} + R_{load} + X_L
$$

Inductive reactance is present when voltage and current are constantly changing, dependent on frequency:

$$
X_L = 2\pi * f * L
$$

However, reactance is dominant in higher RPMs (6000RPM+). For low RPMs, the impedance characteristics can be calculated without reactance:

&emsp;&emsp;&emsp;Low RPM (<2000) : $Z \approx R_{phase} + R_{load}$

&emsp;&emsp;&emsp;Medium RPM (2000-6000) : Z = $\sqrt{(R_{phase} + R_{load})^2 + X_L^2}$

&emsp;&emsp;&emsp;High RPM (>6000) : $Z \approx X_L \approx 2\pi * f * L$

This current is related to _braking torque_, calculated as follows:

$$
T_{brake} = K_t * I
$$

