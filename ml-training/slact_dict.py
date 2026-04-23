# Common abusive slang and their expansions
SLANG_MAP = {
    # Self-harm threats (extremely serious)
    'kys': 'kill yourself',
    'kms': 'kill myself',
    'selfharm': 'self harm',
    
    # Leetspeak variations
    'h8': 'hate',
    'h8te': 'hate',
    'h8ter': 'hater',
    'fck': 'fuck',
    'fvck': 'fuck',
    'sh1t': 'shit',
    'b1tch': 'bitch',
    'n1gga': 'nigger',
    
    # Common abbreviations
    'stfu': 'shut the fuck up',
    'gtfo': 'get the fuck out',
    'foh': 'fuck outta here',
    
    # Subtle threats
    'go die': 'kill yourself',
    'drop dead': 'kill yourself',
    'roast yourself': 'kill yourself',
}

def expand_slang(text):
    """Replace slang with full phrases"""
    text = text.lower()
    for slang, expansion in SLANG_MAP.items():
        text = text.replace(slang, expansion)
    return text