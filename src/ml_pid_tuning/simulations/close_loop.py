from ml_pid_tuning.plants.first_order import FirstOrderPlant
from ml_pid_tuning.controllers.pid import PIDController
import matplotlib.pyplot as plt

def run_simulation():
    plant = FirstOrderPlant(gain=2.0, time_constant=5.0)
    pid = PIDController(kp=1.5, ti=4.0, td=0.5)

    setpoint = 1.0
    simulation_time = 20.0
    dt = 0.1

    current_time = 0.0
    step_number = 0

    time_values = []
    output_values = []
    setpoint_values = []
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
        control_signal_values.append(control_signal)

        if step_number % 10 == 0:
            print(f"{current_time:8.1f}\t{setpoint:8.2f}\t{plant.output:8.4f}\t{control_signal:8.4f}")

        plant.update(input_signal=control_signal, dt=dt)

        current_time += dt
        step_number += 1

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
    run_simulation()