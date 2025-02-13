import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta

# Crear un DataFrame con los datos
data = {
    'Actividad': ['Inicio', 'Preparación', 'Diagnóstico', 'Análisis', 'Requisitos', 'Diseño',
                  'Desarrollo M1', 'Desarrollo M2', 'Integración', 'Pruebas', 'Validación',
                  'Implementación', 'Final'],
    'ID Actividad': ['Inicio', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Final'],
    'Dependencia': ['', 'Inicio', 'A', 'A', 'B, C', 'D', 'E', 'E', 'F, G', 'H', 'I', 'J', 'K'],
    'Duración (días)': [0, 7, 5, 8, 3, 12, 15, 12, 6, 10, 4, 7, 0]
}

df = pd.DataFrame(data)

# Función para calcular las fechas de inicio basado en dependencias
def calcular_fechas(df):
    df['Fecha Inicio'] = pd.NaT
    df['Fecha Fin'] = pd.NaT
    df.loc[df['Actividad'] == 'Inicio', 'Fecha Inicio'] = pd.Timestamp.today()

    for i, row in df.iterrows():
        if pd.isna(row['Fecha Inicio']):
            dependencias = row['Dependencia'].split(', ')
            fechas_fin = df[df['ID Actividad'].isin(dependencias)]['Fecha Fin']
            fecha_inicio = max(fechas_fin) if not fechas_fin.empty else pd.Timestamp.today()
            df.at[i, 'Fecha Inicio'] = fecha_inicio

        df.at[i, 'Fecha Fin'] = df.at[i, 'Fecha Inicio'] + timedelta(days=row['Duración (días)'])
    
    return df

# Calcular fechas
df = calcular_fechas(df)

# Organizar actividades de forma descendente
df = df.sort_values(by='Fecha Inicio', ascending=False)

# Crear el diagrama de Gantt
fig, ax = plt.subplots(figsize=(10, 6))

# Colores para las barras
colors = plt.cm.Dark2(range(len(df)))

# Dibujar barras para cada actividad en orden descendente
for i, row in df.iterrows():
    ax.barh(row['Actividad'], row['Duración (días)'], left=row['Fecha Inicio'], color=colors[i])

# Configuraciones del gráfico
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.xticks(rotation=45)
plt.ylabel('Actividades')
plt.xlabel('Fechas')
plt.title('Diagrama de Gantt')
plt.grid(True)

plt.tight_layout()
plt.show()
