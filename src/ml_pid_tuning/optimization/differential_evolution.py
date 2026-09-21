import math
from scipy.optimize import differential_evolution
from ml_pid_tuning.plants.first_order import FirstOrderPlant
from ml_pid_tuning.controllers.pid import PIDController
from ml_pid_tuning.simulations.close_loop import run_simulation


def objective(parameters):
    kp, ti, td = parameters

    plant = FirstOrderPlant(gain=2.0, time_constant=5.0)
    controller = PIDController(kp=kp, ti=ti, td=td)

    try:
        results = run_simulation(plant=plant, controller=controller, setpoint=10.0, simulation_time=60.0, dt=0.1)
        itae = results["itae"]

        if not math.isfinite(itae):
            return 1000000000.0

        max_control = max(abs(value) for value in results["control_signal"])
        penalty = 0.0

        if max_control > 20.0:
            penalty = (max_control - 20.0) ** 2

        return itae + penalty

    except (ValueError, OverflowError):
        return 1000000000.0


def main():
    bounds = [(0.01, 10.0), (0.1, 20.0), (0.0, 5.0)]

    result = differential_evolution(objective, bounds)
    best_kp, best_ti, best_td = result.x

    print("Best PID parameters")
    print("Kp:", round(best_kp, 4))
    print("Ti:", round(best_ti, 4))
    print("Td:", round(best_td, 4))
    print("Objective value:", round(result.fun, 4))


if __name__ == "__main__":
    main()