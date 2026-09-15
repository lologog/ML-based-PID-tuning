import pytest

from ml_pid_tuning.controllers.pid import PIDController

#########################################################################################
###                                   Initial state
#########################################################################################

def test_initial_state():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    assert controller.integral == 0.0
    assert controller.previous_error == 0.0

#########################################################################################
###                                      kp input
#########################################################################################

def test_positive_kp():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.04)

def test_zero_kp():
    controller = PIDController(kp=0.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(0.0)

def test_negative_kp():
    controller = PIDController(kp=-2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(-22.04)

def test_invalid_kp_type():
    try:
        controller = PIDController(kp="2.0", ti=5.0, td=1.0)
        assert False

    except TypeError as error:
        assert str(error) == "kp must be a number"

def test_nan_kp():
    try:
        controller = PIDController(kp=float("nan"), ti=5.0, td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "kp must be finite"

def test_positive_infinity_kp():
    try:
        controller = PIDController(kp=float("inf"), ti=5.0, td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "kp must be finite"

def test_negative_infinity_kp():
    try:
        controller = PIDController(kp=float("-inf"), ti=5.0, td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "kp must be finite"

#########################################################################################
###                                      ti input
#########################################################################################

def test_positive_ti():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.04)

def test_zero_ti():
    controller = PIDController(kp=2.0, ti=0.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.0)

def test_negative_ti():
    try:
        controller = PIDController(kp=2.0, ti=-5.0, td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "ti must be greater than or equal to 0"

def test_invalid_ti_type():
    try:
        controller = PIDController(kp=2.0, ti="5.0", td=1.0)
        assert False

    except TypeError as error:
        assert str(error) == "ti must be a number"

def test_nan_ti():
    try:
        controller = PIDController(kp=2.0, ti=float("nan"), td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "ti must be finite"

def test_positive_infinity_ti():
    try:
        controller = PIDController(kp=2.0, ti=float("inf"), td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "ti must be finite"

def test_negative_infinity_ti():
    try:
        controller = PIDController(kp=2.0, ti=float("-inf"), td=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "ti must be finite"

#########################################################################################
###                                      td input
#########################################################################################

def test_positive_td():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.04)

def test_zero_td():
    controller = PIDController(kp=2.0, ti=5.0, td=0.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(2.04)

def test_negative_td():
    try:
        controller = PIDController(kp=2.0, ti=5.0, td=-1.0)
        assert False

    except ValueError as error:
        assert str(error) == "td must be greater than or equal to 0"

def test_invalid_td_type():
    try:
        controller = PIDController(kp=2.0, ti=5.0, td="1.0")
        assert False

    except TypeError as error:
        assert str(error) == "td must be a number"

def test_nan_td():
    try:
        controller = PIDController(kp=2.0, ti=5.0, td=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "td must be finite"

def test_positive_infinity_td():
    try:
        controller = PIDController(kp=2.0, ti=5.0, td=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "td must be finite"

def test_negative_infinity_td():
    try:
        controller = PIDController(kp=2.0, ti=5.0, td=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "td must be finite"

#########################################################################################
###                                    error input
#########################################################################################

def test_positive_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.04)

def test_zero_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=0.0, dt=0.1)

    assert control_signal == pytest.approx(0.0)

def test_negative_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=-1.0, dt=0.1)

    assert control_signal == pytest.approx(-22.04)

def test_invalid_error_type():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error="1.0", dt=0.1)
        assert False

    except TypeError as error:
        assert str(error) == "error must be a number"

def test_nan_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=float("nan"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "error must be finite"

def test_positive_infinity_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=float("inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "error must be finite"

def test_negative_infinity_error():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=float("-inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "error must be finite"

#########################################################################################
###                                        dt input
#########################################################################################

def test_positive_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    control_signal = controller.update(error=1.0, dt=0.1)

    assert control_signal == pytest.approx(22.04)

def test_zero_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_negative_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt=-0.1)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_invalid_dt_type():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt="0.1")
        assert False

    except TypeError as error:
        assert str(error) == "dt must be a number"

def test_nan_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_positive_infinity_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_negative_infinity_dt():
    controller = PIDController(kp=2.0, ti=5.0, td=1.0)

    try:
        controller.update(error=1.0, dt=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"