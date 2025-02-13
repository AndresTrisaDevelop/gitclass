import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        global selected_files
        selected_files = list(files)  # Guardar la lista de archivos seleccionados
        file_listbox.delete(0, tk.END)  # Limpiar la lista actual
        for file in files:
            file_listbox.insert(tk.END, file)  # Añadir archivos a la lista

def save_file():
    if not selected_files:
        messagebox.showwarning("Advertencia", "No se han seleccionado archivos PDF")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        merge_pdfs(selected_files, output_path)  # Pasar la lista de archivos directamente
        messagebox.showinfo("Éxito", f"Se ha creado el archivo PDF: {output_path}")

app = tk.Tk()
app.title("Fusionar PDFs")

selected_files = []

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Selected files:")
label.pack()

file_listbox = tk.Listbox(frame, width=50, height=10)
file_listbox.pack()

button_select = tk.Button(frame, text="Select as many pdf's you want", command=select_files)
button_select.pack(pady=5)

button_merge = tk.Button(frame, text="Save merged file", command=save_file)
button_merge.pack(pady=5)

app.mainloop()
