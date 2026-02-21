# main.py - FastAPI app
from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

# Your "hello message" storage (using SQLite for simplicity)
messages = []

@app.get("/")
def read_root():
    return {"message": "Hello World", "timestamp": datetime.now()}

@app.get("/health")
def health_check():
    return {"status": "alive", "timestamp": datetime.now()}

@app.post("/messages")
def create_message(content: str):
    messages.append({"content": content, "timestamp": datetime.now()})
    return {"status": "saved"}

@app.get("/messages")
def get_messages():
    return messages

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)