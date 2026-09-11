# Motor Constant K

The motor constant K can either be experimentally derived by measuring KV or analytically derived using mechanical and electrical properties.

It is simply KV, in RPM/V multiplied by the number of turns.

$K =$ turns * KV

K itself is a function of both mechanical attributes and electrical attributes:

$B_g$ : Airgap flux density (T)

$r_{gap}$ : Radial gap, distance from the center of the motor to the middle of the air gap (mm)

$K_w$ : Winding factor

$N_{poles}$ : Number of poles

$N_{TPP}$ : Teeth per phase

$L_{stack}$ : Stack length or thickness of stator (mm)

$C_{SD}$ : Multiplier, 1 for delta config or $\sqrt{3}$ for star.

$\phi_{Pole}$ : Flux per pole (Wb)

$A_{pole}$ : Pole area (mm^2)

$$
K = \frac{60/2\pi}{C_{SD} * N_{TPP} * K_w * (N_{poles}/2) * \phi_{Pole}}
$$

$$
\phi_{Pole} = B_g * A_{pole}
$$

$$
A_{pole} = (\frac{2\pi * r_{gap} * L_{stack}}{N_{poles}})
$$

Where $B_g$ can be estimated, or calculated using:

$B_r$ : Remanent flux density, dependent on NdFeB grade. Referring to the following table:

| Magnet Grade | Br (T) |
| --- | --- |
| N35 | 1.17 – 1.22 |
| N38 | 1.22 – 1.25 |
| N40 | 1.25 – 1.28 |
| N42 | 1.28 – 1.32 |
| N45 | 1.32 – 1.38 |
| N48 | 1.37 – 1.42 |
| N50 | 1.40 – 1.45 |
| N52 | 1.43 – 1.48 |

$L_M$ : Magnet thickness (mm)

$\mu_r$ : Magnetic recoil permeability, generally close to 1.01-1.15 for NdFeB magnets. Dimensionless, as it is the slope of the linear portion of a magnet's demagnetization curve. Set as default 1.05 in the code.

$g$ : Airgap length - the very small space between rotor and stator (mm)

$$
B_g = \frac{B_r * L_M}{L_M + (\mu_r*g)}
$$

For fun, the entire analytical equation for $K_c$ using all inputted variables is:

Star:

$$
K = \frac{60/2\pi}{\sqrt{3} * N_{TPP} * K_w * (N_{poles}/2) * \frac{B_r * L_M}{L_M + (\mu_r*g)} * (\frac{2\pi * r_{gap} * L_{stack}}{N_{poles}})}
$$

$$
K = \frac{1}{\sqrt{3}} * \frac{30*(L_M + (\mu_r * g))}{\pi^2 * N_{TPP} * K_W * B_r * L_M * r_{gap} * L_{stack}}
$$

The effect of the motor constant K is a simple scaling of KV, notable affecting the design parameter, **Turn Count.**

## Carter's Coefficient K_c (Correction for airgap -> K)

Yes, that's right, another K. When analytically calculating values such as airgap flux, it is necessary to account for the leakage flux, iron saturation, and slot-opening correction (K_c).

Without this, the equations noteably for $B_g$ assume a smooth gap between the rotor and the stator, resulting in much higher KV and torque values than in reality. Carter's coefficient addresses the unevenness of the air gap due to the presence of slots, which in creases _magnetic reluctance._

$K_c$ is a scaling factor for airgap length $g$, giving us an effective airgap length $g'$:

$$
g' = K_c * g
$$

Where $K_c >= 1$.

The formula for $K_c$ depends on the slot pitch $t_s$ (which is a function of diameter D and number of slots $n_{slots}$, the width of each slot opening $w_s$, and the airgap $g$.

$$
t_s = \frac{\pi*D}{n_{slots}}
$$

$$
K_c = \frac{t_s}{t_s - \sigma*w_s}
$$

Where $\sigma$ is a function of the slot width to airgap ratio:

$$
\sigma = \frac{w_s/g}{5+ (w_s/g)}
$$

This is to be calculated for both the stator ($K_{CS}$) and the rotor ($K_{CR}$) since both contain slots. 

Finally, the effective airgap g':

$$
g' = g * K_CS * K_{CR}
$$
