from flask import render_template, request, redirect, url_for, flash, session
from flask_mail import Message
from app import app
from app.models import Usuarios, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
import cloudinary.uploader
import os


@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    print("Función recuperar() llamada")  # Añade esta línea
    if request.method == 'POST':
        correo = request.form.get('correo')
        usuario = Usuarios.query.filter_by(correo=correo).first()

        if usuario:
            print("Usuario encontrado:", usuario.nombre)  # Imprime el nombre del usuario
            # Generar el token
            token = generar_token(usuario)
            print("Token generado:", token)
            # Enviar el correo de recuperación
            enviar_email_recuperacion(usuario, token)
            flash('Se ha enviado un correo para restablecer tu contraseña.', 'success')
        else:
            flash('El correo no está registrado en nuestro sistema.', 'warning')
        
        return redirect(url_for('login'))
    
    return render_template('recuperar_contraseña.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    usuario = verificar_token(token)
    if not usuario:
        flash('El enlace de restablecimiento de contraseña no es válido o ha expirado.', 'warning')
        return redirect(url_for('recuperar'))

    if request.method == 'POST':
        nueva_clave = request.form['nueva_clave']
        # Hashear la nueva contraseña
        nueva_clave_hash = generate_password_hash(nueva_clave)
        usuario.clave = nueva_clave_hash
        db.session.commit()
        flash('Tu contraseña ha sido actualizada.', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html')

    # Generar token
def generar_token(usuario):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'user_id': usuario.id})

# Verificar token
def verificar_token(token, expiration=1800):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, max_age=expiration)['user_id']
    except:
        return None
    return Usuarios.query.get(user_id)

def enviar_email_recuperacion(usuario, token):
    from app import mail
    # Construir la URL para la recuperación de la contraseña
    reset_url = url_for('reset_password', token=token, _external=True)

    print(f'URL de restablecimiento de contraseña: {reset_url}')
    # Crear el mensaje de correo
    msg = Message('Recupera tu contraseña',
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[usuario.correo])
    
    # Definir el cuerpo del mensaje
    msg.body = f'''Hola {usuario.nombre},

Para restablecer tu contraseña, haz clic en el siguiente enlace:

{reset_url}

Si no solicitaste este cambio, simplemente ignora este correo.
'''
    try:
        mail.send(msg)
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

#ruta para registrar cada usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        telefono = request.form['telefono']
        foto = None
        
         # Agregar foto
        if 'foto' in request.files:
            foto_file = request.files['foto']
            if foto_file.filename != '':
                # Subir la imagen a Cloudinary
                upload_result = cloudinary.uploader.upload(foto_file)
                # Guardar la URL de la imagen subida
                foto = upload_result['secure_url']
            else:
                # Si no se selecciona ninguna imagen, usa la imagen predeterminada
                foto = 'static/uploads/perfil.jpg'
        else:
            foto = 'static/uploads/perfil.jpg'
                
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
   
    return render_template('perfil.html', usuario=usuario, datetime=datetime)

# Ruta para editar perfil
@app.route('/editar_perfil/<int:user_id>', methods=['GET', 'POST'])
def editar_perfil(user_id):
    usuario = Usuarios.query.get(user_id)
    
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']
        usuario.telefono = request.form['telefono']
        foto = None
        
        nueva_clave = request.form['clave']
        if nueva_clave:
            usuario.clave = generate_password_hash(nueva_clave)

        # Manejar la carga de la foto
        if 'foto' in request.files:
            foto_file = request.files['foto']
            if foto_file.filename != '':                
                # Subir la nueva imagen a Cloudinary
                upload_result = cloudinary.uploader.upload(foto_file)
                # Guardar la nueva URL de la imagen en la base de datos
                foto = upload_result['secure_url']
                usuario.foto = foto  # Actualizar el campo foto en la base de datos

        # Guardar cambios en la base de datos
        db.session.commit()
        flash('Datos actualizados correctamente.', 'success')
        
        # Redirigir al perfil del usuario después de actualizar
        return redirect(url_for('perfil_usuario', user_id=user_id))  # Ajusta según tu ruta del perfil

    return render_template('editar_perfil.html', usuario=usuario)
        