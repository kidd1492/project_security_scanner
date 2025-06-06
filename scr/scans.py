import subprocess
import os

def bandit(directory):
    print(f"Scanning: {directory}")

    # Make sure the path is properly formatted for Windows

    command = f"bandit -r {directory} -x {directory}\\venv,migrations,tests -f json -o reports/bandit_scan.json"
    subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
    return 0
   

#TODO function for semgrep
def run_semgrep_scan(directory):
    # Ensure the reports directory exists
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(reports_dir, "scans/semgrep_results.json")

    # Run Semgrep safely
    command = [
        "semgrep", "scan", directory,  # Correct way to specify the scan target
        "--config=auto",
        "--output", output_file,
        "--json"
        
    ]

    subprocess.run(command, check=True)

    print(f"Scan completed! Results saved to {output_file}")
