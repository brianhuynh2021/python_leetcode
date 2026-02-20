"""
Order Service (FastAPI)
- Owns order data
- Independent deployment unit
- Demonstrates a common microservices pattern: validate user via a call to user-service
  (in production, you'd add caching, timeouts, circuit breakers, and/or async events).

Run:
  pip install fastapi uvicorn httpx
  uvicorn order_service:app --reload --port 8002

Requires:
  user_service running on :8001
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid
import httpx

app = FastAPI(title="Order Service Demo")

ORDERS: Dict[str, dict] = {}

USER_SVC = "http://127.0.0.1:8001"
TIMEOUT = 3.0

class CreateOrder(BaseModel):
    user_id: str
    item: str
    qty: int = 1

async def user_exists(user_id: str) -> bool:
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.get(f"{USER_SVC}/users/{user_id}")
    return r.status_code == 200

@app.post("/orders")
async def create_order(payload: CreateOrder):
    if not await user_exists(payload.user_id):
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
