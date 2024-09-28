import secrets
from datetime import timedelta


class config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://railway_wb2i_user:KrxKouW9tjNy1M83JKQROy8CdwLU4q19@dpg-crnn4gu8ii6s73etpe70-a.oregon-postgres.render.com/railway_wb2i'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)  # Genera una clave secreta aleatoria
    SECRET_KEY = 'tu_clave_secreta_fija_aqui'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    #configuracion del sistema para recuperar contraseña:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mundosbkoficial@gmail.com'
    MAIL_PASSWORD = 'krhh vsi h emey nulx'
    MAIL_DEFAULT_SENDER = 'mundosbkoficial@gmail.com'
