import json, os, socket
from fastapi import FastAPI
import httpx


HOST = os.getenv("BACKEND_URL", "http://localhost:8000")

app = FastAPI()

@app.get("/")
async def root():
    message = httpx.get(HOST)
    decoded = json.loads(message.text)
    decoded["iam"] = socket.gethostname()
    return decoded

