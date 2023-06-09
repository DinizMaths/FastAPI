"""add apt number

Revision ID: 1a771809dae1
Revises: 0a29460163a1
Create Date: 2023-06-08 21:07:41.687025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a771809dae1'
down_revision = '0a29460163a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
