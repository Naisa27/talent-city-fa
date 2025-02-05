"""initial migration

Revision ID: 6e2f14c63344
Revises: 
Create Date: 2025-02-05 23:55:50.133872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e2f14c63344'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()





def upgrade_db_talent_city() -> None:
    op.create_table('articles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=250), nullable=False),
        sa.Column('article_body', sa.Text(), nullable=False),
        sa.Column('title_img', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('isPublish', sa.Boolean(), nullable=False),
        sa.Column('publish_at', sa.DateTime(), nullable=False),
        sa.Column('unpublish_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('mark_for_del', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade_db_talent_city() -> None:
    op.drop_table('articles')

