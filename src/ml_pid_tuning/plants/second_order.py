class SecondOrderPlant:
    def __init__(self, gain, time_constant_1, time_constant_2):
        self.gain = gain
        self.time_constant_1 = time_constant_1
        self.time_constant_2 = time_constant_2

        self.previous_output = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        denominator = (self.time_constant_1 * self.time_constant_2) + (self.time_constant_1 + self.time_constant_2) * dt + dt ** 2

        a1 = (2 * self.time_constant_1 * self.time_constant_2 + (self.time_constant_1 + self.time_constant_2) *dt) / denominator
        a2 = -(self.time_constant_1 * self.time_constant_2) / (denominator)
        b = (self.gain * dt ** 2) / (denominator)

        new_output = a1 * self.output + a2 * self.previous_output + b * input_signal

        self.previous_output = self.output
        self.output = new_output

        return self.output