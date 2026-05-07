# ProductPulse AI 🚀

AI-powered customer review intelligence dashboard that analyzes product feedback and extracts actionable insights using semantic search and embeddings.

---

## Live Demo

Frontend: https://your-vercel-url.vercel.app

Backend API: https://productpulse-ai-production.up.railway.app/docs

---

## Features

- 🔍 Semantic search over customer reviews
- 🤖 AI-generated insight extraction
- ⚡ FastAPI backend with vector-based retrieval
- 🎨 Modern Next.js frontend UI
- ☁️ Fully deployed full-stack application
- 📊 Real-time review intelligence exploration

---

## Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- Python
- Uvicorn

### AI / Data
- Sentence Transformers
- ChromaDB
- Pandas
- NumPy

### Deployment
- Vercel (Frontend)
- Railway (Backend)
- GitHub

---

## Project Structure

```bash
ProductPulse-AI/
│
├── productpulse-frontend/
│   ├── src/app/
│   ├── package.json
│   └── next.config.ts
│
├── api.py
├── insights.py
├── embeddings.py
├── search.py
├── preprocess.py
├── load_data.py
├── requirements.txt
└── amazon_reviews.csv
```

---

## How It Works

1. Customer reviews are cleaned and preprocessed.
2. Semantic embeddings are generated using Sentence Transformers.
3. Embeddings are stored in ChromaDB.
4. User queries are semantically matched against reviews.
5. AI-generated insights are returned through FastAPI APIs.
6. Frontend displays insights interactively in real time.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shreysexperience/ProductPulse-AI.git
cd ProductPulse-AI
```

---

### Backend Setup

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

---

### Frontend Setup

```bash
cd productpulse-frontend
npm install
npm run dev
```

---

## API Endpoint

```bash
GET /insights?query=battery
```

---

## Deployment

- Frontend deployed using Vercel
- Backend deployed using Railway

---

## Future Improvements

- Sentiment analysis dashboard
- Interactive charts
- Authentication system
- AI summary cards
- Search analytics
- Exportable reports
- Voice-enabled search
