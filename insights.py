@app.get("/insights")
def generate_insights(query: str):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    reviews = results["documents"][0]

    combined_reviews = " ".join(reviews)

    summary = summarizer(
        combined_reviews[:500],
        max_length=100,
        num_return_sequences=1
    )

    return {
        "query": query,
        "reviews": reviews,
        "insights": summary[0]["generated_text"]
    }