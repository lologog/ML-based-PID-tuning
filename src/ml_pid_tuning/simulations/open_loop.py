from ml_pid_tuning.plants.first_order import FirstOrderPlant
from ml_pid_tuning.plants.second_order import SecondOrderPlant

import matplotlib.pyplot as plt

def run_simulation(plant, input_signal=1.0, simulation_time=60.0, dt=0.1):
    current_time = 0.0
    step_number = 0

    time_values = []
    output_values = []

    print("Open-loop simulation")
    print()
    print("Time [s]\tInput\tOutput")

    while current_time <= simulation_time:
        time_values.append(current_time)
        output_values.append(plant.output)

        if step_number % 10 == 0:
            print(f"{current_time:8.1f}\t{input_signal:5.2f}\t{plant.output:6.4f}")

        plant.update(input_signal=input_signal, dt=dt)

        current_time += dt
        step_number += 1

    plt.plot(time_values, output_values)

    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.title("Open-loop step response")
    plt.grid()

    plt.savefig("plots/step_response.png")
    plt.close()

if __name__ == "__main__":
    plant1 = FirstOrderPlant(gain=2.0, time_constant=5.0)
    plant2 = SecondOrderPlant(gain=2.0, time_constant_1=3.0, time_constant_2=5.0)

    run_simulation(plant2)