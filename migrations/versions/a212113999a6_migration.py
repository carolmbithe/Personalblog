""" Migration

Revision ID: a212113999a6
Revises: 4bf8e1c50330
Create Date: 2018-10-22 21:28:34.361040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a212113999a6'
down_revision = '4bf8e1c50330'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###
