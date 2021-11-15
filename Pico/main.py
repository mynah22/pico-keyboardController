print("Starting")

import board
from digitalio import DigitalInOut, Direction

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

onlight=DigitalInOut(board.LED)
onlight.direction=Direction.OUTPUT

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())


keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8,board.GP7, board.GP6, board.GP5, board.GP4,board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.row_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18)
keyboard.diode_orientation = DiodeOrientation.ROW2COL
UNASS=KC.TRNS
NOKEY=KC.TRNS
MOD = KC.MO(1)

#Layer 0
#|......||_ESC__||__1___||__2___||__3___||___4__||__5___||__6___||__7___||__8___||__9___||__0___||_MINS_||_EQUAL||_BKSP_________||_MUTE_|
#|__?___||_TAB______||__Q___||__W___||__E___||__R___||__T___||__Y___||__U___||__I___||__O___||__P___||_LBRC_||_RBRC_||_BSLASH___||_DEL__|
#|__?___||_BKSP_______||__A___||__S___||__D___||__F___||__G___||__H___||__J___||__K___||__L___||SCOLON||_QUOTE|.|______ENTER____||_VOLU_|
#|__?___||_LSHIFT_________|.|__Z___||__X___||__C___||__V___||__B___||__N___||__M___||_COMMA||_DOT__||_SLASH|  |_RSHIFT|  |__UP__||_VOLD_|
#|__?___||_LCTRL__||_LWIN___||_LALT___||......||......||......||_SPACE||......||......||......||_RCTRL||LAYER1|  |_LEFT_||_DOWN_||_RIGHT|
#Layer 1
#|......||_TILDE||______||______||______||______||______||______||______||______||______||______||______||______||______________||_PLAY_|
#|______||__________||______||______||______||______||______||______||______||______||______||______||______||______||__________||______|
#|______||_CAPS_______||______||______||______||______||______||______||______||______||______||______||______|.|_______________||______|
#|______||________________|.|______||______||______||______||______||______||______||______||______||______|  |_______|  |_PGUP_||______|
#|______||________||________||________||......||......||......||______||......||......||......||______||______|  |_HOME_||_PGDN_||_END__|
#Layer 2
#|......||______||______||______||______||______||______||______||______||______||______||______||______||______||______________||______|
#|______||__________||______||______||______||______||______||______||______||______||______||______||______||______||__________||______|
#|______||____________||______||______||______||______||______||______||______||______||______||______||______|.|_______________||______|
#|______||________________|.|______||______||______||______||______||______||______||______||______||______|  |_______|  |______||______|
#|______||________||________||________||......||......||......||______||......||......||......||______||______|  |______||______||______|


keyboard.keymap = [
    [NOKEY, KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQUAL, KC.BKSP, KC.MUTE,
     UNASS, KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLASH, KC.DEL,
     UNASS, KC.BKSP, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, NOKEY, KC.ENTER, KC.VOLU,
     UNASS, KC.LSHIFT, NOKEY, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.VOLD,
     UNASS, KC.LCTRL, KC.LWIN, KC.LALT, NOKEY, NOKEY, NOKEY, KC.SPACE, NOKEY, NOKEY, NOKEY, KC.RCTRL, KC.MO(1), KC.LEFT, KC.DOWN, KC.RIGHT, 
    ],
    [NOKEY, KC.GRAVE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, UNASS, KC.MPLY,
     UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS,
     UNASS, KC.CAPS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, NOKEY, UNASS, UNASS,
     UNASS, UNASS, NOKEY, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, KC.PGUP, UNASS,
     UNASS, UNASS, UNASS, UNASS, NOKEY, NOKEY, NOKEY, UNASS, NOKEY, NOKEY, NOKEY, UNASS, UNASS, KC.HOME, KC.PGDN, KC.END,
    ],
    [NOKEY, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS,
     UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS,
     UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, NOKEY, UNASS, UNASS,
     UNASS, UNASS, NOKEY, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS, UNASS,
     UNASS, UNASS, UNASS, UNASS, NOKEY, NOKEY, NOKEY, UNASS, NOKEY, NOKEY, NOKEY, UNASS, UNASS, UNASS, UNASS, UNASS,
    ],
]

if __name__ == '__main__':
    onlight.value=1
    keyboard.go()