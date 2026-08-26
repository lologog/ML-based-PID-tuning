class SecondOrderPlant:
    def __init__(self, gain, time_constant_1, time_constant_2):
        self.gain = gain
        self.time_constant_1 = time_constant_1
        self.time_constant_2 = time_constant_2

        self.state_1 = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        state_1_derivative = (self.gain * input_signal - self.state_1) / self.time_constant_1
        self.state_1 += state_1_derivative * dt

        output_derivative = (self.state_1 - self.output) / self.time_constant_2
        self.output += output_derivative * dt

        return self.output