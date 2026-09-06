class DifferentiatingFirstOrderPlant:
    def __init__(self, gain, time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.previous_input = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        a = (self.time_constant) / (self.time_constant + dt)
        b1 = (self.gain) / (self.time_constant + dt)
        b2 = - (self.gain) / (self.time_constant + dt)

        new_output = a * self.output + b1 * input_signal + b2 * self.previous_input

        self.previous_input = input_signal
        self.output = new_output

        return self.output