# Finite Element Method Magnetics (FEMM) 2D Simulation

<img width="786" height="678" alt="IMG_4128" src="https://github.com/user-attachments/assets/693b72cf-29ac-40c4-859d-2ada0fe9b138" />


In conjunction with my analytical model, I wanted to have a numerical model as well. David Meeker's FEMM allows for a 2D simulation for calculating airgap flux density, torque (and cogging torque by a spinning Lua script), flux linkage, and back-EMF. 

Both analytical model (my Python UI), the FEMM simulation, and experimental characterization using my dynos will support the creation of these motors, and be improved periodically.

Limitations of the FEMM model:

There will inevitably be some error from FEMM since it is in 2D, so end effects and axial leakage, so errors will be more apparent for shorter stack lengths (thinner motors).

OnShape Model:
<img width="955" height="745" alt="Screenshot 2026-10-16 at 12 39 53 PM" src="https://github.com/user-attachments/assets/dfdcbe1a-02fb-480e-bec1-cce122ddb903" />

Material: M19 Stator Laminations
<img width="551" height="498" alt="Screenshot 2026-10-16 at 1 29 58 PM" src="https://github.com/user-attachments/assets/0ec79f57-00fd-4161-a54a-57f4f4541d48" />

I generated the rest of the rotor and magnets using Python, so further adjustments to magnet strength and dimensions, airgap, and rotor back-iron thickness can be quickly tested, while the stator remains the same.

<img width="816" height="678" alt="Screenshot 2026-10-16 at 1 47 56 PM" src="https://github.com/user-attachments/assets/ca3f652f-e714-4417-97ea-39f4640afe6d" />

<img width="886" height="691" alt="Screenshot 2026-10-16 at 2 01 41 PM" src="https://github.com/user-attachments/assets/60acae5b-52ca-4bb1-98ee-51593dd89af5" />

Correct winding directions of A,B, and C phases wound using AabBCcaABbcC [etc...] are programmed into the python script.

Magnetic Meshing

<img width="771" height="589" alt="Screenshot 2026-10-16 at 2 05 47 PM" src="https://github.com/user-attachments/assets/681892f5-b385-435b-b1f5-0a3d65c07777" />


Static analysis
<img width="847" height="759" alt="Screenshot 2026-10-16 at 2 21 52 PM" src="https://github.com/user-attachments/assets/57a2e2cc-226f-4504-80ad-a9e601125107" />


