# inicializador de la app 
# En app/__init__.py
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

 # Importa routes aquí para evitar el ciclo

from app import controlMotos
from app import controlUser
from app import comentarios
from app import historial