import os
from app import app, db

# Crear tablas en la base de datos
with app.app_context():
    try:
        db.create_all()  # Intenta crear todas las tablas
        print("Tablas creadas con éxito.")
    except Exception as e:
        print(f"Error al crear tablas: {e}")

if __name__ == "__main__":
    app.run(debug=True)
