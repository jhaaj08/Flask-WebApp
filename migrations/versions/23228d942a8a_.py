"""empty message

Revision ID: 23228d942a8a
Revises: 799c79b41ec0
Create Date: 2023-09-23 23:44:34.435394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23228d942a8a'
down_revision = '799c79b41ec0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('sales_register',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('product_name', sa.String(length=100), nullable=False),
    # sa.Column('quantity_purchased', sa.Integer(), nullable=False),
    # sa.PrimaryKeyConstraint('id')
    # )
    # with op.batch_alter_table('product', schema=None) as batch_op:
    #     batch_op.create_unique_constraint('unique_product_name', ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('product', schema=None) as batch_op:
    #     batch_op.drop_constraint(None, type_='unique')
    #
    # op.drop_table('sales_register')
    # # ### end Alembic commands ###