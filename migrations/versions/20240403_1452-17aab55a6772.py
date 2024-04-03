"""auto

Revision ID: 17aab55a6772
Revises: 935f35b1107e
Create Date: 2024-04-03 14:52:27.295836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17aab55a6772'
down_revision: Union[str, None] = '935f35b1107e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    status_project_enum = sa.Enum('ONGOING', 'UPCOMING', 'COMPLETED', name='statusproject')
    status_project_enum.create(op.get_bind())
    op.add_column('launchpad_project', sa.Column('status', sa.Enum('ONGOING', 'UPCOMING', 'COMPLETED', name='statusproject'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('launchpad_project', 'status')
    # ### end Alembic commands ###
