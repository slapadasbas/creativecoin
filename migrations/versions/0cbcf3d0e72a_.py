"""empty message

Revision ID: 0cbcf3d0e72a
Revises: a08638248a8e
Create Date: 2020-05-24 04:37:13.939970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cbcf3d0e72a'
down_revision = 'a08638248a8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('emailverified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'emailverified')
    # ### end Alembic commands ###
