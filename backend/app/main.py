from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .bedrock_service import BedrockService
from .config import settings

app = FastAPI(title="Seu Python API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bedrock_service = BedrockService()

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "Seu Python API - Python Brasil 2025 🐍"}

@app.post("/chat", response_model=ChatResponse)
async def chat(chat_message: ChatMessage):
    response = await bedrock_service.get_response(chat_message.message)
    return ChatResponse(response=response)

@app.get("/health")
async def health():
    return {"status": "healthy"}
