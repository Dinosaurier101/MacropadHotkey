import time
import os
import displayio
import terminalio
import supervisor

from adafruit_macropad import MacroPad
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label


### user defined

# select your keyboard layout:
# https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
# also add the keycode_... to your macros if they use Keycode.* values
## QWERTY
# none needed. already included in MacroPad. comment out the rest.
## win_de (QWERTZ)
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
## win_fr (AZERTY)
# from keyboard_layout_win_fr import KeyboardLayout
# from keycode_win_fr import Keycode

pressed_color = 0xffffff    # led color of the pressed key
MACRO_FOLDER = '/macros'    # folder where macro files are stored
brightness = 0.1            # overall led pixel brightness


### functions
def set_pixels(keynum):     # set pixel to background color. -1 for all.
    if keynum < 0:
        i = 0
        while i < 12:
            macropad.pixels[i] = colors[i]
            i = i + 1
    else:
        macropad.pixels[keynum] = colors[keynum]

    macropad.pixels.show()

def keypress(keynum):       # handle key presses

    macropad.pixels[keynum] = pressed_color

    function = funcs[keynum]

    # keys[keynum] is an arbitrary-length list, each item is one of:
    # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
    # Negative integer: (absolute value) key released
    # Float (e.g. 0.25): delay in seconds
    # String (e.g. "Foo"): corresponding keys pressed & released
    # List []: one or more Consumer Control codes (can also do float delay)
    # Dict {}: mouse buttons/motion (might extend in future)
    for item in keys[keynum]:
        if isinstance(item, int):
            if item >= 0:
                macropad.keyboard.press(item)
            else:
                macropad.keyboard.release(-item)
        elif isinstance(item, float):
            time.sleep(item)
        elif isinstance(item, str):
            macropad.keyboard_layout.write(item)
        elif isinstance(item, list):
            for code in item:
                if isinstance(code, int):
                    macropad.consumer_control.release()
                    macropad.consumer_control.press(code)
                if isinstance(code, float):
                    time.sleep(code)
        elif isinstance(item, dict):
            if 'buttons' in item:
                if item['buttons'] >= 0:
                    macropad.mouse.press(item['buttons'])
                else:
                    macropad.mouse.release(-item['buttons'])
            macropad.mouse.move(item['x'] if 'x' in item else 0,
                                item['y'] if 'y' in item else 0,
                                item['wheel'] if 'wheel' in item else 0)
            if 'tone' in item:
                if item['tone'] > 0:
                    macropad.stop_tone()
                    macropad.start_tone(item['tone'])
                else:
                    macropad.stop_tone()
            elif 'play' in item:
                macropad.play_file(item['play'])

    if isinstance(function, str):
        #print('str: ', function)
        exec(function)
    if isinstance(function, list):
        #print('list: ',function)
        for item in function:
            #print(item)
            exec(item)

def keyrelease(keynum):     # handle key releases

    set_pixels(keynum)

    for item in keys[keynum]:
        if isinstance(item, int):
            if item >= 0:
                macropad.keyboard.release(item)
        elif isinstance(item, dict):
            if 'buttons' in item:
                if item['buttons'] >= 0:
                    macropad.mouse.release(item['buttons'])
            elif 'tone' in item:
                macropad.stop_tone()
    macropad.consumer_control.release()

def set_brightness():       # set brightness of pixels and handle stealth mode
    global last_brightness
    global brightness
    last_brightness = brightness
    if brightness > 1:
        brightness = 1
    if brightness < 0:
        brightness = 0
    if dim == 1:
        macropad.pixels.brightness = 0
    else:
        macropad.pixels.brightness = brightness
    macropad.pixels.show()

def switch():               # handle switching between apps 
    global app_name         # global to make it accessable for use in macro-functions
    # clear and then read colors, labels, keys, functions from apps
    colors.clear()
    labels.clear()
    keys.clear()
    funcs.clear()

    app_name = apps[app_num]['name']    # app name as displayed on the top row

    a = 0
    while a < 12:   # split apps[] into smaller, more managable pieces
        colors.append(apps[app_num]['macros'][a][0])    # explanation for apps[]... see 'initialisation' section
        labels.append(apps[app_num]['macros'][a][1])
        keys.append(apps[app_num]['macros'][a][2])
        try:
            funcs.append(apps[app_num]['macros'][a][3])
        except:     # enables compatibility with macros without functions (like the original Hotkeys firmware from Adafruit)
            funcs.append('')
        a = a + 1

    # set pixel colors, labels
    set_pixels(-1)

    group[13].text = app_name
    for i in range(12):
        group[i].text = labels[i]

    macropad.keyboard.release_all()
    macropad.consumer_control.release()
    macropad.mouse.release_all()
    macropad.stop_tone()
    macropad.display.refresh()

def import_apps():          # import macros from 'MACRO_FOLDER'
    apps.clear()
    files = os.listdir(MACRO_FOLDER)
    files.sort()
    for filename in files:
        if filename.endswith('.py') and not filename.startswith('._'):
            try:    #read all macros from their files and store in 'apps'
                module = __import__(MACRO_FOLDER + '/' + filename[:-3])
                apps.append(module.app)     # module.app is the dict containing the macro
            except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                    IndexError, TypeError) as err:
                print("ERROR in", filename)
                import traceback
                traceback.print_exception(err, err, err.__traceback__)
    if not apps:
        group[13].text = 'NO MACRO FILES FOUND'
        macropad.display.refresh()
        while True:
            pass

def display_setup():        # set up display groups
    global group
    group = displayio.Group()
    for key_index in range(12):
        x = key_index % 3
        y = key_index // 3
        group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                                anchored_position=((macropad.display.width - 1) * x / 2,
                                                    macropad.display.height - 1 -
                                                    (3 - y) * 12),
                                anchor_point=(x / 2, 1.0)))
    group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
    group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                            anchored_position=(macropad.display.width//2, -2),
                            anchor_point=(0.5, 0.0)))
    macropad.display.show(group)


### initialisation
try:
    macropad = MacroPad(layout_class=KeyboardLayout, keycode_class=Keycode)
except:
    macropad = MacroPad()

macropad.display.auto_refresh = False   # don't automatically update screen to prevent flickering

dim = 0         # dim = 1 allows to disable key illumination. set by encoder button.
app_num = 0     # currently selected app/macro

apps = []           # list to store all macros. to access: apps[app number from import]['macros'][key number][0:colors, 1:labels, 2:keys, 3:funcs]
app_name = ()       # variable to store the currently loaded macro name
colors = []         # list to store the pixel colors of the selected macro
labels = []         # list to store the key labels of the selected macro
keys = []           # list to store the key sequences of the selected macro
funcs = []          # list to store the functions of the selected macro


import_apps()

display_setup()

set_brightness()

switch()


# Main Loop
while True:

    set_brightness()

    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        if dim == 0:
            dim = 1
        elif dim == 1:
            dim = 0

    # switch selected app/macro when encoder position changes
    app_num_last = app_num
    app_num = macropad.encoder % len(apps)
    if app_num != app_num_last:
        switch()

    # handle key presses
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            keypress(key_event.key_number)

        if key_event.released:
            keyrelease(key_event.key_number)
