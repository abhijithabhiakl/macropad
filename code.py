print("Starting")
import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.extensions.led import LED
from kmk.modules.encoder import EncoderHandler

#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT

keyboard = KMKKeyboard()
keyboard.debug_enabled = False
led_red = LED(led_pin=board.GP9,
    brightness_step=5,
    brightness_limit=100,
    breathe_center=2.75,
    animation_mode=3,
    animation_speed=0.14,
    val=100,)
led_blue = LED(led_pin=board.GP10,
    brightness_step=5,
    brightness_limit=100,
    breathe_center=2.75,
    animation_mode=3,
    animation_speed=0.21,
    val=100,)
led_green = LED(led_pin=board.GP12,
    brightness_step=5,
    brightness_limit=0,
    breathe_center=2.75,
    animation_mode=3,
    animation_speed=0.07,
    val=100,)
keyboard.extensions.append(led_red)
keyboard.extensions.append(led_blue)
keyboard.extensions.append(led_green)
    
# Encoder
encoder_map = [[(KC.VOLD,KC.VOLU,1)]]
encoder_ext = EncoderHandler([board.GP13],[board.GP14],encoder_map)
encoder_ext.encoders[0].is_inverted = True
# -----
keyboard.col_pins = (board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [
        KC.LCTL(KC.LSFT(KC.T)),KC.LCTL(KC.F4),KC.LCTL(KC.T),
        KC.F11,KC.LCTL(KC.LSFT(KC.TAB)),KC.LCTL(KC.TAB),
        KC.LWIN(KC.PSCR),KC.LEFT,KC.MPLY
     ]
]
keyboard.modules = [encoder_ext]

if __name__ == '__main__':
    #led.value = True
    keyboard.go()

