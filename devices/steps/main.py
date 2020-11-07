
import random
from devices.steps.util import *
from devices.steps.steps import Steps



def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)

def off(strip):
    for led in range(strip.numPixels()):
        strip.setPixelColor(led, Color(0, 0, 0))
    strip.show()

def woosh(strip, color=None, multicolor=True, step_wait=50, led_wait=10):
    """Sliding effect for steps"""
    # iterate over every step 
    for step in steps:
        # select colors for endings
        if color:
            # select color from parameter as single color
            color1, color2 = color, color
        else:
            # generate 2 random colors for rainbow effect
            color1, color2 = randomRGB(), randomRGB()

        # iterate over ever led on step
        for i, led in enumerate(step):
            # compute interpolated color for led
            pixel_color = compute_color(color1, color2, i, len(step))
            # set color of led
            strip.setPixelColor(led, pixel_color)
            # update strip
            strip.show()
            # short break after every led
            wait(led_wait)
        # short break after every step
        wait(step_wait)

