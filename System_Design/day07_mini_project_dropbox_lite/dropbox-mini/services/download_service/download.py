import os
import sys

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.database import get_db
from common.models import File, FileChunk, FileVersion, User
from common.s3_client import s3_client
from services.auth_service.auth import get_current_user

app = FastAPI(title="Download Service", version="1.0.0")


class DownloadResponse(BaseModel):
    file_id: str
    file_name: str
    file_size: int
    download_url: str
    expires_in: int


@app.get("/download/{file_id}")
async def download_file(
    file_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Get file metadata
    file_record = (
        db.query(File)
        .filter(
            File.file_id == file_id,
            File.user_id == current_user.user_id,
            File.is_deleted == False,
        )
        .first()
    )

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    # Get latest version
    version = (
        db.query(FileVersion)
        .filter(FileVersion.file_id == file_id)
        .order_by(FileVersion.version_number.desc())
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="File version not found")

    # Get all chunks
    chunks = (
        db.query(FileChunk)
        .filter(FileChunk.version_id == version.version_id)
        .order_by(FileChunk.chunk_index)
        .all()
    )

    # Stream file chunks
    async def chunk_generator():
        for chunk in chunks:
            chunk_data = s3_client.download_chunk(chunk.storage_path)
            yield chunk_data

    return StreamingResponse(
        chunk_generator(),
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={file_record.file_name}",
            "Content-Length": str(file_record.file_size),
        },
    )


@app.get("/download/{file_id}/url", response_model=DownloadResponse)
async def get_download_url(
    file_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Get file metadata
    file_record = (
        db.query(File)
        .filter(
            File.file_id == file_id,
            File.user_id == current_user.user_id,
            File.is_deleted == False,
        )
        .first()
    )

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    # Get latest version
    version = (
        db.query(FileVersion)
        .filter(FileVersion.file_id == file_id)
        .order_by(FileVersion.version_number.desc())
        .first()
    )

    # Generate presigned URL for first chunk (simplified)
    first_chunk = (
        db.query(FileChunk)
        .filter(FileChunk.version_id == version.version_id, FileChunk.chunk_index == 0)
        .first()
    )

    download_url = s3_client.generate_presigned_url(first_chunk.storage_path)

    return DownloadResponse(
        file_id=str(file_record.file_id),
        file_name=file_record.file_name,
        file_size=file_record.file_size,
        download_url=download_url,
        expires_in=3600,
    )


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
