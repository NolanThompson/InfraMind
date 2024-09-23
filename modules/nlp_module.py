from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def identify_missing_params(terraform_request):
    """
    Asks the LLM to identify which parameters are missing from the user's request 
    before generating any Terraform code.
    """
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an intelligent assistant that identifies missing parameters for Terraform resources."},
        {
            "role": "user",
            "content": f"""
            The user wants to create infrastructure with Terraform. 
            Based on this request: "{terraform_request}", please identify any required parameters that are missing.
            Do not generate Terraform code at this stage. Only list the required parameters that need user input to complete the request.
            """
        }
    ],
    max_tokens=150,
    temperature=0.5)
    
    missing_params = response.choices[0].message.content.strip()
    return missing_params

def prompt_for_missing_params(missing_params):
    """
    Prompt the user for any missing parameters identified by the LLM.
    """
    print(f"The following parameters are missing from your request: {missing_params}")
    user_inputs = {}
    
    for param in missing_params.split(","):
        value = input(f"Please provide a value for {param.strip()}: ")
        user_inputs[param.strip()] = value
    
    return user_inputs

def generate_terraform_code_with_inputs(terraform_request, user_inputs):
    """
    Generate Terraform code by combining the original request and user-provided inputs for missing parameters.
    """
    # Convert user inputs into a format the model can use
    input_str = ", ".join([f"{key}: {value}" for key, value in user_inputs.items()])
    
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a Terraform code generator."},
        {
            "role": "user",
            "content": f"""
            Generate Terraform code for the following request: {terraform_request}.
            Here are the missing parameters provided by the user: {input_str}.
            Do not include provider or region unless explicitly specified.
            """
        }
    ],
    max_tokens=200,
    temperature=0.5)
    
    terraform_code = response.choices[0].message.content.strip()
    return terraform_code

