import random
from adafruit_macropad import MacroPad

class Song:
    def __init__(self, notes):
        self.notes = notes
        self.tones_dict =  {
            'g3': 196,
            'a3': 220,
            'b3': 247,
            'c4': 262,
            'd4': 394,
            'e4': 330,
            'f4': 175,
            'g4': 392,
            'a4': 440,
            'b4': 494,
            'c5': 523,
            'd5': 587,
            'e5': 659,
            'f5': 698,
            'g5': 784,
            'a5': 880,
            'b5': 988,
            'c6': 1046,
            'd6': 1174,
            'e6': 1318,
            'f6': 1396,
            'g6': 1568,
            'a6': 1760,
            'b6': 1975,
            '': 0,
        }

    
    def play_note(self, macropad: MacroPad, tone: str, duration: float) -> None:
        # Color random pixel a random color
        pixel = random.randrange(0, 12)        # Pick random pixel
        color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))     # Generate random color
        macropad.pixels[pixel] = color

        # Play tone
        macropad.play_tone(self.tones_dict[tone], duration)
        macropad.play_tone(0, 0.01)

        # Turn off pixel
        macropad.pixels[pixel] = 0x000000


    def play(self, macropad: MacroPad) -> None:
        for tone, duration in self.notes:
            self.play_note(macropad, tone, duration)