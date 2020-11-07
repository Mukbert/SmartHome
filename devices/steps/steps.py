from devices.steps.step import Step

class Steps:
    # number of steps
    NUMBER_OF_LEDS = [55, 42, 38, 44, 51, 40, 39, 47, 39, 33, 36, 57, 37, 39]

    def __init__(self):
        # define steps
        self.steps = []

        for i, led_counter in enumerate(Steps.NUMBER_OF_LEDS):
            # get last led
            start = 0 if i == 0 else (steps[-1][-1] + 1)
            # define step 
            step = Step(start, start + led_counter)
            steps.append(step)

    def off(self, strip):
        for step in steps:
            step.off(strip)
    
    def __len__(self):
        return sum(NUMBER_OF_LEDS)
