import secrets
from datetime import timedelta
import cloudinary
import os

class config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres.unobzvvcnumgglngjjpb:66aCkyJsQgCoEISG@aws-1-us-east-1.pooler.supabase.com:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")  # Genera una clave secreta aleatoria
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # Configuración del sistema para recuperar contraseña
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mundosbkoficial@gmail.com'
    MAIL_PASSWORD = 'krhh vsi h emey nulx'
    MAIL_DEFAULT_SENDER = 'mundosbkoficial@gmail.com'
    
    # Configuración de Cloudinary
    CLOUD_NAME = 'dcg9njwmk'
    API_KEY = '173894522551611'
    API_SECRET = 'QpgpM1sFU6F7KDFFa47Jn-jvx5E'  # Asegúrate de que esta sea tu API Secret real

    @staticmethod
    def init_cloudinary():
        cloudinary.config(
            cloud_name=config.CLOUD_NAME,
            api_key=config.API_KEY,
            api_secret=config.API_SECRET
        )
