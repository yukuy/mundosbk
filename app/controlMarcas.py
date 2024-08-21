from flask import render_template, request,current_app, redirect, url_for, flash, session
from app import app
from app.models import Marca, db

#ruta para listar las marcas
@app.route('/marcas')
def marcas():
    marca = Marca.query.all()
    return render_template('marcas.html', marca=marca)

#ruta para agregar
app.route('/add_marca')
def add_marca():
    return render_template('add_marcas.html')

#ruta para modificar
@app.route('/edit_marca')
def edit_marca():
    return render_template('edit_marca.html')

#ruta para eliminar
@app.route('/delete_maraca')
def delete_marca():
    return redirect(url_for('marcas'))