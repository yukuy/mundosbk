import secrets
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://railway_wb2i_user:KrxKouW9tjNy1M83JKQROy8CdwLU4q19@dpg-crnn4gu8ii6s73etpe70-a.oregon-postgres.render.com/railway_wb2i'  # URL de PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar rastreo de modificaciones para mejorar rendimiento
    SECRET_KEY = secrets.token_hex(16)  # Clave secreta para la app
    SECRET_KEY = 'tu_clave_secreta_fija_aqui'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # Duración de la sesión permanente (por ejemplo, 7 días)
