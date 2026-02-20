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
