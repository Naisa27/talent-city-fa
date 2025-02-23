"""make email unique users

Revision ID: 577232c1a009
Revises: 2b7a1385b7ac
Create Date: 2025-02-23 21:19:56.911227

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "577232c1a009"
down_revision: Union[str, None] = "2b7a1385b7ac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.create_unique_constraint(None, "users", ["email"])


def downgrade_db_talent_city() -> None:
    op.drop_constraint(None, "users", type_="unique")
