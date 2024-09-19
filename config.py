# config.py
import secrets

class config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/mundosbk'  # Conexión a MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar rastreo de modificaciones para mejorar rendimiento
    SECRET_KEY = secrets.token_hex(16)   # Clave secreta para la app
