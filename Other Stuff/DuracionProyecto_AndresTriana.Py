import pandas as pd
import networkx as nx

# Datos de actividades
actividades = {
    'Inicio': {'duracion': 0, 'predecesores': []},
    'A': {'duracion': 7, 'predecesores': ['Inicio']},
    'B': {'duracion': 5, 'predecesores': ['A']},
    'C': {'duracion': 8, 'predecesores': ['A']},
    'D': {'duracion': 3, 'predecesores': ['B', 'C']},
    'E': {'duracion': 12, 'predecesores': ['D']},
    'F': {'duracion': 15, 'predecesores': ['E']},
    'G': {'duracion': 12, 'predecesores': ['E']},
    'H': {'duracion': 6, 'predecesores': ['F', 'G']},
    'I': {'duracion': 10, 'predecesores': ['H']},
    'J': {'duracion': 4, 'predecesores': ['I']},
    'K': {'duracion': 7, 'predecesores': ['J']},
    'Final': {'duracion': 0, 'predecesores': ['K']}
}

# Crear grafo
G = nx.DiGraph()

# Agregar nodos con duraciones
for actividad, datos in actividades.items():
    G.add_node(actividad, duracion=datos['duracion'])

# Agregar aristas según predecesores
for actividad, datos in actividades.items():
    for predecesor in datos['predecesores']:
        G.add_edge(predecesor, actividad)

# Calcular la ruta crítica
ruta_critica = nx.algorithms.dag.dag_longest_path(G, weight='duracion')

# Calcular la duración mínima del proyecto (suma de las duraciones en la ruta crítica)
duracion_minima = sum(actividades[actividad]['duracion'] for actividad in ruta_critica)

# Crear tabla de actividades y duraciones
tabla_duraciones = pd.DataFrame({
    'Actividad': [actividad for actividad in actividades],
    'Duración': [actividades[actividad]['duracion'] for actividad in actividades],
    'Es parte de la ruta crítica': ['Sí' if actividad in ruta_critica else 'No' for actividad in actividades]
})

# Mostrar la tabla
print(tabla_duraciones)
print(f"\nDuración mínima del proyecto (Ruta Crítica): {duracion_minima} días")
