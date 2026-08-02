class FirstOrderPlant:
    def __init__(self, gain, time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.output = 0.0

    def update(self, input_signal, dt):
        output_derivative = (self.gain * input_signal - self.output) / self.time_constant
        self.output += output_derivative * dt
        return self.output