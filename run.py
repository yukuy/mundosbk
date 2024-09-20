import os
from app import app, db

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()
    print("Tablas creadas con éxito.")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

