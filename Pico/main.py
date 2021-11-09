print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP0, board.GP1, board.GP2)
keyboard.col_pins = (board.GP28, board.GP27, board.GP26)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.N1, KC.N4, KC.N7,
     KC.N2, KC.N5, KC.N8, 
     KC.N3, KC.N6, KC.N9,],
]

if __name__ == '__main__':
    keyboard.go()