from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI()

# DB_PATH = Path("db/shopping_list.json")

class Item(BaseModel):
    id: int
    name: str
    quantity: int

def load_database() -> list:
    try:
        with open("shopping_list.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")

def save_database(data: list) -> None:
    with open("shopping_list.json", "w") as f:
        json.dump(data, f, indent=2)

@app.get("/items")
def list_all_items() -> None:
    items = load_database()
    return items


@app.post("/item")
def add_item(name, quantity):
    db_shopping_list = load_database()
    item_id = len(db_shopping_list) + 1
    new_item = {"id": item_id, "name": name, "quantity": quantity}
    db_shopping_list.append(new_item)
    save_database(db_shopping_list)
    return {"message": "item added succesfully",
            "item id": item_id,
            "new item": new_item}

