import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

print("Loading dataset...")
df = pd.read_csv("cleaned_reviews.csv")

texts = df["cleaned_text"].fillna("").tolist()

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

print("Initializing ChromaDB...")

client = chromadb.PersistentClient(path="./chromadb_data")

collection = client.get_or_create_collection(
    name="amazon_reviews"
)

print("Storing embeddings...")

for i, (text, embedding) in enumerate(zip(texts, embeddings)):

    collection.add(
        documents=[text],
        embeddings=[embedding.tolist()],
        ids=[str(i)]
    )

print("Embeddings stored successfully!")