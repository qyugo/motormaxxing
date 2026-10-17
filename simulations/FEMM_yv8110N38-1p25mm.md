# FEMM vs. Analytical vs. Experimental for PETG Motor

Version: YV8110, N38 NdFeB magnets, 1.25mm airgap, PETG backiron. 

First, the rotor was redrawn in FEMM to change the backiron material to air (as the magnetic permeability for PETG is essentially the same).

The magnets are also slightly smaller, with a 2.5mm thickness compared to the N42 magnets, and a narrower width of 4.5mm. The new rotor with alternating N38 magnets was drawn using Python around the stator, which remains the same.

<img width="942" height="579" alt="Screenshot 2026-10-17 at 2 34 54 PM" src="https://github.com/user-attachments/assets/b91afcdf-33ba-4bf5-af5d-0f82fbdec149" />

Visible in the FEMM solver that the lack of a back-iron causes the motor flux to go outwards. 

<img width="710" height="629" alt="Screenshot 2026-10-17 at 3 00 19 PM" src="https://github.com/user-attachments/assets/cfb3d404-6426-4691-baf3-8e36a5af003c" />
<img width="808" height="766" alt="Screenshot 2026-10-17 at 2 59 52 PM" src="https://github.com/user-attachments/assets/02f0a659-d694-46c0-8d86-55c29f5ad8ad" />
