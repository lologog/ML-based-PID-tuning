import math

class SecondOrderPlant:
    def __init__(self, gain, time_constant_1, time_constant_2):
        if not isinstance(gain, (int, float)):
            raise TypeError("gain must be a number")

        if not math.isfinite(gain):
            raise ValueError("gain must be finite")

        if not isinstance(time_constant_1, (int, float)):
            raise TypeError("time_constant_1 must be a number")

        if not math.isfinite(time_constant_1):
            raise ValueError("time_constant_1 must be finite")

        if time_constant_1 <= 0:
            raise ValueError("time_constant_1 must be greater than 0")

        if not isinstance(time_constant_2, (int, float)):
            raise TypeError("time_constant_2 must be a number")

        if not math.isfinite(time_constant_2):
            raise ValueError("time_constant_2 must be finite")

        if time_constant_2 <= 0:
            raise ValueError("time_constant_2 must be greater than 0")

        self.gain = gain
        self.time_constant_1 = time_constant_1
        self.time_constant_2 = time_constant_2

        self.previous_output = 0.0
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

        denominator = (self.time_constant_1 * self.time_constant_2) + (self.time_constant_1 + self.time_constant_2) * dt + dt ** 2

        a1 = (2 * self.time_constant_1 * self.time_constant_2 + (self.time_constant_1 + self.time_constant_2) * dt) / denominator
        a2 = -(self.time_constant_1 * self.time_constant_2) / (denominator)
        b = (self.gain * dt ** 2) / (denominator)

        new_output = a1 * self.output + a2 * self.previous_output + b * input_signal

        self.previous_output = self.output
        self.output = new_output

        return self.output