from fastapi import APIRouter, File, UploadFile, Form
from src.controllers.file import saveFile

router = APIRouter(tags = ['File'])

@router.post('/upload')
async def upload(file: UploadFile = File(...), delimiter: str = Form(...), decimal: str = Form(...)): 
  try: 
    res = await saveFile(
      {'file': file, 'delimiter': delimiter, 'decimal': decimal}, 
      './data/dataset.csv'
    )
    return res
  except Exception as exc: 
    return {
      'state': 'Failed', 
      'data': None, 
      'message': str(exc)
    }