import os, sys
sys.path.insert(0, os.path.abspath("../rpi_ws281x"))
sys.path.insert(0, os.path.abspath("../rpi_ws281x/python"))
sys.path.insert(0, os.path.abspath("../rpi_ws281x/python/example"))

#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

from rpi_ws281x import *
import argparse
from util import *

# LED strip configuration:
LED_COUNT      = 80     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# number of steps
NUMBER_OF_LEDS = [42, 42, 42, 48, 42, 42, 42, 42, 48, 42, 42, 42, 42, 42]

# define steps
steps = []
for i, led_counter in enumerate(NUMBER_OF_LEDS):
    # get last identifier
    start = 0 if i == 0 else steps[-1][-1]
    # define range 
    steps.append(range(start, start + led_counter))


def pong(strip, color=None, rainbow=True):
    """Create pong effect"""

    # reset strip
    for i, step in enumerate(steps):
        for led in step:
            strip.setPixelColor(led, Color(0, 0, 0))
    strip.show()

    # init pong
    pointers = list()
    directions = list()
    colors = list()
    for i, step in enumerate(steps):
        # init pointer
        pointer = randint(0, NUMBER_OF_LEDS[i])
        pointers.append(pointer)

        # define color
        pixel_color = color if color else random_color()
        colors.append(color)

        # init direction
        direction = -1 if randint(0, 2) else 1
        directions.append(direction)

        # get led
        led = step[pointer]
        # set color of led
        strip.setPixelColor(led, pixel_color)

    # init strip
    strip.show()

    while True:
        for i, step in enumerate(steps):            
            # turn off led 
            pointer = pointers[i]
            led = step[pointer]
            pixel_color = Color(0, 0, 0)
            strip.setPixelColor(led, pixel_color)

            # switch direction if necessary
            direction = directions[i]
            if 0 > pointer + direction >= NUMBER_OF_LEDS[i]:
                direction *= -1

            # move pointer
            pointers[i] += direction

            if rainbow:
                colors[i] = (colors[i] + 1) % 0xFFFFFF

            # set color of next led
            pointer = pointers[i]
            led = step[pointer]
            pixel_color = colors[i]            
            strip.setPixelColor(led, pixel_color)



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
        for i, led in step:
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

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

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
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            colorWipe(strip, Color(0, 0, 255))  # Green wipe
            print ('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            print ('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
