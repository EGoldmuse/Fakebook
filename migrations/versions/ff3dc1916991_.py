"""empty message

Revision ID: ff3dc1916991
Revises: 78ace169776d
Create Date: 2021-07-13 11:46:48.022765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff3dc1916991'
down_revision = '78ace169776d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product', sa.String(), nullable=False))
    op.drop_column('cart', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('cart', 'product')
    # ### end Alembic commands ###
