import subprocess

def bandit(directory):
    print(f"Scanning: {directory}")

    # Make sure the path is properly formatted for Windows

    command = f"bandit -r {directory} -x {directory}\\venv,migrations,tests -f json -o reports/output.json"
    subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
    return 0
   

#TODO function for OWASP ZAP

