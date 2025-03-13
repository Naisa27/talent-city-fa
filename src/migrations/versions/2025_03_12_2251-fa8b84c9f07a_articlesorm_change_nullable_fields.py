"""ArticlesOrm change nullable fields

Revision ID: fa8b84c9f07a
Revises: 577232c1a009
Create Date: 2025-03-12 22:51:54.912504

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa8b84c9f07a"
down_revision: Union[str, None] = "577232c1a009"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.alter_column("articles", "article_body", existing_type=sa.TEXT(), nullable=True)
    op.alter_column("articles", "title_img", existing_type=sa.TEXT(), nullable=True)


def downgrade_db_talent_city() -> None:
    op.alter_column("articles", "title_img", existing_type=sa.TEXT(), nullable=False)
    op.alter_column("articles", "article_body", existing_type=sa.TEXT(), nullable=False)
