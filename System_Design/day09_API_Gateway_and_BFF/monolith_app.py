"""
Monolith example (FastAPI)
- One deploy unit
- Single DB abstraction (in-memory for demo)
- Modules are organized by routers/services but run in one process

Run:
  pip install fastapi uvicorn
  uvicorn monolith_app:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import uuid

app = FastAPI(title="Monolith Demo")

# -----------------------------
# "DB" (in-memory for demo)
# -----------------------------
USERS: Dict[str, dict] = {}
ORDERS: Dict[str, dict] = {}

# -----------------------------
# Models
# -----------------------------
class CreateUser(BaseModel):
    email: str
    name: str

class CreateOrder(BaseModel):
    user_id: str
    item: str
    qty: int = 1

# -----------------------------
# User module
# -----------------------------
@app.post("/users")
def create_user(payload: CreateUser):
    user_id = str(uuid.uuid4())
    USERS[user_id] = {"id": user_id, "email": payload.email, "name": payload.name}
    return USERS[user_id]

@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# -----------------------------
# Order module
# -----------------------------
@app.post("/orders")
def create_order(payload: CreateOrder):
    if payload.user_id not in USERS:
        raise HTTPException(status_code=400, detail="Invalid user_id")

    order_id = str(uuid.uuid4())
    ORDERS[order_id] = {
        "id": order_id,
        "user_id": payload.user_id,
        "item": payload.item,
        "qty": payload.qty,
        "status": "CREATED",
    }
    return ORDERS[order_id]

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/users/{user_id}/orders")
def list_orders_for_user(user_id: str) -> List[dict]:
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [o for o in ORDERS.values() if o["user_id"] == user_id]
