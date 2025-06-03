import re
import json
import logging

# Define comment patterns
pattern_dict = {
    "python_comment": r"^\s*(\"{3}.*?\"|\'{3}.*?\')|^#",
    "html_comment": r"<!--(.*?)-->",
    "doctype_pattern": r"<!DOCTYPE\s+\w+>",
    "js_comment": r"^\s*(//.*|/\*.*\*/)"
}

def read_file_content(file_path):
    """ Reads full content of a given file """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None
        

def project_report(categorized_files):
    """ Collects project file metadata and full content of README & requirements.txt """
    file_count = 0
    file_types = []
    all_files = []
    readme_content = None
    requirements_content = None

    for file_type, file_list in categorized_files.items():
        file_types.append(file_type)
        file_count += len(file_list)

        for file in file_list:
            all_files.append(file)
            if "readme.md" in file.lower():
                readme_content = read_file_content(file)  # Capture full README content
            if "requirements.txt" in file.lower():
                requirements_content = read_file_content(file)  # Capture full dependencies info

    return file_count, file_types, all_files, readme_content, requirements_content


def extract_file_data(all_files):
    """ Extracts comments from each file """
    extracted_data = []

    for file in all_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()

                    # Check for matching patterns
                    for pattern_name, pattern in pattern_dict.items():
                        if re.match(pattern, line):
                            extracted_data.append(line)
        
        except Exception as e:
            logging.error(f"Error processing {file}: {e}")

    return extracted_data

def generate_json(categorized_files, output_file="reports/project_data.json"):
    """ Compiles all project data and writes to a JSON file """
    file_count, file_types, all_files, readme_content, requirements_content = project_report(categorized_files)

    extracted_data = extract_file_data(all_files)

    project_data = {
        "file_count": file_count,
        "file_types": file_types,
        "files": all_files,
        "readme_content": readme_content,  # Full README content
        "requirements_content": requirements_content,  # Full dependencies content
        "comments": extracted_data
    }

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(project_data, json_file, indent=4)

    return project_data