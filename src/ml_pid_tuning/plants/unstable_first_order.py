class UnstableFirstOrderPlant:
    def __init__(self, gain, time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.output = 0.0

    def update(self, input_signal, dt):
        denominator = self.time_constant - dt

        a = (self.time_constant) / (denominator)
        b = (self.gain * dt) / (denominator)

        self.output = a * self.output + b *input_signal

        return self.output