from pydantic import BaseModel

class Message(BaseModel): 
  role: str
  content: str

class ChatHistory(BaseModel): 
  history: list[Message]