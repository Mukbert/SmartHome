from rpi_ws281x import PixelStrip, Color
from devices.steps.step import Step
from devices.steps.util import *

# number of steps
NUMBER_OF_LEDS = [55, 42, 38, 44, 51, 40, 39, 47, 39, 33, 36, 57, 37, 39]
# LED strip configuration:
LED_COUNT = sum(NUMBER_OF_LEDS) #600        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class Steps(list):
    def __init__(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

        for i, led_counter in enumerate(NUMBER_OF_LEDS):
            # get last led
            start = 0 if i == 0 else (self[-1][-1] + 1)
            # define step 
            step = Step(self.strip, start, start + led_counter)
            self.append(step)
    
    def __len__(self):
        return sum(NUMBER_OF_LEDS)

    def off(self, step_ms=0, led_ms=0):
        for step in self:
            step.off(led_ms)
        wait(step_ms)

    def color_test(self):
        for step in self:
            color = random_color()
            for led in step:
                self.strip.setPixelColor(led, color)
                self.strip.show()

    def pong(self):
        self.pong_init()

        while True:
            self.pong_loop()

    def pong_init(self):
        for step in self:
            step.pong_init()

    def pong_loop(self, ms=10):
        for step in self:
            step.pong_loop(ms=0)
        wait(ms)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, wheel(i & 255))
            self.strip.show()
            wait(wait_ms)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            wait(wait_ms)
