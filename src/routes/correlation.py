from fastapi import APIRouter
from src.schemas.common import FileParams
from src.schemas.correlation import DispersionParams
from src.controllers.correlation import correlationMatrix, dispersionData

router = APIRouter(tags = ['Correlation'])

@router.post('/matrix')
async def matrix(fileParams: FileParams = None): 
  try: 
    res = await correlationMatrix(fileParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }
  
@router.post('/dispersion')
async def dispersion(dispersionParams: DispersionParams = None): 
  try: 
    res = await dispersionData(dispersionParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }