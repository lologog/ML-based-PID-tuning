class DifferentiatingPlant:
    def __init__(self, gain):
        self.gain = gain
        self.previous_input = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        self.output = self.gain * (input_signal - self.previous_input) / (dt)

        self.previous_input = input_signal

        return self.output