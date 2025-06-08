import ollama
import subprocess
import test


def start_ollama():
    """Start the Ollama server and ensure the AI model is ready."""
    try:
        print("Checking for available models...")
        pull_model()
        print("Starting Ollama Server...")
        #TODO fix shell True
        subprocess.run(['start', 'cmd', '/c', 'ollama serve'], shell=True)
        print("Finished Ollama Setup.")
    except Exception as e:
        print(f"An error occurred while starting Ollama: {e}")


def pull_model():
    """Pull the required Ollama model."""
    try:
        subprocess.run(["ollama", "pull", "qwen2.5-coder:3b"], check=True)
        print("Successfully pulled 'qwen2.5-coder:3b'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pulling the model: {e}")


# Get AI response based on user input
def security_scan_response(project_data):
    prompt = """Evaluate the following semgrep_data. if the issue occurs more than 1 time group all of them together with a list of 
    files with that issue. for each type of issue give me the "file_name": file name or list, "issue": explain why it is an issue. 
    "fix": give a detailed fix for the issue. after evaluating the issues give a "final_summary": give a summary of your evaluation. semgrep_data:"""
    question = f"{prompt} {project_data}"

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open("scr\\reports\\security_summary.txt", "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        test.create_menu("reports")
    except Exception as e:
        print(f"An error occurred while getting the AI response: {e}")
        return ""
    

def overview_scan_response(project_data):
    prompt = """Evaluate the following project_data. Based on the data create a project summary report with-
     "summary": a 2 parahraph summary Detailing the project. "stack" Give a summary the stack used and what dependiancies there are.
    "other_info": any other relevant information you think would be helpfull for an overview. -if there is not enough information
    to give a good report give the information you can and 3 suggestions to """
    question = f"{prompt} {project_data}"

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open("scr\\reports\\overview.txt", "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        test.create_menu("reports")
    except Exception as e:
        print(f"An error occurred while getting the AI response: {e}")
        return ""
