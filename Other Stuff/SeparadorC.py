







import tkinter as tk
from tkinter import filedialog
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo

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
            with pd.ExcelWriter(save_filepath, engine='openpyxl') as writer:
                for index, row in dfVendor.iterrows():
                    sheet_name = row['vendor_name'][0:30]
                    table_name = row['vendor_name'][0:3]  # Tomar los primeros tres caracteres del nombre del proveedor
                    df_filtered = df.query("vendor_name==@row['vendor_name']")
                    df_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

                    # Dar formato de tabla a la hoja
                    wb = writer.book
                    ws = writer.sheets[sheet_name]
                    tab = Table(displayName=f"Table_{table_name}", ref=ws.dimensions)
                    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                           showLastColumn=False, showRowStripes=True, showColumnStripes=True)
                    tab.tableStyleInfo = style
                    ws.add_table(tab)

root = tk.Tk()
root.title("Procesamiento de Excel")

btn_process = tk.Button(root, text="Procesar Archivo Excel", command=process_excel)
btn_process.pack(pady=20)

root.mainloop()
