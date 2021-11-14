import supervisor

supervisor.set_next_stack_limit(4096 + 4096)


#####   My boot.py : disable midi, repl and mass storage unless button pressed
#from usb_midi import disable as mididisable
#from usb_cdc import disable as consoledisable
#from digitalio import DigitalInOut, Direction, DriveMode, Pull
#from storage import disable_usb_drive as massstoragedisable
#from board import GP28
#
#mididisable()
#
## button gp28 at boot will allow access to repl and files
#accessButton = DigitalInOut(GP28); accessButton.direction = Direction.INPUT; accessButton.pull = Pull.UP
#
## Disable devices only if button is not pressed.
#if accessButton.value:
#    massstoragedisable()
#    consoledisable()