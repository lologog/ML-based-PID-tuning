import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def main():
    data = pd.read_csv("src/ml_pid_tuning/data/datasets/second_order_dataset.csv")

    X = data[["gain", "time_constant_1", "time_constant_2"]]
    y = data[["kp", "ti", "td"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, random_state=42)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

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
        time_constant_1 = X_test.iloc[i]["time_constant_1"]
        time_constant_2 = X_test.iloc[i]["time_constant_2"]

        predicted_kp = predictions[i][0]
        predicted_ti = predictions[i][1]
        predicted_td = predictions[i][2]

        print()
        print("Object parameters")
        print("Gain:", round(gain, 4))
        print("Time constant 1:", round(time_constant_1, 4))
        print("Time constant 2:", round(time_constant_2, 4))

        print("Predicted PID parameters")
        print("Kp:", round(predicted_kp, 4))
        print("Ti:", round(predicted_ti, 4))
        print("Td:", round(predicted_td, 4))

if __name__ == "__main__":
    main()