"""1.2.3

Revision ID: 313bf0f53299
Revises: 13a58bd5311f
Create Date: 2023-07-23 00:10:11.089367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a4f6f4e7e4'
down_revision = '313bf0f53299'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # 1.2.1
    try:
        with op.batch_alter_table("SITE_BRUSH_TASK") as batch_op:
            batch_op.add_column(sa.Column('BRUSHTASK_FREE_LIMIT_SPEED', sa.Text, nullable=True))
    except Exception as e:
        pass

    try:
        with op.batch_alter_table("SITE_BRUSH_TORRENTS") as batch_op:
            batch_op.add_column(sa.Column('FREE_DEADLINE', sa.Text, nullable=True))
    except Exception as e:
        pass
    # ### end Alembic commands ###

def downgrade() -> None:
    pass
