"""
Load and preprocess the warner.txt dataset
Run this first to prepare your data
"""

import pandas as pd
import re
from sklearn.model_selection import train_test_split
import os

def parse_warner_txt(filepath):
    """Parse your warner.txt into a DataFrame"""
    texts = []
    labels = []
    
    # Check if file exists in parent directory
    if not os.path.exists(filepath):
        # Try to find it in the repo root
        alt_path = '../' + filepath
        if os.path.exists(alt_path):
            filepath = alt_path
        else:
            raise FileNotFoundError(f"Could not find {filepath}. Make sure warner.txt is in your repo root.")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by the delimiter
    entries = content.split('#*#*#*#*#*#*#')
    
    for entry in entries:
        lines = entry.strip().split('\n')
        if not lines:
            continue
        
        # First line contains the label
        first_line = lines[0].strip()
        if first_line.startswith('LABEL:'):
            label = first_line.replace('LABEL:', '').strip()
            # Join the rest as the text
            text = ' '.join(lines[1:]).strip()
            
            if text:  # Only add if there's actual text
                texts.append(text)
                labels.append(1 if label == 'abusive' else 0)
    
    return pd.DataFrame({'text': texts, 'label': labels})

def clean_text(text):
    """Basic text cleaning for model input"""
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove @mentions
    text = re.sub(r'#', '', text)        # Remove # (keep the word though)
    text = re.sub(r'[^a-z\s]', '', text) # Keep only letters and spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    print("Loading warner.txt...")
    df = parse_warner_txt('warner.txt')  # Look for file in repo root
    print(f"✅ Loaded {len(df)} examples")
    print(f"Class distribution:\n  Not Abusive: { (df['label'] == 0).sum() }\n  Abusive: { (df['label'] == 1).sum() }")
    
    # Clean the text
    print("\nCleaning text...")
    df['clean_text'] = df['text'].apply(clean_text)
    
    # Split for training (80% train, 10% validation, 10% test)
    train_texts, temp_texts, train_labels, temp_labels = train_test_split(
        df['clean_text'], df['label'], test_size=0.2, random_state=42, stratify=df['label']
    )
    
    val_texts, test_texts, val_labels, test_labels = train_test_split(
        temp_texts, temp_labels, test_size=0.5, random_state=42, stratify=temp_labels
    )
    
    print(f"\nData split:")
    print(f"  Train: {len(train_texts)} examples")
    print(f"  Validation: {len(val_texts)} examples")
    print(f"  Test: {len(test_texts)} examples")
    
    # Save the splits for later use
    df.to_csv('processed_data.csv', index=False)
    print("\n✅ Saved processed data to 'processed_data.csv'")
