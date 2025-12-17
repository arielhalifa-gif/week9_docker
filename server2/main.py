from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json
import uvicorn

app2 = FastAPI()

DB_PATH = Path("db/shopping_list.json")

class Item(BaseModel):
    id: int
    name: str
    quantity: int

def load_database() -> list:
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")

def save_database(data: list) -> None:
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

@app2.get("/items")
def list_all_items() -> None:
    items = load_database()
    return items


@app2.post("/item")
def add_item(name, quantity):
    db_shopping_list = load_database()
    item_id = len(db_shopping_list) + 1
    new_item = {"id": item_id, "name": name, "quantity": quantity}
    db_shopping_list.append(new_item)
    save_database(db_shopping_list)
    return {"message": "item added succesfully",
            "item id": item_id,
            "new item": new_item}

if __name__ == "__main__":
    uvicorn.run(app2, host = 0.0.0.0, port = 8080)