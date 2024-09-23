def get_user_confirmation():
    """
    Ask the user to confirm or modify the suggested changes.
    """
    user_input = input("Are you happy with the changes? (yes/no) ")
    if user_input.lower() == "yes":
        return True
    else:
        return False

