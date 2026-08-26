class PIDController:
    def __init__(self, kp, ti, td):
        self.kp = kp
        self.ti = ti
        self.td = td

        self.integral = 0.0
        self.previous_error = 0.0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        control_signal = self.kp * (error + self.integral / self.ti + self.td * derivative)
        self.previous_error = error

        return control_signal