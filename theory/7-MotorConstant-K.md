# Motor Constant K

The motor constant K can either be experimentally derived by measuring KV or analytically derived using mechanical and electrical properties.

It is simply KV, in RPM/V multiplied by the number of turns.

$K_C =$ turns * KV

K_c itself is a function of both mechanical attributes and electrical attributes:

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
K_c = \frac{60/2\pi}{C_{SD} * N_{TPP} * K_w * (N_{poles}/2) * \phi_{Pole}}
$$

$$
\phi_{Pole} = B_g * A_{pole}
$$

$$
A_{pole} = (\frac{2\pi * r_{gap} * L_{stack}}{N_{poles}})
$$

Where $B_g$ can be estimated, or calculated using:

$B_r$ : Remanent flux density, dependent on NdFeB grade.

$L_M$ : Magnet thickness (mm)

$\mu_r$ : Magnetic recoil permeability, generally close to 1.01-1.15 for NdFeB magnets. Dimensionless, as it is the slope of the linear portion of a magnet's demagnetization curve.

$g$ : Airgap length - the very small space between rotor and stator (mm)

$$
B_g = \frac{B_r * L_M}{L_M + (\mu_r*g)}
$$

For fun, the entire analytical equation for $K_c$ using all inputted variables is:

Star:

$$
K_c = \frac{60/2\pi}{\sqrt{3} * N_{TPP} * K_w * (N_{poles}/2) * \frac{B_r * L_M}{L_M + (\mu_r*g)} * (\frac{2\pi * r_{gap} * L_{stack}}{N_{poles}})}
$$

$$
K_c = \frac{1}{\sqrt{3}} * \frac{30*(L_M + (\mu_r * g))}{\pi^2 * N_{TPP} * K_W * B_r * L_M * r_{gap} * L_{stack}}
$$

The effect of the motor constant K is a simple scaling of KV, notable affecting the design parameter, **Turn Count.**


