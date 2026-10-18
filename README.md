# Machine Learning-Based PID Controller Tuning

## Abstract

This repository investigates supervised regression as an approach to PID controller tuning for parameterized dynamic systems. Synthetic training data are constructed by numerically optimizing controller parameters for sampled plant configurations. The resulting plant–controller pairs are used to learn a mapping from plant parameters to proportional gain, integral time, and derivative time. The implementation combines discrete-time plant simulation, differential evolution, and regression models, with separate facilities for evaluating prediction error and closed-loop response characteristics.

The research objective is to examine whether a learned parameter mapping can approximate the settings obtained through repeated numerical optimization. The repository provides an experimental implementation; a comparative benchmark establishing control performance or computational speedup has not yet been reported here.

## Problem formulation

Let $\boldsymbol{\theta}$ denote the parameters of a plant and $\mathbf{q} = [K_p, T_i, T_d]^\mathsf{T}$ the controller parameters. For each plant configuration, numerical optimization produces a reference parameter vector $\mathbf{q}^{\star}(\boldsymbol{\theta})$. A regression model $f_\phi$ is then fitted to approximate the mapping

$$
f_\phi: \boldsymbol{\theta} \mapsto \widehat{\mathbf{q}}.
$$

Plant parameters are supplied directly to the regressors. Estimation of these parameters from measured input–output data is outside the current workflow.

### Plant families

Dataset generation is implemented for three families, represented by the following continuous-time transfer functions:

| Plant family | Transfer function | Regression inputs |
| --- | --- | --- |
| First order | $G(s) = K/(Ts + 1)$ | $K, T$ |
| Second order | $G(s) = K/[(T_1s + 1)(T_2s + 1)]$ | $K, T_1, T_2$ |
| Integrating first order | $G(s) = K/[s(Ts + 1)]$ | $K, T$ |

Simulation uses discrete recurrence equations implemented in the plant classes. The broader simulation library contains 13 plant models, including transport-delay, differentiating, oscillatory, and unstable systems; these additional models are not currently included in the dataset-generation workflow.

### Controller parameterization

The controller uses the ideal PID parameterization. For tracking error $e_k = r_k - y_k$ and sampling interval $h$, its implementation is

$$
I_k = I_{k-1} + h e_k,
\qquad
u_k = K_p \left(e_k + \frac{I_k}{T_i} + T_d \frac{e_k - e_{k-1}}{h}\right).
$$

The integral accumulator and previous error are initialized to zero. Setting `ti=0` disables the integral contribution, and setting `td=0` disables the derivative contribution. The controller does not implement actuator saturation, anti-windup, or derivative filtering.

## Experimental methodology

```mermaid
flowchart LR
    A[Sample plant parameters] --> B[Optimize PID by closed-loop simulation]
    B --> C[Construct labeled dataset]
    C --> D[Partition training and test data]
    D --> E[Fit regression models]
    E --> F[Evaluate parameter prediction error]
```

### Reference parameter generation

For each sampled plant, SciPy's differential evolution algorithm searches for controller parameters that minimize the Integral of Time-weighted Absolute Error (ITAE). The implemented objective approximates the finite-horizon integral using

$$
J(\mathbf{q}; \boldsymbol{\theta})
= \sum_{k=1}^{N} t_k \lvert r_k - y_k \rvert (t_k - t_{k-1}).
$$

A fresh plant and controller are instantiated for each objective evaluation. Non-finite objective values and evaluations raising `ValueError` or `OverflowError` receive a penalty of $10^9$. The optimization output is a numerical reference within the specified bounds; global optimality is not established.

Each generator samples 100 plant configurations with gain drawn uniformly from $[0.5, 5.0]$ and each time constant drawn uniformly from $[1.0, 10.0]$. CSV records contain the plant parameters, optimized `kp`, `ti`, and `td`, and the corresponding objective value.

### Regression models and evaluation

Random Forest, Extra Trees, Gradient Boosting, and multilayer perceptron (MLP) regressors are implemented for first-order and integrating first-order plants. A Random Forest regressor is also implemented for second-order plants.

Training scripts use an 80:20 training–test split with `random_state=42`. The MLP workflow standardizes both input features and target parameters using scalers fitted on the training partition, and transforms predictions back to the original parameter units.

Prediction accuracy is reported separately for each controller parameter using Mean Absolute Error (MAE):

$$
\operatorname{MAE}_j = \frac{1}{n_{\mathrm{test}}}
\sum_{i=1}^{n_{\mathrm{test}}}
\left|q_{ij}^{\star} - \widehat{q}_{ij}\right|.
$$

Closed-loop simulation additionally provides IAE, ISE, ITAE, percentage overshoot, settling time with a default 2% tolerance band, and absolute final-sample tracking error. The latter is reported by the implementation as steady-state error and depends on the simulation horizon.

Training scripts print evaluation results and example predictions. They do not persist trained models or automatically evaluate predicted settings in closed-loop simulation.

## Execution with Docker

Install Docker with the Compose plugin, then run these commands from the repository root:

```bash
docker compose build
docker compose up
```

The default workflow runs **tests → open-loop simulation → closed-loop simulation**. Dataset generation and training are enabled separately through Compose profiles.

Generated files are available on the host:

| Output | Location |
| --- | --- |
| Open-loop response plot | `plots/step_response.png` |
| Closed-loop response plot | `plots/closed_loop_response.png` |
| Control signal plot | `plots/control_signal.png` |
| Simulation data | `src/ml_pid_tuning/simulations/data/` |
| Generated datasets | `src/ml_pid_tuning/data/datasets/` |

Run only the test suite:

