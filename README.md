# MacropadHotkey
My own implementation of the [Macropad-Hotkeys](https://learn.adafruit.com/macropad-hotkeys/overview) firmware for Adafruit Macropad.
For use with [CircuitPython](https://github.com/adafruit/circuitpython).

## Features
- Compatible with original Macropad-Hotkey macros
- Option to have functions in macros
- Support for multiple [keyboard layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts) (QWERTY, QWERTZ, AZERTY) and possibility to add more

## How to use functions
  Simply add your function to the end of each button macro:  
  as a string:   `(color, 'label', 'key sequence', 'function1')`  
  or as a list:  `(color, 'label', 'key sequence', ['function1', 'function2', 'more functions...'])`  
  Examples can be found in the [Example Macro](https://github.com/Dinosaurier101/MacropadHotkey/blob/master/macros/example.py).
