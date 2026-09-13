import pytest
from ml_pid_tuning.plants.oscillatory_second_order import OscillatorySecondOrderPlant

def test_initial_output():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    assert plant.output == 0.0

def test_positive_input():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.004750594)

def test_zero_input():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-0.004750594)

def test_output_oscillates_for_positive_step():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)

    output_values = []

    for _ in range(200):
        output_values.append(plant.update(input_signal=1.0, dt=0.1))

    assert max(output_values) > 2.0

def test_output_approaches_steady_state():
    plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)

    for _ in range(1000):
        plant.update(input_signal=1.0, dt=0.1)

    assert plant.output == pytest.approx(2.0, rel=1e-3)

def test_lower_damping_ratio_gives_larger_overshoot():
    low_damping_plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.2)
    high_damping_plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.8)

    low_damping_outputs = []
    high_damping_outputs = []

    for _ in range(300):
        low_damping_outputs.append(low_damping_plant.update(input_signal=1.0, dt=0.1))
        high_damping_outputs.append(high_damping_plant.update(input_signal=1.0, dt=0.1))

    assert max(low_damping_outputs) > max(high_damping_outputs)

def test_larger_natural_frequency_gives_faster_response():
    slow_plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.3, damping_ratio=0.5)
    fast_plant = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=1.0, damping_ratio=0.5)

    for _ in range(20):
        slow_plant.update(input_signal=1.0, dt=0.1)
        fast_plant.update(input_signal=1.0, dt=0.1)

    assert fast_plant.output > slow_plant.output

def test_larger_dt_gives_larger_first_step():
    plant_1 = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    plant_2 = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    output_1 = plant_1.update(input_signal=1.0, dt=0.1)
    output_2 = plant_2.update(input_signal=1.0, dt=0.5)
    assert output_1 == pytest.approx(0.004750594)
    assert output_2 == pytest.approx(0.095238095)
    assert output_2 > output_1