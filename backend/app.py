from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)
CORS(app)

MODEL_PATH = Path("../models/random_forest_model.joblib")
model = joblib.load(MODEL_PATH)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    try:
        chromosome = data["chromosome"]
        ref = data["ref"]
        alt = data["alt"]
        position = float(data["position"])
    except KeyError:
        return jsonify({"error": "Invalid input format"}), 400

    # Feature engineering (MUST MATCH TRAINING)
    ref_len = len(ref)
    alt_len = len(alt)
    len_diff = alt_len - ref_len

    position_norm = position / 3e8  # approx human genome max

    df = pd.DataFrame([{
        "Chromosome": chromosome,
        "ref_len": ref_len,
        "alt_len": alt_len,
        "len_diff": len_diff,
        "position_norm": position_norm
    }])

    prob = model.predict_proba(df)[0][1]

    prediction = "Likely Pathogenic" if prob >= 0.5 else "Benign"

    return jsonify({
        "risk_probability": round(float(prob), 4),
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

