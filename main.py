from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/markets")
async def get_markets():
    url = "https://gamma-api.polymarket.com/markets?closed=false&limit=20&order=volume24hr&ascending=false"
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url)
        return resp.json()

@app.get("/health")
async def health():
    return {"status": "ok"}
