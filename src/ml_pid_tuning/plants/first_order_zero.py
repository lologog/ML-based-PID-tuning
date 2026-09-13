class FirstOrderZeroPlant:
    def __init__(self, gain, time_constant, zero_time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.zero_time_constant = zero_time_constant
        self.previous_input = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        denominator = self.time_constant + dt

        a = self.time_constant / denominator
        b1 = (self.gain * (self.zero_time_constant + dt)) / (denominator)
        b2 = - (self.gain * self.zero_time_constant) / (denominator)

        new_output = a * self.output + b1 * input_signal + b2 * self.previous_input

        self.previous_input = input_signal
        self.output = new_output

        return self.output