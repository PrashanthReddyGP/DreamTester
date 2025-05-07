import os
import re
import subprocess

def convert_ui_to_py(ui_file, output_file):
    # Check if the .ui file exists in the current directory
    if not os.path.exists(ui_file):
        print(f"Error: {ui_file} does not exist.")
        return
    
    try:
        # Convert .ui file to .py using pyside6-uic
        subprocess.run(['pyside6-uic', ui_file, '-o', output_file], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error converting .ui to .py: {e}")
    except FileNotFoundError:
        print("pyside6-uic command not found. Make sure PySide6 is installed.")

def fix_alignment_flag(file_path):
    # Check if the .py file exists before trying to modify it
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to replace occurrences of 'Qt.AlignmentFlag.Qt.AlignmentFlag' with 'Qt'
    fixed_content = re.sub(r'Qt\.AlignmentFlag\.Qt\.AlignmentFlag', 'Qt', content)

    # Save the updated content back to the .py file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)

# Define the file paths for the .ui and .py files
current_directory = os.getcwd()  # Get the current working directory
utils_folder = os.path.join(current_directory, 'utils')
ui_file_path = os.path.join(utils_folder, 'form.ui')  # form.ui should be in the same folder
output_file_path = os.path.join(utils_folder, 'app_ui.py')  # Output will be saved as app_ui.py in the same folder

# Convert the .ui file to a .py file
convert_ui_to_py(ui_file_path, output_file_path)

# Fix alignment flag in the generated .py file
fix_alignment_flag(output_file_path)
