import math

class TransportDelayPlant:
    def __init__(self, delay):
        if not isinstance(delay, (int, float)):
            raise TypeError("delay must be a number")

        if not math.isfinite(delay):
            raise ValueError("delay must be finite")

        if delay < 0:
            raise ValueError("delay must be greater than or equal to 0")

        self.delay = delay
        self.input_buffer = []
        self.output = 0.0

    def update(self, input_signal, dt):
        if not isinstance(input_signal, (int, float)):
            raise TypeError("input_signal must be a number")

        if not math.isfinite(input_signal):
            raise ValueError("input_signal must be finite")

        if not isinstance(dt, (int, float)):
            raise TypeError("dt must be a number")

        if not math.isfinite(dt):
            raise ValueError("dt must be finite")

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        delay_steps = round(self.delay / dt)

        self.input_buffer.append(input_signal)

        if len(self.input_buffer) <= delay_steps:
            self.output = 0.0
        else:
            self.output = self.input_buffer[-delay_steps - 1]

        return self.output