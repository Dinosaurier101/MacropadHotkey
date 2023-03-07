#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values  # use this for QWERTY
from keycode_win_de import Keycode                                              # use this for QWERTZ
from adafruit_hid.consumer_control_code import ConsumerControlCode

color=0x090909

app = {               
    'name' : 'Media', # Name of the Macro. Gets shown on the display.
    'macros' : [      
        # COLOR    LABEL    KEY SEQUENCE    FUNCTION(optional)
        # 1st row ----------
        (color, '', []),
        (color, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        (color, 'Bright+', [[ConsumerControlCode.BRIGHTNESS_INCREMENT]]),
        # 2nd row ----------
        (color, '', []),
        (color, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (color, 'Bright-', [[ConsumerControlCode.BRIGHTNESS_DECREMENT]]),
        # 3rd row ----------
        (color, '', []),
        (color, 'Mute', [[ConsumerControlCode.MUTE]]),
        (color, '', []),
        # 4th row ----------
        (color, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (color, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (color, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
