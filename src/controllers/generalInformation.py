import pandas as pd
import numpy as np
from src.schemas.common import FileParams
from src.schemas.generalInformation import PreviewParams

async def summaryData(fileParams: FileParams, path: str): 
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

  return {
    'state': 'Success', 
    'data': {
      'instances': df.shape[0], 
      'attributes': df.shape[1], 
      'null': int(df.isnull().sum().sum())
    }, 
    'message': 'Query executed successfully'
  }

async def attributesInfo(fileParams: FileParams, path: str): 
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

  df_attributes = df.dtypes
  df_attributes = df_attributes.to_frame().reset_index()
  df_attributes.columns = ['attribute', 'type']
  df_attributes['nulls(%)'] = np.round([df[col].isnull().sum() / df.shape[0] for col in df.columns], 2)
  df_attributes['unique'] = [df[col].nunique() for col in df.columns]
  
  df_attributes['type'] = df_attributes['type'].astype(str)
  return {
    'state': 'Success', 
    'data': df_attributes.to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def previewData(previewParams: PreviewParams, path: str): 
  if not previewParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = previewParams.delimiter
  decimal = previewParams.decimal
  n = previewParams.n

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  return {
    'state': 'Success', 
    'data': df.head(n).to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def describeData(fileParams: FileParams, path: str): 
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

  df_describe = df.describe().reset_index()
  df_describe.rename(columns = {'index': 'measure'}, inplace = True)
  df_describe = df_describe.round(2)
  return {
    'state': 'Success', 
    'data': df_describe.to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }