"""empty message

Revision ID: 99fb00e6e5c0
Revises: 
Create Date: 2024-03-27 19:09:32.471106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99fb00e6e5c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onramp_orders',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('hash', sa.Text(), nullable=True),
    sa.Column('amount', sa.Text(), nullable=False),
    sa.Column('currency', sa.Text(), nullable=True),
    sa.Column('status', sa.Text(), server_default='new', nullable=True),
    sa.Column('extra', sa.JSON(), server_default=sa.text("'{}'::jsonb"), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash')
    )
    op.create_index(op.f('ix_onramp_orders_address'), 'onramp_orders', ['address'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_onramp_orders_address'), table_name='onramp_orders')
    op.drop_table('onramp_orders')
    # ### end Alembic commands ###