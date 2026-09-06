class FirstOrderPlant:
    def __init__(self, gain, time_constant):
        self.gain = gain
        self.time_constant = time_constant
        self.output = 0.0

    def update(self, input_signal, dt):
        T = self.time_constant
        Ts = dt
        K = self.gain

        a = T / (T + Ts)
        b = (K * Ts) / (T + Ts)

        self.output = a * self.output + b * input_signal

        return self.output