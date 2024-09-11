from flask import render_template, request, session
from app import app
from app.models import Motos, Marca, Usuarios, db
import json
import os

# Función para guardar el historial de búsqueda en un archivo
def guardar_historial(user_id, query):
    historial_file = f'historial_busqueda_{user_id}.json'
    
    if os.path.exists(historial_file):
        with open(historial_file, 'r') as f:
            historial_busqueda = json.load(f)
    else:
        historial_busqueda = []

    if query not in historial_busqueda:
        historial_busqueda.append(query)
        if len(historial_busqueda) > 10:
            historial_busqueda.pop(0)
        
        with open(historial_file, 'w') as f:
            json.dump(historial_busqueda, f)

# Función para leer el historial de búsqueda desde un archivo
def leer_historial(user_id):
    historial_file = f'historial_busqueda_{user_id}.json'
    
    if os.path.exists(historial_file):
        with open(historial_file, 'r') as f:
            return json.load(f)
    return []

@app.route('/buscar_motos')
def buscar_motos():
    query = request.args.get('query')
    user_id = session.get('user_id')  # Obtén el ID del usuario de la sesión
    
    if query and user_id:
        # Realizar la búsqueda en la base de datos
        motos = Motos.query.join(Marca).filter(
            (Motos.nombre.like(f'%{query}%')) | 
            (Marca.nombre.like(f'%{query}%'))
        ).all()

        # Obtener el historial de búsqueda desde el archivo específico del usuario
        historial_busqueda = leer_historial(user_id)

        # Agregar la nueva búsqueda al historial si no está ya presente
        if query not in historial_busqueda:
            historial_busqueda.append(query)
            # Limitar el tamaño del historial a 10 entradas
            if len(historial_busqueda) > 10:
                historial_busqueda.pop(0)
            guardar_historial(user_id, query)  # Asegúrate de pasar el user_id también al guardar

    else:
        motos = []

    return render_template('resultados.html', motos=motos, user_nombre=session.get('user_nombre'))

@app.route('/historial')
def historial():
    user_id = session.get('user_id')  # Obtén el ID del usuario de la sesión
    historial_busqueda = leer_historial(user_id) if user_id else []
    return render_template('historial.html', historial_busqueda=historial_busqueda)
