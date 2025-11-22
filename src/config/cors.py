from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app): 
  app.add_middleware(
    CORSMiddleware, 
    allow_origins = [
      'http://localhost:5173', 
      'http://localhost:5173/', 
      'http://localhost:4173', 
      'http://localhost:4173/', 
      'https://eda-laboratory-frontend.vercel.app', 
      'https://eda-laboratory-frontend.vercel.app/'
    ], 
    allow_credentials = True, 
    allow_methods = ['*'], 
    allow_headers = ['*']
  )