from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.models import Usuarios, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os

#ruta para registrar cada usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        telefono = request.form['telefono']
        foto = None
        
        #agregar foto
        if 'foto' in request.files:
            foto_file = request.files['foto']
            if foto_file.filename != '':
                foto = foto_file.filename
                foto_path = os.path.join('app/static/uploads', foto)
                foto_file.save(foto_path)
                
        # Hash de la contraseña utilizando un método específico
        clave_hash = generate_password_hash(clave, method='pbkdf2:sha256', salt_length=8)

        try:
            nuevo_usuarios = Usuarios(nombre=nombre, correo=correo, clave=clave_hash, 
                                      telefono=telefono, foto=foto)
            db.session.add(nuevo_usuarios)
            db.session.commit()
            flash('Registro exitoso!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error al registrar el usuario: {e}', 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')

#ruta para el login
@app.route('/', methods=['GET', 'POST'])
def login():
    
    #si el algun usuario ya ainicio secion redirigirlo al ala pagina prinsipal   
    if 'user_id' in session:
        return redirect(url_for("base")) 
      
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']
        
        # Buscar el usuario por correo
        usuario = Usuarios.query.filter_by(correo=correo).first()
        if usuario and check_password_hash(usuario.clave, clave):
            session['user_id'] = usuario.id
            session['user_nombre'] = usuario.nombre
            session.permanent = True  # Marca la sesión como permanente
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('base'))
        else:
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

#ruta para el cierre de session
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_nombre', None)
    flash('Has cerrado sesión correctamente.', 'success')
    return redirect(url_for('login'))

#ruta para abrir la pagina principal
@app.route('/base')
def base():
    if 'user_id' not in session:
        flash('Por favor, inicia sesión primero.', 'warning')
        return redirect(url_for('login'))

    # Obtener el historial de búsqueda desde la sesión o inicializarlo como una lista vacía
    historial_busqueda = session.get('historial_busqueda', [])

    # Obtener la información del usuario desde la base de datos
    usuario = Usuarios.query.get(session['user_id'])
    
    # Pasar el historial de búsqueda, el nombre de usuario y el objeto usuario
    return render_template('base.html', user_nombre=session['user_nombre'], historial_busqueda=historial_busqueda, usuario=usuario)


#logo del perfil
@app.route('/perfil/<int:user_id>')
def perfil_usuario(user_id):
    usuario = Usuarios.query.get(user_id)
    if usuario:
        return render_template('perfil.html', usuario=usuario)
    else:
        return "usuario no encontrado", 404