import ollama
import subprocess, json
import time

def start_ollama(project_data):
    """Start the Ollama server and ensure the AI model is ready."""
    try:
        print("Checking for available models...")
        pull_model()
        print("Starting Ollama Server...")
        subprocess.Popen(['start', 'cmd', '/c', 'ollama serve'], shell=True)
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
    prompt = """from the following data write me a detailed report that first identifies what kind of project it is. then what kind of stack. then it should have a summary section that has a 2 paragraph explanati
    on of what the project is for and what it does. and last it should include a list of recommended scans for security such as owasp or bandit or tool that goes with the project type. just a list ofthe names."""
    json_file_path = "reports/output.json"
    try:
        with open(json_file_path, "r") as file:
            bandit_data = json.load(file)
            
    except Exception as e:
        print(f"Error loading JSON file: {e}")
 
    question = f"{prompt} {project_data} {bandit_data}"
    print(question)

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open("reports\\overview.txt", "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        return response["message"]["content"]
    except Exception as e:
        print(f"An error occurred while getting the AI response: {e}")
        return ""
