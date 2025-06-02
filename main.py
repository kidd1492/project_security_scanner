from base_analyzer import generate_json
from ollama_test import start_ollama
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

'''function to walk through a directory pick what kinds of file it wants
ignoring directories like venv, .git, it then saves the type of file and a list of
files for that type into a dict. returns catagorized files'''
def gather_categorized_files(directory):
    allowed_extensions = [".py", ".html", ".js", ".md", ".txt", ".db" ".css"]  # Update to add more file types
    ignored_directories = [".git", "env", "venv"]
    categorized_files = {}

    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignored_directories]  # Skip ignored directories
            for file in files:
                # Check if the file's extension is in the allowed list
                if any(file.endswith(ext) for ext in allowed_extensions):
                    ext = file.split('.')[-1]  # Extract the file extension (without dot)

                    # Initialize the list for this file type if not already present
                    if ext not in categorized_files:
                        categorized_files[ext] = []
                    # Append the file path to the appropriate list
                    categorized_files[ext].append(os.path.abspath(os.path.join(root, file)))
    except Exception as e:
        logging.error(f"An error occurred while gathering files: {e}")

    return categorized_files


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        print("Please enter a directory path.")
        sys.exit(1)

    elif len(args) == 2:

        directory_name = os.path.normpath(args[1])
        if not os.path.exists(directory_name):
            logging.error(f"The specified directory does not exist: {directory_name}")
            sys.exit(1)

        categorized_files = gather_categorized_files(directory_name)
        project_data = generate_json(categorized_files)
        start_ollama(project_data)
    else:
        print("Invalid number of arguments. Please provide exactly one directory path.")
        sys.exit(1)