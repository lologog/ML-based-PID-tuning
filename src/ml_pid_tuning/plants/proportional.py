import math

class ProportionalPlant:
    def __init__(self, gain):
        if not isinstance(gain, (int, float)):
            raise TypeError("gain must be a number")

        if not math.isfinite(gain):
            raise ValueError("gain must be finite")

        self.gain = gain
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

        self.output = self.gain * input_signal

        return self.output