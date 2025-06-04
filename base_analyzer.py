import os
import json
import logging
import helper

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def project_report():
    """Collects project file metadata and extracts filenames instead of full paths."""

    # Flags for project classification
    models_py = False
    views_py = False
    urls_py = False
    docker_used = False
    docker_compose_used = False
    database_type = None
    readme_content = []
    requirements_content = []

    json_file = "reports/categorized_files.json"
    with open(json_file, "r", encoding="utf-8") as file:
        categorized_files = json.load(file)  # Load JSON data
        for file_type, file_list in categorized_files.items():

            for file in file_list:
                file_lower = file.lower()
                if ".db" in file_lower:
                    database_type = ".db"      
                if "models.py" in file_lower:
                    models_py = True
                if "views.py" in file_lower:
                    views_py = True
                if "urls.py" in file_lower:
                    urls_py = True
                if "dockerfile" in file_lower:
                    docker_used = True
                if "docker-compose.yml" in file_lower:
                    docker_compose_used = True
                if "settings.py" in file_lower:  # Check for database in Django settings
                    settings_content = helper.read_file_content(file)
                    if settings_content:
                        if "postgresql" in settings_content.lower():
                            database_type = "PostgreSQL"
                        elif "mysql" in settings_content.lower():
                            database_type = "MySQL"
                        elif "sqlite" in settings_content.lower():
                            database_type = "SQLite"

                if "readme" in file_lower:
                    if ".rst" not in file_lower:
                        md_content = helper.read_file_content(file)  # Capture full README content
                        if md_content:
                            readme_content.append(md_content)
                    else:       
                        content = helper.get_rst_text(file)
                        if content:
                            readme_content.append(content)
                        
                if "requirements" in file_lower:
                    requirements_content = helper.read_file_content(file)  # Capture full dependencies info

    return (models_py, views_py, urls_py, 
     docker_used, docker_compose_used, database_type, 
     readme_content, requirements_content)


def generate_json(total_files, file_types, file_count, output_file="reports/project_data.json"):
    """Compiles all project data and writes to a JSON file."""
    logging.info("Generating project report...")
    
    (models_py, views_py, urls_py, 
     docker_used, docker_compose_used, database_type, 
     readme_content, requirements_content) = project_report()

    project_data = {
        "total_files": total_files,
        "file_count": file_count,
        "file_types": file_types,
        "readme_content": readme_content,  # Full README content
        "requirements_content": requirements_content,  # Full dependencies content
        "models_py": models_py,
        "views_py": views_py,
        "urls_py": urls_py,
        "docker_used": docker_used,
        "docker_compose_used": docker_compose_used,
        "database_type": database_type
    }

    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(project_data, json_file, indent=4)
        logging.info(f"Project data successfully written to {output_file}")
    except Exception as e:
        logging.error(f"Error writing project data to {output_file}: {e}")

    return project_data