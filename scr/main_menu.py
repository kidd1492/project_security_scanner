from get_project_data import generate_project_json
from log_handler import app_logger, project_logger
import helper, scans, new_project
import ollama_test
import sys, time, os

'''TODO make a function to check scans and reports directory
loop through and create a menu with those scans '''

menu_opptions = {
"update": ["1. Scans", "2. Reports", "3. EXIT"],
"scans": ["1. Run Security_scan", "2. Generate Overview Report", "3. MAIN MENU", "4. EXIT"],
"reports": ["1. View Security Report", "2. View Overview Report", "3. BACK","4. EXIT"]
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
        for opption in menu:
            print(opption)
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
            reports(menu_selection)
    
    if title.lower() == "update":
        if menu_selection == "1":
            helper.clear_screen()
            create_menu("scans")
        else:
            helper.clear_screen()
            create_menu("reports")
    
    if title.lower() == "scans":
        if menu_selection in menu[-2]:
            helper.clear_screen()
            create_menu("update")
        else:
            helper.clear_screen()
            scan(menu_selection)
    

def scan(opption):
    global directory_name

    project_name = f"project_{directory_name.split("\\" or "/")[-1]}"
    reports_output = os.path.join("scr", "projects", f"{project_name}", "reports")
    scans_output = os.path.join("scr", "projects", f"{project_name}", "scans")

    if opption == "1":
        scans.run_semgrep_scan(directory_name, scans_output)
        scan_data = helper.parse_semgrep_scan(f"scr/projects/{project_name}/scans/semgrep_results.json", scans_output)
        #scans.bandit(directory_name)
        time.sleep(10)
        ollama_test.start_ollama()
        ollama_test.security_scan_response(scan_data, reports_output)

    elif opption == "2":
        project_data_path = os.path.join("scr", "projects", f"{project_name}", "scans", "project_data.json")
        project_data = helper.read_file_content(project_data_path)
        time.sleep(10)
        ollama_test.start_ollama()
        ollama_test.overview_scan_response(project_data, reports_output)


def reports(opption):
    project_name = f"project_{directory_name.split("\\" or "/")[-1]}"
    
    if opption == "1":
        security_report = os.path.join("scr", "projects", f"{project_name}", "reports", "security_summary.txt")
        security_print = helper.read_file_content(security_report)
        print(security_print)

        #TODO fix this if not '' then while True:
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            create_menu("reports")
    if opption == "2":
        overview_report = os.path.join("scr", "projects", f"{project_name}", "reports", "overview.txt")
        overview_print = helper.read_file_content(overview_report)
        print(f"{overview_print}\n\n")
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            create_menu("reports")
