"""article_themes add column

Revision ID: 4f78ed967efe
Revises: 644fdfa2c24e
Create Date: 2025-03-19 23:48:38.967632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "4f78ed967efe"
down_revision: Union[str, None] = "644fdfa2c24e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column(
        "article_themes",
        sa.Column(
            "mark_for_del",
            sa.Boolean(),
            server_default=sa.text("FALSE"),
            nullable=False,
        ),
    )
    op.add_column(
        "article_themes", sa.Column("deleted_at", sa.DateTime(), nullable=True)
    )
    op.drop_column("article_themes", "disactive_at")


def downgrade_db_talent_city() -> None:
    op.add_column(
        "article_themes",
        sa.Column(
            "disactive_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("article_themes", "deleted_at")
    op.drop_column("article_themes", "mark_for_del")
