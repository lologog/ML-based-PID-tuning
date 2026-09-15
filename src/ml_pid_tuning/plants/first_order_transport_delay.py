import math

class FirstOrderTransportDelayPlant:
    def __init__(self, gain, time_constant, delay):
        if not isinstance(gain, (int, float)):
            raise TypeError("gain must be a number")

        if not math.isfinite(gain):
            raise ValueError("gain must be finite")

        if not isinstance(time_constant, (int, float)):
            raise TypeError("time_constant must be a number")

        if not math.isfinite(time_constant):
            raise ValueError("time_constant must be finite")

        if time_constant <= 0:
            raise ValueError("time_constant must be greater than 0")

        if not isinstance(delay, (int, float)):
            raise TypeError("delay must be a number")

        if not math.isfinite(delay):
            raise ValueError("delay must be finite")

        if delay < 0:
            raise ValueError("delay must be greater than or equal to 0")

        self.gain = gain
        self.time_constant = time_constant
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
            delayed_input = 0.0
        else:
            delayed_input = self.input_buffer[-delay_steps - 1]

        a = (self.time_constant) / (self.time_constant + dt)
        b = (self.gain * dt) / (self.time_constant + dt)

        self.output = a * self.output + b * delayed_input

        return self.output