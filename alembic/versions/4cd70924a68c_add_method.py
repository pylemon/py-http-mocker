"""add method

Revision ID: 4cd70924a68c
Revises: 2f1fe8629953
Create Date: 2016-10-14 14:46:44.241581

"""

# revision identifiers, used by Alembic.
revision = '4cd70924a68c'
down_revision = '2f1fe8629953'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('response', sa.Column('method', sa.Enum('DELETE', 'GET', 'HEAD', 'POST', 'PUT', name='methods'), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('response', 'method')
    ### end Alembic commands ###