"""add user_id in articles

Revision ID: d36653eeb324
Revises: 2de7e6cfbd6a
Create Date: 2025-02-18 00:48:37.702809

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d36653eeb324"
down_revision: Union[str, None] = "2de7e6cfbd6a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.add_column("articles", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "articles", "users", ["user_id"], ["id"])


def downgrade_db_talent_city() -> None:
    op.drop_constraint(None, "articles", type_="foreignkey")
    op.drop_column("articles", "user_id")
