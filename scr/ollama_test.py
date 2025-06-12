import ollama
import subprocess
import os
from log_handler import app_logger, project_logger
from helper import clear_screen
import main_menu

def ollama_installed():
    """Check if Ollama is installed before proceeding."""
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        app_logger.error("Ollama is not installed or not found.")
        print("Ollama is not installed. Please install it before proceeding.")
        return False


def model_exists(model_name):
    """Check if the specified Ollama model is already available."""
    if not ollama_installed():
        return False
    
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        return model_name in result.stdout
    except subprocess.CalledProcessError as e:
        app_logger.error(f"Error checking model existence: {e}")
        return False


def pull_model():
    """Pull the required Ollama model if not already available."""
    model_name = "qwen2.5-coder:3b"
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"Successfully pulled '{model_name}'.")
    except subprocess.CalledProcessError as e:
        app_logger.error(f"An error occurred while pulling the model: {e}")


def start_ollama():
    """Start the Ollama server and ensure the AI model is ready."""
    try:
        print("Checking for available models...")
        pull_model()
        
        print("Starting Ollama Server...")
        subprocess.run(['start', 'cmd', '/c', 'ollama serve'], shell=True)
        print("Finished Ollama Setup.")
    except Exception as e:
        app_logger.error(f"An error occurred while starting Ollama: {e}")
        print("Please make sure Ollama is installed.")


def stop_ollama():
    """Stop the Ollama server after processing responses."""
    try:
        subprocess.run(["taskkill", "/F", "/IM", "ollama.exe"], check=True)
        subprocess.run(["taskkill", "/F", "/IM", "ollama app.exe"], check=True)
        
        print("Ollama server stopped.")
    except subprocess.CalledProcessError as e:
        app_logger.error(f"Error stopping Ollama: {e}")
        print("Failed to stop Ollama server.")


# Get AI response based on user input
def security_scan_response(project_data, output):
    output_file = os.path.join(output, "security_summary.txt")

    prompt = """Evaluate the following semgrep_data. if the issue occurs more than 1 time group all of them together with a list of 
    files with that issue. for each type of issue give me the "file_name": file name or list, "issue": explain why it is an issue. 
    "fix": give a detailed fix for the issue. after evaluating the issues give a "final_summary": give a summary of your evaluation. semgrep_data:"""
    question = f"{prompt} {project_data}"

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open(output_file, "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        stop_ollama()
        clear_screen()
        main_menu.create_menu("reports")
    except Exception as e:
        app_logger.error(f"An error occurred while getting the AI response: {e}")
        return ""
    

def overview_scan_response(project_data, output):
    output_file = os.path.join(output, "overview.txt")
    prompt = """Evaluate the following project_data. Based on the data create a project summary report with-
     "summary": a 2 parahraph summary Detailing the project. "stack" Give a summary the stack used and what dependiancies there are.
    "other_info": any other relevant information you think would be helpfull for an overview. -if there is not enough information
    to give a good report give the information you can and 3 suggestions to """
    question = f"{prompt} {project_data}"

    try:
        print("Waiting on response....")
        response = ollama.chat(model="qwen2.5-coder:3b", messages=[{"role": "user", "content": question}])
        with open(output_file, "w") as out:
            out.write(response["message"]["content"])
        print("reports saved")
        stop_ollama()
        clear_screen()
        main_menu.create_menu("reports")
    except Exception as e:
        app_logger.error(f"An error occurred while getting the AI response: {e}")
        return ""


'''TODO make another prompt for ai to do something'''
