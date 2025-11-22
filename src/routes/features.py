from fastapi import APIRouter
from src.schemas.features import FeatureSelectionParams, PreprocessParams, FeatureImportanceParams
from src.controllers.features import correlationMatrix, modelDataPreview, modelFeatures

router = APIRouter(tags = ['Features'])

@router.post('/matrix')
async def matrix(featureSelectionParams: FeatureSelectionParams = None): 
  try: 
    res = await correlationMatrix(featureSelectionParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }
  
@router.post('/preprocess')
async def preprocess(preprocessParams: PreprocessParams = None): 
  try: 
    res = await modelDataPreview(preprocessParams, './data/dataset.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }
  
@router.post('/model')
async def model(featureImportanceParams: FeatureImportanceParams = None): 
  try: 
    res = await modelFeatures(featureImportanceParams, './data/df_model.csv')
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }