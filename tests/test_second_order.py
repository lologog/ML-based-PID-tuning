import pytest
from ml_pid_tuning.plants.second_order import SecondOrderPlant

def test_initial_output():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.001265022)

def test_zero_input():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-0.001265022)

def test_output_increases_for_positive_step():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=1.0, dt=0.1)
    output_3 = plant.update(input_signal=1.0, dt=0.1)
    assert output_1 < output_2 < output_3

def test_output_approaches_steady_state():
    plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    for _ in range(2000):
        plant.update(input_signal=1.0, dt=0.1)

    assert plant.output == pytest.approx(2.0, rel=1e-3)

def test_larger_time_constants_give_slower_response():
    fast_plant = SecondOrderPlant(gain=2.0, time_constant_1=1.0, time_constant_2=2.0)
    slow_plant = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    for _ in range(10):
        fast_plant.update(input_signal=1.0, dt=0.1)
        slow_plant.update(input_signal=1.0, dt=0.1)

    assert fast_plant.output > slow_plant.output

def test_larger_dt_gives_larger_first_step():
    plant_1 = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    plant_2 = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.001265022)
    assert output_2 == pytest.approx(0.025974026)
    assert output_2 > output_1