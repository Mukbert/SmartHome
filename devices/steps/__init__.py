from devices.steps.steps import Steps

steps = Steps()

def run(action):
    return getattr(steps, action)()

def actions():
    return list(filter(lambda x: not x.startswith("_"), dir(steps)))