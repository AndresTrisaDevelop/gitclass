import pandas as pd

# Definir las zonas horarias y sus diferencias respecto a UTC
timezones = {
    "UTC": 0,
    "PST": -8,
    "MST": -7,
    "CST": -6,
    "EST": -5,
    "CET": 1,
    "IST": 5.5,
    "JST": 9,
    "AEST": 10
}

# Crear la matriz de tiempos relativos
timezone_names = list(timezones.keys())
num_timezones = len(timezone_names)
time_diff_matrix = [[0] * num_timezones for _ in range(num_timezones)]

for i in range(num_timezones):
    for j in range(num_timezones):
        time_diff_matrix[i][j] = timezones[timezone_names[j]] - timezones[timezone_names[i]]

# Crear un DataFrame para visualizar la matriz
df = pd.DataFrame(time_diff_matrix, index=timezone_names, columns=timezone_names)

df
