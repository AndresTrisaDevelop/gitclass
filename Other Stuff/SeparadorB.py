import tkinter as tk
from tkinter import filedialog
import pandas as pd



def process_excel():
    filepath = filedialog.askopenfilename(title="Selecciona el archivo Excel", filetypes=(("Archivos de Excel", "*.xlsx"), ("Todos los archivos", "*.*")))
    if filepath:
        df = pd.read_excel(filepath)

        df['vendor_name'] = df['vendor_name'].fillna('NAMELESS')
        df['vendor_name'] = df['vendor_name'].str.upper()
        df['vendor_name'] = df['vendor_name'].str.replace('[^\w\s]', '', regex=True)
        df['vendor_name'] = df['vendor_name'].str.replace('/', '_')
        df['vendor_name'] = df['vendor_name'].str.strip()

        df = df.sort_values(by=['vendor_name'], ignore_index=True)
        dfVendor = pd.DataFrame(df['vendor_name'])
        dfVendor = dfVendor.drop_duplicates()

        save_filepath = filedialog.asksaveasfilename(title="Guardar archivo Excel", defaultextension=".xlsx", filetypes=(("Archivos de Excel", "*.xlsx"), ("Todos los archivos", "*.*")))
        if save_filepath:
            with pd.ExcelWriter(save_filepath) as writer:
                for index, row in dfVendor.iterrows():
                    df.query("vendor_name==@row['vendor_name']").to_excel(writer, sheet_name=row['vendor_name'][0:30], index=False)

root = tk.Tk()
root.title("Procesamiento de Excel")

btn_process = tk.Button(root, text="Procesar Archivo Excel", command=process_excel)
btn_process.pack(pady=20)

root.mainloop()
