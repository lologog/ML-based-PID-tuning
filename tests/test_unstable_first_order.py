import pytest
from ml_pid_tuning.plants.unstable_first_order import UnstableFirstOrderPlant

def test_initial_output():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.040816327)


def test_zero_input():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)


def test_negative_input():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-0.040816327)

def test_output_increases_for_positive_step():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=1.0, dt=0.1)
    output_3 = plant.update(input_signal=1.0, dt=0.1)
    assert output_1 < output_2 < output_3

def test_output_keeps_growing_for_constant_input():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)

    for _ in range(100):
        plant.update(input_signal=1.0, dt=0.1)

    output_1 = plant.output

    for _ in range(100):
        plant.update(input_signal=1.0, dt=0.1)

    output_2 = plant.output

    assert output_2 > output_1

def test_output_continues_growing_after_input_becomes_zero():
    plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output_before = plant.update(input_signal=1.0, dt=0.1)
    output_after = plant.update(input_signal=0.0, dt=0.1)
    assert output_after > output_before

def test_larger_time_constant_gives_slower_response():
    fast_plant = UnstableFirstOrderPlant(gain=2.0, time_constant=2.0)
    slow_plant = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    fast_output = fast_plant.update(input_signal=1.0, dt=0.1)
    slow_output = slow_plant.update(input_signal=1.0, dt=0.1)
    assert fast_output > slow_output

def test_larger_dt_gives_larger_first_step():
    plant_1 = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant_2 = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.040816327)
    assert output_2 == pytest.approx(0.222222222)
    assert output_2 > output_1