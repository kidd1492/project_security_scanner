import os
from log_handler import app_logger, project_logger
import helper
from get_project_data import generate_project_json
import main_menu, scans

def get_directory():
    while True:
        directory = input("Enter Project Directory Path: ")
        directory_name = os.path.normpath(directory)
        if not os.path.exists(directory_name):
            continue
        else:
            return directory_name


def check_log(directory):
    with open("scr/logs/project.log", "r", encoding="utf-8") as report:
        for line in report:
            if directory in line:
                return True  # Return True if found
        
        project_logger.info(directory)  # Log only if not found in any line
        new_project(directory)
        return False  # Return False only after checking all lines


def new_project(directory):
    #unique name for project directory Define project path
    project_id = directory.split("\\" or "/")[-1]
    project_path = os.path.join("scr", "projects", f"project_{project_id}")
    
    # Create project directories
    os.makedirs(project_path, exist_ok=True)
    app_logger.info(f"New Project Created: ID={project_id}, Directory={directory}")
    os.makedirs(os.path.join(project_path, "scans"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "reports"), exist_ok=True)

    gather_poject_info(directory, project_path)


def gather_poject_info(directory, project_path):
    categorized_files = os.path.join(project_path, "scans", "categorized_files.json")
    project_data = os.path.join(project_path, "scans", "project_data.json")
    total_files, file_types, file_count = helper.gather_categorized_files(directory, categorized_files)
    generate_project_json(total_files, file_types, file_count, project_data, categorized_files )
    scans_dir = os.path.join(project_path, "scans")
    scans.run_semgrep_scan(directory, scans_dir)

    helper.parse_semgrep_scan(f"{scans_dir}/semgrep_results.json", scans_dir)
    helper.clear_screen()
    main_menu.create_menu("scans")
    