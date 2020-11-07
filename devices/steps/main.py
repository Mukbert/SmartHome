from rpi_ws281x import PixelStrip, Color
import random
from devices.steps.util import *
from devices.steps.steps import Steps

steps = Steps()


# LED strip configuration:
LED_COUNT = len(steps) #600        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

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

def pong(strip):
    step = steps[0]
    # reset
    for led in step:
        strip.setPixelColor(led, Color(0, 0, 0))

    pointer = random.randint(0, len(steps[0]))
 
    led = step[pointer]
    strip.setPixelColor(led, Color(255, 0, 0))
    strip.show()

    direction = -1 if random.randint(0, 10) < 5 else 1

    while True:
        led = step[pointer]
        strip.setPixelColor(led, Color(0, 0, 0))

        pointer += direction

        led = step[pointer]
        strip.setPixelColor(led, Color(255, 0, 0))

        if pointer == 0 or pointer == len(step) - 1:
            direction *= -1

        strip.show()
        time.sleep(0.01)



if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    #pong(strip)
