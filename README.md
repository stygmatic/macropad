Meddys macropad


This macropad is a 4 key macropad with an OLED Display
I will use it on my pc to control my spotify and mic settings as well as display music info. It also has 4 neopixels which will light up every time i press a key.

Features:
It will be printed in a translucent green filament like my rocket
128x32 OLED Display
4 Keys
4 neopixels

The case is 1 piece and the pcb should be able to slide into the case and still be screwed in nicely

Schematic

<img width="775" alt="Screenshot 2025-07-04 at 12 26 22 AM" src="https://github.com/user-attachments/assets/92aef736-f040-4f1e-a4d1-547678cf2afd" />


My case, made in OnShape

<img width="758" alt="Screenshot 2025-07-04 at 12 50 18 AM" src="https://github.com/user-attachments/assets/1cc440b7-db19-4999-ad11-b89441874f01" />

PCB
My pcb was made in kicad, which ive been using for everything :D


<img width="836" alt="Screenshot 2025-07-04 at 12 26 58 AM" src="https://github.com/user-attachments/assets/e1432909-da8b-4276-87bd-8cad17e96e43" />


I used MX_V2 for the keyswitch footprints. I think in retrospect, I should've added a ground plane

Firmware Overview
This hackpad uses QMK firmware.

The macropad has 4 keys which will be used as my push to talk key, and then the next, previous, and pause/resume for my spotify.
The oled will display the current song playing(still have to figure out the firmware for that)

BOM:

4x Blue MX Switches(I already have)

4x Keycaps

3x 3.2mm screws

2X 3.2mm Bolts

4X capacitors.

4X Neopixels

1x 0.96" OLED Display

1x XIAO RP2040

1x Case

I like rockets
