"""Moving tb_idata to redis

Revision ID: 2c2a6b0b68ca
Revises: ab1e63ac9749
Create Date: 2016-03-25 23:15:33.509219

"""

# revision identifiers, used by Alembic.
revision = '2c2a6b0b68ca'
down_revision = 'ab1e63ac9749'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_idata')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_idata',
    sa.Column('id', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('value', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    ### end Alembic commands ###
