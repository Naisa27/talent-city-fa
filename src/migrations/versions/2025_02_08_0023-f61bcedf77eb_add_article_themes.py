"""add article_themes

Revision ID: f61bcedf77eb
Revises: 6e2f14c63344
Create Date: 2025-02-08 00:23:22.183478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f61bcedf77eb'
down_revision: Union[str, None] = '6e2f14c63344'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()





def upgrade_db_talent_city() -> None:
    op.create_table('article_themes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('theme', sa.String(length=250), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('isActive', sa.Boolean(), nullable=False),
        sa.Column('active_at', sa.DateTime(), nullable=True),
        sa.Column('disactive_at', sa.DateTime(), nullable=True),
        sa.Column('update_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade_db_talent_city() -> None:
    op.drop_table('article_themes')

