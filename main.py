from terraform_ai_tool.user_input import get_user_input
from terraform_ai_tool.nlp_module import convert_instruction_to_terraform
from terraform_ai_tool.change_summary import summarize_changes
from terraform_ai_tool.confirmation import get_user_confirmation
from terraform_ai_tool.terraform_execute import apply_terraform_changes

def main():
    # Step 1: Get user input
    instruction = get_user_input()

    # Step 2: Convert instruction to Terraform code
    terraform_code = convert_instruction_to_terraform(instruction)

    # Step 3: Summarize the changes for the user
    summary = summarize_changes(terraform_code)
    print(summary)

    # Step 4: Get user confirmation
    if get_user_confirmation():
        print("Applying changes...")
        apply_terraform_changes(terraform_code)
    else:
        print("Changes aborted. You can modify your instructions and try again.")

if __name__ == "__main__":
    main()

