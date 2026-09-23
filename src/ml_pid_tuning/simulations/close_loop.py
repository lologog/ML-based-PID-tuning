import csv
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
from ml_pid_tuning.plants.first_order_zero import FirstOrderZeroPlant

from ml_pid_tuning.controllers.pid import PIDController
from ml_pid_tuning.metrics.performance import calculate_iae, calculate_ise, calculate_itae, calculate_overshoot, calculate_settling_time, calculate_steady_state_error, calculate_max_control, calculate_isu
import matplotlib.pyplot as plt

def run_simulation(plant, controller, setpoint, simulation_time, dt):
    current_time = 0.0

    time_values = []
    output_values = []
    setpoint_values = []
    error_values = []
    control_signal_values = []

    while current_time <= simulation_time:
        error = setpoint - plant.output
        control_signal = controller.update(error=error, dt=dt)

        time_values.append(current_time)
        output_values.append(plant.output)
        setpoint_values.append(setpoint)
        error_values.append(error)
        control_signal_values.append(control_signal)

        plant.update(input_signal=control_signal, dt=dt)

        current_time += dt

    iae = calculate_iae(time_values, error_values)
    ise = calculate_ise(time_values, error_values)
    itae = calculate_itae(time_values, error_values)
    overshoot = calculate_overshoot(output_values, setpoint)
    settling_time = calculate_settling_time(time_values, output_values, setpoint)
    steady_state_error = calculate_steady_state_error(output_values, setpoint)
    max_control = calculate_max_control(control_signal_values)
    isu = calculate_isu(time_values, control_signal_values)

    return {
        "time": time_values,
        "output": output_values,
        "setpoint": setpoint_values,
        "error": error_values,
        "control_signal": control_signal_values,
        "iae": iae,
        "ise": ise,
        "itae": itae,
        "overshoot": overshoot,
        "settling_time": settling_time,
        "steady_state_error": steady_state_error,
        "max_control": max_control,
        "isu": isu
    }

if __name__ == "__main__":
    plant1 = ProportionalPlant(gain=2.0)
    plant2 = FirstOrderPlant(gain=2.2585, time_constant=2.2869)
    plant3 = SecondOrderPlant(gain=4.958, time_constant_1=3.5553, time_constant_2=7.8527)
    plant4 = IntegratingPlant(gain=2.0)
    plant5 = IntegratingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant6 = DifferentiatingPlant(gain=2.0)
    plant7 = DifferentiatingFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant8 = OscillatorySecondOrderPlant(gain=2.0, natural_frequency=0.5, damping_ratio=0.5)
    plant9 = TransportDelayPlant(delay = 5.0)
    plant10 = FirstOrderTransportDelayPlant(gain=2.0, time_constant=5.0, delay=2.0)
    plant11 = SecondOrderTransportDelayPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0, delay=2.0)
    plant12 = UnstableFirstOrderPlant(gain=2.0, time_constant=5.0)
    plant13 = FirstOrderZeroPlant(gain=2.0, time_constant=5.0, zero_time_constant=2.0)

    pid = PIDController(kp=1.2966, ti=9.8089, td=1.3689)

    results = run_simulation(plant=plant3, controller=pid, setpoint=10.0, simulation_time=60.0, dt=0.1)

    with open("src/ml_pid_tuning/simulations/data/closed_loop_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "setpoint", "output", "error", "control_signal"])

        for i in range(len(results["time"])):
            writer.writerow([results["time"][i], results["setpoint"][i], results["output"][i], results["error"][i], results["control_signal"][i]])

    print("Performance metrics")
    print("IAE:", round(results["iae"], 4))
    print("ISE:", round(results["ise"], 4))
    print("ITAE:", round(results["itae"], 4))
    print("Overshoot:", round(results["overshoot"], 2), "%")
    print("Settling time:", results["settling_time"])
    print("Steady-state error:", round(results["steady_state_error"], 4))
    print("Max control signal:", round(results["max_control"], 4))
    print("ISU:", round(results["isu"], 4))

    plt.plot(results["time"], results["output"], label="Output")
    plt.plot(results["time"], results["setpoint"], label="Setpoint")
    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.title("Closed-loop PID response")
    plt.grid()
    plt.legend()
    plt.savefig("plots/closed_loop_response.png")
    plt.close()

    plt.plot(results["time"], results["control_signal"], label="Control signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Control signal")
    plt.title("PID control signal")
    plt.grid()
    plt.legend()
    plt.savefig("plots/control_signal.png")
    plt.close()
