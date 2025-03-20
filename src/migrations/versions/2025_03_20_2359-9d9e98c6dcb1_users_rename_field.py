"""users rename field

Revision ID: 9d9e98c6dcb1
Revises: 4f78ed967efe
Create Date: 2025-03-20 23:59:24.783681

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "9d9e98c6dcb1"
down_revision: Union[str, None] = "4f78ed967efe"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column("users", sa.Column("disactive_at", sa.DateTime(), nullable=True))
    op.drop_column("users", "active_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "users",
        sa.Column(
            "active_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("users", "disactive_at")
