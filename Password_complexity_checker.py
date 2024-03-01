import re

MIN_LENGTH = 8

def has_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def has_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def has_digit(password):
    return bool(re.search(r'\d', password))

def has_special_char(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_password_strength(password):
    criteria_checks = [
        len(password) >= MIN_LENGTH,
        has_lowercase(password),
        has_uppercase(password),
        has_digit(password),
        has_special_char(password),
    ]

    return sum(criteria_checks)

def provide_feedback(strength):
    if strength == 5:
        print("Password is very strong.")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    else:
        print("Password is weak. Consider the following:")
        if strength == 0:
            print("- Password is too short.")
        if strength <= 1:
            print("- Include a mix of uppercase and lowercase letters.")
        if strength <= 2:
            print("- Add at least one digit.")
        if strength <= 3:
            print("- Include at least one special character.")

def get_user_input():
    return input("Enter your password: ")

def main():
    password = get_user_input()
    strength = check_password_strength(password)
    provide_feedback(strength)

if __name__ == "__main__":
    main()
    