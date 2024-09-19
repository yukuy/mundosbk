# app/models.py
from datetime import datetime
from app import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45))
    correo = db.Column(db.String(200))
    clave = db.Column(db.String(200))
    telefono = db.Column(db.BigInteger)
    foto = db.Column(db.String(200))
    numero_ventas = db.Column(db.Integer, default=0)  # Número de ventas realizadas
    calificacion_promedio = db.Column(db.Float, default=0.0)  # Campo para la calificación promedio
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)  # Tiempo en la plataforma
    
    motos = db.relationship('Motos', backref=db.backref('usuarios', lazy=True))
    
class Valoraciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    comprador_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)  # Valor entre 1 y 5 estrellas
    
    vendedor = db.relationship('Usuarios', foreign_keys=[vendedor_id], backref='valoraciones')
    comprador = db.relationship('Usuarios', foreign_keys=[comprador_id])

class Motos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    foto = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    descripcion = db.Column(db.Text)

    # Nuevos campos agregados
    marca = db.Column(db.String(45))        # Campo para la marca de la moto
    cilindrada = db.Column(db.Integer)      # Campo para la cilindrada de la moto

    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.Text, nullable=False)
    idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    idMotos = db.Column(db.Integer, db.ForeignKey('motos.id'), nullable=False)

    usuarios = db.relationship('Usuarios', backref=db.backref('comentario', lazy=True))
    motos = db.relationship('Motos', backref=db.backref('comentario', lazy=True))
