import re
from preprocessing.stopwords import STOPWORDS

def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"\b[a-z0-9]+\b", text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    return tokens
