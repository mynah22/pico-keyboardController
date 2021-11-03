from machine import Pin as pin 
from time import sleep_ms

bounceThreshold = 5

r0pin=pin(28, pin.OUT, pin.OPEN_DRAIN)
r1pin=pin(27, pin.OUT, pin.OPEN_DRAIN)
r2pin=pin(26, pin.OUT, pin.OPEN_DRAIN)
rows = (r0pin, r1pin, r2pin)
totalRows = len(rows)
poweredRow=0

#c0=r, c1=g, c2=y
c0pin=pin(0, pin.IN, pin.PULL_UP)
c1pin=pin(1, pin.IN, pin.PULL_UP)
c2pin=pin(2, pin.IN, pin.PULL_UP)
collumnPins = (c0pin, c1pin, c2pin)
totalCollumns=len(collumnPins)

class Key:
    def __init__(self, id):
        self.id = id
        self.state=False
        self.changeCounter=0
        self.previousState=False


c0Buttons = (Key('1'),Key('4'),Key('7'))
c1Buttons = (Key('2'),Key('5'),Key('8'))
c2Buttons = (Key('3'),Key('6'),Key('9'))
collumnButtons = (c0Buttons, c1Buttons, c2Buttons)





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
while True:
    readCollumns()
    poweredRowCycle()