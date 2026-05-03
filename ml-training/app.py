# app.py
from flask import Flask, request, jsonify
import joblib  # or torch / tensorflow depending on your model

app = Flask(__name__)

# Load your trained model
model = joblib.load("hate_speech_model.pkl")

def predict(text):
    # adapt this to your preprocessing
    prediction = model.predict([text])[0]
    prob = model.predict_proba([text])[0].max()
    return prediction, prob

@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    text = data.get("text", "")

    pred, prob = predict(text)

    return jsonify({
        "hate": bool(pred),
        "confidence": float(prob)
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
