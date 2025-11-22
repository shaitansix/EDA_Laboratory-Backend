from fastapi import APIRouter
from src.schemas.common import FileParams
from src.schemas.distribution import HistogramParams
from src.controllers.distribution import skewnessData, histogramData

router = APIRouter(tags = ['Distribution'])

@router.post('/skewness')
async def skewness(fileParams: FileParams = None): 
  try: 
    res = await skewnessData(fileParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }
  
@router.post('/histogram')
async def histogram(histogramParams: HistogramParams = None): 
  try: 
    res = await histogramData(histogramParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }