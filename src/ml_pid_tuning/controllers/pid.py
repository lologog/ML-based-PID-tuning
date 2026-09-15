import math

class PIDController:
    def __init__(self, kp, ti, td):
        if not isinstance(kp, (int, float)):
            raise TypeError("kp must be a number")

        if not math.isfinite(kp):
            raise ValueError("kp must be finite")

        if not isinstance(ti, (int, float)):
            raise TypeError("ti must be a number")

        if not math.isfinite(ti):
            raise ValueError("ti must be finite")

        if ti < 0:
            raise ValueError("ti must be greater than or equal to 0")

        if not isinstance(td, (int, float)):
            raise TypeError("td must be a number")

        if not math.isfinite(td):
            raise ValueError("td must be finite")

        if td < 0:
            raise ValueError("td must be greater than or equal to 0")

        self.kp = kp
        self.ti = ti
        self.td = td

        self.integral = 0.0
        self.previous_error = 0.0

    def update(self, error, dt):
        if not isinstance(error, (int, float)):
            raise TypeError("error must be a number")

        if not math.isfinite(error):
            raise ValueError("error must be finite")

        if not isinstance(dt, (int, float)):
            raise TypeError("dt must be a number")

        if not math.isfinite(dt):
            raise ValueError("dt must be finite")

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        self.integral += error * dt

        integral_term = 0.0
        if self.ti > 0.0:
            integral_term = self.integral / self.ti

        derivative_term = (error - self.previous_error) / dt

        control_signal = self.kp * (error + integral_term + self.td * derivative_term)

        self.previous_error = error

        return control_signal