"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const searchInsights = async () => {
    if (!query) return;

    setLoading(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/insights?query=${query}`
      );

      const result = await response.json();

      setData(result);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-black via-zinc-950 to-blue-950 text-white p-10">
      <div className="max-w-5xl mx-auto">
        
        {/* Header */}
        <div className="mb-10">
          <h1 className="text-6xl font-bold mb-4">
            ProductPulse AI
          </h1>

          <p className="text-zinc-400 text-lg">
            AI-powered customer review intelligence dashboard
          </p>
        </div>

        {/* Search */}
        <div className="flex gap-4 mb-10">
          <input
            type="text"
            placeholder="Search customer problems..."
            className="flex-1 p-5 rounded-2xl bg-zinc-900 border border-zinc-700 outline-none"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            onClick={searchInsights}
            className="bg-white text-black px-8 rounded-2xl font-semibold hover:scale-105 transition-all duration-300"
          >
            Search
          </button>
        </div>

        {/* Loading */}
        {loading && (
          <div className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800">
            <p className="text-zinc-400">
              Analyzing customer reviews...
            </p>
          </div>
        )}

        {/* Results */}
        {data && (
          <div className="space-y-8">

            {/* Stats */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              
              <div className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800">
                <p className="text-zinc-400 text-sm mb-2">
                  Reviews Found
                </p>

                <h2 className="text-4xl font-bold">
                  {data.reviews.length}
                </h2>
              </div>

              <div className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800">
                <p className="text-zinc-400 text-sm mb-2">
                  Search Query
                </p>

                <h2 className="text-2xl font-bold">
                  {data.query}
                </h2>
              </div>

              <div className="bg-zinc-900 p-6 rounded-2xl border border-zinc-800">
                <p className="text-zinc-400 text-sm mb-2">
                  AI Status
                </p>

                <h2 className="text-2xl font-bold text-green-400">
                  Active
                </h2>
              </div>
            </div>

            {/* AI Insights */}
            <div className="bg-zinc-900 p-8 rounded-2xl border border-zinc-800">
              <h2 className="text-3xl font-bold mb-5">
                AI Insights
              </h2>

              <p className="text-zinc-300 whitespace-pre-wrap leading-8">
                {data.insights}
              </p>
            </div>

            {/* Reviews */}
            <div className="bg-zinc-900 p-8 rounded-2xl border border-zinc-800">
              <h2 className="text-3xl font-bold mb-6">
                Top Matching Reviews
              </h2>

              <div className="space-y-4">
                {data.reviews.map(
                  (review: string, index: number) => (
                    <div
                      key={index}
                      className="bg-black border border-zinc-800 p-5 rounded-2xl text-zinc-300"
                    >
                      {review}
                    </div>
                  )
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}