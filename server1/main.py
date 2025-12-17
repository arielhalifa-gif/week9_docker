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

def load_database() -> dict:
    try:
        with open("shopping_list.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")

@app.get("/items")
def list_all_items() -> None:
    items = load_database()
    return items


@app.post("/item")
def add_item(item:Item):
    db_shopping_list = load_database()
    item_id = len(db_shopping_list) + 1
    db_shopping_list