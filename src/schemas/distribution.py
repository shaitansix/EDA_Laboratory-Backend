from src.schemas.common import FileParams

class HistogramParams(FileParams): 
  attribute: str
  bins: int