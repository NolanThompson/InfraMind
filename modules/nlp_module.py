import openai
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_instruction_to_terraform(instruction):
    """
    Converts natural language instructions to Terraform code using OpenAI's API.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following instruction to Terraform code: {instruction}",
        max_tokens=150,
        temperature=0.7
    )
    terraform_code = response.choices[0].text.strip()
    return terraform_code

