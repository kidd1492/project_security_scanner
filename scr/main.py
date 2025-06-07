from main_menu import start
from get_project_data import generate_project_json
import helper, scans
from ollama_test import start_ollama
import os, time
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    start()
    #directory_name = helper.get_directory()
    #total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
    #generate_project_json(total_files, file_types, file_count)
    #scans.run_semgrep_scan(directory_name)
    #scan_data = helper.parse_semgrep_scan("scr/reports/scans/semgrep_results.json")
    #scans.bandit(directory_name)
    #time.sleep(10)
    #start_ollama(scan_data)

    

if __name__ == "__main__":
    main()


