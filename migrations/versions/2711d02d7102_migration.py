""" Migration

Revision ID: 2711d02d7102
Revises: c26e2ef842db
Create Date: 2018-10-18 20:58:32.852921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2711d02d7102'
down_revision = 'c26e2ef842db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('blog', sa.String(length=1000), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###
