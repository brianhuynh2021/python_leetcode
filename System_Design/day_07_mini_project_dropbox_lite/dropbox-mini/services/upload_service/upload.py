from fastapi import FastAPI, Depends, HTTPException, UploadFile, File as FastAPIFile
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
import hashlib
import uuid
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.database import get_db
from common.models import File, FileVersion, FileChunk, User
from common.s3_client import s3_client
from common.config import Config
from services.auth_service.auth import get_current_user

app = FastAPI(title="Upload Service", version="1.0.0")


class UploadInitRequest(BaseModel):
    file_name: str
    file_size: int
    file_hash: str
    file_path: str = "/"


class ChunkUploadRequest(BaseModel):
    version_id: str
    chunk_index: int
    chunk_hash: str


class UploadInitResponse(BaseModel):
    file_id: str
    version_id: str
    chunk_size: int
    num_chunks: int
    deduplication: bool


@app.post("/upload/init", response_model=UploadInitResponse)
async def init_upload(
    request: UploadInitRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Check storage limit
    if current_user.storage_used + request.file_size > current_user.storage_limit:
        raise HTTPException(status_code=400, detail="Storage limit exceeded")

    # Check if file with same hash exists (deduplication)
    existing_version = (
        db.query(FileVersion).filter(FileVersion.file_hash == request.file_hash).first()
    )

    if existing_version:
        # File already exists, just create metadata reference
        file_record = File(
            user_id=current_user.user_id,
            file_name=request.file_name,
            file_path=request.file_path,
            file_size=request.file_size,
            file_hash=request.file_hash,
        )
        db.add(file_record)
        db.commit()

        return UploadInitResponse(
            file_id=str(file_record.file_id),
            version_id=str(existing_version.version_id),
            chunk_size=Config.CHUNK_SIZE,
            num_chunks=0,
            deduplication=True,
        )

    # Create new file record
    file_record = File(
        user_id=current_user.user_id,
        file_name=request.file_name,
        file_path=request.file_path,
        file_size=request.file_size,
        file_hash=request.file_hash,
    )
    db.add(file_record)
    db.flush()

    # Create version
    version = FileVersion(
        file_id=file_record.file_id,
        version_number=1,
        file_hash=request.file_hash,
        file_size=request.file_size,
        storage_path=f"{current_user.user_id}/{file_record.file_id}",
    )
    db.add(version)
    db.commit()

    # Calculate chunks
    num_chunks = (request.file_size + Config.CHUNK_SIZE - 1) // Config.CHUNK_SIZE

    return UploadInitResponse(
        file_id=str(file_record.file_id),
        version_id=str(version.version_id),
        chunk_size=Config.CHUNK_SIZE,
        num_chunks=num_chunks,
        deduplication=False,
    )


@app.post("/upload/chunk")
async def upload_chunk(
    version_id: str,
    chunk_index: int,
    chunk_hash: str,
    chunk_file: UploadFile = FastAPIFile(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verify version belongs to user
    version = db.query(FileVersion).filter(FileVersion.version_id == version_id).first()

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    # Read chunk data
    chunk_data = await chunk_file.read()

    # Verify chunk hash
    calculated_hash = hashlib.sha256(chunk_data).hexdigest()
    if calculated_hash != chunk_hash:
        raise HTTPException(status_code=400, detail="Chunk hash mismatch")

    # Upload to S3
    object_key = f"{version.storage_path}/chunk_{chunk_index}"
    s3_client.upload_chunk(chunk_data, object_key)

    # Save chunk metadata
    chunk_record = FileChunk(
        version_id=version.version_id,
        chunk_index=chunk_index,
        chunk_hash=chunk_hash,
        chunk_size=len(chunk_data),
        storage_path=object_key,
    )
    db.add(chunk_record)
    db.commit()

    return {"chunk_index": chunk_index, "uploaded": True}


@app.post("/upload/complete/{version_id}")
async def complete_upload(
    version_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    version = db.query(FileVersion).filter(FileVersion.version_id == version_id).first()

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    # Verify all chunks uploaded
    chunks = (
        db.query(FileChunk)
        .filter(FileChunk.version_id == version_id)
        .order_by(FileChunk.chunk_index)
        .all()
    )

    expected_chunks = (version.file_size + Config.CHUNK_SIZE - 1) // Config.CHUNK_SIZE
    if len(chunks) != expected_chunks:
        raise HTTPException(status_code=400, detail="Missing chunks")

    # Update user storage
    current_user.storage_used += version.file_size
    db.commit()

    return {"version_id": str(version.version_id), "status": "completed"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
