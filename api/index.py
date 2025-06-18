# api/index.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)  # Required for Vercel

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.post("/api/")
async def process_query(payload: dict):
    question = payload.get("question")
    image = payload.get("image")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")
    
    return {
        "answer": "Placeholder answer",
        "links": [
            {"url": "https://example.com", "text": "Example Source"}
        ]
    }
