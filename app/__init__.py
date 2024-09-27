# app/__init__.py

from flask import Flask
from config import config
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config.from_object(config)

# Inicializar SQLAlche
db.init_app(app)

# Inicializa Flask-Mail
mail = Mail(app)
    
# Importar controladores y modelos
from app import controlMotos
from app import controlUser
from app import comentarios
from app import historial