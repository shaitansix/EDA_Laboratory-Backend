import os
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app): 
  CORS_ORIGINS = os.getenv('CORS_ORIGINS')
  app.add_middleware(
    CORSMiddleware, 
    allow_origins = CORS_ORIGINS.split(','), 
    allow_credentials = True, 
    allow_methods = ['*'], 
    allow_headers = ['*']
  )