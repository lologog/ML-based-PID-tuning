import pytest

from ml_pid_tuning.plants.oscillatory_second_order import OscillatorySecondOrderPlant

#########################################################################################
###                                   Initial state
#########################################################################################

def test_initial_state():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    assert plant.output == 0.0
    assert plant.previous_output == 0.0

#########################################################################################
###                                     Gain input
#########################################################################################

def test_positive_gain():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.064516129)

def test_zero_gain():
    plant = OscillatorySecondOrderPlant(gain=0.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_gain():
    plant = OscillatorySecondOrderPlant(gain=-2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(-0.064516129)

def test_invalid_gain_type():
    try:
        plant = OscillatorySecondOrderPlant(gain="2.0", natural_frequency=2.0, damping_ratio=0.5)
        assert False

    except TypeError as error:
        assert str(error) == "gain must be a number"

def test_nan_gain():
    try:
        plant = OscillatorySecondOrderPlant(gain=float("nan"), natural_frequency=2.0, damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_positive_infinity_gain():
    try:
        plant = OscillatorySecondOrderPlant(gain=float("inf"), natural_frequency=2.0, damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

def test_negative_infinity_gain():
    try:
        plant = OscillatorySecondOrderPlant(gain=float("-inf"), natural_frequency=2.0, damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "gain must be finite"

#########################################################################################
###                              natural_frequency input
#########################################################################################

def test_positive_natural_frequency():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.064516129)

def test_zero_natural_frequency():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.0, damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "natural_frequency must be greater than 0"

def test_negative_natural_frequency():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=-2.0, damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "natural_frequency must be greater than 0"

def test_invalid_natural_frequency_type():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency="2.0", damping_ratio=0.5)
        assert False

    except TypeError as error:
        assert str(error) == "natural_frequency must be a number"

def test_nan_natural_frequency():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=float("nan"), damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "natural_frequency must be finite"

def test_positive_infinity_natural_frequency():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=float("inf"), damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "natural_frequency must be finite"

def test_negative_infinity_natural_frequency():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=float("-inf"), damping_ratio=0.5)
        assert False

    except ValueError as error:
        assert str(error) == "natural_frequency must be finite"

#########################################################################################
###                                damping_ratio input
#########################################################################################

def test_positive_damping_ratio():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.064516129)

def test_zero_damping_ratio():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.0)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.076923077)

def test_negative_damping_ratio():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=-0.5)
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be greater than or equal to 0 and less than 1"

def test_damping_ratio_equal_to_one():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=1.0)
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be greater than or equal to 0 and less than 1"

def test_damping_ratio_greater_than_one():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=1.5)
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be greater than or equal to 0 and less than 1"

def test_invalid_damping_ratio_type():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio="0.5")
        assert False

    except TypeError as error:
        assert str(error) == "damping_ratio must be a number"

def test_nan_damping_ratio():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be finite"

def test_positive_infinity_damping_ratio():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be finite"

def test_negative_infinity_damping_ratio():
    try:
        plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "damping_ratio must be finite"

#########################################################################################
###                                input_signal input
#########################################################################################

def test_positive_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.064516129)

def test_zero_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=-1.0, dt=0.1)

    assert output == pytest.approx(-0.064516129)

def test_invalid_input_signal_type():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal="1.0", dt=0.1)
        assert False

    except TypeError as error:
        assert str(error) == "input_signal must be a number"

def test_nan_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=float("nan"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_positive_infinity_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=float("inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

def test_negative_infinity_input_signal():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=float("-inf"), dt=0.1)
        assert False

    except ValueError as error:
        assert str(error) == "input_signal must be finite"

#########################################################################################
###                                        dt input
#########################################################################################

def test_positive_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    output = plant.update(input_signal=1.0, dt=0.1)

    assert output == pytest.approx(0.064516129)

def test_zero_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt=0.0)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_negative_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt=-0.1)
        assert False

    except ValueError as error:
        assert str(error) == "dt must be greater than 0"

def test_invalid_dt_type():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt="0.1")
        assert False

    except TypeError as error:
        assert str(error) == "dt must be a number"

def test_nan_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt=float("nan"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_positive_infinity_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt=float("inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"

def test_negative_infinity_dt():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=2.0, damping_ratio=0.5)

    try:
        plant.update(input_signal=1.0, dt=float("-inf"))
        assert False

    except ValueError as error:
        assert str(error) == "dt must be finite"