"""empty message

Revision ID: 59043f318c4f
Revises: d2373e016dc2
Create Date: 2020-05-13 10:47:06.776492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59043f318c4f'
down_revision = 'd2373e016dc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('subscribe', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'subscribe')
    # ### end Alembic commands ###
