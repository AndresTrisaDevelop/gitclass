import pandas as pd
import re

# Lee el archivo Excel
df = pd.read_excel('Grid1.xlsx')

# Borra columnas vacias
# df.drop(columns=['acknowledgment_number', 'acknowledgment_total'], inplace=True)

# Asigna NAMELESS a vendor-name vacio
df['vendor_name'] = df['vendor_name'].fillna('NAMELESS')
# Convierte a mayusculas
df['vendor_name']  = df['vendor_name'].str.upper()
# Ignora caracteres especiales
df['vendor_name']  = df['vendor_name'].str.replace('. ', '')
df['vendor_name']  = df['vendor_name'].str.replace('.', '')
df['vendor_name']  = df['vendor_name'].str.replace(':', '')
df['vendor_name']  = df['vendor_name'].str.replace('•', '')
df['vendor_name']  = df['vendor_name'].str.replace('[', '')
df['vendor_name']  = df['vendor_name'].str.replace('`', '')
df['vendor_name']  = df['vendor_name'].str.replace(',,', '')
df['vendor_name']  = df['vendor_name'].str.replace('_', '')
df['vendor_name']  = df['vendor_name'].str.replace('+', '')
df['vendor_name']  = df['vendor_name'].str.replace('=', '')
df['vendor_name']  = df['vendor_name'].str.replace('*', '')
df['vendor_name']  = df['vendor_name'].str.replace('¡', '')
df['vendor_name']  = df['vendor_name'].str.replace('!-', '')
df['vendor_name']  = df['vendor_name'].str.replace('/', '_')
df['vendor_name'] = df['vendor_name'].str.strip()

# Ordenamos el dataset por 'countriesAndTerritories' & 'dateRep'
df = df.sort_values(by=['vendor_name'], ignore_index=True)

# Crea dfVendor
dfVendor = pd.DataFrame(df['vendor_name'])
# Elimina Duplicados
dfVendor = dfVendor.drop_duplicates()

# Crea libro Excel
with pd.ExcelWriter('datos_separados_por_proveedor.xlsx') as writer:
    for index, row in dfVendor.iterrows():
        df.query("vendor_name==@row['vendor_name']").to_excel(writer, sheet_name=row['vendor_name'][0:30], index=False)
        print(row['vendor_name']) 


