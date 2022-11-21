""" 'uvicorn 05_main_validations_q_p:app --reload' """
from fastapi import FastAPI, Query, Path, Body
# Path cumple el mismo funcionamiento que Query pero para parametros de la url
# Body cumple el mismo funcionamiento que Query pero para parametros del body.

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query( # Query nos sirve para agregar descripciones y validaciones del q param
        default=None, min_length=3, max_length=50, title="title to swagger", description="desc to swagger"
    ),
    int_q: int | None = Query(
        default=None, gt=1, le=10
    ),
    list: list[str] | None = Query(default=None) # query params as list
):
    """ TEST Query Params with validators """
    results = {"items": [{"item_id":"Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    if list:
        """Declare query param too many times with the values to append to the list
        http://localhost:8000/items/?list=pepe&list=saul
        returns:{"items":[{"item_id":"Foo"},{"item_id":"Bar"}],"list":["pepe","saul"]}"""
        results.update({"list": list})
    if int_q:
        results.update({"int_q": int_q})
    return results
