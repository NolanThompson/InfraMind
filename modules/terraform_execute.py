import os

def apply_terraform_changes(terraform_code):
    """
    Applies the generated Terraform code.
    """
    # Write the terraform_code to a file
    with open("generated_infra.tf", "w") as file:
        file.write(terraform_code)
    
    # Initialize and apply Terraform changes
    os.system("terraform init")
    os.system("terraform apply -auto-approve generated_infra.tf")

