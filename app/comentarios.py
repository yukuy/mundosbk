from flask import render_template, redirect, url_for, request, flash, session
from app import app
from datetime import datetime
from app.models import Motos, Comentarios, Usuarios, db

# Ruta para los comentarios
@app.route('/add_comentario/<int:moto_id>', methods=['POST'])
def add_comentario(moto_id):
    # Verificar si el usuario está autenticado
    if 'user_id' not in session:
        flash('Debes iniciar sesión para comentar.', 'warning')
        return redirect(url_for('login'))

    comentario = request.form.get('comentario')
    if not comentario:
        flash('El comentario no puede estar vacío.', 'error')
        return redirect(url_for('info_motos', moto_id=moto_id))

    # Obtener el ID del usuario desde la sesión
    user_id = session['user_id']

    # Crear y guardar el nuevo comentario
    nuevo_comentario = Comentarios(comentario=comentario, idUsuarios=user_id, idMotos=moto_id)
    db.session.add(nuevo_comentario)
    db.session.commit()

    flash('Comentario agregado exitosamente!', 'success')
    return redirect(url_for('ver_comentarios', moto_id=moto_id))

#ruta para ver y poder agregar nuevos comentarios y ver las caracteristicas de cada moto
@app.route('/ver_comentarios/<int:moto_id>', methods=['GET'])
def ver_comentarios(moto_id):
    if 'user_id' not in session:
        flash('Debes iniciar sesión para ver y agregar comentarios.', 'warning')
        return redirect(url_for('login')) 

    # Obtener la moto
    moto = Motos.query.get_or_404(moto_id)
    
    # Obtener los comentarios asociados a la moto
    comentarios = Comentarios.query.filter_by(idMotos=moto_id).all()
    
    # Obtener el usuario que registró la moto usando la relación definida en el modelo
    vendedor = Usuarios.query.get_or_404(moto.usuarios_id)

    # Obtener la URL del video de la moto
    video_url = moto.video_url

    # Inicializar la URL del video o Short
    embed_url = None

    if video_url:
        # Verificar si es un video normal o un Short
        if "youtube.com/watch" in video_url:
            # Video normal de YouTube
            video_id = video_url.split('v=')[-1]  # Extraer solo el ID del video
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1"
        elif "youtube.com/shorts" in video_url:
            # Video Short de YouTube
            video_id = video_url.split('shorts/')[-1]  # Extraer solo el ID del Short
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1"

    return render_template('info_motos.html', moto=moto, comentarios=comentarios, 
                           vendedor=vendedor, video_url=embed_url, datetime=datetime)