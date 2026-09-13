import pytest
from ml_pid_tuning.plants.first_order_transport_delay import FirstOrderTransportDelayPlant

def test_initial_output():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)
    assert plant.output == 0.0

def test_positive_input():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(30):
        plant.update(input_signal=1.0, dt=0.1)

    output = plant.update(input_signal=1.0, dt=0.1)
    assert output == pytest.approx(0.039215686)

def test_zero_input():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(40):
        output = plant.update(input_signal=0.0, dt=0.1)

    assert output == pytest.approx(0.0)

def test_negative_input():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(30):
        plant.update(input_signal=-1.0, dt=0.1)

    output = plant.update(input_signal=-1.0, dt=0.1)

    assert output == pytest.approx(-0.039215686)

def test_output_is_zero_during_delay():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(30):
        output = plant.update(input_signal=1.0, dt=0.1)
        assert output == pytest.approx(0.0)

def test_output_increases_after_delay():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(30):
        plant.update(input_signal=1.0, dt=0.1)

    output_1 = plant.update(input_signal=1.0, dt=0.1)
    output_2 = plant.update(input_signal=1.0, dt=0.1)
    output_3 = plant.update(input_signal=1.0, dt=0.1)
    assert output_1 < output_2 < output_3

def test_output_approaches_steady_state():
    plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(1000):
        plant.update(input_signal=1.0, dt=0.1)

    assert plant.output == pytest.approx(2.0, rel=1e-3)

def test_larger_delay_gives_slower_response():
    short_delay_plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=2.0)
    long_delay_plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=5.0)

    for _ in range(40):
        short_delay_plant.update(input_signal=1.0, dt=0.1)
        long_delay_plant.update(input_signal=1.0, dt=0.1)

    assert short_delay_plant.output > long_delay_plant.output

def test_larger_time_constant_gives_slower_response():
    fast_plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=1.0, delay=3.0)
    slow_plant = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(31):
        fast_plant.update(input_signal=1.0, dt=0.1)
        slow_plant.update(input_signal=1.0, dt=0.1)

    assert fast_plant.output > slow_plant.output

def test_larger_dt_gives_larger_first_step():
    plant_1 = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)
    plant_2 = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=3.0)

    for _ in range(30):
        plant_1.update(input_signal=1.0, dt=0.1)

    output_1 = plant_1.update(input_signal=1.0, dt=0.1)

    for _ in range(6):
        plant_2.update(input_signal=1.0, dt=0.5)

    output_2 = plant_2.update(input_signal=1.0, dt=0.5)

    assert output_2 > output_1