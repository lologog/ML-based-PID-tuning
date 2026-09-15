import pytest

from ml_pid_tuning.plants.differentiating import DifferentiatingPlant

#########################################################################################
###                                   Initial state
#########################################################################################

def test_initial_state():
    plant = DifferentiatingPlant(gain=2.0)

    assert plant.output == 0.0
    assert plant.previous_input == 0.0

#########################################################################################
###                                     Gain input
#########################################################################################

def test_positive_gain():
    plant = DifferentiatingPlant(gain=2.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(20.0)

def test_zero_gain():
    plant = DifferentiatingPlant(gain=0.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_gain():
    plant = DifferentiatingPlant(gain=-2.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(-20.0)

def test_invalid_gain_type():
    try:
        plant = DifferentiatingPlant(gain="2.0")
        assert False

    except TypeError as error:
        assert str(error) == "gain must be a number"

def test_nan_gain():
    try:
        plant = DifferentiatingPlant(gain=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_positive_infinity_gain():
    try:
        plant = DifferentiatingPlant(gain=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_negative_infinity_gain():
    try:
        plant = DifferentiatingPlant(gain=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

#########################################################################################
###                                input_signal input
#########################################################################################

def test_positive_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(20.0)

def test_zero_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    output = plant.update(input_signal=-1.0, dt=0.1)

    assert output == pytest.approx(-20.0)

def test_invalid_input_signal_type():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal="1.0", dt=0.1)
        assert False

    except TypeError as error:
        assert str(error) == "input_signal must be a number"

def test_nan_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=float("nan"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_positive_infinity_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=float("inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_negative_infinity_input_signal():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=float("-inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

#########################################################################################
###                                        dt input
#########################################################################################

def test_positive_dt():
    plant = DifferentiatingPlant(gain=2.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(20.0)

def test_zero_dt():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_negative_dt():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt=-0.1)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_invalid_dt_type():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt="0.1")
        assert False

    except TypeError as error:
        assert str(error) == "dt must be a number"

def test_nan_dt():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_positive_infinity_dt():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_negative_infinity_dt():
    plant = DifferentiatingPlant(gain=2.0)

    try:
        plant.update(input_signal=1.0, dt=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"