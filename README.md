
# **InfraMind**

**InfraMind** is a Python tool that leverages AI to automate the generation of Terraform code from plain English descriptions. The tool translates natural language inputs into Terraform code, summarizes the proposed changes, and applies them after user confirmation, streamlining cloud infrastructure management.

## **Features**
- Convert plain English instructions into Terraform infrastructure code using OpenAI's API.
- Generate a human-readable summary of the proposed infrastructure changes.
- Prompt the user to review and confirm before making changes.
- Modular structure for easy extension and customization.

## **Prerequisites**
- [Terraform](https://www.terraform.io/downloads) installed locally.
- Python 3.x
- OpenAI API key for accessing GPT models.

## **Installation**

### 1. **Clone the repository**:
   ```bash
   git clone https://github.com/NolanThompson/InfraMind.git
   cd InfraMind
   ```

### 2. **Install Python dependencies**:
   Install the required dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Install Terraform**:
   You must have Terraform installed locally to apply the generated infrastructure changes.
   - macOS (using Homebrew): 
     ```bash
     brew install terraform
     ```
   - Linux (using APT):
     ```bash
     sudo apt-get install terraform
     ```
   - Windows: Download the Terraform binary from [Terraform Downloads](https://www.terraform.io/downloads).

### 4. **Set up the `.env` file**:
   In the root directory of the project, create a `.env` file to store your OpenAI API key.

   **Example `.env` file**:
   ```plaintext
   # OpenAI API Key
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## **Usage**

### 1. **Run the main script**:
   After setting up the environment, run the main script to start interacting with InfraMind:
   ```bash
   python main.py
   ```

### 2. **Follow the prompts**:
   - You will be prompted to describe the infrastructure you want to create in plain English.
     - Example: "Create an S3 bucket with versioning enabled."
   - The tool will then generate the Terraform code, summarize the changes, and display them for your review.

### 3. **Review and confirm**:
   - After reviewing the summary, you can either confirm the changes to apply the Terraform code or modify the description and try again.
   - No changes will be made until you confirm the summary.

## **Project Structure**

```plaintext
.
├── modules/                # Contains all the functional modules of the project
│   ├── __init__.py
│   ├── user_input.py       # Handles user input
│   ├── nlp_module.py       # Converts natural language to Terraform code via OpenAI API
│   ├── change_summary.py   # Summarizes the generated Terraform code in plain English
│   ├── confirmation.py     # Handles user confirmation before applying changes
│   └── terraform_execute.py# Executes the Terraform code if confirmed
├── .env                    # Contains API keys and cloud credentials (not committed to git)
├── .gitignore               # Ignores sensitive files and Terraform state
├── main.py                  # Main script to run the tool
├── requirements.txt         # List of Python dependencies
├── README.md                # This file
```
