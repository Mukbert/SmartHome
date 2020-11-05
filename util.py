import time
from random import randint 
from rpi_ws281x import Color

def randomRGB():
    return randint(0, 255), randint(0, 255), randint(0, 255)

def random_color():
    return Color(*randomRGB())

def compute_color(color1, color2, i, end):
    if color1 == color2:
        return color1
    def interpolation(c1, c2):
        return int(c1 + (c2 - c1) * (i / end))
    return Color(*[interpolation(c1, c2) for c1, c2 in zip(color1, color2)])

def wait(ms):
    time.sleep(ms/1000.0)