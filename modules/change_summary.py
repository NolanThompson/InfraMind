from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_changes(terraform_code):
    """
    Summarizes the Terraform code in plain English using GPT-4 from OpenAI's API.
    """
    # Ask GPT-4 to generate a plain English summary of the Terraform code
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a Terraform code summarizer."},
        {"role": "user", "content": f"Summarize the following Terraform code in plain English:\n\n{terraform_code}"}
    ],
    max_tokens=150,
    temperature=0.5)
    
    # Extract the summary from the response
    summary = response.choices[0].message.content.strip()

    # Combine both Terraform code and summary in the final output
    combined_summary = f"The following Terraform code will be applied:\n\n{terraform_code}\n\n"
    combined_summary += f"Summary of changes:\n{summary}\n"
    return combined_summary

