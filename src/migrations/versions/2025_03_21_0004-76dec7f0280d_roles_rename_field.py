"""roles rename field

Revision ID: 76dec7f0280d
Revises: 9d9e98c6dcb1
Create Date: 2025-03-21 00:04:21.185089

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "76dec7f0280d"
down_revision: Union[str, None] = "9d9e98c6dcb1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column("roles", sa.Column("disactive_at", sa.DateTime(), nullable=True))
    op.drop_column("roles", "active_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "roles",
        sa.Column(
            "active_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("roles", "disactive_at")
