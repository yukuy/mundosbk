from app import app, db

with app.app_context():
    db.create_all()
    print("Tablas creadas con éxito.")

if __name__ == "__main__":
    app.run(debug=True)
