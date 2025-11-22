from ollama import Client
import os
from src.schemas.chatbot import ChatHistory

async def ollamaChat(payload: ChatHistory): 
  if not payload: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing payload'
    }
  
  API_KEY = os.environ.get('OLLAMA_API_KEY')
  client = Client(
    host = 'https://ollama.com', 
    headers = {'Authorization': f'Bearer {API_KEY}'}
  )

  responseOllama = client.chat(
    model = 'gpt-oss:20b', 
    messages = [msg.model_dump() for msg in payload.history], 
    stream = True
  )

  reply = ''
  for part in responseOllama:
    reply += part['message']['content']
  
  return {
    'state': 'Success', 
    'data': {
      'role': 'assistant', 
      'content': reply
    }, 
    'message': 'Query executed successfully'
  }