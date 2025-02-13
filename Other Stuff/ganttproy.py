import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pandas.tseries.offsets import BDay

# Definir las tareas del proyecto con sus duraciones
tasks = {
    'Task': ['WP1 – Gestión del proyecto', 'WP2 – Análisis y levantamiento', 
             'WP3 – Diseño de nueva plataforma', 'WP4 – Desarrollo módulos', 
             'WP5 – Pruebas y validación', 'WP6 – Implementación'],
    'Duration': [20, 15, 25, 69, 10, 10],  # Duraciones en días hábiles
    'Dependency': [None, 'WP1 – Gestión del proyecto', 'WP2 – Análisis y levantamiento', 
                   'WP3 – Diseño de nueva plataforma', 'WP4 – Desarrollo módulos', 
                   'WP5 – Pruebas y validación']  # Dependencias
}

# Crear DataFrame
df = pd.DataFrame(tasks)

# Asignar fechas de inicio y fin
start_date = pd.to_datetime('2024-01-01')  # Fecha de inicio del proyecto
df['Start'] = [start_date] + [None] * (len(df) - 1)  # Inicio del WP1

# Calcular fechas de inicio y fin considerando días hábiles
for i in range(1, len(df)):
    prev_task = df.loc[i - 1]
    df.loc[i, 'Start'] = prev_task['Start'] + BDay(prev_task['Duration'])

df['Finish'] = df['Start'] + df['Duration'].apply(lambda d: BDay(d))

# Convertir explícitamente a formato datetime si no lo es ya
df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
df['Finish'] = pd.to_datetime(df['Finish'], errors='coerce')

# Verificar si las columnas están correctamente convertidas
print(df[['Start', 'Finish']].dtypes)

# Si la duración total del proyecto excede los 5 meses hábiles (aprox 105 días)
max_duration = 105  # Aproximadamente 5 meses hábiles
total_duration = (df['Finish'].max() - df['Start'].min()).days

# Ajustar las duraciones si el proyecto excede el máximo de 5 meses
if total_duration > max_duration:
    factor = max_duration / total_duration
    df['Duration'] = df['Duration'] * factor
    df['Finish'] = df['Start'] + df['Duration'].apply(lambda d: BDay(int(d)))

# Asegurar que las columnas estén convertidas a fecha antes de acceder con .dt
df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
df['Finish'] = pd.to_datetime(df['Finish'], errors='coerce')

# Convertir a formato necesario para Matplotlib (solo la fecha sin horas)
df['Start'] = df['Start'].dt.date
df['Finish'] = df['Finish'].dt.date

# Crear el diagrama de Gantt
fig, ax = plt.subplots(figsize=(10, 6))

# Invertir el orden para que aparezca de WP1 a WP6 (ascendente)
df = df.iloc[::-1]

# Iterar sobre las tareas para añadir las barras del diagrama de Gantt
for i, task in enumerate(df.itertuples()):
    start = task.Start
    end = task.Finish
    ax.barh(task.Task, (end - start).days, left=start, color='skyblue')

# Configuración de formato de fechas y ejes
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
ax.set_xlabel('Fecha')
ax.set_ylabel('Fases del Proyecto')
plt.title('Diagrama de Gantt - Proyecto de Actualización')

plt.tight_layout()
plt.show()
