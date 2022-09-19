import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello from {socket.gethostname()}"}
