import logging
from log_handler import app_logger, project_logger
from docutils.core import publish_doctree
import os
import json


def read_file_content(file_path):
    """Reads full content of a given file with error handling."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content
    except Exception as e:
        app_logger.error(f"Error reading {file_path}: {e}")
        return None
    

# Read the .rst file
def get_rst_text(file):
    with open(file, "r", encoding="utf-8") as rst_file:
        rst_content = rst_file.read()

    # Parse the rst content
    doctree = publish_doctree(rst_content)

    # Extract only relevant text
    text_list = [node.astext() for node in doctree.traverse() if node.tagname == "paragraph"]
    return text_list 


#function to clear the terminal screen for menus
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  
        os.system('clear')


def gather_categorized_files(directory, output_file):
    allowed_extensions = [".py", ".html", ".js", ".md", ".txt", ".db", ".css", ".rst", ".yml"]  # Add more as needed
    ignored_directories = [".git", "env", "venv"]
    categorized_files = {}
    total_files = 0
    file_count = 0
    file_types = {}

    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignored_directories]  # Skip ignored directories
            for file in files:
                total_files += 1
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    ext = file.split('.')[-1]  # Extract the file extension (without dot)
                    
                    categorized_files.setdefault(ext, []).append(os.path.abspath(os.path.join(root, file)))


        for file_type, file_list in categorized_files.items():
            file_types[file_type] = len(file_list)
            file_count += len(file_list)
        # Create output directory if it doesn't exist
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write categorized files directly to JSON
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(categorized_files, json_file, indent=4)

        project_logger.info(f"Categorized files successfully written to {output_file}")
    
    except Exception as e:
        app_logger.error(f"An error occurred while gathering files: {e}")

    return total_files, file_types, file_count  # Return the path of the saved JSON file


'''function to parse json semgrep scan to make it easier for ai to process'''
def parse_semgrep_scan(file_path, reports_dir):
    output_file = os.path.join(reports_dir, "semgrep_ai_data.json")
    try:
        # Load the JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extract information from each result
        results = []
        for result in data.get('results', []):
            check_id = result['check_id']
            path = result['path']
            metadata = result.get('extra', {}).get('metadata', {})
            owasp = metadata.get('owasp')
            message = result.get('extra', {}).get('message')

            # Create a dictionary with the extracted information
            issue_info = {
                'check_id': check_id,
                'path': path,
                'owasp': owasp,
                'message': message
            }
            results.append(issue_info)
         # Save the results to a JSON file
        with open(output_file, 'w') as out:
            json.dump(results, out, indent=4)
        project_logger.info(f"semgrep_ai_ data successfully written to {output_file}")
        return results

    except FileNotFoundError:
        app_logger.error(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        app_logger.error("Error: The file is not a valid JSON file.")
        return []
