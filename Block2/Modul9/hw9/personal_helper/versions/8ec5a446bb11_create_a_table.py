"""Create a table

Revision ID: 8ec5a446bb11
Revises: 
Create Date: 2021-07-29 23:23:55.810264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec5a446bb11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
   op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(20)),
        sa.Column('birthday', sa.String(20)),
    )


def downgrade():
    op.drop_table('user')
