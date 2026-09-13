import pytest
from ml_pid_tuning.plants.proportional import ProportionalPlant

def test_initial_output():
    plant = ProportionalPlant(gain=2.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = ProportionalPlant(gain=2.0)
    output = plant.update(input_signal=3.0, dt=0.1)
    assert output == pytest.approx(6.0)

def test_zero_input():
    plant = ProportionalPlant(gain=2.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = ProportionalPlant(gain=2.0)
    output = plant.update(input_signal=-3.0, dt=0.1)
    assert output == pytest.approx(-6.0)

def test_output_changes_immediately():
    plant = ProportionalPlant(gain=2.0)
    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=4.0, dt=0.1)
    assert output_1 == pytest.approx(2.0)
    assert output_2 == pytest.approx(8.0)

def test_dt_does_not_affect_output():
    plant = ProportionalPlant(gain=2.0)
    output_1 = plant.update(input_signal=3.0, dt=0.1)
    output_2 = plant.update(input_signal=3.0, dt=1.0)
    assert output_1 == pytest.approx(output_2)