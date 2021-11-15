import supervisor

supervisor.set_next_stack_limit(4096 + 4096)


####   My boot.py : disable midi, repl and mass storage unless button pressed
from usb_midi import disable as mididisable
from usb_cdc import disable as consoledisable
from digitalio import DigitalInOut, Direction, Pull
from storage import disable_usb_drive as massstoragedisable
from board import GP28, LED
from time import sleep
mididisable()

# button gp28 at boot will allow access to repl and files
accessButton = DigitalInOut(GP28); accessButton.direction = Direction.INPUT; accessButton.pull = Pull.UP

# Disable devices by default (button not pressed)
if accessButton.value:
    massstoragedisable()
    consoledisable()
else:
    onlight=DigitalInOut(LED)
    onlight.direction=Direction.OUTPUT
    blinkcount=3
    while blinkcount:
        onlight.value=1
        sleep(.1)
        onlight.value=0
        sleep(.1)
        blinkcount-=1