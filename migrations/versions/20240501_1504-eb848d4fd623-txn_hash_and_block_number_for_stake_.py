"""txn_hash and block number for stake history

Revision ID: eb848d4fd623
Revises: fc9df0701eb9
Create Date: 2024-05-01 15:04:58.553392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb848d4fd623'
down_revision: Union[str, None] = 'fc9df0701eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stake_history', sa.Column('txn_hash', sa.String(), nullable=True))
    op.add_column('stake_history', sa.Column('block_number', sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(), 'sqlite'), nullable=True))
    op.create_unique_constraint("ux_stake_history_txn_hash", 'stake_history', ['txn_hash'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("ux_stake_history_txn_hash", 'stake_history', type_='unique')
    op.drop_column('stake_history', 'block_number')
    op.drop_column('stake_history', 'txn_hash')
    # ### end Alembic commands ###