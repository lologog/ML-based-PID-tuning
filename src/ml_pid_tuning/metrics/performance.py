def calculate_iae(time_values, error_values):
    iae = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]
        iae += abs(error_values[i]) * dt

    return iae


def calculate_ise(time_values, error_values):
    ise = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]
        ise += error_values[i] ** 2 * dt

    return ise


def calculate_itae(time_values, error_values):
    itae = 0.0

    for i in range(1, len(time_values)):
        dt = time_values[i] - time_values[i - 1]
        itae += time_values[i] * abs(error_values[i]) * dt

    return itae


def calculate_overshoot(output_values, setpoint):
    max_output = max(output_values)

    overshoot = ((max_output - setpoint) / setpoint) * 100.0

    return max(0.0, overshoot)


def calculate_settling_time(time_values, output_values, setpoint, tolerance=0.02):
    lower_bound = setpoint * (1.0 - tolerance)
    upper_bound = setpoint * (1.0 + tolerance)

    for i in range(len(output_values)):
        remaining_values = output_values[i:]

        if all(lower_bound <= value <= upper_bound for value in remaining_values):
            return time_values[i]

    return None