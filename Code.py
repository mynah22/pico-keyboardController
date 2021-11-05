import board
from digitalio import DigitalInOut, Direction, DriveMode, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from usb_hid import devices
kb=Keyboard(devices)

#keycode aliases
ALT=Keycode.ALT
TAB=Keycode.TAB
THREE=Keycode.THREE
FOUR=Keycode.FOUR
FIVE=Keycode.FIVE
SIX=Keycode.SIX
SEVEN=Keycode.SEVEN
EIGHT=Keycode.EIGHT
NINE=Keycode.NINE
#end keycode aliases

#"row" (output) pins and related variables set up 
r0pin = DigitalInOut(board.GP28); r0pin.direction = Direction.OUTPUT; r0pin.drive_mode = DriveMode.OPEN_DRAIN
r1pin = DigitalInOut(board.GP27); r1pin.direction = Direction.OUTPUT; r1pin.drive_mode = DriveMode.OPEN_DRAIN
r2pin = DigitalInOut(board.GP26); r2pin.direction = Direction.OUTPUT; r2pin.drive_mode = DriveMode.OPEN_DRAIN
rows = (r0pin, r1pin, r2pin)
totalRows = len(rows)
poweredRow=0
#end rows


#c0=r, c1=g, c2=y
#collumns and related set up
c0pin = DigitalInOut(board.GP0); c0pin.direction = Direction.INPUT; c0pin.pull = Pull.UP
c1pin = DigitalInOut(board.GP1); c1pin.direction = Direction.INPUT; c1pin.pull = Pull.UP
c2pin = DigitalInOut(board.GP2); c2pin.direction = Direction.INPUT; c2pin.pull = Pull.UP
collumnPins = (c0pin, c1pin, c2pin)
totalCollumns=len(collumnPins)
#end collumns


class Key:
    def __init__(self, kcode):
        self.kcode = kcode
        self.state=False
        self.changeCounter=0
        self.previousState=False


c0Buttons = (Key(ALT),Key(FOUR),Key(SEVEN))
c1Buttons = (Key(TAB),Key(FIVE),Key(EIGHT))
c2Buttons = (Key(THREE),Key(SIX),Key(NINE))
collumnButtons = (c0Buttons, c1Buttons, c2Buttons)


bounceThreshold = 5


def poweredRowCycle():
    global rows
    global poweredRow
    global totalRows
    if poweredRow < (totalRows-1):
        poweredRow += 1
    else:
        poweredRow = 0

    currentRow=0
    while currentRow < totalRows:
        if currentRow == poweredRow:
            rows[currentRow].value=0
        else:
            rows[currentRow].value=1
        currentRow += 1


def readCollumns():
    global poweredRow
    global collumnButtons
    global collumnPins
    global totalCollumns
    global bounceThreshold

    currentCollumn=0
    while currentCollumn < totalCollumns:
        #readKeyStatus will be "True" when current key is being read as pressed
        readKeyStatus= not bool(collumnPins[currentCollumn].value)
        currentKey=collumnButtons[currentCollumn][poweredRow]

        if readKeyStatus == currentKey.previousState:
            if readKeyStatus != currentKey.state:
                currentKey.changeCounter += 1
                if currentKey.changeCounter > bounceThreshold:
                    currentKey.state = readKeyStatus
                    if currentKey.state:
                        kb.press(currentKey.kcode)
                        print(currentKey.kcode)
                    else:
                        kb.release(currentKey.kcode)
                        print('released')

        else:
            currentKey.previousState = readKeyStatus
            currentKey.changeCounter = 0

        currentCollumn += 1
print('loaded')
#Begin Main Loop
while True:
    poweredRowCycle()
    readCollumns()
