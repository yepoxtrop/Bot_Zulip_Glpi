import uvicorn;
from src.adapters.infraestructure.api.app import app;

if __name__ == "__main__":
    uvicorn.run(
        "DoomBot:app", host="127.0.0.1", port=8000, reload=True
    ); 