from rpi_ws281x import Color
from devices.steps import util

class Step:
    def __init__(self, strip, start, stop):
        self.strip = strip
        self.leds = range(start, stop)

    def off(self, ms=0):
        for led in self.leds:
            self.strip.setPixelColor(led, Color(0, 0, 0))
        self.strip.show()
        util.wait(ms)