import pytest

from ml_pid_tuning.plants.second_order import SecondOrderPlant

#########################################################################################
###                                   Initial state
#########################################################################################

def test_initial_state():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    assert plant.output == 0.0
    assert plant.previous_output == 0.0

#########################################################################################
###                                     Gain input
#########################################################################################

def test_positive_gain():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.001265022)

def test_zero_gain():
    plant = SecondOrderPlant(gain=0.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_gain():
    plant = SecondOrderPlant(gain=-2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(-0.001265022)

def test_invalid_gain_type():
    try:
        plant = SecondOrderPlant(gain="2.0", time_constant_1=3.0, time_constant_2=5.0)
        assert False

    except TypeError as error:
        assert str(error) == "gain must be a number"

def test_nan_gain():
    try:
        plant = SecondOrderPlant(gain=float("nan"), time_constant_1=3.0, time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_positive_infinity_gain():
    try:
        plant = SecondOrderPlant(gain=float("inf"), time_constant_1=3.0, time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_negative_infinity_gain():
    try:
        plant = SecondOrderPlant(gain=float("-inf"), time_constant_1=3.0, time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

#########################################################################################
###                              time_constant_1 input
#########################################################################################

def test_positive_time_constant_1():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.001265022)

def test_zero_time_constant_1():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=0.0, time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_1 must be greater than 0"

def test_negative_time_constant_1():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=-3.0, time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_1 must be greater than 0"

def test_invalid_time_constant_1_type():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1="3.0", time_constant_2=5.0)
        assert False

    except TypeError as error:
        assert str(error) == "time_constant_1 must be a number"

def test_nan_time_constant_1():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=float("nan"), time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_1 must be finite"

def test_positive_infinity_time_constant_1():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=float("inf"), time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_1 must be finite"

def test_negative_infinity_time_constant_1():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=float("-inf"), time_constant_2=5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_1 must be finite"

#########################################################################################
###                              time_constant_2 input
#########################################################################################

def test_positive_time_constant_2():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.001265022)

def test_zero_time_constant_2():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_2 must be greater than 0"

def test_negative_time_constant_2():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=-5.0)
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_2 must be greater than 0"

def test_invalid_time_constant_2_type():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2="5.0")
        assert False

    except TypeError as error:
        assert str(error) == "time_constant_2 must be a number"

def test_nan_time_constant_2():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_2 must be finite"

def test_positive_infinity_time_constant_2():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_2 must be finite"

def test_negative_infinity_time_constant_2():
    try:
        plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "time_constant_2 must be finite"

#########################################################################################
###                                input_signal input
#########################################################################################

def test_positive_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.001265022)

def test_zero_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=-1.0, dt=0.1)

    assert output == pytest.approx(-0.001265022)

def test_invalid_input_signal_type():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal="1.0", dt=0.1)
        assert False

    except TypeError as error:
        assert str(error) == "input_signal must be a number"

def test_nan_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=float("nan"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_positive_infinity_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=float("inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_negative_infinity_input_signal():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=float("-inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

#########################################################################################
###                                        dt input
#########################################################################################

def test_positive_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.001265022)

def test_zero_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_negative_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt=-0.1)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_invalid_dt_type():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt="0.1")
        assert False

    except TypeError as error:
        assert str(error) == "dt must be a number"

def test_nan_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_positive_infinity_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_negative_infinity_dt():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    try:
        plant.update(input_signal=1.0, dt=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"