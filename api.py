from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import chromadb

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading text model...")
generator = pipeline(
    "text-generation",
    model="gpt2"
)

print("Connecting to ChromaDB...")
client = chromadb.PersistentClient(path="./chromadb_data")

collection = client.get_collection("amazon_reviews")


@app.get("/insights")
def generate_insights(query: str):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    reviews = results["documents"][0]

    combined_reviews = " ".join(reviews)

    prompt = f"""
Customer issue: {query}

Reviews:
{combined_reviews}

Summarize the customer complaints:
"""

    output = generator(
        prompt,
        max_length=120,
        num_return_sequences=1
    )

    return {
        "query": query,
        "reviews": reviews,
        "insights": output[0]["generated_text"]
    }