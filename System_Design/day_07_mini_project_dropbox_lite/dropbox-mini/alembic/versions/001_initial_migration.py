"""initial migration

Revision ID: 001
Revises:
Create Date: 2025-01-06

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create users table
    op.create_table(
        "users",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("name", sa.String(255)),
        sa.Column("password_hash", sa.String(255)),
        sa.Column("storage_used", sa.BigInteger(), default=0),
        sa.Column("storage_limit", sa.BigInteger(), default=10737418240),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )

    # Create files table
    op.create_table(
        "files",
        sa.Column("file_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.user_id")
        ),
        sa.Column("file_name", sa.String(255), nullable=False),
        sa.Column("file_path", sa.String(500)),
        sa.Column("file_size", sa.BigInteger()),
        sa.Column("file_type", sa.String(50)),
        sa.Column("file_hash", sa.String(64)),
        sa.Column("is_deleted", sa.Boolean(), default=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
    )

    # Create file_versions table
    op.create_table(
        "file_versions",
        sa.Column("version_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "file_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("files.file_id")
        ),
        sa.Column("version_number", sa.Integer(), nullable=False),
        sa.Column("storage_path", sa.String(500)),
        sa.Column("file_hash", sa.String(64)),
        sa.Column("file_size", sa.BigInteger()),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )

    # Create file_chunks table
    op.create_table(
        "file_chunks",
        sa.Column("chunk_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "version_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("file_versions.version_id"),
        ),
        sa.Column("chunk_index", sa.Integer(), nullable=False),
        sa.Column("chunk_hash", sa.String(64)),
        sa.Column("chunk_size", sa.BigInteger()),
        sa.Column("storage_path", sa.String(500)),
    )

    # Create shared_files table
    op.create_table(
        "shared_files",
        sa.Column("share_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "file_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("files.file_id")
        ),
        sa.Column(
            "owner_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.user_id")
        ),
        sa.Column(
            "shared_with_user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.user_id"),
        ),
        sa.Column("permission", sa.String(20), default="read"),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
    )

    # Create indexes
    op.create_index("idx_files_user_id", "files", ["user_id"])
    op.create_index("idx_files_hash", "files", ["file_hash"])
    op.create_index("idx_file_versions_file_id", "file_versions", ["file_id"])
    op.create_index("idx_file_chunks_version_id", "file_chunks", ["version_id"])


def downgrade():
    op.drop_table("shared_files")
    op.drop_table("file_chunks")
    op.drop_table("file_versions")
    op.drop_table("files")
    op.drop_table("users")
