""" 'uvicorn main_path:app --reload' """

from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """ TEST WITH PATHS:
    path example: /files//home/johndoe/myfile.txt"""
    return {"file_path": file_path}