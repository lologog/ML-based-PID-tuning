import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_absolute_error
from ml_pid_tuning.ml.integrating_first_order.test_object import gain as test_gain
from ml_pid_tuning.ml.integrating_first_order.test_object import time_constant as test_time_constant

def main():
    data = pd.read_csv("src/ml_pid_tuning/data/datasets/integrating_first_order_dataset.csv")

    X = data[["gain", "time_constant"]]
    y = data[["kp", "ti", "td"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    base_model = GradientBoostingRegressor(n_estimators=200, random_state=42)

    model = MultiOutputRegressor(base_model)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    kp_mae = mean_absolute_error(y_test["kp"], predictions[:, 0])
    ti_mae = mean_absolute_error(y_test["ti"], predictions[:, 1])
    td_mae = mean_absolute_error(y_test["td"], predictions[:, 2])

    print("Model performance")
    print("Kp MAE:", round(kp_mae, 4))
    print("Ti MAE:", round(ti_mae, 4))
    print("Td MAE:", round(td_mae, 4))

    # print()
    # print("Predictions")

    # for i in range(len(predictions)):
    #     gain = X_test.iloc[i]["gain"]
    #     time_constant = X_test.iloc[i]["time_constant"]

    #     predicted_kp = predictions[i][0]
    #     predicted_ti = predictions[i][1]
    #     predicted_td = predictions[i][2]

    #     print()
    #     print("Object parameters")
    #     print("Gain:", round(gain, 4))
    #     print("Time constant:", round(time_constant, 4))

    #     print("Predicted PID parameters")
    #     print("Kp:", round(predicted_kp, 4))
    #     print("Ti:", round(predicted_ti, 4))
    #     print("Td:", round(predicted_td, 4))

    print()
    print("Test object")

    test_input = pd.DataFrame([[test_gain, test_time_constant]], columns=["gain", "time_constant"])

    test_prediction = model.predict(test_input)

    predicted_kp = test_prediction[0][0]
    predicted_ti = test_prediction[0][1]
    predicted_td = test_prediction[0][2]

    print("Object parameters")
    print("Gain:", test_gain)
    print("Time constant:", test_time_constant)

    print("Predicted PID parameters")
    print("Kp:", round(predicted_kp, 4))
    print("Ti:", round(predicted_ti, 4))
    print("Td:", round(predicted_td, 4))

if __name__ == "__main__":
    main()