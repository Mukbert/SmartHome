from rpi_ws281x import Color
from devices.steps import util
import random

class Step(list):
    def __init__(self, strip, start, stop):
        super().__init__(range(start, stop))
        self.strip = strip
    
    def off(self, ms=0):
        for led in self:
            self.strip.setPixelColor(led, Color(0, 0, 0))
            self.strip.show()
            util.wait(ms)

    def pong(self):
        self.pong_init()

        while True:
            self.pong_loop()

    def pong_init(self):
        # reset
        for led in self:
            self.strip.setPixelColor(led, Color(0, 0, 0))

        self.pointer = random.randint(0, len(self))
        self.color = util.random_color()
        self.strip.setPixelColor(self[self.pointer], Color(255, 0, 0))
        self.strip.show()

        self.direction = -1 if random.randint(0, 10) < 5 else 1

    def pong_loop(self, ms=10):
        self.strip.setPixelColor(self[self.pointer], Color(0, 0, 0))

        self.pointer += self.direction

        self.strip.setPixelColor(self[self.pointer], self.color)

        if self.pointer == 0 or self.pointer == len(self) - 1:
            self.direction *= -1

        self.strip.show()
        util.wait(ms)

