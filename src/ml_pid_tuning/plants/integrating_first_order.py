class IntegratingFirstOrderPlant:
    def __init__(self, gain, time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.previous_output = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        a1 = (2 * self.time_constant + dt) / (self.time_constant + dt)
        a2 = - (self.time_constant) / (self.time_constant + dt)
        b = (self.gain * dt ** 2) / (self.time_constant + dt)

        new_output = a1 * self.output + a2 * self.previous_output + b * input_signal

        self.previous_output = self.output
        self.output = new_output

        return self.output