"""roles add column

Revision ID: 644fdfa2c24e
Revises: a8b02272348c
Create Date: 2025-03-19 23:41:22.859761

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "644fdfa2c24e"
down_revision: Union[str, None] = "a8b02272348c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column(
        "roles",
        sa.Column(
            "mark_for_del",
            sa.Boolean(),
            server_default=sa.text("FALSE"),
            nullable=False,
        ),
    )
    op.add_column("roles", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    op.drop_column("roles", "disactive_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "roles",
        sa.Column(
            "disactive_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("roles", "deleted_at")
    op.drop_column("roles", "mark_for_del")
