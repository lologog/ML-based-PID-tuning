import pytest
from ml_pid_tuning.plants.differentiating import DifferentiatingPlant

def test_initial_output():
    plant = DifferentiatingPlant(gain=2.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = DifferentiatingPlant(gain=2.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(20.0)

def test_zero_input():
    plant = DifferentiatingPlant(gain=2.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = DifferentiatingPlant(gain=2.0)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-20.0)

def test_constant_input_gives_zero_output_after_first_step():
    plant = DifferentiatingPlant(gain=2.0)
    plant.update(input_signal=1.0, dt=0.1)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_output_reacts_to_input_change():
    plant = DifferentiatingPlant(gain=2.0)
    plant.update(input_signal=1.0, dt=0.1)
    output = plant.update(input_signal=2.0, dt=0.1)
    assert output == pytest.approx(20.0)

def test_smaller_dt_gives_larger_output():
    plant_1 = DifferentiatingPlant(gain=2.0)
    plant_2 = DifferentiatingPlant(gain=2.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(20.0)
    assert output_2 == pytest.approx(4.0)
    assert output_1 > output_2