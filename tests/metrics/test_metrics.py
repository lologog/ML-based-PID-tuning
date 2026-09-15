from ml_pid_tuning.metrics.performance import calculate_iae

#########################################################################################
###                                  time_values input
#########################################################################################

def test_positive_time_values():
    iae = calculate_iae(
        time_values=[0.0, 1.0, 2.0],
        error_values=[1.0, 0.5, 0.0]
    )

    assert iae >= 0.0

def test_zero_time_values():
    try:
        iae = calculate_iae(
            time_values=[0.0, 0.0],
            error_values=[1.0, 0.5]
        )
        assert False

    except ValueError as error:
        assert str(error) == "time_values must be strictly increasing"

def test_negative_time_values():
    iae = calculate_iae(
        time_values=[-2.0, -1.0, 0.0],
        error_values=[1.0, 0.5, 0.0]
    )

    assert iae >= 0.0

def test_invalid_time_values_type():
    try:
        iae = calculate_iae(
            time_values="invalid",
            error_values=[1.0, 0.5]
        )
        assert False

    except TypeError as error:
        assert str(error) == "time_values must be a list or tuple"

def test_invalid_time_value_type():
    try:
        iae = calculate_iae(
            time_values=[0.0, "1.0"],
            error_values=[1.0, 0.5]
        )
        assert False

    except TypeError as error:
        assert str(error) == "time_values must contain only numbers"

def test_nan_time_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, float("nan")],
            error_values=[1.0, 0.5]
        )
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_positive_infinity_time_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, float("inf")],
            error_values=[1.0, 0.5]
        )
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

def test_negative_infinity_time_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, float("-inf")],
            error_values=[1.0, 0.5]
        )
        assert False

    except ValueError as error:
        assert str(error) == "time_values must contain only finite values"

#########################################################################################
###                                  error_values input
#########################################################################################

def test_positive_error_values():
    iae = calculate_iae(
        time_values=[0.0, 1.0, 2.0],
        error_values=[1.0, 0.5, 0.2]
    )

    assert iae >= 0.0

def test_zero_error_values():
    iae = calculate_iae(
        time_values=[0.0, 1.0, 2.0],
        error_values=[0.0, 0.0, 0.0]
    )

    assert iae >= 0.0

def test_negative_error_values():
    iae = calculate_iae(
        time_values=[0.0, 1.0, 2.0],
        error_values=[-1.0, -0.5, -0.2]
    )

    assert iae >= 0.0

def test_invalid_error_values_type():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values="invalid"
        )
        assert False

    except TypeError as error:
        assert str(error) == "error_values must be a list or tuple"

def test_invalid_error_value_type():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values=[1.0, "0.5"]
        )
        assert False

    except TypeError as error:
        assert str(error) == "error_values must contain only numbers"

def test_nan_error_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values=[1.0, float("nan")]
        )
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_positive_infinity_error_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values=[1.0, float("inf")]
        )
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

def test_negative_infinity_error_value():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values=[1.0, float("-inf")]
        )
        assert False

    except ValueError as error:
        assert str(error) == "error_values must contain only finite values"

#########################################################################################
###                                     Length input
#########################################################################################

def test_different_lengths():
    try:
        iae = calculate_iae(
            time_values=[0.0, 1.0],
            error_values=[1.0]
        )
        assert False

    except ValueError as error:
        assert str(error) == "time_values and error_values must have the same length"