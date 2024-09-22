# config.py
import secrets
from datetime import timedelta

class config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/railway'
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/railway'  # Conexión a MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar rastreo de modificaciones para mejorar rendimiento
    SECRET_KEY = secrets.token_hex(16)   # Clave secreta para la app
    
    SECRET_KEY = 'tu_clave_secreta_fija_aqui'  # Reemplázalo con una clave secreta fija
    PERMANENT_SESSION_LIFETIME = timedelta(days=7) # Duración de la sesión permanente (por ejemplo, 7 días)
