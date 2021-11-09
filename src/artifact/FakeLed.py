class FakeLed:
    def __init__(self, gpio, pin):
        self.isOn = False

    def on(self):
        self.isOn = True

    def off(self):
        self.isOn = False
