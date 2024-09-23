import openai

def summarize_changes(terraform_code):
    """
    Summarizes the Terraform code in plain English using OpenAI's API.
    """
    # Ask the OpenAI model to generate a plain English summary of the Terraform code
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following Terraform code in plain English:\n\n{terraform_code}",
        max_tokens=150,
        temperature=0.5
    )
    summary = response.choices[0].text.strip()

    # Combine both Terraform code and summary in the final output
    combined_summary = f"The following Terraform code will be applied:\n\n{terraform_code}\n\n"
    combined_summary += f"Summary of changes:\n{summary}\n"
    return combined_summary

