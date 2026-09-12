class SecondOrderTransportDelayPlant:
    def __init__(self, gain, time_constant_1, time_constant_2, delay):
        self.gain = gain
        self.time_constant_1 = time_constant_1
        self.time_constant_2 = time_constant_2
        self.delay = delay
        self.input_buffer = []
        self.previous_output = 0.0
        self.output = 0.0

    def update(self, input_signal, dt):
        delay_steps = round(self.delay / dt)

        self.input_buffer.append(input_signal)

        if len(self.input_buffer) <= delay_steps:
            delayed_input = 0.0
        else:
            delayed_input = self.input_buffer[-delay_steps - 1]

        denominator = self.time_constant_1 * self.time_constant_2 + (self.time_constant_1 + self.time_constant_2) *dt + dt ** 2

        a1 = (2 * self.time_constant_1 * self.time_constant_2 + (self.time_constant_1 + self.time_constant_2) * dt) / (denominator)
        a2 = - (self.time_constant_1 * self.time_constant_2) / (denominator)
        b = (self.gain * dt ** 2) / (denominator)

        new_output = a1 * self.output + a2 * self.previous_output + b * delayed_input

        self.previous_output = self.output
        self.output = new_output

        return self.output