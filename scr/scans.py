import subprocess, os
from log_handler import app_logger, project_logger


def bandit(directory):
    print(f"Scanning: {directory}")

    # Make sure the path is properly formatted for Windows

    command = f"bandit -r {directory} -x {directory}\\venv,migrations,tests -f json -o reports/bandit_scan.json"
    subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
    return 0
   

def run_semgrep_scan(directory, reports_dir):
    # Ensure the reports directory exist
    os.makedirs(reports_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(reports_dir, "semgrep_results.json")

    # Run Semgrep safely
    command = [
        "semgrep", "scan", directory,  # Correct way to specify the scan target
        "--config=auto",
        "--output", output_file,
        "--json"
        
    ]

    subprocess.run(command, check=True)
    project_logger.info(f"semgrep_scan data successfully written to {output_file}")
    print(f"Scan completed! Results saved to {output_file}")
