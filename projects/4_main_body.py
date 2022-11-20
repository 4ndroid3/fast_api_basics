""" 'uvicorn 04_main_body:app --reload' """

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """ example of a model """
    name: str
    description: str | None = None # Este parametro no es obligatorio.
    price: float
    tax: float | None = None # Este parametro no es obligatorio.

app = FastAPI()


@app.post("/items/")
async def create_item(item_id: int, item: Item, q: str | None = None):
    """ 
    TEST BODY WITH, URL param, QUERY PARAM & BODY
    ---------
    The function parameters will be recognized as follows:

    - If the parameter is also declared in the path,
      it will be used as a path parameter.
    - If the parameter is of a singular type (like int, float, str, bool, etc)
      it will be interpreted as a query parameter.
    - If the parameter is declared to be of the type of a Pydantic model,
      it will be interpreted as a request body.
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
