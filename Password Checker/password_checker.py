# Import necessary modules
import os  # For handling file paths
import re  # For regular expressions

# Load common passwords from a file
def load_common_passwords():
    try:
        # Get the directory of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "common_passwords.txt")

        # Open the file and read each line into a set
        with open(file_path, "r") as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty set
        print("Error: 'common_passwords.txt' file not found.")
        return set()

# Check if a password is common
def is_common_password(password, common_passwords):
    return password.lower() in common_passwords

# Check password strength based on defined rules
def check_password_strength(password):
    feedback = []

    # Rule 1: Minimum length
    if len(password) < 12:
        feedback.append("❌ Too short: Use at least 12 characters.")

    # Rule 2: Uppercase letter
    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Missing uppercase letter.")

    # Rule 3: Lowercase letter
    if not re.search(r"[a-z]", password):
        feedback.append("❌ Missing lowercase letter.")

    # Rule 4: Number
    if not re.search(r"[0-9]", password):
        feedback.append("❌ Missing number.")

    # Rule 5: Special character
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        feedback.append("❌ Missing special character.")

    return feedback

# Example usage
if __name__ == "__main__":
    # Load the common passwords
    common_passwords = load_common_passwords()

    # Prompt the user for a password to check
    password_to_check = input("🔐 Enter a password to check: ")

    # Check if the password is common
    if is_common_password(password_to_check, common_passwords):
        print("\n❌ The password is too common. Please choose a more unique password.")
    else:
        # Check strength and print feedback
        strength_feedback = check_password_strength(password_to_check)

        if not strength_feedback:
            print("\n✅ Strong password!")
        else:
            print("\nPassword Strength Feedback:")
            for item in strength_feedback:
                print(item)
