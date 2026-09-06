class IntegratingPlant:
    def __init__(self, gain):
        self.gain = gain
        self.output = 0.0

    def update(self, input_signal, dt):
        self.output = self.output + self.gain * dt * input_signal

        return self.output