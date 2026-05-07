from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import chromadb
from sentence_transformers import SentenceTransformer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Connecting to ChromaDB...")
client = chromadb.PersistentClient(path="./chromadb_data")
collection = client.get_collection("amazon_reviews")


@app.get("/insights")
def get_insights(query: str):

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    reviews = results["documents"][0]

    insights = f"""
Customer issue: {query}

Reviews:
{" ".join(reviews)}

Summary:
Customers are repeatedly mentioning problems related to {query}.
"""

    return {
        "query": query,
        "reviews": reviews,
        "insights": insights
    }