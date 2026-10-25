import math
from scipy.optimize import differential_evolution
from ml_pid_tuning.controllers.pid import PIDController
from ml_pid_tuning.simulations.close_loop import run_simulation


def objective(parameters, plant_factory):
    kp, ti, td = parameters

    plant = plant_factory()
    controller = PIDController(kp=kp, ti=ti, td=td)

    try:
        results = run_simulation(plant=plant, controller=controller, setpoint=10.0, simulation_time=60.0, dt=0.1)
        itae = results["itae"]
        control_signal = results["control_signal"]

        if not math.isfinite(itae):
            return 1000000000.0

        # Penalty for exceeding control signal limits
        max_control = max(abs(value) for value in control_signal)
        control_limit = 20.0
        control_excess = max(0.0, max_control - control_limit)
        control_penalty = control_excess ** 2

        objective_value = itae + control_penalty

        return objective_value

    except (ValueError, OverflowError):
        return 1000000000.0

def optimize_pid(plant_factory):
    bounds = [(0.01, 10.0), (0.1, 50.0), (0.0, 10.0)]
    result = differential_evolution(objective, bounds, args=(plant_factory,))
    best_kp, best_ti, best_td = result.x
    return {
        "kp": best_kp,
        "ti": best_ti,
        "td": best_td,
        "objective": result.fun
    }
