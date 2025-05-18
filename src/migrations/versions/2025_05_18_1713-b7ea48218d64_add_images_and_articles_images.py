"""add images and articles_images

Revision ID: b7ea48218d64
Revises: a4ed88754956
Create Date: 2025-05-18 17:13:54.506607

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7ea48218d64"
down_revision: Union[str, None] = "a4ed88754956"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_db_talent_city() -> None:
    op.create_table(
        "images",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=250), nullable=False),
        sa.Column("path", sa.String(length=250), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False
        ),
        sa.Column(
            "isActive", sa.Boolean(), server_default=sa.text("FALSE"), nullable=False
        ),
        sa.Column(
            "mark_for_del",
            sa.Boolean(),
            server_default=sa.text("FALSE"),
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("disactive_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "articles_images",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.Column("image_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("NOW()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["articles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["image_id"],
            ["images.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_index("favourites_article_user_id_idx", table_name="favourites")


def downgrade_db_talent_city() -> None:
    op.create_index(
        "favourites_article_user_id_idx",
        "favourites",
        ["article_id", "user_id"],
        unique=True,
    )
    op.drop_table("articles_images")
    op.drop_table("images")
