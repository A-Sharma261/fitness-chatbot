from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import ChatRequest, ChatResponse
from app.chatbot import get_fitness_response


app = FastAPI(title="Fitness Chatbot API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # okay for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Fitness chatbot backend is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = get_fitness_response(request.message)
    return ChatResponse(answer=answer)