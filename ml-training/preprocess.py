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
    """Enhanced cleaning that handles leetspeak and slang"""
    text = text.lower()
    
    # Replace leetspeak characters
    leet_map = {
        '0': 'o', '1': 'i', '2': 'to', '3': 'e', '4': 'a',
        '5': 's', '6': 'b', '7': 't', '8': 'ate', '9': 'g',
        '@': 'a', '$': 's', '!': 'i', '+': 'and'
    }
    
    for leet, replacement in leet_map.items():
        text = text.replace(leet, replacement)
    
    # Expand common abusive acronyms
    acronyms = {
        r'\bkys\b': 'kill yourself',
        r'\bkms\b': 'kill myself',
        r'\bstfu\b': 'shut the fuck up',
        r'\bgtfo\b': 'get the fuck out',
        r'\bfoh\b': 'fuck out of here',
        r'\bh8\b': 'hate',
        r'\bh8te\b': 'hate',
    }
    
    for acronym, expansion in acronyms.items():
        text = re.sub(acronym, expansion, text)
    
    # Handle "go die" patterns
    text = re.sub(r'go\s+die', 'kill yourself', text)
    
    # Remove URLs and mentions
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    
    # Keep only letters and spaces (but now we've normalized first)
    text = re.sub(r'[^a-z\s]', '', text)
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
