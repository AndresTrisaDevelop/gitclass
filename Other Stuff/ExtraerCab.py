import tkinter as tk
from tkinter import filedialog
from pyunpack import Archive

def extract_cab():
    cab_file_path = filedialog.askopenfilename(title="Seleccionar archivo .cab", filetypes=[("Archivos CAB", "*.cab")])
    if cab_file_path:
        extract_dir = filedialog.askdirectory(title="Seleccionar directorio de extracción")
        if extract_dir:
            try:
                Archive(cab_file_path).extractall(extract_dir)
                print("Extracción completada.")
            except Exception as e:
                print(f"Error al extraer el archivo .cab: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Extracción de archivo .cab")

# Botón para iniciar la extracción
extract_button = tk.Button(root, text="Extraer archivo .cab", command=extract_cab)
extract_button.pack(pady=10)

# Ejecutar el bucle de eventos
root.mainloop()
