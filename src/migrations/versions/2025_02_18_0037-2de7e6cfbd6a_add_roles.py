"""add roles

Revision ID: 2de7e6cfbd6a
Revises: 07206d8bf427
Create Date: 2025-02-18 00:37:44.911906

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2de7e6cfbd6a"
down_revision: Union[str, None] = "07206d8bf427"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=250), nullable=False),
        sa.Column("description", sa.String(length=250), nullable=True),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False
        ),
        sa.Column(
            "isActive", sa.Boolean(), server_default=sa.text("TRUE"), nullable=False
        ),
        sa.Column("active_at", sa.DateTime(), nullable=True),
        sa.Column("disactive_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade_db_talent_city() -> None:
    op.drop_table("roles")
