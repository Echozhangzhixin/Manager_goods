"""empty message

Revision ID: ce3580f524df
Revises: 
Create Date: 2019-04-24 20:00:59.294143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce3580f524df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('information', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prostock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('warning_stock', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=32), nullable=False),
    sa.Column('user_password', sa.String(length=32), nullable=False),
    sa.Column('job_number', sa.String(length=32), nullable=False),
    sa.Column('mobile_phone', sa.String(length=12), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.String(length=16), nullable=False),
    sa.Column('product_name', sa.String(length=32), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('cost_price', sa.Float(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('unit', sa.String(length=10), nullable=False),
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('iid', sa.Integer(), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['category.id'], ),
    sa.ForeignKeyConstraint(['iid'], ['proinfo.id'], ),
    sa.ForeignKeyConstraint(['sid'], ['prostock.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_id')
    )
    op.create_table('out_in',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['products.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['userinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('out_in')
    op.drop_table('products')
    op.drop_table('userinfo')
    op.drop_table('prostock')
    op.drop_table('proinfo')
    op.drop_table('category')
    # ### end Alembic commands ###