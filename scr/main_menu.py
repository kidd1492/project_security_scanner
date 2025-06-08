from get_project_data import generate_project_json
import helper, scans
import ollama_test
import os, time
import logging


menu_opptions = {
"update": ["1. Scans", "2. reports"],
"scans": ["1. Security_scan", "2. Overview Report"],
"reports": ["1. Security Report", "2. Overview Report"]
}

directory_name = ""


def start():
    global directory_name
    print("#" *42)
    print("Welcome to the Project Scanning Tool")
    print("#" *42, "\n\n")

    directory_name = helper.get_directory()
   
    # log to check. check log
    if directory_name ==  "C:\\Users\\chris\\Desktop\\notes_app":
         helper.clear_screen()
         create_menu("scans")
    else:
        logging.info(directory_name)
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
        logging.error(f"No menu names {title}")

    print("\n")
    menu_selection = input("Enter Number for Opption: ")
    
    if title.lower() == "scans":
        scan(menu_selection)
    else:print(title)
    


def scan(opption):
    global directory_name
    if opption == "1":
        total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
        generate_project_json(total_files, file_types, file_count)
        scans.run_semgrep_scan(directory_name)
        scan_data = helper.parse_semgrep_scan("scr/reports/scans/semgrep_results.json")
        #scans.bandit(directory_name)
        time.sleep(10)
        ollama_test.start_ollama()
        ollama_test.security_scan_response(scan_data)

    elif opption == "2":
        total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
        project_data = generate_project_json(total_files, file_types, file_count)
        time.sleep(10)
        ollama_test.start_ollama()
        ollama_test.overview_scan_response(project_data)

if __name__ == "__main__":
    start()
