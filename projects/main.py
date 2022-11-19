"""
El comando 'uvicorn main:app --reload' se refiere a:

main: el archivo main.py (el "módulo" de Python).
app: el objeto creado dentro de main.py con la línea app = FastAPI().
--reload: hace que el servidor se reinicie cada vez que cambia el código.
Úsalo únicamente para desarrollo.
"""
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    """ Enum de strings """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get("/models/{models_name}")
async def get_model(model_name: ModelName):
    """ GET TEST WITHS ENUMS """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
