# Import necessary modules
import os  # Import the os module
import re  # Import the regular expression module

# Load common passwords from a file
def load_common_passwords():
    try:
        # Open the file and read each line into a set
        with open("common_passwords.txt", "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty set
        print("Error: 'common_passwords.txt' file not found.")
        return set()

# Check if a password is common
def is_common_password(password, common_passwords):
    return password in common_passwords

# Example usage
if __name__ == "__main__":
    # Load the common passwords
    common_passwords = load_common_passwords()

    # Prompt the user for a password to check
    password_to_check = input("Enter a password to check: ")
    # Check if the password is common
    if is_common_password(password_to_check, common_passwords):
        print("The password is too common. Please choose a stronger password.")
    else:
        print("The password is not common. Good choice!")
