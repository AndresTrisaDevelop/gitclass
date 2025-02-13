import pandas as pd
import difflib

#  "vendor_name"
# que contiene los nombres de los proveedores con inconsistencias

# se puede cambiar por el proceso de importar excel file
#obtener la columna

df = pd.DataFrame({
    'vendor_name': ['Proveedor A', 'Proveedor B', 'Proveedor c', 'Proveedor D', 'Proveedor e']
})

# Función para encontrar la cadena más similar en una lista de cadenas
def find_similar_string(target, strings):
    similarity_threshold = 0.9  # Umbral de similitud, aqui solo puse 90% como ejemplo
    best_match = None
    max_similarity = 0
    
    for string in strings:
        similarity = difflib.SequenceMatcher(None, target, string).ratio()
        if similarity > similarity_threshold and similarity > max_similarity:
            max_similarity = similarity
            best_match = string
    
    return best_match

# Obtener los valores únicos de la columna "vendor_name"
unique_vendor_names = df['vendor_name'].unique()

# aqui creo un diccionario para almacenar las correspondencias de reemplazo
replacement_mapping = {}

# aqui comparo valores unicos y similitudes
for i, name1 in enumerate(unique_vendor_names):
    for j, name2 in enumerate(unique_vendor_names):
        if i != j and name1 not in replacement_mapping and name2 not in replacement_mapping:
            similarity = difflib.SequenceMatcher(None, name1, name2).ratio()
            if similarity > similarity_threshold:
                replacement_mapping[name2] = name1

# aqui espero almacenar los valores en la columna "vendor_name" según el mapeo generado
# Ayudame integrarlo con el otro codigo que miramos de separar por pestaña en excel
df['vendor_name'] = df['vendor_name'].map(lambda x: replacement_mapping.get(x, x))

print(df)
