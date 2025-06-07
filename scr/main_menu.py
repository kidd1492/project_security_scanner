from get_project_data import generate_project_json
import helper, scans
import ollama_test
import os, time
import sys

def menu_title():
    print("#" *42)
    print("Welcome to the Project Scanning Tool Menu")
    print("#" *42, "\n\n")


def start():
    menu_title()
    first = input("Welcome, Is this a New Project (Y/n):")
    if first.lower() == "y":
        helper.clear_screen()
        scan_menu()    
    else:
        print("no")


def scan_menu():
    scan_opptions = ["1. Security_scan", "2. Overview Report"]
    menu_title()
    for opption in scan_opptions:
        print(opption)
    scan = input(f"\nPlease, Select Number opption: ")
    if scan == "1":
        directory_name = helper.get_directory()
        total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
        generate_project_json(total_files, file_types, file_count)
        scans.run_semgrep_scan(directory_name)
        scan_data = helper.parse_semgrep_scan("scr/reports/scans/semgrep_results.json")
        #scans.bandit(directory_name)
        time.sleep(10)
        ollama_test.start_ollama()
        ollama_test.security_scan_response(scan_data)

    elif scan == "2":
        directory_name = helper.get_directory()
        total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
        project_data = generate_project_json(total_files, file_types, file_count)
        time.sleep(10)
        ollama_test.start_ollama()

