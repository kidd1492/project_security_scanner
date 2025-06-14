from new_project import gather_poject_info
from log_handler import app_logger
import helper, new_project
import ollama_test, reports
import sys, os, time


menu_opptions = {
"update": ["1. Scans", "2. Reports", "3. Update Project Data", "4. Register New Project", "5. EXIT"],
"scans": ["1. Run Security_scan", "2. Generate Overview Report", "3. MAIN MENU", "4. EXIT"],
}

directory_name = ""


def start_program():
    global directory_name
    helper.clear_screen()
    print("#" *42)
    print("Welcome to the Project Scanning Tool")
    print("#" *42, "\n\n")

    directory_name = new_project.get_directory()
    exist = new_project.check_log(directory_name)
    if exist ==  True:
         helper.clear_screen()
         create_menu("update")


def create_menu(title):
    print("#" *42)
    print(title)
    print("#" *42, "\n\n")

    menu = menu_opptions.get(title)
    if menu:
        for option in menu:
            print(option)
    else:
        app_logger.error(f"No menu names {title}")

    print("\n")
    menu_selection = input("Enter Number for Opption: ")
    if menu_selection in menu[-1]:
        sys.exit()

    if title == "reports":
        if menu_selection in menu[-2]:
            helper.clear_screen()
            create_menu("scans")
        else:
            reports.list_available_files(directory_name)
    
    if title.lower() == "update":
        if menu_selection == "1":
            helper.clear_screen()
            create_menu("scans")
        elif menu_selection == "2":
            helper.clear_screen()
            reports.list_available_files(directory_name)
        elif menu_selection == "3":
            update_project_data()
        elif menu_selection == "4":
            start_program()
    
    if title.lower() == "scans":
        if menu_selection in menu[-2]:
            helper.clear_screen()
            create_menu("update")
        else:
            helper.clear_screen()
            scan(menu_selection)
    

def update_project_data():
    global directory_name
    project_id = directory_name.split("\\" or "/")[-1]
    project_path = os.path.join("scr", "projects", f"project_{project_id}")
    gather_poject_info(directory_name, project_path)
    helper.clear_screen()
    

def scan(option):
    global directory_name

    project_name = f"project_{directory_name.split("\\" or "/")[-1]}"
    reports_output = os.path.join("scr", "projects", f"{project_name}", "reports")

    if option == "1":
        scan_data = helper.read_file_content(f"scr/projects/{project_name}/scans/semgrep_ai_data.json")
        #scans.bandit(directory_name)
        time.sleep(5)
        ollama_test.start_ollama()
        ollama_test.security_scan_response(scan_data, reports_output)

    elif option == "2":
        project_data_path = os.path.join("scr", "projects", f"{project_name}", "scans", "project_data.json")
        project_data = helper.read_file_content(project_data_path)
        time.sleep(5)
        ollama_test.start_ollama()
        ollama_test.overview_scan_response(project_data, reports_output)
 