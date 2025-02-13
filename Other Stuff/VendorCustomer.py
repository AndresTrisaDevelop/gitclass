import pandas as pd
from fuzzywuzzy import process

# columna 'vendors' de nuestra base de datos
data = {
    'vendors': ['AIS', 'A I S', 'Ais', 'WorldERF3, LLC.', 'WorldERP LLC.', 'WorldERP, LLC.']
}
df = pd.DataFrame(data)

# Lista de valores de la columna vendors
unique_vendors = ['AIS', 'WorldERP LLC.', 'Vendor3']

def get_closest_match(vendor, choices, threshold=60):
    """
    Encuentra la mejor coincidencia para un vendor dado dentro de una lista de opciones.
    Si la mejor coincidencia tiene una puntuación inferior al umbral, devuelve el vendor original.
    """
    match, score = process.extractOne(vendor, choices)
    if score >= threshold:
        return match
    return vendor

# Homogeneizar los nombres de los vendors
df['homogenized_vendors'] = df['vendors'].apply(lambda x: get_closest_match(x, unique_vendors))

# Generar un archivo de Excel con la salida
output_file = 'homogenized_vendors.xlsx'
df.to_excel(output_file, index=False)

print(f"Archivo de Excel '{output_file}' generado con éxito.")
print(df)