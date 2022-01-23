print("Starting")

import board
import digitalio
import time

from kmk.extensions.rgb import RGB, AnimationModes


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

# Boot Animation
led = digitalio.DigitalInOut(board.GP10)
ledRed = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
ledRed.direction = digitalio.Direction.OUTPUT
ledRed.value = True
time.sleep(0.5)
ledRed.value = False
led.value = True
time.sleep(0.5)
led.value = False
# BA_end


keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoder_handler, tapdance]


# NEOPXEL
rgb_ext = RGB(
    pixel_pin=board.GP9,
    num_pixels=1,
    val_limit=255,
    hue_default=0,
    sat_default=100,
    rgb_order=(2, 0, 1),  # GRB WS2812
    val_default=160,
    hue_step=1,
    sat_step=1,
    val_step=1,
    animation_speed=2.5,
    breathe_center=1.9,  # 1.0-2.7
    knight_effect_length=1,
    animation_mode=4,
    reverse_animation=False,
    )

keyboard.extensions.append(rgb_ext)
# NEOPXEL_end


# LED
# led_red = LED(led_pin=board.GP9,
#     brightness_step=5,
#     brightness_limit=100,
#     breathe_center=2.75,
#     animation_mode=3,
#     animation_speed=0.14,
#     val=100,)

# keyboard.extensions.append(led_red)
# LED_end

# Pin allocation
keyboard.col_pins = (board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP14, board.GP13, board.GP15, False),)
# Pin allocation_end


# Layer map

# LYR_STD, LYR_EXT, LYR_NUM, LYR_GAME = 0, 1, 2, 3

XX = KC.TRNS
FN1 = KC.TO(1)
FN2 = KC.TO(0)
FN3 = KC.TO(2)


# Tap dance
RGB_M1 = KC.TD(
    KC.RGB_M_P,
    KC.RGB_M_B,
    KC.RGB_M_R
)
RGB_M2 = KC.TD(
    KC.RGB_M_S,
    KC.RGB_M_K,
    KC.RGB_M_BR
)


keyboard.keymap = [
    [
        KC.LCTL(KC.LSFT(KC.T)),KC.LCTL(KC.F4),KC.LCTL(KC.T),
        KC.F11,KC.LCTL(KC.LSFT(KC.TAB)),KC.LCTL(KC.TAB),
        KC.LWIN(KC.PSCR),KC.F11,KC.MPLY
     ],
    [
        XX,KC.W,XX,
        KC.A,KC.S,KC.D,
        KC.SPACE,XX,FN3
     ],
    [
        KC.RGB_TOG,KC.RGB_SAI,KC.RGB_SAD,
        RGB_M2,KC.RGB_VAI,KC.RGB_VAD,
        RGB_M1,KC.RGB_ANI,KC.RGB_AND
     ]
]


# Rotary Encoder (1 encoder / 1 definition per layer)

encoder_handler.map = ( ((KC.VOLD, KC.VOLU, FN1),), # Standard
                        ((KC.VOLD, KC.VOLU, FN3),), # Second layer
                        ((KC.RGB_HUI, KC.RGB_HUD, FN2),), # Third layer
                        )

if __name__ == '__main__':
    keyboard.go()