import pytest
from ml_pid_tuning.plants.integrating import IntegratingPlant

def test_initial_output():
    plant = IntegratingPlant(gain=2.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = IntegratingPlant(gain=2.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.2)

def test_output_accumulates():
    plant = IntegratingPlant(gain=2.0)
    plant.update(input_signal=1.0, dt=0.1)
    plant.update(input_signal=1.0, dt=0.1)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.6)

def test_zero_input_keeps_output():
    plant = IntegratingPlant(gain=2.0)
    plant.update(input_signal=1.0, dt=0.1)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.2)

def test_negative_input_decreases_output():
    plant = IntegratingPlant(gain=2.0)
    plant.update(input_signal=1.0, dt=0.1)
    output = plant.update(input_signal=-0.5, dt=0.1)
    assert output == pytest.approx(0.1)

def test_dt_affects_output():
    plant_1 = IntegratingPlant(gain=2.0)
    plant_2 = IntegratingPlant(gain=2.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.2)
    assert output_2 == pytest.approx(1.0)
