"""Data augmentation - create more training examples for common patterns"""

import random
import csv

def create_augmented_examples():
    """Generate synthetic training examples for common abusive patterns"""
    
    patterns = [
        # Pattern, Label (1=abusive)
        ("kys", 1),
        ("kill yourself", 1),
        ("go kill yourself", 1),
        ("h8 u", 1),
        ("i h8te you", 1),
        ("i hate you", 1),
        ("go die", 1),
        ("please die", 1),
        ("you should die", 1),
        ("stfu", 1),
        ("stfu and die", 1),
        ("gtfo", 1),
        ("kms", 1),
        ("just kys", 1),
        ("you're worthless die", 1),
    ]
    
    # Add positive examples (safe phrases)
    safe_patterns = [
        ("i disagree with you", 0),
        ("that's an interesting perspective", 0),
        ("thanks for sharing", 0),
        ("i see your point", 0),
        ("let's agree to disagree", 0),
    ]
    
    all_examples = patterns + safe_patterns
    
    # Append to existing training data
    with open('train.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for text, label in all_examples:
            writer.writerow([text, label])
    
    print(f"✅ Added {len(all_examples)} augmented examples to train.csv")
    print("   Re-run training to see improvements")

if __name__ == "__main__":
    create_augmented_examples()