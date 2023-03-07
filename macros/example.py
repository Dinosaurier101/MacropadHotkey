#from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values  # use this for QWERTY
from keycode_win_de import Keycode                                             # use this for QWERTZ
#from keycode_win_fr import Keycode                                             # use this for AZERTY
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

app = {                     # REQUIRED dict, must be named 'app'
    'name' : 'Example',     # Application name
    'macros' : [            # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE    FUNCTION(optional)
        # 1st row ----------
        (0xff0000, 'Key1', 'Quebec Whiskey Zulu Alpha!\n', ''),                                                                     # type 'Quebec Whiskey Zulu Alpha!' (to test if your Keyboard Layout is correctly set) and jump to next line
        (0xff8000, 'Key2', ['Hello ', 1.0, 'World! '], ''),                                                                         # type 'Hello', wait 1s, type 'World!'
        (0xffff00, 'Keycode', [Keycode.WINDOWS, 'e'], ''),                                                                          # press the Windows-Key + 'e'
        # 2nd row ----------
        (0x80ff00, 'Tone1', [{'tone':500}]),                                                                                        # play tone; this key has no FUNCTION to show it can be left out
        (0x00ff00, 'Tone2', [{'tone':400}, 0.2, {'tone':600}, 0.2, {'tone':800}], ''),                                              # play melody
        (0x00ff80, 'CCC', [[ConsumerControlCode.VOLUME_DECREMENT]], ''),                                                            # decrease your pc's volume
        # 3rd row ----------
        (0x00ffff, 'Mouse1', [{'buttons':Mouse.RIGHT_BUTTON}], ''),                                                                 # click with right mouse button
        (0x0080ff, 'Mouse2', [{'y':50}], ''),                                                                                       # move mouse down
        (0x0000ff, 'Mouse3', [{'wheel':-2}], ''),                                                                                   # scroll down
        # 4th row ----------
        (0x8000ff, 'Func1', '', 'brightness = brightness + 0.1'),                                                                   # increase brightness for key backlight
        (0xff00ff, 'Func2', 'Typing and executing a function!', 'print("Executing a function and typing!")'),                       # typing and printing over serial
        (0xff0080, 'Func3', '', ['brightness = 0.05', 'macropad.red_led = (True if macropad.red_led == False else False)']),        # set brightness to 0.05 and switch the small red led next to the usb port
        ]
}
