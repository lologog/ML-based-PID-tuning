class PIDController:
    def __init__(self, kp, ti, td):
        self.kp = kp
        self.ti = ti
        self.td = td

        self.integral = 0.0
        self.previous_error = 0.0

    def update(self, error, dt):
        self.integral += error * dt

        integral_term = 0.0
        if self.ti > 0.0:
            integral_term = self.integral / self.ti

        derivative_term = (error - self.previous_error) / dt

        control_signal = self.kp * (error + integral_term + self.td * derivative_term)
        self.previous_error = error

        return control_signal