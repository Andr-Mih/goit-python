"""Create a table phone

Revision ID: 9fc3af590a17
Revises: 8ec5a446bb11
Create Date: 2021-07-29 23:27:41.835250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = '9fc3af590a17'
down_revision = '8ec5a446bb11'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'phone',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('phone', sa.String(20), nullable=False),
        sa.Column('user_id', sa.String(20), nullable=False),
    )


def downgrade():
    op.drop_table('phone')
