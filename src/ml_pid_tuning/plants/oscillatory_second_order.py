import math

class OscillatorySecondOrderPlant:
    def __init__(self, gain, natural_frequency, damping_ratio):
        if not isinstance(gain, (int, float)):
            raise TypeError("gain must be a number")

        if not math.isfinite(gain):
            raise ValueError("gain must be finite")

        if not isinstance(natural_frequency, (int, float)):
            raise TypeError("natural_frequency must be a number")

        if not math.isfinite(natural_frequency):
            raise ValueError("natural_frequency must be finite")

        if natural_frequency <= 0:
            raise ValueError("natural_frequency must be greater than 0")

        if not isinstance(damping_ratio, (int, float)):
            raise TypeError("damping_ratio must be a number")

        if not math.isfinite(damping_ratio):
            raise ValueError("damping_ratio must be finite")

        if damping_ratio < 0 or damping_ratio >= 1:
            raise ValueError("damping_ratio must be greater than or equal to 0 and less than 1")

        self.gain = gain
        self.natural_frequency = natural_frequency
        self.damping_ratio = damping_ratio

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

        denominator = 1 + 2 * self.damping_ratio * self.natural_frequency * dt + self.natural_frequency ** 2 * dt ** 2

        a1 = (2 + 2 * self.damping_ratio * self.natural_frequency * dt) / (denominator)
        a2 = - (1) / (denominator)
        b = (self.gain * self.natural_frequency ** 2 * dt ** 2) / (denominator)

        new_output = a1 * self.output + a2 * self.previous_output + b * input_signal

        self.previous_output = self.output
        self.output = new_output

        return self.output