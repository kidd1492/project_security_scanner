import ollama
import subprocess, json
import time

def start_ollama(project_data):
    """Start the Ollama server and ensure the AI model is ready."""
    try:
        print("Checking for available models...")
        pull_model()
        print("Starting Ollama Server...")
        #TODO fix shell True
        subprocess.run(['start', 'cmd', '/c', 'ollama serve'], shell=True)
        print("Finished Ollama Setup.")
        get_ai_response(project_data)
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
def get_ai_response(project_data):
    prompt = """Evaluate the following semgrep_data. if the issue occurs more than 1 time group all of them together with a list of 
    files with that issue. for each type of issue give me the "file_name": file name or list, "issue": explain why it is an issue. 
    "fix": give a detailed fix for the issue. after evaluating the issues give a "final_summary": give a summary of your evaluation. semgrep_data:"""
    question = f"{prompt} {project_data}"

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open("scr\\reports\\overview.txt", "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        return response["message"]["content"]
    except Exception as e:
        print(f"An error occurred while getting the AI response: {e}")
        return ""
