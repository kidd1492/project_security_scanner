import ollama
import subprocess
import time


def install_ollama(project_data):
    install = input("Whould you like to install Ollama: Y/n  ")
    if install.lower() == "y": 
        # Define the command to run Ollama with the specified model
        command = f"ai_model/OllamaSetup.exe"
        try:
            # Open a Command Prompt window and execute the command
            print("Waiting for Ollama Setup...")
            finish = subprocess.run(command, check=True)
            if finish:
                print("Starting Ollama Setup...")
                subprocess.Popen(f'start cmd /k ollama pull qwen2.5-coder:3b', shell=True)
                print("Finished Ollama Setup")
                get_ai_response(project_data)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        start_ollama(project_data)


def start_ollama(project_data):
    # Define the command to run Ollama with the specified model
    try:
        # Open a Command Prompt window and execute the command
        print("Waiting for Ollama Setup...")
        finish = subprocess.Popen(f'start cmd /k ollama serve', shell=True)
        if finish:
            print("Finished Ollama Setup")
            get_ai_response(project_data)
            #check_available_models()
    except Exception as e:
        print(f"An error occurred: {e}")


# Get AI response based on user input
def get_ai_response(project_data):
    prompt = """from the following data write me a detailed report that first identifies what kind of project it is. then what kind of stack. then it should have a summary section that has a 2 paragraph explanati
    on of what the project is for and what it does. and last it should include a list of recommended scans for security such as owasp or bandit or tool that goes with the project type. just a list ofthe names."""
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
