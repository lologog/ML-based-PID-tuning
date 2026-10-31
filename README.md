# Machine Learning-Based PID Controller Tuning

## Overview

This project investigates supervised regression for PID controller tuning in simulated dynamic systems. Differential evolution generates reference controller settings by minimizing tracking error. Regression models then learn to predict proportional gain, integral time, and derivative time from known plant parameters.

The objective is to approximate numerical tuning through a learned mapping:

$$
f_\phi: \boldsymbol{\theta} \mapsto [K_p, T_i, T_d],
$$

where $\boldsymbol{\theta}$ denotes the plant parameters.

## Methodology

1. Sample 100 plant configurations per dataset, with gain in $[0.5, 5.0]$ and plant time constants, including the zero time constant, in $[1.0, 10.0]$.
2. Optimize PID parameters using differential evolution and the Integral of Time-weighted Absolute Error:

   $$
   J = \int_0^{60} t\,|r(t)-y(t)|\,dt.
   $$

   The objective is evaluated numerically with a sampling interval of $0.1$ s and a reference value of $10$.
3. Train regression models using an 80:20 training–test split.
4. Evaluate predictions using Mean Absolute Error for each controller parameter.

| Plant family | Transfer function | Implemented regressors |
| --- | --- | --- |
| First order | $K/(Ts+1)$ | Random Forest, Extra Trees, Gradient Boosting, MLP |
| First order with zero | $K(T_zs+1)/(Ts+1)$ | Random Forest, Extra Trees, Gradient Boosting, MLP |
| Second order | $K/[(T_1s+1)(T_2s+1)]$ | Random Forest |
| Integrating first order | $K/[s(Ts+1)]$ | Random Forest, Extra Trees, Gradient Boosting, MLP |

The simulation library also includes additional plant models and computes IAE, ISE, ITAE, overshoot, settling time, and final tracking error.

## Execution

Run commands from the repository root. Docker with the Compose plugin is required.

```bash
# Build and run tests, followed by open- and closed-loop simulations
docker compose up --build

# Generate datasets and train models for a selected plant family
docker compose --profile first_order up --build
docker compose --profile first_order_zero up --build
docker compose --profile integrating_first_order up --build

# Run tests independently
docker compose run --rm tests
```

The second-order Compose training service references additional scripts that are not yet implemented. Run its available workflow explicitly:

```bash
docker compose run --rm generate_second_order_data
docker compose run --rm train_second_order \
  python src/ml_pid_tuning/ml/second_order/random_forest_regressor/train_second_order.py
```

Simulation plots are saved in `plots/`, simulation CSV files in `src/ml_pid_tuning/simulations/data/`, and training datasets in `src/ml_pid_tuning/data/datasets/`. Dataset generation overwrites the corresponding CSV and performs a separate optimization for each sampled plant.

### Local setup

The Docker image uses Python 3.14. For a local environment on Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest matplotlib scipy pandas scikit-learn
export PYTHONPATH="$PWD/src"
mkdir -p plots src/ml_pid_tuning/simulations/data src/ml_pid_tuning/data/datasets

python -m pytest -v
python -m ml_pid_tuning.simulations.close_loop
python -m ml_pid_tuning.ml.first_order.extra_trees_regressor.train_first_order
```

## Scope and limitations

Experiments use synthetic data and known plant parameters. Prediction MAE measures agreement with numerically optimized settings; it does not establish closed-loop stability or performance on physical systems. Training scripts print predictions without saving models or automatically validating predicted settings in closed-loop simulation.

Dataset sampling and optimization are stochastic, dependencies are not pinned, and evaluation uses a single training–test split. Comparisons against conventional tuning methods and repeated experimental trials remain necessary for a broader assessment.

## License

[MIT License](LICENSE).
