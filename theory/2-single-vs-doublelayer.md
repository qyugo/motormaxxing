# **Single vs. Double Layer Winding Configs**

While researching motor construction, oftentimes I found that concepts were seemingly kept behind a layer of abstraction, whether it be intuitive for the motor overlords or a trade secret, as Hanselman himself acknowledged, but either way, there is a lack of a coherent explanation for what motor windings actually constitute.

Therefore, I will attempt clarify all confusion that led to my own understanding. 

The first concept is that of stator **slots** and **teeth**. It may seem simple, but online resources for winding configurations can be inconsistent in which they refer to, and it can generate a lot of confusion for those who are new to the subject.

<img src="https://github.com/user-attachments/assets/ed6a0b57-fbf0-42da-bda1-fc8780ddaa1e" width="30%"> 

Simply put, teeth are what the coils actually wrap around, while slots are the empty space in between. For one, it is worth understanding there is the same number of slots as there are teeth for a given stator.*

*The structure with slots/teeth that have coils winding around them is always the **stator** in BLDC motors.


## Single vs. Double Layer Winding Configurations

You might have seen 'single layer' and 'double layer' configurations mentioned. However, it is easy to get confused when the descriptions refer to that of the teeth, or the slots, since it's different.

If you attempt to look up what constitutes a "single layer" winding, most sources will describe something along the lines of "there is only one coil side per stator slot." While a double layer winding contains "two coil sides (top and bottom) per stator slot."

While this is correct, this can be confusing since it refers to the _empty space_ between the teeth (slots), and it can be difficult to visualize what's happening with the teeth. A much better way to describe this is the following, as it's much more visually intuitive:

**Single Layer:** In order for there to only be one 'coil side' per stator slot, half of the actual stator _teeth_ are empty.
**Double Layer:** All stator teeth are wrapped in coils, resulting in the 'two coil sides' per slot. 

Therefore, the 'single' and 'double' layer actually refers to is how many layers of windings are in the slots, not the teeth.

Here is a drawing that can help understand the picture:

<img src="https://github.com/user-attachments/assets/02c7d839-e049-4142-9c1f-fae8c39be30e" width="50%">

With each black box being a tooth, and the blue lines being the presence of a stator coil, you can see that single layer is much better represented as "every other stator tooth is empty."

As we can see, the most common construction of BLDC motors is actually double layer, where all of the stator teeth are wrapped. Therefore, this assumption of a double layer winding is used in the calculations in this repository.

### The Path of the Three Phases
How then do the three phases actually orient themselves in a double layer winding?
Using the **BLDC Winding** visualizer from _hlaboratories.com_, using this repo's example of a 8110, 36N42P outrunner BLDC motor, we can visualize the following:

<img width="528" height="514" alt="Screenshot 2026-09-08 at 12 53 52 PM" src="https://github.com/user-attachments/assets/003043ae-29ed-478c-be52-63af2c836059" />

Each of the 36 teeth are wound, so we can assume double-layer. 
The calculator presents a letter-type description of the **teeth** denoting phases A, B, C (+), and a lowercase a, b, and c (-) being opposite direction to it's same-letter counterpart, as shown by the following:

<img width="974" height="162" alt="Screenshot 2026-09-08 at 1 09 19 PM" src="https://github.com/user-attachments/assets/fe301c21-77ea-44b5-ab12-0b2ca066df5e" />

We can understand now that a clockwise and a counterclockwise winding of each phase is placed adjacent to one another, with a space of 4 slots between each Xx pair, to allow for two more pairs of the remaining phases.

It doesn't matter if + or - is clockwise or counterclockwise per se, but they must be opposite to each other and consistent across all windings.

Here I have wound one A phase on an empty stator with 36 teeth, for a more practical visualization:

**_Double Layer Config:_**

<img src="https://github.com/user-attachments/assets/8cd07fa5-f778-471f-b842-35365dd99a58" width="50%"> 
<img src="https://github.com/user-attachments/assets/6c4fa08e-212e-40e1-ba08-10ce7e5e6c81" width="45%"> 

We can see visually the clockwise-counterclockwise pair of one phase being adjacent, resulting in "two coil sides (top and bottom) per stator slot." In other words, the space between two neighboring teeth will contain two windings. 

Although, I still think this is a bad descriptor presented by Google articles. As phase B is wound in following phase A, you'll see the A- and the B- (or lowercase a and b) are adjacent, so it is not an alternating clockwise-counterclockwise winding [+ - + - + - + - ...], but rather a [+ + - - + + - - ...]

**Confusion: Slot Winding Descriptor vs. Teeth Winding Descriptor**

Possible confusion is if you come across a similar letter-based descriptor as provided above (using A, a, B, b, C, c) that describes each _slot_ instead of each _tooth_. Here is a slot descriptor of a single-layer and a double-layer winding:

<img width="664" height="159" alt="Screenshot 2026-09-08 at 1 27 39 PM" src="https://github.com/user-attachments/assets/bf0911c5-9659-4a92-8632-f3fe7cda722d" />

If you notice, the _single layer **slot** descriptor_ looks like the _double layer **teeth** descriptor_ (AabBCc...).















