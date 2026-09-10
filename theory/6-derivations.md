# Mathematical Derivations for Motor Python Calculator

The following derivations explains the equations in each part of the Python code.

Variables:

$n_g$ : AWG gauge

$n_s$ : Strand count

$n_t$ : Turn count

$d(n)$ : Strand diameter ($mm$)

$A(n)$ : Strand cross sectional area ($mm^2$)

$MTL$ : Mean Turn Length ($mm$)

$\rho$ : Copper resistivity ($\ohm*m$)

$KV$ : Speed constant of a motor ($RPM/V$)

$K_e$ : Motor b-EMF constant ($V/rad/s$)

$K_t$ : Motor torque constant ($N*m/A$)

$\phi$ : Magnetic flux ($Wb$, or $V*s$)

$B$ : Magnetic flux density ($T$, or $Wb/m^2$)

$\lambda$ : Flux linkage ($Wb$)

$\theta$ : Angle ($rad$)

$\tau$ : Torque ($N*m$)

$I_{phase}$ : Phase current ($A$)

$\frac{d\lambda}{d\theta}$ : Change in flux linkage with rotor angle ($Wb/rad$)

$K_w$ : Winding factor

$E$ : Back-EMF ($V$)

$\omega$ : Angular velocity of the rotor ($rad/s$)






## 1. AWG Wire Geometry

Referencing the equation for motor AWG gauge ($n_g$) to wire diameter d($n_g$), in mm:

$$
d(n_g) = 0.127 * 92 ^{\frac{36-n}{39}} 
$$

And cross sectional area $A(n_g)$, in $mm^2$:

$$
A(n_g) = \frac{\pi*d(n)^2}{4}
$$

When using multiple strands, an effective area $A_{total}$ from the number of strands $n_s$, as well as its equivalent AWG gauge $AMG_{equiv}$:

$$
A_{total} = n_s * A(n_g)
$$
$$
d_{equiv} = 2\sqrt{\frac{A_{total}}{\pi}}
$$
$$
AMG_{equiv} = 36 - 39 * \log_{92} (\frac{d_{equiv}}{0.127})
$$

## 2. Resistance

A function for copper resistivity $\rho$ ($\ohm*m$) is estimated over motor operating temperature T for annealed copper:

$$
\rho(T) = \rho_{20C} * (1 + \alpha (T-20))
$$

where $\alpha = 0.00393/C$ , and $\rho_{20C} = 1.724 x 10^{-8} \ohm*m$.

Then, resistance per unit length in $\ohm/m$ is calculated using the total effective area $A_{total}$ accounting for strand count $n_s$:

$$
R_{per_{m}} = \frac{\rho(T)}{A_{total}*n_s}
$$

Then, the coil resistance $R_{coil}$ is found when factoring in turn count $n_t$ and mean turn length MTL (mm):

$$
R_{coil} = R_{per_{m}} * (n_t * \frac{MTL}{1000})
$$

## 3. Turns, KV and Kt Relationship (For Star/Wye, 3-phase, sinusoidal)

The K-constant is a function of turn count and motor KV, so it is independent of how many stator teeth/slots there are.

$$
K_{const} = n_t * KV
$$

Derivation of Kt from KV, an _ideal_ approximation for sine-commutated BLDC motors, and line-to-line KV:

First, $K_e$ and $KV$ are reciprocals of one another when units are matched.

$$
K_e (\frac{V}{rad/s}) = \frac{1}{KV} (\frac{V}{rev/min}) * (\frac{1 rev}{2\pi rad}) * (\frac{1 min}{60s})
$$

$$
K_{e, line} = \frac{1}{KV_{line}} * \frac{2\pi}{60} 
$$

The above expression is for _line-to-line_ characteristics, since KV is often measured from phase-to-phase using test hardware (since in star configurations, the neutral point is usually inaccessible).

However, these equations assume $K_e$ from _star-to-phase_ characteristics, so the value must be converted for subsequent calculations.

For a star winding, the line voltage and the phase voltage vary by a factor of $\sqrt{3} as per the characteristics of tying the phases together at a neutral point:

$$
V_{phase} = V_{line} / \sqrt{3} 
$$

