import tkinter as tk
from tkinter import filedialog, messagebox
from lxml import etree
import webbrowser
import os

def load_file():
    """Open a file dialog to load an XML file."""
    file_path = filedialog.askopenfilename(
        title="Select an XML file", filetypes=[("XML Files", "*.xml")]
    )
    return file_path

def get_xml_structure(file_path):
    """Parse the XML file and extract its structure as a dictionary with line numbers."""
    try:
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_path, parser)
        root = tree.getroot()

        def parse_element(element):
            structure = {}
            for child in element:
                line_number = child.sourceline
                structure[child.tag] = {
                    "line": line_number,
                    "children": parse_element(child)
                }
            return structure

        return {root.tag: {"line": root.sourceline, "children": parse_element(root)}}
    except Exception as e:
        messagebox.showerror("Error", f"Error parsing XML file: {e}")
        return None

def compare_structures(structure1, structure2, path="Root"):
    """Compare two XML structures at the tag level and return detailed discrepancies."""
    discrepancies = []

    def compare_dicts(dict1, dict2, path):
        keys1 = set(dict1.keys())
        keys2 = set(dict2.keys())

        for key in keys1 - keys2:
            discrepancies.append((path, key, f"Tag '{key}' in {path} (line {dict1[key]['line']}) is missing in file 2."))
        for key in keys2 - keys1:
            discrepancies.append((path, key, f"Tag '{key}' in {path} (line {dict2[key]['line']}) is missing in file 1."))

        for key in keys1 & keys2:
            compare_dicts(dict1[key]["children"], dict2[key]["children"], f"{path}/{key}")

    compare_dicts(structure1, structure2, path)
    return discrepancies

def generate_html_report(structure1, structure2, discrepancies):
    """Generate an HTML report comparing the structures of two XML files."""
    html_content = """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>XML Comparison Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
        th { background-color: #f4f4f4; }
        .missing { background-color: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>XML Comparison Report</h1>
    <h2>Structures</h2>
    <table>
        <thead>
            <tr>
                <th>File 1 Structure</th>
                <th>File 2 Structure</th>
            </tr>
        </thead>
        <tbody>
"""

    def generate_structure_rows(struct1, struct2, depth=0):
        nonlocal html_content
        all_keys = set(struct1.keys()).union(set(struct2.keys()))
        for key in all_keys:
            line1 = struct1[key]['line'] if key in struct1 else ""
            line2 = struct2[key]['line'] if key in struct2 else ""

            class1 = "missing" if key not in struct2 else ""
            class2 = "missing" if key not in struct1 else ""

            html_content += f"<tr><td class='{class1}'>{'&nbsp;' * depth * 4}{key} (line {line1})</td>"
            html_content += f"<td class='{class2}'>{'&nbsp;' * depth * 4}{key} (line {line2})</td></tr>"

            if key in struct1 and key in struct2:
                generate_structure_rows(struct1[key]['children'], struct2[key]['children'], depth + 1)

    generate_structure_rows(structure1, structure2)

    html_content += """        </tbody>
    </table>

    <h2>Discrepancies</h2>
    <table>
        <thead>
            <tr>
                <th>Path</th>
                <th>Tag</th>
                <th>Issue</th>
            </tr>
        </thead>
        <tbody>
"""

    for path, tag, issue in discrepancies:
        html_content += f"<tr><td>{path}</td><td>{tag}</td><td>{issue}</td></tr>"

    html_content += """        </tbody>
    </table>
</body>
</html>"""

    return html_content

def compare_files():
    """Handle the comparison of two selected XML files."""
    file1 = load_file()
    if not file1:
        return
    file2 = load_file()
    if not file2:
        return

    structure1 = get_xml_structure(file1)
    structure2 = get_xml_structure(file2)

    if structure1 and structure2:
        discrepancies = compare_structures(structure1, structure2)

        html_report = generate_html_report(structure1, structure2, discrepancies)
        report_path = os.path.abspath("comparison_report.html")
        with open(report_path, "w") as report_file:
            report_file.write(html_report)

        webbrowser.open(report_path)

def main():
    """Set up the GUI for the XML comparison tool."""
    root = tk.Tk()
    root.title("XML Structure Comparator")
    root.geometry("400x200")

    tk.Label(
        root, text="XML Structure Comparator", font=("Helvetica", 16)
    ).pack(pady=10)

    tk.Button(
        root, text="Compare XML Files", command=compare_files, font=("Helvetica", 12), bg="lightblue"
    ).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
