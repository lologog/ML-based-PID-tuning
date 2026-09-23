import math

def calculate_iae(time_values, error_values):
    if not isinstance(time_values, (list, tuple)):
        raise TypeError("time_values must be a list or tuple")

    if not isinstance(error_values, (list, tuple)):
        raise TypeError("error_values must be a list or tuple")

    if len(time_values) == 0:
        raise ValueError("time_values must not be empty")

    if len(error_values) == 0:
        raise ValueError("error_values must not be empty")

    if len(time_values) != len(error_values):
        raise ValueError("time_values and error_values must have the same length")

    for value in time_values:
        if not isinstance(value, (int, float)):
            raise TypeError("time_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("time_values must contain only finite values")

    for value in error_values:
        if not isinstance(value, (int, float)):
            raise TypeError("error_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("error_values must contain only finite values")

    for i in range(1, len(time_values)):
        if time_values[i] <= time_values[i - 1]:
            raise ValueError("time_values must be strictly increasing")

    iae = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]

        iae += abs(error_values[i]) * dt

    return iae


def calculate_ise(time_values, error_values):
    if not isinstance(time_values, (list, tuple)):
        raise TypeError("time_values must be a list or tuple")

    if not isinstance(error_values, (list, tuple)):
        raise TypeError("error_values must be a list or tuple")

    if len(time_values) == 0:
        raise ValueError("time_values must not be empty")

    if len(error_values) == 0:
        raise ValueError("error_values must not be empty")

    if len(time_values) != len(error_values):
        raise ValueError("time_values and error_values must have the same length")

    for value in time_values:
        if not isinstance(value, (int, float)):
            raise TypeError("time_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("time_values must contain only finite values")

    for value in error_values:
        if not isinstance(value, (int, float)):
            raise TypeError("error_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("error_values must contain only finite values")

    for i in range(1, len(time_values)):
        if time_values[i] <= time_values[i - 1]:
            raise ValueError("time_values must be strictly increasing")

    ise = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]

        ise += error_values[i] ** 2 * dt

    return ise


def calculate_itae(time_values, error_values):
    if not isinstance(time_values, (list, tuple)):
        raise TypeError("time_values must be a list or tuple")

    if not isinstance(error_values, (list, tuple)):
        raise TypeError("error_values must be a list or tuple")

    if len(time_values) == 0:
        raise ValueError("time_values must not be empty")

    if len(error_values) == 0:
        raise ValueError("error_values must not be empty")

    if len(time_values) != len(error_values):
        raise ValueError("time_values and error_values must have the same length")

    for value in time_values:
        if not isinstance(value, (int, float)):
            raise TypeError("time_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("time_values must contain only finite values")

    for value in error_values:
        if not isinstance(value, (int, float)):
            raise TypeError("error_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("error_values must contain only finite values")

    for i in range(1, len(time_values)):
        if time_values[i] <= time_values[i - 1]:
            raise ValueError("time_values must be strictly increasing")

    itae = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]

        itae += time_values[i] * abs(error_values[i]) * dt

    return itae


def calculate_overshoot(output_values, setpoint):
    if not isinstance(output_values, (list, tuple)):
        raise TypeError("output_values must be a list or tuple")

    if len(output_values) == 0:
        raise ValueError("output_values must not be empty")

    for value in output_values:
        if not isinstance(value, (int, float)):
            raise TypeError("output_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("output_values must contain only finite values")

    if not isinstance(setpoint, (int, float)):
        raise TypeError("setpoint must be a number")

    if not math.isfinite(setpoint):
        raise ValueError("setpoint must be finite")

    if setpoint == 0:
        raise ValueError("setpoint must not be equal to 0")

    max_output = max(output_values)

    overshoot = ((max_output - setpoint) / setpoint) * 100.0

    return max(0.0, overshoot)


def calculate_settling_time(time_values, output_values, setpoint, tolerance=0.02):
    if not isinstance(time_values, (list, tuple)):
        raise TypeError("time_values must be a list or tuple")

    if not isinstance(output_values, (list, tuple)):
        raise TypeError("output_values must be a list or tuple")

    if len(time_values) == 0:
        raise ValueError("time_values must not be empty")

    if len(output_values) == 0:
        raise ValueError("output_values must not be empty")

    if len(time_values) != len(output_values):
        raise ValueError("time_values and output_values must have the same length")

    for value in time_values:
        if not isinstance(value, (int, float)):
            raise TypeError("time_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("time_values must contain only finite values")

    for value in output_values:
        if not isinstance(value, (int, float)):
            raise TypeError("output_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("output_values must contain only finite values")

    for i in range(1, len(time_values)):
        if time_values[i] <= time_values[i - 1]:
            raise ValueError("time_values must be strictly increasing")

    if not isinstance(setpoint, (int, float)):
        raise TypeError("setpoint must be a number")

    if not math.isfinite(setpoint):
        raise ValueError("setpoint must be finite")

    if not isinstance(tolerance, (int, float)):
        raise TypeError("tolerance must be a number")

    if not math.isfinite(tolerance):
        raise ValueError("tolerance must be finite")

    if tolerance <= 0:
        raise ValueError("tolerance must be greater than 0")

    lower_bound = setpoint * (1.0 - tolerance)

    upper_bound = setpoint * (1.0 + tolerance)

    for i in range(len(output_values)):
        remaining_values = output_values[i:]

        if all(lower_bound <= value <= upper_bound for value in remaining_values):
            return time_values[i]

    return None


def calculate_steady_state_error(output_values, setpoint):
    if not isinstance(output_values, (list, tuple)):
        raise TypeError("output_values must be a list or tuple")

    if len(output_values) == 0:
        raise ValueError("output_values must not be empty")

    for value in output_values:
        if not isinstance(value, (int, float)):
            raise TypeError("output_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("output_values must contain only finite values")

    if not isinstance(setpoint, (int, float)):
        raise TypeError("setpoint must be a number")

    if not math.isfinite(setpoint):
        raise ValueError("setpoint must be finite")

    steady_state_error = abs(setpoint - output_values[-1])

    return steady_state_error

def calculate_max_control(control_signal_values):

    if not isinstance(control_signal_values, (list, tuple)):
        raise TypeError("control_signal_values must be a list or tuple")

    if len(control_signal_values) == 0:
        raise ValueError("control_signal_values must not be empty")

    for value in control_signal_values:

        if not isinstance(value, (int, float)):
            raise TypeError("control_signal_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("control_signal_values must contain only finite values")

    max_control = max(abs(value) for value in control_signal_values)

    return max_control


def calculate_isu(time_values, control_signal_values):

    if not isinstance(time_values, (list, tuple)):
        raise TypeError("time_values must be a list or tuple")

    if not isinstance(control_signal_values, (list, tuple)):
        raise TypeError("control_signal_values must be a list or tuple")

    if len(time_values) == 0:
        raise ValueError("time_values must not be empty")

    if len(control_signal_values) == 0:
        raise ValueError("control_signal_values must not be empty")

    if len(time_values) != len(control_signal_values):
        raise ValueError("time_values and control_signal_values must have the same length")

    for value in time_values:

        if not isinstance(value, (int, float)):
            raise TypeError("time_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("time_values must contain only finite values")

    for value in control_signal_values:

        if not isinstance(value, (int, float)):
            raise TypeError("control_signal_values must contain only numbers")

        if not math.isfinite(value):
            raise ValueError("control_signal_values must contain only finite values")

    for i in range(1, len(time_values)):

        if time_values[i] <= time_values[i - 1]:
            raise ValueError("time_values must be strictly increasing")

    isu = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]
        isu += control_signal_values[i - 1] ** 2 * dt

    return isu