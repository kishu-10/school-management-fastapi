from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.v1.api import apiv1 

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/api/v1", apiv1)

@app.get("/")
async def main():
    return {"message": "Hello World"}