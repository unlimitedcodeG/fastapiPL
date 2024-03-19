from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool| None
    model_config = {
    "json_schema_extra": {
        "examples": [
            {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        ]
    }
}
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items(skip:int = 0, limit:int = 10):
    return fake_items_db[skip: skip + limit]
    

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str| None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id":item_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}