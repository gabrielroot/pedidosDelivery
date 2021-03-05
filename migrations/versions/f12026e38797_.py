"""empty message

Revision ID: f12026e38797
Revises: 
Create Date: 2021-03-04 20:25:26.966951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f12026e38797'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_deleted_at'), 'client', ['deleted_at'], unique=False)
    op.create_table('flavor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_flavor_deleted_at'), 'flavor', ['deleted_at'], unique=False)
    op.create_table('item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_deleted_at'), 'item', ['deleted_at'], unique=False)
    op.create_table('flavorItems',
    sa.Column('flavor_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['flavor_id'], ['flavor.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('flavor_id', 'item_id')
    )
    op.create_index(op.f('ix_flavorItems_deleted_at'), 'flavorItems', ['deleted_at'], unique=False)
    op.create_table('order',
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('flavor_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['flavor_id'], ['flavor.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'flavor_id', 'client_id')
    )
    op.create_index(op.f('ix_order_deleted_at'), 'order', ['deleted_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_deleted_at'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_flavorItems_deleted_at'), table_name='flavorItems')
    op.drop_table('flavorItems')
    op.drop_index(op.f('ix_item_deleted_at'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_flavor_deleted_at'), table_name='flavor')
    op.drop_table('flavor')
    op.drop_index(op.f('ix_client_deleted_at'), table_name='client')
    op.drop_table('client')
    # ### end Alembic commands ###