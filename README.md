# AI-Powered Code Security Scanner

## **Overview**
The **AI-Powered Security Assessment Tool** is an automated security scanning and evaluation system designed to **analyze, classify, and assess** software projects. It leverages **structured data extraction**, **automated security scans**, and **AI-driven analysis** to provide a **comprehensive security overview**.

This tool systematically:
1. **Collects project files** using `os.walk()`, categorizing file types and generating structured JSON reports.
2. **Executes security scans** (Semgrep, Bandit, Trivy, Checkov, etc.), parsing results for AI evaluation.
3. **Uses AI to analyze findings**, grouping related security issues, explaining risks, and suggesting fixes.
4. **Tracks security posture over time**, comparing past and current assessments to measure improvements.

## **Features**
✅ **Automated file discovery** (`os.walk()`) with structured JSON output  
✅ **Project structure analysis** (`README.md`, `settings.py`, `views.py`, database presence)  
✅ **Execution of multiple security scans** (Semgrep, Bandit, Trivy, Checkov, OWASP ZAP, JSLint)  
✅ **AI-driven security evaluation**, grouping issues and providing actionable fixes  
✅ **False positive likelihood estimation** for better accuracy  
✅ **Automated document size management**, ensuring AI can process large reports efficiently  
✅ **Security posture tracking**, comparing past and current assessments  
✅ **User-friendly CLI execution** for seamless analysis  

## **Workflow**
1. **File Collection & JSON Generation**  
   - Uses `os.walk()` to gather project files, categorize file types, and generate JSON reports.  

2. **Project Structure Analysis**  
   - Identifies key files (`README.md`, `settings.py`, `views.py`, database presence) to understand project architecture.  

3. **Security Scanning & AI Evaluation**  
   - Runs multiple security scans (Semgrep, Bandit, Trivy, Checkov, OWASP ZAP, JSLint).  
   - AI **groups related issues**, explains risks, suggests fixes, and estimates false positive likelihood.  

4. **Report Compilation & Summary Generation**  
   - Aggregates AI feedback with structured reports to create a **final security assessment**.  
   - Splits large documents if needed for AI processing.  

5. **Security Posture Tracking**  
   - Stores and compares past security scans against new ones to measure improvements.  

## **Next Steps 🚀**
🔹 Expand **static analysis coverage** with additional security scans  
🔹 Automate **AI-driven security assessments** within CI/CD pipelines  
🔹 Improve **report parsing** for better AI processing  
🔹 Enhance **security posture tracking** for long-term monitoring  


## Installation
Install Ollama from https://ollama.com/

Clone this repository:
```bash
git clone https://github.com/kidd1492/project_security_scanner.git
```
```bash
cd project_security_scanner
```

Set up the virtual environment:
```bash
python -m venv venv
```
```bash
pip install -r requirements.txt
``` 

### Run the program:

Analyze files in a specific directory:
```bash
python scr/main.py Path/to/ProjectDirectory 
```

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
