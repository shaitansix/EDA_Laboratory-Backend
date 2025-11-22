from pydantic import BaseModel

class FileParams(BaseModel): 
  delimiter: str
  decimal: str