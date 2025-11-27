from fastapi import FastAPI, APIRouter
from src.routes.file import router as fileRouter
from src.routes.generalInformation import router as informationRouter
from src.routes.distribution import router as distributionRouter
from src.routes.correlation import router as correlationRouter
from src.routes.features import router as featuresRouter
from src.routes.chatbot import router as chatbotRouter
from src.config.cors import setup_cors
from dotenv import load_dotenv

load_dotenv('.env.dev')
app = FastAPI(
  title = 'EDA-Laboratory API', 
  version = '1.0.0'
)
setup_cors(app)

api_router = APIRouter(prefix = '/api/v1')
api_router.include_router(prefix = '/file', router = fileRouter)
api_router.include_router(prefix = '/general-information', router = informationRouter)
api_router.include_router(prefix = '/distribution', router = distributionRouter)
api_router.include_router(prefix = '/correlation', router = correlationRouter)
api_router.include_router(prefix = '/features', router = featuresRouter)
api_router.include_router(prefix = '/chatbot', router = chatbotRouter)
app.include_router(api_router)