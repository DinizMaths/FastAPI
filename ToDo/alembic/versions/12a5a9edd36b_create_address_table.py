"""Create address table

Revision ID: 12a5a9edd36b
Revises: b5a0cf25b00d
Create Date: 2023-06-08 16:21:40.865394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12a5a9edd36b'
down_revision = 'b5a0cf25b00d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id",          sa.Integer(), nullable=False, primary_key=True),
        sa.Column("address1",    sa.String(),  nullable=False),
        sa.Column("address2",    sa.String(),  nullable=True),
        sa.Column("city",        sa.String(),  nullable=False),
        sa.Column("state",       sa.String(),  nullable=False),
        sa.Column("country",     sa.String(),  nullable=False),
        sa.Column("postal_code", sa.String(),  nullable=False),
    )


def downgrade() -> None:
    op.drop_table("address")
