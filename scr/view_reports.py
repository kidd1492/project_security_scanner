import helper
import main_menu
import os


def reports(opption, directory_name):
    project_name = f"project_{directory_name.split("\\" or "/")[-1]}"
    
    if opption == "1":
        security_report = os.path.join("scr", "projects", f"{project_name}", "reports", "security_summary.txt")
        security_print = helper.read_file_content(security_report)
        print(security_print)

        #TODO fix this if not '' then while True:
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            main_menu.create_menu("reports")

    if opption == "2":
        overview_report = os.path.join("scr", "projects", f"{project_name}", "reports", "overview.txt")
        overview_print = helper.read_file_content(overview_report)
        print(f"{overview_print}\n\n")
        close = input("Press Enter key to close: ")
        if close == "":
            helper.clear_screen()
            main_menu.create_menu("reports")