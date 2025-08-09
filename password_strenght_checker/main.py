import re
import getpass

def check_password_strength(password):
    """Check password strength and return level with suggestions."""
    
    # Define checks with patterns and messages
    checks = [
        (len(password) >= 8, "Too short (min 8 characters)"),
        (re.search(r"[a-z]", password), "Add lowercase letters"),
        (re.search(r"[A-Z]", password), "Add uppercase letters"),
        (re.search(r"\d", password), "Add digits"),
        (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "Add special characters")
    ]
    
    # Calculate strength and collect suggestions
    strength = sum(1 for check, _ in checks if check)
    suggestions = [msg for check, msg in checks if not check]
    
    # Determine strength level
    levels = ["Weak", "Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    level = levels[strength]
    
    return level, suggestions

def main():
    """Main function to check password strength."""
    password = getpass.getpass("Enter your password: ")
    level, suggestions = check_password_strength(password)
    
    print(f"\nPassword Strength: {level}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()