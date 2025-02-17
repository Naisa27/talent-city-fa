"""add users

Revision ID: 07206d8bf427
Revises: 7fd0f3caee79
Create Date: 2025-02-18 00:25:28.760568

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "07206d8bf427"
down_revision: Union[str, None] = "7fd0f3caee79"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("last_name", sa.String(length=250), nullable=False),
        sa.Column("first_name", sa.String(length=250), nullable=False),
        sa.Column("patronimic", sa.String(length=250), nullable=True),
        sa.Column("city", sa.String(length=250), nullable=True),
        sa.Column("email", sa.String(length=250), nullable=False),
        sa.Column("phone", sa.String(length=15), nullable=False),
        sa.Column("hashed_password", sa.String(length=250), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False
        ),
        sa.Column(
            "isBlocked", sa.Boolean(), server_default=sa.text("FALSE"), nullable=False
        ),
        sa.Column("blocked_at", sa.DateTime(), nullable=True),
        sa.Column(
            "isActive", sa.Boolean(), server_default=sa.text("TRUE"), nullable=False
        ),
        sa.Column("active_at", sa.DateTime(), nullable=True),
        sa.Column("disactive_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.alter_column(
        "articles", "publish_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    op.alter_column(
        "articles", "unpublish_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    op.alter_column(
        "articles", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    op.alter_column(
        "articles", "deleted_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )


def downgrade_db_talent_city() -> None:
    op.alter_column(
        "articles", "deleted_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    op.alter_column(
        "articles", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    op.alter_column(
        "articles", "unpublish_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    op.alter_column(
        "articles", "publish_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    op.drop_table("users")
