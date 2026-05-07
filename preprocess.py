import pandas as pd
import spacy
import re

print("Loading spaCy model...")
nlp = spacy.load("en_core_web_sm")

print("Loading dataset...")
df = pd.read_csv("amazon_reviews.csv")

print("Cleaning text...")

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(tokens)

df["cleaned_text"] = df["text"].apply(clean_text)

print(df[["text", "cleaned_text"]].head())

df.to_csv("cleaned_reviews.csv", index=False)

print("Cleaned dataset saved successfully!")