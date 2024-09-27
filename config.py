# config.py
import secrets

class config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/mundosbk'  # Conexión a MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar rastreo de modificaciones para mejorar rendimiento
    SECRET_KEY = secrets.token_hex(16)   # Clave secreta para la app
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mundosbkoficial@gmail.com'
    MAIL_PASSWORD = 'krhh vsi h emey nulx'
    MAIL_DEFAULT_SENDER = 'mundosbkoficial@gmail.com'
