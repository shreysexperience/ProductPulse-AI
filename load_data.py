from datasets import load_dataset
import pandas as pd

print("Loading dataset...")

dataset = load_dataset(
    "amazon_polarity",
    split="train",
    streaming=True
)

reviews = []

print("Collecting reviews...")

for i, item in enumerate(dataset):

    reviews.append({
        "label": item["label"],
        "title": item["title"],
        "text": item["content"]
    })

    if i >= 10000:
        break

df = pd.DataFrame(reviews)

print(df.head())

df.to_csv("amazon_reviews.csv", index=False)

print("Dataset saved successfully!")