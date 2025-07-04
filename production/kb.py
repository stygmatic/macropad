import board, neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Macros, MacroAction

keyboard = KMKKeyboard()
pixels = neopixel.NeoPixel(board.D0, 4, brightness=0.3, auto_write=False)

def px(i, on):
    pixels[i] = (40, 40, 40) if on else (0, 0, 0)
    pixels.show()

class On(MacroAction):
    def __init__(self, i): self.i = i
    def press(self, k): px(self.i, True)

class Off(MacroAction):
    def __init__(self, i): self.i = i
    def press(self, k): px(self.i, False)

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

keyboard.keymap = [[
    KC.MACRO(On(0), Press(KC.A), Release(KC.A), Off(0)),
    KC.MACRO(On(1), Press(KC.DELETE), Release(KC.DELETE), Off(1)),
    KC.MACRO(On(2), Press(KC.B), Release(KC.B), Off(2)),
    KC.MACRO(On(3), Press(KC.C), Release(KC.C), Off(3)),
]]

if __name__ == '__main__':
    keyboard.go()
