# =====================
# MONOLITH
# =====================
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


# =====================
# MICROSERVICES: GATEWAY
# =====================
"""
API Gateway example (FastAPI)
- In real life you would also add auth, rate limits, routing rules, retries/timeouts, etc.

Run:
  pip install fastapi uvicorn httpx
  uvicorn gateway:app --reload --port 8000

Requires:
  user_service running on :8001
  order_service running on :8002
"""

from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Gateway Demo")

USER_SVC = "http://127.0.0.1:8001"
ORDER_SVC = "http://127.0.0.1:8002"

# NOTE: In production, ALWAYS set timeouts.
TIMEOUT = 3.0

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.get(f"{USER_SVC}/users/{user_id}")
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()

@app.post("/users")
async def create_user(payload: dict):
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.post(f"{USER_SVC}/users", json=payload)
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()

@app.post("/orders")
async def create_order(payload: dict):
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.post(f"{ORDER_SVC}/orders", json=payload)
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()

@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.get(f"{ORDER_SVC}/orders/{order_id}")
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    return r.json()


# =====================
# MICROSERVICES: USER SERVICE
# =====================
"""
User Service (FastAPI)
- Owns user data
- Independent deployment unit

Run:
  pip install fastapi uvicorn
  uvicorn user_service:app --reload --port 8001
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI(title="User Service Demo")

USERS: Dict[str, dict] = {}

class CreateUser(BaseModel):
    email: str
    name: str

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


# =====================
# MICROSERVICES: ORDER SERVICE
# =====================
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
