"""empty message

Revision ID: e8f29043f084
Revises: 305f68cc8ed2
Create Date: 2021-02-21 15:49:58.066656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8f29043f084'
down_revision = '305f68cc8ed2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('items_name_key', 'items', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('items_name_key', 'items', ['name'])
    # ### end Alembic commands ###