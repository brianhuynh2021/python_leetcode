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
