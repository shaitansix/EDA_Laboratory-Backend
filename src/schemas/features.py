from src.schemas.common import FileParams

class FeatureSelectionParams(FileParams): 
  threshold: float

class PreprocessParams(FileParams): 
  target: str
  encode: bool

class FeatureImportanceParams(FileParams): 
  model: str