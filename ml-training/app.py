# app.py

import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/classify": {
        "origins": ["https://x.com", "https://twitter.com"]
    }
})

# (Optional) keep the load if you want, but we'll not use it yet
# model = joblib.load("hate_speech_model.pkl")

def predict(text: str):
    # TEMPORARY STUB:
    # Always say "not hate" with 0.5 confidence
    # so your extension can function end‑to‑end.
    return 0, 0.5

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json(force=True) or {}
    text = data.get("text", "")

    pred, prob = predict(text)

    return jsonify({
        "hate": bool(pred),
        "confidence": float(prob)
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)