from rpi_ws281x import Color
from devices.steps import util

class Step:
    def __init__(self, start, stop):
        self.leds = range(start, stop)

    def off(self, strip, ms=0):
        for led in self.leds:
            strip.setPixelColor(led, Color(0, 0, 0))
        strip.show()
        util.wait(ms)