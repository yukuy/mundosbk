from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.models import Motos, Marca, Usuarios, db
import os
import json
import os

HISTORIAL_FILE = 'historial_busqueda.json'

def guardar_historial(historial):
    with open(HISTORIAL_FILE, 'w') as f:
        json.dump(historial, f)
        
def leer_historial():
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, 'r') as f:
            return json.load(f)
    return []

@app.route('/buscar_motos')
def buscar_motos():
    query = request.args.get('query')
    if query:
        # Realizar la búsqueda en la base de datos
        motos = Motos.query.join(Marca).filter(
            (Motos.nombre.like(f'%{query}%')) | 
            (Marca.nombre.like(f'%{query}%'))
        ).all()

        # Obtener el historial de búsqueda desde el archivo
        historial_busqueda = leer_historial()

        # Agregar la nueva búsqueda al historial si no está ya presente
        if query not in historial_busqueda:
            historial_busqueda.append(query)
            # Limitar el tamaño del historial a 10 entradas
            if len(historial_busqueda) > 10:
                historial_busqueda.pop(0)
            guardar_historial(historial_busqueda)

    else:
        motos = []

    return render_template('resultados.html', motos=motos, user_nombre=session['user_nombre'])


@app.route('/historial')
def historial():
    # Obtener el historial de búsqueda desde el archivo
    historial_busqueda = leer_historial()
    return render_template('historial.html', historial_busqueda=historial_busqueda)
