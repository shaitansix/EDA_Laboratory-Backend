from fastapi import APIRouter
from src.schemas.chatbot import ChatHistory
from src.controllers.chatbot import ollamaChat

router = APIRouter(tags = ['Chatbot'])

@router.post('/query')
async def chatbot(payload: ChatHistory = None): 
  try: 
    res = await ollamaChat(payload)
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }