"""empty message

Revision ID: 9c36db55ec53
Revises: None
Create Date: 2016-10-17 09:49:20.372263

"""

# revision identifiers, used by Alembic.
revision = '9c36db55ec53'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.Date(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('page', sa.String(length=12), nullable=False),
    sa.Column('subject', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('image_ext', sa.String(length=240), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('parking', sa.Integer(), nullable=True),
    sa.Column('sqft', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_joined', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    ### end Alembic commands ###