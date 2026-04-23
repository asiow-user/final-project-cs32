"""
Test your trained model on new examples
"""

import joblib
import sys
import os

# Add parent directory to path so we can import preprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocess import clean_text

def load_model():
    """Load the trained model and vectorizer"""
    model = joblib.load('hate_speech_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer

def predict(text, model, vectorizer):
    """Predict if a text is abusive or not"""
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    proba = model.predict_proba(vectorized)[0]
    prediction = 1 if proba[1] > 0.5 else 0
    return prediction, proba[1]  # Returns (is_abusive, confidence)

def main():
    print("Loading model...")
    model, vectorizer = load_model()
    
    # Test on the provided dataset examples
    test_examples = [
        "I completely agree with your point, well said!",
        "You're an idiot and everyone hates you.",
        "This is a thoughtful discussion about politics.",
        "Go back to your own country you worthless piece of trash.",
        "I disagree with your opinion but respect your right to say it.",
        "KILL ALL NIGGERS",  # From your dataset
        "Thanks for sharing this article, very informative!"
    ]
    
    print("\n" + "="*60)
    print("TESTING MODEL ON EXAMPLES")
    print("="*60)
    
    for example in test_examples:
        is_abusive, confidence = predict(example, model, vectorizer)
        status = "🔴 ABUSIVE" if is_abusive else "🟢 SAFE"
        print(f"\nText: \"{example[:60]}{'...' if len(example) > 60 else ''}\"")
        print(f"Result: {status} (confidence: {confidence:.3f})")
    
    # Interactive mode
    print("\n" + "="*60)
    print("INTERACTIVE MODE - Type your own text to test")
    print("Type 'quit' to exit")
    print("="*60)
    
    while True:
        user_input = input("\nEnter text to analyze: ")
        if user_input.lower() == 'quit':
            break
        if user_input.strip():
            is_abusive, confidence = predict(user_input, model, vectorizer)
            status = "🔴 ABUSIVE (would be censored)" if is_abusive else "🟢 SAFE (would be shown)"
            print(f"Result: {status}")
            print(f"Confidence: {confidence:.3f}")

if __name__ == "__main__":
    main()
