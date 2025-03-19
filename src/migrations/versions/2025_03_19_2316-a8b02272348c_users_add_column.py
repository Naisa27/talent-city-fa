"""users add column

Revision ID: a8b02272348c
Revises: fa8b84c9f07a
Create Date: 2025-03-19 23:16:08.936749

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "a8b02272348c"
down_revision: Union[str, None] = "fa8b84c9f07a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column(
        "users",
        sa.Column(
            "mark_for_del",
            sa.Boolean(),
            server_default=sa.text("FALSE"),
            nullable=False,
        ),
    )
    op.add_column("users", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    op.drop_column("users", "disactive_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "users",
        sa.Column(
            "disactive_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("users", "deleted_at")
    op.drop_column("users", "mark_for_del")
