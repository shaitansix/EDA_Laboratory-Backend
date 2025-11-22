import pandas as pd
from src.schemas.common import FileParams
from src.schemas.correlation import DispersionParams

async def correlationMatrix(fileParams: FileParams, path: str): 
  if not fileParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = fileParams.delimiter
  decimal = fileParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  df = df.select_dtypes(include = ['float64', 'int64', 'float32', 'int32'])
  df_corr = df.corr(method = 'pearson')
  df_corr = df_corr.unstack().reset_index().round(2)
  df_corr.columns = ['attribute_1', 'attribute_2', 'correlation']
  return {
    'state': 'Success', 
    'data': df_corr.to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def dispersionData(dispersionParams: DispersionParams, path: str): 
  if not dispersionParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = dispersionParams.delimiter
  decimal = dispersionParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  attribute_x = dispersionParams.attribute_x
  attribute_y = dispersionParams.attribute_y

  x = df[attribute_x].values
  y = df[attribute_y].values
  return {
    'state': 'Success', 
    'data': {
      'x': x.tolist(), 
      'y': y.tolist()
    }, 
    'message': 'Query executed successfully'
  }