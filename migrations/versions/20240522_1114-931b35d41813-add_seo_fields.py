"""Add seo fields

Revision ID: 931b35d41813
Revises: e1ca83d34ec1
Create Date: 2024-05-22 11:14:48.919895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '931b35d41813'
down_revision: Union[str, None] = 'e1ca83d34ec1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('launchpad_project', sa.Column('seo_title', sa.Text(), nullable=True))
    op.add_column('launchpad_project', sa.Column('seo_description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('launchpad_project', 'seo_description')
    op.drop_column('launchpad_project', 'seo_title')
    # ### end Alembic commands ###
