import pytest
from ml_pid_tuning.plants.differentiating_first_order import DifferentiatingFirstOrderPlant

def test_initial_output():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.392156863)

def test_zero_input():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-0.392156863)

def test_output_decays_for_constant_input():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=1.0, dt=0.1)
    output_3 = plant.update(input_signal=1.0, dt=0.1)
    assert output_1 > output_2 > output_3 > 0.0

def test_output_approaches_zero_for_constant_input():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)

    for _ in range(1000):
        plant.update(input_signal=1.0, dt=0.1)

    assert plant.output == pytest.approx(0.0, abs=1e-6)

def test_output_reacts_to_input_change():
    plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant.update(input_signal=1.0, dt=0.1)
    output_before_change = plant.update(input_signal=1.0, dt=0.1)
    output_after_change = plant.update(input_signal=2.0, dt=0.1)
    assert output_after_change > output_before_change

def test_larger_time_constant_gives_slower_decay():
    fast_plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=1.0)
    slow_plant = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    fast_output_1 = fast_plant.update(input_signal=1.0, dt=0.1)
    fast_output_2 = fast_plant.update(input_signal=1.0, dt=0.1)
    slow_output_1 = slow_plant.update(input_signal=1.0, dt=0.1)
    slow_output_2 = slow_plant.update(input_signal=1.0, dt=0.1)
    fast_decay_ratio = fast_output_2 / fast_output_1
    slow_decay_ratio = slow_output_2 / slow_output_1
    assert slow_decay_ratio > fast_decay_ratio

def test_smaller_dt_gives_larger_first_step_response():
    plant_1 = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant_2 = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.392156863)
    assert output_2 == pytest.approx(0.363636364)
    assert output_1 > output_2