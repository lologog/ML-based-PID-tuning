class OscillatorySecondOrderPlant:
    def __init__(self, gain, natural_frequency, damping_ratio):
        self.gain = gain
        self.natural_frequency = natural_frequency
        self.damping_ratio = damping_ratio

        self.previous_output = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        denominator = 1 + 2 * self.damping_ratio * self.natural_frequency * dt + self.natural_frequency ** 2 * dt ** 2

        a1 = (2 + 2 * self.damping_ratio * self.natural_frequency * dt) / (denominator)
        a2 = - (1) / (denominator)
        b = (self.gain * self.natural_frequency ** 2 * dt ** 2) / (denominator)

        new_output = a1 * self.output + a2 * self.previous_output + b * input_signal

        self.previous_output = self.output
        self.output = new_output

        return self.output