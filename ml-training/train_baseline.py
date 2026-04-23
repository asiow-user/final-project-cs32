"""
Train a fast baseline model using Logistic Regression + TF-IDF
This model is lightweight and can run in ~2 minutes
"""

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import numpy as np

def main():
    print("Loading preprocessed data...")
    df = pd.read_csv('processed_data.csv')
    
    # Split back into train/val/test (in a real project, save these separately)
    from sklearn.model_selection import train_test_split
    
    train_texts, temp_texts, train_labels, temp_labels = train_test_split(
        df['clean_text'], df['label'], test_size=0.2, random_state=42, stratify=df['label']
    )
    val_texts, test_texts, val_labels, test_labels = train_test_split(
        temp_texts, temp_labels, test_size=0.5, random_state=42, stratify=temp_labels
    )
    
    print(f"Training on {len(train_texts)} examples...")
    
    # Convert text to numerical features
    vectorizer = TfidfVectorizer(
        max_features=10000,  # Limit to top 10k words
        ngram_range=(1, 2),   # Use single words and word pairs
        min_df=2,             # Ignore words that appear less than twice
        max_df=0.95           # Ignore words that appear in >95% of docs
    )
    
    X_train = vectorizer.fit_transform(train_texts)
    X_val = vectorizer.transform(val_texts)
    
    print(f"Feature matrix shape: {X_train.shape}")
    
    # Train logistic regression model
    model = LogisticRegression(
        C=1.0,                # Regularization strength
        max_iter=1000,        # Enough iterations to converge
        random_state=42,
        class_weight='balanced'  # Handle class imbalance
    )
    
    print("Training model...")
    model.fit(X_train, train_labels)
    
    # Evaluate on validation set
    val_preds = model.predict(X_val)
    val_proba = model.predict_proba(X_val)
    
    print("\n" + "="*50)
    print("VALIDATION RESULTS")
    print("="*50)
    print(classification_report(val_labels, val_preds, target_names=['Not Abusive', 'Abusive']))
    print(f"Accuracy: {accuracy_score(val_labels, val_preds):.4f}")
    
    # Confusion matrix
    cm = confusion_matrix(val_labels, val_preds)
    print(f"\nConfusion Matrix:")
    print(f"  True Negatives: {cm[0,0]}  False Positives: {cm[0,1]}")
    print(f"  False Negatives: {cm[1,0]}  True Positives: {cm[1,1]}")
    
    # Save the model
    print("\n💾 Saving model...")
    joblib.dump(model, 'hate_speech_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    
    print("✅ Model saved as 'hate_speech_model.pkl'")
    print("✅ Vectorizer saved as 'vectorizer.pkl'")
    
    return model, vectorizer

if __name__ == "__main__":
    main()