$$
\therefore K_{e, phase} = \frac{1}{KV_{line}} * \frac{2\pi}{60} * \frac{1}{\sqrt{3}}
$$

We can then find the torque constant $K_t$ by summing the instantaneous power from three phases, offset 120 ° from each other in a 3-phase motor.

Torque is related to power $P = V*I$. In a moving motor, this will be the instantaneous product of the back-EMF waveform and the current waveform.

Earlier in the repo it is mentioned that change in flux linkage (due to the cutting of the motor across the magnetic field during motor motion) is related to back-EMF, which is related to torque. Here, we can spell it out by referencing both the _torque equation_ as well as the _back-EMF equation_ that references change in flux linkage. In other words, they describe the _spatial rate of change_ of flux linkage and the _temporal rate of change_ of flux linkage, respectively.

$$
\tau = I_{phase} * \frac{d\lambda}{d\theta}
$$

Where $\lambda$ is the flux linkage (Wb), defined as $\lambda = n_t*\phi*K_w$.

$$
E = \omega * \frac{d\lambda}{d\theta}
$$

Where E is the back-EMF (V), and $\omega$ is the angular velocity of the rotor (rad/s).

You can further prove that both $\frac{d\lambda}{d\theta}$ values are the same if you play around with some unit conversions, but I won't bother in this module. We can obtain an energy balance equation between $E, I_{phase}, \tau, \omega$ from the two above equations:

$$
E * I_{phase} = \tau * \omega
$$

The left side of the equation is a simple voltage * current expression - an expression for power (W). Likewise, the right side is also the expression for power in terms of torque, if you remember from physics class. This is another way to arrive at these equations, but I wanted to also connect the impact of flux linkage for the sake of motormaxxing.

In ideal field-oriented control (FOC), the back-EMF is sinusoidal, as well as the phase current. Maximum torque is then achieved when E and $I_{phase}$ are in phase with each other. We can describe both sinusoidal waves as a function of the maximum EMF and current with the following:

$$
E = E_{max} * cos(\theta)
$$

$$
I_{phase} = I_{max} * cos(\theta)
$$

$$
\therefore
$$

$$
E * I_{phase} = E_{max} * I_{max} * cos^2(\theta).
$$

Finally, we can obtain the average value of %cos^2(\theta) over one period. You can derive this using cosine trig identities, but for the sake of showing why cos and sin would be equal:

$$
cos^2(\theta) + sin^2(\theta) = 1
$$
Since the above is always true, it implies the average value of each term is 1/2.

And for three phases,

$$
3 * \frac{1}/{2} = \frac{3}{2}.
$$

$$
E * I_{total} = E_{max} * I_{max} * \frac{3}{2}) = \tau*\omega = P_{Ideal}.
$$

After all this, we can obtain a relation between $K_t$ and $K_e$ for a motor commutated by FOC:

By definition, the peak back-EMF $E_{max}$ is the back-EMF constant $K_e$ times speed:

$$
E_{max} = K_e * \omega,
$$

Plugging this in for $E_{max}$ from the previous energy balance equation but for all three phases (equating power to power, using $E, I, \tau, \omega$):

$$
P_{total} = E_{max} * I_{max} * \frac{3}{2}) = \tau*\omega
$$

$$
P_{total} = K_e * \omega * I_{max} * \frac{3}{2} = \tau*\omega
$$

$$
K_e * I_{max} * \frac{3}{2} = \tau.
$$

Finally, the torque constant $K_t$ is defined as _torque per peak current_ $\tau = K_t * I_{max}$.

Substituting this in,

$$
K_e * I_{max} * \frac{3}{2} = K_t * I_{max},
$$

$$
\therefore  K_e * \frac{3}{2} = K_t.
$$

Plugging in K_e in terms of KV, utilizing the equivalence derived earlier, we can finally obtain a relation between $K_t$ and $KV$.

$$
K_t = \frac{3}{2} * \frac{1}{\sqrt{3}} * \frac{60}{2\pi} * \frac{1}{KV}
$$

$$
K_t = 8.27/KV
$$



Source: 
https://source-robotics.com/blogs/blog/motor-constants-kv-kt-ke-km-explained




