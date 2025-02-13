# Importamos Tkinter para construir la calculadora
import tkinter as tk
from math import sin, cos, tan, sqrt, pi, e

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")

# Una entrada donde escribimos los números y operaciones
entrada = tk.Entry(ventana, width=20, font=("Arial", 20), borderwidth=5, relief="ridge")
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Función para agregar números o símbolos al cuadro de entrada
def agregar(valor):
    entrada.insert(tk.END, valor)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())  # eval convierte texto como "2+2" en un cálculo real
        entrada.delete(0, tk.END)  # Borra lo que está escrito
        entrada.insert(0, str(resultado))  # Muestra el resultado
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Crear botones para números, operaciones y funciones
botones = [
    "7", "8", "9", "/", "sin(", 
    "4", "5", "6", "*", "cos(",
    "1", "2", "3", "-", "tan(",
    "0", ".", "pi", "+", "sqrt(",
    "C", "=", "(", ")", "e"
]

# Agregamos los botones a la ventana
fila = 1
columna = 0
for boton in botones:
    if boton == "=":
        # Botón especial para calcular el resultado
        tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                  command=calcular).grid(row=fila, column=columna)
    elif boton == "C":
        # Botón para limpiar la entrada
        tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                  command=limpiar).grid(row=fila, column=columna)
    else:
        # Botones generales
        tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                  command=lambda b=boton: agregar(b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 4:  # Cambiamos de fila después de 5 botones
        columna = 0
        fila += 1

# Mostramos la ventana y esperamos interacción del usuario
ventana.mainloop()
