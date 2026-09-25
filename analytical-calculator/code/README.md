## Instructions for Python Calculator


Run the following in terminal:
 
    python winding_calculator_gui.py
 
If error, a GUI toolkit may be needed:

    pip install PyQt5
    
(some Linux distros: sudo apt install python3-tk)
 
Equations and UI are contained in one file.

### 1. Stator Construction

All length units in mm.

<img width="334" height="256" alt="Screenshot 2026-09-15 at 3 40 15 PM" src="https://github.com/user-attachments/assets/efe401fd-a816-40aa-9543-e7e467f0914c" />

<img src="https://github.com/user-attachments/assets/0088e0bc-7fb2-4d31-a034-906d540b74ec" width="45%"> 

<img src="https://github.com/user-attachments/assets/e624efa3-b559-4be4-88e2-dcd0bde2b555" width="45%"> 

<img src="https://github.com/user-attachments/assets/d0e92c8a-4a4f-446a-9635-8c5c462f336d" width="28%">

### 2. Winding
Note: Parallel config is currently set to maximum number of parallel paths. This may be fixed later on if there is a point, since this is uncommon for BLDCs.

Star and delta can affect current/voltage and therefore performance properties.

Turns per tooth = number of complete turns of copper. Half-turns are not considered and rounded to the nearest full turn.
Strands per bundle = Number of strands per phase that make the same complete path (Internal parallel strands, different from parallel coil branching).

<img src="https://github.com/user-attachments/assets/5707a4df-b932-45dc-b56c-1169da129da7" width="35%">

Buildup: Extra length estimate of copper for increasing MTL over more windings.
Kp = pitch coefficient (= 1.00 for concentrated windings)
Ksk = skew coefficient (= 1.00 for no magnet skew)
Kd = Distribution coefficient

### 3. Magnetic Flux
Rectangular NdFeB magnets are assumed. 

<img src="https://github.com/user-attachments/assets/618c5d27-709f-4f1d-aca6-9f80e789214b" width="40%">

Note: Magnet length (the longer side of the face) is not considered in any equations. Width and thickness are used to adjust the flux and the slot leakage, respectively.

<img src="https://github.com/user-attachments/assets/c97dfa6c-ecd7-4e4a-a085-f4e36d5d4eb6" width="30%">
<img src="https://github.com/user-attachments/assets/25b06e81-ad81-499e-997f-6772340b9dc2" width="30%">

Magnetic permeability $\mu_r$ is in units of $T*m/A$. A default of 1.05 is recommended for NdFeB.

### 4. Corrections
Corrections are used mostly to decrease the analytical K constant to better match experimental values, accounting for slot leakage, operating temperature (as there is an apparent decrease in magnetic remanence $B_r$). This is used in conjunction with Carter coefficients accounting for slot pitch for the stator and rotor, which is utilized in the "Magnetic Flux" section to adjust the effective airgap.

<img src="https://github.com/user-attachments/assets/8d5d8f14-d829-466d-9df3-666341fcc44b" width="45%">

A default empirical K value can be adjusted to test theoretical KV adjustments and therefore independent of all the correction factors.

Additionally, the material of the rotor ring which houses the permanent magnets can be selected, in case a plastic prototype ring with a permeability $\mu_r = 1$ were to be used, compared to a metal ring where $\mu_r = 2000$. The use of a metal ring will be an enhancement to the magnetic flux, as the impermeability of the metal will redirect the magnetic flux inwards. For plastic materials, the same permeability of air (= 1) will be used.


### 5. Result Graphs
Results and derived variables can be interpreted in detail in the "Results" section. An interactive plot is also provided to observe visual adjustments to KV and current density given the variable sliders.

<img src="https://github.com/user-attachments/assets/01664398-71e7-436d-92d2-7f5c4642aafe" width="45%">
<img src="https://github.com/user-attachments/assets/e516549a-44ad-4fc3-b9d5-c9d18847082a" width="45%">

The terminal current $I_term$ can also be adjusted based on expected testing and operating conditions. In the "Results" panel, an interpretation of the phase resistance and current per phase/coil due to configuration parameters are provided.

Peak torque, KV and Kt values are also provided in the "Results" section.








