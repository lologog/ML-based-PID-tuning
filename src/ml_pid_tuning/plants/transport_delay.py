class TransportDelayPlant:
    def __init__(self, delay):
        self.delay = delay
        self.input_buffer = []
        self.output = 0.0

    def update(self, input_signal, dt):
        delay_steps = round(self.delay / dt)

        self.input_buffer.append(input_signal)

        if len(self.input_buffer) <= delay_steps:
            self.output = 0.0
        else:
            self.output = self.input_buffer[-delay_steps - 1]

        return self.output
