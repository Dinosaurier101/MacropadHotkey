import storage
import board, digitalio
import storage

########################
# rename CIRCUITPY drive
########################

new_name = "Macropad"
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = new_name
storage.remount("/", readonly=True)


##############################################
# disable usb drive when button is not pressed
##############################################

#button = digitalio.DigitalInOut(board.KEY12)
#button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
#if button.value:
   #storage.disable_usb_drive()
   
##############################################
#disable autoreload to prevent resetting
##############################################  
#import supervisor

#supervisor.disable_autoreload()
