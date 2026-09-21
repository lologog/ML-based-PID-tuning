import csv
import random
from ml_pid_tuning.plants.second_order import SecondOrderPlant
from ml_pid_tuning.optimization.differential_evolution import optimize_pid


def main():
    number_of_samples = 100

    with open("src/ml_pid_tuning/data/datasets/second_order_dataset.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["gain", "time_constant_1", "time_constant_2", "kp", "ti", "td", "objective"])

        for _ in range(number_of_samples):
            gain = random.uniform(0.5, 5.0)
            time_constant_1 = random.uniform(1.0, 10.0)
            time_constant_2 = random.uniform(1.0, 10.0)

            plant_factory = lambda: SecondOrderPlant(gain=gain, time_constant_1=time_constant_1, time_constant_2=time_constant_2)
            result = optimize_pid(plant_factory)

            writer.writerow([gain, time_constant_1, time_constant_2, result["kp"], result["ti"], result["td"], result["objective"]])

            print("Generated:", round(gain, 4), round(time_constant_1, 4), round(time_constant_2, 4))

if __name__ == "__main__":
    main()