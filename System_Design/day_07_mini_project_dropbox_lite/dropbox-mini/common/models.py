from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Boolean,
    DateTime,
    Integer,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from common.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255))
    password_hash = Column(String(255))
    storage_used = Column(BigInteger, default=0)
    storage_limit = Column(BigInteger, default=10737418240)  # 10GB
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class File(Base):
    __tablename__ = "files"

    file_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500))
    file_size = Column(BigInteger)
    file_type = Column(String(50))
    file_hash = Column(String(64))  # SHA-256
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class FileVersion(Base):
    __tablename__ = "file_versions"

    version_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey("files.file_id"))
    version_number = Column(Integer, nullable=False)
    storage_path = Column(String(500))
    file_hash = Column(String(64))
    file_size = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class FileChunk(Base):
    __tablename__ = "file_chunks"

    chunk_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version_id = Column(UUID(as_uuid=True), ForeignKey("file_versions.version_id"))
    chunk_index = Column(Integer, nullable=False)
    chunk_hash = Column(String(64))
    chunk_size = Column(BigInteger)
    storage_path = Column(String(500))


class SharedFile(Base):
    __tablename__ = "shared_files"

    share_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file_id = Column(UUID(as_uuid=True), ForeignKey("files.file_id"))
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    shared_with_user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    permission = Column(String(20), default="read")  # read, write
    created_at = Column(DateTime(timezone=True), server_default=func.now())
