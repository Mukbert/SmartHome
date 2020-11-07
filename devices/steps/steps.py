from rpi_ws281x import PixelStrip, Color
from devices.steps.step import Step

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


class Steps:    
    def __init__(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

        # define steps
        self.steps = []

        for i, led_counter in enumerate(NUMBER_OF_LEDS):
            # get last led
            start = 0 if i == 0 else (self.steps[-1][-1] + 1)
            # define step 
            step = Step(self.strip, start, start + led_counter)
            self.steps.append(step)

    def off(self):
        for step in self.steps:
            step.off()
    
    def __len__(self):
        return sum(NUMBER_OF_LEDS)
