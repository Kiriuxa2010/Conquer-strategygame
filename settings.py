import pygame
from pygame import mixer 

# sc
WIDTH = 800
HEIGHT = 600

#Colors
GREEN = 000,255,000
WHITE = 255,255,255
BLACK = 000,000,000
BLUE = 000,000,255
RED = 255,000,000

# voice lines

def line1():
    mixer.music.load('GameFiles//soundsvoiceline01.ogg')
    mixer.music.set_volume(0.9)
    mixer.music.play()