```bash
docker compose run --rm tests
```

### Dataset generation and model training

The following profiles execute the workflow for the selected plant family:

```bash
# First-order plants: generate data, then train four regressors
docker compose --profile first_order up --build

# Integrating first-order plants: generate data, then train four regressors
docker compose --profile integrating_first_order up --build
```

Each profile also runs the tests and simulations through its service dependencies. Dataset generation performs a separate optimization for each of 100 sampled plants and may take considerably longer than the simulations. Re-running a generator overwrites its dataset CSV.

**Second-order workflow:** the `second_order` Compose profile currently references Extra Trees, Gradient Boosting, and MLP scripts that are not present. Run the available generator and Random Forest trainer directly:

```bash
docker compose run --rm generate_second_order_data
docker compose run --rm train_second_order \
  python src/ml_pid_tuning/ml/second_order/random_forest_regressor/train_second_order.py
```

## Local environment

The Docker image uses **Python 3.14**. To set up a local virtual environment on Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest matplotlib scipy pandas scikit-learn
export PYTHONPATH="$PWD/src"
mkdir -p plots src/ml_pid_tuning/simulations/data src/ml_pid_tuning/data/datasets
```

Run all commands from the repository root because scripts use relative paths for inputs and outputs.

```bash
# Validate controllers, plant models, and performance metrics
python -m pytest -v

# Generate simulation CSV files and plots
python -m ml_pid_tuning.simulations.open_loop
python -m ml_pid_tuning.simulations.close_loop

# Train Extra Trees using the existing first-order dataset
python -m ml_pid_tuning.ml.first_order.extra_trees_regressor.train_first_order

# Optionally regenerate that dataset before training
python -m ml_pid_tuning.data.generate_first_order_dataset
```

## Programmatic simulation and optimization

```python
from ml_pid_tuning.controllers.pid import PIDController
from ml_pid_tuning.plants.first_order import FirstOrderPlant
from ml_pid_tuning.simulations.close_loop import run_simulation

plant = FirstOrderPlant(gain=2.5, time_constant=4.0)
controller = PIDController(kp=9.8596, ti=4.0232, td=0.0)

results = run_simulation(
    plant=plant,
    controller=controller,
    setpoint=10.0,
    simulation_time=60.0,
    dt=0.1,
)

print(f"ITAE: {results['itae']:.4f}")
print(f"Overshoot: {results['overshoot']:.2f}%")
```

`run_simulation()` returns time series and performance metrics. The executable `close_loop` script adds CSV export and plotting.

To optimize settings instead, pass a factory that creates a fresh plant for each trial:

```python
from ml_pid_tuning.optimization.differential_evolution import optimize_pid
from ml_pid_tuning.plants.first_order import FirstOrderPlant

settings = optimize_pid(
    lambda: FirstOrderPlant(gain=2.5, time_constant=4.0)
)
print(settings)  # kp, ti, td, objective
```

## Illustrative simulation outputs

The checked-in plots illustrate simulation outputs. The default open-loop script uses a second-order plant, while the default closed-loop script uses a first-order plant.

| Open-loop response | Closed-loop PID response |
| --- | --- |
| ![Open-loop step response](plots/step_response.png) | ![Closed-loop PID response](plots/closed_loop_response.png) |

## Experimental configuration

Settings are currently edited in the Python scripts rather than supplied through command-line arguments.

| Setting | Current value or location |
| --- | --- |
| Samples per generated dataset | `100` in each dataset generator |
| Sampled plant gain | `0.5–5.0` |
| Sampled time constants | `1.0–10.0` |
| Optimization bounds | `Kp: 0.01–10`, `Ti: 0.1–50`, `Td: 0–10` |
| Optimization simulation | Setpoint `10`, duration `60 s`, time step `0.1 s` |
| Example plant for first-order predictions | `ml/first_order/examined_object.py` |
| Example plant for integrating first-order predictions | `ml/integrating_first_order/examined_object.py` |

Dataset sampling and differential evolution are stochastic, so regenerated labels and subsequent training results can vary. Prediction MAE measures agreement with optimized parameter labels; use closed-loop simulation to assess the control performance of predicted settings.

## Limitations and reproducibility

The experiments use synthetic data generated by the same simulation models used during optimization. Generalization to measurement noise, unmodeled dynamics, external disturbances, and physical plants has not been established. Parameter prediction MAE measures agreement with numerical reference settings; it does not directly establish closed-loop stability or tracking performance.

The current evaluation uses a single training–test split. Cross-validation, repeated-seed analysis, comparisons against conventional tuning rules, and systematic closed-loop evaluation of predicted settings would be needed for a broader comparative study. The optimization objective contains no explicit penalty on control effort or actuator constraints.

Dataset sampling and differential evolution do not currently use fixed random seeds. Dependencies are installed without pinned versions. Consequently, the fixed split and estimator seeds do not make the complete data-generation and training workflow reproducible across runs and environments. Regenerating a dataset overwrites the corresponding CSV file.

## Repository structure

```text
src/ml_pid_tuning/
├── controllers/       # PID implementation
├── plants/            # Dynamic plant models
├── simulations/       # Open- and closed-loop experiments and CSV outputs
├── metrics/           # Control performance metrics
├── optimization/      # Differential evolution PID tuning
├── data/              # Dataset generators and CSV datasets
└── ml/                # Training scripts grouped by plant family and regressor
tests/                 # Controller, plant, and metric tests
plots/                 # Generated response and control signal figures
Dockerfile             # Python runtime and dependencies
compose.yaml           # Test, simulation, and training workflows
```

## License

Released under the [MIT License](LICENSE).
