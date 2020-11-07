from rpi_ws281x import Color
from devices.steps import util

class Step(list):
    def __init__(self, strip, start, stop):
        super().__init__(range(start, stop))
        self.strip = strip
    
    def off(self, ms=0):
        for led in self:
            self.strip.setPixelColor(led, Color(0, 0, 0))
            self.strip.show()
            util.wait(ms)