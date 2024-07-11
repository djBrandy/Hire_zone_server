"""Added user table

Revision ID: 56333075642d
Revises: 67b185ef04e7
Create Date: 2024-07-11 22:10:58.476253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56333075642d'
down_revision = '67b185ef04e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.Column('job_seeker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employers_table.id'], name=op.f('fk_users_employer_id_employers_table')),
    sa.ForeignKeyConstraint(['job_seeker_id'], ['job_seekers_table.id'], name=op.f('fk_users_job_seeker_id_job_seekers_table')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
