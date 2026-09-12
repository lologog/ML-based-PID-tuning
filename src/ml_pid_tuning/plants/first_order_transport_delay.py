class FirstOrderTransportDelayPlant:
    def __init__(self, gain, time_constant, delay):
        self.gain = gain
        self.time_constant = time_constant
        self.delay = delay
        self.input_buffer = []
        self.output = 0.0

    def update(self, input_signal, dt):
        delay_steps = round(self.delay / dt)

        self.input_buffer.append(input_signal)

        if len(self.input_buffer) <= delay_steps:
            delayed_input = 0.0
        else:
            delayed_input = self.input_buffer[-delay_steps - 1]

        a = (self.time_constant) / (self.time_constant + dt)
        b = (self.gain * dt) / (self.time_constant + dt)

        self.output = a * self.output + b * delayed_input

        return self.output