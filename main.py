from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Create the FastAPI app
app = FastAPI()

# Sample data (in-memory database)
fake_db = {}

# Define a model for the data
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Route: GET (Read data)
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id in fake_db:
        return fake_db[item_id]
    return {"error": "Item not found"}

# Route: POST (Create new data)
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_id = len(fake_db) + 1
    fake_db[item_id] = item
    return {"item_id": item_id, **item.dict()}

# Route: PUT (Update data)
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        return {"error": "Item not found"}
    fake_db[item_id] = item
    return item

# Route: DELETE (Delete data)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"message": f"Item {item_id} deleted successfully"}
    return {"error": "Item not found"}
