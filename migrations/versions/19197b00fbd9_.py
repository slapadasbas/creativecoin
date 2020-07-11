"""empty message

Revision ID: 19197b00fbd9
Revises: d0ebfe797415
Create Date: 2020-06-29 23:16:34.958070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19197b00fbd9'
down_revision = 'd0ebfe797415'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'payment', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'transaction', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'wallet', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wallet', type_='foreignkey')
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.drop_constraint(None, 'payment', type_='foreignkey')
    # ### end Alembic commands ###
