from get_project_data import generate_project_json
import helper, scans
import ollama_test
import sys, time
import logging


menu_opptions = {
"update": ["1. Scans", "2. Reports", "3. EXIT"],
"scans": ["1. Run Security_scan", "2. Generate Overview Report", "3. MAIN MENU", "4. EXIT"],
"reports": ["1. View Security Report", "2. View Overview Report", "3. BACK","4. EXIT"]
}

directory_name = ""


def start():
    global directory_name
    helper.clear_screen()
    print("#" *42)
    print("Welcome to the Project Scanning Tool")
    print("#" *42, "\n\n")

    directory_name = helper.get_directory()
   
    '''TODO check log to see if file has been scanned '''
    exist = helper.check_log(directory_name)
    if exist ==  True:
         helper.clear_screen()
         create_menu("update")
    else:
        logging.info(directory_name)
        helper.clear_screen()
        create_menu("scans")
    

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



def reports(opption):
    if opption == "1":
        security_print = helper.read_file_content("scr\\reports\\security_summary.txt")
        print(security_print)
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            create_menu("reports")
    if opption == "2":
        overview_print = helper.read_file_content("scr\\reports\\overview.txt")
        print(f"{overview_print}\n\n")
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            create_menu("reports")


if __name__ == "__main__":
    start()
