from flask import render_template, redirect, url_for, request, session, flash
from app import app, db
from app.models import Comentarios, Motos, Usuarios

#agregar comentarios
@app.route('/moto/<int:moto_id>', methods=['GET', 'POST'])
def ver_moto(moto_id):
    moto = Motos.query.get_or_404(moto_id)
    if request.method == 'POST':
        if 'user_id' not in session:
            flash('Debes iniciar sesión para comentar.', 'warning')
            return redirect(url_for('login'))
        
        comentario_texto = request.form.get('comentario')
        if comentario_texto:
            nuevo_comentario = Comentarios(
                comentario=comentario_texto,
                idUsuarios=session['user_id'],
                idmotos=moto.id
            )
            db.session.add(nuevo_comentario)
            try:
                db.session.commit()
                flash('Comentario agregado exitosamente.', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Error al agregar comentario: {e}', 'danger')
                print(f'Error al agregar comentario: {e}')
            return redirect(url_for('ver_moto', moto_id=moto.id))
        else:
            flash('El comentario no puede estar vacío.', 'danger')

    comentarios = Comentarios.query.filter_by(idmotos=moto.id).all()
    return render_template('moto_comentarios.html', moto=moto, comentarios=comentarios)
