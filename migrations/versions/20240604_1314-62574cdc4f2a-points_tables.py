"""points tables

Revision ID: 62574cdc4f2a
Revises: 9e42c3f96a16
Create Date: 2024-06-04 13:14:50.518458

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = '62574cdc4f2a'
down_revision: Union[str, None] = '9e42c3f96a16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    operationtype = ENUM('ADD', 'ADD_REF', 'ADD_REF_BONUS', 'ADD_SYNC', 'ADD_REF_SYNC', 'ADD_EXTRA',
                         'ADD_MANUAL', 'ADD_IDO_POINTS', name='operationtype', create_type=False)
    operationreason = ENUM('ERR_COMPENSATION', 'BLASTBOX', 'OTHER_GIVEAWAY', name='operationreason', create_type=False)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
                    sa.Column('id', sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                         'sqlite'),
                              nullable=False),
                    sa.Column('address', sa.Text(), nullable=False),
                    sa.Column('referrer', sa.Text(), nullable=True),
                    sa.Column('points',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              server_default=sa.text('0::bigint'), nullable=True),
                    sa.Column('ref_points',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              server_default=sa.text('0::bigint'), nullable=True),
                    sa.Column('ref_percent', sa.Integer(), server_default=sa.text('20::int'), nullable=True),
                    sa.Column('ref_bonus_used', sa.Boolean(), server_default='false', nullable=False),
                    sa.Column('terms_accepted', sa.Boolean(), server_default='false', nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_profiles_address'), 'profiles', ['address'], unique=True)
    op.create_index(op.f('ix_profiles_referrer'), 'profiles', ['referrer'], unique=False)
    op.create_table('points_history',
                    sa.Column('id', sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                         'sqlite'),
                              nullable=False),
                    sa.Column('operation_type', operationtype, nullable=False),
                    sa.Column('operation_reason', operationreason, nullable=True),
                    sa.Column('points_before',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              server_default=sa.text('0::bigint'), nullable=False),
                    sa.Column('amount',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              server_default=sa.text('0::bigint'), nullable=False),
                    sa.Column('points_after',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              server_default=sa.text('0::bigint'), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('profile_id',
                              sa.BigInteger().with_variant(sa.BIGINT(), 'postgresql').with_variant(sa.INTEGER(),
                                                                                                   'sqlite'),
                              nullable=False),
                    sa.Column('project_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
                    sa.ForeignKeyConstraint(['project_id'], ['launchpad_project.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_constraint('extra_points_profile_id_fkey', 'extra_points', type_='foreignkey')
    op.create_foreign_key(None, 'extra_points', 'profiles', ['profile_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'extra_points', type_='foreignkey')
    op.create_foreign_key('extra_points_profile_id_fkey', 'extra_points', 'tmp_profiles', ['profile_id'], ['id'])
    op.drop_table('points_history')
    op.drop_index(op.f('ix_profiles_referrer'), table_name='profiles')
    op.drop_index(op.f('ix_profiles_address'), table_name='profiles')
    op.drop_table('profiles')
    # ### end Alembic commands ###