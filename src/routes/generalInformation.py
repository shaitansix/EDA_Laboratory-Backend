from fastapi import APIRouter
from src.schemas.common import FileParams
from src.schemas.generalInformation import PreviewParams
from src.controllers.generalInformation import summaryData, attributesInfo, previewData, describeData

router = APIRouter(tags = ['General Information'])

@router.post('/summary')
async def summary(fileParams: FileParams = None): 
  try: 
    res = await summaryData(fileParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }

@router.post('/attributes')
async def attributes(fileParams: FileParams = None): 
  try: 
    res = await attributesInfo(fileParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }

@router.post('/preview')
async def preview(previewParams: PreviewParams = None): 
  try: 
    res = await previewData(previewParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }
  
@router.post('/describe')
async def describe(fileParams: FileParams = None): 
  try: 
    res = await describeData(fileParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }