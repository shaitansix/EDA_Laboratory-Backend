import pandas as pd
import numpy as np
from scipy import stats
from src.schemas.common import FileParams
from src.schemas.distribution import HistogramParams

async def skewnessData(fileParams: FileParams, path: str): 
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

  df_skweness = df.select_dtypes(include = ['float64', 'int64', 'float32', 'int32'])
  df_skweness = df_skweness.skew().round(2).reset_index()
  df_skweness.columns = ['attribute', 'skewness']
  return {
    'state': 'Success', 
    'data': df_skweness.to_dict(orient = 'records'), 
    'message': 'Query executed successfully'
  }

async def histogramData(histogramParams: HistogramParams, path: str): 
  if not histogramParams: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'Missing parameters'
    }
  
  delimiter = histogramParams.delimiter
  decimal = histogramParams.decimal

  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )

  bins = histogramParams.bins
  attribute = histogramParams.attribute

  hist, bins = np.histogram(df[attribute], bins = bins, density = True)
  kde = stats.gaussian_kde(df.loc[:, attribute].values)
  kde_x = np.linspace(min(df.loc[:, attribute].values), max(df.loc[:, attribute].values), histogramParams.bins * 10)
  kde_y = kde(kde_x)

  hist_points = [{'x': x, 'y': y} for x, y in zip(np.round(bins[:-1], 2), np.round(hist, 2))]
  kde_points = [{'x': x, 'y': y} for x, y in zip(np.round(kde_x, 4), np.round(kde_y, 4))]
  return {
    'state': 'Success', 
    'data': {
      'hist': hist_points, 
      'kde': kde_points
    }, 
    'message': 'Query executed successfully'
  }