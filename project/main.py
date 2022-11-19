"""
El comando uvicorn 'main:app --reload' se refiere a:

main: el archivo main.py (el "módulo" de Python).
app: el objeto creado dentro de main.py con la línea app = FastAPI().
--reload: hace que el servidor se reinicie cada vez que cambia el código.
Úsalo únicamente para desarrollo.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """ Prueba de GET """
    return {"message": "Hello World"}
