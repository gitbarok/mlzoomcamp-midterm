import pandas as pd
import pickle

from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier


def load(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


app = Flask("predict")


def predict_approval(data):
    model, dv = load("model/randomforest.bin")
    X = dv.transform(data)
    y_pred = model.predict_proba(X)[0, 1]
    THRESHOLD = 0.01
    approval = y_pred > THRESHOLD

    return y_pred, approval


@app.route("/")
def index():
    return "<h1> hello world </h1>"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    pred, approval = predict_approval(data)

    if approval:
        detail = "Prediction: Customer is elligible to get a credit card"
    else:
        detail = "Prediction: Customer is  not elligible to get a credit card"

    result = {
        "prediction_probability": float(pred),
        "detail": detail,
        "approval": bool(approval),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
