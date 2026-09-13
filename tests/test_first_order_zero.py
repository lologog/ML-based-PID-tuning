import pytest
from ml_pid_tuning.plants.first_order_zero import FirstOrderZeroPlant

def test_initial_output():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.823529412)

def test_zero_input():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-0.823529412)

def test_output_increases_for_positive_step():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=1.0, dt=0.1)
    output_3 = plant.update(input_signal=1.0, dt=0.1)
    assert output_1 < output_2 < output_3

def test_output_approaches_steady_state():
    plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)

    for _ in range(1000):
        plant.update(input_signal=1.0, dt=0.1)

    assert plant.output == pytest.approx(2.0, rel=1e-3)

def test_larger_zero_time_constant_gives_larger_first_response():
    plant_1 = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=1.0)
    plant_2 = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=3.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.1)
    assert output_2 > output_1

def test_larger_time_constant_gives_slower_response():
    fast_plant = FirstOrderZeroPlant(gain=2.0, time_constant=3.0, zero_time_constant=2.0)
    slow_plant = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    fast_output = fast_plant.update(input_signal=1.0, dt=0.1)
    slow_output = slow_plant.update(input_signal=1.0, dt=0.1)
    assert fast_output > slow_output

def test_larger_dt_gives_larger_first_step():
    plant_1 = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    plant_2 = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.823529412)
    assert output_2 == pytest.approx(0.909090909)
    assert output_2 > output_1