# Pokemon-Trader-Code

This repository holds the key parts to use an Arduino as a trading partner for Generation 2 Pokemon games. The "ArduinoGen2" folder has the Arduino code, and the "Pokemon Builder Code" folder has the Python code.

# Required Hardware

1. Arduino (I used Uno R4 WiFi)
2. GBA (Gameboy Advance) or GBC (Gameboy Color) port (The GBC cable fits in the GBA port)
3. GBC link cable (This is NOT the same as the GBA cable. A GBA cable will NOT work.)
4. 3 1000 ohm resistors
5. 4 jumper wires
6. Pokemon Silver or Pokemon Gold
7. GBC, GBA, or GBA SP

# Required Software

1. Arduino IDE
2. Something to run Python (I used Spyder in Anaconda)

# Usage

Python:
1. Open Spyder and open the "Pokemon Builder.py" file.
2. Run the file and follow the prompts. The code is built for Generations 1-5, BUT ONLY GEN 2 IS FUNCTIONAL. The inputs are specific, so double-check your spelling. 
3. Copy the "output_gen2.h" and paste it into the "ArduinoGen2" folder

Arduino:
1. Open the Arduino IDE and open the ArduinoGen2.ino file.
2. At the top you can "#include" whichever pokemon set you would like. Each file has a list of the included Pokemon at the top.
3. Upload the ArduinoGen2.ino code onto your Arduino.
4. Turn on your Gameboy device.
5. Enter the Pokemon Center, go upstairs, and enter the trading room as normal.
6. The Arduino will select the Pokemon to trade that is in the same party spot as the Pokemon you chose. For example, if you chose the 3rd pokemon in your party, then the Arduino will choose the 3rd Pokemon in its party. You can rearrange your Pokemon as needed in the Trading Room before interacting with the trading desk. There is an exception to the rule. If the Pokemon you chose is further down than the Arduino party has available Pokemon, then the Arduino will choose the last Pokemon in its party. For example, if you chose the 5th Pokemon, but the Arduino party only has 2, then the Arduino will choose the the second (its last) Pokemon.
7. When you leave the Trading Room, you will lose the Pokemon in the Arduino party.
8. After leaving the Trading Room, reset the Arduino, or it will not let you in the Trading Room.

# Notes

1. I have only tested the process with an Arduino Uno R4 WiFi. I believe other Arduinos should work, but I do not know for sure.
2. I tested with Pokemon Silver. Everything should work for Gold, but for Crystal, I am not sure. I would test the other games, but I do not want to drop $200. 


