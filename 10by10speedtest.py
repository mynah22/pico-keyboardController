from machine import Pin as pin 
from time import ticks_ms, ticks_diff
bounceThreshold = 3

r0pin=pin(28, pin.OUT, pin.OPEN_DRAIN)
r1pin=pin(27, pin.OUT, pin.OPEN_DRAIN)
r2pin=pin(26, pin.OUT, pin.OPEN_DRAIN)
r3pin=pin(22, pin.OUT, pin.OPEN_DRAIN)
r4pin=pin(21, pin.OUT, pin.OPEN_DRAIN)
r5pin=pin(20, pin.OUT, pin.OPEN_DRAIN)
r6pin=pin(19, pin.OUT, pin.OPEN_DRAIN)
r7pin=pin(18, pin.OUT, pin.OPEN_DRAIN)
r8pin=pin(17, pin.OUT, pin.OPEN_DRAIN)
r9pin=pin(16, pin.OUT, pin.OPEN_DRAIN)

rows = (r0pin, r1pin, r2pin, r3pin, r4pin, r5pin, r6pin, r7pin, r8pin, r9pin)
totalRows = len(rows)
poweredRow= -1

#c0=r, c1=g, c2=y
c0pin=pin(0, pin.IN, pin.PULL_UP)
c1pin=pin(1, pin.IN, pin.PULL_UP)
c2pin=pin(2, pin.IN, pin.PULL_UP)
c3pin=pin(3, pin.IN, pin.PULL_UP)
c4pin=pin(4, pin.IN, pin.PULL_UP)
c5pin=pin(5, pin.IN, pin.PULL_UP)
c6pin=pin(6, pin.IN, pin.PULL_UP)
c7pin=pin(7, pin.IN, pin.PULL_UP)
c8pin=pin(8, pin.IN, pin.PULL_UP)
c9pin=pin(9, pin.IN, pin.PULL_UP)

collumnPins = (c0pin, c1pin, c2pin, c3pin, c4pin, c5pin, c6pin, c7pin, c8pin, c9pin)
totalCollumns=len(collumnPins)

class Key:
    def __init__(self, id):
        self.id = id
        self.state=False
        self.changeCounter=0
        self.previousState=False


c0Buttons = (Key('1'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c1Buttons = (Key('2'),Key('5'),Key('8'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c2Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c3Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c4Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c5Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c6Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c7Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c8Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))
c9Buttons = (Key('3'),Key('6'),Key('9'),Key('4'),Key('7'),Key('4'),Key('7'),Key('4'),Key('7'),Key('5'))

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
            rows[currentRow].off()
        else:
            rows[currentRow].on()
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
        readKeyStatus= not bool(collumnPins[currentCollumn].value())
        currentKey=collumnButtons[currentCollumn][poweredRow]
        if readKeyStatus == currentKey.previousState:
            if readKeyStatus != currentKey.state:
                currentKey.changeCounter += 1
                if currentKey.changeCounter > bounceThreshold:
                    currentKey.state = readKeyStatus
                    if currentKey.state:
                        print(currentKey.id+" Down")
                    else:
                        print(currentKey.id+" Up")
        else:
            currentKey.previousState = readKeyStatus
            currentKey.changeCounter = 0

        currentCollumn += 1

#Begin Main Loop
totalcycles=20000
cycle = totalcycles
stick = ticks_ms()
while cycle:
    poweredRowCycle()
    readCollumns()
    cycle -= 1
timeelapsed=ticks_diff(ticks_ms(), stick)
print(str(timeelapsed/totalcycles)+"ms / cycle, "+str(1/(timeelapsed/totalcycles)*1000)+" cycles per second")