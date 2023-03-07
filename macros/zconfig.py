#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values  # use this for QWERTY
#from keycode_win_de import Keycode                                             # use this for QWERTZ
#from keycode_win_fr import Keycode                                             # use this for AZERTY

color=0xFFFFFF

app = {                       
    'name' : 'Config', 
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE    FUNCTION(optional)
        # 1st row ----------
        (color, 'Bri -', '', 'brightness = brightness - 0.05'),     
        (color, 'reset', '', 'brightness = brightness_default'),
        (color, 'Bri +', '', 'brightness = brightness + 0.05'), 
        # 2nd row ----------
        (color, '', ''),
        (color, '', ''),
        (color, '', ''),                   
        # 3rd row ----------
        (color, '', ''),
        (color, '', ''),
        (color, '', ''),    
        # 4th row ----------
        (color, '', ''),
        (color, '', ''),
        (color, '', ''),
    ]
}
