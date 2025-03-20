"""article_themes rename field

Revision ID: 50627ccf2a5b
Revises: 76dec7f0280d
Create Date: 2025-03-21 00:06:31.536102

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "50627ccf2a5b"
down_revision: Union[str, None] = "76dec7f0280d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column(
        "article_themes", sa.Column("disactive_at", sa.DateTime(), nullable=True)
    )
    op.drop_column("article_themes", "active_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "article_themes",
        sa.Column(
            "active_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("article_themes", "disactive_at")
