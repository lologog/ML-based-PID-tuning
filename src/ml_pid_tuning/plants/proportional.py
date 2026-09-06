class ProportionalPlant:
    def __init__(self, gain):
        self.gain = gain
        self.output = 0.0

    def update(self, input_signal, dt):
        self.output = self.gain * input_signal

        return self.output