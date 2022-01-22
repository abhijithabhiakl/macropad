print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

#Pin allocation
keyboard.col_pins = (board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP13, board.GP14, board.GP15, False),)


XX = KC.TRNS
FN1 = KC.TO(1)
FN2 = KC.TO(0)
FN3 = KC.TO(2)
keyboard.keymap = [
    [
        KC.LCTL(KC.LSFT(KC.T)),KC.LCTL(KC.F4),KC.LCTL(KC.T),
        KC.F11,KC.LCTL(KC.LSFT(KC.TAB)),KC.LCTL(KC.TAB),
        KC.LWIN(KC.PSCR),XX,FN1
     ],
    [
        XX,KC.W,XX,
        KC.A,KC.S,KC.D,
        KC.SPACE,XX,FN3
     ],
    [
        KC.Q,KC.W,KC.E,
        KC.O,KC.P,KC.U,
        KC.Z,KC.X,FN2
     ]
]


# Rotary Encoder (1 encoder / 1 definition per layer)

encoder_handler.map = ( ((KC.VOLD, KC.VOLU, FN1),), # Standard
                        ((KC.VOLD, KC.VOLU, FN3),), # Second layer
                        ((KC.VOLD, KC.VOLU, FN2),), # Third layer
                        )

if __name__ == '__main__':
    keyboard.go()
