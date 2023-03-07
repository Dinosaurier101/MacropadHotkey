#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values  # use this for QWERTY
from keycode_win_de import Keycode                                              # use this for QWERTZ
#from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Firefox', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE    FUNCTION(optional)
        # 1st row ----------
        (0xFF4E00, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB], ''),
        (0xFF0000, 'X', [Keycode.CONTROL, 'w'], ''),
        (0xFF4E00, 'Tab >', [Keycode.CONTROL, Keycode.TAB], ''),
        # 2nd row ----------
        (0xFF4E00, '< Back', [Keycode.CONTROL, '['], ''),
        (0xFF4E00, 'Reload', [Keycode.CONTROL, 'r'], ''),
        (0xFF4E00, 'Fwd >', [Keycode.CONTROL, ']'], ''),
        # 3rd row ----------
        (0xFF4E00, 'Find', [Keycode.CONTROL, 'f'], ''),  
        (0xFF4E00, '', [], ''),
        (0xFF4E00, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p'], ''),
        # 4th row ----------
        (0xFF4E00, 'New', [Keycode.CONTROL, 't'], ''),      #New Tab
        (0xFF4E00, 'DDG', [Keycode.CONTROL, 't', -Keycode.CONTROL, 'https://duckduckgo.com\n'], ''), 
        (0xFF4E00, 'Github', [Keycode.CONTROL, 't', -Keycode.CONTROL, 'https://github.com/Dinosaurier101/MacropadHotkey\n'], ''),          
    ]
}
