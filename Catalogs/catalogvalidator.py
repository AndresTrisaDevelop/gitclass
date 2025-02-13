import tkinter as tk
from tkinter import filedialog, messagebox
from lxml import etree

# Function to open a file dialog and allow the user to select an XML file
def load_file():
    """Open a file dialog to load an XML file."""
    file_path = filedialog.askopenfilename(
        title="Select an XML file", filetypes=[("XML Files", "*.xml")]
    )
    return file_path

# Function to parse the XML file and extract its structure as a nested dictionary
def get_xml_structure(file_path):
    """Parse the XML file and extract its structure as a dictionary with line numbers."""
    try:
        # Create an XML parser that removes blank text nodes
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_path, parser)  # Parse the XML file
        root = tree.getroot()  # Get the root element of the XML

        # Recursively parse each XML element and build a nested dictionary
        def parse_element(element):
            structure = {}
            for child in element:
                line_number = child.sourceline  # Get the line number of the child element
                structure[child.tag] = {
                    "line": line_number,  # Store the line number
                    "children": parse_element(child)  # Recursively parse child elements
                }
            return structure

        # Return the structure of the root element
        return {root.tag: {"line": root.sourceline, "children": parse_element(root)}}
    except Exception as e:
        # Show an error message if parsing fails
        messagebox.showerror("Error", f"Error parsing XML file: {e}")
        return None

# Function to compare the structures of two XML files and identify discrepancies
def compare_structures(structure1, structure2, path="Root"):
    """Compare two XML structures at the tag level and return detailed discrepancies."""
    discrepancies = []

    # Helper function to compare two dictionaries representing XML structures
    def compare_dicts(dict1, dict2, path):
        keys1 = set(dict1.keys())  # Get all keys (tags) from the first structure
        keys2 = set(dict2.keys())  # Get all keys (tags) from the second structure

        # Identify tags that are present in dict1 but missing in dict2
        for key in keys1 - keys2:
            discrepancies.append(f"Tag '{key}' in {path} (line {dict1[key]['line']}) is missing in file 2.")
        
        # Identify tags that are present in dict2 but missing in dict1
        for key in keys2 - keys1:
            discrepancies.append(f"Tag '{key}' in {path} (line {dict2[key]['line']}) is missing in file 1.")

        # Compare common tags recursively
        for key in keys1 & keys2:
            compare_dicts(dict1[key]["children"], dict2[key]["children"], f"{path}/{key}")

    # Start comparison from the root path
    compare_dicts(structure1, structure2, path)
    return discrepancies

# Function to handle the comparison of two selected XML files
def compare_files():
    """Handle the comparison of two selected XML files."""
    file1 = load_file()  # Load the first XML file
    if not file1:
        return  # Exit if no file is selected

    file2 = load_file()  # Load the second XML file
    if not file2:
        return  # Exit if no file is selected

    # Parse the structures of both XML files
    structure1 = get_xml_structure(file1)
    structure2 = get_xml_structure(file2)

    if structure1 and structure2:
        # Compare the structures and get discrepancies
        discrepancies = compare_structures(structure1, structure2)

        # Create a new window to display the comparison results
        result_window = tk.Toplevel()
        result_window.title("Comparison Results")
        result_window.geometry("800x600")

        # Create a text widget to display the results
        result_text = tk.Text(result_window, wrap=tk.WORD)
        result_text.pack(fill=tk.BOTH, expand=True)

        # Display discrepancies or a success message if the structures match
        if discrepancies:
            result_text.insert(tk.END, "Discrepancies found:\n\n")
            for line in discrepancies:
                result_text.insert(tk.END, line + "\n")
        else:
            result_text.insert(tk.END, "The structures of the two XML files match perfectly.")

# Main function to set up the GUI for the XML comparison tool
def main():
    """Set up the GUI for the XML comparison tool."""
    root = tk.Tk()  # Create the main window
    root.title("XML Structure Comparator")  # Set the title of the window
    root.geometry("400x200")  # Set the window size

    # Add a label for the application title
    tk.Label(
        root, text="XML Structure Comparator", font=("Helvetica", 16)
    ).pack(pady=10)

    # Add a button to start the comparison process
    tk.Button(
        root, text="Compare XML Files", command=compare_files, font=("Helvetica", 12), bg="lightblue"
    ).pack(pady=20)

    # Start the Tkinter main loop
    root.mainloop()

# Entry point of the program
if __name__ == "__main__":
    main()
