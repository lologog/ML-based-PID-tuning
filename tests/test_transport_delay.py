import pytest
from ml_pid_tuning.plants.transport_delay import TransportDelayPlant

def test_initial_output():
    plant = TransportDelayPlant(delay=3.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = TransportDelayPlant(delay=3.0)

    for _ in range(30):
        plant.update(input_signal=1.0, dt=0.1)

    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(1.0)

def test_zero_input():
    plant = TransportDelayPlant(delay=3.0)

    for _ in range(31):
        output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = TransportDelayPlant(delay=3.0)

    for _ in range (30):
        plant.update(input_signal=-1.0, dt=0.1)

    output = plant.update(input_signal=-1.0, dt=0.1)
    assert output == pytest.approx(-1.0)

def test_output_is_zero_during_delay():
    plant = TransportDelayPlant(delay=3.0)

    for _ in range(30):
        output = plant.update(input_signal=1.0, dt=0.1)
        assert output == pytest.approx(0.0)

def test_input_is_reproduced_after_delay():
    plant = TransportDelayPlant(delay=3.0)
    plant.update(input_signal=3.0, dt=0.1)

    for _ in range(29):
        plant.update(input_signal=0.0, dt=0.1)

    output = plant.update(input_signal=0.0, dt=0.1)
    assert output == pytest.approx(3.0)

def test_constant_input_is_passed_without_change():
    plant = TransportDelayPlant(delay=3.0)

    for _ in range(30):
        plant.update(input_signal=2.0, dt=0.1)

    output = plant.update(input_signal=2.0, dt=0.1)
    assert output == pytest.approx(2.0)

def test_larger_delay_gives_slower_response():
    short_delay_plant = TransportDelayPlant(delay=2.0)
    long_delay_plant = TransportDelayPlant(delay=5.0)

    for _ in range(30):
        short_delay_plant.update(input_signal=1.0, dt=0.1)
        long_delay_plant.update(input_signal=1.0, dt=0.1)

    assert short_delay_plant.output == pytest.approx(1.0)
    assert long_delay_plant.output == pytest.approx(0.0)

def test_larger_dt_requires_fewer_delay_steps():
    plant_1 = TransportDelayPlant(delay=3.0)
    plant_2 = TransportDelayPlant(delay=3.0)

    for _ in range(30):
        plant_1.update(input_signal=1.0, dt=0.1)

    output_1 = plant_1.update(input_signal=1.0, dt=0.1)

    for _ in range(6):
        plant_2.update(input_signal=1.0, dt=0.5)

    output_2 = plant_2.update(input_signal=1.0, dt=0.5)

    assert output_1 == pytest.approx(1.0)
    assert output_2 == pytest.approx(1.0)