import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

def main():
    data = pd.read_csv("src/ml_pid_tuning/data/datasets/integrating_first_order_dataset.csv")

    X = data[["gain", "time_constant"]]
    y = data[["kp", "ti", "td"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    x_scaler = StandardScaler()
    y_scaler = StandardScaler()

    X_train_scaled = x_scaler.fit_transform(X_train)
    X_test_scaled = x_scaler.transform(X_test)

    y_train_scaled = y_scaler.fit_transform(y_train)

    model = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=2000, random_state=42)

    model.fit(X_train_scaled, y_train_scaled)

    predictions_scaled = model.predict(X_test_scaled)

    predictions = y_scaler.inverse_transform(predictions_scaled)

    kp_mae = mean_absolute_error(y_test["kp"], predictions[:, 0])
    ti_mae = mean_absolute_error(y_test["ti"], predictions[:, 1])
    td_mae = mean_absolute_error(y_test["td"], predictions[:, 2])

    print("Model performance")
    print("Kp MAE:", round(kp_mae, 4))
    print("Ti MAE:", round(ti_mae, 4))
    print("Td MAE:", round(td_mae, 4))

    print()
    print("Predictions")

    for i in range(len(predictions)):
        gain = X_test.iloc[i]["gain"]
        time_constant = X_test.iloc[i]["time_constant"]

        predicted_kp = predictions[i][0]
        predicted_ti = predictions[i][1]
        predicted_td = predictions[i][2]

        print()
        print("Object parameters")
        print("Gain:", round(gain, 4))
        print("Time constant:", round(time_constant, 4))

        print("Predicted PID parameters")
        print("Kp:", round(predicted_kp, 4))
        print("Ti:", round(predicted_ti, 4))
        print("Td:", round(predicted_td, 4))

if __name__ == "__main__":
    main()