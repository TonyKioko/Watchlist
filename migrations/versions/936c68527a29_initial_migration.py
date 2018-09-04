"""Initial Migration

Revision ID: 936c68527a29
Revises: 9525773847d6
Create Date: 2018-09-03 16:30:19.084075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936c68527a29'
down_revision = '9525773847d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
