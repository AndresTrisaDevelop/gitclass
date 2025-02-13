import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from fuzzywuzzy import process
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut

# Diccionario de estados y abreviaciones
states = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming"
}

# Configura tu API Key de Google Maps aquí
API_KEY = 'AIzaSyCey2zGPKPuPZd6amEipkjGfayq3nDQ97A'
geolocator = GoogleV3(api_key=API_KEY)

# Función para normalizar y estandarizar direcciones
def preprocess_address(address):
    address = address.strip().upper()  # Convertir a mayúsculas y eliminar espacios innecesarios
    address = re.sub(r'\s+', ' ', address)  # Reemplazar múltiples espacios por uno solo
    address = re.sub(r'[\.,]', '', address)  # Eliminar puntos y comas
    address = re.sub(r'\bST\b', 'STREET', address)  # Expandir abreviaciones comunes
    address = re.sub(r'\bAVE\b', 'AVENUE', address)
    # Añadir otras abreviaciones si es necesario
    return address

# Función para encontrar el código del estado más cercano usando el nombre del estado
def find_closest_state(state_name):
    state_names = list(states.values())
    closest_match, score = process.extractOne(state_name, state_names)
    if score >= 80:  # Umbral de coincidencia, puedes ajustar
        return [code for code, name in states.items() if name == closest_match][0]
    return 'Unknown'

# Función para extraer y dividir la dirección usando expresiones regulares
def extract_address_parts(address):
    address = preprocess_address(address)
    address_1 = ''
    state = ''
    zip_code = ''
    
    # Regex para extraer la parte de la dirección, el estado y el código postal
    address_match = re.search(r'(.+?)\s+(\w{2})\s+(\d{5}(?:-\d{4})?)$', address)
    if address_match:
        address_1 = address_match.group(1).strip()
        state_code = address_match.group(2).strip()  # Obtener el código del estado
        
        # Verificar si el código del estado es válido
        if state_code in states:
            state = state_code
        else:
            # Buscar el estado más cercano si el código no es válido
            state_name = address_match.group(2).strip()
            state = find_closest_state(state_name)
        zip_code = address_match.group(3).strip()
    else:
        state = 'Unknown'
    
    country = 'US'  # Asumimos que es EE.UU. Puedes ajustar si es necesario
    
    return address_1, state, country, zip_code

# Función para obtener coordenadas usando la API de Google Maps
def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_coordinates(address)  # Reintentar si se produce un timeout

# Función para cargar y procesar el archivo CSV
def process_csv():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select CSV File"
    )
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        if 'Ship To Address' not in df.columns:
            messagebox.showerror("Error", "El archivo CSV debe contener una columna 'Ship To Address'.")
            return
        
        # Extraer partes de la dirección
        df[['address_1', 'state', 'country', 'zip_code']] = df['Ship To Address'].apply(
            lambda addr: pd.Series(extract_address_parts(addr))
        )

        # Obtener coordenadas
        df[['latitude', 'longitude']] = df['Ship To Address'].apply(
            lambda addr: pd.Series(get_coordinates(addr))
        )

        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save CSV File"
        )
        if output_file_path:
            df.to_csv(output_file_path, index=False)
            messagebox.showinfo("Success", f"Archivo CSV procesado y guardado como: {output_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error al procesar el archivo: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("CSV Address Processor")
root.geometry("300x200")

# Crear y colocar el botón para cargar y procesar el archivo
process_button = tk.Button(root, text="Cargar y Procesar CSV", command=process_csv)
process_button.pack(pady=50)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
