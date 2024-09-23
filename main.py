from modules.nlp_module import identify_missing_params, prompt_for_missing_params, generate_terraform_code_with_inputs

def main():
    # Get the user's initial Terraform request
    terraform_request = input("Please describe the infrastructure changes you want to make: ")
    
    # Step 1: Identify missing parameters
    missing_params = identify_missing_params(terraform_request)
    
    # Step 2: Prompt the user for any missing parameters
    if missing_params:
        user_inputs = prompt_for_missing_params(missing_params)
    else:
        user_inputs = {}
    
    # Step 3: Generate Terraform code with the provided inputs
    terraform_code = generate_terraform_code_with_inputs(terraform_request, user_inputs)
    
    # Output the generated Terraform code
    print("\nGenerated Terraform Code:\n")
    print(terraform_code)

if __name__ == "__main__":
    main()

