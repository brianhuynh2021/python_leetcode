from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.database import get_db
from common.models import File, User
from services.auth_service.auth import get_current_user

app = FastAPI(title="Sync Service", version="1.0.0")


class FileChange(BaseModel):
    file_id: str
    file_name: str
    action: str  # created, modified, deleted
    timestamp: datetime


class SyncDeltaResponse(BaseModel):
    changes: List[FileChange]
    last_sync_time: datetime


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, user_id: str, message: dict):
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_json(message)


manager = ConnectionManager()


@app.get("/sync/delta", response_model=SyncDeltaResponse)
async def get_sync_delta(
    since: datetime,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Get files that changed since timestamp
    changed_files = (
        db.query(File)
        .filter(File.user_id == current_user.user_id, File.updated_at > since)
        .all()
    )

    changes = []
    for file in changed_files:
        if file.is_deleted:
            action = "deleted"
        elif file.created_at > since:
            action = "created"
        else:
            action = "modified"

        changes.append(
            FileChange(
                file_id=str(file.file_id),
                file_name=file.file_name,
                action=action,
                timestamp=file.updated_at or file.created_at,
            )
        )

    return SyncDeltaResponse(changes=changes, last_sync_time=datetime.utcnow())


@app.websocket("/ws/sync/{user_id}")
async def websocket_sync(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle ping/pong or other messages
            await websocket.send_json({"type": "pong"})
    except WebSocketDisconnect:
        manager.disconnect(user_id)


@app.post("/sync/notify")
async def notify_change(user_id: str, change: FileChange):
    """Notify user about file changes via WebSocket"""
    await manager.send_personal_message(
        user_id, {"type": "file_change", "data": change.dict()}
    )
    return {"status": "notified"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
