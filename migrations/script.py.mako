"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    with op.batch_alter_table('comentarios', schema=None) as batch_op:
        # Si necesitas modificar la clave foránea, hazlo aquí.
        # Por ejemplo, si estás ajustando la clave foránea:
        batch_op.drop_constraint('fk_usuarios_has_motos_motos1_idx', type_='foreignkey')
        batch_op.create_foreign_key('fk_usuarios_has_motos_motos1', 'motos', ['idMotos'], ['id'])
        batch_op.create_foreign_key('fk_usuarios_has_motos_usuarios1', 'usuarios', ['idUsuarios'], ['id'])


def downgrade():
    with op.batch_alter_table('comentarios', schema=None) as batch_op:
        # Revertir los cambios realizados en la función upgrade
        batch_op.drop_constraint('fk_usuarios_has_motos_motos1', type_='foreignkey')
        # Aquí puedes volver a agregar el índice si es necesario
        batch_op.create_index('fk_usuarios_has_motos_motos1_idx', ['idMotos'])
