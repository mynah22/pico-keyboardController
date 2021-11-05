import board
from digitalio import DigitalInOut, Direction, DriveMode, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from usb_hid import devices
from time import monotonic, time
bounceThreshold = 3
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

r0pin = DigitalInOut(board.GP28); r0pin.direction = Direction.OUTPUT; r0pin.drive_mode = DriveMode.OPEN_DRAIN
r1pin = DigitalInOut(board.GP27); r1pin.direction = Direction.OUTPUT; r1pin.drive_mode = DriveMode.OPEN_DRAIN
r2pin = DigitalInOut(board.GP26); r2pin.direction = Direction.OUTPUT; r2pin.drive_mode = DriveMode.OPEN_DRAIN
r3pin = DigitalInOut(board.GP22); r3pin.direction = Direction.OUTPUT; r3pin.drive_mode = DriveMode.OPEN_DRAIN
r4pin = DigitalInOut(board.GP21); r4pin.direction = Direction.OUTPUT; r4pin.drive_mode = DriveMode.OPEN_DRAIN
r5pin = DigitalInOut(board.GP20); r5pin.direction = Direction.OUTPUT; r5pin.drive_mode = DriveMode.OPEN_DRAIN
r6pin = DigitalInOut(board.GP19); r6pin.direction = Direction.OUTPUT; r6pin.drive_mode = DriveMode.OPEN_DRAIN
r7pin = DigitalInOut(board.GP18); r7pin.direction = Direction.OUTPUT; r7pin.drive_mode = DriveMode.OPEN_DRAIN
r8pin = DigitalInOut(board.GP17); r8pin.direction = Direction.OUTPUT; r8pin.drive_mode = DriveMode.OPEN_DRAIN
r9pin = DigitalInOut(board.GP16); r9pin.direction = Direction.OUTPUT; r9pin.drive_mode = DriveMode.OPEN_DRAIN

rows = (r0pin, r1pin, r2pin, r3pin, r4pin, r5pin, r6pin, r7pin, r8pin, r9pin)
totalRows = len(rows)
poweredRow= -1

#c0=r, c1=g, c2=y
c0pin = DigitalInOut(board.GP0); c0pin.direction = Direction.INPUT; c0pin.pull = Pull.UP
c1pin = DigitalInOut(board.GP1); c1pin.direction = Direction.INPUT; c1pin.pull = Pull.UP
c2pin = DigitalInOut(board.GP2); c2pin.direction = Direction.INPUT; c2pin.pull = Pull.UP
c3pin = DigitalInOut(board.GP3); c3pin.direction = Direction.INPUT; c3pin.pull = Pull.UP
c4pin = DigitalInOut(board.GP4); c4pin.direction = Direction.INPUT; c4pin.pull = Pull.UP
c5pin = DigitalInOut(board.GP5); c5pin.direction = Direction.INPUT; c5pin.pull = Pull.UP
c6pin = DigitalInOut(board.GP6); c6pin.direction = Direction.INPUT; c6pin.pull = Pull.UP
c7pin = DigitalInOut(board.GP7); c7pin.direction = Direction.INPUT; c7pin.pull = Pull.UP
c8pin = DigitalInOut(board.GP8); c8pin.direction = Direction.INPUT; c8pin.pull = Pull.UP
c9pin = DigitalInOut(board.GP9); c9pin.direction = Direction.INPUT; c9pin.pull = Pull.UP

collumnPins = (c0pin, c1pin, c2pin, c3pin, c4pin, c5pin, c6pin, c7pin, c8pin, c9pin)
totalCollumns=len(collumnPins)

class Key:
    def __init__(self, kcode):
        self.kcode = kcode
        self.state=False
        self.changeCounter=0
        self.previousState=False


c0Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c1Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c2Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c3Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c4Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c5Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c6Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c7Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c8Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))
c9Buttons = (Key(ALT),Key(FOUR),Key(SEVEN),Key(TAB),Key(SIX),Key(EIGHT),Key(ALT),Key(NINE),Key(THREE),Key(FIVE))

collumnButtons = (c0Buttons, c1Buttons, c2Buttons, c3Buttons, c4Buttons, c5Buttons, c6Buttons, c7Buttons, c8Buttons, c9Buttons)





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

#Begin Main Loop
totalcycles=20000
cycle = totalcycles
print('loaded')
startseconds=time()
stime = monotonic()
while cycle:
    poweredRowCycle()
    readCollumns()
    cycle -= 1
timeelapsed=monotonic()-stime
print(str((timeelapsed/totalcycles)*1000)+"ms / cycle, "+str(1/(timeelapsed/totalcycles))+" cycles per second")
print(str(time()-startseconds)+" seconds elapsed")