import re
import string
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ensure you’ve run: python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocessing(text: str) -> str:
    """Lowercase, remove numbers, stopwords, punctuation, then lemmatize."""
    # 1. lowercase
    text = text.lower()
    # 2. remove numbers
    text = re.sub(r"\d+", " ", text)
    # 3. tokenize & remove punctuation
    tokens = [
        token.text for token in nlp(text)
        if token.text not in string.punctuation
    ]
    # 4. remove stopwords
    tokens = [t for t in tokens if t not in stop_words]
    # 5. lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)
