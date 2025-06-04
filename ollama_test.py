import ollama
import subprocess, json
import time

def start_ollama(project_data):
    """Start the Ollama server and ensure the AI model is ready."""
    try:
        print("Checking for available models...")
        pull_model()
        print("Starting Ollama Server...")
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
    prompt = """Evaluate the following data to give me a responce in json format to determine: 1. project type: what type of project it is.
                2. stack: what kind of stack is uses. 3. summary: A summary section that has a 2 paragraph explanation of what the project is for and what it does.
                4. recomemded scans: it should include a list of recommended security scans that are avalible for the kind of project. 5.Comman Risk: give a list of 5 comman security issus for this type of project"""
    question = f"{prompt} {project_data}"

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
