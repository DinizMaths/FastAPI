"""create column for user phone number

Revision ID: b5a0cf25b00d
Revises: 7d6022f01541
Create Date: 2023-06-08 13:59:21.214658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5a0cf25b00d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
