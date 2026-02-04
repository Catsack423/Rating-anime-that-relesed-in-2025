from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List, Optional
import uvicorn


app = FastAPI(title="Anime List API")

client = MongoClient("mongodb://localhost:27017/")
db = client["Dataen"]
collection = db["AnimeList"]

@app.get("/")
def read_root():
    return {"message": "Welcome to Anime List API"}

@app.get("/anime", response_model=List[dict])
def get_all_anime():
    animes = list(collection.find({}, {"_id": 0}))
    return animes

@app.get("/anime/search")
def search_anime(title: str):
    query = {"title": {"$regex": title, "$options": "i"}}
    results = list(collection.find(query, {"_id": 0}))
    if not results:
        raise HTTPException(status_code=404, detail="Anime not found")
    return results

# API สำหรับดึงข้อมูลตาม Season
@app.get("/anime/season/{season_name}")
def get_by_season(season_name: str):
    results = list(collection.find({"season": season_name}, {"_id": 0}))
    return results

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=9919)