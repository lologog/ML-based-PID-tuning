import pytest

from ml_pid_tuning.metrics.performance import calculate_iae
from ml_pid_tuning.metrics.performance import calculate_ise
from ml_pid_tuning.metrics.performance import calculate_itae
from ml_pid_tuning.metrics.performance import calculate_overshoot
from ml_pid_tuning.metrics.performance import calculate_settling_time
from ml_pid_tuning.metrics.performance import calculate_steady_state_error

#########################################################################################
###                                      IAE
#########################################################################################

def test_calculate_iae():
    time_values = [0.0, 1.0, 2.0]
    error_values = [1.0, 0.5, 0.0]

    iae = calculate_iae(time_values, error_values)

    assert iae == pytest.approx(0.5)

def test_iae_invalid_time_values_type():
    try:
        calculate_iae("invalid", [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must be a list or tuple"

def test_iae_invalid_error_values_type():
    try:
        calculate_iae([0.0, 1.0], "invalid")
        assert False

    except TypeError as error:
        assert str(error) == "error_values must be a list or tuple"

def test_iae_empty_time_values():
    try:
        calculate_iae([], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must not be empty"

def test_iae_empty_error_values():
    try:
        calculate_iae([0.0], [])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must not be empty"

def test_iae_different_lengths():
    try:
        calculate_iae([0.0, 1.0], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values and error_values must have the same length"

def test_iae_invalid_time_value_type():
    try:
        calculate_iae([0.0, "1.0"], [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must contain only numbers"

def test_iae_invalid_error_value_type():
    try:
        calculate_iae([0.0, 1.0], [1.0, "0.5"])
        assert False

    except TypeError as error:
        assert str(error) == "error_values must contain only numbers"

def test_iae_nan_time_value():
    try:
        calculate_iae([0.0, float("nan")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_iae_nan_error_value():
    try:
        calculate_iae([0.0, 1.0], [1.0, float("nan")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_iae_positive_infinity_time_value():
    try:
        calculate_iae([0.0, float("inf")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_iae_positive_infinity_error_value():
    try:
        calculate_iae([0.0, 1.0], [1.0, float("inf")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_iae_negative_infinity_time_value():
    try:
        calculate_iae([0.0, float("-inf")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_iae_negative_infinity_error_value():
    try:
        calculate_iae([0.0, 1.0], [1.0, float("-inf")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_iae_time_not_strictly_increasing():
    try:
        calculate_iae([0.0, 1.0, 1.0], [1.0, 0.5, 0.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must be strictly increasing"

#########################################################################################
###                                      ISE
#########################################################################################

def test_calculate_ise():
    time_values = [0.0, 1.0, 2.0]
    error_values = [1.0, 0.5, 0.0]

    ise = calculate_ise(time_values, error_values)

    assert ise == pytest.approx(0.25)

def test_ise_invalid_time_values_type():
    try:
        calculate_ise("invalid", [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must be a list or tuple"

def test_ise_invalid_error_values_type():
    try:
        calculate_ise([0.0, 1.0], "invalid")
        assert False

    except TypeError as error:
        assert str(error) == "error_values must be a list or tuple"

def test_ise_empty_time_values():
    try:
        calculate_ise([], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must not be empty"

def test_ise_empty_error_values():
    try:
        calculate_ise([0.0], [])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must not be empty"

def test_ise_different_lengths():
    try:
        calculate_ise([0.0, 1.0], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values and error_values must have the same length"

def test_ise_invalid_time_value_type():
    try:
        calculate_ise([0.0, "1.0"], [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must contain only numbers"

def test_ise_invalid_error_value_type():
    try:
        calculate_ise([0.0, 1.0], [1.0, "0.5"])
        assert False

    except TypeError as error:
        assert str(error) == "error_values must contain only numbers"

def test_ise_nan_time_value():
    try:
        calculate_ise([0.0, float("nan")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_ise_nan_error_value():
    try:
        calculate_ise([0.0, 1.0], [1.0, float("nan")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_ise_positive_infinity_time_value():
    try:
        calculate_ise([0.0, float("inf")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_ise_positive_infinity_error_value():
    try:
        calculate_ise([0.0, 1.0], [1.0, float("inf")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_ise_negative_infinity_time_value():
    try:
        calculate_ise([0.0, float("-inf")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_ise_negative_infinity_error_value():
    try:
        calculate_ise([0.0, 1.0], [1.0, float("-inf")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_ise_time_not_strictly_increasing():
    try:
        calculate_ise([0.0, 1.0, 1.0], [1.0, 0.5, 0.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must be strictly increasing"

#########################################################################################
###                                     ITAE
#########################################################################################

def test_calculate_itae():
    time_values = [0.0, 1.0, 2.0]
    error_values = [1.0, 0.5, 0.0]

    itae = calculate_itae(time_values, error_values)

    assert itae == pytest.approx(0.5)

def test_itae_invalid_time_values_type():
    try:
        calculate_itae("invalid", [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must be a list or tuple"

def test_itae_invalid_error_values_type():
    try:
        calculate_itae([0.0, 1.0], "invalid")
        assert False

    except TypeError as error:
        assert str(error) == "error_values must be a list or tuple"

def test_itae_empty_time_values():
    try:
        calculate_itae([], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must not be empty"

def test_itae_empty_error_values():
    try:
        calculate_itae([0.0], [])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must not be empty"

def test_itae_different_lengths():
    try:
        calculate_itae([0.0, 1.0], [1.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values and error_values must have the same length"

def test_itae_invalid_time_value_type():
    try:
        calculate_itae([0.0, "1.0"], [1.0, 0.5])
        assert False

    except TypeError as error:
        assert str(error) == "time_values must contain only numbers"

def test_itae_invalid_error_value_type():
    try:
        calculate_itae([0.0, 1.0], [1.0, "0.5"])
        assert False

    except TypeError as error:
        assert str(error) == "error_values must contain only numbers"

def test_itae_nan_time_value():
    try:
        calculate_itae([0.0, float("nan")], [1.0, 0.5])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_itae_nan_error_value():
    try:
        calculate_itae([0.0, 1.0], [1.0, float("nan")])
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_itae_time_not_strictly_increasing():
    try:
        calculate_itae([0.0, 1.0, 1.0], [1.0, 0.5, 0.0])
        assert False

    except ValueError as error:
        assert str(error) == "time_values must be strictly increasing"

#########################################################################################
###                                   Overshoot
#########################################################################################

def test_calculate_overshoot():
    output_values = [0.0, 0.8, 1.2, 1.0]

    overshoot = calculate_overshoot(output_values, setpoint=1.0)

    assert overshoot == pytest.approx(20.0)

def test_zero_overshoot():
    output_values = [0.0, 0.5, 1.0]

    overshoot = calculate_overshoot(output_values, setpoint=1.0)

    assert overshoot == pytest.approx(0.0)

def test_overshoot_invalid_output_values_type():
    try:
        calculate_overshoot("invalid", setpoint=1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must be a list or tuple"

def test_overshoot_empty_output_values():
    try:
        calculate_overshoot([], setpoint=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must not be empty"

def test_overshoot_invalid_output_value_type():
    try:
        calculate_overshoot([0.0, "1.0"], setpoint=1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must contain only numbers"

def test_overshoot_nan_output_value():
    try:
        calculate_overshoot([0.0, float("nan")], setpoint=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_overshoot_positive_infinity_output_value():
    try:
        calculate_overshoot([0.0, float("inf")], setpoint=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_overshoot_negative_infinity_output_value():
    try:
        calculate_overshoot([0.0, float("-inf")], setpoint=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_overshoot_invalid_setpoint_type():
    try:
        calculate_overshoot([0.0, 1.0], setpoint="1.0")
        assert False

    except TypeError as error:
        assert str(error) == "setpoint must be a number"

def test_overshoot_nan_setpoint():
    try:
        calculate_overshoot([0.0, 1.0], setpoint=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_overshoot_positive_infinity_setpoint():
    try:
        calculate_overshoot([0.0, 1.0], setpoint=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_overshoot_negative_infinity_setpoint():
    try:
        calculate_overshoot([0.0, 1.0], setpoint=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_overshoot_zero_setpoint():
    try:
        calculate_overshoot([0.0, 1.0], setpoint=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must not be equal to 0"

#########################################################################################
###                                Settling time
#########################################################################################

def test_calculate_settling_time():
    time_values = [0.0, 1.0, 2.0, 3.0]
    output_values = [0.0, 0.95, 0.99, 1.0]

    settling_time = calculate_settling_time(
        time_values,
        output_values,
        setpoint=1.0
    )

    assert settling_time == pytest.approx(2.0)

def test_settling_time_not_reached():
    time_values = [0.0, 1.0, 2.0]
    output_values = [0.0, 0.5, 0.8]

    settling_time = calculate_settling_time(
        time_values,
        output_values,
        setpoint=1.0
    )

    assert settling_time is None

def test_settling_time_invalid_time_values_type():
    try:
        calculate_settling_time("invalid", [0.0, 1.0], 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "time_values must be a list or tuple"

def test_settling_time_invalid_output_values_type():
    try:
        calculate_settling_time([0.0, 1.0], "invalid", 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must be a list or tuple"

def test_settling_time_empty_time_values():
    try:
        calculate_settling_time([], [1.0], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_values must not be empty"

def test_settling_time_empty_output_values():
    try:
        calculate_settling_time([0.0], [], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must not be empty"

def test_settling_time_different_lengths():
    try:
        calculate_settling_time([0.0, 1.0], [1.0], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_values and output_values must have the same length"

def test_settling_time_invalid_time_value_type():
    try:
        calculate_settling_time([0.0, "1.0"], [0.0, 1.0], 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "time_values must contain only numbers"

def test_settling_time_invalid_output_value_type():
    try:
        calculate_settling_time([0.0, 1.0], [0.0, "1.0"], 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must contain only numbers"

def test_settling_time_nan_time_value():
    try:
        calculate_settling_time([0.0, float("nan")], [0.0, 1.0], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_settling_time_nan_output_value():
    try:
        calculate_settling_time([0.0, 1.0], [0.0, float("nan")], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_settling_time_not_strictly_increasing():
    try:
        calculate_settling_time([0.0, 1.0, 1.0], [0.0, 0.9, 1.0], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_values must be strictly increasing"

def test_settling_time_invalid_setpoint_type():
    try:
        calculate_settling_time([0.0, 1.0], [0.0, 1.0], "1.0")
        assert False

    except TypeError as error:
        assert str(error) == "setpoint must be a number"

def test_settling_time_nan_setpoint():
    try:
        calculate_settling_time([0.0, 1.0], [0.0, 1.0], float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_settling_time_invalid_tolerance_type():
    try:
        calculate_settling_time(
            [0.0, 1.0],
            [0.0, 1.0],
            1.0,
            tolerance="0.02"
        )
        assert False

    except TypeError as error:
        assert str(error) == "tolerance must be a number"

def test_settling_time_nan_tolerance():
    try:
        calculate_settling_time(
            [0.0, 1.0],
            [0.0, 1.0],
            1.0,
            tolerance=float("nan")
        )
        assert False

    except ValueError as error:
        assert str(error) == "tolerance must be finite"

def test_settling_time_zero_tolerance():
    try:
        calculate_settling_time(
            [0.0, 1.0],
            [0.0, 1.0],
            1.0,
            tolerance=0.0
        )
        assert False

    except ValueError as error:
        assert str(error) == "tolerance must be greater than 0"

def test_settling_time_negative_tolerance():
    try:
        calculate_settling_time(
            [0.0, 1.0],
            [0.0, 1.0],
            1.0,
            tolerance=-0.02
        )
        assert False

    except ValueError as error:
        assert str(error) == "tolerance must be greater than 0"

#########################################################################################
###                            Steady state error
#########################################################################################

def test_calculate_steady_state_error():
    output_values = [0.0, 0.5, 0.9]

    steady_state_error = calculate_steady_state_error(
        output_values,
        setpoint=1.0
    )

    assert steady_state_error == pytest.approx(0.1)

def test_zero_steady_state_error():
    output_values = [0.0, 0.5, 1.0]

    steady_state_error = calculate_steady_state_error(
        output_values,
        setpoint=1.0
    )

    assert steady_state_error == pytest.approx(0.0)

def test_steady_state_error_invalid_output_values_type():
    try:
        calculate_steady_state_error("invalid", 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must be a list or tuple"

def test_steady_state_error_empty_output_values():
    try:
        calculate_steady_state_error([], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must not be empty"

def test_steady_state_error_invalid_output_value_type():
    try:
        calculate_steady_state_error([0.0, "1.0"], 1.0)
        assert False

    except TypeError as error:
        assert str(error) == "output_values must contain only numbers"

def test_steady_state_error_nan_output_value():
    try:
        calculate_steady_state_error([0.0, float("nan")], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_steady_state_error_positive_infinity_output_value():
    try:
        calculate_steady_state_error([0.0, float("inf")], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_steady_state_error_negative_infinity_output_value():
    try:
        calculate_steady_state_error([0.0, float("-inf")], 1.0)
        assert False

    except ValueError as error:
        assert str(error) == "output_values must contain only finite values"

def test_steady_state_error_invalid_setpoint_type():
    try:
        calculate_steady_state_error([0.0, 1.0], "1.0")
        assert False

    except TypeError as error:
        assert str(error) == "setpoint must be a number"

def test_steady_state_error_nan_setpoint():
    try:
        calculate_steady_state_error([0.0, 1.0], float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_steady_state_error_positive_infinity_setpoint():
    try:
        calculate_steady_state_error([0.0, 1.0], float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"

def test_steady_state_error_negative_infinity_setpoint():
    try:
        calculate_steady_state_error([0.0, 1.0], float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "setpoint must be finite"