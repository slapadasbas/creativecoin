"""empty message

Revision ID: a70b1a5e08e9
Revises: f195d64e3292
Create Date: 2020-06-24 20:28:42.719122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a70b1a5e08e9'
down_revision = 'f195d64e3292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('txn_id', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('item_name', sa.String(length=128), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('amount1', sa.DECIMAL(precision=20, scale=10), nullable=True),
    sa.Column('amount2', sa.DECIMAL(precision=20, scale=10), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('is_transferred', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(length=128), nullable=True),
    sa.Column('received_amount', sa.DECIMAL(precision=20, scale=10), nullable=True),
    sa.Column('recieved_confirmations', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('txn_id')
    )
    op.create_foreign_key(None, 'wallet', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wallet', type_='foreignkey')
    op.drop_table('transaction')
    # ### end Alembic commands ###
