#modelos o tablas de la bd
from app import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45))
    correo = db.Column(db.String(200))
    clave = db.Column(db.String(200))
    telefono = db.Column(db.BigInteger)
    
    motos = db.relationship('Motos', backref=db.backref('usuarios', lazy=True))

class Motos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    foto = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)  
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False) 
    
    marca = db.relationship('Marca', backref='motos')
    
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45))
    modelo = db.Column(db.String(45))
    serie = db.Column(db.String(45))

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.Text, nullable=False)
    idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    idMotos = db.Column(db.Integer, db.ForeignKey('motos.id'), nullable=False)

    usuarios = db.relationship('Usuarios', backref=db.backref('comentario', lazy=True))
    motos = db.relationship('Motos', backref=db.backref('comentario', lazy=True))


