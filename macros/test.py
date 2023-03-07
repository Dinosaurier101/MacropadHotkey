#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from keycode_win_de import Keycode


app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Test', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FF00, 'Key', '0'),
        (0x00FF00, '2Func', '', ['print("Func0")', 'print("Func1")']),
        (0x00FF00, '2Key', ['Key', 1.0,'2'], ''),
        # 2nd row ----------
        (0x00FF00, 'bri-', '', ['brightness = brightness - 0.1', 'print(brightness)']),
        (0x00FF00, 'bri+', '', ['brightness = brightness + 0.1', 'print(brightness)']),
        (0x00FF00, 'bri0.1', '', 'brightness = 0.1'),
        # 3rd row ----------
        (0x00FF00, '6', ['Key','6'], 'print("Func0")'),  
        (0x00FF00, '7', ['Key','7'], 'print("Func0")'),
        (0x00FF00, '8', ['Key','8'], 'print("Func0")'),
        # 4th row ----------
        (0x00FF00, '9', ['Key','9'], 'print("Func0")'),      
        (0x00FF00, '10', ['Key','10'], 'print("Func0")'), 
        (0x00FF00, '11', ['Key','11'], 'print("Func0")'),          
    ]
}
