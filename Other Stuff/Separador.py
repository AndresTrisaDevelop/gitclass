import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from tkinter import ttk
from threading import Thread

def cargar_archivo():
    global df
    archivo = filedialog.askopenfilename(title="Selecciona un archivo Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    if archivo:
        df = pd.read_excel(archivo)
        messagebox.showinfo("Carga completa", "El archivo se ha cargado correctamente.")
        return df

def procesar_y_guardar():
    global df
    if df is None:
        messagebox.showerror("Error", "Primero debes cargar un archivo.")
        return

    try:
        nuevo_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")], title="Guardar archivo")
        if nuevo_archivo:
            with pd.ExcelWriter(nuevo_archivo, engine='xlsxwriter') as writer:
                for vendor, data in df.groupby('vendor_name'):
                    data.to_excel(writer, sheet_name=vendor, index=False)
            messagebox.showinfo("Éxito", "Proceso completado. Se ha creado el archivo: {}".format(nuevo_archivo))
            barra_progreso.stop()  # Detener la barra de progreso al finalizar
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error durante el procesamiento del archivo: {str(e)}")

def procesar_con_progreso():
    barra_progreso.start()
    thread = Thread(target=procesar_y_guardar)
    thread.start()

# Crear ventana principal
root = tk.Tk()
root.title("Procesador de archivos Excel")

# Variables globales
df = None
progreso = tk.DoubleVar()

# Etiqueta
etiqueta = tk.Label(root, text="Bienvenido al Procesador de Archivos Excel", font=("Arial", 14))
etiqueta.pack(pady=10)

# Botón para cargar archivo
btn_cargar = tk.Button(root, text="Cargar Archivo Excel", command=lambda: cargar_archivo(), padx=10, pady=5, bg="blue", fg="white", font=("Arial", 12))
btn_cargar.pack(pady=10)

# Botón para procesar archivo con barra de progreso
btn_procesar = tk.Button(root, text="Procesar Archivo", command=procesar_con_progreso, padx=10, pady=5, bg="green", fg="white", font=("Arial", 12))
btn_procesar.pack(pady=10)

# Barra de progreso
barra_progreso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=progreso)
barra_progreso.pack(pady=10)

# Ejecutar el bucle principal de la interfaz de usuario
root.mainloop()
