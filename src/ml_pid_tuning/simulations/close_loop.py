from ml_pid_tuning.plants.proportional import ProportionalPlant
from ml_pid_tuning.plants.first_order import FirstOrderPlant
from ml_pid_tuning.plants.second_order import SecondOrderPlant
from ml_pid_tuning.plants.integrating import IntegratingPlant
from ml_pid_tuning.plants.integrating_first_order import IntegratingFirstOrderPlant
from ml_pid_tuning.plants.differentiating import DifferentiatingPlant
from ml_pid_tuning.plants.differentiating_first_order import DifferentiatingFirstOrderPlant
from ml_pid_tuning.plants.oscillatory_second_order import OscillatorySecondOrderPlant
from ml_pid_tuning.plants.transport_delay import TransportDelayPlant
from ml_pid_tuning.plants.first_order_transport_delay import FirstOrderTransportDelayPlant
from ml_pid_tuning.plants.second_order_transport_delay import SecondOrderTransportDelayPlant
from ml_pid_tuning.plants.unstable_first_order import UnstableFirstOrderPlant
from ml_pid_tuning.controllers.pid import PIDController
from ml_pid_tuning.metrics.performance import calculate_iae, calculate_ise, calculate_itae, calculate_overshoot, calculate_settling_time
import matplotlib.pyplot as plt

def run_simulation(plant, pid, setpoint=1.0, simulation_time=60.0, dt=0.1):
    current_time = 0.0
    step_number = 0

    time_values = []
    output_values = []
    setpoint_values = []
    error_values = []
    control_signal_values = []

    print("Closed-loop simulation with PID controller")
    print()
    print("Time [s]\tSetpoint\tOutput\t\tControl")

    while current_time <= simulation_time:
        error = setpoint - plant.output

        control_signal = pid.update(error=error, dt=dt)

        time_values.append(current_time)
        output_values.append(plant.output)
        setpoint_values.append(setpoint)
        error_values.append(error)
        control_signal_values.append(control_signal)

        if step_number % 10 == 0:
            print(f"{current_time:8.1f}\t{setpoint:8.2f}\t{plant.output:8.4f}\t{control_signal:8.4f}")

        plant.update(input_signal=control_signal, dt=dt)

        current_time += dt
        step_number += 1

    iae = calculate_iae(time_values, error_values)
    ise = calculate_ise(time_values, error_values)
    itae = calculate_itae(time_values, error_values)
    overshoot = calculate_overshoot(output_values, setpoint)
    settling_time = calculate_settling_time(time_values, output_values, setpoint)

    print()
    print("Performance metrics")
    print(f"IAE: {iae:.4f}")
    print(f"ISE: {ise:.4f}")
    print(f"ITAE: {itae:.4f}")
    print(f"Overshoot: {overshoot:.2f}%")
    print(f"Settling time: {settling_time}")

    plt.plot(time_values, output_values, label="Output")
    plt.plot(time_values, setpoint_values, label="Setpoint")

    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.title("Closed-loop PID response")
    plt.grid()
    plt.legend()

    plt.savefig("plots/closed_loop_response.png")
    plt.close()

if __name__ == "__main__":
    plant1 = ProportionalPlant(gain=2.0)
    plant2 = FirstOrderPlant(gain=2.0, time_constant=5.0)
    plant3 = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)
    plant4 = IntegratingPlant(gain=2.0)
    plant5 = IntegratingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant6 = DifferentiatingPlant(gain=2.0)
    plant7 = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant8 = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    plant9 = TransportDelayPlant(delay = 5.0)
    plant10 = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=2.0)
    plant11 = SecondOrderTransportDelayPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0, delay=2.0)
    plant12 = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    pid = PIDController(kp=1.5, ti=4.0, td=0.5)

    run_simulation(plant12, pid)