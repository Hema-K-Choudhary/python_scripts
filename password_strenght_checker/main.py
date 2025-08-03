import re
import getpass

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) < 8:
        remarks.append("Too short (min 8 characters).")
    else:
        strength += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add digits.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add special characters (!@#$%^&* etc).")

    # Strength level
    if strength == 5:
        level = "Very Strong"
    elif strength == 4:
        level = "Strong"
    elif strength == 3:
        level = "Moderate"
    else:
        level = "Weak"

    return level, remarks

if __name__ == "__main__":
    # getpass to hide password on input screen
    pwd = getpass.getpass("Enter your password: ")
    level, feedback = check_password_strength(pwd)
    print(f"\nPassword Strength: {level}")
    if feedback:
        print("Suggestions:")
        for msg in feedback:
            print(f"- {msg}")
