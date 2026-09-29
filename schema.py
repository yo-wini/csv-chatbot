from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class QueryIntent(BaseModel):
    intent: str