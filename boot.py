from usb_midi import disable as mididisable
from usb_cdc import disable as consoledisable
from digitalio import DigitalInOut, Direction, DriveMode, Pull
from storage import disable_usb_drive as massstoragedisable
from board import GP21

mididisable()

# jumper / button gp20 to gp21 
accessButton = DigitalInOut(GP21); accessButton.direction = Direction.INPUT; accessButton.pull = Pull.UP

# Disable devices only if button is not pressed.
if accessButton.value:
	massstoragedisable()
	consoledisable()