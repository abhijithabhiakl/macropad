print("Starting")

import board

from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.led import LED


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

# Boot Animation
# led = digitalio.DigitalInOut(board.GP10)
# led.direction = digitalio.Direction.OUTPUT
# time.sleep(0.5)
# led.value = True
# time.sleep(0.5)
# led.value = False
# BA_end


keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 150
keyboard.modules = [layers, encoder_handler, tapdance]


# NEOPXEL
rgb_ext = RGB(
    pixel_pin=board.GP17,
    num_pixels=7,
    val_limit=255,
    hue_default=120,        #Sets the hue from 0-360, 210 for true white 
    sat_default=100,        #Sets the saturation from 0-100
    rgb_order=(1, 0, 2),    # GRB WS2812 - 102
    val_default=60,         # Sets the brightness from 1-255
    hue_step=2,
    sat_step=5,
    val_step=5,
    animation_speed=5,
    breathe_center=1.6,   # 1.0-2.7
    knight_effect_length=3,
    animation_mode=AnimationModes.STATIC,
    reverse_animation=False,
    )

keyboard.extensions.append(rgb_ext)
# NEOPXEL_end


# LED
# led_red = LED(led_pin=board.GP12,
#     brightness_step=5,
#     brightness_limit=100,
#     breathe_center=2.75,
#     animation_mode=3,
#     animation_speed=0.14,
#     val=150,)
# led_blue = LED(led_pin=board.GP10,
#     brightness_step=5,
#     brightness_limit=100,
#     breathe_center=2.75,
#     animation_mode=3,
#     animation_speed=0.14,
#     val=150,)
# led_green = LED(led_pin=board.GP11,
#     brightness_step=5,
#     brightness_limit=100,
#     breathe_center=2.75,
#     animation_mode=3,
#     animation_speed=0.14,
#     val=100,)


# keyboard.extensions.append(led_red)
# keyboard.extensions.append(led_blue)
# keyboard.extensions.append(led_green)

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
FN1 = KC.TO(0)
FN2 = KC.TO(1)
FN3 = KC.TO(2)
FN4 = KC.TO(3)
FN5 = KC.TO(4)

# Tap dance
DF_M1 = KC.TD(
    KC.LCTL(KC.LSFT(KC.T)),
    KC.LCTL(KC.S)
)
DF_M2 = KC.TD(
    KC.LCTL(KC.F4),
    KC.LALT(KC.F4),
    KC.ESC
)
DF_M3 = KC.TD(
    KC.LCTL(KC.T),
    KC.LGUI(KC.E)
)
DF_M8 = KC.TD(
    KC.LALT(KC.TAB),
    KC.ENTER,
    KC.LWIN(KC.D)
)

RGB_M1 = KC.TD(
    KC.RGB_M_P,
    KC.RGB_M_B,
    KC.RGB_M_K
)
RGB_M2 = KC.TD(
    KC.RGB_M_S,
    KC.RGB_M_R,
    KC.RGB_M_BR
)
APH1 = KC.TD(
    KC.AT,KC.CAPS,KC.DOT,KC.ENTER
)
APH2 = KC.TD(
    KC.A, KC.B,KC.C,KC.COMMA
)
APH3 = KC.TD(
    KC.D,KC.E,KC.F
)
APH4 = KC.TD(
    KC.G,KC.H,KC.I
)
APH5 = KC.TD(
    KC.J,KC.K,KC.L
)
APH6 = KC.TD(
    KC.M,KC.N,KC.O
)
APH7 = KC.TD(
    KC.P,KC.Q,KC.R,KC.S
)
APH8 = KC.TD(
    KC.T,KC.U,KC.V
)
APH9 = KC.TD(
    KC.W,KC.X,KC.Y,KC.Z
)
NM8 = KC.TD(
    KC.LSFT,
    FN5
)
# Keymaps

keyboard.keymap = [
    [
        KC.RGB_TOG,KC.RGB_SAD,KC.RGB_SAI,                # RGB settings layer
        RGB_M2,KC.RGB_VAD,KC.RGB_VAI,
        RGB_M1,KC.RGB_ANI,KC.RGB_AND
     ],
    [
        DF_M1,DF_M2,DF_M3,                               # Default Layer
        KC.F11,KC.LCTL(KC.LSFT(KC.TAB)),KC.LCTL(KC.TAB),
        KC.LWIN(KC.PSCR),DF_M8,KC.MPLY
     ],
    [
        APH1,APH2,APH3,                                  # Alphabet layer
        APH4,APH5,APH6,
        APH7,APH8,APH9
     ],
     [
        KC.N1,KC.N2,KC.N3,                               # Numberpad layer
        KC.N4,KC.N5,KC.N6,      
        KC.N7,KC.N0,KC.N9 
     ],
     [
        KC.Q,KC.W,KC.SPACE,                                   # Gaming Layer
        KC.A,KC.S,KC.D,
        KC.LALT,KC.SPACE,KC.SPACE
     ]
]


# Rotary Encoder (1 encoder / 1 definition per layer )

encoder_handler.map = ( ((KC.RGB_HUI, KC.RGB_HUD, FN2),),  # RGB settings layer
                        ((KC.VOLD, KC.VOLU, FN3),),        # Standard
                        ((KC.BSPC, KC.LCTRL(KC.Z), FN4),), # Alphabet layer
                        ((KC.BSPC,NM8, KC.N8),),           # Numberpad layer
                        ((KC.VOLD, KC.VOLU, FN1),)         # Gaming Layer
                        )

if __name__ == '__main__':
    keyboard.go()