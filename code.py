# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
import random
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from song import Song

# -------------------------------------
# Setup
# -------------------------------------
macropad = MacroPad()


# -------------------------------------
# Define functions
# -------------------------------------
def play(macropad: MacroPad, tone: str, duration: float) -> None:
    # Color random pixel a random color
    pixel = random.randrange(0, 12)        # Pick random pixel
    color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))     # Generate random color
    macropad.pixels[pixel] = color

    # Play tone
    macropad.play_tone(tone, duration)
    macropad.play_tone(0, 0.01)

    # Turn off pixel
    macropad.pixels[pixel] = 0x000000


def play_flower(macropad: MacroPad) -> None:
    macropad.display_image('real_flower_black.bmp')
    macropad.pixels.fill((0, 0, 0))
    notes = [
        ('e5', 0.25),
        ('d5', 0.25),
        ('c5', 0.5),
        ('', 0.25),
        ('d5', 0.25),
        ('c5', 0.25),
        ('b4', 0.5),
        ('', 0.25),
        ('g4', 0.25),
        ('d5', 0.25),
        ('c5', 0.25),
        ('b4', 0.25),
        ('g4', 0.25),
        ('a4', 0.5),
        ('c5', 0.5),
        ('a4', 0.5),
        ('e5', 0.25),
        ('d5', 0.25),
        ('c5', 0.5),
        ('', 0.75),
        ('d5', 0.25),
        ('c5', 0.25),
        ('b4', 0.5),
        ('', 0.25),
        ('g4', 0.25),
        ('d5', 0.25),
        ('c5', 0.25),
        ('b4', 0.25),
        ('g4', 0.25),
        ('a4', 0.5),
        ('c5', 0.5),
        ('a4', 0.5),
        ('a5', 0.5),
        ('a5', 0.5),
        ('a5', 0.25),
        ('g5', 0.25),
        ('e5', 0.25),
        ('d5', 0.25),
        ('e5', 0.5),
        ('g5', 0.5),
        ('e5', 0.5),
        ('', 0.3),
        ('g5', 0.5),
        ('g5', 0.5),
        ('g5', 0.25),
        ('f5', 0.25),
        ('e5', 0.25),
        ('c5', 0.25),
        ('d5', 0.25),
        ('e5', 0.25),
        ('d5', 0.25),
        ('c5', 0.25),
        ('a4', 0.75),
        ('c6', 0.25),
        ('b5', 0.65),
        ('c6', 0.25),
        ('b5', 0.5),
        ('g5', 0.25),
        ('g5', 0.25),
        ('g5', 0.25),
        ('g5', 0.5),
        ('a5', 0.5),
        ('a5', 0.5),
        ('', 0.25),
        ('a5', 0.5),
        ('a5', 0.5),
        ('a5', 0.25),
        ('e6', 0.25),
        ('d6', 0.25),
        ('c6', 0.25),
        ('b5', 0.5),
        ('g5', 0.5),
        ('g5', 0.5),
        ('', 0.25),
        ('g5', 0.5),
        ('g5', 0.5),
        ('g5', 0.25),
        ('d6', 0.25),
        ('c6', 0.25),
        ('b5', 0.25),
        ('c6', 0.5),
        ('a5', 0.5),
        ('a5', 0.75),
        ('a5', 0.5),
        ('a5', 0.5),
        ('a5', 0.25),
        ('e6', 0.25),
        ('d6', 0.25),
        ('c6', 0.25),
        ('b5', 0.5),
        ('g5', 0.5),
        ('g5', 0.5),
        ('', 0.25),
        ('d5', 0.25),
        ('c5', 0.25),
        ('d5', 0.25),
        ('e5', 0.25),
        ('a5', 0.5),
        ('a4', 0.25),
        ('g4', 0.25),
        ('a4', 0.5),
        ('a4', 0.5),
        ('a4', 0.75),
    ]

    flower = Song(notes)
    flower.play(macropad)

macros = {
    0: play_flower
}

# -------------------------------------
# Main loop
# -------------------------------------
while True:
    key_event = macropad.keys.events.get()

    for i in range(len(macros)):
        macropad.pixels[i] = 0x666666

    if key_event:
        if key_event.pressed:
            if key_event.key_number in macros:
                func = macros[key_event.key_number]
                func(macropad)
        else:
           pass