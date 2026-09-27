import csv
import random
from ml_pid_tuning.plants.integrating_first_order import IntegratingFirstOrderPlant
from ml_pid_tuning.optimization.differential_evolution import optimize_pid

def main():
    number_of_samples = 100

    with open("src/ml_pid_tuning/data/datasets/integrating_first_order_dataset.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["gain", "time_constant", "kp", "ti", "td", "objective"])

        for _ in range(number_of_samples):
            gain = random.uniform(0.5, 5.0)
            time_constant = random.uniform(1.0, 10.0)

            plant_factory = lambda: IntegratingFirstOrderPlant(gain=gain, time_constant=time_constant)
            result = optimize_pid(plant_factory)

            writer.writerow([gain, time_constant, result["kp"], result["ti"], result["td"], result["objective"]])

            print("Generated:", round(gain, 4), round(time_constant, 4))

if __name__ == "__main__":
    main()