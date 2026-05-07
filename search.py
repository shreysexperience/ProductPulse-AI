from sentence_transformers import SentenceTransformer
import chromadb

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(path="./chromadb_data")

collection = client.get_collection("amazon_reviews")

query = input("Ask something: ")

print("Generating query embedding...")

query_embedding = model.encode(query).tolist()

print("Searching reviews...")

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

print("\nTop Matching Reviews:\n")

for i, doc in enumerate(results["documents"][0]):

    print(f"{i+1}. {doc}\n")