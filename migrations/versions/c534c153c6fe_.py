"""empty message

Revision ID: c534c153c6fe
Revises: a6073550481b
Create Date: 2020-05-11 01:04:59.237143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c534c153c6fe'
down_revision = 'a6073550481b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reactions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reactions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('liked', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='reactions_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='reactions_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reactions_pkey')
    )
    op.drop_table('comments')
    # ### end Alembic commands ###
