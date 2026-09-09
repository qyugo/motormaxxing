# Delta vs. Wye Configuration

Unlike a single-phase brushed motor, most BLDCs involve three distinct motor phases that are wired in a 120 degree orientation. 
The pattern in which the three-phase coil windings are wired on a motor can adjust its performance. 

The distinction between delta and wye is the pattern in which the three motor phases are wired together at its termination point. A delta configuration effectively wires the phases in parallel, while the star configuration functions as a series connection, as the phases are tied together at a neutral endpoint, separate from the input.

<img src="https://github.com/user-attachments/assets/a3393c5f-cf1a-4d15-93c4-23dcecef7c53" width="45%"> 
<img src="https://github.com/user-attachments/assets/37b9b77b-138d-42c6-960e-cfd1b112e25b" width="47%"> 

## Voltage and Current Characteristics

In a star winding, each of the three phases sees a fraction of the total motor voltage:
$V_{line, star} = \sqrt{3} * V_{phase}$

While a delta winding sees the full phase voltage:
$V_{line, delta} = V_{phase}$

Conversely, the entire phase current goes through each star winding, while a fraction of it goes through a delta winding:

$I_{line, star} = I_{phase}$
$I_{line, delta} = \sqrt{3} * I_{phase}$

## Performance Characteristics

Delta configurations provide better torque efficiency at a high speed and high power. Star configurations involve a neutral point, and less phase current, while delta configurations involve higher phase current and thus higher heat concentration.

Wye (also known as Y- or Star) configurations are generally suitable for low-speed applications, as its efficiency is higher at a low RPM. 

