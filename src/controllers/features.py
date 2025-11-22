import pandas as pd
from src.schemas.features import FeatureSelectionParams, PreprocessParams, FeatureImportanceParams
from util.model import preprocesingData, featureImportance

async def correlationMatrix(featureSelectionParams: FeatureSelectionParams, path: str): 
  if not featureSelectionParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = featureSelectionParams.delimiter
  decimal = featureSelectionParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  threshold = featureSelectionParams.threshold
  df = df.select_dtypes(include = ['float64', 'int64', 'float32', 'int32'])
  df_corr = df.corr(method = 'pearson')
  df_corr = df_corr.unstack().reset_index().round(2)
  df_corr.columns = ['attribute_1', 'attribute_2', 'correlation']
  df_corr = df_corr[
    (df_corr['correlation'].abs() >= threshold) & (df_corr['correlation'] < 1)
  ]
  return {
    'state': 'Success', 
    'data': df_corr.to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def modelDataPreview(preprocessParams: PreprocessParams, path: str): 
  if not preprocessParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = preprocessParams.delimiter
  decimal = preprocessParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  target = preprocessParams.target
  encode = preprocessParams.encode

  df = preprocesingData(df, target, encode)
  return {
    'state': 'Success', 
    'data': df.head(5).to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def modelFeatures(featureImportanceParams: FeatureImportanceParams, path: str): 
  if not featureImportanceParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = featureImportanceParams.delimiter
  decimal = featureImportanceParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  model = featureImportanceParams.model
  df_importance = featureImportance(df, model).round(4).head(8)
  return {
    'state': 'Success', 
    'data': {
      'x': df_importance['importance'].to_list(), 
      'y': df_importance['attribute'].to_list()
    },
    'message': 'Query executed successfully'
  }