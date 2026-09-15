import pytest

from ml_pid_tuning.plants.transport_delay import TransportDelayPlant

#########################################################################################
###                                   Initial state
#########################################################################################

def test_initial_state():
    plant = TransportDelayPlant(delay=1.0)

    assert plant.output == 0.0
    assert plant.input_buffer == []

#########################################################################################
###                                     Delay input
#########################################################################################

def test_positive_delay():
    plant = TransportDelayPlant(delay=1.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_zero_delay():
    plant = TransportDelayPlant(delay=0.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(1.0)

def test_negative_delay():
    try:
        plant = TransportDelayPlant(delay=-1.0)
        assert False

    except ValueError as error:
        assert str(error) == "delay must be greater than or equal to 0"

def test_invalid_delay_type():
    try:
        plant = TransportDelayPlant(delay="1.0")
        assert False

    except TypeError as error:
        assert str(error) == "delay must be a number"

def test_nan_delay():
    try:
        plant = TransportDelayPlant(delay=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "delay must be finite"

def test_positive_infinity_delay():
    try:
        plant = TransportDelayPlant(delay=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "delay must be finite"

def test_negative_infinity_delay():
    try:
        plant = TransportDelayPlant(delay=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "delay must be finite"

#########################################################################################
###                                input_signal input
#########################################################################################

def test_positive_input_signal():
    plant = TransportDelayPlant(delay=0.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(1.0)

def test_zero_input_signal():
    plant = TransportDelayPlant(delay=0.0)

    output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input_signal():
    plant = TransportDelayPlant(delay=0.0)

    output = plant.update(input_signal=-1.0, dt=0.1)

    assert output == pytest.approx(-1.0)

def test_invalid_input_signal_type():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal="1.0", dt=0.1)
        assert False

    except TypeError as error:
        assert str(error) == "input_signal must be a number"

def test_nan_input_signal():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=float("nan"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_positive_infinity_input_signal():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=float("inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_negative_infinity_input_signal():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=float("-inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

#########################################################################################
###                                        dt input
#########################################################################################

def test_positive_dt():
    plant = TransportDelayPlant(delay=0.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(1.0)

def test_zero_dt():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_negative_dt():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt=-0.1)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_invalid_dt_type():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt="0.1")
        assert False

    except TypeError as error:
        assert str(error) == "dt must be a number"

def test_nan_dt():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_positive_infinity_dt():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_negative_infinity_dt():
    plant = TransportDelayPlant(delay=1.0)

    try:
        plant.update(input_signal=1.0, dt=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"