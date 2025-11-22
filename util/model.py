import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, ExtraTreesClassifier, ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder

def preprocesingData(df: pd.DataFrame, target: str, encode: bool): 
  col_target = df[target]
  if col_target.dtype == 'object':
    labelEncoder = LabelEncoder()
    col_target = labelEncoder.fit_transform(col_target)
  else:
    unique = col_target.unique()
    if np.issubdtype(unique.dtype, np.integer) and unique.shape[0] <= 20:
      labelEncoder = LabelEncoder()
      col_target = labelEncoder.fit_transform(col_target)

  df = df.drop(target, axis = 1)
  if encode: 
    df = pd.get_dummies(df, dtype = float)
  else: 
    df = df.select_dtypes(include = ['float64', 'int64', 'float32', 'int32'])
  df[target] = col_target

  df.to_csv('./data/df_model.csv', index = False)
  return df

def featureImportance(df: pd.DataFrame, model: str): 
  target = df.columns[-1]
  X = df.drop(target, axis = 1)
  y = df[target]
  models = {
    'Random Forest': {
      'regression': RandomForestRegressor(criterion = 'squared_error', n_estimators = 100), 
      'classification': RandomForestClassifier(n_estimators = 100)
    }, 
    'Extra Trees': {
      'regression': ExtraTreesRegressor(criterion = 'squared_error'), 
      'classification': ExtraTreesClassifier()
    }
  }

  problem = 'regression'
  if y.dtype == 'object':
    problem = 'classification'
  else:
    unique = y.unique()
    if np.issubdtype(unique.dtype, np.integer) and unique.shape[0] <= 20:
      problem = 'classification'
  
  model_ml = models[model][problem]
  model_ml.fit(X, y)
  df_importance = pd.DataFrame({
    'attribute': X.columns,
    'importance': model_ml.feature_importances_
  }).sort_values('importance', ascending = False)
  return df_importance