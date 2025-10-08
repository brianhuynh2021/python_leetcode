import os
import sys
from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.database import get_db
from common.models import File, User
from services.auth_service.auth import get_current_user

app = FastAPI(title="Metadata Service", version="1.0.0")


class FileMetadata(BaseModel):
    file_id: str
    file_name: str
    file_path: str
    file_size: int
    file_type: str | None
    created_at: datetime
    updated_at: datetime | None


class FileListResponse(BaseModel):
    files: List[FileMetadata]
    total: int


@app.get("/files", response_model=FileListResponse)
async def list_files(
    path: str = "/",
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    files = (
        db.query(File)
        .filter(
            File.user_id == current_user.user_id,
            File.file_path == path,
            File.is_deleted == False,
        )
        .all()
    )

    file_list = [
        FileMetadata(
            file_id=str(f.file_id),
            file_name=f.file_name,
            file_path=f.file_path,
            file_size=f.file_size,
            file_type=f.file_type,
            created_at=f.created_at,
            updated_at=f.updated_at,
        )
        for f in files
    ]

    return FileListResponse(files=file_list, total=len(file_list))


@app.get("/files/{file_id}", response_model=FileMetadata)
async def get_file_metadata(
    file_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
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

    return FileMetadata(
        file_id=str(file_record.file_id),
        file_name=file_record.file_name,
        file_path=file_record.file_path,
        file_size=file_record.file_size,
        file_type=file_record.file_type,
        created_at=file_record.created_at,
        updated_at=file_record.updated_at,
    )


@app.delete("/files/{file_id}")
async def delete_file(
    file_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file_record = (
        db.query(File)
        .filter(File.file_id == file_id, File.user_id == current_user.user_id)
        .first()
    )

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    # Soft delete
    file_record.is_deleted = True
    db.commit()

    return {"message": "File deleted successfully"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
