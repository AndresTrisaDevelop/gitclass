import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Datos del tablero Kanban según el nuevo flujo propuesto
columns = ['To Do', 'In Progress', 'Testing', 'Done']
tasks = [
    # To Do (HU-5 a HU-10)
    ["HU-5: Generación de informes", "HU-6: Seguimiento empleados", "HU-7: Seguros sociales", 
     "HU-8: Protección de datos", "HU-9: Notificaciones automáticas", "HU-10: Portal de empleados"],  

    # In Progress (HU-1, HU-2)
    ["HU-1: Alta de empleados", "HU-2: Gestión de incidencias"],  

    # Testing (HU-2, HU-4)
    ["HU-2: Gestión de incidencias", "HU-4: Permisos para nómina"],

    # Done (Back-End y DevOps)
    ["Back-End: Diseño de base de datos", "Back-End: CRUD operations", "Back-End: Crear APIs", 
     "DevOps: Crear microservicios", "DevOps: Desplegar APIs"]
]

# Configuración del tablero
fig, ax = plt.subplots(figsize=(14, 8))
max_tasks = max(len(t) for t in tasks)  # Máxima cantidad de tareas en una columna

# Dibujar columnas del tablero
for i, column in enumerate(columns):
    # Fondo de columna
    ax.add_patch(Rectangle((i, 0), 1, max_tasks, color="#ecf0f1", edgecolor="black", alpha=0.8))
    # Etiqueta de columna
    ax.text(i + 0.5, max_tasks - 0.5, column, ha='center', va='top', fontsize=12, fontweight='bold')

# Agregar tareas dentro de cada columna
for col_index, task_list in enumerate(tasks):
    for row_index, task in enumerate(task_list):
        x_pos = col_index + 0.1  # Desplazamiento horizontal
        y_pos = max_tasks - row_index - 1  # Desplazamiento vertical
        # Rectángulo para la tarea
        ax.add_patch(Rectangle((x_pos, y_pos - 0.8), 0.8, 0.8, color="#3498db", edgecolor="black", alpha=0.9))
        # Texto dentro del rectángulo
        ax.text(x_pos + 0.4, y_pos - 0.4, task, ha='center', va='center', fontsize=8, color="white", wrap=True)

# Ajustes del gráfico
ax.set_xlim(0, len(columns))  # Asegurar que el eje x se ajuste al número de columnas
ax.set_ylim(0, max_tasks)  # Asegurar que el eje y se ajuste al número máximo de tareas
ax.axis('off')  # Ocultar ejes
ax.set_title('Tablero Kanban del Proyecto', fontsize=16, fontweight='bold', pad=20)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
