import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."

    # Avoidance of common passwords
    common_passwords = ["password", "123456", "qwerty", "abc123", "admin"]
    if password.lower() in common_passwords:
        return "Weak: Avoid common passwords."

    return "Strong: Password meets the criteria."

def main():
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)

if __name__ == "__main__":
    main()
