"""Create donuts table

Revision ID: c08090a33bee
Revises: 
Create Date: 2024-06-04 01:19:34.934626

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c08090a33bee"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "donuts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("donut", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_donuts")),
        sa.UniqueConstraint("donut", name=op.f("uq_donuts_donut")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("donuts")
    # ### end Alembic commands ###