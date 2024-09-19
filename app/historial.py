from flask import render_template, request, session
from app import app
from app.models import Motos, Usuarios, db
import json
import os


def leer_historial(user_id):
    filepath = f'historial_{user_id}.json'
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # Retorna una lista vacía si hay un error en la decodificación o al abrir el archivo
            return []
    return []  # Retorna una lista vacía si el archivo no existe
# Función para guardar el historial de búsqueda en un archivo
def guardar_historial(user_id, query):
    filepath = f'historial_{user_id}.json'
    historial_busqueda = leer_historial(user_id)
    historial_busqueda.append(query)
    # Limitar el tamaño del historial a 10 entradas
    if len(historial_busqueda) > 10:
        historial_busqueda.pop(0)
    with open(filepath, 'w') as f:
        json.dump(historial_busqueda, f)
        
#ruta para la barra de busqueda
@app.route('/buscar_motos')
def buscar_motos():
    query = request.args.get('query')
    user_id = session.get('user_id')  # Obtén el ID del usuario de la sesión
    
    if query and user_id:
        # Realizar la búsqueda en la base de datos
        motos = Motos.query.filter(
            (Motos.nombre.like(f'%{query}%')) | 
            (Motos.marca.like(f'%{query}%')) |
            (Motos.cilindrada.like(f'%{query}%'))  # Añadir filtro por cilindrada si es necesario
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
