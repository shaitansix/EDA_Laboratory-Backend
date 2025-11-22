import pandas as pd

async def saveFile(fileMetadata: dict, path: str): 
  file = fileMetadata['file']
  delimiter = fileMetadata['delimiter']
  decimal = fileMetadata['decimal']

  ext = file.filename.split('.')[-1]
  if (ext != 'csv'): 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': 'The file must be .csv'
    }

  contents = await file.read()
  with open(path, 'wb') as f: 
    f.write(contents)
  
  df = pd.read_csv(
    path, 
    sep = delimiter, 
    decimal = decimal, 
    encoding = 'utf-8'
  )
  df_filtered = df.select_dtypes(include = ['float64', 'int64', 'float32', 'int32'])

  return {
    'state': 'Success', 
    'data': {
      'name': file.filename, 
      'attributes': { 
        'all': df.columns.tolist(), 
        'numeric': df_filtered.columns.tolist()
      },
      'delimiter': delimiter, 
      'decimal': decimal
    }, 
    'message': 'File uploaded successfully'
  }