# Mathematical Derivations for Motor Python Calculator

The following derivations explains the equations in each part of the Python code.

Variables:

$n$ : AWG gauge

$n_s$ : Strand count

$n_t$ : Turn count

$d(n)$ : Strand diameter ($mm$)

$A(n)$ : Strand cross sectional area ($mm^2$)

$MTL$ : Mean Turn Length ($mm$)

$\rho$ : Copper resistivity, ($\ohm*m$)





## 1. AWG Wire Geometry

Referencing the equation for motor AWG gauge (n) to wire diameter d(n), in mm:

$$
d(n) = 0.127 * 92 ^{\frac{36-n}{39}} 
$$

And cross sectional area A(n), in $mm^2$:

$$
A(n) = \frac{\pi*d(n)^2}{4}
$$

When using multiple strands, an effective area $A_{total}$ from the number of strands $n_s$, as well as its equivalent AWG gauge $AMG_{equiv}$:

$$
A_{total} = n_s * A(n)
$$
$$
d_{equiv} = 2\sqrt{\frac{A_{total}}{\pi}}
$$
$$
AMG_{equiv} = 36 - 39 * \log_{92} (\frac{d_{equiv}}{0.127})
$$

## 2. Resistance

A function for copper resistance $\rho$ ($\ohm*m$) is estimated over motor operating temperature T for annealed copper:

$$
\rho(T) = \rho_{20C} * (1 + \alpha (T-20))
$$

where $\alpha = 0.00393/C$ , and $rho_{20C} = 1.724 x 10^{-8} \ohm*m$.

Then, resistance per unit length in $\ohm/m$ is calculated using the total effective area $A_{total}$ accounting for strand count $n_s$:

$$
R_{per_{m}} = \frac{\rho(T)}{A_{total}*n_s}
$$

Then, the coil resistance $R_{coil}$ is found when factoring in turn count $n_t$ and mean turn length MTL (mm):

$$
R_{coil} = R_{per_{m}} * (n_t * \frac{MTL}{1000})
$$

## 3. Turns, KV and Kt Relationship






