# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Firefox web browser for Linux

#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from keycode_win_de import Keycode

color=0x8B00FF

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'System', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (color, 'Apps', [Keycode.WINDOWS, 'a']),     
        (color, 'Close', [Keycode.ALT, Keycode.F4]),
        (color, 'Lock', [Keycode.WINDOWS, 'l']), 
        # 2nd row ----------
        (color, 'Disp1', [Keycode.WINDOWS, Keycode.F1]),
        (color, '/\\', [Keycode.UP_ARROW]),
        (color, 'Disp12', [Keycode.WINDOWS, Keycode.F2]),                   
        # 3rd row ----------
        (color, '<', [Keycode.LEFT_ARROW]),
        (color, 'Alt+Tab', [Keycode.ALT, Keycode.TAB ]),
        (color, '>', [Keycode.RIGHT_ARROW]),    
        # 4th row ----------
        (color, 'Terminal', [Keycode.WINDOWS, 't']),
        (color, '\\/', [Keycode.DOWN_ARROW]),
        (color, 'Files', [Keycode.WINDOWS, 'e']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
