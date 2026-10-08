import uvicorn;
from fastapi import FastAPI;

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#uvicorn.exe DoomBot:app --reload