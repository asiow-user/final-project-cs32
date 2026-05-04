# app.py

import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocess import clean_text  # use your existing cleaner

app = Flask(__name__)

# Allow ANY origin to call /classify (you can tighten later)
CORS(app)
@app.route("/")
def index():
    return "Backend is running"
# Load trained model and vectorizer once at startup
# Make sure these .pkl files are in the same folder as app.py
model = joblib.load("hate_speech_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def predict(text: str):
    """
    Run your real model:
    - clean text with clean_text()
    - vectorize with vectorizer
    - predict class + confidence with model
    """

    # 1) preprocess
    cleaned = clean_text(text)

    # 2) vectorize
    X = vectorizer.transform([cleaned])

    # 3) get prediction + confidence
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[0]  # [p_not_hate, p_hate]
        prob_hate = float(probs[1])
        pred = int(prob_hate >= 0.5)       # 1 if hate, else 0
        confidence = float(max(probs))     # max of the two probs
    else:
        # fallback if model has no predict_proba
        pred = int(model.predict(X)[0])
        prob_hate = 1.0 if pred == 1 else 0.0
        confidence = 1.0

    return pred, confidence


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json(force=True) or {}
    text = data.get("text", "")

    pred, prob = predict(text)

    return jsonify({
        "hate": bool(pred),        # True if abusive/hate
        "confidence": float(prob)  # model confidence 0–1
    })


if __name__ == "__main__":
    # Running on port 5001 as before
    app.run(host="0.0.0.0", port=5001, debug=True)