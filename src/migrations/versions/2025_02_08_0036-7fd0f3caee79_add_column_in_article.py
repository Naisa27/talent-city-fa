"""add column in article

Revision ID: 7fd0f3caee79
Revises: f61bcedf77eb
Create Date: 2025-02-08 00:36:48.474596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fd0f3caee79'
down_revision: Union[str, None] = 'f61bcedf77eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()





def upgrade_db_talent_city() -> None:
    op.add_column('articles', sa.Column('article_theme_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'articles', 'article_themes', ['article_theme_id'], ['id'])


def downgrade_db_talent_city() -> None:
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_column('articles', 'article_theme_id')

