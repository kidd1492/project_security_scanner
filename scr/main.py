from get_project_data import generate_project_json
import helper, scans
from ollama_test import start_ollama
import os, time
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        print("Please enter a directory path.")
        sys.exit(1)

    elif len(args) == 2:

        directory_name = os.path.normpath(args[1])
        if not os.path.exists(directory_name):
            logging.error(f"The specified directory does not exist: {directory_name}")
            sys.exit(1)

        total_files, file_types, file_count = helper.gather_categorized_files(directory_name)
        #TODO better function name!
        generate_project_json(total_files, file_types, file_count)
        scans.run_semgrep_scan(directory_name)
        scan_data = helper.parse_semgrep_scan("scr/reports/scans/semgrep_results.json")
        #scans.bandit(directory_name)
        time.sleep(10)
        start_ollama(scan_data)
    else:
        print("Invalid number of arguments. Please provide exactly one directory path.")
        sys.exit(1)