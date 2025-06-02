# AI-Powered Code Security Scanner

## Overview
**AI-Powered Code Security Scanner** is an advanced security-focused tool designed to **analyze, classify, and assess** software projects. It leverages **structured extraction** and a **custom Ollama AI model** to identify the **project type** (Flask, Django, Node.js, etc.), generate an **overview**, and recommend **security scans** tailored to the project's architecture.

Beyond just classification, this tool **executes security scans** using tools like **Bandit, OWASP ZAP, JSLint, and others**, refining a project's security posture. The final stage involves a **comprehensive AI-driven security review**, providing **detailed recommendations** for improving the project's safety—ensuring non-coders and AI-generated code users understand security flaws and how to fix them.

## Features
- ✅ **Project type classification** (Flask, Django, Node.js, etc.)
- ✅ **Structured data extraction** generating insightful **JSON reports**
- ✅ **AI-generated project summary** for better visibility
- ✅ **Intelligent security scan recommendations** based on project type
- ✅ **Execution of security scans** using tools like Bandit, OWASP, JSLint
- ✅ **AI-driven security evaluation** for actionable improvements
- ✅ **User-friendly CLI execution** for seamless analysis

## Next Steps 🚀
- 🔹 Execute the **recommended security scans** and **generate an overall report**
- 🔹 Leverage AI to **evaluate security findings**, suggest **improvements**, and explain **why and how** fixes should be implemented
- 🔹 Expand **language support** and security checks for broader usability
- 🔹 Automate AI-driven security assessments **within CI/CD pipelines**

## Installation
Clone this repository:
```bash
git clone https://github.com/kidd1492/project_security_scanner.git
```

Navigate to the project directory and set up the virtual environment:
```bash
cd project_security_scanner
pip install -r requirements.txt
```

### Run the program:
```bash
python main.py  # prompts for directory path input
```
Analyze files in a specific directory:
```bash
python main.py Path/to/ProjectDirectory  # Generates JSON report
```

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
